# API Request Inspection

The HFortix SDK provides powerful request inspection capabilities to help you debug, audit, and understand API interactions with FortiOS devices.

## Overview

The request inspection feature allows you to:
- **Debug API calls**: See exactly what was sent and received
- **Audit operations**: Track all configuration changes
- **Troubleshoot errors**: Understand why requests fail
- **Learn the API**: See how high-level operations translate to HTTP requests
- **Build custom tools**: Access raw request/response data

## Quick Start

### Basic Usage

```python
from hfortix import FortiOS

fgt = FortiOS("192.168.1.99", token="your_token")

# Make an API call
response = fgt.api.cmdb.firewall.address.get("server1")

# Inspect the last request
last_request = fgt.http_api_request()

print(f"Method: {last_request['method']}")
print(f"URL: {last_request['url']}")
print(f"Status: {last_request['status_code']}")
print(f"Response: {last_request['response']}")
```

### FortiManager Inspection

For FortiManager, use `fmg_api_request()`:

```python
from hfortix import FortiManager

fmg = FortiManager("192.168.1.100", username="admin", password="password")

# Make an API call
response = fmg.dvmdb.adom.get()

# Inspect the last request
last_request = fmg.fmg_api_request()

print(f"JSON-RPC ID: {last_request['id']}")
print(f"Method: {last_request['method']}")
print(f"URL: {last_request['url']}")
print(f"Response: {last_request['response']}")
```

## Request Object Structure

### FortiOS Request Object

The `http_api_request()` method returns a dictionary with:

```python
{
    'method': str,           # HTTP method (GET, POST, PUT, DELETE)
    'url': str,              # Full request URL
    'headers': dict,         # Request headers
    'body': dict,            # Request body (for POST/PUT)
    'status_code': int,      # HTTP status code
    'response': dict,        # Parsed response body
    'duration': float,       # Request duration in seconds
    'timestamp': str         # ISO timestamp of request
}
```

### FortiManager Request Object

The `fmg_api_request()` method returns a dictionary with:

```python
{
    'id': int,               # JSON-RPC request ID
    'method': str,           # JSON-RPC method (get, set, add, etc.)
    'url': str,              # API endpoint URL
    'params': list,          # JSON-RPC params array
    'response': dict,        # Full JSON-RPC response
    'result': dict,          # Response result object
    'status': dict,          # Response status (code, message)
    'duration': float,       # Request duration in seconds
    'timestamp': str         # ISO timestamp of request
}
```

## Common Use Cases

### 1. Debugging Failed Requests

```python
from hfortix import FortiOS, APIError

fgt = FortiOS("192.168.1.99", token="your_token")

try:
    # This might fail
    fgt.api.cmdb.firewall.policy.post({
        "policyid": 100,
        "name": "test-policy"
        # Missing required fields
    })
except APIError as e:
    # Inspect what went wrong
    last_req = fgt.http_api_request()
    
    print(f"Request failed:")
    print(f"  Method: {last_req['method']}")
    print(f"  URL: {last_req['url']}")
    print(f"  Body: {last_req['body']}")
    print(f"  Status: {last_req['status_code']}")
    print(f"  Error: {last_req['response']}")
```

### 2. Audit Trail

```python
import json
from datetime import datetime

# Store all API operations for audit
audit_log = []

fgt = FortiOS("192.168.1.99", token="your_token")

# Create address
fgt.api.cmdb.firewall.address.post({
    "name": "server1",
    "subnet": "10.0.1.10 255.255.255.255"
})
audit_log.append(fgt.http_api_request())

# Update address
fgt.api.cmdb.firewall.address.put("server1", {
    "comment": "Production server"
})
audit_log.append(fgt.http_api_request())

# Delete address
fgt.api.cmdb.firewall.address.delete("server1")
audit_log.append(fgt.http_api_request())

# Save audit log
with open("audit.json", "w") as f:
    json.dump(audit_log, f, indent=2)
```

### 3. Performance Analysis

```python
import statistics

fgt = FortiOS("192.168.1.99", token="your_token")

durations = []

# Test multiple requests
for i in range(10):
    fgt.api.cmdb.firewall.address.get()
    req = fgt.http_api_request()
    durations.append(req['duration'])

print(f"Average latency: {statistics.mean(durations):.3f}s")
print(f"Min latency: {min(durations):.3f}s")
print(f"Max latency: {max(durations):.3f}s")
```

### 4. Learning the API

```python
# Make a high-level call
fgt = FortiOS("192.168.1.99", token="your_token")

response = fgt.api.cmdb.firewall.policy.post({
    "policyid": 100,
    "name": "allow-web",
    "srcintf": [{"name": "internal"}],
    "dstintf": [{"name": "wan1"}],
    "srcaddr": [{"name": "all"}],
    "dstaddr": [{"name": "all"}],
    "action": "accept",
    "schedule": "always",
    "service": [{"name": "HTTP"}]
})

# See exactly what was sent
req = fgt.http_api_request()

print("To create this policy, the SDK sent:")
print(f"  {req['method']} {req['url']}")
print(f"  Body: {json.dumps(req['body'], indent=2)}")
```

