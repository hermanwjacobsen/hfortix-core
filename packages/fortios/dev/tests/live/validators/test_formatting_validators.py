"""
Tests for hfortix_fortios formatting functions.

Tests all data formatting utilities.
"""

import json

from hfortix_fortios.formatting import (
    to_json,
    to_csv,
    to_dict,
    to_multiline,
    to_list,
    to_quoted,
    to_table,
    to_yaml,
    to_xml,
    to_key_value,
    to_markdown_table,
    to_dictlist,
    to_listdict,
)


# ============================================================================
# to_json tests
# ============================================================================

def test_to_json_dict():
    """Test JSON formatting of dict."""
    data = {"name": "test", "value": 123}
    result = to_json(data)
    assert '"name": "test"' in result
    assert '"value": 123' in result
    print("✅ to_json - dict")


def test_to_json_list():
    """Test JSON formatting of list."""
    data = [1, 2, 3]
    result = to_json(data)
    parsed = json.loads(result)
    assert parsed == [1, 2, 3]
    print("✅ to_json - list")


def test_to_json_nested():
    """Test JSON formatting of nested structure."""
    data = {"policy": {"name": "test", "members": ["a", "b"]}}
    result = to_json(data)
    parsed = json.loads(result)
    assert parsed["policy"]["members"] == ["a", "b"]
    print("✅ to_json - nested")


def test_to_json_with_object():
    """Test JSON formatting of object with __dict__."""
    class TestObj:
        def __init__(self):
            self.name = "test"
            self.value = 42
    
    result = to_json(TestObj())
    parsed = json.loads(result)
    assert parsed["name"] == "test"
    assert parsed["value"] == 42
    print("✅ to_json - object with __dict__")


def test_to_json_with_set():
    """Test JSON formatting of set (converts to list)."""
    data = {"items": {1, 2, 3}}
    result = to_json(data)
    parsed = json.loads(result)
    assert sorted(parsed["items"]) == [1, 2, 3]
    print("✅ to_json - set to list")


def test_to_json_indent():
    """Test JSON formatting with custom indent."""
    data = {"a": 1}
    result = to_json(data, indent=4)
    assert "    " in result  # 4-space indent
    print("✅ to_json - custom indent")


# ============================================================================
# to_csv tests
# ============================================================================

def test_to_csv_list():
    """Test CSV formatting of list."""
    data = ["port1", "port2", "port3"]
    result = to_csv(data)
    assert result == "port1, port2, port3"
    print("✅ to_csv - list")


def test_to_csv_dict():
    """Test CSV formatting of dict."""
    data = {"x": 1, "y": 2}
    result = to_csv(data)
    assert "x=1" in result
    assert "y=2" in result
    print("✅ to_csv - dict")


def test_to_csv_string():
    """Test CSV formatting of string (passthrough)."""
    result = to_csv("already a string")
    assert result == "already a string"
    print("✅ to_csv - string passthrough")


def test_to_csv_none():
    """Test CSV formatting of None."""
    result = to_csv(None)
    assert result == ""
    print("✅ to_csv - None")


def test_to_csv_custom_separator():
    """Test CSV formatting with custom separator."""
    data = [1, 2, 3]
    result = to_csv(data, separator=" | ")
    assert result == "1 | 2 | 3"
    print("✅ to_csv - custom separator")


def test_to_csv_object():
    """Test CSV formatting of object."""
    class Obj:
        def __init__(self):
            self.name = "test"
            self.ip = "10.0.0.1"
    
    result = to_csv(Obj())
    assert "name=test" in result
    assert "ip=10.0.0.1" in result
    print("✅ to_csv - object")


# ============================================================================
# to_dict tests
# ============================================================================

def test_to_dict_dict():
    """Test to_dict with dict (passthrough)."""
    data = {"already": "a dict"}
    result = to_dict(data)
    assert result == {"already": "a dict"}
    print("✅ to_dict - dict passthrough")


def test_to_dict_object():
    """Test to_dict with object."""
    class Policy:
        def __init__(self):
            self.name = "Allow-All"
            self.action = "accept"
    
    result = to_dict(Policy())
    assert result == {"name": "Allow-All", "action": "accept"}
    print("✅ to_dict - object")


