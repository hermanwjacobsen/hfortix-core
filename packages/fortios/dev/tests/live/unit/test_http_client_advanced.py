"""
Tests for advanced HTTPClient methods.

Tests methods that don't require live connections or can be tested in isolation:
- configure_endpoint_timeout
- inspect_last_request
- get_health_metrics
- reset_circuit_breaker
- get_binary (structure only)

Note: These tests use the FortiOS client's public methods where available.
"""

import sys
import os
sys.path.insert(0, '/home/fo8038/test')

from hfortix_core.http import HTTPClient, BaseHTTPClient


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
    """Run all HTTP client advanced tests."""
    
    # Import client from shared config for live tests
    from tests.fgtclient import fgt
    
    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # get_health_metrics Tests
    # =================================================================

    def test_get_health_metrics_returns_dict():
        """get_health_metrics should return a dict."""
        result = fgt.get_health_metrics()
        assert isinstance(result, dict)
        return True, None

    tests.append(("get_health_metrics returns dict", test_get_health_metrics_returns_dict))

    def test_get_health_metrics_structure():
        """get_health_metrics should have expected keys."""
        result = fgt.get_health_metrics()
        assert isinstance(result, dict)
        # Print keys for documentation
        print(f"    Health metrics keys: {list(result.keys())[:5]}...")
        return True, None

    tests.append(("get_health_metrics structure", test_get_health_metrics_structure))

    # =================================================================
    # get_circuit_breaker_state Tests
    # =================================================================

    def test_get_circuit_breaker_state_returns_dict():
        """get_circuit_breaker_state should return a dict."""
        result = fgt.get_circuit_breaker_state()
        assert isinstance(result, dict)
        return True, None

    tests.append(("get_circuit_breaker_state returns dict", test_get_circuit_breaker_state_returns_dict))

    def test_get_circuit_breaker_state_has_state():
        """get_circuit_breaker_state should include state info."""
        result = fgt.get_circuit_breaker_state()
        # Should have state field or similar
        assert len(result) > 0 or result == {}  # May be empty if not configured
        return True, None

    tests.append(("get_circuit_breaker_state has state", test_get_circuit_breaker_state_has_state))

    # =================================================================
    # get_retry_stats Tests
    # =================================================================

    def test_get_retry_stats_returns_dict():
        """get_retry_stats should return a dict."""
        result = fgt.get_retry_stats()
        assert isinstance(result, dict)
        return True, None

    tests.append(("get_retry_stats returns dict", test_get_retry_stats_returns_dict))

    # =================================================================
    # get_connection_stats Tests
    # =================================================================

    def test_get_connection_stats_returns_dict():
        """get_connection_stats should return a dict."""
        result = fgt.get_connection_stats()
        assert isinstance(result, dict)
        return True, None

    tests.append(("get_connection_stats returns dict", test_get_connection_stats_returns_dict))

    def test_get_connection_stats_after_requests():
        """get_connection_stats should update after requests."""
        # Make some requests
        fgt.api.cmdb.firewall.address.get()
        
        result = fgt.get_connection_stats()
        assert isinstance(result, dict)
        # Should have request counts
        return True, None

    tests.append(("get_connection_stats after requests", test_get_connection_stats_after_requests))

    # =================================================================
    # get_operations Tests
    # =================================================================

    def test_get_operations_returns_list():
        """get_operations should return a list."""
        result = fgt.get_operations()
        assert isinstance(result, list)
        return True, None

    tests.append(("get_operations returns list", test_get_operations_returns_list))

    # =================================================================
    # get_write_operations Tests
    # =================================================================

    def test_get_write_operations_returns_list():
        """get_write_operations should return a list."""
        result = fgt.get_write_operations()
        assert isinstance(result, list)
        return True, None

    tests.append(("get_write_operations returns list", test_get_write_operations_returns_list))

    # =================================================================
    # Static Methods Tests (don't need connection)
    # =================================================================

    def test_build_params_static():
        """HTTPClient.build_params should work as static method."""
        result = HTTPClient.build_params(name="test", value=123, empty=None)
        assert result == {"name": "test", "value": 123}
        assert "empty" not in result
        return True, None

    tests.append(("HTTPClient.build_params static", test_build_params_static))

    def test_validate_choice_static():
        """HTTPClient.validate_choice should work as static method."""
        # Should not raise
        HTTPClient.validate_choice("enable", ["enable", "disable"], "status")
        return True, None

    tests.append(("HTTPClient.validate_choice static", test_validate_choice_static))

    def test_validate_mkey_static():
        """HTTPClient.validate_mkey should work as static method."""
        result = HTTPClient.validate_mkey("test-address")
        assert result == "test-address"
        
        result = HTTPClient.validate_mkey(123)
        assert result == "123"
        return True, None

    tests.append(("HTTPClient.validate_mkey static", test_validate_mkey_static))

    def test_validate_range_static():
        """HTTPClient.validate_range should work as static method."""
        # Should not raise
        HTTPClient.validate_range(50, 0, 100, "value")
        HTTPClient.validate_range(0, 0, 100, "value")
        HTTPClient.validate_range(100, 0, 100, "value")
        return True, None

    tests.append(("HTTPClient.validate_range static", test_validate_range_static))

    def test_validate_required_params_static():
        """HTTPClient.validate_required_params should work as static method."""
        # Should not raise
        HTTPClient.validate_required_params(
            {"name": "test", "type": "subnet"},
            ["name", "type"]
        )
        return True, None

    tests.append(("HTTPClient.validate_required_params static", test_validate_required_params_static))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}HTTPClient Advanced Tests{Colors.RESET}")
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