### 5. Custom Monitoring

```python
class APIMonitor:
    def __init__(self, fgt):
        self.fgt = fgt
        self.requests = []
    
    def track_request(self):
        """Call after each API operation"""
        req = self.fgt.http_api_request()
        self.requests.append(req)
        
        # Alert on errors
        if req['status_code'] >= 400:
            print(f"⚠️  API Error: {req['method']} {req['url']}")
            print(f"   Status: {req['status_code']}")
            print(f"   Error: {req['response'].get('error')}")
    
    def report(self):
        """Generate summary report"""
        total = len(self.requests)
        errors = sum(1 for r in self.requests if r['status_code'] >= 400)
        avg_duration = statistics.mean(r['duration'] for r in self.requests)
        
        print(f"\nAPI Usage Summary:")
        print(f"  Total requests: {total}")
        print(f"  Errors: {errors}")
        print(f"  Success rate: {(total-errors)/total*100:.1f}%")
        print(f"  Average duration: {avg_duration:.3f}s")

# Use the monitor
fgt = FortiOS("192.168.1.99", token="your_token")
monitor = APIMonitor(fgt)

# Make some API calls
fgt.api.cmdb.firewall.address.get()
monitor.track_request()

fgt.api.cmdb.firewall.policy.get()
monitor.track_request()

monitor.report()
```

## Advanced Features

### Request History

The SDK only stores the **last request** by default. To track multiple requests:

```python
class RequestHistory:
    def __init__(self, fgt):
        self.fgt = fgt
        self.history = []
    
    def record(self):
        """Record the last request"""
        req = self.fgt.http_api_request()
        self.history.append(req)
        return req
    
    def get_by_method(self, method):
        """Get all requests with a specific HTTP method"""
        return [r for r in self.history if r['method'] == method]
    
    def get_errors(self):
        """Get all failed requests"""
        return [r for r in self.history if r['status_code'] >= 400]

# Usage
fgt = FortiOS("192.168.1.99", token="your_token")
history = RequestHistory(fgt)

# Make requests and record them
fgt.api.cmdb.firewall.address.get()
history.record()

fgt.api.cmdb.firewall.policy.get()
history.record()

# Analyze
print(f"Total requests: {len(history.history)}")
print(f"GET requests: {len(history.get_by_method('GET'))}")
print(f"Errors: {len(history.get_errors())}")
```

### Filtering Sensitive Data

```python
def sanitize_request(request):
    """Remove sensitive data from request"""
    sanitized = request.copy()
    
    # Remove authentication headers
    if 'headers' in sanitized:
        headers = sanitized['headers'].copy()
        headers.pop('Authorization', None)
        headers.pop('X-CSRFTOKEN', None)
        sanitized['headers'] = headers
    
    # Remove sensitive fields from body
    if 'body' in sanitized and isinstance(sanitized['body'], dict):
        body = sanitized['body'].copy()
        body.pop('password', None)
        body.pop('secret', None)
        sanitized['body'] = body
    
    return sanitized

# Usage
fgt.api.cmdb.system.admin.post({
    "name": "newadmin",
    "password": "SecretPassword123"  # Sensitive!
})

req = fgt.http_api_request()
safe_req = sanitize_request(req)

# Safe to log or store
print(json.dumps(safe_req, indent=2))
```

### Transaction Inspection

When using transactions, you can inspect individual operations:

```python
from hfortix import FortiOS

fgt = FortiOS("192.168.1.99", token="your_token")

with fgt.transaction() as txn:
    # First operation
    fgt.api.cmdb.firewall.address.post({"name": "addr1", "subnet": "10.0.1.1/32"})
    req1 = fgt.http_api_request()
    print(f"Op 1: {req1['method']} {req1['url']}")
    
    # Second operation
    fgt.api.cmdb.firewall.address.post({"name": "addr2", "subnet": "10.0.1.2/32"})
    req2 = fgt.http_api_request()
    print(f"Op 2: {req2['method']} {req2['url']}")
    
    # Show transaction details (FortiOS 7.4.1+)
    details = txn.show()
    print(f"Transaction commands: {details}")

# After commit, you can still inspect the last operation
final_req = fgt.http_api_request()
print(f"Final operation: {final_req['method']} {final_req['url']}")
```

## Integration Examples

### Logging Integration

```python
import logging
import json

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('fortios_api')

fgt = FortiOS("192.168.1.99", token="your_token")

# Make API call
fgt.api.cmdb.firewall.address.get("server1")

# Log the request
req = fgt.http_api_request()
logger.info(
    f"API Request: {req['method']} {req['url']} - "
    f"Status: {req['status_code']} - "
    f"Duration: {req['duration']:.3f}s"
)

# Log full details at debug level
logger.debug(f"Full request: {json.dumps(req, indent=2)}")
```

### Metrics Collection (Prometheus)

