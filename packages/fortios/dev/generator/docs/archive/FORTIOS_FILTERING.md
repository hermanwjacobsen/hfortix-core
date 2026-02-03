# FortiOS API - Filtering, Sorting, Paging, and Formatting

**Official FortiOS documentation on query parameters**

This document captures FortiOS capabilities for refining API queries. These features are available in both Configuration (CMDB) and Monitor APIs.

---

## Overview

FortiOS API supports four types of query refinement:

1. **Filtering** - Reduce results based on criteria
2. **Sorting** - Order results by field(s)
3. **Paging** - Limit number of results returned
4. **Formatting** - Return only specific fields

**Version Support:**
- Configuration API: All features available since early versions
- Monitor API: Filtering, paging, formatting added in **FortiOS 6.4.2**
- Sorting added to both Configuration and Monitor in **FortiOS 6.4.2**

**Key Difference:**
- **Configuration API**: Deep search for filter keywords (searches nested objects automatically)
- **Monitor API**: Uses `parent.child.value` syntax to specify keywords in nested objects

---

## 1. Filtering

Filter results by including the `filter` parameter in the request URL:

```
filter=[key][operator][pattern]
```

### Filter Operators

| Operator | Case Sensitive | Description |
|----------|----------------|-------------|
| `==` | Yes | Pattern must be identical to the value |
| `=*` | No | Pattern must be identical to the value |
| `!=` | Yes | Pattern does not match the value |
| `!*` | No | Pattern does not match the value |
| `=@` | No | Pattern found within value (contains) |
| `!@` | No | Pattern not found within value |
| `<=` | n/a | Value must be less than or equal to pattern |
| `<` | n/a | Value must be less than pattern |
| `>=` | n/a | Value must be greater than or equal to pattern |
| `>` | n/a | Value must be greater than pattern |

### Simple Filter Examples

**Display firewall policies with schedule "always":**
```
/api/v2/cmdb/firewall/policy?filter=schedule==always
```

**Display available interfaces that do not have name "wan1":**
```
/api/v2/monitor/system/available-interfaces?filter=name!=wan1
```

### Complex Filters (Combining Filters)

| Combination | How to Use | Example |
|-------------|------------|---------|
| **Logical OR** | Separate values with commas `,` (same key, same operator) | `filter=key1op1value1,key1op1value2` |
| **Logical AND** | Separate filters with ampersands `&` | `filter=key1op1value1&filter=key2op2value2` |
| **Combining AND/OR** | AND different sets of OR filters using `&` | `filter=key1op1value1,key1op1value2&filter=key3op3value3` |

### Complex Filter Examples

**Policies using "always" schedule OR "once" schedule:**
```
/api/v2/cmdb/firewall/policy?filter=schedule==always,schedule==once
```

**Policies with schedule "always" AND action "accept":**
```
/api/v2/cmdb/firewall/policy?filter=schedule==always&filter=action==accept
```

**Policies with schedule "always" AND action "accept" or "deny":**
```
/api/v2/cmdb/firewall/policy?filter=schedule==always&filter=action==accept,action==deny
```

**Available certificates with name "@Fortinet" AND issuer.CN "@Fortinet":**
```
/api/v2/monitor/system/available-certificates?filter=name=@Fortinet&filter=issuer.CN=@Fortinet
```

### Escaped Characters

