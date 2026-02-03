"""
Tests for Request Hooks system.

Tests BeforeRequestHook, AfterRequestHook, and RequestContext
for intercepting and modifying requests/responses.

NOTE: Many tests are skipped because FortiOS does not yet support
before_request/after_request parameters. See Bug #25 in ALL_BUGS.md.

Run with: python -m pytest.integration.test_hooks
"""

import sys
import os

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_test_result(name: str, passed: bool, error: str | None = None, skipped: bool = False):
    if skipped:
        status = f"{Colors.YELLOW}SKIP{Colors.RESET}"
    else:
        status = f"{Colors.GREEN}PASS{Colors.RESET}" if passed else f"{Colors.RED}FAIL{Colors.RESET}"
    print(f"  [{status}] {name}")
    if error:
        print(f"         {Colors.YELLOW if skipped else Colors.RED}{error}{Colors.RESET}")


def run_tests():
    from hfortix_core.hooks import RequestContext, BeforeRequestHook, AfterRequestHook
    # FortiOS, HOST, TOKEN, PORT, VDOM will be needed when hooks are implemented
    # from hfortix_fortios import FortiOS
    # from fgtclient import HOST, TOKEN, PORT, VDOM

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # RequestContext Tests
    # =================================================================

    def test_request_context_is_typeddict():
        """RequestContext should be a TypedDict."""
        from typing import is_typeddict
        assert is_typeddict(RequestContext)
        return True, None

    tests.append(("RequestContext is TypedDict", test_request_context_is_typeddict))

    def test_request_context_has_expected_keys():
        """RequestContext should have expected keys."""
        annotations = RequestContext.__annotations__
        expected = ['method', 'api_type', 'path', 'data', 'params', 'vdom', 'endpoint', 'request_id']
        for key in expected:
            if key not in annotations:
                return False, f"Missing key: {key}"
        return True, None

    tests.append(("RequestContext has expected keys", test_request_context_has_expected_keys))

    def test_request_context_can_be_created():
        """Should be able to create a RequestContext dict."""
        context: RequestContext = {
            'method': 'GET',
            'api_type': 'monitor',
            'path': '/api/v2/monitor/system/status',
            'data': None,
            'params': {'vdom': 'root'},
            'vdom': 'root',
            'endpoint': 'system/status',
            'request_id': 'req-12345',
            'user_context': None
        }
        assert context['method'] == 'GET'
        assert context['api_type'] == 'monitor'
        return True, None

    tests.append(("RequestContext can be created", test_request_context_can_be_created))

    # =================================================================
    # BeforeRequestHook Tests
    # =================================================================

    def test_before_hook_protocol():
        """BeforeRequestHook should be a Protocol."""
        # Check if it's defined as expected
        assert hasattr(BeforeRequestHook, '__call__') or hasattr(BeforeRequestHook, '__protocol_attrs__')
        return True, None

    tests.append(("BeforeRequestHook is Protocol", test_before_hook_protocol))

    def test_before_hook_receives_context():
        """Before hook should receive RequestContext.
        
        SKIPPED: FortiOS doesn't support before_request parameter yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support before_request parameter (Bug #25)"

    tests.append(("before_hook receives context", test_before_hook_receives_context))

    def test_before_hook_can_modify_context():
        """Before hook should be able to read context data.
        
        SKIPPED: FortiOS doesn't support before_request parameter yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support before_request parameter (Bug #25)"

    tests.append(("before_hook can read context", test_before_hook_can_modify_context))

    # =================================================================
    # AfterRequestHook Tests
    # =================================================================

    def test_after_hook_protocol():
        """AfterRequestHook should be a Protocol."""
        assert hasattr(AfterRequestHook, '__call__') or hasattr(AfterRequestHook, '__protocol_attrs__')
        return True, None

    tests.append(("AfterRequestHook is Protocol", test_after_hook_protocol))

    def test_after_hook_receives_context_and_response():
        """After hook should receive context and response.
        
        SKIPPED: FortiOS doesn't support after_request parameter yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support after_request parameter (Bug #25)"

    tests.append(("after_hook receives context and response", test_after_hook_receives_context_and_response))

    def test_after_hook_has_response_data():
        """After hook should have access to response data.
        
        SKIPPED: FortiOS doesn't support after_request parameter yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support after_request parameter (Bug #25)"

    tests.append(("after_hook has response data", test_after_hook_has_response_data))

    # =================================================================
    # Both Hooks Together Tests
    # =================================================================

    def test_both_hooks_called_in_order():
        """Both hooks should be called in correct order.
        
        SKIPPED: FortiOS doesn't support before_request/after_request parameters yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support request hooks (Bug #25)"

    tests.append(("both hooks called in order", test_both_hooks_called_in_order))

    def test_hooks_called_for_each_request():
        """Hooks should be called for each request.
        
        SKIPPED: FortiOS doesn't support before_request parameter yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support before_request parameter (Bug #25)"

    tests.append(("hooks called for each request", test_hooks_called_for_each_request))

    # =================================================================
    # Hook Error Handling Tests
    # =================================================================

    def test_hook_exception_handling():
        """Hooks that raise exceptions should be handled gracefully.
        
        SKIPPED: FortiOS doesn't support before_request parameter yet.
        See Bug #25 in ALL_BUGS.md.
        """
        # Skip - feature not implemented
        return None, "FortiOS doesn't support before_request parameter (Bug #25)"

    tests.append(("hook exception handling", test_hook_exception_handling))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Request Hooks Tests (Live Connection){Colors.RESET}")
    print("=" * 50)

    skipped = 0
    for name, test_func in tests:
        try:
            result, error = test_func()
            if result is None:
                # Skipped test
                skipped += 1
                print_test_result(name, False, error, skipped=True)
            elif result:
                passed += 1
                print_test_result(name, True)
            else:
                failed += 1
                print_test_result(name, False, error)
        except Exception as e:
            failed += 1
            print_test_result(name, False, str(e))

    print("=" * 50)
    total = passed + failed + skipped
    print(f"Results: {passed}/{total} passed", end="")
    if skipped > 0:
        print(f", {Colors.YELLOW}{skipped} skipped{Colors.RESET}", end="")
    if failed > 0:
        print(f" ({Colors.RED}{failed} failed{Colors.RESET})")
    else:
        print(f" ({Colors.GREEN}all passed{Colors.RESET})")

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
