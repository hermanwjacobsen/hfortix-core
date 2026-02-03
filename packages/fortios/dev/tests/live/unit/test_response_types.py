"""
Tests for FortiOS Response TypedDicts.

Tests the response type structures used for API responses:
- FortiOSResponse (base)
- FortiOSSuccessResponse
- FortiOSErrorResponse

These are TypedDicts that define the structure of FortiOS API responses.
"""

import sys
from typing import Any


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
    from hfortix_fortios.types import (
        FortiOSResponse, FortiOSSuccessResponse, FortiOSErrorResponse
    )

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # FortiOSResponse TypedDict Tests
    # =================================================================

    def test_fortios_response_has_required_keys():
        """FortiOSResponse should have http_method and http_status as required."""
        annotations = FortiOSResponse.__annotations__
        assert 'http_method' in annotations
        assert 'http_status' in annotations
        return True, None

    tests.append(("FortiOSResponse has required keys", test_fortios_response_has_required_keys))

    def test_fortios_response_optional_keys():
        """FortiOSResponse should have optional keys for results, status, etc."""
        annotations = FortiOSResponse.__annotations__
        expected_keys = ['results', 'vdom', 'path', 'name', 'status', 'error', 'message', 'build', 'version', 'serial']
        for key in expected_keys:
            if key not in annotations:
                return False, f"Missing optional key: {key}"
        return True, None

    tests.append(("FortiOSResponse has optional keys", test_fortios_response_optional_keys))

    def test_fortios_response_can_be_created():
        """Should be able to create a dict matching FortiOSResponse."""
        response: FortiOSResponse = {
            'http_method': 'GET',
            'http_status': 200,
            'status': 'success',
            'results': [{'name': 'test'}],
            'vdom': 'root',
            'path': 'firewall',
            'serial': 'FGT123456789'
        }
        assert response['http_method'] == 'GET'
        assert response['http_status'] == 200
        return True, None

    tests.append(("FortiOSResponse can be created as dict", test_fortios_response_can_be_created))

    # =================================================================
    # FortiOSSuccessResponse TypedDict Tests
    # =================================================================

    def test_success_response_has_required_keys():
        """FortiOSSuccessResponse should have all required keys for success."""
        annotations = FortiOSSuccessResponse.__annotations__
        required = ['http_method', 'http_status', 'results', 'vdom', 'path', 'status', 'build', 'version', 'serial']
        for key in required:
            if key not in annotations:
                return False, f"Missing required key: {key}"
        return True, None

    tests.append(("FortiOSSuccessResponse has required keys", test_success_response_has_required_keys))

    def test_success_response_status_literal():
        """FortiOSSuccessResponse status should be Literal['success']."""
        annotations = FortiOSSuccessResponse.__annotations__
        status_type = str(annotations.get('status', ''))
        if 'success' not in status_type:
            return False, f"Status type should be Literal['success'], got: {status_type}"
        return True, None

    tests.append(("FortiOSSuccessResponse status is Literal['success']", test_success_response_status_literal))

    def test_success_response_can_be_created():
        """Should be able to create a dict matching FortiOSSuccessResponse."""
        response: FortiOSSuccessResponse = {
            'http_method': 'GET',
            'http_status': 200,
            'status': 'success',
            'results': [{'name': 'policy1', 'policyid': 1}],
            'vdom': 'root',
            'path': 'firewall',
            'build': 1234,
            'version': 'v7.2.0',
            'serial': 'FGT123456789'
        }
        assert response['status'] == 'success'
        assert response['http_status'] == 200
        assert isinstance(response['results'], list)
        return True, None

    tests.append(("FortiOSSuccessResponse can be created", test_success_response_can_be_created))

    def test_success_response_results_types():
        """Results can be list[dict] or dict."""
        # List of dicts (most common)
        response1: FortiOSSuccessResponse = {
            'http_method': 'GET',
            'http_status': 200,
            'status': 'success',
            'results': [{'name': 'a'}, {'name': 'b'}],
            'vdom': 'root',
            'path': 'firewall',
            'build': 1234,
            'version': 'v7.2.0',
            'serial': 'FGT123456789'
        }
        assert isinstance(response1['results'], list)
        
        # Single dict (some endpoints)
        response2: FortiOSSuccessResponse = {
            'http_method': 'GET',
            'http_status': 200,
            'status': 'success',
            'results': {'key': 'value'},  # type: ignore - dict is also valid
            'vdom': 'root',
            'path': 'system',
            'build': 1234,
            'version': 'v7.2.0',
            'serial': 'FGT123456789'
        }
        assert isinstance(response2['results'], dict)
        return True, None

    tests.append(("FortiOSSuccessResponse results can be list or dict", test_success_response_results_types))

    # =================================================================
    # FortiOSErrorResponse TypedDict Tests
    # =================================================================

    def test_error_response_has_required_keys():
        """FortiOSErrorResponse should have error code and http_status."""
        annotations = FortiOSErrorResponse.__annotations__
        required = ['http_method', 'http_status', 'error']
        for key in required:
            if key not in annotations:
                return False, f"Missing required key: {key}"
        return True, None

    tests.append(("FortiOSErrorResponse has required keys", test_error_response_has_required_keys))

    def test_error_response_can_be_created():
        """Should be able to create a dict matching FortiOSErrorResponse."""
        response: FortiOSErrorResponse = {
            'http_method': 'GET',
            'http_status': 404,
            'error': -3,
            'status': 'error',
            'message': 'Entry not found'
        }
        assert response['http_status'] == 404
        assert response['error'] == -3
        return True, None

    tests.append(("FortiOSErrorResponse can be created", test_error_response_can_be_created))

    def test_error_response_common_error_codes():
        """Test common FortiOS error codes can be used."""
        # -3: Entry not found
        error_not_found: FortiOSErrorResponse = {
            'http_method': 'GET',
            'http_status': 404,
            'error': -3,
            'message': 'Entry not found'
        }
        
        # -5: Duplicate entry
        error_duplicate: FortiOSErrorResponse = {
            'http_method': 'POST',
            'http_status': 500,
            'error': -5,
            'message': 'Duplicate entry'
        }
        
        # -6: Entry in use
        error_in_use: FortiOSErrorResponse = {
            'http_method': 'DELETE',
            'http_status': 500,
            'error': -6,
            'message': 'Entry in use'
        }
        
        assert error_not_found['error'] == -3
        assert error_duplicate['error'] == -5
        assert error_in_use['error'] == -6
        return True, None

    tests.append(("FortiOSErrorResponse common error codes", test_error_response_common_error_codes))

    # =================================================================
    # Type Checking Behavior Tests
    # =================================================================

    def test_response_is_typeddict():
        """All response types should be TypedDicts."""
        from typing import is_typeddict
        
        assert is_typeddict(FortiOSResponse), "FortiOSResponse should be TypedDict"
        assert is_typeddict(FortiOSSuccessResponse), "FortiOSSuccessResponse should be TypedDict"
        assert is_typeddict(FortiOSErrorResponse), "FortiOSErrorResponse should be TypedDict"
        return True, None

    tests.append(("Response types are TypedDicts", test_response_is_typeddict))

    def test_response_inheritance():
        """Check if response types have proper structure."""
        # FortiOSResponse should be the base
        base_keys = set(FortiOSResponse.__annotations__.keys())
        success_keys = set(FortiOSSuccessResponse.__annotations__.keys())
        error_keys = set(FortiOSErrorResponse.__annotations__.keys())
        
        # Success and Error should have at least http_method and http_status
        common_required = {'http_method', 'http_status'}
        assert common_required.issubset(base_keys)
        assert common_required.issubset(success_keys)
        assert common_required.issubset(error_keys)
        return True, None

    tests.append(("Response types share common keys", test_response_inheritance))

    # =================================================================
    # Real-world Response Structure Tests
    # =================================================================

    def test_real_world_get_response():
        """Test structure matching real GET response."""
        response: FortiOSSuccessResponse = {
            'http_method': 'GET',
            'http_status': 200,
            'status': 'success',
            'vdom': 'root',
            'path': 'firewall',
            'name': 'address',
            'results': [
                {'name': 'all', 'type': 'ipmask', 'subnet': '0.0.0.0 0.0.0.0'},
                {'name': 'none', 'type': 'ipmask', 'subnet': '255.255.255.255 255.255.255.255'}
            ],
            'build': 2571,
            'version': 'v7.2.8',
            'serial': 'FGVMEV0000000000'
        }
        results = response['results']
        assert isinstance(results, list)
        assert len(results) == 2
        assert results[0]['name'] == 'all'
        return True, None

    tests.append(("Real-world GET response structure", test_real_world_get_response))

    def test_real_world_post_response():
        """Test structure matching real POST response."""
        response: FortiOSSuccessResponse = {
            'http_method': 'POST',
            'http_status': 200,
            'status': 'success',
            'vdom': 'root',
            'path': 'firewall',
            'name': 'address',
            'results': {'mkey': 'new_address'},
            'build': 2571,
            'version': 'v7.2.8',
            'serial': 'FGVMEV0000000000'
        }
        assert response['results']['mkey'] == 'new_address'  # type: ignore
        return True, None

    tests.append(("Real-world POST response structure", test_real_world_post_response))

    def test_real_world_error_response():
        """Test structure matching real error response."""
        response: FortiOSErrorResponse = {
            'http_method': 'DELETE',
            'http_status': 500,
            'status': 'error',
            'error': -6,
            'vdom': 'root',
            'path': 'firewall',
            'message': 'Object is in use by another object'
        }
        assert response['error'] == -6
        assert 'in use' in response.get('message', '')
        return True, None

    tests.append(("Real-world error response structure", test_real_world_error_response))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}FortiOS Response Types Tests{Colors.RESET}")
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
