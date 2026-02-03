# mkey Complexity and Design Decision

**The Problem:** Different FortiOS endpoints use different field names as their primary key (mkey).

---

## The mkey Problem

In FortiOS API, each endpoint has a "master key" (mkey) that uniquely identifies objects. However, **the field name varies by endpoint:**

### Examples from Old Implementation:

**firewall.address** uses `name`:
```python
def get(self, name: str | None = None, ...):
    if name:
        endpoint = f"/firewall/address/{name}"
    
def put(self, name: str, ...):
    endpoint = f"/firewall/address/{name}"
    
def delete(self, name: str, ...):
    endpoint = f"/firewall/address/{name}"
```

**firewall.policy** uses `policyid`:
```python
def get(self, policyid: str | None = None, ...):
    if policyid:
        endpoint = f"/firewall/policy/{policyid}"
    
def put(self, policyid: str, ...):
    endpoint = f"/firewall/policy/{policyid}"
    
def delete(self, policyid: str, ...):
    endpoint = f"/firewall/policy/{policyid}"
```

**system.interface** uses `name`:
```python
def get(self, name: str | None = None, ...):
    if name:
        endpoint = f"/system/interface/{name}"
```

**user.local** uses `name`:
```python
def get(self, name: str | None = None, ...):
    if name:
        endpoint = f"/user/local/{name}"
```

**router.static** uses `seq_num`:
```python
def get(self, seq_num: str | None = None, ...):
    if seq_num:
        endpoint = f"/router/static/{seq_num}"
```

**firewall.schedule.onetime** uses `name`:
```python
def get(self, name: str | None = None, ...):
    if name:
        endpoint = f"/firewall/schedule/onetime/{name}"
```

---

## Why This Is Messy

### 1. **Inconsistent Method Signatures**

Every endpoint class has different method signatures:

```python
# Different parameter names for the same logical operation
fgt.api.cmdb.firewall.address.get(name="addr1")
fgt.api.cmdb.firewall.policy.get(policyid="1")
fgt.api.cmdb.router.static.get(seq_num="10")
fgt.api.cmdb.user.local.get(name="user1")
```

### 2. **Hard to Write Generic Code**

Can't easily write helpers that work across endpoints:

```python
# This doesn't work - different parameter names!
def safe_delete(endpoint, identifier):
    # What parameter name to use?
    endpoint.delete(???)  # name? policyid? seq_num? id?
```

### 3. **Schema Provides mkey Info**

FortiOS schemas include mkey field name:

```json
{
  "path": "firewall",
  "name": "address",
  "mkey": "name",
  "mkey_type": "string"
}
```

```json
{
  "path": "firewall",
  "name": "policy",
  "mkey": "policyid",
  "mkey_type": "integer"
}
```

```json
{
  "path": "router",
  "name": "static",
  "mkey": "seq-num",
  "mkey_type": "integer"
}
```

---

## Design Options

### Option 1: Keep Field-Specific Parameters (Current Approach) ✅

**Generated code uses actual field name from schema:**

```python
# firewall/address.py
class Address:
    def get(self, name: str | None = None, ...):
        if name:
            endpoint = f"/firewall/address/{name}"
    
    def put(self, name: str, ...):
        endpoint = f"/firewall/address/{name}"
    
    def delete(self, name: str, ...) -> ...:
        endpoint = f"/firewall/address/{name}"
```

```python
# firewall/policy.py
class Policy:
    def get(self, policyid: str | None = None, ...):
        if policyid:
            endpoint = f"/firewall/policy/{policyid}"
    
    def put(self, policyid: str, ...):
        endpoint = f"/firewall/policy/{policyid}"
    
    def delete(self, policyid: str, ...) -> ...:
        endpoint = f"/firewall/policy/{policyid}"
```

**Pros:**
- ✅ **Explicit and clear** - matches FortiOS field names exactly
- ✅ **Type hints work perfectly** - IDE knows `name` vs `policyid`
- ✅ **Matches FortiOS documentation** - users know what to pass
- ✅ **No confusion** - parameter name matches object field name
- ✅ **Easy to generate** - use `schema.mkey` directly

