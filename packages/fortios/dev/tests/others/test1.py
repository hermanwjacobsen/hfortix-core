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


get_interface = fgt.api.cmdb.system.interface.get(vdom="test")

for intf in get_interface:
    if intf.name.startswith("port"):
        if hasattr(intf, 'ipv6') and intf.ipv6:
            print(intf.ipv6.ip6_address)  # ✅ Now works at runtime!
            print(intf.ipv6.ip6_mode)     # ✅ Attribute access!
            print(intf.ipv6.ip6_send_adv) # ✅ With autocomplete!

try:
    addresses = fgt.api.cmdb.firewall.address.get()
    for addr in addresses:
        if addr.name == "test_address1":
            try:
                delete_response = fgt.api.cmdb.firewall.address.delete(name="test_address1")
                print(f"Deleted existing test_address1: HTTP {delete_response.http_status}")    
            except Exception:
                pass
except Exception:
    pass

create_address = fgt.api.cmdb.firewall.address.set(
    name="test_address1",
    subnet="10.0.0.0/24"
)

print(f" https status: {create_address.http_status}")


create_address = fgt.api.cmdb.firewall.address.set(
    name="test_address1",
    subnet="10.0.0.0/24",
    comment="Updated via test script"
)
print(f" https status: {create_address.http_status}")
print(f" https method: {create_address.http_method}")
print(f" https stats: {create_address.http_status}")





psirt = fgt.api.service.security_rating.report.get(type="psirt", scope="global")

# Filter to only show checks that did NOT pass
# results is a list of checks directly
failed_checks = []
checks = psirt.raw.get("results", [])
if isinstance(checks, dict):
    checks = checks.get("checks", [])

for check in checks:
    for summary in check.get("summary", []):
        if summary.get("result") != "passed":
            failed_checks.append({
                "check": check.get("check"),
                "title": check.get("title"),
                "severity": check.get("severity"),
                "cve": check.get("customMetadata", {}).get("cve", []),
                "result": summary.get("result"),
                "issueCount": summary.get("issueCount"),
                "device": summary.get("device"),
                "vdom": summary.get("vdom")
            })

if failed_checks:
    print(f"🚨 Found {len(failed_checks)} non-passed checks:")
    print(json.dumps(failed_checks, indent=2))
else:
    print("✅ All PSIRT checks passed!")