def test_to_dict_list_of_tuples():
    """Test to_dict with list of tuples."""
    data = [("a", 1), ("b", 2)]
    result = to_dict(data)
    assert result == {"a": 1, "b": 2}
    print("✅ to_dict - list of tuples")


def test_to_dict_list():
    """Test to_dict with list (indexed)."""
    data = ["x", "y", "z"]
    result = to_dict(data)
    assert result == {0: "x", 1: "y", 2: "z"}
    print("✅ to_dict - list to indexed dict")


def test_to_dict_primitive():
    """Test to_dict with primitive."""
    result = to_dict("simple string")
    assert result == {"value": "simple string"}
    print("✅ to_dict - primitive")


def test_to_dict_none():
    """Test to_dict with None."""
    result = to_dict(None)
    assert result == {"value": None}
    print("✅ to_dict - None")


# ============================================================================
# to_multiline tests
# ============================================================================

def test_to_multiline_list():
    """Test multiline formatting of list."""
    data = ["port1", "port2", "port3"]
    result = to_multiline(data)
    assert result == "port1\nport2\nport3"
    print("✅ to_multiline - list")


def test_to_multiline_dict():
    """Test multiline formatting of dict."""
    data = {"name": "policy1", "action": "accept"}
    result = to_multiline(data)
    assert "name: policy1" in result
    assert "action: accept" in result
    print("✅ to_multiline - dict")


def test_to_multiline_string():
    """Test multiline formatting of string (passthrough)."""
    result = to_multiline("already a string")
    assert result == "already a string"
    print("✅ to_multiline - string passthrough")


def test_to_multiline_none():
    """Test multiline formatting of None."""
    result = to_multiline(None)
    assert result == ""
    print("✅ to_multiline - None")


def test_to_multiline_custom_separator():
    """Test multiline formatting with custom separator."""
    data = ["a", "b", "c"]
    result = to_multiline(data, separator=" | ")
    assert result == "a | b | c"
    print("✅ to_multiline - custom separator")


# ============================================================================
# to_list tests
# ============================================================================

def test_to_list_list():
    """Test to_list with list (passthrough)."""
    data = ["already", "a", "list"]
    result = to_list(data)
    assert result == ["already", "a", "list"]
    print("✅ to_list - list passthrough")


def test_to_list_tuple():
    """Test to_list with tuple."""
    data = ("tuple", "to", "list")
    result = to_list(data)
    assert result == ["tuple", "to", "list"]
    print("✅ to_list - tuple")


def test_to_list_set():
    """Test to_list with set."""
    data = {"a", "b", "c"}
    result = to_list(data)
    assert sorted(result) == ["a", "b", "c"]
    print("✅ to_list - set")


def test_to_list_string_with_delimiter():
    """Test to_list with string and delimiter."""
    data = "port1,port2,port3"
    result = to_list(data, delimiter=",")
    assert result == ["port1", "port2", "port3"]
    print("✅ to_list - string with delimiter")


def test_to_list_string_auto_split():
    """Test to_list with string (auto-split on space)."""
    data = "port1 port2 port3"
    result = to_list(data)
    assert result == ["port1", "port2", "port3"]
    print("✅ to_list - string auto-split")


def test_to_list_single_string():
    """Test to_list with single string (no spaces)."""
    result = to_list("single_string")
    assert result == ["single_string"]
    print("✅ to_list - single string")


def test_to_list_dict():
    """Test to_list with dict (values)."""
    data = {"name": "policy1", "action": "accept"}
    result = to_list(data)
    assert result == ["policy1", "accept"]
    print("✅ to_list - dict values")


def test_to_list_none():
    """Test to_list with None."""
    result = to_list(None)
    assert result == []
    print("✅ to_list - None")


def test_to_list_primitive():
    """Test to_list with primitive."""
    result = to_list(42)
    assert result == [42]
    print("✅ to_list - primitive")


# ============================================================================
# to_quoted tests
# ============================================================================

def test_to_quoted_list():
    """Test quoted formatting of list."""
    data = ["port1", "port2", "port3"]
    result = to_quoted(data)
    assert result == '"port1", "port2", "port3"'
    print("✅ to_quoted - list")


