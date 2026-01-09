"""Verify that iteration over .get() results works without type errors."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_fortios.api.v2.cmdb.firewall.policy import PolicyResponse, PolicyObject

from hfortix_fortios import FortiOS


def test_dict_mode_default():
    """Test that default mode (dict) works with iteration."""
    fg = FortiOS(host="192.168.1.99", token="token")
    
    # Default mode should return list[PolicyResponse] (TypedDict)
    policies = fg.api.cmdb.firewall.policy.get()
    
    # This should work without errors - policies should be list[PolicyResponse]
    for policy in policies:
        print(policy["name"])  # ✅ Should work
        print(policy["action"])  # ✅ Should work
        
    # Accessing first element should also work
    if policies:
        first = policies[0]
        print(first["name"])  # ✅ Should work


def test_dict_mode_explicit():
    """Test that explicit dict mode works with iteration."""
    fg = FortiOS(host="192.168.1.99", token="token")
    
    # Explicit dict mode
    policies = fg.api.cmdb.firewall.policy.get(response_mode="dict")
    
    # Should work without errors
    for policy in policies:
        print(policy["name"])  # ✅ Should work
        print(policy["action"])  # ✅ Should work


def test_object_mode():
    """Test that object mode works with iteration."""
    fg = FortiOS(host="192.168.1.99", token="token")
    
    # Object mode should return list[PolicyObject]
    policies = fg.api.cmdb.firewall.policy.get(response_mode="object")
    
    # Should work without errors
    for policy in policies:
        print(policy.name)  # ✅ Should work
        print(policy.action)  # ✅ Should work
        
    # Accessing first element should also work
    if policies:
        first = policies[0]
        print(first.name)  # ✅ Should work


def test_single_item_dict():
    """Test that getting a single item in dict mode works."""
    fg = FortiOS(host="192.168.1.99", token="token")
    
    # Get single item - should return PolicyResponse (not list)
    policy = fg.api.cmdb.firewall.policy.get(policyid=1)
    
    # Should work - policy is PolicyResponse, not list
    print(policy["name"])  # ✅ Should work
    print(policy["action"])  # ✅ Should work


def test_single_item_object():
    """Test that getting a single item in object mode works."""
    fg = FortiOS(host="192.168.1.99", token="token")
    
    # Get single item - should return PolicyObject (not list)
    policy = fg.api.cmdb.firewall.policy.get(policyid=1, response_mode="object")
    
    # Should work - policy is PolicyObject, not list
    print(policy.name)  # ✅ Should work
    print(policy.action)  # ✅ Should work


if __name__ == "__main__":
    test_dict_mode_default()
    test_dict_mode_explicit()
    test_object_mode()
    test_single_item_dict()
    test_single_item_object()
