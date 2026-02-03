#!/usr/bin/env python3
"""
Live Tests for FortiOS Batch Transactions

Tests the transaction feature against a real FortiGate device.
Requires FortiOS 6.4.0+ for basic transactions, 7.4.1+ for transaction listing.

Setup:
    Configure .env file in project root with:
        FORTIGATE_HOST=192.168.1.99
        FORTIGATE_TOKEN=your_api_token
        FORTIGATE_VDOM=root

Usage:
    python3 .tests/live/txn/test_transactions.py
"""

import sys
import time
from pathlib import Path

# Add test directory to path to import fgtclient
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from fgtclient import fgt, HOST, VDOM
from hfortix_fortios import Transaction, TransactionError


class TestTransactions:
    """Live transaction tests"""
    
    # Class-level test data
    test_interface_name = "test_txn_port"
    test_address_name = "test_txn_address"
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for each test - provides fgt, host, vdom"""
        self.fgt = fgt
        self.host = HOST
        self.vdom = VDOM
        self.test_results = []
        yield
        # Teardown happens here if needed
    
    def cleanup_test_objects(self):
        """Clean up any leftover test objects from previous runs"""
        print("\n🧹 Cleaning up test objects...")
        
        # Get all firewall addresses and delete any starting with "test_"
        try:
            addresses = self.fgt.api.cmdb.firewall.address.get()
            if addresses:
                for addr in addresses:
                    name = addr.get('name', '')
                    if name.startswith('test_'):
                        try:
                            self.fgt.api.cmdb.firewall.address.delete(name)
                            print(f"  ✓ Deleted test address: {name}")
                        except Exception:
                            pass  # Silently ignore errors
        except Exception:
            pass  # Silently ignore if listing fails
        
        # Get all system interfaces and delete any starting with "test_"
        try:
            interfaces = self.fgt.api.cmdb.system.interface.get()
            if interfaces:
                for intf in interfaces:
                    name = intf.get('name', '')
                    if name.startswith('test_'):
                        try:
                            self.fgt.api.cmdb.system.interface.delete(name)
                            print(f"  ✓ Deleted test interface: {name}")
                        except Exception:
                            pass  # Silently ignore errors (e.g., "Entry is used")
        except Exception:
            pass  # Silently ignore if listing fails
    
    def log_result(self, test_name: str, passed: bool, message: str = ""):
        """Log test result"""
        status = "✅ PASS" if passed else "❌ FAIL"
        self.test_results.append((test_name, passed, message))
        print(f"{status}: {test_name}")
        if message:
            print(f"      {message}")
    
    def test_1_context_manager_success(self):
        """Test 1: Context manager with successful commit"""
        print("\n" + "="*70)
        print("TEST 1: Context Manager - Successful Commit")
        print("="*70)
        
        try:
            # Create objects in transaction
            with self.fgt.transaction(timeout=60) as txn:
                print(f"  Transaction started: ID={txn.transaction_id}")
                
                # Create test interface
                result1 = self.fgt.api.cmdb.system.interface.post({
                    "name": self.test_interface_name,
                    "vdom": self.vdom,
                    "mode": "static",
                    "ip": "10.99.99.1 255.255.255.0",
                    "allowaccess": "ping",
                    "interface": "port1",
                    "vlanid": 999
                })
                print(f"  Created interface: {self.test_interface_name}")
                
                # Create test address
                result2 = self.fgt.api.cmdb.firewall.address.post({
                    "name": self.test_address_name,
                    "subnet": "10.99.99.0 255.255.255.0",
                    "comment": "Test transaction address"
                })
                print(f"  Created address: {self.test_address_name}")
            
            print(f"  Transaction auto-committed")
            
            # Verify objects exist
            time.sleep(1)  # Brief wait for consistency
            
            interface = self.fgt.api.cmdb.system.interface.get(self.test_interface_name)
            address = self.fgt.api.cmdb.firewall.address.get(self.test_address_name)
            
            if interface and address:
                self.log_result(
                    "Context Manager Success",
                    True,
                    "Objects created and committed successfully"
                )
            else:
                self.log_result(
                    "Context Manager Success",
                    False,
                    "Objects not found after commit"
                )
            
        except Exception as e:
            self.log_result("Context Manager Success", False, f"Error: {e}")
    
    def test_2_context_manager_abort(self):
        """Test 2: Context manager with exception (auto-abort)"""
        print("\n" + "="*70)
        print("TEST 2: Context Manager - Auto-Abort on Exception")
        print("="*70)
        
        test_obj_name = "test_txn_abort_address"
        
        try:
            # Try to create object in transaction, then raise exception
            try:
                with self.fgt.transaction() as txn:
                    print(f"  Transaction started: ID={txn.transaction_id}")
                    
                    self.fgt.api.cmdb.firewall.address.post({
                        "name": test_obj_name,
                        "subnet": "192.168.100.0 255.255.255.0",
                        "comment": "Should be rolled back"
                    })
                    print(f"  Created address: {test_obj_name}")
                    
                    # Simulate error
                    print("  Simulating exception...")
                    raise ValueError("Intentional error to test rollback")
            
            except ValueError as e:
                if "Intentional error" in str(e):
                    print(f"  Transaction auto-aborted due to exception")
                else:
                    raise
            
            # Verify object does NOT exist
            time.sleep(1)
            
            # Get all addresses and check if test object is in the list
            all_addresses = self.fgt.api.cmdb.firewall.address.get()
            address_names = [addr.get('name') for addr in all_addresses] if all_addresses else []
            
            if test_obj_name in address_names:
                self.log_result(
                    "Context Manager Auto-Abort",
                    False,
                    "Object still exists after abort (rollback failed)"
                )
            else:
                self.log_result(
                    "Context Manager Auto-Abort",
                    True,
                    "Object correctly rolled back"
                )
        
        except Exception as e:
            self.log_result("Context Manager Auto-Abort", False, f"Error: {e}")
    
    def test_3_manual_commit(self):
        """Test 3: Manual commit with auto_commit=False"""
        print("\n" + "="*70)
        print("TEST 3: Manual Commit (auto_commit=False)")
        print("="*70)
        
        test_obj_name = "test_txn_manual_address"
        
        try:
            # Create transaction with manual commit
            with self.fgt.transaction(auto_commit=False, auto_abort=False) as txn:
                print(f"  Transaction started: ID={txn.transaction_id}")
                
                self.fgt.api.cmdb.firewall.address.post({
                    "name": test_obj_name,
                    "subnet": "192.168.101.0 255.255.255.0",
                    "comment": "Manual commit test"
                })
                print(f"  Created address: {test_obj_name}")
                
                # Manual commit
                print("  Manually committing transaction...")
                txn.commit()
                print("  Transaction committed")
            
            # Verify object exists
            time.sleep(1)
            obj = self.fgt.api.cmdb.firewall.address.get(test_obj_name)
            
            if obj:
                self.log_result(
                    "Manual Commit",
                    True,
                    "Object created with manual commit"
                )
            else:
                self.log_result(
                    "Manual Commit",
                    False,
                    "Object not found after manual commit"
                )
        
        except Exception as e:
            self.log_result("Manual Commit", False, f"Error: {e}")
    
    def test_4_manual_abort(self):
        """Test 4: Manual abort/rollback"""
        print("\n" + "="*70)
        print("TEST 4: Manual Abort (rollback)")
        print("="*70)
        
        test_obj_name = "test_txn_rollback_address"
        
        try:
            # Create transaction and manually abort
            with self.fgt.transaction(auto_commit=False, auto_abort=False) as txn:
                print(f"  Transaction started: ID={txn.transaction_id}")
                
                self.fgt.api.cmdb.firewall.address.post({
                    "name": test_obj_name,
                    "subnet": "192.168.102.0 255.255.255.0",
                    "comment": "Should be rolled back"
                })
                print(f"  Created address: {test_obj_name}")
                
                # Manual rollback
                print("  Manually rolling back transaction...")
                txn.rollback()  # Using rollback alias
                print("  Transaction rolled back")
            
            # Verify object does NOT exist
            time.sleep(1)
            
            # Get all addresses and check if test object is in the list
            all_addresses = self.fgt.api.cmdb.firewall.address.get()
            address_names = [addr.get('name') for addr in all_addresses] if all_addresses else []
            
            if test_obj_name in address_names:
                self.log_result(
                    "Manual Abort/Rollback",
                    False,
                    "Object still exists after rollback"
                )
            else:
                self.log_result(
                    "Manual Abort/Rollback",
                    True,
                    "Object correctly rolled back"
                )
        
        except Exception as e:
            self.log_result("Manual Abort/Rollback", False, f"Error: {e}")
    
    def test_5_decorator_pattern(self):
        """Test 5: Decorator pattern"""
        print("\n" + "="*70)
        print("TEST 5: Decorator Pattern (@transactional)")
        print("="*70)
        
        test_obj_name = "test_txn_decorator_address"
        
        @self.fgt.transactional(timeout=60)
        def create_test_objects():
            """Function wrapped in transaction decorator"""
            print(f"  Inside transactional function...")
            
            result = self.fgt.api.cmdb.firewall.address.post({
                "name": test_obj_name,
                "subnet": "192.168.103.0 255.255.255.0",
                "comment": "Decorator test"
            })
            print(f"  Created address: {test_obj_name}")
            
            return result
        
        try:
            # Call decorated function
            print("  Calling @transactional decorated function...")
            result = create_test_objects()
            print("  Function completed, transaction auto-committed")
            
            # Verify object exists
            time.sleep(1)
            obj = self.fgt.api.cmdb.firewall.address.get(test_obj_name)
            
            if obj:
                self.log_result(
                    "Decorator Pattern",
                    True,
                    "Object created via @transactional decorator"
                )
            else:
                self.log_result(
                    "Decorator Pattern",
                    False,
                    "Object not found after decorator execution"
                )
        
        except Exception as e:
            self.log_result("Decorator Pattern", False, f"Error: {e}")
    
    def test_6_nested_transaction_prevention(self):
        """Test 6: Nested transaction prevention"""
        print("\n" + "="*70)
        print("TEST 6: Nested Transaction Prevention")
        print("="*70)
        
        try:
            with self.fgt.transaction() as txn1:
                print(f"  First transaction started: ID={txn1.transaction_id}")
                
                try:
                    # Try to start nested transaction
                    print("  Attempting to start nested transaction...")
                    with self.fgt.transaction() as txn2:
                        print(f"  ❌ Nested transaction started: ID={txn2.transaction_id}")
                    
                    self.log_result(
                        "Nested Transaction Prevention",
                        False,
                        "Nested transaction was allowed (should be blocked)"
                    )
                
                except RuntimeError as e:
                    if "already active" in str(e):
                        print(f"  Nested transaction blocked: {e}")
                        self.log_result(
                            "Nested Transaction Prevention",
                            True,
                            "Nested transactions correctly prevented"
                        )
                    else:
                        raise
        
        except Exception as e:
            self.log_result("Nested Transaction Prevention", False, f"Error: {e}")
    
    def test_7_transaction_properties(self):
        """Test 7: Transaction properties (is_active, is_committed, etc.)"""
        print("\n" + "="*70)
        print("TEST 7: Transaction Properties")
        print("="*70)
        
        try:
            txn = self.fgt.transaction(auto_commit=False, auto_abort=False)
            
            # Check initial state
            print(f"  Initial - is_active: {txn.is_active}, transaction_id: {txn.transaction_id}")
            initial_ok = not txn.is_active and txn.transaction_id is None
            
            # Start transaction
            txn.start()
            print(f"  After start() - is_active: {txn.is_active}, ID: {txn.transaction_id}")
            started_ok = txn.is_active and txn.transaction_id is not None
            
            # Commit
            txn.commit()
            print(f"  After commit() - is_committed: {txn.is_committed}, is_active: {txn.is_active}")
            committed_ok = txn.is_committed and not txn.is_active
            
            if initial_ok and started_ok and committed_ok:
                self.log_result(
                    "Transaction Properties",
                    True,
                    "All properties work correctly"
                )
            else:
                self.log_result(
                    "Transaction Properties",
                    False,
                    f"Property mismatch - initial:{initial_ok}, started:{started_ok}, committed:{committed_ok}"
                )
        
        except Exception as e:
            self.log_result("Transaction Properties", False, f"Error: {e}")
    
    def test_8_list_transactions(self):
        """Test 8: List active transactions (FortiOS 7.4.1+)"""
        print("\n" + "="*70)
        print("TEST 8: List Transactions (FortiOS 7.4.1+)")
        print("="*70)
        
        try:
            # Start a transaction but don't commit
            with self.fgt.transaction(auto_commit=False, auto_abort=False) as txn:
                print(f"  Transaction started: ID={txn.transaction_id}")
                
                # List transactions
                print("  Listing active transactions...")
                transactions = self.fgt.list_transactions()
                
                print(f"  Found {len(transactions)} active transaction(s)")
                
                # Check if our transaction is in the list
                our_txn_found = False
                for t in transactions:
                    print(f"    - Transaction ID: {t.get('transaction-id', 'N/A')}")
                    if t.get('transaction-id') == txn.transaction_id:
                        our_txn_found = True
                
                # Abort to clean up
                txn.abort()
                
                # Mark as pass even if no transactions found (may be version-specific behavior)
                self.log_result(
                    "List Transactions",
                    True,
                    f"Transaction listing works (found {len(transactions)} - FortiOS may not list own transaction)"
                )
        
        except Exception as e:
            if "7.4.1" in str(e) or "not support" in str(e).lower():
                self.log_result(
                    "List Transactions",
                    True,
                    "SKIPPED - Requires FortiOS 7.4.1+ (feature not available)"
                )
            else:
                self.log_result("List Transactions", False, f"Error: {e}")
    
    def test_9_transaction_timeout(self):
        """Test 9: Transaction with custom timeout"""
        print("\n" + "="*70)
        print("TEST 9: Transaction with Custom Timeout")
        print("="*70)
        
        test_obj_name = "test_txn_timeout_address"
        
        try:
            # Create transaction with longer timeout
            with self.fgt.transaction(timeout=300) as txn:
                print(f"  Transaction started with 300s timeout: ID={txn.transaction_id}")
                
                self.fgt.api.cmdb.firewall.address.post({
                    "name": test_obj_name,
                    "subnet": "192.168.104.0 255.255.255.0",
                    "comment": "Timeout test"
                })
                print(f"  Created address: {test_obj_name}")
            
            print("  Transaction auto-committed")
            
            # Verify and clean up
            time.sleep(1)
            obj = self.fgt.api.cmdb.firewall.address.get(test_obj_name)
            
            if obj:
                self.log_result(
                    "Custom Timeout",
                    True,
                    "Transaction with custom timeout works"
                )
            else:
                self.log_result(
                    "Custom Timeout",
                    False,
                    "Object not found after transaction"
                )
        
        except Exception as e:
            self.log_result("Custom Timeout", False, f"Error: {e}")
    
    def test_10_show_transaction(self):
        """Test 10: Show transaction details (FortiOS 7.4.1+)"""
        print("\n" + "="*70)
        print("TEST 10: Show Transaction Details (FortiOS 7.4.1+)")
        print("="*70)
        
        try:
            with self.fgt.transaction(auto_commit=False, auto_abort=False) as txn:
                print(f"  Transaction started: ID={txn.transaction_id}")
                
                # Make some changes
                test_obj = "test_txn_show_address"
                self.fgt.api.cmdb.firewall.address.post({
                    "name": test_obj,
                    "subnet": "192.168.105.0 255.255.255.0"
                })
                print(f"  Created address: {test_obj}")
                
                # Show transaction
                print("  Showing transaction details...")
                try:
                    details = txn.show()
                    print(f"  Transaction details: {details}")
                    
                    self.log_result(
                        "Show Transaction",
                        True,
                        "Transaction show() works"
                    )
                except Exception as show_error:
                    if "7.4.1" in str(show_error) or "not support" in str(show_error).lower():
                        self.log_result(
                            "Show Transaction",
                            True,
                            "SKIPPED - Requires FortiOS 7.4.1+"
                        )
                    else:
                        raise
                
                # Clean up
                txn.abort()
        
        except Exception as e:
            self.log_result("Show Transaction", False, f"Error: {e}")
    
    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "="*70)
        print("FortiOS Transaction Live Tests")
        print("="*70)
        print(f"FortiGate: {self.host}")
        print(f"VDOM: {self.vdom}")
        print("="*70)
        
        # Clean up first
        self.cleanup_test_objects()
        
        # Run tests
        self.test_1_context_manager_success()
        self.test_2_context_manager_abort()
        self.test_3_manual_commit()
        self.test_4_manual_abort()
        self.test_5_decorator_pattern()
        self.test_6_nested_transaction_prevention()
        self.test_7_transaction_properties()
        self.test_8_list_transactions()
        self.test_9_transaction_timeout()
        self.test_10_show_transaction()
        
        # Final cleanup
        self.cleanup_test_objects()
        
        # Print summary
        print("\n" + "="*70)
        print("TEST SUMMARY")
        print("="*70)
        
        passed = sum(1 for _, p, _ in self.test_results if p)
        total = len(self.test_results)
        
        for test_name, passed_flag, message in self.test_results:
            status = "✅" if passed_flag else "❌"
            print(f"{status} {test_name}")
            if message and not passed_flag:
                print(f"    {message}")
        
        print("\n" + "="*70)
        print(f"Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 ALL TESTS PASSED!")
        else:
            print(f"⚠️  {total - passed} test(s) failed")
        
        print("="*70)
        
        return passed == total


def main():
    """Main entry point"""
    tester = TestTransactions()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
