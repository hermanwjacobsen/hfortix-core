"""
Tests for additional response helper functions.

Tests the following from hfortix_fortios._helpers.response:
- get_name(response) - Gets the 'mkey' from response

Run with: python -m pytest.validators.test_response_helpers_extra
"""

import sys


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
    from hfortix_fortios._helpers.response import get_name

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # get_name Tests
    # =================================================================

    def test_get_name_with_mkey():
        """get_name should return mkey when present."""
        response = {'mkey': 'test_address', 'status': 'success'}
        result = get_name(response)
        assert result == 'test_address', f"Expected 'test_address', got {result}"
        return True, None

    tests.append(("get_name with mkey", test_get_name_with_mkey))

    def test_get_name_post_response():
        """get_name should extract mkey from POST response."""
        # Typical response after creating an object
        response = {
            'http_method': 'POST',
            'http_status': 200,
            'status': 'success',
            'mkey': 'new_firewall_address',
            'vdom': 'root',
        }
        result = get_name(response)
        assert result == 'new_firewall_address'
        return True, None

    tests.append(("get_name POST response", test_get_name_post_response))

    def test_get_name_no_mkey():
        """get_name should return None when no mkey."""
        response = {'status': 'success', 'results': []}
        result = get_name(response)
        assert result is None
        return True, None

    tests.append(("get_name no mkey", test_get_name_no_mkey))

    def test_get_name_empty_response():
        """get_name should return None for empty response."""
        response = {}
        result = get_name(response)
        assert result is None
        return True, None

    tests.append(("get_name empty response", test_get_name_empty_response))

    def test_get_name_non_dict():
        """get_name should return None for non-dict input."""
        result = get_name("not a dict")
        assert result is None
        
        result = get_name(None)  # type: ignore
        assert result is None
        
        result = get_name([])  # type: ignore
        assert result is None
        return True, None

    tests.append(("get_name non-dict input", test_get_name_non_dict))

    def test_get_name_mkey_empty_string():
        """get_name should return empty string if mkey is empty."""
        response = {'mkey': '', 'status': 'success'}
        result = get_name(response)
        # Empty string is falsy but still a valid mkey value
        assert result == ''
        return True, None

    tests.append(("get_name empty string mkey", test_get_name_mkey_empty_string))

    def test_get_name_mkey_with_special_chars():
        """get_name should handle mkey with special characters."""
        response = {'mkey': 'addr-with_special.chars', 'status': 'success'}
        result = get_name(response)
        assert result == 'addr-with_special.chars'
        return True, None

    tests.append(("get_name special chars", test_get_name_mkey_with_special_chars))

    def test_get_name_mkey_integer():
        """get_name should handle mkey as integer (policy IDs)."""
        response = {'mkey': 123, 'status': 'success'}
        result = get_name(response)
        assert result == 123
        return True, None

    tests.append(("get_name integer mkey", test_get_name_mkey_integer))

    def test_get_name_real_create_response():
        """get_name should work with real FortiOS create response."""
        response = {
            'http_method': 'POST',
            'http_status': 200,
            'status': 'success',
            'vdom': 'root',
            'path': 'firewall',
            'name': 'address',
            'mkey': 'my_new_address',
            'build': 2571,
            'version': 'v7.2.8',
            'serial': 'FGVMEV123456789',
        }
        result = get_name(response)
        assert result == 'my_new_address'
        return True, None

    tests.append(("get_name real create response", test_get_name_real_create_response))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Response Helpers Extra Tests{Colors.RESET}")
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
