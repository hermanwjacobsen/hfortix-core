# Core Package Features Reference

**Quick reference for what's already built into `hfortix_core`**

This document lists production-ready features available in the core package that the generator and generated code should leverage.

---

## 🎯 Key Takeaway

**Don't re-implement these!** They're already production-ready and extensively tested.

---

## Audit & Logging

### AuditHandler Protocol
**Location:** `hfortix_core.audit.base`

```python
from hfortix_core.audit import AuditHandler, AuditOperation

class MyHandler:
    def log_operation(self, operation: dict[str, Any]) -> None:
        # operation is an AuditOperation TypedDict with:
        # - timestamp, request_id, method, endpoint
        # - api_type, path, vdom, action
        # - object_type, object_name
        # - data, params (both sanitized)
        # - status_code, success, duration_ms
        # - error, user_context, host
        # - read_only_mode
        pass

# Usage
fgt = FortiOS("...", token="...", audit_handler=MyHandler(), track_operations=True)
```

**Features:**
- ✅ Full operation metadata
- ✅ Automatic sensitive data sanitization
- ✅ Request ID for correlation
- ✅ Duration tracking
- ✅ Read-only mode indicator

---

## Request Hooks

### BeforeRequestHook Protocol
**Location:** `hfortix_core.hooks`

```python
from hfortix_core.hooks import BeforeRequestHook, RequestContext

class ValidationHook:
    def before_request(self, context: dict[str, Any]) -> dict[str, Any]:
        # context is RequestContext TypedDict with:
        # - method, api_type, path
        # - data, params (mutable!)
        # - vdom, endpoint, request_id
        # - user_context
        
        # Validate
        if not context['data'].get('required_field'):
            raise ValueError("Missing required field")
        
        # Transform
        context['data']['auto_added'] = True
        
        return context

# Usage
fgt = FortiOS("...", token="...", before_request_hooks=[ValidationHook()])
```

**Use Cases:**
- ✅ Request validation
- ✅ Data transformation
- ✅ Adding headers/parameters
- ✅ Request cancellation (raise exception)
- ✅ Logging/auditing

### AfterRequestHook Protocol
**Location:** `hfortix_core.hooks`

```python
from hfortix_core.hooks import AfterRequestHook

class CacheHook:
    def after_request(
        self, context: dict[str, Any], response: dict[str, Any]
    ) -> dict[str, Any]:
        # Called after successful requests (2xx only)
        # Can transform response, log, cache, etc.
        
        if context['method'] == 'GET':
            self.cache[context['endpoint']] = response
        
        return response

# Usage
fgt = FortiOS("...", token="...", after_request_hooks=[CacheHook()])
```

**Use Cases:**
- ✅ Response transformation
- ✅ Caching
- ✅ Success logging
- ✅ Triggering side effects

---

## Resilience Features

### Read-Only Mode (Dry-Run)
**Location:** `hfortix_core.http.client` (HTTPClient parameter)

```python
# Simulate write operations without executing
fgt = FortiOS("192.168.1.99", token="...", read_only=True)

# GET requests execute normally
addresses = fgt.api.cmdb.firewall.address.get()  # Real API call

# POST/PUT/DELETE are simulated (NOT sent to FortiGate)
result = fgt.api.cmdb.firewall.address.post(name="test", ...)  # Simulated
# Returns success response without making API call

# Audit logs show: read_only_mode: true
```

**Use Cases:**
- ✅ Testing without modifying FortiGate
- ✅ CI/CD pipeline validation
- ✅ Configuration preview
- ✅ Training/learning

### Circuit Breaker
**Location:** `hfortix_core.http.base` (BaseHTTPClient)

```python
fgt = FortiOS(
    "192.168.1.99", 
    token="...",
    circuit_breaker_threshold=10,        # Open after 10 consecutive failures
    circuit_breaker_timeout=30.0,        # Wait 30s before transitioning to half-open
    circuit_breaker_auto_retry=True,     # Auto-retry when circuit opens
    circuit_breaker_max_retries=3,       # Max retry attempts
    circuit_breaker_retry_delay=5.0,     # Delay between retries
)

# Monitor circuit state
state = fgt._client.get_circuit_breaker_state()
# Returns: {"state": "closed|open|half_open", "failure_count": 0, ...}
```

**States:**
- **Closed:** Normal operation
- **Open:** Too many failures, requests fail fast
- **Half-Open:** Testing if service recovered

**Use Cases:**
- ✅ Prevent cascading failures
- ✅ Fast-fail on downstream issues
- ✅ Automatic recovery testing

### Adaptive Retry
**Location:** `hfortix_core.http.base` (BaseHTTPClient)

```python
fgt = FortiOS(
    "192.168.1.99", 
    token="...",
    adaptive_retry=True,              # Enable smart backoff
    retry_strategy="exponential",     # or "linear"
    retry_jitter=True,                # Add randomness (0-25%)
    max_retries=3,                    # Max attempts
)
```

