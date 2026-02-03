# Additional Generator Suggestions

These are extra ideas that came up during design discussions. They can be considered for future versions.

---

## 1. **~~Dry-Run Mode~~** ✅ ALREADY IMPLEMENTED

**Status:** Available as `read_only` mode in HTTPClient

**What's Available:**
- `read_only=True` parameter simulates write operations (POST/PUT/DELETE)
- Read operations (GET) execute normally
- Audit logs show `read_only_mode: true` for simulated operations
- Perfect for testing, validation, CI/CD pipelines

**Example (Already Works):**
```python
fgt = FortiOS(host="192.168.1.99", token="...", read_only=True)

# GET requests execute normally
addresses = fgt.api.cmdb.firewall.address.get()

# POST/PUT/DELETE are simulated (not sent to FortiGate)
result = fgt.api.cmdb.firewall.address.post(
    name="server1",
    subnet="192.168.1.100 255.255.255.255"
)
# Returns success response without actually creating object
```

**Available in Core:**
- `read_only: bool` parameter in HTTPClient
- Automatic detection of write operations
- Audit trail shows simulated vs real operations
- No API calls made for write operations in read-only mode

---

## 2. **Configuration Templates** ⭐⭐

**What:** Pre-defined templates for common configurations

**Why:** Faster setup for standard patterns

**Example:**
```python
# Use built-in template
result = fgt.api.cmdb.firewall.address.from_template(
    "web_server",
    name="web1",
    ip="192.168.1.100"
)

# Equivalent to:
# {
#   "name": "web1",
#   "type": "ipmask",
#   "subnet": "192.168.1.100 255.255.255.255",
#   "comment": "Web server",
#   "allow-routing": "enable"
# }

# Custom templates
templates = {
    "db_server": {
        "type": "ipmask",
        "comment": "Database server",
        "allow-routing": "disable",
        "color": 2
    }
}

result = fgt.api.cmdb.firewall.address.from_template(
    "db_server",
    name="db1",
    ip="10.0.0.50",
    templates=templates
)
```

---

## 3. **Pagination Helper** ⭐⭐

**What:** Automatic pagination for large result sets

**Why:** Simplify working with many objects

**Example:**
```python
# Manual pagination (current):
start = 0
count = 100
all_addresses = []
while True:
    batch = fgt.api.cmdb.firewall.address.get(start=start, count=count)
    if not batch.get("results"):
        break
    all_addresses.extend(batch["results"])
    start += count

# Auto pagination (proposed):
for address in fgt.api.cmdb.firewall.address.paginate(page_size=100):
    print(address["name"])

# Or get all at once:
all_addresses = fgt.api.cmdb.firewall.address.get_all()
```

---

## 4. **~~Audit Logging Hook~~** ✅ ALREADY IMPLEMENTED

**Status:** Available in `hfortix_core.audit` and `hfortix_core.hooks`

**What's Available:**
- `AuditHandler` protocol for custom audit logging
- `BeforeRequestHook` and `AfterRequestHook` protocols
- `audit_handler`, `audit_callback`, `before_request_hooks`, `after_request_hooks` parameters in HTTPClient
- Full request/response context with sanitization
- `track_operations` flag for enabling audit logging

**Example (Already Works):**
```python
from hfortix_core.audit import AuditHandler

class CustomAuditHandler:
    def log_operation(self, operation: dict) -> None:
        print(f"[AUDIT] {operation['method']} {operation['endpoint']}")
        print(f"  Status: {operation['status_code']}")
        print(f"  Duration: {operation['duration_ms']}ms")

# Use in client
fgt = FortiOS(
    "192.168.1.99", 
    token="...",
    audit_handler=CustomAuditHandler(),
    track_operations=True
)
```

**Available in Core:**
- `AuditOperation` TypedDict with all operation metadata
- `RequestContext` TypedDict for hooks
- Automatic sanitization of sensitive data
- Request ID tracking for correlation

---

## 5. **Smart Defaults from Environment** ⭐

**What:** Load common defaults from environment or config file

**Why:** Reduce repetition in scripts

**Example:**
```python
# .fortios_defaults.yaml
defaults:
  firewall.address:
    allow-routing: enable
    color: 1
  firewall.policy:
    action: accept
    logtraffic: all

# In code (auto-loaded):
fgt.api.cmdb.firewall.address.post(
    name="server1",
    subnet="192.168.1.100 255.255.255.255"
    # allow-routing: enable  <- automatically added
    # color: 1               <- automatically added
)
```

