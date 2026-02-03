from os import name
from time import sleep
from hfortix_fortios import FortiOS

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")

fgt: FortiOS = FortiOS(
    host="192.168.1.99", 
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1", 
    port=443, 
    verify=False, 
    error_mode="return", 
    vdom="root",  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1  # Short timeout if it does trigger
)

# policies = fgt.api.cmdb.firewall.policy.get()
# for policy in policies:    
#     print(f"- ID: {policy.policyid}, Name: {policy.name}")
#     policy_id_details = fgt.api.cmdb.firewall.policy.get(policyid=policy.policyid)
#     print(f"  Details: {policy_id_details.raw}")

# addresses = fgt.api.cmdb.firewall.address.get()
# for addr in addresses:
#     print(f"- Name: {addr.name}, Subnet: {addr.subnet}")
#     address_details = fgt.api.cmdb.firewall.address.get(name=addr.name) 
#     print(f"  Details: {address_details.raw}")

"""Test: Update BGP Neighbor - Not implemented (part of BGP config structure)."""
current_config = fgt.api.cmdb.router.bgp.get()
result = fgt.api.cmdb.router.bgp.put(
    asn=str(current_config.asn),
    router_id=str(current_config.router_id),
    neighbor=[
        {
            "ip": "1.1.1.1",
            "remote_as": "65010",
        }
    ]
)
verify = fgt.api.cmdb.router.bgp.get()
# Verification of neighbor addition would go here
assert result is not None
assert result.http_status == "success"
for neighbor in verify.neighbor:
     print(neighbor.json)