**Features:**
- ✅ Monitors FortiGate response times
- ✅ Detects overload (503 errors, slow responses)
- ✅ Adjusts retry delays dynamically
- ✅ Exponential: 1s, 2s, 4s, 8s, 16s, 30s (capped)
- ✅ Linear: 1s, 2s, 3s, 4s, 5s
- ✅ Jitter prevents thundering herd

**Use Cases:**
- ✅ Transient network issues
- ✅ FortiGate overload handling
- ✅ Bulk operation resilience

---

## Exception Handling

### Exception Hierarchy
**Location:** `hfortix_core.exceptions`

```python
FortinetError                    # Base for all exceptions
└── APIError                     # Generic API error (base)
    ├── AuthenticationError      # 401 - Invalid credentials
    ├── PermissionDeniedError    # 403 - Insufficient permissions
    ├── ResourceNotFoundError    # 404 - Object not found
    ├── MethodNotAllowedError    # 405 - Wrong HTTP method
    ├── ResourceConflictError    # 409 - Object already exists
    ├── ValidationError          # 400 - Invalid request data
    ├── InternalServerError      # 500 - FortiGate internal error
    ├── ServiceUnavailableError  # 503 - FortiGate overloaded
    ├── CircuitBreakerOpen       # Circuit breaker triggered
    ├── InvalidVDOMError         # Invalid virtual domain
    ├── ObjectInUseError         # Cannot delete (in use)
    └── many more...
```

### Exception Metadata

All exceptions include:
```python
try:
    fgt.api.cmdb.firewall.address.get(name="missing")
except ResourceNotFoundError as e:
    print(e.http_status)      # 404
    print(e.error_code)       # FortiOS error code (e.g., -3)
    print(e.endpoint)         # '/api/v2/cmdb/firewall/address/missing'
    print(e.method)           # 'GET'
    print(e.params)           # Query params (sanitized)
    print(e.hint)             # "Object 'missing' does not exist"
    print(e.request_id)       # UUID for correlation
    print(e.timestamp)        # ISO 8601 timestamp
```

**Features:**
- ✅ Sensitive data sanitization (passwords, tokens masked)
- ✅ Context-aware error messages
- ✅ Helpful hints for resolution
- ✅ Request correlation via request_id
- ✅ Detailed metadata for debugging

---

## HTTP Client Features

### Connection Management
**Location:** `hfortix_core.http.client` (HTTPClient)

```python
fgt = FortiOS(
    "192.168.1.99",
    token="...",
    max_connections=100,               # Connection pool size
    max_keepalive_connections=20,      # Keepalive connections
    connect_timeout=10.0,              # Connection timeout (seconds)
    read_timeout=300.0,                # Read timeout (seconds)
    verify=True,                       # SSL verification
    user_agent="MyApp/1.0",            # Custom User-Agent
)
```

**Features:**
- ✅ HTTP/2 support via httpx
- ✅ Connection pooling
- ✅ Keepalive for performance
- ✅ Configurable timeouts
- ✅ SSL verification control
- ✅ Custom User-Agent for multi-team environments

### Session Management
**For username/password auth only**

```python
fgt = FortiOS(
    "192.168.1.99",
    username="admin",
    password="...",
    session_idle_timeout=300,  # Re-auth after 5min idle (matches FortiGate)
)
```

**Features:**
- ✅ Automatic session creation
- ✅ Proactive re-authentication on idle timeout
- ✅ Session cookie management
- ✅ Matches FortiGate's `remoteauthtimeout` setting

**Note:** Token auth is stateless, doesn't use sessions.

---

## Debugging

### Debug Information
**Location:** `hfortix_core.debug.base`

```python
from hfortix_core.debug import DebugInfo, RequestInfo

# Available TypedDicts:
# - DebugInfo: Comprehensive debug data
# - RequestInfo: Individual request details
# - SessionSummary: Session statistics
```

**Available Data:**
- ✅ Last request details
- ✅ Connection pool statistics
- ✅ Request history (if enabled)
- ✅ Response times
- ✅ Error tracking

---

## Additional Parameters

### User Context
**Pass custom metadata through all operations**

```python
fgt = FortiOS(
    "192.168.1.99",
    token="...",
    user_context={
        "ticket": "CHG-12345",
        "user": "john.doe",
        "team": "network-ops"
    }
)

# user_context available in:
# - Audit logs (operation['user_context'])
# - Request hooks (context['user_context'])
# - Exception metadata
```

### Custom Parameters in HTTPClient

```python
HTTPClient(
    url="https://192.168.1.99",
    verify=True,
    token="...",
    vdom="root",                           # Default VDOM
    max_retries=3,
    connect_timeout=10.0,
    read_timeout=300.0,
    user_agent="MyApp/1.0",
    circuit_breaker_threshold=10,
    circuit_breaker_timeout=30.0,
    circuit_breaker_auto_retry=False,
    circuit_breaker_max_retries=3,
    circuit_breaker_retry_delay=5.0,
    max_connections=100,
    max_keepalive_connections=20,
    session_idle_timeout=300,              # For username/password auth
    read_only=False,
    track_operations=False,
    adaptive_retry=False,
    retry_strategy="exponential",
    retry_jitter=False,
    audit_handler=None,
    audit_callback=None,                   # Deprecated, use audit_handler
    user_context=None,
)
```

