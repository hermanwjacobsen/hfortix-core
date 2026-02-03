# Query Parameters & Schema Quick Reference

## get_schema() Method

```python
# Get endpoint schema from live firewall
schema = fgt.api.cmdb.firewall.policy.get_schema()

# Available on all 561 CMDB endpoints
schema = fgt.api.cmdb.<category>.<endpoint>.get_schema()
```

**Returns**: Field definitions, types, enums, validation rules, defaults

**Use Cases**: Dynamic forms, runtime validation, API exploration

---

## Filter Parameter

```python
# Single filter
get(filter=["name==test"])

# Multiple filters (AND)
get(filter=["status==enable", "action==accept"])

# OR logic (comma in string)
get(filter=["name==web,name==mail"])

# Combined AND/OR
get(filter=["status==enable", "name==web,name==mail"])
```

### Operators

| Op | Meaning | Example |
|----|---------|---------|
| `==` | Equals | `"name==test"` |
| `!=` | Not equals | `"status!=disable"` |
| `=@` | Contains | `"comment=@prod"` |
| `!@` | Not contains | `"name!@temp"` |
| `<=` | Less/equal | `"policyid<=100"` |
| `<` | Less than | `"sessions<1000"` |
| `>=` | Greater/equal | `"policyid>=1"` |
| `>` | Greater than | `"sessions>5000"` |

---

## Pagination Parameters

```python
# First 100 results
get(count=100)

# Skip first 100, get next 100
get(start=100, count=100)

# Page 3 (50 per page)
get(start=100, count=50)
```

---

## Common Patterns

### Filter + Pagination

```python
results = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"],
    start=0,
    count=100
)
```

### Filter + Advanced Options

```python
results = fgt.api.cmdb.firewall.address.get(
    filter=["type==ipmask"],
    payload_dict={"with_meta": True, "datasource": True}
)
```

### Get All Results (Paginated)

```python
def get_all(endpoint, page_size=100):
    results = []
    start = 0
    while True:
        page = endpoint.get(start=start, count=page_size)
        if not page.get('results'):
            break
        results.extend(page['results'])
        if len(page['results']) < page_size:
            break
        start += page_size
    return results

all_policies = get_all(fgt.api.cmdb.firewall.policy)
```

---

## Advanced Options (payload_dict)

```python
payload_dict = {
    "datasource": True,           # Include datasource info
    "with_meta": True,            # Include metadata
    "with_contents_hash": True,   # Include checksums
    "format": ["policyid", "name"], # Property filter
    "scope": "global",            # global/vdom/both
    "exclude-default-values": True,
}
```

---

## Type Hints

```python
from typing import Any

# Parameters
filter: list[str] | None = None
count: int | None = None
start: int | None = None
payload_dict: dict[str, Any] | None = None

# Return
-> dict[str, Any]  # or Coroutine for async
```

---

## Backward Compatibility

```python
# Old way (still works)
get(payload_dict={"filter": ["name==test"], "count": 100})

# New way (preferred)
get(filter=["name==test"], count=100)

# Both work, parameters are merged
```

---

## Examples by Use Case

### Search by Name Pattern

```python
fgt.api.cmdb.firewall.address.get(
    filter=["name=@web"]
)
```

### Get Enabled Policies

```python
fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"]
)
```

### Numeric Range

```python
fgt.api.cmdb.firewall.policy.get(
    filter=["policyid>=1000", "policyid<=2000"]
)
```

### Exclude Items

```python
fgt.api.cmdb.firewall.address.get(
    filter=["name!@temp", "comment!@test"]
)
```

### Complex Filter

```python
fgt.api.cmdb.firewall.policy.get(
    filter=[
        "status==enable",
        "action==accept",
        "srcintf==port1,srcintf==port2"  # port1 OR port2
    ]
    # status is enable AND action is accept AND (srcintf is port1 OR port2)
)
```

---

## Quick Stats

- ✅ 561 CMDB endpoints updated
- ✅ 100% coverage
- ✅ Full type hints in .pyi stubs
- ✅ Backward compatible
- ✅ Production ready