---

## 6. **Conflict Resolution Strategies** ⭐

**What:** Handle name conflicts automatically

**Why:** Simplify bulk imports

**Example:**
```python
# Import with conflict resolution
fgt.api.cmdb.firewall.address.import_config(
    "addresses.json",
    on_conflict="rename"  # or "skip", "overwrite", "error"
)

# If "server1" exists and file has "server1":
# - rename: Creates "server1_1"
# - skip: Keeps existing, doesn't import
# - overwrite: Replaces existing
# - error: Raises exception
```

---

## 7. **Field History/Changelog** ⭐

**What:** Track which fields changed over time

**Why:** Audit, debugging, rollback capability

**Example:**
```python
# Get change history for object
history = fgt.api.cmdb.firewall.address.get_history(
    name="server1",
    since="2026-01-01"
)

# Returns:
# [
#   {
#     "timestamp": "2026-01-03T10:00:00Z",
#     "operation": "update",
#     "fields_changed": {
#       "subnet": {
#         "old": "192.168.1.100 255.255.255.255",
#         "new": "192.168.2.100 255.255.255.255"
#       }
#     },
#     "user": "admin"
#   }
# ]
```

---

## 8. **Validation Pre-Check** ⭐⭐

**What:** Validate before sending to API

**Why:** Faster feedback, reduce API calls

**Example:**
```python
# Check validity without making API call
is_valid, errors = fgt.api.cmdb.firewall.address.validate(
    name="server1",
    type="ipmask",
    start_ip="10.0.0.1"  # Conflict!
)

if not is_valid:
    print("Validation errors:")
    for error in errors:
        print(f"  - {error}")
    # Validation errors:
    #   - Field 'start-ip' conflicts with type='ipmask'
    #   - Missing required field 'subnet' for type='ipmask'
else:
    # Only send to API if valid
    fgt.api.cmdb.firewall.address.post(...)
```

---

## 9. **Search and Filter Helpers** ⭐⭐

**What:** Human-readable search syntax

**Why:** Easier than FortiOS filter syntax

**Example:**
```python
# Current FortiOS syntax (cryptic):
addresses = fgt.api.cmdb.firewall.address.get(
    filter="type==ipmask,subnet@@192.168.1"
)

# Helper methods (clearer):
addresses = fgt.api.cmdb.firewall.address.search(
    type="ipmask",
    subnet_contains="192.168.1"
)

# Or using builder:
addresses = fgt.api.cmdb.firewall.address.find() \
    .where("type").equals("ipmask") \
    .where("subnet").contains("192.168.1") \
    .execute()
```

---

## 10. **Object Relationships Visualization** ⭐

**What:** Show which objects reference this object

**Why:** Understand dependencies before deletion

**Example:**
```python
# Check what uses this address
refs = fgt.api.cmdb.firewall.address.get_references("server1")

print(refs)
# {
#   "firewall.policy": [
#     {"name": "policy1", "field": "srcaddr"},
#     {"name": "policy5", "field": "dstaddr"}
#   ],
#   "firewall.addrgrp": [
#     {"name": "servers_group", "field": "member"}
#   ]
# }

# Safe delete (fails if references exist)
fgt.api.cmdb.firewall.address.delete("server1", safe=True)
# Raises: ReferencedObjectError("Cannot delete 'server1': used by 3 policies")
```

---

## 11. **Bulk Update with Conditions** ⭐

**What:** Update multiple objects matching criteria

**Why:** Mass configuration changes

**Example:**
```python
# Update all addresses with old subnet
fgt.api.cmdb.firewall.address.update_where(
    filter={"subnet": "192.168.1.0 255.255.255.0"},
    updates={"subnet": "192.168.2.0 255.255.255.0"}
)

# Or with callback for custom logic:
def update_subnet(address):
    old_subnet = address["subnet"]
    if old_subnet.startswith("192.168.1"):
        new_subnet = old_subnet.replace("192.168.1", "192.168.2")
        return {"subnet": new_subnet}
    return None

fgt.api.cmdb.firewall.address.bulk_update(update_subnet)
```

---

## 12. **Configuration Snapshots** ⭐⭐

**What:** Save complete configuration state for restore

**Why:** Backup before major changes, rollback capability

