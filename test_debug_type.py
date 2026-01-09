"""Minimal test for type checking."""
from hfortix_fortios import FortiOS
from hfortix_fortios.cmdb.authentication.rule import Rule

# Direct import test
from typing import reveal_type  # type: ignore

fgt = FortiOS(host="192.168.1.99", token="test-token")

# Get the rule endpoint
rule_endpoint = fgt.api.cmdb.authentication.rule
reveal_type(rule_endpoint)  # Should be Rule

# Call get with name keyword arg - NO response_mode
result = rule_endpoint.get(name="test")
reveal_type(result)  # Should be RuleResponse

# Access a field
print(result["name"])

# Test chained access (like the failing test)
result2 = fgt.api.cmdb.authentication.rule.get(name="test_rule1")
reveal_type(result2)

# Try to iterate srcintf
for intf in result2["srcintf"]:
    print(intf["name"])


def test_in_function():
    """Test inside a function - does it behave differently?"""
    rule = fgt.api.cmdb.authentication.rule.get(name="test_rule1")
    reveal_type(rule)
    # Try to iterate srcintf
    for intf in rule['srcintf']:
        print(intf['name'])
    # Test with any() like the failing test
    assert any(intf['name'] == "port3" for intf in rule['srcintf'])
