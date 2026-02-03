# Action Methods Implementation Plan

**Date:** January 3, 2026  
**Feature:** Add clone() and move() methods to generated endpoints  
**Status:** 📋 Planning

---

## Overview

FortiOS API supports special action parameters for certain endpoints:
- **`action=clone`** - Clone/duplicate an existing object
- **`action=move`** - Reorder objects (for sequence-based resources like policies)

These should be implemented as dedicated methods in generated endpoint classes for better developer experience.

---

## API Behavior

### Clone Action

**Query Parameters:**
```
action=clone
nkey=<new_name>
```

**Example:**
```http
POST /api/v2/cmdb/firewall/address/address1?action=clone&nkey=address1_clone
```

**Behavior:**
- Clones the resource specified in the path
- Creates new resource with ID specified in `nkey`
- Copies all properties from source to destination

**Applicable To:**
- Most CMDB objects (addresses, policies, services, etc.)
- Objects that can be duplicated

---

### Move Action

**Query Parameters:**
```
action=move
before=<mkey>  (mutually exclusive with 'after')
after=<mkey>   (mutually exclusive with 'before')
```

**Examples:**
```http
# Move policy 5 before policy 3
PUT /api/v2/cmdb/firewall/policy/5?action=move&before=3

# Move policy 5 after policy 7
PUT /api/v2/cmdb/firewall/policy/5?action=move&after=7

# Move to top (before first policy)
PUT /api/v2/cmdb/firewall/policy/5?action=move&before=1

# Move to bottom (after last policy)
PUT /api/v2/cmdb/firewall/policy/5?action=move&after=100
```

**Behavior:**
- Reorders sequence-based resources
- Changes the order in which policies/rules are evaluated
- Critical for firewall policies (evaluation order matters!)

**Applicable To:**
- `firewall/policy` (most common)
- `firewall/policy6` (IPv6 policies)
- Other sequence-based resources

---

## Proposed Implementation

### 1. Add clone() Method

```python
def clone(
    self,
{% if schema.mkey %}
    {{ schema.mkey }}: {{ schema.mkey_type|to_python_type }},
    new_{{ schema.mkey }}: {{ schema.mkey_type|to_python_type }},
{% else %}
    name: str,
    new_name: str,
{% endif %}
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Clone (duplicate) an existing resource.
    
    Creates a new resource by copying all properties from an existing one.
    
    Args:
{% if schema.mkey %}
        {{ schema.mkey }}: Source resource identifier to clone from
        new_{{ schema.mkey }}: New resource identifier for the cloned object
{% else %}
        name: Source resource name to clone from
        new_name: New resource name for the cloned object
{% endif %}
        vdom: Virtual domain name
        raw_json: Return raw JSON response
        **kwargs: Additional query parameters
        
    Returns:
        API response dictionary
        
    Example:
        >>> # Clone address1 to address1_backup
{% if schema.mkey %}
        >>> result = endpoint.clone(
        ...     {{ schema.mkey }}="address1",
        ...     new_{{ schema.mkey }}="address1_backup"
        ... )
{% else %}
        >>> result = endpoint.clone(
        ...     name="address1",
        ...     new_name="address1_backup"
        ... )
{% endif %}
    """
{% if schema.mkey %}
    endpoint = "/{{ schema.api_path }}/" + str({{ schema.mkey }})
{% else %}
    endpoint = f"/{{ schema.api_path }}/{name}"
{% endif %}
    
    # Clone uses POST with action=clone&nkey=new_name
    params = {
        "action": "clone",
{% if schema.mkey %}
        "nkey": str(new_{{ schema.mkey }}),
{% else %}
        "nkey": new_name,
{% endif %}
    }
    params.update(kwargs)
    
    return self._client.post(
        "{{ schema.category }}", endpoint, params=params, vdom=vdom, raw_json=raw_json
    )
```

---

### 2. Add move() Method (for sequence-based resources)

