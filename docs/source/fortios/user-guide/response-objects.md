# Response Objects

All HFortix API methods return `FortiObject` or `FortiObjectList` instances that provide
clean attribute access to response data, plus metadata about the API request.

## Quick Reference

```python
result = fgt.api.cmdb.firewall.address.post(
    name='webserver',
    subnet='192.168.1.100 255.255.255.255'
)

# Access response data as attributes
print(result.name)      # 'webserver'
print(result.subnet)    # '192.168.1.100 255.255.255.255'

# Check if configuration actually changed
if result.fgt_revision_changed:
    print(f"Config changed! New revision: {result.fgt_revision}")
else:
    print("No configuration change (object already existed with same values)")

# HTTP/API metadata
print(result.http_status_code)   # 200
print(result.http_status)        # 'success'
print(result.http_response_time) # 45.2 (milliseconds)
```

## Response Properties

### HTTP/API Status Properties

| Property | Type | Description |
|----------|------|-------------|
| `http_status_code` | `int` | HTTP status code (200, 400, 404, 500, etc.) |
| `http_status` | `str` | API status: `'success'` or `'error'` |
| `http_method` | `str` | HTTP method used: `GET`, `POST`, `PUT`, `DELETE` |
| `http_response_time` | `float` | Response time in milliseconds |
| `http_stats` | `dict` | Summary dict with all HTTP stats |

### FortiGate Metadata Properties

| Property | Type | Description |
|----------|------|-------------|
| `fgt_revision` | `str` | Current configuration revision number |
| `fgt_revision_changed` | `bool` | **True if configuration was modified** |
| `fgt_old_revision` | `str` | Previous revision (before this change) |
| `fgt_vdom` | `str` | Virtual domain name |
| `fgt_mkey` | `str\|int` | Primary key of created/modified object |
| `fgt_serial` | `str` | Device serial number |
| `fgt_version` | `str` | FortiOS version (e.g., `'v7.6.5'`) |
| `fgt_build` | `int` | Firmware build number |
| `fgt_api_path` | `str` | API path segment (e.g., `'firewall'`) |
| `fgt_api_name` | `str` | API endpoint name (e.g., `'address'`) |

### Pagination Properties (for list queries)

| Property | Type | Description |
|----------|------|-------------|
| `fgt_response_size` | `int` | Number of objects returned |
| `fgt_matched_count` | `int` | Total objects matching query |
| `fgt_limit_reached` | `bool` | True if pagination limit was hit |
| `fgt_next_idx` | `int` | Index for next page |

### FortiManager Proxy Properties

When using FortiManager proxy, additional properties are available:

| Property | Type | Description |
|----------|------|-------------|
| `fmg_status_code` | `int` | FortiManager status code |
| `fmg_status_message` | `str` | FortiManager status message |
| `fmg_proxy_status_code` | `int` | Proxy request status |
| `fmg_proxy_target` | `str` | Target device name |
| `fmg_id` | `int` | FortiManager request ID |
| `fmg_raw` | `dict` | Raw FortiManager response |

### Data Conversion Properties

| Property/Method | Type | Description |
|-----------------|------|-------------|
| `dict` | `dict` | Object data as dictionary |
| `json` | `str` | Object data as pretty-printed JSON string |
| `raw` | `dict` | Full API response envelope (includes metadata) |
| `to_dict()` | `dict` | Alias for `dict` property |
| `get_full(field)` | `Any` | Get raw field value (not auto-flattened) |

**Example:**

```python
address = fgt.api.cmdb.firewall.address.get(mkey='webserver')

# As dictionary - for programmatic access
data = address.dict
data['name']  # 'webserver'

# As JSON - for display/logging
print(address.json)
# {
#   "name": "webserver",
#   "subnet": "192.168.1.100 255.255.255.255",
#   "comment": "Production server"
# }

# Raw envelope - for debugging/metadata
address.raw
# {'http_status': 200, 'status': 'success', 'vdom': 'root', 'results': {...}}
```

## Understanding `fgt_revision_changed`

The `fgt_revision_changed` property is crucial for understanding whether your API call actually modified the FortiGate configuration.

### Why This Matters

FortiOS is idempotent - if you create an object that already exists with identical values, it returns HTTP 200 (success) but **doesn't actually change the config**. This property tells you the difference:

