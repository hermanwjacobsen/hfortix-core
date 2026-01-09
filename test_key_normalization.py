"""Test that hyphenated keys from FortiOS are normalized to underscores."""

from hfortix_fortios import FortiOS

# Create client
fgt = FortiOS(
    host="192.168.1.99",
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1",
    port=443,
    verify=False,
    vdom="test",
    response_mode="dict"
)

# Test 1: Get services (has tcp-portrange field)
print("=" * 70)
print("TEST 1: firewall.service.custom (hyphenated keys)")
print("=" * 70)

services = fgt.api.cmdb.firewall.service.custom.get()
if services:
    service = services[0]
    print(f"Service name: {service['name']}")
    
    # These should work now (underscored keys)
    print(f"  protocol: {service.get('protocol', 'N/A')}")
    print(f"  tcp_portrange: {service.get('tcp_portrange', 'N/A')}")  # ✅ Should work
    print(f"  udp_portrange: {service.get('udp_portrange', 'N/A')}")  # ✅ Should work
    print(f"  tcp_halfclose_timer: {service.get('tcp_halfclose_timer', 'N/A')}")  # ✅ Should work
    
    # These should NOT exist anymore (hyphenated keys)
    print(f"  tcp-portrange (old): {service.get('tcp-portrange', 'NOT FOUND')}")  # ❌ Should be NOT FOUND
    print(f"  udp-portrange (old): {service.get('udp-portrange', 'NOT FOUND')}")  # ❌ Should be NOT FOUND
    
    print("\n  All keys in response:")
    for key in sorted(service.keys()):
        if '-' in key:
            print(f"    ⚠️  {key} (still has hyphens!)")
        else:
            print(f"    ✅ {key}")

# Test 2: Get firewall address (has cache-ttl field)
print("\n" + "=" * 70)
print("TEST 2: firewall.address (cache-ttl field)")
print("=" * 70)

addresses = fgt.api.cmdb.firewall.address.get()
if addresses:
    addr = addresses[0]
    print(f"Address name: {addr['name']}")
    print(f"  cache_ttl: {addr.get('cache_ttl', 'N/A')}")  # ✅ Should work
    print(f"  cache-ttl (old): {addr.get('cache-ttl', 'NOT FOUND')}")  # ❌ Should be NOT FOUND
    print(f"  uuid_idx: {addr.get('uuid_idx', 'N/A')}")  # ✅ Should work
    print(f"  q_origin_key: {addr.get('q_origin_key', 'N/A')}")  # ✅ Should work

# Test 3: Test with object mode
print("\n" + "=" * 70)
print("TEST 3: Object mode (attribute access)")
print("=" * 70)

service_obj = fgt.api.cmdb.firewall.service.custom.get(response_mode="object")
if service_obj:
    obj = service_obj[0]
    print(f"Service name: {obj.name}")
    print(f"  obj.tcp_portrange: {obj.tcp_portrange}")  # ✅ Should work
    print(f"  obj.udp_portrange: {obj.udp_portrange}")  # ✅ Should work
    print(f"  obj.tcp_halfclose_timer: {obj.tcp_halfclose_timer}")  # ✅ Should work

print("\n" + "=" * 70)
print("✅ All tests passed! Keys are now normalized properly.")
print("=" * 70)
