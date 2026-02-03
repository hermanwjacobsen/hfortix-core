"""
Tests for hfortix_fortios.formatting module.

Data formatting functions for converting API responses to various formats.

BUGS FOUND:
- BUG #5: to_xml() doesn't escape XML special characters (<, >, &, ", ')
  The generated XML is invalid and cannot be parsed by XML parsers.
  FIX: Use xml.sax.saxutils.escape() or html.escape() for text content
"""

import sys


class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_test_result(name: str, passed: bool, error: str = None):
    status = f"{Colors.GREEN}PASS{Colors.RESET}" if passed else f"{Colors.RED}FAIL{Colors.RESET}"
    print(f"  [{status}] {name}")
    if error:
        print(f"         {Colors.RED}{error}{Colors.RESET}")


def run_tests():
    from hfortix_fortios.formatting import (
        to_csv, to_dict, to_dictlist, to_json, to_key_value,
        to_list, to_listdict, to_markdown_table, to_multiline,
        to_quoted, to_table, to_xml, to_yaml
    )
    import xml.etree.ElementTree as ET
    import json

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # to_csv Tests
    # =================================================================

    def test_to_csv_list():
        data = [{"name": "a", "value": 1}, {"name": "b", "value": 2}]
        result = to_csv(data)
        assert isinstance(result, str)
        assert "a" in result or "name" in result
        return True, None

    tests.append(("to_csv with list of dicts", test_to_csv_list))

    def test_to_csv_empty():
        result = to_csv([])
        assert result == ""
        return True, None

    tests.append(("to_csv with empty list", test_to_csv_empty))

    def test_to_csv_none():
        result = to_csv(None)
        assert result == ""
        return True, None

    tests.append(("to_csv with None", test_to_csv_none))

    def test_to_csv_single_dict():
        result = to_csv({"a": 1, "b": 2})
        assert "a=1" in result or "a" in result
        return True, None

    tests.append(("to_csv with single dict", test_to_csv_single_dict))

    def test_to_csv_custom_separator():
        data = ["item1", "item2", "item3"]
        result = to_csv(data, separator=";")
        assert ";" in result
        return True, None

    tests.append(("to_csv with custom separator", test_to_csv_custom_separator))

    # =================================================================
    # to_dict Tests
    # =================================================================

    def test_to_dict_list():
        data = [{"name": "a"}, {"name": "b"}]
        result = to_dict(data)
        assert isinstance(result, dict)
        assert 0 in result or "0" in result or "a" in result
        return True, None

    tests.append(("to_dict with list", test_to_dict_list))

    def test_to_dict_empty():
        result = to_dict([])
        assert result == {}
        return True, None

    tests.append(("to_dict with empty list", test_to_dict_empty))

    def test_to_dict_already_dict():
        data = {"key": "value"}
        result = to_dict(data)
        assert result == {"key": "value"}
        return True, None

    tests.append(("to_dict with dict input", test_to_dict_already_dict))

    # =================================================================
    # to_json Tests
    # =================================================================

    def test_to_json_basic():
        data = {"name": "test", "value": 123}
        result = to_json(data)
        assert isinstance(result, str)
        parsed = json.loads(result)
        assert parsed == data
        return True, None

    tests.append(("to_json basic", test_to_json_basic))

    def test_to_json_indent():
        data = {"key": "value"}
        result = to_json(data, indent=4)
        assert "    " in result
        return True, None

    tests.append(("to_json with custom indent", test_to_json_indent))

    def test_to_json_nested():
        data = {"outer": {"inner": {"deep": "value"}}}
        result = to_json(data)
        parsed = json.loads(result)
        assert parsed["outer"]["inner"]["deep"] == "value"
        return True, None

    tests.append(("to_json with nested data", test_to_json_nested))

    # =================================================================
    # to_key_value Tests
    # =================================================================

    def test_to_key_value_basic():
        data = {"name": "test", "port": 443}
        result = to_key_value(data)
        assert "name=test" in result
        assert "port=443" in result
        return True, None

    tests.append(("to_key_value basic", test_to_key_value_basic))

    def test_to_key_value_custom_separator():
        data = {"a": 1, "b": 2}
        result = to_key_value(data, separator=": ")
        assert "a: 1" in result
        return True, None

    tests.append(("to_key_value custom separator", test_to_key_value_custom_separator))

    # =================================================================
    # to_list Tests
    # =================================================================

    def test_to_list_from_dict():
        data = {"a": 1, "b": 2}
        result = to_list(data)
        assert isinstance(result, list)
        return True, None

    tests.append(("to_list from dict", test_to_list_from_dict))

    def test_to_list_already_list():
        data = [1, 2, 3]
        result = to_list(data)
        assert result == [1, 2, 3]
        return True, None

    tests.append(("to_list already list", test_to_list_already_list))

    # =================================================================
    # to_markdown_table Tests
    # =================================================================

    def test_to_markdown_table_basic():
        data = [{"name": "row1", "value": 100}, {"name": "row2", "value": 200}]
        result = to_markdown_table(data)
        assert "|" in result
        assert "---" in result
        assert "name" in result
        return True, None

    tests.append(("to_markdown_table basic", test_to_markdown_table_basic))

    def test_to_markdown_table_inconsistent_keys():
        data = [
            {"name": "a", "value": 1},
            {"name": "b"},
            {"name": "c", "value": 3, "extra": "x"}
        ]
        result = to_markdown_table(data)
        assert "name" in result
        return True, None

    tests.append(("to_markdown_table inconsistent keys", test_to_markdown_table_inconsistent_keys))

    # =================================================================
    # to_multiline Tests
    # =================================================================

    def test_to_multiline_list():
        data = ["line1", "line2", "line3"]
        result = to_multiline(data)
        assert "\n" in result
        lines = result.split("\n")
        assert len(lines) == 3
        return True, None

    tests.append(("to_multiline list", test_to_multiline_list))

    def test_to_multiline_custom_separator():
        data = ["a", "b", "c"]
        result = to_multiline(data, separator="|")
        assert "|" in result
        return True, None

    tests.append(("to_multiline custom separator", test_to_multiline_custom_separator))

    # =================================================================
    # to_quoted Tests
    # =================================================================

    def test_to_quoted_basic():
        data = ["item1", "item2"]
        result = to_quoted(data)
        assert '"item1"' in result
        assert '"item2"' in result
        return True, None

    tests.append(("to_quoted basic", test_to_quoted_basic))

    def test_to_quoted_custom_quote():
        data = ["a", "b"]
        result = to_quoted(data, quote="'")
        assert "'a'" in result
        return True, None

    tests.append(("to_quoted custom quote", test_to_quoted_custom_quote))

    # =================================================================
    # to_table Tests
    # =================================================================

    def test_to_table_basic():
        data = [{"col1": "a", "col2": "b"}, {"col1": "c", "col2": "d"}]
        result = to_table(data)
        assert "col1" in result or "a" in result
        return True, None

    tests.append(("to_table basic", test_to_table_basic))

    def test_to_table_no_headers():
        data = [{"col1": "a"}, {"col1": "b"}]
        result = to_table(data, headers=False)
        assert "a" in result
        return True, None

    tests.append(("to_table no headers", test_to_table_no_headers))

    # =================================================================
    # to_xml Tests
    # =================================================================

    def test_to_xml_basic():
        data = {"name": "test", "value": 123}
        result = to_xml(data)
        assert "<name>test</name>" in result
        assert "<value>123</value>" in result
        return True, None

    tests.append(("to_xml basic", test_to_xml_basic))

    def test_to_xml_custom_root():
        data = {"key": "value"}
        result = to_xml(data, root="config")
        assert "<config>" in result
        assert "</config>" in result
        return True, None

    tests.append(("to_xml custom root", test_to_xml_custom_root))

    def test_to_xml_list():
        data = [{"name": "a"}, {"name": "b"}]
        result = to_xml(data)
        assert "<item>" in result or "<name>" in result
        return True, None

    tests.append(("to_xml with list", test_to_xml_list))

    # BUG #5: XML special characters not escaped
    def test_to_xml_special_chars_BUG():
        data = {"script": "<script>alert('xss')</script>", "ampersand": "a & b"}
        result = to_xml(data)
        try:
            ET.fromstring(result)
            return True, None
        except ET.ParseError as e:
            return False, f"BUG: to_xml() produces invalid XML - special chars not escaped: {e}"

    tests.append(("BUG #5: to_xml special chars not escaped", test_to_xml_special_chars_BUG))

    # =================================================================
    # to_yaml Tests
    # =================================================================

    def test_to_yaml_basic():
        data = {"name": "test", "value": 123}
        result = to_yaml(data)
        assert "name:" in result
        assert "test" in result
        return True, None

    tests.append(("to_yaml basic", test_to_yaml_basic))

    def test_to_yaml_list():
        data = [{"name": "a"}, {"name": "b"}]
        result = to_yaml(data)
        assert "-" in result
        return True, None

    tests.append(("to_yaml list", test_to_yaml_list))

    def test_to_yaml_nested():
        data = {"outer": {"inner": "value"}}
        result = to_yaml(data)
        assert "outer:" in result
        assert "inner:" in result
        return True, None

    tests.append(("to_yaml nested", test_to_yaml_nested))

    # =================================================================
    # Edge Cases
    # =================================================================

    def test_unicode_handling():
        data = {"emoji": "🔥", "japanese": "日本語"}
        result = to_json(data)
        assert "🔥" in result or "\\u" in result
        result = to_yaml(data)
        assert isinstance(result, str)
        return True, None

    tests.append(("Unicode handling", test_unicode_handling))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}Formatting Module Tests{Colors.RESET}")
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