**Example:**
```python
# Take snapshot before changes
snapshot = fgt.api.snapshot(name="before_migration", scope="firewall.address")

try:
    # Make lots of changes
    fgt.api.cmdb.firewall.address.set(...)
    fgt.api.cmdb.firewall.address.set(...)
    # ...
except Exception as e:
    # Restore from snapshot on error
    snapshot.restore()
    raise

# Or manual restore later:
fgt.api.restore_snapshot("before_migration")
```

---

## 13. **~~Rate Limiting & Retry Strategies~~** ✅ PARTIALLY IMPLEMENTED

**Status:** Adaptive retry and circuit breaker available in HTTPClient

**What's Available:**
- **Adaptive Retry:** Monitors FortiGate health and adjusts retry delays
- **Circuit Breaker:** Opens after threshold failures, prevents cascading issues
- **Retry Strategies:** Exponential (default) or linear backoff
- **Retry Jitter:** Prevents thundering herd problem
- **Auto-Retry on Circuit Break:** Configurable retry behavior

**Example (Already Works):**
```python
fgt = FortiOS(
    host="192.168.1.99",
    token="...",
    adaptive_retry=True,              # Smart backoff based on FortiGate health
    retry_strategy="exponential",     # or "linear"
    retry_jitter=True,                # Add randomness to prevent herd
    max_retries=3,
    circuit_breaker_threshold=10,     # Open after 10 consecutive failures
    circuit_breaker_timeout=30.0,     # Wait 30s before retry
    circuit_breaker_auto_retry=True,  # Auto-retry when circuit opens
    circuit_breaker_max_retries=3,
    circuit_breaker_retry_delay=5.0,
)

# Automatically handles:
# - 503 errors (FortiGate overloaded)
# - Slow responses (backpressure detection)
# - Connection failures
# - Cascading failures (circuit breaker)
```

**Available in Core:**
- `adaptive_retry: bool` - Smart backoff with backpressure detection
- `retry_strategy: str` - "exponential" or "linear"
- `retry_jitter: bool` - Random jitter to prevent synchronization
- `max_retries: int` - Max attempts before giving up
- Circuit breaker with states: closed, open, half-open
- `get_circuit_breaker_state()` - Monitor circuit state

**Still Missing:**
- Explicit rate limiting (requests/second throttling)
- Rate limit detection from API responses
- Token bucket or leaky bucket algorithms

---

## 14. **~~Configuration Validation Rules~~** ❌ OUT OF SCOPE

**Status:** Use BeforeRequestHook instead (already in core)

