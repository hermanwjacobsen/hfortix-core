# Enhanced Query Parameters & Schema Introspection

**Implementation Date:** January 7, 2026  
**Status:** ✅ Complete (100% coverage)  
**Endpoints Affected:** 561 CMDB endpoints

## Overview

This document describes two major enhancements to the FortiOS API client:

1. **Feature #25**: Runtime schema introspection via `get_schema()` method
2. **Feature #26**: Improved query parameter handling with explicit `filter`, `count`, and `start` parameters

Both features improve developer experience while maintaining full backward compatibility.

---

## Feature #25: Runtime Schema Introspection

### Summary

Added a `get_schema()` method to all CMDB endpoints that support the `schema_introspection` capability. This method queries the live FortiGate firewall for the current endpoint schema definition.

### Implementation

#### Method Signature

```python
def get_schema(
    self,
    vdom: str | None = None,
    format: str = "schema",
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Get schema/metadata for this endpoint.
    
    Returns the FortiOS schema definition including available fields,
    their types, required vs optional properties, enum values, nested
    structures, and default values.
    """
```

#### Usage Examples

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-token")

# Get FortiOS native schema
schema = fgt.api.cmdb.firewall.policy.get_schema()
print(schema["results"])

# Schema contains:
# - Field names and types
# - Required vs optional fields
# - Enum values for choice fields
# - Validation constraints (min, max, length)
# - Default values
# - Nested object structures

# Get JSON Schema format (if supported)
json_schema = fgt.api.cmdb.firewall.policy.get_schema(format="json-schema")
```

### Use Cases

1. **Dynamic Form Generation**: Build UI forms from live schema
2. **Runtime Validation**: Validate payloads before sending to API
3. **API Exploration**: Discover available fields and their constraints
4. **Version Compatibility**: Detect schema differences across FortiOS versions
5. **Auto-documentation**: Generate field documentation from schema

### Technical Details

- **Capability Check**: Only added to endpoints with `capabilities.features.schema_introspection: true`
- **Implementation**: Internally calls `self.get(action=format, vdom=vdom)`
- **Schema Formats**:
  - `"schema"`: FortiOS native format (default, widely supported)
  - `"json-schema"`: JSON Schema standard format (if supported by endpoint)
- **Coverage**: 561/561 CMDB endpoints (100%)

---

## Feature #26: Improved Query Parameter Handling

### Summary

Added three explicit query parameters to the `get()` method:
- `filter`: For filtering results with operators
- `count`: For pagination (max results)
- `start`: For pagination (offset)

The advanced `payload_dict` parameter remains available for other options.

### Implementation

#### Updated Method Signature

```python
def get(
    self,
    policyid: int | None = None,  # or name, depending on endpoint
    filter: list[str] | None = None,  # NEW
    count: int | None = None,         # NEW
    start: int | None = None,         # NEW
    payload_dict: dict[str, Any] | None = None,  # Still available
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
```

### Filter Parameter

#### Filter Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Case insensitive match | `"name==test"` |
| `!=` | Does not match | `"status!=disable"` |
| `=@` | Pattern found in value (contains) | `"comment=@production"` |
| `!@` | Pattern not found | `"name!@temp"` |
| `<=` | Less than or equal | `"policyid<=100"` |
| `<` | Less than | `"sessions<1000"` |
| `>=` | Greater than or equal | `"policyid>=1"` |
| `>` | Greater than | `"sessions>5000"` |

#### Filter Logic

- **AND Logic**: Multiple filters in the list are combined with AND
  ```python
  filter=["status==enable", "action==accept"]
  # Returns: status is enable AND action is accept
  ```

- **OR Logic**: Use comma within a single string
  ```python
  filter=["name==test,name==prod"]
  # Returns: name is test OR name is prod
  ```

- **Combined AND/OR**: Mix both approaches
  ```python
  filter=["status==enable", "name==web,name==mail"]
  # Returns: status is enable AND (name is web OR name is mail)
  ```

#### Filter Examples

```python
# Simple filter
policies = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"]
)

# Multiple conditions (AND)
addresses = fgt.api.cmdb.firewall.address.get(
    filter=["type==ipmask", "subnet=@192.168"]
)

