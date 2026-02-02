# HTTP API Request Inspection

## Overview

Starting from version 0.5.152, all `FortiObject`, `FortiObjectList`, and `ContentResponse` instances include an `http_api_request` property (and its alias `fmg_api_request` for FortiManager proxy usage) that provides complete details about the HTTP request that generated the response.

## Properties

### `http_api_request`

Returns a dictionary with the following information:

- **method**: HTTP method used (`GET`, `POST`, `PUT`, `DELETE`)
- **url**: Full URL that was requested
- **endpoint**: API endpoint path
- **params**: Query parameters sent with the request
- **data**: Request body (for `POST`/`PUT` operations)
- **timestamp**: Unix timestamp when the request was made

Returns `None` if request information was not tracked.

### `fmg_api_request`

Alias for `http_api_request` that makes code more readable when using FortiManager proxy connections. Both properties return the exact same information.

## Use Cases

### 1. Debugging - See Exact Request Details

**Direct FortiGate Connection:**
```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# Make a query with filters
result = fgt.api.cmdb.firewall.policy.get(filter='srcaddr==internal')

# See exactly what was sent to FortiGate
print(result.http_api_request)
# Output:
# {
#     'method': 'GET',
#     'url': 'https://192.168.1.99/api/v2/cmdb/firewall/policy',
#     'endpoint': '/api/v2/cmdb/firewall/policy',
#     'params': {'filter': 'srcaddr==internal', 'vdom': 'root'},
#     'data': None,
#     'timestamp': 1706889600.123
# }
```

**FortiManager Proxy Connection:**
```python
from hfortix_fortios import FortiManager

fmg = FortiManager(host="fmg.example.com", username="admin", password="password")

# Make a query through FortiManager proxy
result = fmg.devices['FGT-01'].api.cmdb.firewall.policy.get()

# See the FMG proxy request details
print(result.fmg_api_request)
# Output:
# {
#     'method': 'POST',
#     'url': 'https://fmg.example.com/jsonrpc',
#     'endpoint': '/api/v2/cmdb/firewall/policy',
#     'params': {'vdom': 'root'},
#     'data': {'method': 'get', 'params': [{'url': '/pm/config/device/FGT-01/...'}]},
#     'timestamp': 1706889600.123
# }
```

### 2. Audit Logging - Track Operations

```python
import logging
import json

logger = logging.getLogger(__name__)

# Create a firewall address
new_addr = fgt.api.cmdb.firewall.address.post(
    name="webserver",
    subnet="10.0.1.100/32",
    comment="Production web server"
)

# Log the full request for audit trail
logger.info(
    "Created firewall address",
    extra={
        "request": new_addr.http_api_request,
        "mkey": new_addr.fgt_mkey,
        "status": new_addr.http_status
    }
)
```

### 3. Troubleshooting - Verify Parameters

```python
# Complex query that's not working as expected
result = fgt.api.cmdb.firewall.policy.get(
    filter='srcaddr==10.0.0.0/8',
    format=['name', 'srcaddr'],
    count=100
)

# Check what was actually sent
request = result.http_api_request
print(f"Filter sent: {request['params'].get('filter')}")
print(f"Format sent: {request['params'].get('format')}")
print(f"Count sent: {request['params'].get('count')}")
```

### 4. Generate Documentation from Actual Requests

```python
def document_api_call(result):
    """Generate documentation from an actual API call"""
    req = result.http_api_request
    
    doc = f"""
## {req['method']} {req['endpoint']}

**URL**: `{req['url']}`

**Parameters**:
```json
{json.dumps(req['params'], indent=2)}
```
"""
    
    if req['data']:
        doc += f"""
**Request Body**:
```json
{json.dumps(req['data'], indent=2)}
```
"""
    
    return doc

# Use it
policies = fgt.api.cmdb.firewall.policy.get(filter='action==accept')
print(document_api_call(policies))
```

### 5. Testing - Validate Request Construction

```python
def test_filter_construction():
    """Verify that filters are being sent correctly"""
    result = fgt.api.cmdb.firewall.address.get(
        filter='subnet==10.0.0.0/8'
    )
    
    # Assert the filter was sent as expected
    assert result.http_api_request['params']['filter'] == 'subnet==10.0.0.0/8'
    
    # Verify vdom was included
    assert 'vdom' in result.http_api_request['params']
```

### 6. Works with All Response Types

```python
# Works with single object (unwrapped)
addr = fgt.api.cmdb.firewall.address.get(name="webserver")
print(addr.http_api_request)

# Works with lists
policies = fgt.api.cmdb.firewall.policy.get()
print(policies.http_api_request)  # From the list
print(policies[0].http_api_request)  # From individual items

# Works with POST/PUT/DELETE
created = fgt.api.cmdb.firewall.address.post(name="test", subnet="10.0.0.1/32")
print(created.http_api_request)

# Works with content responses (file downloads)
config = fgt.api.monitor.system.config_revision.file.get(config_id=45)
print(config.http_api_request)
```

## Combining with Other Properties

The `http_api_request` property works well with other HTTP metadata properties:

```python
result = fgt.api.cmdb.firewall.policy.get()

# Request information
print(f"Method: {result.http_api_request['method']}")
print(f"URL: {result.http_api_request['url']}")
print(f"Params: {result.http_api_request['params']}")

# Response information
print(f"Status Code: {result.http_status_code}")
print(f"Response Time: {result.http_response_time}ms")
print(f"VDOM: {result.fgt_vdom}")

# Full envelope
print(f"Raw Response: {result.raw}")
```

## Example Output

For a GET request:
```python
{
    'method': 'GET',
    'url': 'https://192.168.1.99/api/v2/cmdb/firewall/policy',
    'endpoint': '/api/v2/cmdb/firewall/policy',
    'params': {
        'filter': 'srcaddr==internal',
        'format': ['name', 'srcaddr'],
        'vdom': 'root'
    },
    'data': None,
    'timestamp': 1706889600.123
}
```

For a POST request:
```python
{
    'method': 'POST',
    'url': 'https://192.168.1.99/api/v2/cmdb/firewall/address',
    'endpoint': '/api/v2/cmdb/firewall/address',
    'params': {'vdom': 'root'},
    'data': {
        'name': 'webserver',
        'subnet': '10.0.1.100 255.255.255.255',
        'comment': 'Production web server'
    },
    'timestamp': 1706889602.789
}
```

## Notes

- Request information is automatically captured for all API calls
- The `data` field shows the payload after field name conversion (snake_case → kebab-case)
- The `timestamp` is a Unix timestamp (seconds since epoch)
- This feature has zero performance impact - request details are already tracked internally
- Returns `None` if the response was not generated from a tracked HTTP request