**Why Out of Scope:**
- Business logic is organization-specific (not universal)
- Would require validator registration system in generated code
- Better handled by existing `BeforeRequestHook` protocol
- Validation rules change frequently (don't belong in generated code)

**What Users Should Do Instead:**
```python
from hfortix_core.hooks import BeforeRequestHook

class SubnetPolicyHook:
    """Enforce approved subnet policy using existing hooks"""
    APPROVED_SUBNETS = ["192.168.1", "10.0.0", "172.16"]
    
    def before_request(self, context: dict) -> dict:
        if "firewall/address" in context['path']:
            if context['method'] in ('POST', 'PUT'):
                data = context.get('data', {})
                if 'subnet' in data:
                    subnet = data['subnet'].split()[0]
                    if not any(subnet.startswith(s) for s in self.APPROVED_SUBNETS):
                        raise ValueError(
                            f"Subnet {subnet} not in approved list: "
                            f"{', '.join(self.APPROVED_SUBNETS)}"
                        )
        return context

# Use existing hook system (no changes to generated code!)
fgt = FortiOS(
    "192.168.1.99",
    token="...",
    before_request_hooks=[SubnetPolicyHook()]
)

# Now enforced automatically
fgt.api.cmdb.firewall.address.post(
    name="test",
    subnet="203.0.113.1 255.255.255.255"
)
# Raises: ValueError("Subnet 203.0.113.1 not in approved list: ...")
```

**Generator Responsibility:**
- ✅ Schema-based validation (enums, ranges, required fields)
- ✅ Document how to use hooks for custom validation
- ❌ Do NOT add validator registration to generated code

**See:** `.dev/OUT_OF_SCOPE.md` for detailed explanation

---

## 15. **Performance Profiling** ⭐

**What:** Track API call timing and performance

**Why:** Identify bottlenecks, optimize

**Example:**
```python
# Enable profiling
fgt = FortiOS(host="...", token="...", profile=True)

# Make API calls
fgt.api.cmdb.firewall.address.get()
fgt.api.cmdb.firewall.policy.get()

# Get performance report
report = fgt.api.get_performance_report()

print(report)
# {
#   "total_calls": 2,
#   "total_time": 1.234,
#   "by_endpoint": {
#     "firewall.address": {"calls": 1, "avg_time": 0.456},
#     "firewall.policy": {"calls": 1, "avg_time": 0.778}
#   },
#   "slowest": [
#     {"endpoint": "firewall.policy", "time": 0.778},
#     {"endpoint": "firewall.address", "time": 0.456}
#   ]
# }
```

---

## Summary

These additional suggestions focus on:

**Already Implemented in Core** ✅
- ✅ **Dry-run mode** (`read_only=True`) - Simulate write operations
- ✅ **Audit logging** (`audit_handler`, `track_operations`) - Full request/response tracking
- ✅ **Request hooks** (`BeforeRequestHook`, `AfterRequestHook`) - Intercept and modify requests
- ✅ **Adaptive retry** (`adaptive_retry=True`) - Smart backoff with backpressure detection
- ✅ **Circuit breaker** - Prevent cascading failures
- ✅ **Retry strategies** - Exponential/linear with jitter

**Developer Experience:**
- Templates, smart defaults
- Better search/filter syntax
- Validation pre-check

**Operations:**
- Pagination, bulk updates
- Explicit rate limiting (requests/second)
- Configuration snapshots
- Performance profiling

**Safety:**
- Reference checking before delete
- Conflict resolution strategies
- Custom validation rules

**Future Consideration:**
Most of these can be added incrementally in future versions without breaking existing code. They're optional enhancements that make the library more powerful while keeping the core simple.

---

**Priority Ranking (Excluding Already Implemented):**
1. 🥇 **Pagination helper** (very common need)
2. 🥈 **Validation pre-check** (faster development)
3. 🥉 **Search/filter helpers** (better DX)
4. **Smart defaults** (reduce repetition)
5. **Explicit rate limiting** (prevent 429 errors)
6. **Configuration templates** (faster setup)
7. **Object relationships** (understand dependencies)
8. **Bulk update with conditions** (mass changes)
9. **Configuration snapshots** (backup/restore)
10. **Performance profiling** (identify bottlenecks)
11. Everything else (nice but niche)

---

## Core Package Features Already Available

For reference, here's what's already built into `hfortix_core`:

### Audit & Logging
- `AuditHandler` protocol - Custom audit log handlers
- `AuditOperation` TypedDict - Full operation metadata
- `track_operations` flag - Enable/disable audit logging
- Automatic sanitization of sensitive data (passwords, tokens, etc.)
- Request ID tracking for correlation

### Hooks
- `BeforeRequestHook` protocol - Pre-request interception
- `AfterRequestHook` protocol - Post-response handling
- `RequestContext` TypedDict - Full request context
- Multiple hooks supported (list of handlers)

### Resilience
- **Circuit Breaker:**
  - States: closed, open, half-open
  - Configurable threshold and timeout
  - Auto-retry on circuit break (optional)
  - `get_circuit_breaker_state()` monitoring

- **Adaptive Retry:**
  - Monitors response times
  - Detects FortiGate overload (503 errors, slow responses)
  - Adjusts retry delays dynamically
  - Exponential or linear backoff strategies
  - Jitter support (prevent thundering herd)

### Read-Only Mode
- `read_only=True` - Simulate write operations
- GET requests execute normally
- POST/PUT/DELETE simulated (not sent)
- Audit logs mark simulated operations
- Perfect for testing and CI/CD

### HTTP Client Features
- HTTP/2 support via httpx
- Connection pooling
- Keepalive connections
- Configurable timeouts (connect, read)
- Session management (username/password auth)
- Session idle timeout with proactive re-authentication
- Custom User-Agent for multi-team environments
- SSL verification control

### Exception Handling
- Rich exception hierarchy
- FortiOS error code mapping
- HTTP status code handling
- Context-aware error messages
- Sensitive data sanitization in errors
- Request ID in exceptions for correlation

### Debugging
- `DebugInfo` TypedDict - Comprehensive debug data
- Request history tracking
- Connection statistics
- Response time metrics
- `user_context` for custom metadata

These features are production-ready and extensively tested. The generator should leverage them where appropriate!
