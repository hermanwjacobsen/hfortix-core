"""
Tests for FortiObject type system and attribute access.

Validates that:
1. FortiObject supports dot notation (policy.name, policy.policyid)
2. FortiObjectList is iterable and returns FortiObject instances
3. Dynamic attributes work for undocumented API fields
4. Type stubs align with runtime behavior

Note: This test file specifically tests runtime __getattr__ behavior.
Pylance warnings are expected here since we're testing dynamic attributes.
In production code, use typed endpoint objects (PolicyObject, AddressObject, etc.)
which provide full autocomplete and type safety.
"""

from typing import Any
import pytest


class TestFortiObjectAttributeAccess:
    """Test FortiObject attribute access patterns."""

    def test_forti_object_dot_notation(self):
        """FortiObject should support dot notation for field access."""
        from hfortix_fortios.models import FortiObject
        
        data = {"name": "test-policy", "policyid": 42, "action": "accept"}
        obj = FortiObject(data)
        
        # Dot notation works at runtime via __getattr__
        # Type checker warnings are expected for generic FortiObject
        # Use typed subclasses (PolicyObject, etc.) in production code
        assert obj.name == "test-policy"  # type: ignore[attr-defined]
        assert obj.policyid == 42  # type: ignore[attr-defined]
        assert obj.action == "accept"  # type: ignore[attr-defined]
        print("✅ FortiObject dot notation works")

    def test_forti_object_missing_attribute_returns_none(self):
        """Accessing non-existent attribute should return None, not raise."""
        from hfortix_fortios.models import FortiObject
        
        obj = FortiObject({"name": "test"})
        
        # Should return None, not raise AttributeError
        assert obj.nonexistent_field is None  # type: ignore[attr-defined]
        assert obj.some_undocumented_field is None  # type: ignore[attr-defined]
        print("✅ FortiObject missing attributes return None")
    
    def test_forti_object_type_safe_access(self):
        """Demonstrate type-safe ways to access FortiObject data."""
        from hfortix_fortios.models import FortiObject
        
        data = {"name": "test-policy", "policyid": 42, "action": "accept"}
        obj = FortiObject(data)
        
        # Method 1: Use get_full() - type-safe
        assert obj.get_full("name") == "test-policy"
        assert obj.get_full("policyid") == 42
        
        # Method 2: Use to_dict() - type-safe
        obj_dict = obj.to_dict()
        assert obj_dict["name"] == "test-policy"
        assert obj_dict["policyid"] == 42
        
        # Method 3: Use .dict property - type-safe
        assert obj.dict["name"] == "test-policy"
        
        # Method 4: Check existence first - type-safe
        assert "name" in obj
        assert "policyid" in obj
        
        print("✅ FortiObject type-safe access methods")