# Pattern matching
rules = fgt.api.cmdb.firewall.policy.get(
    filter=["name=@prod", "comment!@temp"]
)

# Numeric comparisons
high_priority = fgt.api.cmdb.firewall.policy.get(
    filter=["policyid>=1000", "policyid<=2000"]
)
```

### Pagination Parameters

#### count Parameter

Maximum number of entries to return.

```python
# Get first 100 policies
policies = fgt.api.cmdb.firewall.policy.get(count=100)

# Limit to 50 addresses
addresses = fgt.api.cmdb.firewall.address.get(count=50)
```

#### start Parameter

Starting entry index (0-based offset).

```python
# Skip first 100, get next batch
policies = fgt.api.cmdb.firewall.policy.get(start=100, count=100)

# Page 3 (showing 50 per page)
page_3 = fgt.api.cmdb.firewall.address.get(start=100, count=50)
```

#### Pagination Examples

```python
# Simple pagination - first page
page1 = fgt.api.cmdb.firewall.policy.get(start=0, count=100)

# Second page
page2 = fgt.api.cmdb.firewall.policy.get(start=100, count=100)

# Iterate through all results
def get_all_policies(fgt):
    """Get all policies using pagination."""
    policies = []
    start = 0
    page_size = 100
    
    while True:
        page = fgt.api.cmdb.firewall.policy.get(
            start=start,
            count=page_size
        )
        
        if not page.get('results'):
            break
            
        policies.extend(page['results'])
        
        # Check if we got fewer than requested (last page)
        if len(page['results']) < page_size:
            break
            
        start += page_size
    
    return policies
```

### Combined Usage

```python
# Filter + Pagination
enabled_policies = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable", "action==accept"],
    start=0,
    count=100
)

