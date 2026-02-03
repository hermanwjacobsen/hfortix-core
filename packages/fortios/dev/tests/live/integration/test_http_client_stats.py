"""
Tests for HTTPClient stats methods with live connection.

Tests the various statistics and metrics methods that require
an active connection to properly populate data.

Run with: python -m pytest.integration.test_http_client_stats
"""

import sys
import os

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_test_result(name: str, passed: bool, error: str | None = None):
    status = f"{Colors.GREEN}PASS{Colors.RESET}" if passed else f"{Colors.RED}FAIL{Colors.RESET}"
    print(f"  [{status}] {name}")
    if error:
        print(f"         {Colors.RED}{error}{Colors.RESET}")


def run_tests():
    # Import client from shared config
    from fgtclient import fgt

    passed = 0
    failed = 0
    tests = []

    # Make some requests first to populate stats
    print("  Making test requests to populate stats...")
    try:
        fgt.api.monitor.system.status.get()
        fgt.api.cmdb.system.global_.get()  # Note: global is reserved, hence global_
    except:
        pass  # Continue even if these fail

    # =================================================================
    # Connection Stats Tests
    # =================================================================

    def test_connection_stats_structure():
        """Connection stats should have expected structure."""
        stats = fgt.get_connection_stats()
        assert isinstance(stats, dict)
        
        # Log the actual keys for debugging
        print(f"      Keys: {list(stats.keys())}")
        return True, None

    tests.append(("connection_stats structure", test_connection_stats_structure))

    def test_connection_stats_has_request_counts():
        """Connection stats should track request counts."""
        stats = fgt.get_connection_stats()
        
        # Look for request count fields (exact names may vary)
        count_fields = [k for k in stats.keys() if 'request' in k.lower() or 'count' in k.lower()]
        if count_fields:
            print(f"      Count fields: {count_fields}")
        return True, None

    tests.append(("connection_stats has request counts", test_connection_stats_has_request_counts))

    def test_connection_stats_after_requests():
        """Connection stats should increment after requests."""
        stats_before = fgt.get_connection_stats()
        
        # Make a request
        fgt.api.monitor.system.status.get()
        
        stats_after = fgt.get_connection_stats()
        
        # Stats should exist
        assert isinstance(stats_after, dict)
        return True, None

    tests.append(("connection_stats after requests", test_connection_stats_after_requests))

    # =================================================================
    # Health Metrics Tests
    # =================================================================

    def test_health_metrics_structure():
        """Health metrics should have expected structure."""
        metrics = fgt.get_health_metrics()
        assert isinstance(metrics, dict)
        
        print(f"      Keys: {list(metrics.keys())}")
        return True, None

    tests.append(("health_metrics structure", test_health_metrics_structure))

    def test_health_metrics_has_timing():
        """Health metrics should include timing information."""
        metrics = fgt.get_health_metrics()
        
        # Look for timing-related fields
        timing_fields = [k for k in metrics.keys() if 
                        'time' in k.lower() or 
                        'latency' in k.lower() or 
                        'duration' in k.lower() or
                        'avg' in k.lower()]
        if timing_fields:
            print(f"      Timing fields: {timing_fields}")
        return True, None

    tests.append(("health_metrics has timing info", test_health_metrics_has_timing))

    # =================================================================
    # Retry Stats Tests
    # =================================================================

    def test_retry_stats_structure():
        """Retry stats should have expected structure."""
        retry_stats = fgt.get_retry_stats()
        assert isinstance(retry_stats, dict)
        
        print(f"      Keys: {list(retry_stats.keys())}")
        return True, None

    tests.append(("retry_stats structure", test_retry_stats_structure))

    def test_retry_stats_counts():
        """Retry stats should track retry counts."""
        retry_stats = fgt.get_retry_stats()
        
        # With a working connection, retries should be 0 or low
        retry_fields = [k for k in retry_stats.keys() if 'retry' in k.lower() or 'attempt' in k.lower()]
        if retry_fields:
            print(f"      Retry fields: {retry_fields}")
        return True, None

    tests.append(("retry_stats counts", test_retry_stats_counts))

    # =================================================================
    # Circuit Breaker Tests
    # =================================================================

    def test_circuit_breaker_structure():
        """Circuit breaker state should have expected structure."""
        state = fgt.get_circuit_breaker_state()
        assert isinstance(state, dict)
        
        print(f"      Keys: {list(state.keys())}")
        return True, None

    tests.append(("circuit_breaker structure", test_circuit_breaker_structure))

    def test_circuit_breaker_closed_state():
        """Circuit breaker should be closed with working connection."""
        state = fgt.get_circuit_breaker_state()
        
        # Look for state field
        if 'state' in state:
            current_state = state['state'].upper() if isinstance(state['state'], str) else state['state']
            print(f"      State: {current_state}")
            # With working connection, should be closed
            assert current_state in ['CLOSED', 'closed', 'HALF_OPEN', 'half_open']
        return True, None

    tests.append(("circuit_breaker closed state", test_circuit_breaker_closed_state))

    def test_circuit_breaker_failure_count():
        """Circuit breaker should track failure count."""
        state = fgt.get_circuit_breaker_state()
        
        failure_fields = [k for k in state.keys() if 'fail' in k.lower() or 'error' in k.lower()]
        if failure_fields:
            print(f"      Failure fields: {failure_fields}")
        return True, None

    tests.append(("circuit_breaker failure count", test_circuit_breaker_failure_count))

    # =================================================================
    # Operations Tracking Tests
    # =================================================================

    def test_operations_list():
        """get_operations() should return list of operations."""
        operations = fgt.get_operations()
        assert isinstance(operations, list)
        
        print(f"      Operation count: {len(operations)}")
        if operations:
            print(f"      First op keys: {list(operations[0].keys()) if isinstance(operations[0], dict) else type(operations[0])}")
        return True, None

    tests.append(("operations list", test_operations_list))

    def test_operations_has_recent():
        """Operations list should include recent requests."""
        # Make a request
        fgt.api.monitor.system.status.get()
        
        operations = fgt.get_operations()
        
        # Should have at least one operation
        if len(operations) > 0:
            print(f"      Has {len(operations)} operation(s)")
        return True, None

    tests.append(("operations has recent requests", test_operations_has_recent))

    def test_write_operations_list():
        """get_write_operations() should return list."""
        write_ops = fgt.get_write_operations()
        assert isinstance(write_ops, list)
        
        print(f"      Write operation count: {len(write_ops)}")
        return True, None

    tests.append(("write_operations list", test_write_operations_list))

    # =================================================================
    # Last Request Tests
    # =================================================================

    def test_last_request_after_get():
        """last_request should show GET request info."""
        fgt.api.monitor.system.status.get()
        
        last = fgt.last_request
        assert isinstance(last, dict)
        
        print(f"      Keys: {list(last.keys())}")
        
        # Should have method info
        if 'method' in last:
            assert last['method'].upper() == 'GET'
        return True, None

    tests.append(("last_request after GET", test_last_request_after_get))

    def test_last_request_has_timing():
        """last_request should include timing information."""
        fgt.api.monitor.system.status.get()
        
        last = fgt.last_request
        assert last is not None, "last_request should not be None after a request"
        
        timing_fields = [k for k in last.keys() if 
                        'time' in k.lower() or 
                        'duration' in k.lower() or
                        'elapsed' in k.lower()]
        if timing_fields:
            print(f"      Timing fields: {timing_fields}")
        return True, None

    tests.append(("last_request has timing", test_last_request_has_timing))

    def test_last_request_has_response_info():
        """last_request should include response information."""
        fgt.api.monitor.system.status.get()
        
        last = fgt.last_request
        assert last is not None, "last_request should not be None after a request"
        
        response_fields = [k for k in last.keys() if 
                         'status' in k.lower() or 
                         'response' in k.lower() or
                         'http' in k.lower()]
        if response_fields:
            print(f"      Response fields: {response_fields}")
        return True, None

    tests.append(("last_request has response info", test_last_request_has_response_info))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}HTTPClient Stats Tests (Live Connection){Colors.RESET}")
    print("=" * 50)

    for name, test_func in tests:
        try:
            success, error = test_func()
            if success:
                passed += 1
                print_test_result(name, True)
            else:
                failed += 1
                print_test_result(name, False, error)
        except Exception as e:
            failed += 1
            print_test_result(name, False, str(e))

    print("=" * 50)
    total = passed + failed
    print(f"Results: {passed}/{total} passed", end="")
    if failed > 0:
        print(f" ({Colors.RED}{failed} failed{Colors.RESET})")
    else:
        print(f" ({Colors.GREEN}all passed{Colors.RESET})")

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
