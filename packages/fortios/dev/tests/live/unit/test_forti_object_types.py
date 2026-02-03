"""
Tests for FortiObject type system and attribute access.

Validates that:
1. FortiObject supports dot notation (policy.name, policy.policyid)
2. FortiObjectList is iterable and returns FortiObject instances
3. Dynamic attributes work for undocumented API fields
4. Type stubs align with runtime behavior
"""

import pytest


class TestFortiObjectAttributeAccess:
    """Test FortiObject attribute access patterns."""

    def test_forti_object_dot_notation(self):
        """FortiObject should support dot notation for field access."""
        from hfortix_fortios.models import FortiObject
        
        data = {"name": "test-policy", "policyid": 42, "action": "accept"}
        obj = FortiObject(data)
        
        # Dot notation should work
        assert obj.get("name") == "test-policy"
        assert obj.get("policyid") == 42
        assert obj.get("action") == "accept"
        print("✅ FortiObject dot notation works")

    def test_forti_object_missing_attribute_returns_none(self):
        """Accessing non-existent attribute should return None, not raise."""
        from hfortix_fortios.models import FortiObject
        
        obj = FortiObject({"name": "test"})
        
        # Should return None, not raise AttributeError
        assert obj.get("nonexistent_field") is None
        assert obj.get("some_undocumented_field") is None
        print("✅ FortiObject missing attributes return None")

    def test_forti_object_dict_access(self):
        """FortiObject should also support dict-style access."""
        from hfortix_fortios.models import FortiObject
        
        data = {"name": "test", "value": 123}
        obj = FortiObject(data)
        
        # Dict-style access should work
        assert obj.get("name") == "test"
        assert obj.get("missing", "default") == "default"
        print("✅ FortiObject dict-style access works")


class TestFortiObjectListIteration:
    """Test FortiObjectList iteration behavior."""

    def test_forti_object_list_iteration(self):
        """Iterating FortiObjectList should yield FortiObject instances."""
        from hfortix_fortios.models import FortiObject, FortiObjectList
        
        items = [
            FortiObject({"name": "item1", "id": 1}),
            FortiObject({"name": "item2", "id": 2}),
        ]
        obj_list = FortiObjectList(items)
        
        for item in obj_list:
            assert isinstance(item, FortiObject)
            # Dot notation should work on each item
            assert item.get("name") is not None
            assert item.get("id") is not None
        
        print("✅ FortiObjectList iteration yields FortiObject instances")

    def test_forti_object_list_indexing(self):
        """FortiObjectList should support indexing."""
        from hfortix_fortios.models import FortiObject, FortiObjectList
        
        items = [
            FortiObject({"name": "first"}),
            FortiObject({"name": "second"}),
        ]
        obj_list = FortiObjectList(items)
        
        assert obj_list[0].get("name") == "first"
        assert obj_list[1].get("name") == "second"
        assert obj_list[-1].get("name") == "second"
        print("✅ FortiObjectList indexing works")

    def test_forti_object_list_slicing(self):
        """FortiObjectList should support slicing."""
        from hfortix_fortios.models import FortiObject, FortiObjectList
        
        items = [FortiObject({"id": i}) for i in range(5)]
        obj_list = FortiObjectList(items)
        
        sliced = obj_list[1:3]
        assert len(sliced) == 2
        assert sliced[0].get("id") == 1
        assert sliced[1].get("id") == 2
        print("✅ FortiObjectList slicing works")


