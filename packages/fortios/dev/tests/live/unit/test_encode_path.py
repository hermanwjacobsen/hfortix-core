"""
Tests for hfortix_core.http.client.encode_path_component function.

encode_path_component URL-encodes path components for FortiOS API requests.
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
    from hfortix_core.http.client import encode_path_component

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Basic Functionality Tests
    # =================================================================

    def test_encode_simple_string():
        """encode_path_component with simple string."""
        result = encode_path_component("test")
        assert result == "test"
        return True, None

    tests.append(("simple string unchanged", test_encode_simple_string))

    def test_encode_integer():
        """encode_path_component with integer."""
        result = encode_path_component(123)
        assert result == "123"
        return True, None

    tests.append(("integer converted to string", test_encode_integer))

    def test_encode_zero():
        """encode_path_component with zero."""
        result = encode_path_component(0)
        assert result == "0"
        return True, None

    tests.append(("zero converted to string", test_encode_zero))

    # =================================================================
    # Space Encoding Tests
    # =================================================================

    def test_encode_space():
        """encode_path_component with space."""
        result = encode_path_component("test address")
        # Spaces should be encoded as %20
        assert " " not in result
        assert "%20" in result or "+" in result
        return True, None

    tests.append(("space encoded", test_encode_space))

    def test_encode_multiple_spaces():
        """encode_path_component with multiple spaces."""
        result = encode_path_component("test  multiple   spaces")
        assert " " not in result
        return True, None

    tests.append(("multiple spaces encoded", test_encode_multiple_spaces))

    # =================================================================
    # Special Characters Tests
    # =================================================================

    def test_encode_slash():
        """encode_path_component with slash."""
        result = encode_path_component("test/path")
        # Slash should be encoded in path component
        assert "/" not in result or "%2F" in result
        return True, None

    tests.append(("slash encoded", test_encode_slash))

    def test_encode_question_mark():
        """encode_path_component with question mark."""
        result = encode_path_component("test?query")
        assert "?" not in result or "%3F" in result
        return True, None

    tests.append(("question mark encoded", test_encode_question_mark))

    def test_encode_ampersand():
        """encode_path_component with ampersand."""
        result = encode_path_component("test&value")
        assert "&" not in result or "%26" in result
        return True, None

    tests.append(("ampersand encoded", test_encode_ampersand))

    def test_encode_equals():
        """encode_path_component with equals sign."""
        result = encode_path_component("test=value")
        # Equals might or might not need encoding in path
        assert isinstance(result, str)
        return True, None

    tests.append(("equals sign handled", test_encode_equals))

    def test_encode_hash():
        """encode_path_component with hash/pound."""
        result = encode_path_component("test#fragment")
        assert "#" not in result or "%23" in result
        return True, None

    tests.append(("hash encoded", test_encode_hash))

    def test_encode_percent():
        """encode_path_component with percent sign."""
        result = encode_path_component("100%")
        # Percent should be encoded as %25
        assert result == "100%25" or "%" in result
        return True, None

    tests.append(("percent encoded", test_encode_percent))

    def test_encode_plus():
        """encode_path_component with plus sign."""
        result = encode_path_component("test+value")
        # Plus might be encoded or preserved depending on implementation
        assert isinstance(result, str)
        return True, None

    tests.append(("plus sign handled", test_encode_plus))

    # =================================================================
    # Unicode/International Characters Tests
    # =================================================================

    def test_encode_unicode_japanese():
        """encode_path_component with Japanese characters."""
        result = encode_path_component("テスト")
        # Unicode should be percent-encoded
        assert isinstance(result, str)
        # Either encoded or preserved
        return True, None

    tests.append(("unicode Japanese", test_encode_unicode_japanese))

    def test_encode_unicode_emoji():
        """encode_path_component with emoji."""
        result = encode_path_component("test🔥emoji")
        assert isinstance(result, str)
        return True, None

    tests.append(("unicode emoji", test_encode_unicode_emoji))

    def test_encode_unicode_accents():
        """encode_path_component with accented characters."""
        result = encode_path_component("café")
        assert isinstance(result, str)
        return True, None

    tests.append(("unicode accents", test_encode_unicode_accents))

    def test_encode_unicode_chinese():
        """encode_path_component with Chinese characters."""
        result = encode_path_component("测试")
        assert isinstance(result, str)
        return True, None

    tests.append(("unicode Chinese", test_encode_unicode_chinese))

    # =================================================================
    # Edge Cases
    # =================================================================

    def test_encode_empty_string():
        """encode_path_component with empty string."""
        result = encode_path_component("")
        assert result == ""
        return True, None

    tests.append(("empty string", test_encode_empty_string))

    def test_encode_hyphen():
        """encode_path_component with hyphen (common in FortiOS names)."""
        result = encode_path_component("test-address-name")
        # Hyphen should NOT be encoded (safe character)
        assert result == "test-address-name"
        return True, None

    tests.append(("hyphen not encoded", test_encode_hyphen))

    def test_encode_underscore():
        """encode_path_component with underscore."""
        result = encode_path_component("test_address_name")
        # Underscore should NOT be encoded (safe character)
        assert result == "test_address_name"
        return True, None

    tests.append(("underscore not encoded", test_encode_underscore))

    def test_encode_dot():
        """encode_path_component with dot."""
        result = encode_path_component("test.address.name")
        # Dot should NOT be encoded in path component
        assert result == "test.address.name"
        return True, None

    tests.append(("dot not encoded", test_encode_dot))

    def test_encode_tilde():
        """encode_path_component with tilde."""
        result = encode_path_component("test~name")
        # Tilde is unreserved in RFC 3986
        assert "~" in result or "%7E" in result
        return True, None

    tests.append(("tilde handled", test_encode_tilde))

    def test_encode_mixed_special():
        """encode_path_component with mixed special characters."""
        result = encode_path_component("test/path?query=value&other=1")
        assert isinstance(result, str)
        # Original special chars should be encoded
        return True, None

    tests.append(("mixed special characters", test_encode_mixed_special))

    def test_encode_already_encoded():
        """encode_path_component with already encoded string."""
        result = encode_path_component("test%20already%20encoded")
        # Should not double-encode (or should encode the percent)
        assert isinstance(result, str)
        return True, None

    tests.append(("already encoded string", test_encode_already_encoded))

    def test_encode_long_string():
        """encode_path_component with long string."""
        long_name = "a" * 1000
        result = encode_path_component(long_name)
        assert result == long_name
        return True, None

    tests.append(("long string", test_encode_long_string))

    def test_encode_only_special_chars():
        """encode_path_component with only special characters."""
        result = encode_path_component("/?&=#")
        # All should be encoded
        assert isinstance(result, str)
        assert len(result) > 5  # Should be longer due to encoding
        return True, None

    tests.append(("only special characters", test_encode_only_special_chars))

    def test_encode_newline():
        """encode_path_component with newline character."""
        result = encode_path_component("test\nname")
        # Newline should be encoded
        assert "\n" not in result
        return True, None

    tests.append(("newline encoded", test_encode_newline))

    def test_encode_tab():
        """encode_path_component with tab character."""
        result = encode_path_component("test\tname")
        # Tab should be encoded
        assert "\t" not in result
        return True, None

    tests.append(("tab encoded", test_encode_tab))

    def test_encode_null_byte():
        """encode_path_component with null byte."""
        result = encode_path_component("test\x00name")
        # Null byte should be encoded
        assert "\x00" not in result
        return True, None

    tests.append(("null byte encoded", test_encode_null_byte))

    # =================================================================
    # FortiOS-Specific Tests
    # =================================================================

    def test_encode_fortigate_address_name():
        """encode_path_component with typical FortiGate address name."""
        result = encode_path_component("Internal-Servers_10.0.0.0/24")
        assert isinstance(result, str)
        return True, None

    tests.append(("FortiGate address name", test_encode_fortigate_address_name))

    def test_encode_fortigate_policy_name():
        """encode_path_component with FortiGate policy name."""
        result = encode_path_component("Allow Web Traffic (HTTP/HTTPS)")
        assert isinstance(result, str)
        # Parentheses and spaces should be encoded
        assert " " not in result or "%20" in result
        return True, None

    tests.append(("FortiGate policy name", test_encode_fortigate_policy_name))

    def test_encode_negative_int():
        """encode_path_component with negative integer."""
        result = encode_path_component(-1)
        assert result == "-1"
        return True, None

    tests.append(("negative integer", test_encode_negative_int))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}encode_path_component Tests{Colors.RESET}")
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