def test_to_quoted_dict():
    """Test quoted formatting of dict (keys)."""
    data = {"x": 1, "y": 2}
    result = to_quoted(data)
    assert '"x"' in result
    assert '"y"' in result
    print("✅ to_quoted - dict keys")


def test_to_quoted_string():
    """Test quoted formatting of string."""
    result = to_quoted("hello")
    assert result == '"hello"'
    print("✅ to_quoted - string")


def test_to_quoted_none():
    """Test quoted formatting of None."""
    result = to_quoted(None)
    assert result == '""'
    print("✅ to_quoted - None")


def test_to_quoted_custom_quote():
    """Test quoted formatting with custom quote."""
    data = [1, 2, 3]
    result = to_quoted(data, quote="'")
    assert result == "'1', '2', '3'"
    print("✅ to_quoted - custom quote")


# ============================================================================
# to_table tests
# ============================================================================

def test_to_table_list_of_dicts():
    """Test table formatting of list of dicts."""
    data = [
        {"name": "Allow-Web", "action": "accept"},
        {"name": "Block-All", "action": "deny"}
    ]
    result = to_table(data)
    assert "name" in result
    assert "action" in result
    assert "Allow-Web" in result
    assert "Block-All" in result
    print("✅ to_table - list of dicts")


def test_to_table_no_headers():
    """Test table formatting without headers."""
    data = [{"name": "test", "value": 1}]
    result = to_table(data, headers=False)
    assert "name" not in result
    assert "test" in result
    print("✅ to_table - no headers")


def test_to_table_custom_delimiter():
    """Test table formatting with custom delimiter."""
    data = [{"a": 1, "b": 2}]
    result = to_table(data, delimiter=" || ")
    assert " || " in result
    print("✅ to_table - custom delimiter")


def test_to_table_none():
    """Test table formatting of None."""
    result = to_table(None)
    assert result == ""
    print("✅ to_table - None")


def test_to_table_single_dict():
    """Test table formatting of single dict."""
    data = {"name": "test", "value": 1}
    result = to_table(data)
    assert "name" in result
    assert "test" in result
    print("✅ to_table - single dict")


# ============================================================================
# to_yaml tests
# ============================================================================

def test_to_yaml_dict():
    """Test YAML formatting of dict."""
    data = {"name": "Allow-Web", "action": "accept"}
    result = to_yaml(data)
    assert "name: Allow-Web" in result
    assert "action: accept" in result
    print("✅ to_yaml - dict")


def test_to_yaml_nested():
    """Test YAML formatting of nested dict."""
    data = {"nested": {"key": "value"}}
    result = to_yaml(data)
    assert "nested:" in result
    assert "key: value" in result
    print("✅ to_yaml - nested")


def test_to_yaml_list():
    """Test YAML formatting of list in dict."""
    data = {"ports": ["80", "443"]}
    result = to_yaml(data)
    assert "ports:" in result
    assert "- 80" in result
    assert "- 443" in result
    print("✅ to_yaml - list")


def test_to_yaml_none():
    """Test YAML formatting of None."""
    result = to_yaml(None)
    assert result == "null"
    print("✅ to_yaml - None")


def test_to_yaml_bool():
    """Test YAML formatting of bool."""
    assert to_yaml(True) == "true"
    assert to_yaml(False) == "false"
    print("✅ to_yaml - bool")


def test_to_yaml_empty():
    """Test YAML formatting of empty structures."""
    assert to_yaml([]) == "[]"
    assert to_yaml({}) == "{}"
    print("✅ to_yaml - empty")


# ============================================================================
# to_xml tests
# ============================================================================

def test_to_xml_dict():
    """Test XML formatting of dict."""
    data = {"name": "Allow-Web", "policyid": 1}
    result = to_xml(data, root="policy")
    assert "<policy>" in result
    assert "<name>Allow-Web</name>" in result
    assert "<policyid>1</policyid>" in result
    assert "</policy>" in result
    print("✅ to_xml - dict")


def test_to_xml_list():
    """Test XML formatting of list."""
    data = [{"name": "p1"}, {"name": "p2"}]
    result = to_xml(data, root="policies")
    assert "<policies>" in result
    assert "<item>" in result
    assert "</policies>" in result
    print("✅ to_xml - list")


