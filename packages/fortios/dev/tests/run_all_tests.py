#!/usr/bin/env python3
"""
HFortix Complete Test Suite Runner - v1.0.0

Runs all tests across both live integration tests and schema validators.

Test Suites:
    1. Schema Validators (1,447 tests)
       - Validator function imports
       - Required field validation
       - Enum value validation
       - No live API calls required
       - Runs in parallel (fast)
    
    2. Live Integration Tests
       - FortiGate Direct Client tests
       - FortiManager Proxy Client tests
       - Real API calls to devices
       - Sequential execution (respects rate limits)

Usage:
    python run_all_tests.py                          # Run all tests
    python run_all_tests.py --schema-only            # Only schema validators
    python run_all_tests.py --live-only              # Only live integration tests
    python run_all_tests.py --live-client=direct     # Live tests with FGT direct client only
    python run_all_tests.py --live-client=fmg_proxy  # Live tests with FMG proxy client only
    python run_all_tests.py --live-client=both       # Live tests with both clients (default)
    python run_all_tests.py --verbose                # Verbose output
    python run_all_tests.py --no-cleanup             # Skip cleanup before live tests

Exit Codes:
    0 - All tests passed
    1 - Some tests failed
    2 - Configuration/environment error
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Literal


class TestSuiteRunner:
    """Orchestrates running multiple test suites."""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.tests_dir = Path(__file__).parent
        self.project_root = self.tests_dir.parent
        self.venv_python = self._get_venv_python()
        self.total_passed = 0
        self.total_failed = 0
        
    def _get_venv_python(self) -> str:
        """Get path to virtual environment Python."""
        venv_python = self.project_root / ".venv" / "bin" / "python"
        if venv_python.exists():
            return str(venv_python)
        return sys.executable
    
    def _print_section(self, title: str, char: str = "="):
        """Print a formatted section header."""
        print()
        print(char * 80)
        print(f"{title:^80}")
        print(char * 80)
        print()
    
    def run_schema_validators(self) -> bool:
        """
        Run schema validator tests (no live API calls).
        
        Returns:
            True if all tests passed, False otherwise
        """
        self._print_section("Schema Validator Tests (1,447 tests)")
        
        schema_runner = self.tests_dir / "schema-validators" / "__runtests__.py"
        
        if not schema_runner.exists():
            print(f"❌ Schema validator runner not found: {schema_runner}")
            return False
        
        try:
            result = subprocess.run(
                [self.venv_python, str(schema_runner)],
                cwd=str(self.tests_dir / "schema-validators"),
                check=False,
            )
            
            if result.returncode == 0:
                print("\n✅ All schema validator tests passed!")
                return True
            else:
                print(f"\n❌ Schema validator tests failed (exit code: {result.returncode})")
                return False
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Schema validator tests interrupted by user")
            raise  # Re-raise to propagate to main
                
        except Exception as e:
            print(f"❌ Error running schema validators: {e}")
            return False
    
    def run_live_tests(
        self,
        client: Literal["direct", "fmg_proxy", "both"] = "both",
        no_cleanup: bool = False
    ) -> bool:
        """
        Run live integration tests against FortiGate/FortiManager.
        
        Args:
            client: Which client to test ("direct", "fmg_proxy", or "both")
            no_cleanup: Skip cleanup before running tests
            
        Returns:
            True if all tests passed, False otherwise
        """
        live_runner = self.tests_dir / "live" / "__runtests__.py"
        
        if not live_runner.exists():
            print(f"❌ Live test runner not found: {live_runner}")
            return False
        
        # Determine which clients to run
        if client == "both":
            clients = ["direct", "fmg_proxy"]
        else:
            clients = [client]
        
        all_passed = True
        
        for client_type in clients:
            # Display friendly names for output
            client_display = {
                "direct": "FGT Direct",
                "fmg_proxy": "FMG Proxy"
            }.get(client_type, client_type.upper())
            
            self._print_section(
                f"Live Integration Tests - {client_display} Client"
            )
            
            cmd = [self.venv_python, str(live_runner), f"--client={client_type}"]
            if no_cleanup:
                cmd.append("--no-cleanup")
            if not self.verbose:
                cmd.append("--quiet")
            
            try:
                result = subprocess.run(
                    cmd,
                    cwd=str(self.tests_dir / "live"),
                    check=False,
                )
                
                if result.returncode == 0:
                    print(f"\n✅ All {client_display} client tests passed!")
                else:
                    print(f"\n❌ {client_display} client tests failed (exit code: {result.returncode})")
                    all_passed = False
            
            except KeyboardInterrupt:
                print(f"\n\n⚠️  {client_display} client tests interrupted by user")
                raise  # Re-raise to propagate to main
                    
            except Exception as e:
                print(f"❌ Error running {client_display} tests: {e}")
                all_passed = False
        
        return all_passed
    
    def run_all(
        self,
        schema_only: bool = False,
        live_only: bool = False,
        live_client: Literal["direct", "fmg_proxy", "both"] = "both",
        no_cleanup: bool = False
    ) -> int:
        """
        Run all test suites.
        
        Returns:
            Exit code (0 = success, 1 = failures, 2 = error)
        """
        self._print_section("HFortix Complete Test Suite", "=")
        
        print("Test Suites:")
        if not live_only:
            print("  • Schema Validators (1,447 tests) - No API calls, parallel execution")
        if not schema_only:
            if live_client == "both":
                print("  • Live Integration Tests - FGT Direct Client")
                print("  • Live Integration Tests - FMG Proxy Client")
            elif live_client == "direct":
                print("  • Live Integration Tests - FGT Direct Client")
            else:
                print("  • Live Integration Tests - FMG Proxy Client")
        
        results = {}
        
        # Run schema validators
        if not live_only:
            results["schema"] = self.run_schema_validators()
        
        # Run live tests
        if not schema_only:
            results["live"] = self.run_live_tests(
                client=live_client,
                no_cleanup=no_cleanup
            )
        
        # Print summary
        self._print_section("Test Suite Summary", "=")
        
        all_passed = all(results.values())
        
        for suite, passed in results.items():
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"{suite.upper():20} {status}")
        
        print()
        if all_passed:
            print("🎉 All test suites passed!")
            return 0
        else:
            print("❌ Some test suites failed. See details above.")
            return 1


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run all HFortix tests (schema validators + live integration)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # Run all tests
  %(prog)s --schema-only                # Only schema validators
  %(prog)s --live-only                  # Only live integration tests
  %(prog)s --live-client=direct         # Live tests with FGT direct client only
  %(prog)s --live-client=fmg_proxy      # Live tests with FMG proxy client only
  %(prog)s --verbose                    # Verbose output
  %(prog)s --no-cleanup                 # Skip cleanup before live tests
        """
    )
    
    parser.add_argument(
        "--schema-only",
        action="store_true",
        help="Run only schema validator tests (no live API calls)"
    )
    
    parser.add_argument(
        "--live-only",
        action="store_true",
        help="Run only live integration tests (skip schema validators)"
    )
    
    parser.add_argument(
        "--live-client",
        choices=["direct", "fmg_proxy", "both"],
        default="both",
        help="Which client to use for live tests (default: both)"
    )
    
    parser.add_argument(
        "--no-cleanup",
        action="store_true",
        help="Skip cleanup before running live tests"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.schema_only and args.live_only:
        print("❌ Error: --schema-only and --live-only are mutually exclusive")
        return 2
    
    # Run tests
    runner = TestSuiteRunner(verbose=args.verbose)
    
    try:
        return runner.run_all(
            schema_only=args.schema_only,
            live_only=args.live_only,
            live_client=args.live_client,
            no_cleanup=args.no_cleanup
        )
    except KeyboardInterrupt:
        print("\n\n⚠️  Test suite interrupted by user (Ctrl+C)")
        print("Exiting gracefully...")
        return 130  # Standard exit code for SIGINT


if __name__ == "__main__":
    sys.exit(main())
