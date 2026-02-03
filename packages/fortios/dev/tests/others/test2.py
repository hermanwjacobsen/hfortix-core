
from hfortix_fortios import FortiManagerProxy
import json

# Force reload to pick up latest changes during development
import importlib
import hfortix_fortios.models
import hfortix_fortios.fmg_proxy.models
importlib.reload(hfortix_fortios.models)
importlib.reload(hfortix_fortios.fmg_proxy.models)

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")


# =============================================================================
# Basic Connection
# =============================================================================

# # Connect to FortiManager
# fmg = FortiManagerProxy(
#     host="fortimanager.example.com",
#     username="admin",
#     password="password",
#     verify=False,  # Set True in production with valid certs
#     adom="BUS",   # Default ADOM
# )

# fgt = fmg.proxy(device="BUS-HJA-FW101")


# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    verify=False,  # Set True in production with valid certs
    adom="HWJ",   # Default ADOM
)

# Get a proxied FortiOS client for a specific device
fgt = fmg.proxy(device="hwj-fw", vdom="root")

policies = fgt.api.cmdb.firewall.policy.get()
print("Firewall Policies:")
for policy in policies:    
    print(f"- ID: {policy.policyid}, Name: {policy.name}")

print(policies.http_status_code)

psirt = fgt.api.service.security_rating.report.get(type="psirt", scope="global")


print(f"Type: {type(psirt)}")
print(f"Value: {psirt}")
print(f"HTTP Status: {psirt.http_status_code}")
print(f"Raw: {psirt.raw}")