**Cons:**
- ❌ Inconsistent across endpoints (can't write generic helpers easily)
- ❌ More verbose (but more explicit)

---

### Option 2: Generic `mkey` Parameter ❌

**Use generic `mkey` parameter for all endpoints:**

```python
# firewall/address.py
class Address:
    def get(self, mkey: str | None = None, ...):
        if mkey:
            endpoint = f"/firewall/address/{mkey}"
    
    def put(self, mkey: str, ...):
        endpoint = f"/firewall/address/{mkey}"
    
    def delete(self, mkey: str, ...) -> ...:
        endpoint = f"/firewall/address/{mkey}"
```

```python
# firewall/policy.py
class Policy:
    def get(self, mkey: str | int | None = None, ...):
        if mkey:
            endpoint = f"/firewall/policy/{mkey}"
    
    def put(self, mkey: str | int, ...):
        endpoint = f"/firewall/policy/{mkey}"
    
    def delete(self, mkey: str | int, ...) -> ...:
        endpoint = f"/firewall/policy/{mkey}"
```

**Usage:**
```python
# Generic but unclear
fgt.api.cmdb.firewall.address.get(mkey="addr1")  # What is mkey here? name!
fgt.api.cmdb.firewall.policy.get(mkey="1")       # What is mkey here? policyid!
```

**Pros:**
- ✅ Consistent across all endpoints
- ✅ Easy to write generic helpers

**Cons:**
- ❌ **Loss of clarity** - users must know what mkey means for each endpoint
- ❌ **Poor IDE experience** - doesn't show actual field name
- ❌ **Doesn't match FortiOS docs** - docs say "name" or "policyid", not "mkey"
- ❌ **Confusing for users** - what field is mkey referring to?
- ❌ **Type hints less helpful** - `mkey: str | int` vs `policyid: int`

---

### Option 3: Both Generic + Specific (Dual Parameters) ❌

**Provide both for flexibility:**

```python
class Address:
    def get(
        self, 
        name: str | None = None,
        mkey: str | None = None,  # Alias for name
        ...
    ):
        identifier = name or mkey
        if identifier:
            endpoint = f"/firewall/address/{identifier}"
```

**Pros:**
- ✅ Flexibility for both use cases

**Cons:**
- ❌ **Confusing** - which one to use?
- ❌ **Validation complexity** - what if both provided?
- ❌ **More code to maintain**
- ❌ **Doesn't solve the problem** - still have different field names

---

### Option 4: Use `**kwargs` and Magic ❌

**Generic method that inspects mkey from schema:**

```python
class Address:
    _mkey = "name"  # From schema
    
    def get(self, **kwargs):
        identifier = kwargs.get(self._mkey)
        if identifier:
            endpoint = f"/firewall/address/{identifier}"
```

**Usage:**
```python
fgt.api.cmdb.firewall.address.get(name="addr1")
fgt.api.cmdb.firewall.policy.get(policyid="1")
```

**Pros:**
- ✅ Flexible parameter names
- ✅ Matches field names from schema

**Cons:**
- ❌ **NO TYPE HINTS** - complete loss of type safety
- ❌ **NO IDE AUTOCOMPLETE** - users must guess parameters
- ❌ **Harder to debug** - magic behavior
- ❌ **Validation complexity** - must check kwargs for mkey field

---

## Decision: Option 1 (Field-Specific Parameters) ✅

**We will use actual field names from schema as method parameters.**

### Why:

1. **Clarity Over Consistency**
   - Explicit is better than implicit
   - Users immediately know what to pass
   - Matches FortiOS documentation exactly

2. **Type Safety**
   - Perfect IDE autocomplete
   - Type checkers work correctly
   - `policyid: int` vs `name: str` is valuable information

3. **User Experience**
   - FortiOS docs say "name" or "policyid" - so do we
   - No mental translation from "mkey" to actual field
   - Error messages reference actual field names

4. **Generation is Simple**
   - Read `schema.mkey` → use as parameter name
   - Read `schema.mkey_type` → use as type hint
   - No complex logic needed

### Handling the Inconsistency:

**For users who need generic code:**

```python
# They can use introspection or helper functions
def get_mkey_name(endpoint_class):
    """Get mkey parameter name for an endpoint"""
    import inspect
    sig = inspect.signature(endpoint_class.get)
    # First parameter after 'self' is the mkey
    params = list(sig.parameters.keys())
    return params[0] if len(params) > 0 else None

def safe_get(endpoint, identifier):
    """Generic get that works across endpoints"""
    mkey_name = get_mkey_name(endpoint)
    return endpoint.get(**{mkey_name: identifier})

# Usage
safe_get(fgt.api.cmdb.firewall.address, "addr1")
safe_get(fgt.api.cmdb.firewall.policy, "1")
```

**Or we provide a helper in the future:**

```python
# Future enhancement (v0.6.0+)
class Address:
    _mkey_field = "name"  # Metadata for generic code
    
    def get(self, name: str | None = None, ...):
        ...

# Generic helper can check _mkey_field
def delete_object(endpoint, identifier):
    mkey_field = getattr(endpoint, '_mkey_field', None)
    if mkey_field:
        return endpoint.delete(**{mkey_field: identifier})
```

---

## Implementation Plan

### 1. **Schema Parser Enhancement**

Extract mkey info from schema:

```python
def parse_endpoint_metadata(schema: dict) -> dict:
    return {
        "mkey": schema.get("mkey", "name"),  # Default to "name"
        "mkey_type": schema.get("mkey_type", "string"),
        # ... other metadata
    }
```

### 2. **Generator Uses mkey Info**

```python
def generate_get_method(endpoint_info: dict) -> str:
    mkey_name = endpoint_info["mkey"]
    mkey_type = TYPE_MAP[endpoint_info["mkey_type"]]  # "string" → str, "integer" → int
    
    return f'''
    def get(
        self,
        {mkey_name}: {mkey_type} | None = None,
        payload_dict: dict[str, Any] | None = None,
        ...
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get {endpoint_info["name"]} configuration.
        
        Args:
            {mkey_name}: Object identifier (optional for list, required for specific)
            ...
        """
        if {mkey_name}:
            endpoint = f"/{endpoint_info['path']}/{endpoint_info['name']}/{{{mkey_name}}}"
        else:
            endpoint = f"/{endpoint_info['path']}/{endpoint_info['name']}"
        ...
    '''
```

### 3. **Generated Code Examples**

**firewall/address.py:**
```python
class Address:
    """Address endpoint (mkey: name)"""
    _mkey_field = "name"  # Metadata for generic helpers
    
    def get(self, name: str | None = None, ...):
        """Get address configuration.
        
        Args:
            name: Address name (object identifier)
        """
        if name:
            endpoint = f"/firewall/address/{name}"
        ...
    
    def put(self, name: str, ...):
        """Update address configuration.
        
        Args:
            name: Address name (must exist)
        """
        endpoint = f"/firewall/address/{name}"
        ...
    
    def delete(self, name: str, ...):
        """Delete address object.
        
        Args:
            name: Address name to delete
        """
        endpoint = f"/firewall/address/{name}"
        ...
    
    def set(self, name: str, ...):
        """Create or update address (idempotent).
        
        Args:
            name: Address name
        """
        if self.exists(name):
            return self.put(name, ...)
        else:
            return self.post(name=name, ...)
    
    def exists(self, name: str, ...) -> bool:
        """Check if address exists.
        
        Args:
            name: Address name to check
        """
        ...
```

**firewall/policy.py:**
```python
class Policy:
    """Policy endpoint (mkey: policyid)"""
    _mkey_field = "policyid"  # Metadata for generic helpers
    
    def get(self, policyid: int | None = None, ...):
        """Get policy configuration.
        
        Args:
            policyid: Policy ID (object identifier)
        """
        if policyid:
            endpoint = f"/firewall/policy/{policyid}"
        ...
    
    def put(self, policyid: int, ...):
        """Update policy configuration.
        
        Args:
            policyid: Policy ID (must exist)
        """
        endpoint = f"/firewall/policy/{policyid}"
        ...
    
    def delete(self, policyid: int, ...):
        """Delete policy.
        
        Args:
            policyid: Policy ID to delete
        """
        endpoint = f"/firewall/policy/{policyid}"
        ...
    
    def set(self, policyid: int, ...):
        """Create or update policy (idempotent).
        
        Args:
            policyid: Policy ID
        """
        if self.exists(policyid):
            return self.put(policyid, ...)
        else:
            return self.post(policyid=policyid, ...)
    
    def exists(self, policyid: int, ...) -> bool:
        """Check if policy exists.
        
        Args:
            policyid: Policy ID to check
        """
        ...
```

### 4. **Type Mapping**

```python
TYPE_MAP = {
    "string": "str",
    "integer": "int",
}

def get_mkey_type_hint(mkey_type: str) -> str:
    return TYPE_MAP.get(mkey_type, "str")
```

---

## Documentation Strategy

### In Generated Docstrings:

Always mention the mkey field name in docstrings:

```python
class Address:
    """
    Address endpoint for firewall address objects.
    
    Primary Key: name (string)
    
    The `name` parameter uniquely identifies address objects.
    Required for get/put/delete operations on specific objects.
    """
```

### In API Reference:

Create a reference table:

| Endpoint | mkey Field | Type | Example |
|----------|------------|------|---------|
| firewall.address | name | str | "server1" |
| firewall.policy | policyid | int | 1 |
| firewall.addrgrp | name | str | "servers" |
| router.static | seq-num | int | 10 |
| user.local | name | str | "admin" |
| system.interface | name | str | "port1" |

### In User Guide:

Explain the mkey concept:

```markdown
## Understanding Object Identifiers (mkey)

Each FortiOS endpoint has a primary key field that uniquely identifies objects.
This field name varies by endpoint:

- `firewall.address` uses `name`
- `firewall.policy` uses `policyid`
- `router.static` uses `seq_num`

Our API mirrors FortiOS field names exactly for clarity.

**Example:**
```python
# Address uses 'name'
fgt.api.cmdb.firewall.address.get(name="server1")

# Policy uses 'policyid'
fgt.api.cmdb.firewall.policy.get(policyid=1)
```

**Why different names?**
This matches FortiOS API and documentation exactly. You'll never have to 
guess or translate - if FortiOS docs say "name", we use "name".
```

---

## Future Enhancement: Generic Helpers (v0.6.0+)

If users need generic code, we can provide helpers:

```python
# Future: Generic endpoint interface
class GenericEndpoint(Protocol):
    _mkey_field: str
    
    def get(self, **kwargs): ...
    def put(self, **kwargs): ...
    def delete(self, **kwargs): ...

def delete_by_id(endpoint: GenericEndpoint, identifier: str | int):
    """Delete object using its primary key"""
    mkey = endpoint._mkey_field
    return endpoint.delete(**{mkey: identifier})

# Usage
delete_by_id(fgt.api.cmdb.firewall.address, "addr1")
delete_by_id(fgt.api.cmdb.firewall.policy, 1)
```

But this is **not in scope for v0.5.0**.

---

## Summary

**Decision:** Use field-specific parameter names from schema

**Why:**
- Clarity and explicitness
- Perfect type hints
- Matches FortiOS documentation
- Better user experience
- Simpler to generate

**Trade-off:**
- Inconsistent across endpoints (accepted for clarity)
- Users who need generic code can use introspection or future helpers

**Implementation:**
1. Extract `mkey` and `mkey_type` from schema
2. Use as parameter name and type hint in generated methods
3. Add `_mkey_field` class variable for metadata
4. Document mkey concept clearly
5. Future: provide generic helpers if needed

**Priority:** Must implement in v0.5.0 (core feature)