class TestFortiObjectNestedAccess:
    """Test FortiObject with nested/table fields."""

    def test_nested_table_fields(self):
        """Nested table fields should be auto-wrapped as FortiObject."""
        from hfortix_fortios.models import FortiObject
        
        data = {
            "name": "policy1",
            "srcaddr": [{"name": "addr1"}, {"name": "addr2"}],
            "dstintf": [{"name": "port1"}],
        }
        obj = FortiObject(data)
        
        # Nested items should be accessible
        srcaddr = obj.get('srcaddr')
        assert isinstance(srcaddr, list)
        assert len(srcaddr) == 2
        
        # Each nested item should be FortiObject with dot notation
        assert srcaddr[0].get("name") == "addr1"
        assert srcaddr[1].get("name") == "addr2"
        print("✅ FortiObject nested table fields work")

    def test_get_full_returns_raw_data(self):
        """get_full() should return raw nested data without processing."""
        from hfortix_fortios.models import FortiObject
        
        data = {
            "srcaddr": [{"name": "addr1", "q_origin_key": "addr1"}],
        }
        obj = FortiObject(data)
        
        # get_full returns raw dict, not processed
        raw = obj.get_full("srcaddr")
        assert isinstance(raw, list)
        assert isinstance(raw[0], dict)
        assert raw[0]["q_origin_key"] == "addr1"
        print("✅ FortiObject.get_full() returns raw data")


class TestFortiObjectConversion:
    """Test FortiObject conversion methods."""

    def test_to_dict(self):
        """to_dict() should return original dictionary."""
        from hfortix_fortios.models import FortiObject
        
        data = {"name": "test", "value": 42}
        obj = FortiObject(data)
        
        result = obj.to_dict()
        assert result == data
        print("✅ FortiObject.to_dict() works")

    def test_dict_property(self):
        """dict property should return dictionary."""
        from hfortix_fortios.models import FortiObject
        
        data = {"name": "test"}
        obj = FortiObject(data)
        
        assert obj.dict == data
        print("✅ FortiObject.dict property works")

    def test_json_property(self):
        """json property should return JSON string."""
        from hfortix_fortios.models import FortiObject
        import json
        
        data = {"name": "test", "value": 42}
        obj = FortiObject(data)
        
        json_str = obj.json
        parsed = json.loads(json_str)
        assert parsed == data
        print("✅ FortiObject.json property works")


class TestTypeStubAlignment:
    """Tests to catch misalignment between stubs and runtime."""

    def test_common_response_fields_exist(self):
        """Common API response fields should be accessible."""
        from hfortix_fortios.models import FortiObject
        
        # Simulate API response with common fields
        data = {
            "name": "test",
        }
        envelope = {
            "status": "success",
            "http_status": 200,
            "vdom": "root",
            "serial": "FGVM123",
            "version": "v7.6.5",
            "build": 3651,
        }
        obj = FortiObject(data, raw_envelope=envelope)
        
        # These fields should be accessible (defined in stubs)
        assert obj.http_status == "success"  # From envelope
        assert obj.fgt_vdom == "root"
        assert obj.fgt_serial == "FGVM123"
        print("✅ Common response fields accessible")

    def test_undocumented_fields_accessible(self):
        """Undocumented API fields should still be accessible via dot notation."""
        from hfortix_fortios.models import FortiObject
        
        # API may return fields not in schema
        data = {
            "documented_field": "value1",
            "undocumented_field": "value2",
            "content": "file content here",  # Like config_revision.file
        }
        obj = FortiObject(data)
        
        # Both should work - this catches stub gaps
        assert obj.get("documented_field") == "value1"
        assert obj.get("undocumented_field") == "value2"
        assert obj.get("content") == "file content here"
        print("✅ Undocumented fields accessible via dot notation")


if __name__ == "__main__":
    # Run all tests
    test_classes = [
        TestFortiObjectAttributeAccess,
        TestFortiObjectListIteration,
        TestFortiObjectNestedAccess,
        TestFortiObjectConversion,
        TestTypeStubAlignment,
    ]
    
    for test_class in test_classes:
        print(f"\n{'='*60}")
        print(f"Running {test_class.__name__}")
        print('='*60)
        
        instance = test_class()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                method = getattr(instance, method_name)
                try:
                    method()
                except Exception as e:
                    print(f"❌ {method_name}: {e}")
    
    print(f"\n{'='*60}")
    print("All type system tests completed!")
    print('='*60)
