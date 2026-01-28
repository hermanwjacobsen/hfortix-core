# Quick Start Guide

Get up and running with HFortix in 5 minutes.

## Prerequisites

Before you begin, ensure you have:

1. Python 3.10 or higher installed
2. A FortiGate device with FortiOS 6.0+ and REST API enabled
3. An API token (see [Authentication](/fortios/getting-started/authentication.md) for setup)

## Installation

Install HFortix from PyPI:

```bash
pip install hfortix[fortios]
```

## Your First Script

Create a file named `test_hfortix.py`:

```python
from hfortix import FortiOS, APIError

# Initialize the client
fgt = FortiOS(
    host='192.168.1.99',           # Your FortiGate IP/hostname
    token='your-api-token-here',   # Your API token
    verify=False                   # Use True in production with valid SSL cert
)

# List all firewall addresses
try:
    addresses = fgt.api.cmdb.firewall.address.get()
    print(f"Found {len(addresses)} firewall addresses")
    
    # Display first few addresses
    for addr in addresses[:5]:
        print(f"  - {addr['name']}: {addr.get('subnet', 'N/A')}")
        
except APIError as e:
    print(f"Error: {e.message} (Code: {e.error_code})")
```

Run it:

```bash
python test_hfortix.py
```

## Common Operations

### List Resources

```python
# List firewall addresses
addresses = fgt.api.cmdb.firewall.address.get()

# List firewall policies
policies = fgt.api.cmdb.firewall.policy.get()

# List configured interfaces
interfaces = fgt.api.cmdb.system.interface.get()
```

### Create a Resource

```python
# Create a firewall address
result = fgt.api.cmdb.firewall.address.post(
    name='web-server',
    subnet='192.0.2.100 255.255.255.255',
    comment='Production web server'
)

print(f"Created: {result}")
```

### Update a Resource

```python
# Update the address
result = fgt.api.cmdb.firewall.address.put(
    mkey='web-server',
    payload_dict={'comment': 'Updated web server address'}
)
```

### Delete a Resource

```python
# Delete the address
result = fgt.api.cmdb.firewall.address.delete(mkey='web-server')
print("Address deleted successfully")
```

## Using FortiManager Proxy

Manage multiple FortiGate devices through FortiManager:

```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    adom="root"
)

# Login (or use context manager for auto login/logout)
fmg.login()

try:
    # Create a proxy client for a specific device
    fgt = fmg.proxy(device="firewall-01", vdom="root")

    # Use normal FortiOS API - routed through FortiManager!
    address = fgt.api.cmdb.firewall.address.post(
        name="webserver",
        subnet="192.168.1.100 255.255.255.255",
        comment="Managed via FMG"
    )

    # Manage multiple devices
    fw1 = fmg.proxy(device="firewall-01")
    fw2 = fmg.proxy(device="firewall-02")
    fw1.api.cmdb.firewall.address.post(name="test", subnet="10.1.0.0 255.255.255.0")
    fw2.api.cmdb.firewall.address.post(name="test", subnet="10.2.0.0 255.255.255.0")
finally:
    fmg.logout()
```

See [FortiManager Proxy Guide](/fortios/guides/fmg-proxy.md) for more details.

## Using FortiProxy

HFortix also supports FortiProxy devices using the same API:

```python
from hfortix_fortios import FortiOS

# Connect to FortiProxy (same as FortiGate)
fproxy = FortiOS(
    host="fortiproxy.example.com",
    token="your-api-token",
    verify=True
)

# Configure web filter profile
profile = fproxy.api.cmdb.webfilter.profile.post(
    name="corporate-policy",
    comment="Corporate web filtering",
    web={
        "urlfilter-table": 1,
        "content-header-list": 1,
        "blocklist": "enable"
    }
)

# Apply to firewall policy
policy = fproxy.api.cmdb.firewall.policy.post(
    name="Web-Filter-Policy",
    srcintf=[{"name": "port1"}],
    dstintf=[{"name": "port2"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "HTTP"}, {"name": "HTTPS"}],
    action="accept",
    webfilter_profile="corporate-policy"
)

# Monitor proxy statistics
stats = fproxy.api.monitor.web_proxy.stats.get()
print(f"Active sessions: {stats.get('sessions', 0)}")
```

**Note**: FortiProxy uses the same FortiOS API, so all endpoints work identically.

## Flexible Interface

HFortix supports both dictionary and keyword-based syntax:

```python
# Method 1: Keyword arguments (recommended for readability)
fgt.api.cmdb.firewall.address.post(
    name='server-1',
    subnet='10.0.1.100 255.255.255.255',
    comment='Server'
)

# Method 2: Dictionary with payload_dict
config = {
    'name': 'server-1',
    'subnet': '10.0.1.100 255.255.255.255',
    'comment': 'Server'
}
fgt.api.cmdb.firewall.address.post(payload_dict=config)

# Method 3: Using request() for zero-translation
# Copy JSON directly from FortiGate GUI!
fgt.request(
    method='POST',
    path='/api/v2/cmdb/firewall/address',
    data=config
)
```

## Error Handling

Always wrap API calls in try-except blocks:

```python
from hfortix_core.exceptions import HTTPError, NotFoundError

try:
    result = fgt.api.cmdb.firewall.address.post(
        name='test-addr',
        subnet='10.0.0.1 255.255.255.255'
    )
except HTTPError as e:
    if e.status_code == 424:
        print("Address already exists!")
    else:
        print(f"API Error {e.status_code}: {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Optimization

For high-performance scenarios, run a performance test first:

```python
# Run performance test to get optimal settings
results = fgt.api.utils.performance_test()

# Create optimized client with recommended settings
fgt_optimized = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    max_connections=results['recommended']['max_connections'],
    max_keepalive_connections=results['recommended']['max_keepalive']
)
```

## Monitoring

Access real-time monitoring data:

```python
# Get system status
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}")
print(f"Version: {status['version']}")

# Get firewall policy statistics
stats = fgt.api.monitor.firewall.policy.get()

# Get active sessions
sessions = fgt.api.monitor.firewall.session.get()
```

## What's Next?

Now that you're up and running, explore more:

- **[FortiManager Proxy](/fortios/guides/fmg-proxy.md)** - Manage multiple devices through FortiManager
- **[Custom Wrappers](/fortios/guides/custom-wrappers.md)** - Create your own convenience wrappers
- **[Endpoint Methods](/fortios/user-guide/endpoint-methods.md)** - Learn about .get(), .post(), .put(), .delete(), .set()
- **[Error Handling](/fortios/user-guide/error-handling.md)** - Advanced error handling patterns
- **[API Reference](/fortios/api-reference/index.rst)** - Complete API documentation (1,219 endpoints)

## Getting Help

- **GitHub Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **Documentation**: https://hfortix.readthedocs.io/
- **Examples**: Check the `examples/` directory in the repository
