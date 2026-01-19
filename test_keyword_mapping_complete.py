"""Test Python keyword to API field mapping - comprehensive test."""

import sys
sys.path.insert(0, '/app/dev/classes/fortinet/packages/fortios')

from hfortix_fortios._helpers.builders import build_api_payload

print("=" * 60)
print("Testing Python Keyword to API Field Mapping")
print("=" * 60)

# Test 1: BGP AS number (asn -> as)
print("\n1. Testing BGP AS number (asn -> as):")
result1 = build_api_payload(asn="65000", router_id="0.0.0.0")
print(f"   Input: asn='65000', router_id='0.0.0.0'")
print(f"   Output: {result1}")
assert result1.get("as") == "65000", "asn should be converted to 'as'"
assert result1.get("router-id") == "0.0.0.0", "router_id should be converted to 'router-id'"
print("   ✅ PASS")

# Test 2: RADIUS class field (class_ -> class)
print("\n2. Testing RADIUS class field (class_ -> class):")
result2 = build_api_payload(class_=[{"name": "test-class"}])
print(f"   Input: class_=[{{'name': 'test-class'}}]")
print(f"   Output: {result2}")
assert result2.get("class") == [{"name": "test-class"}], "class_ should be converted to 'class'"
print("   ✅ PASS")

# Test 3: Firewall type field (type_ -> type)
print("\n3. Testing firewall type field (type_ -> type):")
result3 = build_api_payload(name="test-pool", type_="overload")
print(f"   Input: name='test-pool', type_='overload'")
print(f"   Output: {result3}")
assert result3.get("type") == "overload", "type_ should be converted to 'type'"
assert result3.get("name") == "test-pool", "name should remain as 'name'"
print("   ✅ PASS")

# Test 4: Mixed keywords and regular fields
print("\n4. Testing mixed keywords and regular fields:")
result4 = build_api_payload(
    asn="65001",
    router_id="1.1.1.1",
    type_="static",
    class_=[{"name": "premium"}],
    interface_name="port1"
)
print(f"   Input: asn, router_id, type_, class_, interface_name")
print(f"   Output: {result4}")
assert result4.get("as") == "65001", "asn -> as"
assert result4.get("router-id") == "1.1.1.1", "router_id -> router-id"
assert result4.get("type") == "static", "type_ -> type"
assert result4.get("class") == [{"name": "premium"}], "class_ -> class"
assert result4.get("interface-name") == "port1", "interface_name -> interface-name"
print("   ✅ PASS")

# Test 5: Fields with trailing underscore (from_, import_, global_)
print("\n5. Testing other keyword fields (from_, import_, global_):")
result5 = build_api_payload(
    from_="source",
    import_="external",
    global_="yes"
)
print(f"   Input: from_='source', import_='external', global_='yes'")
print(f"   Output: {result5}")
assert result5.get("from") == "source", "from_ -> from"
assert result5.get("import") == "external", "import_ -> import"
assert result5.get("global") == "yes", "global_ -> global"
print("   ✅ PASS")

print("\n" + "=" * 60)
print("✅ All keyword mapping tests passed!")
print("=" * 60)
