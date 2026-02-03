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

log1 = fgt.api.log.disk.traffic.forward.get(rows=15)
print(log1.json)

result = fgt.api.log.memory.ips.archive.get()
print(result.raw)

monitor1 = fgt.api.monitor.firewall.policy.get()
print(monitor1.json)

monitor2 = fgt.api.monitor.firewall.policy.reset.post()
print(monitor2.raw)

service1 = fgt.api.service.sniffer.list.get(vdom="test")
print(service1.raw)


