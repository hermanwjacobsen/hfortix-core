"""
Tests for hfortix_fortios._helpers.validators module.

Input validation functions for FortiOS API parameters.

BUGS FOUND:
- BUG #6: validate_port_number allows ports 0-4294967295 (should be 0-65535)
  Valid TCP/UDP ports are 0-65535, but the validator accepts up to 4 billion.
  FIX: Change max from 4294967295 to 65535
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
    from hfortix_fortios._helpers.validators import (
        validate_ip_address, validate_mac_address, validate_port_number,
        validate_integer_range, validate_enable_disable, validate_color,
        validate_string_length, validate_time_format, validate_policy_id,
        validate_ip_network, validate_ipv6_address, validate_status
    )

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # validate_ip_address Tests
    # =================================================================

    def test_ip_address_valid():
        validate_ip_address("192.168.1.1")
        validate_ip_address("10.0.0.1")
        validate_ip_address("255.255.255.255")
        validate_ip_address("0.0.0.0")
        return True, None

    tests.append(("validate_ip_address valid IPs", test_ip_address_valid))

    def test_ip_address_invalid():
        try:
            validate_ip_address("invalid")
            return False, "Should raise ValueError for 'invalid'"
        except ValueError:
            return True, None

    tests.append(("validate_ip_address invalid raises ValueError", test_ip_address_invalid))

    def test_ip_address_out_of_range():
        try:
            validate_ip_address("256.0.0.1")
            return False, "Should raise ValueError for '256.0.0.1'"
        except ValueError:
            return True, None

    tests.append(("validate_ip_address out of range", test_ip_address_out_of_range))

    def test_ip_address_none():
        try:
            validate_ip_address(None)  # type: ignore[arg-type]  # Intentionally testing error handling
            return False, "Should raise ValueError for None"
        except (ValueError, TypeError):
            return True, None

    tests.append(("validate_ip_address None", test_ip_address_none))

    # =================================================================
    # validate_mac_address Tests
    # =================================================================

    def test_mac_address_valid():
        validate_mac_address("00:11:22:33:44:55")
        validate_mac_address("AA:BB:CC:DD:EE:FF")
        validate_mac_address("aa:bb:cc:dd:ee:ff")
        return True, None

    tests.append(("validate_mac_address valid MACs", test_mac_address_valid))

    def test_mac_address_invalid():
        try:
            validate_mac_address("invalid")
            return False, "Should raise ValueError for 'invalid'"
        except ValueError:
            return True, None

    tests.append(("validate_mac_address invalid raises ValueError", test_mac_address_invalid))

    def test_mac_address_wrong_format():
        try:
            validate_mac_address("00-11-22-33-44-55")  # Wrong separator
            return False, "Should raise ValueError for wrong format"
        except ValueError:
            return True, None

    tests.append(("validate_mac_address wrong format", test_mac_address_wrong_format))

    # =================================================================
    # validate_port_number Tests
    # =================================================================

    def test_port_number_valid():
        validate_port_number(0)
        validate_port_number(1)
        validate_port_number(80)
        validate_port_number(443)
        validate_port_number(65535)
        return True, None

    tests.append(("validate_port_number valid ports", test_port_number_valid))

    def test_port_number_none():
        # None should be accepted (optional parameter)
        validate_port_number(None)
        return True, None

    tests.append(("validate_port_number None accepted", test_port_number_none))

    def test_port_number_negative():
        try:
            validate_port_number(-1)
            return False, "Should raise ValueError for -1"
        except ValueError:
            return True, None

    tests.append(("validate_port_number negative raises ValueError", test_port_number_negative))

    # BUG #6: validate_port_number allows ports > 65535
    def test_port_number_over_65535_BUG():
        try:
            validate_port_number(65536)
            # Should have raised ValueError but didn't
            return False, "BUG: validate_port_number(65536) should raise ValueError but allows ports up to 4294967295"
        except ValueError:
            return True, None

    tests.append(("BUG #6: port > 65535 should fail", test_port_number_over_65535_BUG))

    def test_port_number_very_large_BUG():
        try:
            validate_port_number(1000000)
            return False, "BUG: validate_port_number(1000000) should fail - not a valid port"
        except ValueError:
            return True, None

    tests.append(("BUG #6: port 1000000 should fail", test_port_number_very_large_BUG))

    # =================================================================
    # validate_color Tests
    # =================================================================

    def test_color_valid():
        validate_color(0)
        validate_color(16)
        validate_color(32)
        return True, None

    tests.append(("validate_color valid values", test_color_valid))

    def test_color_invalid_high():
        try:
            validate_color(33)
            return False, "Should raise ValueError for 33"
        except ValueError:
            return True, None

    tests.append(("validate_color 33 raises ValueError", test_color_invalid_high))

    def test_color_invalid_negative():
        try:
            validate_color(-1)
            return False, "Should raise ValueError for -1"
        except ValueError:
            return True, None

    tests.append(("validate_color -1 raises ValueError", test_color_invalid_negative))

    # =================================================================
    # validate_enable_disable Tests
    # =================================================================

    def test_enable_disable_valid():
        validate_enable_disable("enable", "status")
        validate_enable_disable("disable", "status")
        validate_enable_disable(None, "status")  # None is allowed
        return True, None

    tests.append(("validate_enable_disable valid values", test_enable_disable_valid))

    def test_enable_disable_invalid():
        try:
            validate_enable_disable("invalid", "status")
            return False, "Should raise ValueError for 'invalid'"
        except ValueError:
            return True, None

    tests.append(("validate_enable_disable invalid raises ValueError", test_enable_disable_invalid))

    def test_enable_disable_common_mistakes():
        # Test common mistakes: 'enabled' vs 'enable'
        try:
            validate_enable_disable("enabled", "status")
            return False, "Should raise ValueError for 'enabled'"
        except ValueError:
            pass
        try:
            validate_enable_disable("disabled", "status")
            return False, "Should raise ValueError for 'disabled'"
        except ValueError:
            pass
        return True, None

    tests.append(("validate_enable_disable 'enabled'/'disabled' fail", test_enable_disable_common_mistakes))

    # =================================================================
    # validate_status Tests
    # =================================================================

    def test_status_valid():
        validate_status("enable")
        validate_status("disable")
        return True, None

    tests.append(("validate_status valid values", test_status_valid))

    # =================================================================
    # validate_string_length Tests
    # =================================================================

    def test_string_length_valid():
        validate_string_length("test", 10, "field")
        validate_string_length("a", 1, "field")
        validate_string_length("hello world", 100, "field")
        return True, None

    tests.append(("validate_string_length valid strings", test_string_length_valid))

    def test_string_length_too_long():
        try:
            validate_string_length("hello world", 5, "field")
            return False, "Should raise ValueError for too long string"
        except ValueError:
            return True, None

    tests.append(("validate_string_length too long", test_string_length_too_long))

    # =================================================================
    # validate_time_format Tests
    # =================================================================

    def test_time_format_valid():
        validate_time_format("00:00", "time")
        validate_time_format("12:30", "time")
        validate_time_format("23:59", "time")
        return True, None

    tests.append(("validate_time_format valid times", test_time_format_valid))

    def test_time_format_invalid():
        try:
            validate_time_format("25:00", "time")
            return False, "Should raise ValueError for invalid hour"
        except ValueError:
            return True, None

    tests.append(("validate_time_format invalid hour", test_time_format_invalid))

    def test_time_format_wrong_format():
        try:
            validate_time_format("12:30:00", "time")  # With seconds
            return False, "Should raise ValueError for HH:MM:SS format"
        except ValueError:
            return True, None

    tests.append(("validate_time_format wrong format", test_time_format_wrong_format))

    # =================================================================
    # validate_policy_id Tests
    # =================================================================

    def test_policy_id_valid():
        validate_policy_id(0)  # 0 is valid according to docstring
        validate_policy_id(1)
        validate_policy_id(100)
        validate_policy_id(4294967295)
        return True, None

    tests.append(("validate_policy_id valid IDs", test_policy_id_valid))

    def test_policy_id_none():
        try:
            validate_policy_id(None)
            return False, "Should raise ValueError for None"
        except ValueError:
            return True, None

    tests.append(("validate_policy_id None raises ValueError", test_policy_id_none))

    def test_policy_id_negative():
        try:
            validate_policy_id(-1)
            return False, "Should raise ValueError for -1"
        except ValueError:
            return True, None

    tests.append(("validate_policy_id negative raises ValueError", test_policy_id_negative))

    # =================================================================
    # validate_integer_range Tests
    # =================================================================

    def test_integer_range_valid():
        validate_integer_range(5, 0, 10, "field")
        validate_integer_range(0, 0, 10, "field")
        validate_integer_range(10, 0, 10, "field")
        return True, None

    tests.append(("validate_integer_range valid values", test_integer_range_valid))

    def test_integer_range_none():
        # None should be accepted
        validate_integer_range(None, 0, 10, "field")
        return True, None

    tests.append(("validate_integer_range None accepted", test_integer_range_none))

    def test_integer_range_out_of_range():
        try:
            validate_integer_range(11, 0, 10, "field")
            return False, "Should raise ValueError for 11"
        except ValueError:
            return True, None

    tests.append(("validate_integer_range out of range", test_integer_range_out_of_range))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Validators Tests{Colors.RESET}")
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