```python
def move(
    self,
{% if schema.mkey %}
    {{ schema.mkey }}: {{ schema.mkey_type|to_python_type }},
{% else %}
    name: str,
{% endif %}
    before: {{ schema.mkey_type|to_python_type }} | None = None,
    after: {{ schema.mkey_type|to_python_type }} | None = None,
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Move (reorder) a resource in the sequence.
    
    Changes the evaluation order by moving this resource before or after another.
    Exactly one of 'before' or 'after' must be specified.
    
    Args:
{% if schema.mkey %}
        {{ schema.mkey }}: Resource identifier to move
{% else %}
        name: Resource name to move
{% endif %}
        before: Move this resource before the specified resource ID
        after: Move this resource after the specified resource ID
        vdom: Virtual domain name
        raw_json: Return raw JSON response
        **kwargs: Additional query parameters
        
    Returns:
        API response dictionary
        
    Raises:
        ValueError: If both or neither 'before' and 'after' are specified
        
    Example:
        >>> # Move policy 5 before policy 3
{% if schema.mkey %}
        >>> result = endpoint.move({{ schema.mkey }}=5, before=3)
{% else %}
        >>> result = endpoint.move(name="policy5", before="policy3")
{% endif %}
        
        >>> # Move policy 5 after policy 7
{% if schema.mkey %}
        >>> result = endpoint.move({{ schema.mkey }}=5, after=7)
{% else %}
        >>> result = endpoint.move(name="policy5", after="policy7")
{% endif %}
    """
    # Validate: exactly one of before/after must be specified
    if before is None and after is None:
        raise ValueError("Either 'before' or 'after' must be specified")
    if before is not None and after is not None:
        raise ValueError("Cannot specify both 'before' and 'after'")
    
{% if schema.mkey %}
    endpoint = "/{{ schema.api_path }}/" + str({{ schema.mkey }})
{% else %}
    endpoint = f"/{{ schema.api_path }}/{name}"
{% endif %}
    
    # Move uses PUT with action=move&before/after=target
    params = {"action": "move"}
    if before is not None:
        params["before"] = str(before)
    else:
        params["after"] = str(after)
    
    params.update(kwargs)
    
    return self._client.put(
        "{{ schema.category }}", endpoint, params=params, vdom=vdom, raw_json=raw_json
    )
```

---

### 3. Add Convenience Methods for move()

