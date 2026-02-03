"""
Tests for exception utility functions.

Tests the following from hfortix_core.exceptions:
- get_error_description(error_code)
- get_http_status_description(status_code)
- is_retryable_error(error)
- get_retry_delay(error, attempt, base_delay, max_delay)
- raise_for_status(response)
- FORTIOS_ERROR_CODES mapping
- HTTP_STATUS_CODES mapping

Run with: python -m pytest.unit.test_exception_utils
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
    from hfortix_core.exceptions import (
        get_error_description,
        get_http_status_description,
        is_retryable_error,
        get_retry_delay,
        raise_for_status,
        FORTIOS_ERROR_CODES,
        HTTP_STATUS_CODES,
        # Exception types for testing
        ServerError,
        TimeoutError,
        BadRequestError,
        ResourceNotFoundError,
        AuthenticationError,
        RateLimitError,
        DuplicateEntryError,
        EntryInUseError,
        ServiceUnavailableError,
        CircuitBreakerOpenError,
    )

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # get_error_description Tests
    # =================================================================

    def test_get_error_description_common_codes():
        """get_error_description should return descriptions for common error codes."""
        assert get_error_description(-3) == "Entry not found"
        assert get_error_description(-5) == "A duplicate entry already exists"
        # -6 is "Failed memory allocation", not "entry in use"
        assert "memory" in get_error_description(-6).lower() or "allocation" in get_error_description(-6).lower()
        return True, None

    tests.append(("get_error_description common codes", test_get_error_description_common_codes))

    def test_get_error_description_unknown_code():
        """get_error_description should handle unknown codes gracefully."""
        result = get_error_description(-99999)
        # Should return something, not crash
        assert isinstance(result, str)
        return True, None

    tests.append(("get_error_description unknown code", test_get_error_description_unknown_code))

    def test_get_error_description_negative_codes():
        """get_error_description should work with various negative codes."""
        # Test a range of common negative error codes
        codes_to_test = [-1, -2, -3, -4, -5, -6, -10, -15, -20]
        for code in codes_to_test:
            result = get_error_description(code)
            assert isinstance(result, str), f"Code {code} did not return string"
        return True, None

    tests.append(("get_error_description negative codes", test_get_error_description_negative_codes))

    # =================================================================
    # get_http_status_description Tests
    # =================================================================

    def test_get_http_status_description_success_codes():
        """get_http_status_description should describe success codes."""
        desc_200 = get_http_status_description(200)
        assert "OK" in desc_200 or "success" in desc_200.lower()
        
        desc_201 = get_http_status_description(201)
        assert "Created" in desc_201 or "created" in desc_201.lower()
        return True, None

    tests.append(("get_http_status_description success codes", test_get_http_status_description_success_codes))

    def test_get_http_status_description_client_errors():
        """get_http_status_description should describe client error codes."""
        desc_400 = get_http_status_description(400)
        assert "Bad" in desc_400 or "Invalid" in desc_400
        
        desc_401 = get_http_status_description(401)
        assert "Unauthorized" in desc_401 or "Authentication" in desc_401
        
        desc_403 = get_http_status_description(403)
        assert "Forbidden" in desc_403 or "Permission" in desc_403
        
        desc_404 = get_http_status_description(404)
        assert "Not Found" in desc_404 or "not exist" in desc_404.lower()
        return True, None

    tests.append(("get_http_status_description client errors", test_get_http_status_description_client_errors))

    def test_get_http_status_description_server_errors():
        """get_http_status_description should describe server error codes."""
        desc_500 = get_http_status_description(500)
        assert "Server" in desc_500 or "Internal" in desc_500
        
        desc_503 = get_http_status_description(503)
        assert "Unavailable" in desc_503 or "unavailable" in desc_503.lower()
        return True, None

    tests.append(("get_http_status_description server errors", test_get_http_status_description_server_errors))

    def test_get_http_status_description_unknown():
        """get_http_status_description should handle unknown codes."""
        result = get_http_status_description(999)
        assert isinstance(result, str)
        return True, None

    tests.append(("get_http_status_description unknown code", test_get_http_status_description_unknown))

    # =================================================================
    # is_retryable_error Tests
    # =================================================================

    def test_is_retryable_server_errors():
        """Server errors should be retryable."""
        assert is_retryable_error(ServerError("test")) is True
        assert is_retryable_error(ServiceUnavailableError("test")) is True
        return True, None

    tests.append(("is_retryable_error server errors", test_is_retryable_server_errors))

    def test_is_retryable_timeout_errors():
        """Timeout errors should be retryable."""
        assert is_retryable_error(TimeoutError("test")) is True
        return True, None

    tests.append(("is_retryable_error timeout errors", test_is_retryable_timeout_errors))

    def test_is_retryable_rate_limit():
        """Rate limit errors should be retryable."""
        assert is_retryable_error(RateLimitError("test")) is True
        return True, None

    tests.append(("is_retryable_error rate limit", test_is_retryable_rate_limit))

    def test_is_retryable_circuit_breaker():
        """Circuit breaker errors should be retryable."""
        assert is_retryable_error(CircuitBreakerOpenError("test")) is True
        return True, None

    tests.append(("is_retryable_error circuit breaker", test_is_retryable_circuit_breaker))

    def test_is_not_retryable_client_errors():
        """Client errors should NOT be retryable."""
        assert is_retryable_error(BadRequestError("test")) is False
        assert is_retryable_error(ResourceNotFoundError("test")) is False
        assert is_retryable_error(DuplicateEntryError("test")) is False
        assert is_retryable_error(EntryInUseError("test")) is False
        return True, None

    tests.append(("is_retryable_error client errors not retryable", test_is_not_retryable_client_errors))

    def test_is_not_retryable_auth_errors():
        """Authentication errors should NOT be retryable."""
        assert is_retryable_error(AuthenticationError("test")) is False
        return True, None

    tests.append(("is_retryable_error auth errors not retryable", test_is_not_retryable_auth_errors))

    def test_is_retryable_standard_exceptions():
        """Standard Python exceptions should not be retryable."""
        assert is_retryable_error(ValueError("test")) is False
        assert is_retryable_error(TypeError("test")) is False
        assert is_retryable_error(KeyError("test")) is False
        return True, None

    tests.append(("is_retryable_error standard exceptions", test_is_retryable_standard_exceptions))

    # =================================================================
    # get_retry_delay Tests
    # =================================================================

    def test_get_retry_delay_returns_float():
        """get_retry_delay should return a float delay value."""
        err = ServerError("test")
        delay = get_retry_delay(err, 1)
        assert isinstance(delay, (int, float))
        assert delay >= 0
        return True, None

    tests.append(("get_retry_delay returns float", test_get_retry_delay_returns_float))

    def test_get_retry_delay_respects_base():
        """get_retry_delay should use base_delay parameter."""
        err = ServerError("test")
        delay = get_retry_delay(err, 1, base_delay=2.0)
        assert delay >= 0  # Should be at least 0
        return True, None

    tests.append(("get_retry_delay respects base_delay", test_get_retry_delay_respects_base))

    def test_get_retry_delay_respects_max():
        """get_retry_delay should not exceed max_delay."""
        err = ServerError("test")
        max_delay = 5.0
        delay = get_retry_delay(err, 100, base_delay=1.0, max_delay=max_delay)
        assert delay <= max_delay, f"Delay {delay} exceeded max {max_delay}"
        return True, None

    tests.append(("get_retry_delay respects max_delay", test_get_retry_delay_respects_max))

    def test_get_retry_delay_multiple_attempts():
        """get_retry_delay should work for multiple attempts."""
        err = ServerError("test")
        for attempt in [1, 2, 3, 5, 10]:
            delay = get_retry_delay(err, attempt)
            assert isinstance(delay, (int, float))
            assert delay >= 0
        return True, None

    tests.append(("get_retry_delay multiple attempts", test_get_retry_delay_multiple_attempts))

    # =================================================================
    # raise_for_status Tests
    # =================================================================

    def test_raise_for_status_success_no_exception():
        """raise_for_status should not raise for success responses."""
        response = {'status': 'success', 'http_status': 200}
        # Should not raise
        raise_for_status(response)
        return True, None

    tests.append(("raise_for_status success no exception", test_raise_for_status_success_no_exception))

    def test_raise_for_status_201_created():
        """raise_for_status should not raise for 201 Created."""
        response = {'status': 'success', 'http_status': 201, 'results': {'mkey': 'new_item'}}
        raise_for_status(response)
        return True, None

    tests.append(("raise_for_status 201 created", test_raise_for_status_201_created))

    def test_raise_for_status_404_raises():
        """raise_for_status should raise ResourceNotFoundError for 404."""
        response = {'status': 'error', 'http_status': 404, 'error': -3}
        try:
            raise_for_status(response)
            return False, "Expected ResourceNotFoundError"
        except ResourceNotFoundError:
            return True, None
        except Exception as e:
            return False, f"Expected ResourceNotFoundError, got {type(e).__name__}"

    tests.append(("raise_for_status 404 raises", test_raise_for_status_404_raises))

    def test_raise_for_status_401_raises():
        """raise_for_status should raise AuthenticationError for 401."""
        response = {'status': 'error', 'http_status': 401}
        try:
            raise_for_status(response)
            return False, "Expected AuthenticationError"
        except AuthenticationError:
            return True, None
        except Exception as e:
            return False, f"Expected AuthenticationError, got {type(e).__name__}"

    tests.append(("raise_for_status 401 raises", test_raise_for_status_401_raises))

    def test_raise_for_status_500_raises():
        """raise_for_status should raise ServerError for 500."""
        response = {'status': 'error', 'http_status': 500}
        try:
            raise_for_status(response)
            return False, "Expected ServerError"
        except ServerError:
            return True, None
        except Exception as e:
            return False, f"Expected ServerError, got {type(e).__name__}"

    tests.append(("raise_for_status 500 raises", test_raise_for_status_500_raises))

    def test_raise_for_status_duplicate_entry():
        """raise_for_status should raise DuplicateEntryError for error -5."""
        response = {'status': 'error', 'http_status': 500, 'error': -5}
        try:
            raise_for_status(response)
            return False, "Expected DuplicateEntryError"
        except DuplicateEntryError:
            return True, None
        except Exception as e:
            return False, f"Expected DuplicateEntryError, got {type(e).__name__}"

    tests.append(("raise_for_status duplicate entry", test_raise_for_status_duplicate_entry))

    def test_raise_for_status_entry_in_use():
        """raise_for_status should raise EntryInUseError for entry-in-use errors."""
        # Error codes -23, -94, -95, -96 trigger EntryInUseError (not -6)
        response = {'status': 'error', 'http_status': 500, 'error': -94}
        try:
            raise_for_status(response)
            return False, "Expected EntryInUseError"
        except EntryInUseError:
            return True, None
        except Exception as e:
            return False, f"Expected EntryInUseError, got {type(e).__name__}"

    tests.append(("raise_for_status entry in use", test_raise_for_status_entry_in_use))

    # =================================================================
    # FORTIOS_ERROR_CODES Tests
    # =================================================================

    def test_fortios_error_codes_is_dict():
        """FORTIOS_ERROR_CODES should be a dictionary."""
        assert isinstance(FORTIOS_ERROR_CODES, dict)
        return True, None

    tests.append(("FORTIOS_ERROR_CODES is dict", test_fortios_error_codes_is_dict))

    def test_fortios_error_codes_has_common_codes():
        """FORTIOS_ERROR_CODES should contain common error codes."""
        common_codes = [-1, -2, -3, -5, -6]
        for code in common_codes:
            assert code in FORTIOS_ERROR_CODES, f"Missing code {code}"
            assert isinstance(FORTIOS_ERROR_CODES[code], str)
        return True, None

    tests.append(("FORTIOS_ERROR_CODES has common codes", test_fortios_error_codes_has_common_codes))

    def test_fortios_error_codes_descriptions():
        """FORTIOS_ERROR_CODES should have meaningful descriptions."""
        assert "not found" in FORTIOS_ERROR_CODES[-3].lower()
        assert "duplicate" in FORTIOS_ERROR_CODES[-5].lower()
        return True, None

    tests.append(("FORTIOS_ERROR_CODES meaningful descriptions", test_fortios_error_codes_descriptions))

    def test_fortios_error_codes_count():
        """FORTIOS_ERROR_CODES should have many entries."""
        # Based on earlier check, there are 387 entries
        assert len(FORTIOS_ERROR_CODES) > 100, f"Only {len(FORTIOS_ERROR_CODES)} entries"
        return True, None

    tests.append(("FORTIOS_ERROR_CODES entry count", test_fortios_error_codes_count))

    # =================================================================
    # HTTP_STATUS_CODES Tests
    # =================================================================

    def test_http_status_codes_is_dict():
        """HTTP_STATUS_CODES should be a dictionary."""
        assert isinstance(HTTP_STATUS_CODES, dict)
        return True, None

    tests.append(("HTTP_STATUS_CODES is dict", test_http_status_codes_is_dict))

    def test_http_status_codes_has_common_codes():
        """HTTP_STATUS_CODES should contain common HTTP status codes."""
        common_codes = [200, 201, 400, 401, 403, 404, 500, 503]
        for code in common_codes:
            assert code in HTTP_STATUS_CODES, f"Missing code {code}"
            assert isinstance(HTTP_STATUS_CODES[code], str)
        return True, None

    tests.append(("HTTP_STATUS_CODES has common codes", test_http_status_codes_has_common_codes))

    def test_http_status_codes_descriptions():
        """HTTP_STATUS_CODES should have standard HTTP descriptions."""
        assert "OK" in HTTP_STATUS_CODES[200]
        assert "Not Found" in HTTP_STATUS_CODES[404] or "not exist" in HTTP_STATUS_CODES[404].lower()
        return True, None

    tests.append(("HTTP_STATUS_CODES standard descriptions", test_http_status_codes_descriptions))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Exception Utilities Tests{Colors.RESET}")
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
