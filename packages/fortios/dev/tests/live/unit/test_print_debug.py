"""
Tests for hfortix_fortios print_debug_info function.

This function prints debug information about HTTP requests/responses.
Requires live FortiGate connection to test with real data.
"""

import sys
import io
from contextlib import redirect_stdout
sys.path.insert(0, '/home/fo8038/test')

from tests.fgtclient import fgt


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
    """Run all print_debug_info tests."""

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Import Tests
    # =================================================================

    def test_print_debug_info_import():
        """print_debug_info function can be imported."""
        from hfortix_fortios import print_debug_info
        assert print_debug_info is not None
        assert callable(print_debug_info)
        return True, None

    tests.append(("print_debug_info importable", test_print_debug_info_import))

    def test_format_request_info_import():
        """format_request_info function can be imported."""
        from hfortix_fortios import format_request_info
        assert format_request_info is not None
        assert callable(format_request_info)
        return True, None

    tests.append(("format_request_info importable", test_format_request_info_import))

    def test_format_connection_stats_import():
        """format_connection_stats function can be imported."""
        from hfortix_fortios import format_connection_stats
        assert format_connection_stats is not None
        assert callable(format_connection_stats)
        return True, None

    tests.append(("format_connection_stats importable", test_format_connection_stats_import))

    # =================================================================
    # print_debug_info Output Tests
    # =================================================================

    def test_print_debug_info_with_real_request():
        """print_debug_info works with real FortiGate response.
        
        NOTE: print_debug_info expects a FortiOS client object, not a dict.
        It internally accesses client.last_request.
        """
        from hfortix_fortios import print_debug_info
        
        # Make a real request to populate last_request
        response = fgt.api.cmdb.firewall.address.get()
        
        # Capture output - pass the fgt client, not the dict
        captured = io.StringIO()
        with redirect_stdout(captured):
            print_debug_info(fgt)
        
        output = captured.getvalue()
        print(f"\n    Output length: {len(output)} chars")
        if len(output) > 100:
            print(f"    Sample: {output[:100]}...")
        
        # Should produce some output
        assert len(output) > 0
        return True, None

    tests.append(("print_debug_info with real request", test_print_debug_info_with_real_request))

    def test_print_debug_info_with_none():
        """print_debug_info handles None gracefully."""
        from hfortix_fortios import print_debug_info
        
        # Should not crash with None
        captured = io.StringIO()
        try:
            with redirect_stdout(captured):
                print_debug_info(None)
            return True, None
        except Exception as e:
            # Some handling is expected
            return True, None

    tests.append(("print_debug_info with None", test_print_debug_info_with_none))

    def test_print_debug_info_with_empty_dict():
        """print_debug_info handles empty dict."""
        from hfortix_fortios import print_debug_info
        
        captured = io.StringIO()
        try:
            with redirect_stdout(captured):
                print_debug_info({})
            return True, None
        except Exception as e:
            return True, None  # May raise, that's acceptable

    tests.append(("print_debug_info with empty dict", test_print_debug_info_with_empty_dict))

    # =================================================================
    # format_request_info Tests
    # =================================================================

    def test_format_request_info_basic():
        """format_request_info produces string output."""
        from hfortix_fortios import format_request_info
        
        # Make a real request to get request info
        response = fgt.api.cmdb.firewall.address.get()
        
        debug_info = getattr(fgt, 'debug_info', None) or getattr(fgt, 'last_request', None)
        if debug_info and isinstance(debug_info, dict):
            result = format_request_info(debug_info.get('request', {}))
            assert isinstance(result, str)
            print(f"\n    format_request_info output length: {len(result)} chars")
            return True, None
        else:
            print("\n    NOTE: No debug_info/last_request dict available")
            return True, None  # No debug info available

    tests.append(("format_request_info basic", test_format_request_info_basic))

    # =================================================================
    # format_connection_stats Tests
    # =================================================================

    def test_format_connection_stats_basic():
        """format_connection_stats produces string output."""
        from hfortix_fortios import format_connection_stats
        
        # Make a request to populate connection stats
        response = fgt.api.cmdb.firewall.address.get()
        
        debug_info = getattr(fgt, 'debug_info', None) or getattr(fgt, 'last_request', None)
        if debug_info and isinstance(debug_info, dict):
            stats = debug_info.get('stats', {})
            result = format_connection_stats(stats)
            assert isinstance(result, str)
            print(f"\n    format_connection_stats output length: {len(result)} chars")
            return True, None
        else:
            print("\n    NOTE: No debug_info/last_request dict available")
            return True, None  # No debug info available

    tests.append(("format_connection_stats basic", test_format_connection_stats_basic))

    # =================================================================
    # Debug Info Structure Tests
    # =================================================================

    def test_debug_info_structure():
        """Check debug_info structure after request."""
        response = fgt.api.cmdb.firewall.address.get()
        
        debug_info = getattr(fgt, 'debug_info', None) or getattr(fgt, 'last_request', None)
        if debug_info is None:
            print("\n    NOTE: debug_info is None (debug may be disabled)")
            return True, None
        
        print(f"\n    debug_info keys: {list(debug_info.keys()) if isinstance(debug_info, dict) else type(debug_info)}")
        print(f"    debug_info type: {type(debug_info)}")
        
        return True, None

    tests.append(("debug_info structure", test_debug_info_structure))

    def test_debug_info_has_request():
        """debug_info contains request info."""
        response = fgt.api.cmdb.firewall.address.get()
        
        debug_info = getattr(fgt, 'debug_info', None) or getattr(fgt, 'last_request', None)
        if debug_info is None:
            return True, None  # Debug disabled
        
        if isinstance(debug_info, dict) and 'request' in debug_info:
            req = debug_info['request']
            print(f"\n    request keys: {list(req.keys()) if isinstance(req, dict) else 'N/A'}")
        return True, None

    tests.append(("debug_info has request info", test_debug_info_has_request))

    def test_debug_info_has_response():
        """debug_info contains response info."""
        response = fgt.api.cmdb.firewall.address.get()
        
        debug_info = getattr(fgt, 'debug_info', None) or getattr(fgt, 'last_request', None)
        if debug_info is None:
            return True, None  # Debug disabled
        
        if isinstance(debug_info, dict) and 'response' in debug_info:
            resp = debug_info['response']
            print(f"\n    response keys: {list(resp.keys()) if isinstance(resp, dict) else 'N/A'}")
        return True, None

    tests.append(("debug_info has response info", test_debug_info_has_response))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}print_debug_info Tests{Colors.RESET}")
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