# Filter + Pagination + Advanced options
detailed_results = fgt.api.cmdb.firewall.address.get(
    filter=["type==ipmask"],
    start=0,
    count=50,
    payload_dict={
        "with_meta": True,
        "datasource": True,
        "scope": "vdom"
    }
)
```

### Advanced Options (payload_dict)

The `payload_dict` parameter still supports all advanced FortiOS query options:

```python
# Available options (not exhaustive):
payload_dict = {
    "datasource": True,              # Include datasource information
    "with_meta": True,               # Include metadata about objects
    "with_contents_hash": True,      # Include checksum of contents
    "format": ["policyid", "name"],  # Property filter (specific fields)
    "scope": "global",               # Query scope (global/vdom/both)
    "skip": True,                    # Enable CLI skip operator
    "exclude-default-values": True,  # Exclude default values
    "unfiltered_count": 1000,        # Max unfiltered iterations
}
```

---

## Type Hints & IDE Support

### Python Files (.py)

All endpoint files have explicit parameter type hints:

```python
def get(
    self,
    policyid: int | None = None,
    filter: list[str] | None = None,
    count: int | None = None,
    start: int | None = None,
    payload_dict: dict[str, Any] | None = None,
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
```

### Stub Files (.pyi)

All `.pyi` files include complete type hints with overloads:

```python
@overload
def get(
    self,
    policyid: int | None = ...,
    filter: list[str] | None = ...,
    count: int | None = ...,
    start: int | None = ...,
    payload_dict: dict[str, Any] | None = ...,
    vdom: str | bool | None = ...,
    raw_json: bool = ...,
    **kwargs: Any,
) -> dict[str, Any]: ...

def get_schema(
    self,
    vdom: str | None = ...,
    format: str = ...,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
```

This provides:
- ✅ Full IDE autocomplete
- ✅ Type checking with mypy/pyright
- ✅ IntelliSense documentation
- ✅ Parameter hints

---

## Documentation Improvements

### Enhanced Docstrings

All `get()` methods now include:

1. **Parameter Documentation**: Detailed explanation of each parameter
2. **Filter Operators Table**: Complete reference for all operators
3. **Usage Examples**: Multiple real-world examples
4. **See Also Section**: Cross-references to related methods

Example docstring excerpt:

```
Args:
    filter: List of filter expressions to limit results.
        Each filter uses format: "field==value" or "field!=value"
        Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
        Multiple filters use AND logic. For OR, use comma in single string.
        Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
    count: Maximum number of entries to return (pagination).
    start: Starting entry index for pagination (0-based).
    payload_dict: Additional query parameters for advanced options:
        - datasource (bool): Include datasource information
        - with_meta (bool): Include metadata about each object
        - with_contents_hash (bool): Include checksum of object contents
        - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
        - scope (str): Query scope - "global", "vdom", or "both"
        - action (str): Special actions - "schema", "default"
        See FortiOS REST API documentation for complete list.
```

---

## Generator Changes

### Files Modified

1. **`schema_parser.py`**
   - Added `query_params` field to `EndpointSchema` dataclass
   - Parses query parameter metadata from schema JSON
   - Supports both v1.7.0 and legacy schema formats

2. **`endpoint_class.py.j2`** (Python template)
   - Added filter, count, start parameters to `get()` signature
   - Added parameter assignment logic
   - Added conditional `get_schema()` method
   - Enhanced docstrings with examples

3. **`endpoint_class.pyi.j2`** (Stub template)
   - Updated all overloads with new parameters
   - Changed filter type from `str` to `list[str]`
   - Added `get_schema()` method stub

### Template Logic

The `get_schema()` method is conditionally generated:

```jinja
{% if schema.capabilities.features and schema.capabilities.features.schema_introspection %}
    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """..."""
        return self.get(action=format, vdom=vdom)
{% endif %}
```

---

## Statistics

### Coverage

- **Total CMDB Endpoints**: 561
- **Endpoints with new parameters**: 561 (100%)
- **Endpoints with get_schema()**: 561 (100%)
- **Stub files updated**: 561 (100%)

### Verification

All endpoints verified to have:
- ✅ `filter: list[str] | None = None` parameter
- ✅ `count: int | None = None` parameter
- ✅ `start: int | None = None` parameter
- ✅ `def get_schema()` method
- ✅ Complete type hints in `.pyi` stubs
- ✅ Enhanced documentation

---

## Backward Compatibility

### Full Compatibility Maintained

All existing code continues to work without changes:

```python
# Old code still works
result = fgt.api.cmdb.firewall.policy.get()
result = fgt.api.cmdb.firewall.policy.get(policyid=1)
result = fgt.api.cmdb.firewall.policy.get(
    payload_dict={"filter": ["name==test"]}
)

# New code uses explicit parameters
result = fgt.api.cmdb.firewall.policy.get(
    filter=["name==test"]
)
```

### Migration Path

No migration required! The new parameters are additive:

- ✅ Old `payload_dict={"filter": [...]}` still works
- ✅ New `filter=[...]` parameter is preferred
- ✅ Both can be used together (merged)
- ✅ No breaking changes

---

## Best Practices

### When to Use Each Approach

**Use explicit parameters for:**
- Common operations (filtering, pagination)
- Code readability
- Type safety and IDE support
- New code

**Use payload_dict for:**
- Advanced/rare options
- Multiple advanced options at once
- Options not exposed as parameters
- Temporary/experimental features

### Recommended Patterns

```python
# ✅ Good: Use explicit parameters for common cases
policies = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"],
    count=100
)

# ✅ Good: Use payload_dict for advanced options
policies = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"],
    payload_dict={"with_meta": True, "datasource": True}
)

# ⚠️ Acceptable but verbose: Both ways together
policies = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"],
    payload_dict={"filter": ["action==accept"]}  # Merged
)

# ❌ Avoid: Using payload_dict for common options in new code
policies = fgt.api.cmdb.firewall.policy.get(
    payload_dict={"filter": ["status==enable"], "count": 100}
)
```

---

## References

- **FortiOS REST API Documentation**: Filter syntax and query parameters
- **Schema Version**: 1.7.0+
- **Generator Version**: Updated January 7, 2026
- **Related Features**: Endpoint relationship documentation, FortiObject model

---

## Future Enhancements

Potential future improvements:

1. **QueryBuilder Helper Class**: Fluent API for building complex queries
2. **Filter Validation**: Runtime validation of filter expressions
3. **Smart Pagination Iterator**: Auto-paginate through all results
4. **Schema Cache**: Cache schemas to reduce API calls
5. **More Explicit Parameters**: Add common options like `scope`, `with_meta`

---

**Status**: ✅ Implementation Complete  
**Testing**: All endpoints verified  
**Documentation**: Complete  
**Ready for**: Production use
