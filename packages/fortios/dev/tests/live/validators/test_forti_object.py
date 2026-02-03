"""
Tests for hfortix_fortios FortiObject class.

FortiObject is a wrapper around dict data returned from FortiOS API
that provides attribute-style access and automatic member_table handling.

BUGS FOUND:
- BUG #3: __getattr__ doesn't convert underscore to hyphen for key lookup.
  Accessing obj.list_data when the key is "list-data" returns None.
  The hyphen-to-underscore conversion works the OTHER way (normalize_keys),
  but FortiObject doesn't reverse it for attribute access.
  FIX: In __getattr__, try: self._data.get(name) OR self._data.get(name.replace('_', '-'))

- BUG #4: get(key, default) ignores the default value!
  Because __getattr__ returns None for missing keys (instead of raising
  AttributeError), the try/except in get() never catches an exception,
  so the default is never returned.
  FIX: Use `if key in self._data: return getattr(self, key) else: return default`
  OR: Check for None and use default, but that breaks if value is actually None
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
    from hfortix_fortios import FortiObject  # type: ignore[attr-defined]

    passed = 0
    failed = 0
    tests = []

    # =================================================================
    # Basic Initialization Tests
    # =================================================================

    # Test 1: Initialize with simple dict
    def test_init_simple_dict():
        data = {"name": "test", "status": "enable"}
        obj = FortiObject(data)
        assert obj._data == data
        return True, None

    tests.append(("Initialize with simple dict", test_init_simple_dict))

    # Test 2: Initialize with empty dict
    def test_init_empty_dict():
        obj = FortiObject({})
        assert obj._data == {}
        return True, None

    tests.append(("Initialize with empty dict", test_init_empty_dict))

    # Test 3: Initialize with nested dict
    def test_init_nested_dict():
        data = {"name": "test", "config": {"port": 443, "ssl": True}}
        obj = FortiObject(data)
        assert obj._data["config"]["port"] == 443
        return True, None

    tests.append(("Initialize with nested dict", test_init_nested_dict))

    # =================================================================
    # Attribute Access Tests
    # =================================================================

    # Test 4: Access simple attribute
    def test_attr_simple():
        obj = FortiObject({"name": "firewall-policy", "action": "accept"})
        assert obj.name == "firewall-policy"
        assert obj.action == "accept"
        return True, None

    tests.append(("Access simple attribute", test_attr_simple))

    # Test 5: Access numeric attribute
    def test_attr_numeric():
        obj = FortiObject({"port": 443, "count": 0})
        assert obj.port == 443
        assert obj.count == 0
        return True, None

    tests.append(("Access numeric attribute", test_attr_numeric))

    # Test 6: Access missing attribute returns None
    def test_attr_missing():
        obj = FortiObject({"name": "test"})
        result = obj.missing_field
        assert result is None, f"Expected None, got {result}"
        return True, None

    tests.append(("Access missing attribute returns None", test_attr_missing))

    # Test 7: Access private attribute raises AttributeError
    def test_attr_private():
        obj = FortiObject({"name": "test"})
        try:
            _ = obj._private
            return False, "Expected AttributeError for private attribute"
        except AttributeError:
            return True, None

    tests.append(("Access private attribute raises AttributeError", test_attr_private))

    # Test 8: BUG #3 - Hyphenated key via underscore attribute access
    # This test documents the bug - accessing hyphenated keys via underscore fails
    def test_attr_hyphen_to_underscore_BUG():
        obj = FortiObject({"list-data": [1, 2, 3], "user-name": "admin"})
        # BUG: obj.list_data should return [1, 2, 3] but returns None
        # because __getattr__ doesn't convert underscore to hyphen
        result = obj.list_data
        if result is None:
            return False, "BUG: obj.list_data returns None for key 'list-data'. __getattr__ doesn't convert _ to -"
        assert result == [1, 2, 3]
        return True, None

    tests.append(("BUG #3: Hyphenated key via underscore attribute", test_attr_hyphen_to_underscore_BUG))

    # =================================================================
    # get() Method Tests
    # =================================================================

    # Test 9: get() with existing key
    def test_get_existing():
        obj = FortiObject({"name": "test", "status": "enable"})
        assert obj.get("name") == "test"
        assert obj.get("status") == "enable"
        return True, None

    tests.append(("get() with existing key", test_get_existing))

    # Test 10: get() with missing key returns None
    def test_get_missing():
        obj = FortiObject({"name": "test"})
        result = obj.get("missing")
        assert result is None
        return True, None

    tests.append(("get() with missing key returns None", test_get_missing))

    # Test 11: BUG #4 - get() with default value is ignored
    def test_get_default_BUG():
        obj = FortiObject({"name": "test"})
        result = obj.get("missing", "default_value")
        # BUG: The default is ignored because __getattr__ returns None
        # instead of raising AttributeError for missing keys
        if result is None:
            return False, "BUG: get('missing', 'default') returns None, ignoring default value"
        assert result == "default_value", f"Expected 'default_value', got {result}"
        return True, None

    tests.append(("BUG #4: get() default value ignored", test_get_default_BUG))

    # Test 12: get() with hyphenated key
    def test_get_hyphenated_key():
        obj = FortiObject({"list-data": [1, 2, 3]})
        # Direct key access via get() should work
        result = obj.get("list-data")
        assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"
        return True, None

    tests.append(("get() with hyphenated key", test_get_hyphenated_key))

    # =================================================================
    # get_full() Method Tests
    # =================================================================

    # Test 13: get_full() returns raw value
    def test_get_full_raw():
        obj = FortiObject({"srcaddr": [{"name": "addr1"}, {"name": "addr2"}]})
        result = obj.get_full("srcaddr")
        # get_full should return raw data, not wrapped
        assert result == [{"name": "addr1"}, {"name": "addr2"}]
        assert isinstance(result[0], dict)  # Not FortiObject
        return True, None

    tests.append(("get_full() returns raw value", test_get_full_raw))

    # Test 14: get_full() vs attribute access for member_table
    def test_get_full_vs_attr():
        obj = FortiObject({"srcaddr": [{"name": "addr1", "extra": "data"}]})
        raw = obj.get_full("srcaddr")
        wrapped = obj.srcaddr
        assert isinstance(raw, list)
        assert isinstance(wrapped, list)
        assert isinstance(raw[0], dict)
        assert isinstance(wrapped[0], FortiObject)
        return True, None

    tests.append(("get_full() vs attribute access for member_table", test_get_full_vs_attr))

    # =================================================================
    # Member Table Auto-Wrapping Tests
    # =================================================================

    # Test 15: List of dicts gets wrapped in FortiObject
    def test_member_table_wrapping():
        obj = FortiObject({"srcaddr": [{"name": "all"}, {"name": "internal"}]})
        result = obj.srcaddr
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], FortiObject)
        assert result[0].name == "all"
        return True, None

    tests.append(("Member table gets wrapped in FortiObject", test_member_table_wrapping))

    # Test 16: Empty list not wrapped
    def test_empty_list_not_wrapped():
        obj = FortiObject({"empty_list": []})
        result = obj.empty_list
        assert result == []
        return True, None

    tests.append(("Empty list not wrapped", test_empty_list_not_wrapped))

    # Test 17: List of non-dicts not wrapped
    def test_list_non_dict_not_wrapped():
        obj = FortiObject({"ports": [80, 443, 8080]})
        result = obj.ports
        assert isinstance(result, list)
        assert result == [80, 443, 8080]
        assert isinstance(result[0], int)
        return True, None

    tests.append(("List of non-dicts not wrapped", test_list_non_dict_not_wrapped))

    # Test 18: Nested FortiObject access
    def test_nested_forti_object():
        obj = FortiObject({
            "srcaddr": [{"name": "addr1", "type": "subnet", "subnet": "10.0.0.0/8"}]
        })
        srcaddr = obj.srcaddr
        assert isinstance(srcaddr, list)
        addr = srcaddr[0]
        assert addr.name == "addr1"
        assert addr.type == "subnet"
        assert addr.subnet == "10.0.0.0/8"
        return True, None

    tests.append(("Nested FortiObject access", test_nested_forti_object))

    # =================================================================
    # Dict-like Interface Tests
    # =================================================================

    # Test 19: keys() method
    def test_keys():
        obj = FortiObject({"name": "test", "status": "enable", "port": 443})
        keys = list(obj.keys())
        assert "name" in keys
        assert "status" in keys
        assert "port" in keys
        assert len(keys) == 3
        return True, None

    tests.append(("keys() method", test_keys))

    # Test 20: values() method
    def test_values():
        obj = FortiObject({"name": "test", "port": 443})
        values = list(obj.values())
        assert "test" in values
        assert 443 in values
        return True, None

    tests.append(("values() method", test_values))

    # Test 21: items() method
    def test_items():
        obj = FortiObject({"name": "test", "port": 443})
        items = list(obj.items())
        assert ("name", "test") in items
        assert ("port", 443) in items
        return True, None

    tests.append(("items() method", test_items))

    # Test 22: to_dict() method
    def test_to_dict():
        data = {"name": "test", "status": "enable", "nested": {"key": "value"}}
        obj = FortiObject(data)
        result = obj.to_dict()
        assert result == data
        # NOTE: to_dict() returns the same reference, not a copy
        # This is by design (returns original API response)
        return True, None

    tests.append(("to_dict() method", test_to_dict))

    # Test 23: __getitem__ access
    def test_getitem():
        obj = FortiObject({"name": "test", "list-data": [1, 2, 3]})
        assert obj["name"] == "test"
        assert obj["list-data"] == [1, 2, 3]
        return True, None

    tests.append(("__getitem__ bracket access", test_getitem))

    # =================================================================
    # Edge Cases
    # =================================================================

    # Test 24: None values
    def test_none_values():
        obj = FortiObject({"name": None, "config": None})
        assert obj.name is None
        assert obj.config is None
        return True, None

    tests.append(("None values handled", test_none_values))

    # Test 25: Boolean values
    def test_boolean_values():
        obj = FortiObject({"enabled": True, "disabled": False})
        assert obj.enabled is True
        assert obj.disabled is False
        return True, None

    tests.append(("Boolean values handled", test_boolean_values))

    # Test 26: Mixed list (dict and non-dict) - edge case
    def test_mixed_list():
        # What happens with mixed list? First element is checked
        obj = FortiObject({"mixed": [{"name": "dict"}, "string", 123]})
        result = obj.mixed
        assert isinstance(result, list)
        # Since first element is dict, all should be wrapped
        assert isinstance(result[0], FortiObject)
        # But wrapping non-dict will fail if code doesn't handle it
        return True, None

    tests.append(("Mixed list handling", test_mixed_list))

    # Test 27: Deeply nested structure
    def test_deeply_nested():
        obj = FortiObject({
            "policy": [{
                "name": "policy1",
                "srcaddr": [{"name": "addr1"}],
                "dstaddr": [{"name": "addr2"}]
            }]
        })
        policy_list = obj.policy
        assert isinstance(policy_list, list)
        policy = policy_list[0]
        assert isinstance(policy, FortiObject)
        # Note: srcaddr inside the wrapped FortiObject is raw data
        # because it's a new FortiObject wrapping the inner dict
        srcaddr = policy.srcaddr
        assert isinstance(srcaddr, list)
        assert isinstance(srcaddr[0], FortiObject)
        return True, None

    tests.append(("Deeply nested structure", test_deeply_nested))

    # =================================================================
    # json Property Tests
    # =================================================================

    # Test: json property returns raw dict
    def test_json_property_returns_dict():
        data = {"name": "test", "status": "enable"}
        obj = FortiObject(data)
        assert obj.json == data
        assert isinstance(obj.json, dict)
        return True, None

    tests.append(("json property returns raw dict", test_json_property_returns_dict))

    # Test: json property returns same reference as _data
    def test_json_property_same_as_data():
        data = {"name": "test", "nested": {"key": "value"}}
        obj = FortiObject(data)
        assert obj.json is obj._data
        return True, None

    tests.append(("json property same as _data", test_json_property_same_as_data))

    # Test: json property with empty dict
    def test_json_property_empty():
        obj = FortiObject({})
        assert obj.json == {}
        return True, None

    tests.append(("json property with empty dict", test_json_property_empty))

    # Test: json property with nested data
    def test_json_property_nested():
        data = {"name": "test", "config": {"port": 443, "enabled": True}}
        obj = FortiObject(data)
        assert obj.json["config"]["port"] == 443
        assert obj.json["config"]["enabled"] is True
        return True, None

    tests.append(("json property with nested data", test_json_property_nested))

    # =================================================================
    # Run All Tests
    # =================================================================

    print(f"\n{Colors.BOLD}FortiObject Tests{Colors.RESET}")
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
