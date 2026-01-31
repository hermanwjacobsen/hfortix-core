# Endpoint Methods

Understanding the available HTTP methods for FortiOS API endpoints.

## Available HTTP Methods

HFortix provides direct access to FortiOS REST API through standard HTTP methods. Each endpoint may support one or more of the following methods depending on the FortiOS API capabilities:

### Standard CRUD Methods

- **`.get()`** - HTTP GET - Retrieve resources (list all or get specific by mkey)
- **`.post()`** - HTTP POST - Create new resources
- **`.put()`** - HTTP PUT - Update existing resources  
- **`.delete()`** - HTTP DELETE - Delete resources
- **`.set()`** - HTTP PUT - Set/replace entire configuration (available on some endpoints)

### Method Usage

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host='192.168.1.99', api_token='your-token')

# GET - Retrieve all resources
addresses = fgt.api.cmdb.firewall.address.get()

# GET - Retrieve specific resource by mkey
address = fgt.api.cmdb.firewall.address.get(mkey='webserver')

# POST - Create new resource
result = fgt.api.cmdb.firewall.address.post(
    payload_dict={
        'name': 'webserver',
        'subnet': '192.168.1.100 255.255.255.255',
        'comment': 'Production web server'
    }
)

# PUT - Update existing resource
result = fgt.api.cmdb.firewall.address.put(
    mkey='webserver',
    payload_dict={
        'comment': 'Updated comment'
    }
)

# DELETE - Remove resource
result = fgt.api.cmdb.firewall.address.delete(mkey='webserver')

# SET - Replace entire configuration (when available)
result = fgt.api.cmdb.system.settings.set(
    payload_dict={
        'opmode': 'nat',
        'inspection_mode': 'proxy',
        # ... full configuration
    }
)
```

## Method Availability

Not all endpoints support all methods. The available methods depend on the FortiOS API design:

| Endpoint Type | GET | POST | PUT | DELETE | SET |
| ------------- | --- | ---- | --- | ------ | --- |
| **CMDB Table** (e.g., firewall.address) | ✅ | ✅ | ✅ | ✅ | ❌ |
| **CMDB Global** (e.g., system.global) | ✅ | ❌ | ✅ | ❌ | ✅ |
| **Monitor** (e.g., system.status) | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Log** (e.g., disk.event) | ✅ | ❌ | ❌ | ❌ | ❌ |

## Common Parameters

### GET Method

```python
# List all with filtering
addresses = fgt.api.cmdb.firewall.address.get(
    filter=['type==ipmask'],
    count=10,
    start=0
)

# Get specific by mkey
address = fgt.api.cmdb.firewall.address.get(mkey='webserver')

# With VDOM
address = fgt.api.cmdb.firewall.address.get(
    mkey='webserver',
    vdom='root'
)
```

### POST Method

```python
# Create with payload_dict
result = fgt.api.cmdb.firewall.policy.post(
    payload_dict={
        'name': 'Allow-Web',
        'srcintf': [{'name': 'port1'}],
        'dstintf': [{'name': 'port2'}],
        'srcaddr': [{'name': 'all'}],
        'dstaddr': [{'name': 'webserver'}],
        'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
        'action': 'accept'
    }
)

# Create with keyword arguments (Pydantic models where available)
result = fgt.api.cmdb.firewall.address.post(
    name='testserver',
    subnet='10.0.1.5 255.255.255.255',
    comment='Test server'
)
```

### PUT Method

```python
# Update with mkey and payload_dict
result = fgt.api.cmdb.firewall.address.put(
    mkey='webserver',
    payload_dict={
        'comment': 'Updated web server',
        'color': 3
    }
)

# Update with keyword arguments
result = fgt.api.cmdb.firewall.address.put(
    mkey='webserver',
    comment='Updated comment',
    color=3
)
```

### DELETE Method

```python
# Delete by mkey
result = fgt.api.cmdb.firewall.address.delete(mkey='webserver')

# Delete with VDOM
result = fgt.api.cmdb.firewall.address.delete(
    mkey='webserver',
    vdom='root'
)
```

### SET Method

```python
# Replace entire configuration
result = fgt.api.cmdb.system.global.set(
    payload_dict={
        'hostname': 'firewall-01',
        'timezone': 'America/New_York',
        'admin_sport': 443,
        # ... complete configuration
    }
)
```

## Response Objects

All methods return `FortiObject` or `FortiObjectList` instances:

```python
# Single object response (POST, PUT, DELETE)
result = fgt.api.cmdb.firewall.address.post(...)
print(result.http_status_code)  # 200
print(result.revision)          # Configuration revision
print(result.raw)               # Full API envelope

# List response (GET without mkey)
addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    print(addr.name)
    print(addr.subnet)

# Single object response (GET with mkey)
address = fgt.api.cmdb.firewall.address.get(mkey='webserver')
print(address.name)
print(address.subnet)
```

## Using the request() Method

For maximum flexibility, use the low-level `request()` method:

```python
# Direct request - copy JSON from FortiGate GUI
response = fgt.request(
    method='POST',
    path='/api/v2/cmdb/firewall/address',
    data={
        'name': 'webserver',
        'subnet': '192.168.1.100 255.255.255.255',
        'comment': 'Production web server'
    }
)
```

## Monitor API Methods

Monitor endpoints typically only support GET and POST:

```python
# GET - Retrieve monitoring data
status = fgt.api.monitor.system.status.get()
interfaces = fgt.api.monitor.system.interface.get()

# POST - Trigger actions
result = fgt.api.monitor.system.config.backup.post()
```

## Error Handling

```python
from hfortix_core.exceptions import APIError, ResourceNotFoundError

try:
    address = fgt.api.cmdb.firewall.address.get(name='nonexistent')
except ResourceNotFoundError:
    print("Address not found")
except APIError as e:
    print(f"Error: {e.http_status} - {e.message}")
```

## See Also

- [API Reference](/fortios/api-reference/index.rst) - Complete endpoint documentation (1,219 endpoints)
- [Custom Wrappers Guide](/fortios/guides/custom-wrappers.md) - Create your own convenience wrappers
- [FortiOS Client](/fortios/user-guide/client.rst) - Client configuration and usage
- [Error Handling](/fortios/user-guide/error-handling.md) - Error handling patterns
