from hfortix_fortios import FortiOS

# Verify we're using local code
import hfortix_fortios
import json
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")

# Disable circuit breaker for testing by setting a very high threshold
# This allows tests to run without being blocked by protective circuit breaker
fgt: FortiOS = FortiOS(
    host="192.168.1.99", 
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1", 
    port=443, 
    verify=False, 
    error_mode="return", 
    vdom="test",  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1  # Short timeout if it does trigger
)


addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    if addr.name.startswith("test_") or addr.name.startswith("Test_"):
        print(f"Deleting address {addr.name} with ID {addr.name}")
        fgt.api.cmdb.firewall.address.delete(name=addr.name)


result = fgt.api.cmdb.firewall.address.post(
    name="Test_Address2",
    subnet="192.168.0.0/24"
)


raw_response = result.raw

print(raw_response.get('revision'))  

config_revision_meta = fgt.api.monitor.system.config_revision.info.get(config_id=45)
print(config_revision_meta.raw)