```python
# First creation - config changes
result1 = fgt.api.cmdb.firewall.address.post(
    name='webserver',
    subnet='192.168.1.100 255.255.255.255'
)
print(result1.fgt_revision_changed)  # True - new object created
print(result1.fgt_revision)          # '12345'

# Identical call - NO config change
result2 = fgt.api.cmdb.firewall.address.post(
    name='webserver',
    subnet='192.168.1.100 255.255.255.255'
)
print(result2.fgt_revision_changed)  # False - already exists, same values
print(result2.fgt_revision)          # '12345' - same revision

# Update with different value - config changes
result3 = fgt.api.cmdb.firewall.address.put(
    mkey='webserver',
    comment='Updated comment'
)
print(result3.fgt_revision_changed)  # True - config modified
print(result3.fgt_revision)          # '12346' - new revision
print(result3.fgt_old_revision)      # '12345' - previous revision
```

### Use Cases

**1. Change Detection in Automation**

```python
def apply_config_if_changed(fgt, addresses):
    """Only report actual changes."""
    changes = []
    for addr in addresses:
        result = fgt.api.cmdb.firewall.address.post(**addr)
        if result.fgt_revision_changed:
            changes.append(addr['name'])
    
    if changes:
        print(f"Modified: {', '.join(changes)}")
    else:
        print("No changes needed - config already up to date")
```

**2. Audit Logging**

```python
def create_address_with_audit(fgt, **kwargs):
    """Log only actual configuration changes."""
    result = fgt.api.cmdb.firewall.address.post(**kwargs)
    
    if result.fgt_revision_changed:
        log.info(f"CONFIG CHANGED: Created {kwargs['name']}, "
                 f"revision {result.fgt_old_revision} → {result.fgt_revision}")
    else:
        log.debug(f"No change: {kwargs['name']} already exists with same config")
    
    return result
```

**3. Rollback Tracking**

```python
# Track revisions for potential rollback
changes = []

result = fgt.api.cmdb.firewall.address.post(name='test', subnet='10.0.0.1/32')
if result.fgt_revision_changed:
    changes.append({
        'object': 'test',
        'old_revision': result.fgt_old_revision,
        'new_revision': result.fgt_revision
    })
```

## Data Access Patterns

### Attribute Access (Recommended)

```python
# Clean attribute access for known fields
address = fgt.api.cmdb.firewall.address.get(mkey='webserver')
print(address.name)
print(address.subnet)
print(address.comment)
```

### Dict-Style Access

```python
# Dict-style for dynamic field names
field_name = 'subnet'
print(address[field_name])

# With default value
print(address.get('comment', 'No comment'))
```

### Auto-Flattening of Member Tables

HFortix automatically simplifies member table fields:

```python
# FortiOS API returns complex structure:
# {"srcaddr": [{"name": "addr1", "q_origin_key": "addr1"}, {"name": "addr2", ...}]}

policy = fgt.api.cmdb.firewall.policy.get(mkey=1)

# HFortix auto-flattens to simple list:
print(policy.srcaddr)  # ['addr1', 'addr2']

# Access full raw data when needed:
print(policy.get_full('srcaddr'))  
# [{"name": "addr1", "q_origin_key": "addr1"}, {"name": "addr2", ...}]
```

## FortiObjectList (List Responses)

GET requests without `mkey` return `FortiObjectList`:

```python
addresses = fgt.api.cmdb.firewall.address.get()

# Iterate
for addr in addresses:
    print(addr.name)

# Length
print(len(addresses))  # 42

# Index access
first = addresses[0]
last = addresses[-1]

# Slice
first_ten = addresses[:10]

# List comprehension
names = [addr.name for addr in addresses]

# Filter
internal = [a for a in addresses if a.subnet.startswith('10.')]

# Check pagination
if addresses.fgt_limit_reached:
    print(f"More results available, next index: {addresses.fgt_next_idx}")
```

## Converting to Dict/JSON

```python
# Single object
address = fgt.api.cmdb.firewall.address.get(mkey='webserver')

# Using properties (recommended)
data = address.dict           # Dictionary
json_str = address.json       # Pretty-printed JSON string
envelope = address.raw        # Full API envelope with metadata

# Using methods (equivalent)
data = address.to_dict()      # Same as .dict

# List to dicts
addresses = fgt.api.cmdb.firewall.address.get()
all_data = [addr.dict for addr in addresses]

# Export to file
with open('addresses.json', 'w') as f:
    import json
    json.dump([addr.dict for addr in addresses], f, indent=2)
```

## See Also

- [Endpoint Methods](endpoint-methods.md) - GET, POST, PUT, DELETE methods
- [Error Handling](error-handling.md) - Exception handling patterns
- [Audit Logging Guide](/fortios/guides/audit-logging.rst) - Tracking configuration changes
