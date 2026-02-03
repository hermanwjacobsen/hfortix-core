# Out of Scope for v0.5.0

**Features explicitly excluded from the initial generator release**

This document lists features that are **intentionally not being implemented** in v0.5.0. They may be considered for future versions, but are currently out of scope to keep the initial release focused and achievable.

---

## Why This Document Exists

To maintain focus on the core goal: **Regenerate FortiOS API from schemas with enhanced validation and type safety.**

These features, while potentially useful, are:
- ❌ Too complex for initial release
- ❌ Too niche for most users
- ❌ Better suited for user-space implementations
- ❌ Would delay the core generator significantly

---

## Out of Scope Features

### 1. Configuration Templates ❌

**What it would be:**
Pre-defined templates for common configuration patterns.

**Example:**
```python
# Would allow this:
fgt.api.cmdb.firewall.address.from_template(
    "web_server",
    name="web1",
    ip="192.168.1.100"
)

# Instead of:
fgt.api.cmdb.firewall.address.post(
    name="web1",
    type="ipmask",
    subnet="192.168.1.100 255.255.255.255",
    comment="Web server",
    allow_routing="enable"
)
```

**Why Out of Scope:**
- ❌ Templates are highly organization-specific
- ❌ Hard to maintain (what's "common"?)
- ❌ Users can easily create their own wrapper functions
- ❌ Not schema-driven (manually curated)
- ❌ Would require separate template management system

**Better Alternative:**
Users can create their own helper functions:
```python
def create_web_server_address(fgt, name: str, ip: str):
    """Create address for web server (our org standard)"""
    return fgt.api.cmdb.firewall.address.post(
        name=name,
        type="ipmask",
        subnet=f"{ip} 255.255.255.255",
        comment="Web server",
        allow_routing="enable",
        color=1  # Our standard color
    )

# Use it:
create_web_server_address(fgt, "web1", "192.168.1.100")
```

**Verdict:** ❌ Out of scope - users can implement themselves

---

### 2. Bulk Update with Conditions ❌

**What it would be:**
Update multiple objects matching filter criteria.

**Example:**
```python
# Would allow this:
fgt.api.cmdb.firewall.address.update_where(
    filter={"subnet": "192.168.1.0 255.255.255.0"},
    updates={"subnet": "192.168.2.0 255.255.255.0"}
)

# Or with callback:
def update_subnet(address):
    if address["subnet"].startswith("192.168.1"):
        return {"subnet": address["subnet"].replace("192.168.1", "192.168.2")}
    return None

fgt.api.cmdb.firewall.address.bulk_update(update_subnet)
```

**Why Out of Scope:**
- ❌ Complex to implement safely (what if filter matches 1000s of objects?)
- ❌ Dangerous (bulk changes without explicit list)
- ❌ FortiOS API doesn't support bulk updates natively
- ❌ Would require GET all → filter → PUT each (inefficient)
- ❌ Error handling complex (partial failures)
- ❌ Not all endpoints support filtering the same way

**Better Alternative:**
Users can implement explicit bulk operations:
```python
# Get all addresses
addresses = fgt.api.cmdb.firewall.address.get()

# Filter and update explicitly
for addr in addresses.get("results", []):
    if addr["subnet"] == "192.168.1.0 255.255.255.0":
        fgt.api.cmdb.firewall.address.put(
            name=addr["name"],
            subnet="192.168.2.0 255.255.255.0"
        )
```

Or use the proposed `set_batch()` (which is in scope):
```python
# Explicit list of changes
updates = [
    {"name": "addr1", "subnet": "192.168.2.0 255.255.255.0"},
    {"name": "addr2", "subnet": "192.168.2.0 255.255.255.0"},
]
fgt.api.cmdb.firewall.address.set_batch(updates)
```

**Verdict:** ❌ Out of scope - too dangerous, users can implement safer alternatives

---

### 3. Custom Business Logic Validation Rules ❌

**What it would be:**
Framework for users to define organization-specific validation rules.

**Example from ADDITIONAL_SUGGESTIONS.md:**
```python
# Define custom validation rules
def validate_subnet_policy(payload):
    """Ensure all addresses use approved subnets"""
    approved_subnets = ["192.168.1", "10.0.0", "172.16"]
    
    if "subnet" in payload:
        subnet = payload["subnet"].split()[0]
        if not any(subnet.startswith(s) for s in approved_subnets):
            return False, f"Subnet {subnet} not in approved list"
    
    return True, None

# Register validator
fgt.api.cmdb.firewall.address.add_validator(validate_subnet_policy)

# Now enforced on all operations
fgt.api.cmdb.firewall.address.post(
    name="test",
    subnet="203.0.113.1 255.255.255.255"
)
# Raises: ValidationError("Subnet 203.0.113.1 not in approved list")
```

**Why Out of Scope:**
- ❌ Business logic is organization-specific (not universal)
- ❌ Would require validator registration system in generated code
- ❌ Would complicate API endpoint classes
- ❌ Validation rules change frequently (don't belong in generated code)
- ❌ Better handled by `BeforeRequestHook` (already available in core!)

**Better Alternative - Use BeforeRequestHook (Already Available!):**
```python
from hfortix_core.hooks import BeforeRequestHook

class SubnetPolicyHook:
    """Enforce approved subnet policy"""
    
    APPROVED_SUBNETS = ["192.168.1", "10.0.0", "172.16"]
    
    def before_request(self, context: dict) -> dict:
        # Only check firewall address POST/PUT
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

# Use it (no changes to generated code needed!)
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

**Clarification:**
The example in `ADDITIONAL_SUGGESTIONS.md` was **poorly worded**. It suggested adding `add_validator()` to generated code, which is wrong. 

**What we actually mean:**
- ✅ Users **should** implement custom business logic validation
- ✅ They **should** use `BeforeRequestHook` (already in core!)
- ❌ We should **NOT** add validator registration to generated code
- ❌ We should **NOT** create a validation framework in the generator

**The generator provides:**
- ✅ Schema-based validation (enums, ranges, required fields, dependencies)
- ✅ Documentation on how to use hooks for custom validation

**Users provide:**
- ✅ Organization-specific business rules via hooks
- ✅ Custom validation logic in their own code

**Verdict:** ❌ Out of scope - use existing `BeforeRequestHook` instead

---

### 4. Object Relationship Visualization ❌

**What it would be:**
Show which objects reference this object before deletion.

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

**Why Out of Scope:**
- ❌ FortiOS API doesn't provide reverse lookup natively
- ❌ Would require scanning ALL endpoints for references (extremely slow)
- ❌ Different field types reference differently (string, array, datasource)
- ❌ Can't know all possible reference locations
- ❌ Would need to maintain reference map (manual, error-prone)
- ❌ FortiOS already prevents deletion of in-use objects (returns error)

**Better Alternative:**
FortiOS already handles this:
```python
try:
    fgt.api.cmdb.firewall.address.delete("server1")
except ObjectInUseError as e:
    print(f"Cannot delete: {e.hint}")
    # FortiOS error tells you it's in use
    # Check policies manually or use FortiGate GUI
```

**Verdict:** ❌ Out of scope - FortiOS already prevents invalid deletions

---

### 5. Configuration Snapshots ❌

**What it would be:**
Save complete configuration state for rollback.

**Example:**
```python
# Take snapshot before changes
snapshot = fgt.api.snapshot(name="before_migration", scope="firewall.address")

try:
    # Make lots of changes
    fgt.api.cmdb.firewall.address.set(...)
    fgt.api.cmdb.firewall.address.set(...)
except Exception:
    # Restore from snapshot on error
    snapshot.restore()
```

**Why Out of Scope:**
- ❌ FortiOS has built-in backup/restore (config backup)
- ❌ Not API-focused (configuration management tool territory)
- ❌ Complex to implement (dependencies between objects)
- ❌ Storage requirements (where to store snapshots?)
- ❌ Versioning complexity
- ❌ Better handled by external tools (Ansible, Terraform)

**Better Alternative:**
Use FortiOS built-in backup or external tools:
```python
# Export current config using FortiOS backup API
backup = fgt.api.monitor.system.config.backup.download()
save_to_file("backup_before_migration.conf", backup)

# Or use external configuration management:
# - Ansible with fortios modules
# - Terraform with fortios provider
# - Git to version control exported configs
```

**Verdict:** ❌ Out of scope - use FortiOS backup or external tools

---

### 6. Field History/Changelog ❌

**What it would be:**
Track which fields changed over time.

**Example:**
```python
history = fgt.api.cmdb.firewall.address.get_history(
    name="server1",
    since="2026-01-01"
)
# Returns list of changes with timestamps, users, old/new values
```

**Why Out of Scope:**
- ❌ FortiOS doesn't store field-level change history via API
- ❌ Would require external database to track changes
- ❌ Audit logging already provides operation tracking
- ❌ FortiOS has built-in audit logs (config change log)
- ❌ Not generator responsibility (monitoring tool territory)

**Better Alternative:**
Use audit logging (already in core!):
```python
class ChangeTracker:
    def __init__(self):
        self.changes = []
    
    def log_operation(self, operation: dict) -> None:
        if operation['method'] in ('POST', 'PUT', 'DELETE'):
            self.changes.append({
                'timestamp': operation['timestamp'],
                'object': operation['object_name'],
                'action': operation['action'],
                'data': operation['data'],
            })

tracker = ChangeTracker()
fgt = FortiOS("...", token="...", audit_handler=tracker)

# Later: review changes
for change in tracker.changes:
    print(f"{change['timestamp']}: {change['action']} {change['object']}")
```

**Verdict:** ❌ Out of scope - use audit logging or FortiOS built-in logs

---

### 7. Transaction Support ❌

**What it would be:**
Group multiple operations, rollback on failure.

**Example:**
```python
with fgt.api.transaction() as txn:
    txn.add(fgt.api.cmdb.firewall.address.post(name="addr1", ...))
    txn.add(fgt.api.cmdb.firewall.address.post(name="addr2", ...))
    txn.add(fgt.api.cmdb.firewall.policy.post(name="policy1", ...))
    # If any fails, all rollback
```

**Why Out of Scope:**
- ❌ FortiOS API doesn't support transactions
- ❌ Would require complex rollback logic (delete what was created)
- ❌ Can't truly rollback (other users might have modified objects)
- ❌ Partial failure handling is complex
- ❌ Better handled at application level

**Better Alternative:**
Implement application-level rollback:
```python
created_objects = []

try:
    addr1 = fgt.api.cmdb.firewall.address.post(name="addr1", ...)
    created_objects.append(("address", "addr1"))
    
    addr2 = fgt.api.cmdb.firewall.address.post(name="addr2", ...)
    created_objects.append(("address", "addr2"))
    
    policy = fgt.api.cmdb.firewall.policy.post(name="policy1", ...)
    created_objects.append(("policy", "policy1"))
    
except Exception as e:
    # Rollback: delete what we created
    for obj_type, obj_name in reversed(created_objects):
        try:
            if obj_type == "address":
                fgt.api.cmdb.firewall.address.delete(obj_name)
            elif obj_type == "policy":
                fgt.api.cmdb.firewall.policy.delete(obj_name)
        except Exception:
            pass  # Best effort
    raise
```

**Verdict:** ❌ Out of scope - FortiOS doesn't support transactions

---

### 8. Performance Profiling ❌

**What it would be:**
Track API call timing and performance.

**Example:**
```python
fgt = FortiOS(host="...", token="...", profile=True)

# Make API calls
fgt.api.cmdb.firewall.address.get()
fgt.api.cmdb.firewall.policy.get()

# Get performance report
report = fgt.api.get_performance_report()
```

**Why Out of Scope:**
- ❌ Better handled by external APM tools
- ❌ Audit logging already tracks duration_ms
- ❌ Not generator responsibility
- ❌ Users can easily implement via AfterRequestHook

**Better Alternative:**
Use audit logging or hooks:
```python
class PerformanceTracker:
    def __init__(self):
        self.timings = []
    
    def log_operation(self, op: dict) -> None:
        self.timings.append({
            'endpoint': op['endpoint'],
            'duration_ms': op['duration_ms'],
        })
    
    def get_report(self):
        # Calculate stats
        by_endpoint = {}
        for t in self.timings:
            endpoint = t['endpoint']
            if endpoint not in by_endpoint:
                by_endpoint[endpoint] = []
            by_endpoint[endpoint].append(t['duration_ms'])
        
        return {
            endpoint: {
                'calls': len(times),
                'avg_ms': sum(times) / len(times),
                'max_ms': max(times),
            }
            for endpoint, times in by_endpoint.items()
        }

tracker = PerformanceTracker()
fgt = FortiOS("...", token="...", audit_handler=tracker)

# Use API...

# Get report
print(tracker.get_report())
```

**Verdict:** ❌ Out of scope - use audit logging or external tools

---

### 9. Relationship Traversal ❌

**What it would be:**
Follow datasource references automatically.

**Example:**
```python
address = fgt.api.cmdb.firewall.address.get(
    name="server1",
    expand_references=True  # Expand 'interface' reference
)
# Returns address with full interface object embedded
```

**Why Out of Scope:**
- ❌ Requires multiple API calls (performance impact)
- ❌ Can create circular references (infinite loops)
- ❌ Not all datasources should be expanded
- ❌ Complexity in generated code
- ❌ Users can easily fetch referenced objects themselves

**Better Alternative:**
Fetch references explicitly:
```python
# Get address
address = fgt.api.cmdb.firewall.address.get(name="server1")

# Get referenced interface if needed
if address.get("interface"):
    interface = fgt.api.cmdb.system.interface.get(name=address["interface"])
    # Use interface data...
```

**Verdict:** ❌ Out of scope - users can implement when needed

---

## Summary

**Out of Scope for v0.5.0:**
1. ❌ Configuration Templates - users can create helpers
2. ❌ Bulk Update with Conditions - too dangerous, use explicit updates
3. ❌ Custom Business Validation Rules - use `BeforeRequestHook` instead
4. ❌ Object Relationship Visualization - FortiOS prevents invalid deletions
5. ❌ Configuration Snapshots - use FortiOS backup or external tools
6. ❌ Field History/Changelog - use audit logging
7. ❌ Transaction Support - FortiOS doesn't support it
8. ❌ Performance Profiling - use audit logging or APM tools
9. ❌ Relationship Traversal - fetch references explicitly

**Key Principle:**
> If it's not schema-driven or can be implemented by users with existing hooks/features, it's out of scope.

**What IS in Scope:**
- ✅ Schema-based code generation
- ✅ Field validators from schema
- ✅ TypedDict and Literal types
- ✅ `set()` method (upsert)
- ✅ Smart validation with field dependencies
- ✅ Better error messages
- ✅ Documentation referencing core features
- ✅ Leveraging existing core infrastructure

**Focus Areas:**
1. Generate correct, type-safe code from schemas
2. Provide excellent developer experience (autocomplete, docs)
3. Validate against schema constraints
4. Document how to use existing core features
5. Keep generated code simple and maintainable

**The generator's job is to generate code, not to be a full-featured configuration management platform!**