```python
from prometheus_client import Counter, Histogram, start_http_server

# Define metrics
api_requests_total = Counter(
    'fortios_api_requests_total',
    'Total FortiOS API requests',
    ['method', 'status']
)

api_request_duration = Histogram(
    'fortios_api_request_duration_seconds',
    'FortiOS API request duration'
)

def track_api_metrics(fgt):
    """Track request metrics"""
    req = fgt.http_api_request()
    
    # Record metrics
    status = 'success' if req['status_code'] < 400 else 'error'
    api_requests_total.labels(method=req['method'], status=status).inc()
    api_request_duration.observe(req['duration'])

# Start Prometheus metrics server
start_http_server(8000)

# Make API calls and track metrics
fgt = FortiOS("192.168.1.99", token="your_token")

fgt.api.cmdb.firewall.address.get()
track_api_metrics(fgt)

fgt.api.cmdb.firewall.policy.get()
track_api_metrics(fgt)
```

### Testing/Mocking

```python
import unittest
from unittest.mock import Mock, patch

class TestFirewallOperations(unittest.TestCase):
    def test_address_creation(self):
        # Mock FortiOS client
        fgt = Mock()
        fgt.http_api_request.return_value = {
            'method': 'POST',
            'url': 'https://192.168.1.99/api/v2/cmdb/firewall/address',
            'status_code': 200,
            'response': {'status': 'success'},
            'duration': 0.123
        }
        
        # Your code that uses the client
        create_firewall_address(fgt, "server1", "10.0.1.10/32")
        
        # Verify the request was made
        req = fgt.http_api_request()
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['status_code'], 200)
```

## Best Practices

### 1. Always Check After Critical Operations

```python
# Create important object
fgt.api.cmdb.firewall.policy.post({...})

# Verify it succeeded
req = fgt.http_api_request()
if req['status_code'] != 200:
    logger.error(f"Policy creation failed: {req['response']}")
    raise Exception("Failed to create policy")
```

### 2. Use for Debugging, Not Production Logic

```python
# ❌ Bad: Don't rely on http_api_request for application logic
response = fgt.api.cmdb.firewall.address.get("server1")
req = fgt.http_api_request()
if req['status_code'] == 200:
    # Use response directly, not req['response']
    
# ✅ Good: Use for debugging and monitoring
try:
    response = fgt.api.cmdb.firewall.address.get("server1")
    # Use response here
except APIError as e:
    # Use http_api_request to understand the error
    req = fgt.http_api_request()
    logger.debug(f"Request details: {req}")
```

### 3. Sanitize Before Logging

```python
# Always remove sensitive data before logging/storing
req = fgt.http_api_request()
safe_req = sanitize_request(req)
logger.info(f"Request: {safe_req}")
```

### 4. Use Structured Logging

```python
import structlog

logger = structlog.get_logger()

fgt.api.cmdb.firewall.address.get("server1")
req = fgt.http_api_request()

logger.info(
    "api_request",
    method=req['method'],
    url=req['url'],
    status_code=req['status_code'],
    duration=req['duration']
)
```

## Limitations

### 1. Only Last Request

The SDK stores only the **most recent request**. For multiple requests, implement your own history:

```python
# This only shows the last request
fgt.api.cmdb.firewall.address.get("addr1")
fgt.api.cmdb.firewall.address.get("addr2")
req = fgt.http_api_request()  # Only shows addr2 request
```

### 2. No Automatic Filtering

Sensitive data is not filtered automatically. Always sanitize before sharing:

```python
req = fgt.http_api_request()
# req may contain tokens, passwords, etc.
# Sanitize before logging or storing
```

### 3. FortiOS vs FortiManager

Use the correct method for each platform:
- FortiOS: `fgt.http_api_request()`
- FortiManager: `fmg.fmg_api_request()`

## Troubleshooting

### Request Returns None

**Symptom:** `http_api_request()` returns `None` or empty dict

**Cause:** No request has been made yet

**Solution:**
```python
# Make sure to call an API method first
fgt.api.cmdb.firewall.address.get()
req = fgt.http_api_request()  # Now returns data
```

### Missing Request Details

**Symptom:** Some fields are missing from the request object

**Cause:** Different request types have different fields

**Solution:**
```python
req = fgt.http_api_request()

# Always check if field exists
method = req.get('method', 'UNKNOWN')
body = req.get('body', {})  # May not exist for GET requests
```

### Old Request Data

**Symptom:** Request object shows old data

**Cause:** Only the last request is stored

**Solution:**
```python
# Get request immediately after the operation you want to inspect
fgt.api.cmdb.firewall.address.get("server1")
req = fgt.http_api_request()  # Get it immediately

# Don't wait or make other calls
fgt.api.cmdb.firewall.policy.get()  # This overwrites the previous request
```

## See Also

- [Transactions](TRANSACTIONS.md)
- [Error Handling](ERROR_HANDLING_CONFIG.md)
- [Audit Logging](AUDIT_LOGGING.md)
- [Debugging Guide](DEBUGGING.md)