def test_to_xml_none():
    """Test XML formatting of None."""
    result = to_xml(None, root="empty")
    assert "<empty/>" in result
    print("✅ to_xml - None")


def test_to_xml_custom_root():
    """Test XML formatting with custom root."""
    data = {"value": "test"}
    result = to_xml(data, root="custom_root")
    assert "<custom_root>" in result
    assert "</custom_root>" in result
    print("✅ to_xml - custom root")


# ============================================================================
# to_key_value tests
# ============================================================================

def test_to_key_value_dict():
    """Test key-value formatting of dict."""
    data = {"host": "192.168.1.1", "port": 443}
    result = to_key_value(data)
    assert "host=192.168.1.1" in result
    assert "port=443" in result
    print("✅ to_key_value - dict")


def test_to_key_value_custom_separator():
    """Test key-value formatting with custom separator."""
    data = {"a": 1, "b": 2}
    result = to_key_value(data, separator=": ", delimiter="; ")
    assert "a: 1" in result
    assert "; " in result
    print("✅ to_key_value - custom separators")


def test_to_key_value_none():
    """Test key-value formatting of None."""
    result = to_key_value(None)
    assert result == ""
    print("✅ to_key_value - None")


def test_to_key_value_list():
    """Test key-value formatting of list (indexed)."""
    data = ["x", "y", "z"]
    result = to_key_value(data)
    assert "0=x" in result
    assert "1=y" in result
    assert "2=z" in result
    print("✅ to_key_value - list indexed")


# ============================================================================
# to_markdown_table tests
# ============================================================================

def test_to_markdown_table_list_of_dicts():
    """Test markdown table formatting."""
    data = [
        {"name": "Allow-Web", "action": "accept"},
        {"name": "Block-All", "action": "deny"}
    ]
    result = to_markdown_table(data)
    assert "| name | action |" in result
    assert "| --- | --- |" in result
    assert "| Allow-Web | accept |" in result
    assert "| Block-All | deny |" in result
    print("✅ to_markdown_table - list of dicts")


def test_to_markdown_table_none():
    """Test markdown table of None."""
    result = to_markdown_table(None)
    assert result == ""
    print("✅ to_markdown_table - None")


def test_to_markdown_table_single_dict():
    """Test markdown table of single dict."""
    data = {"name": "test", "value": 1}
    result = to_markdown_table(data)
    assert "| name | value |" in result
    assert "| test | 1 |" in result
    print("✅ to_markdown_table - single dict")


# ============================================================================
# to_dictlist tests
# ============================================================================

def test_to_dictlist_columnar():
    """Test columnar to row conversion."""
    data = {"name": ["p1", "p2"], "action": ["accept", "deny"]}
    result = to_dictlist(data)
    assert result == [
        {"name": "p1", "action": "accept"},
        {"name": "p2", "action": "deny"}
    ]
    print("✅ to_dictlist - columnar to rows")


def test_to_dictlist_single_column():
    """Test single column conversion."""
    data = {"ports": ["80", "443", "8080"]}
    result = to_dictlist(data)
    assert result == [{"ports": "80"}, {"ports": "443"}, {"ports": "8080"}]
    print("✅ to_dictlist - single column")


def test_to_dictlist_already_list_of_dicts():
    """Test passthrough for list of dicts."""
    data = [{"name": "p1"}, {"name": "p2"}]
    result = to_dictlist(data)
    assert result == data
    print("✅ to_dictlist - already list of dicts")


def test_to_dictlist_none():
    """Test to_dictlist with None."""
    result = to_dictlist(None)
    assert result == []
    print("✅ to_dictlist - None")


def test_to_dictlist_uneven_columns():
    """Test to_dictlist with uneven column lengths."""
    data = {"a": [1, 2, 3], "b": [4, 5]}
    result = to_dictlist(data)
    assert len(result) == 3
    assert result[2]["b"] is None  # Padded with None
    print("✅ to_dictlist - uneven columns")


# ============================================================================
# to_listdict tests
# ============================================================================

