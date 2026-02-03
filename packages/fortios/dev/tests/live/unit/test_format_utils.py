"""
Tests for hfortix_core format utility functions.

Tests:
- format_connection_stats() - formats connection stats dict to string
- format_request_info() - formats request info dict to string
"""

import sys
from typing import Any
sys.path.insert(0, '/home/fo8038/test')


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
    from hfortix_core import format_connection_stats, format_request_info

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # format_connection_stats Tests
    # =================================================================

    def test_format_connection_stats_none():
        """format_connection_stats should handle None gracefully."""
        result = format_connection_stats(None)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats with None", test_format_connection_stats_none))

    def test_format_connection_stats_empty():
        """format_connection_stats should handle empty dict."""
        result = format_connection_stats({})
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats with empty dict", test_format_connection_stats_empty))

    def test_format_connection_stats_basic():
        """format_connection_stats should format basic stats."""
        stats = {
            'total_requests': 10,
            'successful_requests': 8,
            'failed_requests': 2,
            'average_response_time': 0.5
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        assert len(result) > 0
        return True, None

    tests.append(("format_connection_stats basic stats", test_format_connection_stats_basic))

    def test_format_connection_stats_with_nested():
        """format_connection_stats should handle nested structures."""
        stats = {
            'total_requests': 100,
            'by_method': {
                'GET': 60,
                'POST': 30,
                'DELETE': 10
            },
            'errors': {
                '404': 5,
                '500': 2
            }
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats nested stats", test_format_connection_stats_with_nested))

    def test_format_connection_stats_with_floats():
        """format_connection_stats should handle float values."""
        stats = {
            'average_response_time': 0.12345,
            'min_response_time': 0.001,
            'max_response_time': 5.5
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats with floats", test_format_connection_stats_with_floats))

    def test_format_connection_stats_with_zero():
        """format_connection_stats should handle zero values."""
        stats = {
            'total_requests': 0,
            'failed_requests': 0,
            'average_response_time': 0.0
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats with zeros", test_format_connection_stats_with_zero))

    def test_format_connection_stats_with_none_values():
        """format_connection_stats should handle None values in dict."""
        stats = {
            'total_requests': 10,
            'last_error': None,
            'last_request_time': None
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats with None values", test_format_connection_stats_with_none_values))

    def test_format_connection_stats_with_list():
        """format_connection_stats should handle list values."""
        stats = {
            'recent_errors': ['timeout', 'connection refused', '500'],
            'total': 3
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats with list values", test_format_connection_stats_with_list))

    # =================================================================
    # format_request_info Tests
    # =================================================================

    def test_format_request_info_none():
        """format_request_info should handle None gracefully."""
        result = format_request_info(None)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with None", test_format_request_info_none))

    def test_format_request_info_empty():
        """format_request_info should handle empty dict."""
        result = format_request_info({})
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with empty dict", test_format_request_info_empty))

    def test_format_request_info_basic():
        """format_request_info should format basic request info."""
        info = {
            'method': 'GET',
            'url': 'https://fortigate.example.com/api/v2/cmdb/firewall/address',
            'status_code': 200,
            'response_time': 0.234
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        assert len(result) > 0
        return True, None

    tests.append(("format_request_info basic info", test_format_request_info_basic))

    def test_format_request_info_with_headers():
        """format_request_info should handle headers."""
        info = {
            'method': 'POST',
            'url': '/api/v2/cmdb/firewall/address',
            'headers': {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer xxx'
            },
            'status_code': 200
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with headers", test_format_request_info_with_headers))

    def test_format_request_info_with_body():
        """format_request_info should handle request body."""
        info = {
            'method': 'POST',
            'url': '/api/v2/cmdb/firewall/address',
            'body': {'name': 'test-address', 'subnet': '10.0.0.0/8'},
            'status_code': 200
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with body", test_format_request_info_with_body))

    def test_format_request_info_error_response():
        """format_request_info should handle error responses."""
        info = {
            'method': 'DELETE',
            'url': '/api/v2/cmdb/firewall/address/nonexistent',
            'status_code': 404,
            'error': 'Entry not found'
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info error response", test_format_request_info_error_response))

    def test_format_request_info_with_params():
        """format_request_info should handle query params."""
        info = {
            'method': 'GET',
            'url': '/api/v2/cmdb/firewall/address',
            'params': {'vdom': 'root', 'filter': 'name=@test'},
            'status_code': 200
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with params", test_format_request_info_with_params))

    def test_format_request_info_with_special_chars():
        """format_request_info should handle special characters."""
        info = {
            'method': 'GET',
            'url': '/api/v2/cmdb/firewall/address/test%20address',
            'body': {'comment': 'Test <script>alert("xss")</script>'},
            'status_code': 200
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with special chars", test_format_request_info_with_special_chars))

    def test_format_request_info_with_unicode():
        """format_request_info should handle unicode."""
        info = {
            'method': 'POST',
            'url': '/api/v2/cmdb/firewall/address',
            'body': {'name': 'test-日本語', 'comment': '🔥 emoji test'},
            'status_code': 200
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_request_info with unicode", test_format_request_info_with_unicode))

    def test_format_request_info_large_body():
        """format_request_info should handle large bodies (truncation?)."""
        info = {
            'method': 'POST',
            'url': '/api/v2/cmdb/firewall/policy',
            'body': {'data': 'x' * 10000},  # Very large body
            'status_code': 200
        }
        result = format_request_info(info)
        assert isinstance(result, str)
        # Should either include full body or truncate gracefully
        return True, None

    tests.append(("format_request_info large body", test_format_request_info_large_body))

    # =================================================================
    # Edge Cases
    # =================================================================

    def test_format_connection_stats_unexpected_types():
        """format_connection_stats with unexpected value types."""
        stats = {
            'count': 'not-a-number',  # String instead of int
            'flag': True,  # Boolean
            'timestamp': 1234567890  # Timestamp as int
        }
        result = format_connection_stats(stats)
        assert isinstance(result, str)
        return True, None

    tests.append(("format_connection_stats unexpected types", test_format_connection_stats_unexpected_types))

    def test_format_request_info_circular_reference():
        """format_request_info should handle circular references gracefully."""
        # Use plain dict (not TypedDict) for this test since we're adding arbitrary keys
        info: dict[str, Any] = {'method': 'GET', 'url': '/test'}
        # Note: Can't actually test circular ref in TypedDict, but test deeply nested
        info['nested'] = {'level1': {'level2': {'level3': {'level4': 'deep'}}}}
        try:
            result = format_request_info(info)
            assert isinstance(result, str)
            return True, None
        except RecursionError:
            return False, "RecursionError on deeply nested structure"

    tests.append(("format_request_info deeply nested", test_format_request_info_circular_reference))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Format Utils Tests{Colors.RESET}")
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
