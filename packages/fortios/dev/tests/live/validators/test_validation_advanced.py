"""
Tests for advanced validation functions.

Tests the following from hfortix_fortios._helpers.validation:
- validate_multiple_enums(payload, enum_fields, field_descriptions)
- validate_multiple_query_params(params, valid_params)

Run with: python -m pytest.validators.test_validation_advanced
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
    from hfortix_fortios._helpers.validation import (
        validate_multiple_enums,
        validate_multiple_query_params,
    )

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # validate_multiple_enums Tests
    # =================================================================

    def test_validate_multiple_enums_all_valid():
        """validate_multiple_enums should pass when all values are valid."""
        payload = {'status': 'enable', 'type': 'ipmask'}
        enum_fields = {
            'status': ['enable', 'disable'],
            'type': ['ipmask', 'iprange', 'fqdn', 'wildcard'],
        }
        descriptions = {'status': 'Status setting', 'type': 'Address type'}
        
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        assert is_valid is True, f"Expected valid, got error: {error}"
        assert error is None
        return True, None

    tests.append(("validate_multiple_enums all valid", test_validate_multiple_enums_all_valid))

    def test_validate_multiple_enums_invalid_value():
        """validate_multiple_enums should fail when a value is invalid."""
        payload = {'status': 'invalid_status', 'type': 'ipmask'}
        enum_fields = {
            'status': ['enable', 'disable'],
            'type': ['ipmask', 'iprange', 'fqdn'],
        }
        descriptions = {'status': 'Status setting', 'type': 'Address type'}
        
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        assert is_valid is False
        assert error is not None
        assert 'invalid_status' in error.lower() or 'status' in error.lower()
        return True, None

    tests.append(("validate_multiple_enums invalid value", test_validate_multiple_enums_invalid_value))

    def test_validate_multiple_enums_missing_field():
        """validate_multiple_enums should handle missing fields gracefully."""
        payload = {'status': 'enable'}  # Missing 'type'
        enum_fields = {
            'status': ['enable', 'disable'],
            'type': ['ipmask', 'iprange'],
        }
        descriptions = {'status': 'Status', 'type': 'Type'}
        
        # Should not crash - missing fields are typically OK
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        # If missing fields are allowed, is_valid should be True
        assert isinstance(is_valid, bool)
        return True, None

    tests.append(("validate_multiple_enums missing field", test_validate_multiple_enums_missing_field))

    def test_validate_multiple_enums_empty_payload():
        """validate_multiple_enums should handle empty payload."""
        payload = {}
        enum_fields = {'status': ['enable', 'disable']}
        descriptions = {'status': 'Status'}
        
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        assert isinstance(is_valid, bool)
        return True, None

    tests.append(("validate_multiple_enums empty payload", test_validate_multiple_enums_empty_payload))

    def test_validate_multiple_enums_error_includes_options():
        """validate_multiple_enums error should include valid options."""
        payload = {'status': 'bad_value'}
        enum_fields = {'status': ['enable', 'disable']}
        descriptions = {'status': 'Status setting'}
        
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        assert is_valid is False
        assert error is not None
        # Error should mention valid options
        assert 'enable' in error or 'disable' in error
        return True, None

    tests.append(("validate_multiple_enums error includes options", test_validate_multiple_enums_error_includes_options))

    def test_validate_multiple_enums_single_field():
        """validate_multiple_enums should work with single field."""
        payload = {'visibility': 'enable'}
        enum_fields = {'visibility': ['enable', 'disable']}
        descriptions = {'visibility': 'Show in GUI'}
        
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        assert is_valid is True
        return True, None

    tests.append(("validate_multiple_enums single field", test_validate_multiple_enums_single_field))

    def test_validate_multiple_enums_many_options():
        """validate_multiple_enums should handle many options."""
        payload = {'color': '5'}
        enum_fields = {'color': [str(i) for i in range(33)]}  # 0-32
        descriptions = {'color': 'Icon color'}
        
        is_valid, error = validate_multiple_enums(payload, enum_fields, descriptions)
        assert is_valid is True
        return True, None

    tests.append(("validate_multiple_enums many options", test_validate_multiple_enums_many_options))

    # =================================================================
    # validate_multiple_query_params Tests
    # =================================================================

    def test_validate_multiple_query_params_valid():
        """validate_multiple_query_params should pass valid params."""
        params = {'format': 'json'}
        valid_params = {'format': ['json', 'xml']}
        
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert is_valid is True
        assert error is None
        return True, None

    tests.append(("validate_multiple_query_params valid", test_validate_multiple_query_params_valid))

    def test_validate_multiple_query_params_invalid():
        """validate_multiple_query_params should fail invalid params."""
        params = {'format': 'csv'}
        valid_params = {'format': ['json', 'xml']}
        
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert is_valid is False
        assert error is not None
        assert 'csv' in error or 'format' in error
        return True, None

    tests.append(("validate_multiple_query_params invalid", test_validate_multiple_query_params_invalid))

    def test_validate_multiple_query_params_multiple_valid():
        """validate_multiple_query_params should handle multiple valid params."""
        params = {'format': 'json', 'vdom': 'root'}
        valid_params = {
            'format': ['json', 'xml'],
            'vdom': ['root', 'vdom1', 'vdom2'],
        }
        
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert is_valid is True
        return True, None

    tests.append(("validate_multiple_query_params multiple valid", test_validate_multiple_query_params_multiple_valid))

    def test_validate_multiple_query_params_one_invalid():
        """validate_multiple_query_params should fail if any param is invalid."""
        params = {'format': 'json', 'vdom': 'invalid_vdom'}
        valid_params = {
            'format': ['json', 'xml'],
            'vdom': ['root', 'vdom1'],
        }
        
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert is_valid is False
        assert error is not None
        return True, None

    tests.append(("validate_multiple_query_params one invalid", test_validate_multiple_query_params_one_invalid))

    def test_validate_multiple_query_params_empty():
        """validate_multiple_query_params should handle empty params."""
        params = {}
        valid_params = {'format': ['json', 'xml']}
        
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert is_valid is True  # Empty params should be valid
        return True, None

    tests.append(("validate_multiple_query_params empty", test_validate_multiple_query_params_empty))

    def test_validate_multiple_query_params_unknown_param():
        """validate_multiple_query_params should handle unknown params."""
        params = {'unknown_param': 'value'}
        valid_params = {'format': ['json', 'xml']}
        
        # Unknown params should either be ignored or cause validation to pass
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert isinstance(is_valid, bool)
        return True, None

    tests.append(("validate_multiple_query_params unknown param", test_validate_multiple_query_params_unknown_param))

    def test_validate_multiple_query_params_error_shows_valid():
        """validate_multiple_query_params error should show valid options."""
        params = {'format': 'yaml'}
        valid_params = {'format': ['json', 'xml']}
        
        is_valid, error = validate_multiple_query_params(params, valid_params)
        assert is_valid is False
        assert error is not None
        # Error should include valid options
        assert 'json' in error or 'xml' in error
        return True, None

    tests.append(("validate_multiple_query_params error shows valid", test_validate_multiple_query_params_error_shows_valid))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Advanced Validation Tests{Colors.RESET}")
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