def test_to_listdict_rows():
    """Test row to columnar conversion."""
    data = [
        {"name": "p1", "action": "accept"},
        {"name": "p2", "action": "deny"}
    ]
    result = to_listdict(data)
    assert result == {"name": ["p1", "p2"], "action": ["accept", "deny"]}
    print("✅ to_listdict - rows to columnar")


def test_to_listdict_single_dict():
    """Test single dict conversion."""
    data = {"name": "p1", "action": "accept"}
    result = to_listdict(data)
    assert result == {"name": ["p1"], "action": ["accept"]}
    print("✅ to_listdict - single dict")


def test_to_listdict_none():
    """Test to_listdict with None."""
    result = to_listdict(None)
    assert result == {}
    print("✅ to_listdict - None")


def test_to_listdict_already_columnar():
    """Test passthrough for already columnar data."""
    data = {"names": ["a", "b"], "values": [1, 2]}
    result = to_listdict(data)
    assert result == {"names": ["a", "b"], "values": [1, 2]}
    print("✅ to_listdict - already columnar")


def test_to_listdict_missing_keys():
    """Test to_listdict with rows having different keys."""
    data = [
        {"name": "p1", "action": "accept"},
        {"name": "p2"}  # Missing 'action'
    ]
    result = to_listdict(data)
    assert result["name"] == ["p1", "p2"]
    assert result["action"] == ["accept", None]
    print("✅ to_listdict - missing keys")


def run_all_tests():
    """Run all formatting tests."""
    print("\n" + "=" * 60)
    print("FORMATTING FUNCTION TESTS")
    print("=" * 60 + "\n")

    # to_json tests
    test_to_json_dict()
    test_to_json_list()
    test_to_json_nested()
    test_to_json_with_object()
    test_to_json_with_set()
    test_to_json_indent()

    # to_csv tests
    test_to_csv_list()
    test_to_csv_dict()
    test_to_csv_string()
    test_to_csv_none()
    test_to_csv_custom_separator()
    test_to_csv_object()

    # to_dict tests
    test_to_dict_dict()
    test_to_dict_object()
    test_to_dict_list_of_tuples()
    test_to_dict_list()
    test_to_dict_primitive()
    test_to_dict_none()

    # to_multiline tests
    test_to_multiline_list()
    test_to_multiline_dict()
    test_to_multiline_string()
    test_to_multiline_none()
    test_to_multiline_custom_separator()

    # to_list tests
    test_to_list_list()
    test_to_list_tuple()
    test_to_list_set()
    test_to_list_string_with_delimiter()
    test_to_list_string_auto_split()
    test_to_list_single_string()
    test_to_list_dict()
    test_to_list_none()
    test_to_list_primitive()

    # to_quoted tests
    test_to_quoted_list()
    test_to_quoted_dict()
    test_to_quoted_string()
    test_to_quoted_none()
    test_to_quoted_custom_quote()

    # to_table tests
    test_to_table_list_of_dicts()
    test_to_table_no_headers()
    test_to_table_custom_delimiter()
    test_to_table_none()
    test_to_table_single_dict()

    # to_yaml tests
    test_to_yaml_dict()
    test_to_yaml_nested()
    test_to_yaml_list()
    test_to_yaml_none()
    test_to_yaml_bool()
    test_to_yaml_empty()

    # to_xml tests
    test_to_xml_dict()
    test_to_xml_list()
    test_to_xml_none()
    test_to_xml_custom_root()

    # to_key_value tests
    test_to_key_value_dict()
    test_to_key_value_custom_separator()
    test_to_key_value_none()
    test_to_key_value_list()

    # to_markdown_table tests
    test_to_markdown_table_list_of_dicts()
    test_to_markdown_table_none()
    test_to_markdown_table_single_dict()

    # to_dictlist tests
    test_to_dictlist_columnar()
    test_to_dictlist_single_column()
    test_to_dictlist_already_list_of_dicts()
    test_to_dictlist_none()
    test_to_dictlist_uneven_columns()

    # to_listdict tests
    test_to_listdict_rows()
    test_to_listdict_single_dict()
    test_to_listdict_none()
    test_to_listdict_already_columnar()
    test_to_listdict_missing_keys()

    print("\n" + "=" * 60)
    print("ALL FORMATTING TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
