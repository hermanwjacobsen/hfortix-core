"""Verify that response_mode set at client level propagates correctly."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_fortios.api.v2.cmdb.firewall.policy import PolicyResponse, PolicyObject

from hfortix_fortios import FortiOS


def test_client_level_dict_mode():
    """Test that response_mode='dict' at client level works."""
    # Create client with dict mode (explicit)
    fg_dict = FortiOS(host="192.168.1.99", token="token", response_mode="dict")
    
    # Get policies - should return list[PolicyResponse] by default
    policies = fg_dict.api.cmdb.firewall.policy.get()
    
    # Should work without errors
    for policy in policies:
        print(policy["name"])  # ✅ Should work
        print(policy["action"])  # ✅ Should work


def test_client_level_object_mode():
    """Test that response_mode='object' at client level works."""
    # Create client with object mode
    fg_obj = FortiOS(host="192.168.1.99", token="token", response_mode="object")
    
    # Get policies - should return list[PolicyObject] by default
    policies = fg_obj.api.cmdb.firewall.policy.get()
    
    # Should work without errors
    for policy in policies:
        print(policy.name)  # ✅ Should work
        print(policy.action)  # ✅ Should work


def test_client_default_mode():
    """Test that client without response_mode defaults to dict."""
    # Create client without specifying response_mode
    fg = FortiOS(host="192.168.1.99", token="token")
    
    # Should default to dict mode
    policies = fg.api.cmdb.firewall.policy.get()
    
    # Should work with dict access
    for policy in policies:
        print(policy["name"])  # ✅ Should work


def test_override_client_mode():
    """Test that endpoint-level response_mode overrides client-level."""
    # Create client with object mode
    fg_obj = FortiOS(host="192.168.1.99", token="token", response_mode="object")
    
    # Override with dict mode at endpoint level
    policies_dict = fg_obj.api.cmdb.firewall.policy.get(response_mode="dict")
    
    # Should work with dict access (override worked)
    for policy in policies_dict:
        print(policy["name"])  # ✅ Should work
    
    # Get with object mode at endpoint level
    policies_obj = fg_obj.api.cmdb.firewall.policy.get(response_mode="object")
    
    # Should work with object access
    for policy in policies_obj:
        print(policy.name)  # ✅ Should work


if __name__ == "__main__":
    test_client_level_dict_mode()
    test_client_level_object_mode()
    test_client_default_mode()
    test_override_client_mode()