---

## Generator Integration Guidelines

### ✅ DO Reference Core Features

In generated docstrings:
```python
def post(...):
    """
    Create a new firewall address.
    
    ... field documentation ...
    
    Testing & Validation:
        Use read_only mode to test without modifying FortiGate:
        >>> fgt = FortiOS("...", token="...", read_only=True)
        >>> fgt.api.cmdb.firewall.address.post(name="test", ...)
    
    Audit Logging:
        Track all operations with custom handler:
        >>> handler = MyAuditHandler()
        >>> fgt = FortiOS("...", token="...", audit_handler=handler)
    
    Raises:
        ResourceNotFoundError: Object not found (404)
        PermissionDeniedError: Insufficient permissions (403)
        ValidationError: Invalid request data (400)
        ResourceConflictError: Object already exists (409)
    """
```

### ❌ DON'T Re-Implement

- ❌ Don't create new audit logging systems
- ❌ Don't implement retry logic in generated code
- ❌ Don't create new exception base classes
- ❌ Don't implement dry-run logic in methods
- ❌ Don't create new hook systems

### ✅ DO Leverage

- ✅ Use existing exception types
- ✅ Document audit_handler usage
- ✅ Reference read_only mode
- ✅ Mention before_request_hooks for validation
- ✅ Use IHTTPClient protocol

---

## Quick Reference

| Feature | Location | Parameter | Status |
|---------|----------|-----------|--------|
| Audit Logging | `hfortix_core.audit` | `audit_handler`, `track_operations` | ✅ Ready |
| Request Hooks | `hfortix_core.hooks` | `before_request_hooks`, `after_request_hooks` | ✅ Ready |
| Read-Only Mode | `hfortix_core.http.client` | `read_only=True` | ✅ Ready |
| Circuit Breaker | `hfortix_core.http.base` | `circuit_breaker_*` | ✅ Ready |
| Adaptive Retry | `hfortix_core.http.base` | `adaptive_retry=True` | ✅ Ready |
| Retry Strategy | `hfortix_core.http.base` | `retry_strategy="exponential"` | ✅ Ready |
| Retry Jitter | `hfortix_core.http.base` | `retry_jitter=True` | ✅ Ready |
| Rich Exceptions | `hfortix_core.exceptions` | Automatic | ✅ Ready |
| User Context | `hfortix_core.http.client` | `user_context={}` | ✅ Ready |
| Debug Info | `hfortix_core.debug` | TypedDicts | ✅ Ready |
| HTTP/2 Support | `hfortix_core.http.client` | Automatic (httpx) | ✅ Ready |
| Session Mgmt | `hfortix_core.http.client` | `session_idle_timeout` | ✅ Ready |

---

## Example: Full Featured Usage

```python
from hfortix_fortios import FortiOS
from hfortix_core.audit import AuditHandler
from hfortix_core.hooks import BeforeRequestHook

# Custom audit handler
class SyslogAudit:
    def log_operation(self, op: dict) -> None:
        send_to_syslog(op)

# Validation hook
class TicketValidator:
    def before_request(self, ctx: dict) -> dict:
        if ctx['method'] in ('POST', 'PUT', 'DELETE'):
            if not ctx.get('user_context', {}).get('ticket'):
                raise ValueError("Change ticket required!")
        return ctx

# Create client with all features
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    
    # Audit & Tracking
    audit_handler=SyslogAudit(),
    track_operations=True,
    user_context={"ticket": "CHG-12345", "user": "john.doe"},
    
    # Request Hooks
    before_request_hooks=[TicketValidator()],
    
    # Resilience
    adaptive_retry=True,
    retry_strategy="exponential",
    retry_jitter=True,
    max_retries=3,
    circuit_breaker_threshold=10,
    circuit_breaker_timeout=30.0,
    circuit_breaker_auto_retry=True,
    
    # Connection
    max_connections=100,
    connect_timeout=10.0,
    read_timeout=300.0,
    
    # Testing
    read_only=False,  # Set True for testing
    
    # Debugging
    user_agent="NetworkOps-Automation/1.0",
)

# Use API
try:
    result = fgt.api.cmdb.firewall.address.post(
        name="server1",
        subnet="192.168.1.100 255.255.255.255"
    )
except ResourceConflictError:
    print("Address already exists")
except PermissionDeniedError:
    print("Insufficient permissions")
```

---

## Summary

The core package is **feature-complete** for:
- ✅ Audit logging and tracking
- ✅ Request interception and transformation
- ✅ Resilience (retry, circuit breaker, backoff)
- ✅ Testing (read-only/dry-run mode)
- ✅ Exception handling with rich context
- ✅ Connection management
- ✅ Session handling

**Generators should:**
1. Document these features in generated code
2. Reference appropriate protocols and types
3. Use existing exceptions
4. NOT re-implement any of these features

**This allows generated code to be simpler and leverage battle-tested infrastructure!**
