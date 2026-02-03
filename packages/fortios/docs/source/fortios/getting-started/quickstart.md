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
from hfortix_fortios import FortiOS
from hfortix_core.exceptions import APIError

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
        # Access fields as attributes (recommended)
        print(f"  - {addr.name}: {addr.subnet}")
        
        # Or use dict-style access for dynamic keys
        # print(f"  - {addr['name']}: {addr.get('subnet', 'N/A')}")
        
except APIError as e:
    print(f"Error: {e}")
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

print(f"Created: {result.name} (status: {result.http_status_code})")
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

## Working with Responses

All API methods return `FortiObject` instances with multiple ways to access data:

### Attribute Access (Recommended)

```python
# Get a firewall address
address = fgt.api.cmdb.firewall.address.get(mkey='web-server')

# Access fields as attributes
print(address.name)     # 'web-server'
print(address.subnet)   # '192.0.2.100 255.255.255.255'
print(address.comment)  # 'Production web server'
```

### Response Metadata

```python
result = fgt.api.cmdb.firewall.address.post(
    name='test-server',
    subnet='10.0.0.1 255.255.255.255'
)

# Check HTTP status
print(result.http_status_code)  # 200
print(result.http_status)       # 'success'

# Check if configuration actually changed
if result.fgt_revision_changed:
    print(f"Config modified! Revision: {result.fgt_revision}")
else:
    print("No change - object already exists with same values")
```

### Converting to Dict/JSON

```python
address = fgt.api.cmdb.firewall.address.get(mkey='web-server')

# Get as dictionary
data = address.dict
print(data['name'])  # 'web-server'

# Get as JSON string (pretty-printed)
print(address.json)
# {
#   "name": "web-server",
#   "subnet": "192.0.2.100 255.255.255.255",
#   ...
# }

# Get full API envelope (includes metadata)
print(address.raw)
# {'http_status': 200, 'status': 'success', 'vdom': 'root', 'results': {...}}
```

See [Response Objects](/fortios/user-guide/response-objects.md) for complete documentation.

## Managing FortiGates via FortiManager

Use `FortiManagerProxy` to manage multiple FortiGate devices through FortiManager's centralized management:

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

    # Manage multiple devices from one connection
    fw1 = fmg.proxy(device="firewall-01")
    fw2 = fmg.proxy(device="firewall-02")
    fw1.api.cmdb.firewall.address.post(name="test", subnet="10.1.0.0 255.255.255.0")
    fw2.api.cmdb.firewall.address.post(name="test", subnet="10.2.0.0 255.255.255.0")
finally:
    fmg.logout()
```

See [FortiManager Proxy Guide](/fortios/guides/fmg-proxy.md) for more details.

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
from hfortix_core.exceptions import APIError, DuplicateEntryError

try:
    result = fgt.api.cmdb.firewall.address.post(
        name='test-addr',
        subnet='10.0.0.1 255.255.255.255'
    )
except DuplicateEntryError:
    print("Address already exists!")
except APIError as e:
    print(f"API Error {e.http_status}: {e.message}")
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
# Get system status (use dict access - Monitor fields may not have type hints)
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}")
print(f"Model: {status['model']}")

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
