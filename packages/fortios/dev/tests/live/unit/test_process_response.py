"""
Tests for hfortix_fortios.models.process_response function.

process_response converts API results to FortiObject instances (or lists of them) and
passes through primitives/other objects unchanged. response_mode was removed in 0.5.71.
"""

import sys
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
    from hfortix_fortios.models import process_response, FortiObject

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Basic Functionality Tests
    # =================================================================

    def test_process_response_returns_fortiobject_for_dict():
        """process_response should wrap dict into FortiObject."""
        result = {'name': 'test', 'status': 'enable'}
        processed = process_response(result)
        assert isinstance(processed, FortiObject)
        assert processed.get("name") == 'test'
        assert processed.get("status") == 'enable'
        return True, None

    tests.append(("dict -> FortiObject", test_process_response_returns_fortiobject_for_dict))

    # =================================================================
    # List Results Tests
    # =================================================================

    def test_process_response_list_to_objects():
        """process_response with list of dict should return list of FortiObjects."""
        result = [{'name': 'addr1'}, {'name': 'addr2'}]
        processed = process_response(result)
        assert isinstance(processed, list)
        assert len(processed) == 2
        assert isinstance(processed[0], FortiObject)
        assert processed[0].name == 'addr1'
        return True, None

    tests.append(("list of dict -> list of FortiObjects", test_process_response_list_to_objects))

    def test_process_response_empty_list():
        """process_response with empty list."""
        result = []
        processed = process_response(result)
        assert isinstance(processed, list)
        assert len(processed) == 0
        return True, None

    tests.append(("empty list", test_process_response_empty_list))

    # =================================================================
    # unwrap_single Tests
    # =================================================================

    def test_process_response_unwrap_single_true():
        """process_response with unwrap_single=True and single item list."""
        result = [{'name': 'only-one'}]
        processed = process_response(result, unwrap_single=True)
        # Should unwrap to single FortiObject, not list
        assert isinstance(processed, FortiObject)
        assert processed.get("name") == 'only-one'
        return True, None

    tests.append(("unwrap_single=True with single item", test_process_response_unwrap_single_true))

    def test_process_response_unwrap_single_multiple():
        """process_response with unwrap_single=True but multiple items."""
        result = [{'name': 'one'}, {'name': 'two'}]
        processed = process_response(result, unwrap_single=True)
        # Should NOT unwrap since there are multiple items
        assert isinstance(processed, list)
        assert len(processed) == 2
        return True, None

    tests.append(("unwrap_single=True with multiple items", test_process_response_unwrap_single_multiple))

    def test_process_response_unwrap_single_false():
        """process_response with unwrap_single=False (default)."""
        result = [{'name': 'only-one'}]
        processed = process_response(result, unwrap_single=False)
        # Should remain as list
        assert isinstance(processed, list)
        assert len(processed) == 1
        return True, None

    tests.append(("unwrap_single=False keeps list", test_process_response_unwrap_single_false))

    def test_process_response_unwrap_empty_list():
        """process_response with unwrap_single=True and empty list."""
        result = []
        processed = process_response(result, unwrap_single=True)
        # Empty list should remain empty list
        assert isinstance(processed, list)
        assert len(processed) == 0
        return True, None

    tests.append(("unwrap_single=True with empty list", test_process_response_unwrap_empty_list))

    # =================================================================
    # Edge Cases
    # =================================================================

    def test_process_response_none_result():
        """process_response with None result."""
        processed = process_response(None)
        # Should handle None gracefully
        assert processed is None
        return True, None

    tests.append(("None result", test_process_response_none_result))

    def test_process_response_nested_dicts():
        """process_response with nested dict structure."""
        result = {
            'name': 'policy1',
            'srcaddr': [{'name': 'addr1'}, {'name': 'addr2'}],
            'dstaddr': [{'name': 'all'}]
        }
        processed = process_response(result)
        assert isinstance(processed, FortiObject)
        assert processed.get("name") == 'policy1'
        # Nested lists should also be accessible
        return True, None

    tests.append(("nested dict structure", test_process_response_nested_dicts))

    def test_process_response_string_result():
        """process_response with string result (edge case)."""
        result = "some string response"
        processed = process_response(result)
        # Should handle non-dict gracefully
        assert processed == result
        return True, None

    tests.append(("string result passthrough", test_process_response_string_result))

    def test_process_response_int_result():
        """process_response with int result (edge case)."""
        result = 42
        processed = process_response(result)
        assert processed == 42
        return True, None

    tests.append(("int result passthrough", test_process_response_int_result))

    def test_process_response_bool_result():
        """process_response with bool result."""
        result = True
        processed = process_response(result)
        assert processed is True
        return True, None

    tests.append(("bool result passthrough", test_process_response_bool_result))

    def test_process_response_mixed_list():
        """process_response with mixed list (dicts and non-dicts)."""
        result = [{'name': 'dict1'}, 'string', 123]
        processed = process_response(result)
        # Should handle gracefully - first item dict triggers wrapping attempt
        assert isinstance(processed, list)
        return True, None

    tests.append(("mixed list handling", test_process_response_mixed_list))

    def test_process_response_deeply_nested():
        """process_response with deeply nested structure."""
        result = {
            'level1': {
                'level2': {
                    'level3': {
                        'value': 'deep'
                    }
                }
            }
        }
        processed = process_response(result)
        assert isinstance(processed, FortiObject)
        return True, None

    tests.append(("deeply nested structure", test_process_response_deeply_nested))

    def test_process_response_with_none_values():
        """process_response with None values in dict."""
        result = {'name': 'test', 'value': None, 'config': None}
        processed = process_response(result)
        assert isinstance(processed, FortiObject)
        assert processed.get("name") == 'test'
        assert processed.get("value") is None
        return True, None

    tests.append(("dict with None values", test_process_response_with_none_values))

    def test_process_response_with_empty_dict():
        """process_response with empty dict."""
        result = {}
        processed = process_response(result)
        assert isinstance(processed, FortiObject)
        return True, None

    tests.append(("empty dict", test_process_response_with_empty_dict))

    def test_process_response_list_of_strings():
        """process_response with list of strings."""
        result = ['item1', 'item2', 'item3']
        processed = process_response(result)
        # List of non-dicts should pass through
        assert isinstance(processed, list)
        assert processed == result
        return True, None

    tests.append(("list of strings passthrough", test_process_response_list_of_strings))

    # =================================================================
    # unwrap_single with nested objects still works
    # =================================================================

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}process_response Tests{Colors.RESET}")
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
