# FortiManager Proxy

Route FortiOS API calls through FortiManager to manage multiple FortiGate devices.

## Overview

The FortiManager Proxy feature allows you to:

- Manage multiple FortiGate devices through a single FortiManager connection
- Execute FortiOS API operations on devices managed by FortiManager
- Use the same FortiOS API syntax while routing through FortiManager
- Support for multiple ADOMs and VDOMs

## Quick Start

### Basic Setup

```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    verify=True,  # SSL verification
    adom="root"   # Default ADOM
)

# Create a proxy client for a specific device
fgt = fmg.proxy(device="firewall-01", vdom="root")

# Use normal FortiOS API syntax
address = fgt.api.cmdb.firewall.address.create(
    name="webserver",
    subnet="192.168.1.100 255.255.255.255",
    comment="Production web server"
)
```

### Using Different ADOMs

```python
# Override default ADOM for specific device
fgt = fmg.proxy(adom="production", device="firewall-01")

# Or set default ADOM when creating the proxy
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    adom="production"  # Default for all proxy() calls
)
```

## API Operations

The proxied client supports all standard FortiOS API methods:

### CMDB Operations

```python
# Create resources
policy = fgt.api.cmdb.firewall.policy.create(
    name="Allow-Web",
    srcintf=[{"name": "port1"}],
    dstintf=[{"name": "port2"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "webserver"}],
    service=[{"name": "HTTP"}, {"name": "HTTPS"}],
    action="accept"
)

# Read resources
policies = fgt.api.cmdb.firewall.policy.list()

# Update resources
fgt.api.cmdb.firewall.policy.update(
    mkey=42,
    status="disable"
)

# Delete resources
fgt.api.cmdb.firewall.policy.delete(mkey=42)
```

### Monitor Operations

```python
# System status
status = fgt.api.monitor.system.status.get()

# Interface stats
interfaces = fgt.api.monitor.system.interface.list()

# Session info
sessions = fgt.api.monitor.firewall.session.list()
```

### Low-Level Request Method

For maximum flexibility, use the `request()` method:

```python
response = fgt.request(
    method="POST",
    path="/api/v2/cmdb/firewall/address",
    data={
        "name": "server-farm",
        "type": "iprange",
        "start-ip": "10.0.1.10",
        "end-ip": "10.0.1.20"
    }
)
```

## Response Handling

Responses include FortiManager proxy metadata:

```python
response = fgt.api.cmdb.firewall.address.get(mkey="webserver")

# Standard FortiOS response data
print(response.results)

# FortiManager proxy status code (if available)
if hasattr(response, 'fmg_proxy_status_code'):
    print(f"FMG Status: {response.fmg_proxy_status_code}")
```

## Multiple Devices

Manage multiple devices with a single FortiManager connection:

```python
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password"
)

# Device 1
fw1 = fmg.proxy(adom="production", device="firewall-01", vdom="root")
fw1.api.cmdb.firewall.address.create(name="test1", subnet="10.1.0.0 255.255.255.0")

# Device 2
fw2 = fmg.proxy(adom="production", device="firewall-02", vdom="root")
fw2.api.cmdb.firewall.address.create(name="test2", subnet="10.2.0.0 255.255.255.0")

# Device 3 in different ADOM
fw3 = fmg.proxy(adom="development", device="firewall-dev", vdom="root")
fw3.api.cmdb.firewall.address.create(name="test3", subnet="10.3.0.0 255.255.255.0")
```

## Error Handling

Handle errors the same way as direct FortiOS connections:

```python
from hfortix_core.exceptions import HTTPError

try:
    fgt.api.cmdb.firewall.address.create(
        name="duplicate",
        subnet="192.168.1.0 255.255.255.0"
    )
except HTTPError as e:
    print(f"Error: {e.status_code} - {e.message}")
```

## Best Practices

1. **Reuse FortiManagerProxy instances** - Create one FMG connection and use it for multiple devices
2. **Set default ADOM** - Specify a default ADOM at creation to avoid repeating it
3. **Use VDOMs** - Always specify the VDOM to avoid ambiguity
4. **Error handling** - Wrap API calls in try/except blocks for production code
5. **SSL verification** - Use `verify=True` in production environments

## Limitations

- FortiManager must have connectivity to the target FortiGate device
- Device must be managed by the specified FortiManager ADOM
- Some real-time monitoring endpoints may have limitations through the proxy
- FortiManager API version must be compatible with target FortiOS version

## API Reference

See the [FortiOS API Reference](/fortios/api-reference/index.rst) for complete endpoint documentation. All endpoints work through the FortiManager proxy.

## Related

- [FortiOS Client](/fortios/user-guide/client.rst) - Direct FortiOS client usage
- [Error Handling](/fortios/user-guide/error-handling.md) - Error handling patterns
- [API Reference](/fortios/api-reference/index.rst) - Complete API documentation