```python
def move_to_top(
    self,
{% if schema.mkey %}
    {{ schema.mkey }}: {{ schema.mkey_type|to_python_type }},
{% else %}
    name: str,
{% endif %}
    vdom: str | bool | None = None,
    raw_json: bool = False,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Move resource to the top of the sequence (first position).
    
    This retrieves the current first item and moves this resource before it.
    
    Args:
{% if schema.mkey %}
        {{ schema.mkey }}: Resource identifier to move
{% else %}
        name: Resource name to move
{% endif %}
        vdom: Virtual domain name
        raw_json: Return raw JSON response
        
    Returns:
        API response dictionary
        
    Example:
        >>> # Move policy to top (evaluated first)
{% if schema.mkey %}
        >>> result = endpoint.move_to_top({{ schema.mkey }}=5)
{% else %}
        >>> result = endpoint.move_to_top(name="policy5")
{% endif %}
    """
    # Get all items to find first one
    items_response = self.get(vdom=vdom, raw_json=True)
    
    if isinstance(items_response, dict):
        items = items_response.get("results", [])
        if not items:
            raise ValueError("No items found in sequence")
        
{% if schema.mkey %}
        first_mkey = items[0].get("{{ schema.mkey }}")
        return self.move({{ schema.mkey }}={{ schema.mkey }}, before=first_mkey, vdom=vdom, raw_json=raw_json)
{% else %}
        first_name = items[0].get("name")
        return self.move(name=name, before=first_name, vdom=vdom, raw_json=raw_json)
{% endif %}
    else:
        # Async version
        async def _move_top():
            response = await items_response
            items = response.get("results", [])
            if not items:
                raise ValueError("No items found in sequence")
            
{% if schema.mkey %}
            first_mkey = items[0].get("{{ schema.mkey }}")
            return await self.move({{ schema.mkey }}={{ schema.mkey }}, before=first_mkey, vdom=vdom, raw_json=raw_json)
{% else %}
            first_name = items[0].get("name")
            return await self.move(name=name, before=first_name, vdom=vdom, raw_json=raw_json)
{% endif %}
        
        return _move_top()


def move_to_bottom(
    self,
{% if schema.mkey %}
    {{ schema.mkey }}: {{ schema.mkey_type|to_python_type }},
{% else %}
    name: str,
{% endif %}
    vdom: str | bool | None = None,
    raw_json: bool = False,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Move resource to the bottom of the sequence (last position).
    
    This retrieves the current last item and moves this resource after it.
    
    Args:
{% if schema.mkey %}
        {{ schema.mkey }}: Resource identifier to move
{% else %}
        name: Resource name to move
{% endif %}
        vdom: Virtual domain name
        raw_json: Return raw JSON response
        
    Returns:
        API response dictionary
        
    Example:
        >>> # Move policy to bottom (evaluated last)
{% if schema.mkey %}
        >>> result = endpoint.move_to_bottom({{ schema.mkey }}=5)
{% else %}
        >>> result = endpoint.move_to_bottom(name="policy5")
{% endif %}
    """
    # Get all items to find last one
    items_response = self.get(vdom=vdom, raw_json=True)
    
    if isinstance(items_response, dict):
        items = items_response.get("results", [])
        if not items:
            raise ValueError("No items found in sequence")
        
{% if schema.mkey %}
        last_mkey = items[-1].get("{{ schema.mkey }}")
        return self.move({{ schema.mkey }}={{ schema.mkey }}, after=last_mkey, vdom=vdom, raw_json=raw_json)
{% else %}
        last_name = items[-1].get("name")
        return self.move(name=name, after=last_name, vdom=vdom, raw_json=raw_json)
{% endif %}
    else:
        # Async version
        async def _move_bottom():
            response = await items_response
            items = response.get("results", [])
            if not items:
                raise ValueError("No items found in sequence")
            
{% if schema.mkey %}
            last_mkey = items[-1].get("{{ schema.mkey }}")
            return await self.move({{ schema.mkey }}={{ schema.mkey }}, after=last_mkey, vdom=vdom, raw_json=raw_json)
{% else %}
            last_name = items[-1].get("name")
            return await self.move(name=name, after=last_name, vdom=vdom, raw_json=raw_json)
{% endif %}
        
        return _move_bottom()
```

---

## Schema Detection

### Challenge
The schema JSON files don't explicitly list which endpoints support which actions.

### Solution Options

#### Option 1: Hardcode Known Endpoints
```python
# In schema_parser.py or endpoint_generator.py
ENDPOINTS_WITH_CLONE = {
    "firewall/address",
    "firewall/address6",
    "firewall/addrgrp",
    "firewall/policy",
    "firewall/service/custom",
    # ... add more as discovered
}

ENDPOINTS_WITH_MOVE = {
    "firewall/policy",
    "firewall/policy6",
    "firewall/policy64",
    "firewall/policy46",
    # ... sequence-based only
}
```

#### Option 2: Convention-Based
```python
# Assume all CMDB endpoints support clone
supports_clone = schema.category == "cmdb"

# Only endpoints with "policy" in path support move
supports_move = "policy" in schema.path
```

#### Option 3: Configuration File
```yaml
# action_support.yaml
clone_support:
  - firewall/address
  - firewall/policy
  - firewall/service/custom
  
move_support:
  - firewall/policy
  - firewall/policy6
```

#### **Recommended: Option 1 + Option 2 Hybrid**
- Start with explicit list for known endpoints
- Add convention-based fallback
- Easy to extend as we discover more

---

## Implementation Steps

### Phase 1: Basic Implementation ✅ Ready

1. **Update EndpointSchema** - Add flags
   ```python
   @dataclass
   class EndpointSchema:
       # ... existing fields ...
       supports_clone: bool = False
       supports_move: bool = False
   ```

2. **Update SchemaParser** - Detect support
   ```python
   def parse(cls, schema_json: dict, source_file: str) -> EndpointSchema:
       # ... existing parsing ...
       
       # Detect action support
       path = schema.path
       supports_clone = path in ENDPOINTS_WITH_CLONE or category == "cmdb"
       supports_move = path in ENDPOINTS_WITH_MOVE
   ```

