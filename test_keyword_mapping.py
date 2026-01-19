"""Test Python keyword to API field mapping."""

import sys
sys.path.insert(0, '/app/dev/classes/fortinet/packages/fortios')

from hfortix_fortios._helpers.builders import build_api_payload

# Test the keyword mapping
# Pass keyword arguments directly, not as a dict
result = build_api_payload(
    asn="65000",
    router_id="0.0.0.0",
    other_field="test"
)

print("Converted payload:")
print(result)
print("\nExpected 'as' field:", result.get("as"))
print("Expected 'router-id' field:", result.get("router-id"))
print("Expected 'other-field' field:", result.get("other-field"))

# Verify the conversion
assert result.get("as") == "65000", "asn should be converted to 'as'"
assert result.get("router-id") == "0.0.0.0", "router_id should be converted to 'router-id'"
assert result.get("other-field") == "test", "other_field should be converted to 'other-field'"

print("\n✅ All tests passed!")
