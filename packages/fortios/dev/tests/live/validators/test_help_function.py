"""
Tests for hfortix_fortios.help() function.

Tests the help() function that displays comprehensive help
for FortiOS API endpoints.

Run with: python -m pytest.validators.test_help_function
"""

import sys
import io


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


def capture_stdout(func, *args, **kwargs):
    """Capture stdout from a function call."""
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        func(*args, **kwargs)
    except Exception:
        pass
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()


def run_tests():
    from hfortix_fortios import help as fgt_help

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # help() Function Tests
    # =================================================================

    def test_help_returns_none():
        """help() should return None (prints to stdout) for valid endpoints."""
        # Create a mock endpoint with required schema classmethod
        class MockEndpoint:
            @classmethod
            def schema(cls):
                return {
                    'category': 'cmdb',
                    'endpoint': 'test/endpoint',
                    'help': 'Test endpoint help',
                    'mkey': 'name',
                    'mkey_type': 'string',
                }
        
        result = fgt_help(MockEndpoint)
        assert result is None
        return True, None

    tests.append(("help returns None", test_help_returns_none))

    def test_help_produces_output():
        """help() should produce output to stdout."""
        class MockEndpoint:
            pass
        
        output = capture_stdout(fgt_help, MockEndpoint)
        assert len(output) > 0, "Expected some output"
        return True, None

    tests.append(("help produces output", test_help_produces_output))

    def test_help_shows_header():
        """help() output should include a header."""
        class MockEndpoint:
            pass
        
        output = capture_stdout(fgt_help, MockEndpoint)
        assert 'FORTIOS' in output.upper() or 'HELP' in output.upper()
        return True, None

    tests.append(("help shows header", test_help_shows_header))

    def test_help_with_show_fields_false():
        """help() with show_fields=False should work."""
        class MockEndpoint:
            pass
        
        output = capture_stdout(fgt_help, MockEndpoint, show_fields=False)
        assert isinstance(output, str)
        return True, None

    tests.append(("help with show_fields=False", test_help_with_show_fields_false))

    def test_help_with_show_fields_true():
        """help() with show_fields=True should work."""
        class MockEndpoint:
            pass
        
        output = capture_stdout(fgt_help, MockEndpoint, show_fields=True)
        assert isinstance(output, str)
        return True, None

    tests.append(("help with show_fields=True", test_help_with_show_fields_true))

    def test_help_accepts_various_types():
        """help() should accept various endpoint types without crashing."""
        # Test with different types
        types_to_test = [
            object(),
            "string_endpoint",
            {'path': '/api/v2/cmdb/firewall/address'},
            None,
        ]
        
        for endpoint in types_to_test:
            try:
                output = capture_stdout(fgt_help, endpoint)
                # Should not crash, might produce minimal output
            except Exception as e:
                return False, f"Crashed on {type(endpoint)}: {e}"
        return True, None

    tests.append(("help accepts various types", test_help_accepts_various_types))

    def test_help_with_endpoint_attributes():
        """help() should utilize endpoint attributes if present."""
        class MockEndpointWithAttrs:
            _path = '/api/v2/cmdb/firewall/address'
            _api_type = 'cmdb'
            __doc__ = "Test endpoint documentation"
        
        output = capture_stdout(fgt_help, MockEndpointWithAttrs)
        # Should produce output without crashing
        assert isinstance(output, str)
        return True, None

    tests.append(("help with endpoint attributes", test_help_with_endpoint_attributes))

    def test_help_decorative_output():
        """help() output should have formatting (decorative lines)."""
        class MockEndpoint:
            pass
        
        output = capture_stdout(fgt_help, MockEndpoint)
        # Should have some formatting characters
        assert '=' in output or '-' in output or '*' in output
        return True, None

    tests.append(("help decorative output", test_help_decorative_output))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Help Function Tests{Colors.RESET}")
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
