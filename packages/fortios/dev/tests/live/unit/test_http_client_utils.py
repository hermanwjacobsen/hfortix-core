"""
Tests for HTTPClient utility methods.

These are static/class methods that don't require a live connection:
- build_params: Build query parameters dict
- validate_choice: Validate value is in allowed choices
- validate_mkey: Validate and convert mkey parameter
- validate_range: Validate numeric value in range
- validate_required_params: Validate required parameters are present
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
    from hfortix_core.http import HTTPClient

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # build_params Tests
    # =================================================================

    def test_build_params_basic():
        """build_params should create dict from kwargs."""
        result = HTTPClient.build_params(name='test', value=123)
        assert result == {'name': 'test', 'value': 123}
        return True, None

    tests.append(("build_params basic", test_build_params_basic))

    def test_build_params_filters_none():
        """build_params should filter out None values."""
        result = HTTPClient.build_params(name='test', empty=None, value=42)
        assert 'empty' not in result
        assert result == {'name': 'test', 'value': 42}
        return True, None

    tests.append(("build_params filters None", test_build_params_filters_none))

    def test_build_params_empty():
        """build_params with no args returns empty dict."""
        result = HTTPClient.build_params()
        assert result == {}
        return True, None

    tests.append(("build_params empty", test_build_params_empty))

    def test_build_params_preserves_false():
        """build_params should keep False values (not filter them)."""
        result = HTTPClient.build_params(enabled=False, count=0)
        assert result.get('enabled') is False
        assert result.get('count') == 0
        return True, None

    tests.append(("build_params preserves False and 0", test_build_params_preserves_false))

    def test_build_params_preserves_empty_string():
        """build_params should keep empty strings."""
        result = HTTPClient.build_params(name='', comment='test')
        assert 'name' in result
        assert result['name'] == ''
        return True, None

    tests.append(("build_params preserves empty string", test_build_params_preserves_empty_string))

    # =================================================================
    # validate_choice Tests
    # =================================================================

    def test_validate_choice_valid():
        """validate_choice should pass for valid choice."""
        # Should not raise
        HTTPClient.validate_choice('enable', ['enable', 'disable'], 'status')
        HTTPClient.validate_choice('tcp', ['tcp', 'udp', 'icmp'], 'protocol')
        return True, None

    tests.append(("validate_choice valid values", test_validate_choice_valid))

    def test_validate_choice_invalid():
        """validate_choice should raise ValueError for invalid choice."""
        try:
            HTTPClient.validate_choice('invalid', ['enable', 'disable'], 'status')
            return False, "Should raise ValueError for invalid choice"
        except ValueError as e:
            assert 'status' in str(e).lower() or 'invalid' in str(e).lower()
            return True, None

    tests.append(("validate_choice invalid raises ValueError", test_validate_choice_invalid))

    def test_validate_choice_case_sensitive():
        """validate_choice should be case-sensitive."""
        try:
            HTTPClient.validate_choice('Enable', ['enable', 'disable'], 'status')
            return False, "Should raise ValueError for wrong case"
        except ValueError:
            return True, None

    tests.append(("validate_choice is case-sensitive", test_validate_choice_case_sensitive))

    def test_validate_choice_with_integers():
        """validate_choice should work with integer choices."""
        HTTPClient.validate_choice(1, [1, 2, 3], 'priority')
        try:
            HTTPClient.validate_choice(4, [1, 2, 3], 'priority')
            return False, "Should raise ValueError for 4 not in [1,2,3]"
        except ValueError:
            return True, None

    tests.append(("validate_choice with integers", test_validate_choice_with_integers))

    # =================================================================
    # validate_mkey Tests
    # =================================================================

    def test_validate_mkey_string():
        """validate_mkey should accept string and return it."""
        result = HTTPClient.validate_mkey('policy_name', 'mkey')
        assert result == 'policy_name'
        return True, None

    tests.append(("validate_mkey string", test_validate_mkey_string))

    def test_validate_mkey_integer():
        """validate_mkey should convert integer to string."""
        result = HTTPClient.validate_mkey(123, 'policyid')
        assert result == '123'
        assert isinstance(result, str)
        return True, None

    tests.append(("validate_mkey integer converts to string", test_validate_mkey_integer))

    def test_validate_mkey_none():
        """validate_mkey should raise ValueError for None."""
        try:
            HTTPClient.validate_mkey(None, 'mkey')  # type: ignore
            return False, "Should raise ValueError for None"
        except (ValueError, TypeError):
            return True, None

    tests.append(("validate_mkey None raises error", test_validate_mkey_none))

    def test_validate_mkey_empty_string():
        """validate_mkey should handle empty string."""
        try:
            result = HTTPClient.validate_mkey('', 'mkey')
            # Empty string might be valid or invalid depending on implementation
            return True, None
        except ValueError:
            return True, None

    tests.append(("validate_mkey empty string handling", test_validate_mkey_empty_string))

    # =================================================================
    # validate_range Tests
    # =================================================================

    def test_validate_range_valid():
        """validate_range should pass for value in range."""
        HTTPClient.validate_range(50, 0, 100, 'percentage')
        HTTPClient.validate_range(0, 0, 100, 'percentage')
        HTTPClient.validate_range(100, 0, 100, 'percentage')
        return True, None

    tests.append(("validate_range valid values", test_validate_range_valid))

    def test_validate_range_below_min():
        """validate_range should raise for value below minimum."""
        try:
            HTTPClient.validate_range(-1, 0, 100, 'percentage')
            return False, "Should raise ValueError for value below min"
        except ValueError as e:
            assert 'percentage' in str(e).lower() or '-1' in str(e)
            return True, None

    tests.append(("validate_range below minimum", test_validate_range_below_min))

    def test_validate_range_above_max():
        """validate_range should raise for value above maximum."""
        try:
            HTTPClient.validate_range(101, 0, 100, 'percentage')
            return False, "Should raise ValueError for value above max"
        except ValueError:
            return True, None

    tests.append(("validate_range above maximum", test_validate_range_above_max))

    def test_validate_range_float():
        """validate_range should work with floats."""
        HTTPClient.validate_range(3.14, 0.0, 10.0, 'value')
        try:
            HTTPClient.validate_range(10.1, 0.0, 10.0, 'value')
            return False, "Should raise ValueError for 10.1 > 10.0"
        except ValueError:
            return True, None

    tests.append(("validate_range with floats", test_validate_range_float))

    def test_validate_range_negative_range():
        """validate_range should work with negative ranges."""
        HTTPClient.validate_range(-50, -100, 0, 'offset')
        HTTPClient.validate_range(-100, -100, 0, 'offset')
        HTTPClient.validate_range(0, -100, 0, 'offset')
        return True, None

    tests.append(("validate_range negative range", test_validate_range_negative_range))

    # =================================================================
    # validate_required_params Tests
    # =================================================================

    def test_validate_required_params_all_present():
        """validate_required_params should pass when all required params present."""
        params = {'name': 'test', 'type': 'ipmask', 'subnet': '10.0.0.0/8'}
        HTTPClient.validate_required_params(params, ['name', 'type'])
        return True, None

    tests.append(("validate_required_params all present", test_validate_required_params_all_present))

    def test_validate_required_params_missing():
        """validate_required_params should raise when required param missing."""
        params = {'name': 'test'}
        try:
            HTTPClient.validate_required_params(params, ['name', 'type'])
            return False, "Should raise ValueError for missing 'type'"
        except ValueError as e:
            assert 'type' in str(e).lower()
            return True, None

    tests.append(("validate_required_params missing param", test_validate_required_params_missing))

    def test_validate_required_params_empty_list():
        """validate_required_params with no requirements should pass."""
        params = {'name': 'test'}
        HTTPClient.validate_required_params(params, [])
        return True, None

    tests.append(("validate_required_params empty requirements", test_validate_required_params_empty_list))

    def test_validate_required_params_none_value():
        """validate_required_params should handle None values."""
        params = {'name': 'test', 'type': None}
        # None value might be considered missing or present depending on implementation
        try:
            HTTPClient.validate_required_params(params, ['name', 'type'])
            # If it passes, None is considered present
            return True, None
        except ValueError:
            # If it fails, None is considered missing
            return True, None

    tests.append(("validate_required_params None value handling", test_validate_required_params_none_value))

    def test_validate_required_params_empty_dict():
        """validate_required_params should fail for empty dict with requirements."""
        try:
            HTTPClient.validate_required_params({}, ['name'])
            return False, "Should raise ValueError for empty dict"
        except ValueError:
            return True, None

    tests.append(("validate_required_params empty dict fails", test_validate_required_params_empty_dict))

    # =================================================================
    # make_exists_method Tests (if it doesn't need connection)
    # =================================================================

    def test_make_exists_method_creates_callable():
        """make_exists_method should return a callable."""
        def mock_get(mkey):
            return {'status': 'success', 'results': [{'name': mkey}]}
        
        exists_method = HTTPClient.make_exists_method(mock_get)
        assert callable(exists_method)
        return True, None

    tests.append(("make_exists_method creates callable", test_make_exists_method_creates_callable))

    def test_make_exists_method_returns_true_on_success():
        """make_exists_method should return True when get succeeds."""
        def mock_get(mkey):
            return {'status': 'success', 'results': [{'name': mkey}]}
        
        exists_method = HTTPClient.make_exists_method(mock_get)
        result = exists_method('test_entry')
        assert result is True
        return True, None

    tests.append(("make_exists_method returns True on success", test_make_exists_method_returns_true_on_success))

    def test_make_exists_method_returns_false_on_error():
        """make_exists_method should return False when get fails."""
        def mock_get(mkey):
            return {'status': 'error', 'error': -3}
        
        exists_method = HTTPClient.make_exists_method(mock_get)
        result = exists_method('nonexistent')
        assert result is False
        return True, None

    tests.append(("make_exists_method returns False on error", test_make_exists_method_returns_false_on_error))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}HTTPClient Utility Methods Tests{Colors.RESET}")
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