3. **Update Template** - Conditional generation
   ```jinja
   {% if schema.supports_clone %}
   {{ clone_method_code }}
   {% endif %}
   
   {% if schema.supports_move %}
   {{ move_method_code }}
   {{ move_to_top_method_code }}
   {{ move_to_bottom_method_code }}
   {% endif %}
   ```

### Phase 2: Testing

1. **Test clone()**
   ```python
   # Test with firewall/address
   result = fgt.api.cmdb.firewall.address.clone(
       name="test_address",
       new_name="test_address_clone"
   )
   ```

2. **Test move()**
   ```python
   # Test with firewall/policy
   result = fgt.api.cmdb.firewall.policy.move(
       policyid=5,
       before=3
   )
   ```

3. **Test convenience methods**
   ```python
   result = fgt.api.cmdb.firewall.policy.move_to_top(policyid=5)
   result = fgt.api.cmdb.firewall.policy.move_to_bottom(policyid=5)
   ```

### Phase 3: Documentation

1. Update method docstrings
2. Add examples to QUICKREF.md
3. Document action support in EDGE_CASES.md

---

## Benefits

### Developer Experience
✅ **Intuitive API:**
```python
# Instead of:
result = fgt.api.cmdb.firewall.address.post(
    endpoint="/firewall/address/addr1?action=clone&nkey=addr1_clone"
)

# Developers can use:
result = fgt.api.cmdb.firewall.address.clone(
    name="addr1",
    new_name="addr1_clone"
)
```

✅ **Type Safety:**
- Parameters are typed
- IDE autocomplete works
- Validation at method call

✅ **Clear Intent:**
- `clone()` is self-documenting
- `move_to_top()` is obvious
- Less error-prone than manual query params

### Practical Use Cases

**Backup/Restore:**
```python
# Clone policy before modifying
backup = fgt.api.cmdb.firewall.policy.clone(
    policyid=10,
    new_policyid=999  # backup ID
)

# Modify original
fgt.api.cmdb.firewall.policy.put(policyid=10, status="disable")

# Restore if needed
fgt.api.cmdb.firewall.policy.delete(policyid=10)
fgt.api.cmdb.firewall.policy.clone(policyid=999, new_policyid=10)
```

**Policy Reordering:**
```python
# Critical policy should be evaluated first
fgt.api.cmdb.firewall.policy.move_to_top(policyid=critical_policy_id)

# Default deny rule should be last
fgt.api.cmdb.firewall.policy.move_to_bottom(policyid=deny_all_policy_id)
```

---

## Known Endpoints with Actions

### Confirmed (from your description)

**Supports Clone:**
- ✅ `firewall/policy` - Confirmed
- ✅ `firewall/service/custom` - Confirmed

**Supports Move:**
- ✅ `firewall/policy` - Confirmed (critical for policy ordering)

### Likely Candidates (to verify)

**Supports Clone:**
- `firewall/address`
- `firewall/address6`
- `firewall/addrgrp`
- `firewall/addrgrp6`
- `firewall/service/group`
- `user/local`
- Most CMDB configuration objects

**Supports Move:**
- `firewall/policy6`
- `firewall/policy64`
- `firewall/policy46`
- Any sequence-based policy/rule

---

## Next Steps

1. **Verify Action Support**
   - Check FortiOS documentation
   - Test with live FortiGate API
   - Build comprehensive list

2. **Update Generator**
   - Add support flags to EndpointSchema
   - Update parser to detect support
   - Add methods to template (conditional)

3. **Test Implementation**
   - Generate test endpoint (firewall/policy)
   - Test clone() with real API
   - Test move() with real API

4. **Document**
   - Add to QUICKREF
   - Add examples to docs
   - Update CHANGELOG

---

## Questions to Resolve

1. **Which endpoints support clone?**
   - Need comprehensive list
   - Or use convention (all CMDB?)

2. **Which endpoints support move?**
   - Only sequence-based?
   - How to detect programmatically?

3. **Error handling?**
   - What if action not supported?
   - How to communicate to user?

4. **Async support?**
   - Both sync and async versions needed
   - Current pattern works but complex

---

**Status:** Ready for implementation  
**Priority:** High (improves developer experience significantly)  
**Effort:** Medium (2-3 hours for basic implementation)