The `.` and `\` characters must be escaped in filter patterns:

| Character | Escaped Value |
|-----------|---------------|
| `.` | `\.` |
| `\` | `\\` |

---

## 2. Sorting

Sort results by including the `sort` parameter:

```
sort=[key]
sort=[key],[order]
```

**Order values:**
- `asc` - Ascending (default)
- `dsc` - Descending

### Sorting Examples

**Sort by name in ascending order:**
```
sort=name
```

**Sort by version in descending order:**
```
sort=version,dsc
```

**Multiple sort keys (priority order):**
```
sort=version,dsc&sort=name,asc
```
Results sorted first by version (descending), then by name (ascending) for entries with same version.

**Available certificates by q_ref (descending), then name (ascending):**
```
/api/v2/monitor/system/available-certificates?sort=q_ref,dsc&sort=name,asc
```

---

## 3. Paging

Limit the number of entries returned using `start` and/or `count` parameters:

```
start=[starting entry index]&count=[Maximum number of entries to return]
```

### Paging Behavior

**Normal behavior:**
- `start` and `count` define the range of results
- Zero-based indexing (start=0 is the first result)

**Edge cases:**
- **Error** when `start > number of entries`
- **Error** when `count > number of entries`
- **All results** returned when:
  - `start + count > number of entries`
  - `start` or `count` is negative
  - `start` and `count` are both 0

### Paging Examples

**Display 50 results starting from the 10th result:**
```
start=10&count=50
```

**Display first 100 results:**
```
start=0&count=100
```

---

## 4. Formatting

Return only specific fields by including the `format` parameter:

```
format=[property1]|[property2]|...
```

### Formatting Examples

**Display only policyid and srcintf fields:**
```
format=policyid|srcintf
```

**Monitor API with nested fields:**
```
format=name|issuer.C|q_ref
```

**Note:** When an invalid field name is specified, all results will be returned.

---

## Combining Parameters

When multiple parameters are used in one query, they are applied in this **fixed order**:

1. **Filtering**
2. **Sorting**
3. **Paging**
4. **Formatting**

**The order in which parameters appear in the request URL does not matter.**

### Complex Query Examples

#### Query 1: Filter and Format
```
/api/v2/monitor/system/available-interfaces?format=name&filter=name=@wan
```

**Processing order:**
1. Filter: Retain only items with "wan" in the name field (case insensitive)
2. Format: Return only the "name" field

#### Query 2: Filter, Sort, Page, and Format
```
/api/v2/cmdb/firewall/address?format=name|type|sub-type&sort=name,dsc&filter=name=@ADDR,type==ipmask&filter=name=@r&start=4&count=3
```

**Processing order:**
1. Filter: Retain items where:
   - Name contains "ADDR" (case insensitive) OR type is exactly "ipmask"
   - AND name contains "r" (case insensitive)
2. Sort: Sort by name in descending order
3. Page: Return 3 items starting at index 4
4. Format: Return only name, type, and sub-type fields

#### Query 3: Filter, Sort, Page, and Format (Monitor API)
```
/api/v2/monitor/firewall/proxy-policy?format=policyid|last_used|hit_count|uuid&sort=uuid,dsc&filter=hit_count<1&start=2&count=3
```

**Processing order:**
1. Filter: Retain items where hit_count > 1
2. Sort: Sort by uuid in descending order
3. Page: Return 3 items starting at index 2
4. Format: Return only policyid, last_used, hit_count, and uuid fields

---

## Important Notes

### Legacy API Behavior (Pre-6.4.2)

For individual APIs that had `start` and `count` parameters **before FortiOS 6.4.2**, the processing order is different:

- **Legacy behavior:** Paging occurs BEFORE filtering and sorting
- **New behavior (6.4.2+):** Paging occurs AFTER filtering and sorting

**Example:**

Base query returns: `9, 8, 7, 6, 5, 4, 3, 2, 1`  
Query parameters: `sort=number,asc&start=3&count=3`

| API | Is paging new in 6.4.2? | Results |
|-----|--------------------------|---------|
| Configuration | Yes | `4, 5, 6` |
| Configuration | No | `6, 7, 8` |
| Monitor | Yes | `4, 5, 6` |
| Monitor | No | `6, 7, 8` |

**Recommendation:** Assume new behavior (6.4.2+) for FortiOS 7.6 target version.

---

## Implementation Implications for Generator

### 1. `.get()` Behavior

**No parameters → Return all results:**
```python
# Get all firewall addresses
all_addresses = fgt.api.cmdb.firewall.address.get()
# Returns: {"results": [...], "http_status": 200, ...}
```

**With mkey parameter → Return specific object:**
```python
# Get specific address by name
address = fgt.api.cmdb.firewall.address.get(name="server1")
# Returns: {"results": {...}, "http_status": 200, ...}
```

### 2. Query Parameters via `**kwargs`

All filtering, sorting, paging, and formatting parameters should be passed via `**kwargs`:

```python
def get(
    self,
    name: str | None = None,  # mkey parameter
    payload_dict: dict[str, Any] | None = None,
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,  # All other query parameters
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Get address configuration.
    
    Args:
        name: Address name (optional for list, required for specific)
        vdom: Virtual domain name
        raw_json: Return full API response or just results
        **kwargs: Additional query parameters:
            filter: Filter results (e.g., 'type==ipmask')
            sort: Sort results (e.g., 'name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries
            format: Fields to return (e.g., 'name|type')
    """
    params = payload_dict.copy() if payload_dict else {}
    
    if name:
        endpoint = f"/firewall/address/{name}"
    else:
        endpoint = "/firewall/address"
    
    params.update(kwargs)  # Add filter, sort, start, count, format, etc.
    
    return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)
```

### 3. Usage Examples in Generated Docstrings

Include comprehensive examples in generated docstrings:

```python
class Address:
    """
    Address endpoint for firewall address objects.
    
    Examples:
        # Get all addresses
        >>> addresses = fgt.api.cmdb.firewall.address.get()
        
        # Get specific address
        >>> address = fgt.api.cmdb.firewall.address.get(name="server1")
        
        # Get addresses with filtering
        >>> ipmask_addrs = fgt.api.cmdb.firewall.address.get(
        ...     filter="type==ipmask"
        ... )
        
        # Get addresses with complex filter
        >>> filtered = fgt.api.cmdb.firewall.address.get(
        ...     filter="type==ipmask&filter=name=@server"
        ... )
        
        # Get addresses with sorting
        >>> sorted_addrs = fgt.api.cmdb.firewall.address.get(
        ...     sort="name,dsc"
        ... )
        
        # Get addresses with paging
        >>> page_addrs = fgt.api.cmdb.firewall.address.get(
        ...     start=10,
        ...     count=50
        ... )
        
        # Get addresses with specific fields only
        >>> minimal_addrs = fgt.api.cmdb.firewall.address.get(
        ...     format="name|type|subnet"
        ... )
        
        # Combine all parameters
        >>> result = fgt.api.cmdb.firewall.address.get(
        ...     filter="type==ipmask",
        ...     sort="name,asc",
        ...     start=0,
        ...     count=100,
        ...     format="name|subnet"
        ... )
    """
```

### 4. Helper Methods (Future Enhancement)

Consider helper methods for common filter patterns:

```python
# Future v0.6.0+ enhancement
def get_filtered(
    self,
    filters: dict[str, Any],
    sort_by: str | None = None,
    limit: int | None = None,
    fields: list[str] | None = None,
    **kwargs: Any
) -> dict[str, Any]:
    """
    Get addresses with Python-friendly filter syntax.
    
    Args:
        filters: Dictionary of field -> value filters
        sort_by: Field to sort by (append ',dsc' for descending)
        limit: Maximum number of results
        fields: List of fields to return
    
    Example:
        >>> addresses = fgt.api.cmdb.firewall.address.get_filtered(
        ...     filters={"type": "ipmask", "name__contains": "server"},
        ...     sort_by="name",
        ...     limit=50,
        ...     fields=["name", "subnet"]
        ... )
    """
    # Build filter string from dict
    filter_parts = []
    for key, value in filters.items():
        if "__contains" in key:
            field = key.replace("__contains", "")
            filter_parts.append(f"{field}=@{value}")
        else:
            filter_parts.append(f"{key}=={value}")
    
    filter_str = "&filter=".join(filter_parts)
    
    kwargs["filter"] = filter_str
    if sort_by:
        kwargs["sort"] = sort_by
    if limit:
        kwargs["count"] = limit
    if fields:
        kwargs["format"] = "|".join(fields)
    
    return self.get(**kwargs)
```

**Note:** Helper methods are **out of scope for v0.5.0** but documented for future consideration.

---

## Summary

### For Generator Implementation (v0.5.0):

1. ✅ `.get()` with no mkey parameter returns ALL results
2. ✅ `.get(mkey=value)` returns SPECIFIC object
3. ✅ All query parameters (filter, sort, start, count, format) via `**kwargs`
4. ✅ Document query parameters in docstrings
5. ✅ Provide usage examples showing filtering, sorting, paging, formatting
6. ✅ No special filter helpers (users use raw FortiOS syntax)

### Processing Order (FortiOS 6.4.2+):

1. Filtering
2. Sorting
3. Paging
4. Formatting

### Future Enhancements (v0.6.0+):

- Python-friendly filter syntax helpers
- Query builder classes
- Filter validation
- Result streaming for large datasets

---

## References

- FortiOS REST API Documentation (6.4.2+)
- GENERATOR_DESIGN.md - API endpoint generator design
- MKEY_COMPLEXITY.md - Primary key handling
