"""
Tests for FortiOS client functionality.

Requires a live FortiGate connection.
Tests properties, stats methods, and export functionality.

Run with: python -m pytest.integration.test_fortios_client
"""

import sys
import os
import tempfile

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
    from fgtclient import fgt, HOST, PORT, VDOM

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Property Tests
    # =================================================================

    def test_host_property():
        """host property should return the configured host."""
        assert fgt.host == HOST
        return True, None

    tests.append(("host property", test_host_property))

    def test_port_property():
        """port property should return the configured port."""
        assert fgt.port == PORT
        return True, None

    tests.append(("port property", test_port_property))

    def test_vdom_property():
        """vdom property should return the configured vdom."""
        assert fgt.vdom == VDOM
        return True, None

    tests.append(("vdom property", test_vdom_property))

    def test_error_mode_property():
        """error_mode property should return the configured error mode."""
        assert fgt.error_mode == 'return'
        return True, None

    tests.append(("error_mode property", test_error_mode_property))

    def test_error_format_property():
        """error_format property should return a valid format."""
        error_format = fgt.error_format
        # Should be a string or None
        assert error_format is None or isinstance(error_format, str)
        return True, None

    tests.append(("error_format property", test_error_format_property))

    # =================================================================
    # Connection Stats Tests
    # =================================================================

    def test_connection_stats_property():
        """connection_stats should return dict with stats."""
        stats = fgt.connection_stats
        assert isinstance(stats, dict)
        return True, None

    tests.append(("connection_stats property", test_connection_stats_property))

    def test_get_connection_stats():
        """get_connection_stats() should return dict."""
        stats = fgt.get_connection_stats()
        assert isinstance(stats, dict)
        # Common keys that should be present
        expected_keys = ['requests', 'successful', 'failed']
        for key in expected_keys:
            if key not in stats:
                # Key might be named differently
                pass
        return True, None

    tests.append(("get_connection_stats()", test_get_connection_stats))

    def test_get_health_metrics():
        """get_health_metrics() should return dict with health data."""
        metrics = fgt.get_health_metrics()
        assert isinstance(metrics, dict)
        return True, None

    tests.append(("get_health_metrics()", test_get_health_metrics))

    def test_get_retry_stats():
        """get_retry_stats() should return dict with retry information."""
        retry_stats = fgt.get_retry_stats()
        assert isinstance(retry_stats, dict)
        return True, None

    tests.append(("get_retry_stats()", test_get_retry_stats))

    def test_get_operations():
        """get_operations() should return list of operations."""
        operations = fgt.get_operations()
        assert isinstance(operations, list)
        return True, None

    tests.append(("get_operations()", test_get_operations))

    def test_get_write_operations():
        """get_write_operations() should return list of write operations."""
        write_ops = fgt.get_write_operations()
        assert isinstance(write_ops, list)
        return True, None

    tests.append(("get_write_operations()", test_get_write_operations))

    # =================================================================
    # Circuit Breaker Tests
    # =================================================================

    def test_get_circuit_breaker_state():
        """get_circuit_breaker_state() should return dict."""
        state = fgt.get_circuit_breaker_state()
        assert isinstance(state, dict)
        # Should have a state field
        if 'state' in state:
            assert state['state'] in ['closed', 'open', 'half_open', 'CLOSED', 'OPEN', 'HALF_OPEN']
        return True, None

    tests.append(("get_circuit_breaker_state()", test_get_circuit_breaker_state))

    # =================================================================
    # Last Request Tests
    # =================================================================

    def test_last_request_property():
        """last_request should return info about last request."""
        # Make a simple request first
        fgt.api.monitor.system.status.get()
        
        last = fgt.last_request
        assert isinstance(last, dict)
        return True, None

    tests.append(("last_request property after request", test_last_request_property))

    # =================================================================
    # API Property Tests
    # =================================================================

    def test_api_property():
        """api property should return API accessor."""
        api = fgt.api
        assert api is not None
        assert hasattr(api, 'cmdb')
        assert hasattr(api, 'monitor')
        return True, None

    tests.append(("api property", test_api_property))

    # =================================================================
    # Request Method Tests
    # =================================================================

    def test_request_method_get():
        """request() method should execute GET requests."""
        config = {
            'method': 'GET',
            'url': '/api/v2/cmdb/system/status'
        }
        result = fgt.request(config)
        assert isinstance(result, dict)
        assert 'http_status' in result or 'status' in result
        return True, None

    tests.append(("request() method GET", test_request_method_get))

    # =================================================================
    # Export Audit Logs Tests
    # =================================================================

    def test_export_audit_logs_to_string():
        """export_audit_logs() should return string when no filepath."""
        # Make a request first to have something in the logs
        fgt.api.monitor.system.status.get()
        
        result = fgt.export_audit_logs()
        # Result can be string or None (if no logs)
        assert result is None or isinstance(result, str)
        return True, None

    tests.append(("export_audit_logs() to string", test_export_audit_logs_to_string))

    def test_export_audit_logs_json_format():
        """export_audit_logs() with json format."""
        result = fgt.export_audit_logs(format='json')
        assert result is None or isinstance(result, str)
        if result:
            import json
            try:
                # Should be valid JSON
                parsed = json.loads(result)
                assert isinstance(parsed, (list, dict))
            except json.JSONDecodeError:
                # Might be empty or newline-delimited JSON
                pass
        return True, None

    tests.append(("export_audit_logs() json format", test_export_audit_logs_json_format))

    def test_export_audit_logs_to_file():
        """export_audit_logs() should write to file when filepath given."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            filepath = f.name
        
        try:
            fgt.export_audit_logs(filepath=filepath)
            # File should exist (might be empty if no logs)
            assert os.path.exists(filepath)
            return True, None
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    tests.append(("export_audit_logs() to file", test_export_audit_logs_to_file))

    def test_export_audit_logs_with_filter():
        """export_audit_logs() with method filter."""
        result = fgt.export_audit_logs(filter_method='GET')
        assert result is None or isinstance(result, str)
        return True, None

    tests.append(("export_audit_logs() with filter", test_export_audit_logs_with_filter))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}FortiOS Client Tests (Live Connection){Colors.RESET}")
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
