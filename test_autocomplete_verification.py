"""
Test that autocomplete and type checking work correctly with the improved type hints.
"""

from hfortix_fortios import FortiOS

# Initialize client (default response_mode="dict")
fg = FortiOS(host="192.168.1.99", token="test-token")

# Test 1: Default behavior (no response_mode specified)
rule_default = fg.api.cmdb.authentication.rule.get(name="test_rule1")

# Should have autocomplete for srcintf
for intf in rule_default["srcintf"]:
    print(intf["name"])  # ✅ Should have autocomplete and show 'name' is valid
    print(intf["nonexistent_field"])  # ❌ Should show error for nonexistent field

# Should detect typo in field name
print(rule_default["srcintf1"])  # ❌ Should show error - 'srcintf1' doesn't exist

# Test 2: Explicit response_mode="dict"
rule_explicit = fg.api.cmdb.authentication.rule.get(name="test_rule1", response_mode="dict")

# Should have autocomplete for srcintf  
for intf in rule_explicit["srcintf"]:
    print(intf['name'])  # ✅ Should have autocomplete and show 'name' is valid
    print(intf["nonexistent_field"])  # ❌ Should show error for nonexistent field

# Test 3: Verify iteration works without "Never is not iterable" error
assert any(intf['name'] == "port3" for intf in rule_default['srcintf'])

print("✅ All type hints working correctly!")
