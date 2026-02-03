"""
Tests for hfortix_core.fmt data formatting functions

Tests 13 pure formatting functions that convert data between various formats.
"""

from hfortix_core.fmt import (
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


class TestObject:
    """Test object with __dict__ for conversion tests"""
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


# Prevent pytest from collecting this helper as a test class
TestObject.__test__ = False  # type: ignore[attr-defined]


def test_to_json():
    """Test to_json conversion"""
    print("\n=== Testing to_json ===")
    
    # Basic dict
    data = {"name": "test", "value": 123}
    result = to_json(data)
    assert '"name"' in result
    assert '"test"' in result
    print(f"✓ Dict to JSON: {result[:50]}...")
    
    # List
    data = ["a", "b", "c"]
    result = to_json(data)
    assert '"a"' in result  # With indent, format differs
    print(f"✓ List to JSON: {result}")
    
    # Object with __dict__
    obj = TestObject("policy1", 42)
    result = to_json(obj)
    assert "policy1" in result
    assert "42" in result
    print(f"✓ Object to JSON: {result}")
    
    # Set (converts to list)
    data = {1, 2, 3}
    result = to_json(data)
    assert "[" in result
    print(f"✓ Set to JSON: {result}")
    
    # Custom indent
    result = to_json({"a": 1}, indent=4)
    assert "\n" in result
    print("✓ Custom indent works")


def test_to_csv():
    """Test to_csv conversion"""
    print("\n=== Testing to_csv ===")
    
    # List
    result = to_csv(["port1", "port2", "port3"])
    assert result == "port1, port2, port3"
    print(f"✓ List to CSV: {result}")
    
    # Dict (key=value pairs)
    result = to_csv({"x": 1, "y": 2})
    assert "x=1" in result
    assert "y=2" in result
    print(f"✓ Dict to CSV: {result}")
    
    # String passthrough
    result = to_csv("already a string")
    assert result == "already a string"
    print(f"✓ String passthrough: {result}")
    
    # None
    result = to_csv(None)
    assert result == ""
    print("✓ None returns empty string")
    
    # Custom separator
    result = to_csv([1, 2, 3], separator=" | ")
    assert result == "1 | 2 | 3"
    print(f"✓ Custom separator: {result}")
    
    # Object with __dict__
    obj = TestObject("port1", 10)
    result = to_csv(obj)
    assert "name=port1" in result
    print(f"✓ Object to CSV: {result}")


def test_to_dict():
    """Test to_dict conversion"""
    print("\n=== Testing to_dict ===")
    
    # Dict passthrough
    data = {"already": "a dict"}
    result = to_dict(data)
    assert result == data
    print(f"✓ Dict passthrough: {result}")
    
    # Object with __dict__
    obj = TestObject("policy", 1)
    result = to_dict(obj)
    assert result["name"] == "policy"
    assert result["value"] == 1
    print(f"✓ Object to dict: {result}")
    
    # List of tuples (converts to dict)
    data = [("a", 1), ("b", 2)]
    result = to_dict(data)
    assert result == {"a": 1, "b": 2}
    print(f"✓ List of tuples to dict: {result}")
    
    # Plain list (indexed dict)
    data = ["x", "y", "z"]
    result = to_dict(data)
    assert result == {0: "x", 1: "y", 2: "z"}
    print(f"✓ List to indexed dict: {result}")
    
    # Primitive (wrapped)
    result = to_dict("simple")
    assert result == {"value": "simple"}
    print(f"✓ Primitive wrapped: {result}")
    
    # None
    result = to_dict(None)
    assert result == {"value": None}
    print("✓ None wrapped")


def test_to_multiline():
    """Test to_multiline conversion"""
    print("\n=== Testing to_multiline ===")
    
    # List
    result = to_multiline(["port1", "port2", "port3"])
    assert result == "port1\nport2\nport3"
    print(f"✓ List to multiline: {repr(result)}")
    
    # Dict
    result = to_multiline({"name": "policy1", "action": "accept"})
    assert "name: policy1" in result
    assert "action: accept" in result
    print(f"✓ Dict to multiline")
    
    # String passthrough
    result = to_multiline("already a string")
    assert result == "already a string"
    print("✓ String passthrough")
    
    # None
    result = to_multiline(None)
    assert result == ""
    print("✓ None returns empty")
    
    # Custom separator
    result = to_multiline([1, 2, 3], separator=" -- ")
    assert result == "1 -- 2 -- 3"
    print(f"✓ Custom separator: {result}")


def test_to_list():
    """Test to_list conversion"""
    print("\n=== Testing to_list ===")
    
    # List passthrough
    result = to_list(["already", "a", "list"])
    assert result == ["already", "a", "list"]
    print("✓ List passthrough")
    
    # Tuple to list
    result = to_list(("tuple", "to", "list"))
    assert result == ["tuple", "to", "list"]
    print("✓ Tuple to list")
    
    # Set to list
    result = to_list({"a", "b"})
    assert len(result) == 2
    assert "a" in result and "b" in result
    print("✓ Set to list")
    
    # String with delimiter
    result = to_list("port1,port2,port3", delimiter=",")
    assert result == ["port1", "port2", "port3"]
    print(f"✓ String with delimiter: {result}")
    
    # String with spaces (auto-split)
    result = to_list("port1 port2 port3")
    assert result == ["port1", "port2", "port3"]
    print(f"✓ String auto-split: {result}")
    
    # Single string (no spaces)
    result = to_list("single_string")
    assert result == ["single_string"]
    print(f"✓ Single string: {result}")
    
    # Dict (values only)
    result = to_list({"name": "policy1", "action": "accept"})
    assert "policy1" in result
    assert "accept" in result
    print(f"✓ Dict values: {result}")
    
    # None
    result = to_list(None)
    assert result == []
    print("✓ None returns empty list")
    
    # Primitive
    result = to_list(42)
    assert result == [42]
    print(f"✓ Primitive to list: {result}")


def test_to_quoted():
    """Test to_quoted conversion"""
    print("\n=== Testing to_quoted ===")
    
    # List
    result = to_quoted(["port1", "port2", "port3"])
    assert result == '"port1", "port2", "port3"'
    print(f"✓ List quoted: {result}")
    
    # Dict (keys quoted)
    result = to_quoted({"x": 1, "y": 2})
    assert '"x"' in result
    assert '"y"' in result
    print(f"✓ Dict keys quoted: {result}")
    
    # String
    result = to_quoted("hello")
    assert result == '"hello"'
    print(f"✓ String quoted: {result}")
    
    # None
    result = to_quoted(None)
    assert result == '""'
    print(f"✓ None quoted: {result}")
    
    # Custom quote
    result = to_quoted([1, 2, 3], quote="'")
    assert result == "'1', '2', '3'"
    print(f"✓ Custom quote: {result}")


def test_to_table():
    """Test to_table conversion"""
    print("\n=== Testing to_table ===")
    
    # List of dicts
    policies = [
        {"name": "Allow-Web", "action": "accept", "policyid": 1},
        {"name": "Block-All", "action": "deny", "policyid": 2}
    ]
    result = to_table(policies)
    assert "name | action | policyid" in result
    assert "Allow-Web | accept | 1" in result
    print(f"✓ List of dicts to table:\n{result}")
    
    # Without headers
    result = to_table(policies, headers=False)
    assert "name | action | policyid" not in result
    assert "Allow-Web" in result
    print("✓ Table without headers")
    
    # Custom delimiter
    result = to_table(policies, delimiter=" || ")
    assert " || " in result
    print("✓ Custom delimiter")
    
    # Single dict
    result = to_table({"name": "test", "value": 123})
    assert "name" in result
    print("✓ Single dict to table")
    
    # None
    result = to_table(None)
    assert result == ""
    print("✓ None returns empty")


def test_to_yaml():
    """Test to_yaml conversion"""
    print("\n=== Testing to_yaml ===")
    
    # Simple dict
    policy = {"name": "Allow-Web", "action": "accept"}
    result = to_yaml(policy)
    assert "name: Allow-Web" in result
    assert "action: accept" in result
    print(f"✓ Dict to YAML:\n{result}")
    
    # Nested dict
    data = {"nested": {"key": "value"}}
    result = to_yaml(data)
    assert "nested:" in result
    assert "key: value" in result
    print(f"✓ Nested dict to YAML:\n{result}")
    
    # List in dict
    policy = {"name": "Allow-Web", "srcintf": ["port1", "port2"]}
    result = to_yaml(policy)
    assert "srcintf:" in result
    assert "- port1" in result
    print(f"✓ Dict with list to YAML:\n{result}")
    
    # Boolean
    result = to_yaml({"enabled": True, "disabled": False})
    assert "true" in result
    assert "false" in result
    print("✓ Booleans in YAML")
    
    # None
    result = to_yaml(None)
    assert result == "null"
    print("✓ None to null")


def test_to_xml():
    """Test to_xml conversion"""
    print("\n=== Testing to_xml ===")
    
    # Simple dict
    policy = {"name": "Allow-Web", "policyid": 1}
    result = to_xml(policy, root="policy")
    assert "<policy>" in result
    assert "<name>Allow-Web</name>" in result
    assert "<policyid>1</policyid>" in result
    assert "</policy>" in result
    print(f"✓ Dict to XML:\n{result}")
    
    # List
    policies = [{"name": "p1"}, {"name": "p2"}]
    result = to_xml(policies, root="policies")
    assert "<policies>" in result
    assert "<item>" in result
    print(f"✓ List to XML:\n{result}")
    
    # None element
    result = to_xml(None, root="empty")
    assert "<empty/>" in result
    print(f"✓ None to self-closing: {result}")


def test_to_key_value():
    """Test to_key_value conversion"""
    print("\n=== Testing to_key_value ===")
    
    # Dict
    config = {"host": "192.168.1.1", "port": 443, "verify": False}
    result = to_key_value(config)
    assert "host=192.168.1.1" in result
    assert "port=443" in result
    assert "verify=False" in result
    print(f"✓ Dict to key-value:\n{result}")
    
    # Custom separator and delimiter
    result = to_key_value(config, separator=": ", delimiter="; ")
    assert "host: 192.168.1.1" in result
    assert "; " in result
    print(f"✓ Custom separators: {result}")
    
    # None
    result = to_key_value(None)
    assert result == ""
    print("✓ None returns empty")
    
    # List (indexed)
    result = to_key_value(["a", "b", "c"])
    assert "0=a" in result
    print(f"✓ List indexed: {result}")


def test_to_markdown_table():
    """Test to_markdown_table conversion"""
    print("\n=== Testing to_markdown_table ===")
    
    # List of dicts
    policies = [
        {"name": "Allow-Web", "action": "accept"},
        {"name": "Block-All", "action": "deny"}
    ]
    result = to_markdown_table(policies)
    assert "| name | action |" in result
    assert "| --- | --- |" in result
    assert "| Allow-Web | accept |" in result
    print(f"✓ List to markdown table:\n{result}")
    
    # None
    result = to_markdown_table(None)
    assert result == ""
    print("✓ None returns empty")
    
    # Single dict
    result = to_markdown_table({"name": "test"})
    assert "| name |" in result
    print("✓ Single dict to markdown")


def test_to_dictlist():
    """Test to_dictlist (columnar to row) conversion"""
    print("\n=== Testing to_dictlist ===")
    
    # Dict of lists (columnar) to list of dicts (rows)
    columnar = {"name": ["p1", "p2"], "action": ["accept", "deny"]}
    result = to_dictlist(columnar)
    assert len(result) == 2
    assert result[0] == {"name": "p1", "action": "accept"}
    assert result[1] == {"name": "p2", "action": "deny"}
    print(f"✓ Columnar to rows: {result}")
    
    # Already list of dicts
    data = [{"name": "p1"}, {"name": "p2"}]
    result = to_dictlist(data)
    assert result == data
    print("✓ List of dicts passthrough")
    
    # None
    result = to_dictlist(None)
    assert result == []
    print("✓ None returns empty list")
    
    # Single column
    result = to_dictlist({"ports": ["80", "443", "8080"]})
    assert len(result) == 3
    assert result[0] == {"ports": "80"}
    print(f"✓ Single column: {result}")


def test_to_listdict():
    """Test to_listdict (row to columnar) conversion"""
    print("\n=== Testing to_listdict ===")
    
    # List of dicts (rows) to dict of lists (columnar)
    rows = [
        {"name": "p1", "action": "accept"},
        {"name": "p2", "action": "deny"}
    ]
    result = to_listdict(rows)
    assert result["name"] == ["p1", "p2"]
    assert result["action"] == ["accept", "deny"]
    print(f"✓ Rows to columnar: {result}")
    
    # Single dict becomes dict of single-item lists
    result = to_listdict({"name": "p1", "action": "accept"})
    assert result["name"] == ["p1"]
    assert result["action"] == ["accept"]
    print(f"✓ Single dict: {result}")
    
    # None
    result = to_listdict(None)
    assert result == {}
    print("✓ None returns empty dict")
    
    # Already dict of lists
    data = {"name": ["p1", "p2"], "action": ["accept", "deny"]}
    result = to_listdict(data)
    assert result == data
    print("✓ Dict of lists passthrough")


def test_objects_with_dict():
    """Test that objects with __dict__ work across all formatters"""
    print("\n=== Testing Objects with __dict__ ===")
    
    obj = TestObject("myobj", 999)
    
    # All functions should handle objects
    assert "myobj" in to_json(obj)
    assert "name=myobj" in to_csv(obj)
    assert to_dict(obj)["name"] == "myobj"
    assert "name: myobj" in to_multiline(obj)
    assert "myobj" in to_list(obj)
    assert '"name"' in to_quoted(obj)
    assert "myobj" in to_yaml(obj)
    assert "<name>myobj</name>" in to_xml(obj)
    assert "name=myobj" in to_key_value(obj)
    
    print("✓ All formatters handle objects with __dict__")


if __name__ == "__main__":
    test_to_json()
    test_to_csv()
    test_to_dict()
    test_to_multiline()
    test_to_list()
    test_to_quoted()
    test_to_table()
    test_to_yaml()
    test_to_xml()
    test_to_key_value()
    test_to_markdown_table()
    test_to_dictlist()
    test_to_listdict()
    test_objects_with_dict()
    
    print("\n" + "=" * 60)
    print("✅ All hfortix_core.fmt tests passed!")
    print("=" * 60)
