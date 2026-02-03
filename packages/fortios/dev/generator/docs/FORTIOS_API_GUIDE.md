# FortiOS API Guide

**Comprehensive reference for FortiOS REST API capabilities**

This document consolidates FortiOS API documentation including filtering, sorting, pagination, response structure, and advanced features.

---

## 📋 Table of Contents

1. [Response Structure](#-response-structure)
2. [Filtering](#-filtering)
3. [Sorting](#-sorting)
4. [Pagination](#-pagination)
5. [Format Parameter](#-format-parameter)
6. [Advanced Features](#-advanced-features)

---

## 📦 Response Structure

All FortiOS API responses follow a consistent structure with metadata and results.

### Standard Response Example

```json
{
    "http_method": "GET",
    "http_status": 200,
    "status": "success",
    "size": 17,
    "matched_count": 17,
    "revision": "bd002ee1735120907182831e7528dc8b",
    "results": [
        {
            "name": "test-address",
            "q_origin_key": "test-address",
            "uuid": "********-****-****-****-************",
            "type": "ipmask",
            "subnet": "10.0.0.0/24"
        }
    ],
    "vdom": "root",
    "path": "firewall",
    "name": "address",
    "serial": "FG5H1E5818906668",
    "version": "v7.6.5",
    "build": 2296
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `http_method` | string | HTTP method (GET, POST, PUT, DELETE) |
| `http_status` | int | HTTP status code (200, 404, 500, etc.) |
| `status` | string | "success" or "error" |
| `results` | array/object | Actual data returned |
| `size` | int | Total objects in database |
| `matched_count` | int | Objects matching filter |
| `revision` | string | Configuration revision hash |
| `vdom` | string | VDOM queried |
| `serial` | string | FortiGate serial number |
| `version` | string | FortiOS version |

### GET Single Object Response

```python
# Request by mkey returns single object
result = fgt.api.cmdb.firewall.address.get(name="test")
# Returns: {"name": "test", "subnet": "10.0.0.0/24", ...}
```

### Mutation Response (POST/PUT/DELETE)

```json
{
    "http_method": "POST",
    "http_status": 200,
    "status": "success",
    "mkey": "new-address",
    "revision_changed": true
}
```

---

## 🔍 Filtering

Filter results using the `filter` parameter:

```
filter=[key][operator][pattern]
```

### Filter Operators

| Operator | Case Sensitive | Description |
|----------|----------------|-------------|
| `==` | Yes | Exact match |
| `=*` | No | Exact match (case insensitive) |
| `!=` | Yes | Not equal |
| `!*` | No | Not equal (case insensitive) |
| `=@` | No | Contains substring |
| `!@` | No | Does not contain |
| `<=` | n/a | Less than or equal |
| `<` | n/a | Less than |
| `>=` | n/a | Greater than or equal |
| `>` | n/a | Greater than |

### Filter Examples

**Single filter:**
```python
# Policies with schedule "always"
fgt.api.cmdb.firewall.policy.get(filter=["schedule==always"])
```

**Multiple filters (AND logic):**
```python
# Policies with schedule "always" AND action "accept"
fgt.api.cmdb.firewall.policy.get(
    filter=["schedule==always", "action==accept"]
)
```

**OR logic (comma within string):**
```python
# Policies with schedule "always" OR "once"
fgt.api.cmdb.firewall.policy.get(
    filter=["schedule==always,schedule==once"]
)
```

**Combined AND/OR:**
```python
# Schedule "always" AND (action "accept" OR "deny")
fgt.api.cmdb.firewall.policy.get(
    filter=["schedule==always", "action==accept,action==deny"]
)
```

### Escaped Characters

| Character | Escaped Value |
|-----------|---------------|
| `.` | `\.` |
| `\` | `\\` |

### CMDB vs Monitor Filtering

- **CMDB API**: Deep search - automatically searches nested objects
- **Monitor API**: Use `parent.child.value` syntax for nested fields

```python
# Monitor API nested filter
fgt.api.monitor.system.available_certificates.get(
    filter=["issuer.CN=@Fortinet"]
)
```

---

## ↕️ Sorting

Sort results using the `sort` parameter:

```
sort=[key]
sort=[key],[order]
```

**Order values:**
- `asc` - Ascending (default)
- `dsc` - Descending

### Sort Examples

```python
# Sort by name ascending
fgt.api.cmdb.firewall.address.get(
    payload_dict={"sort": "name"}
)

# Sort by policyid descending
fgt.api.cmdb.firewall.policy.get(
    payload_dict={"sort": "policyid,dsc"}
)
```

---

## 📄 Pagination

Limit results using `start` and `count` parameters:

```python
# First 100 results
fgt.api.cmdb.firewall.policy.get(count=100)

# Skip 100, get next 100 (page 2)
fgt.api.cmdb.firewall.policy.get(start=100, count=100)

# Combined with filter
fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable"],
    start=0,
    count=50
)
```

### Pagination Helper

```python
def get_all_paginated(endpoint, page_size=100, **kwargs):
    """Fetch all results with pagination."""
    results = []
    start = 0
    while True:
        page = endpoint.get(start=start, count=page_size, **kwargs)
        if not page:
            break
        results.extend(page if isinstance(page, list) else [page])
        if len(page) < page_size:
            break
        start += page_size
    return results

# Get all enabled policies
all_enabled = get_all_paginated(
    fgt.api.cmdb.firewall.policy,
    filter=["status==enable"]
)
```

---

## 📋 Format Parameter

Return only specific fields using `format` parameter:

```python
# Return only name and subnet fields
fgt.api.cmdb.firewall.address.get(
    payload_dict={"format": ["name", "subnet"]}
)
```

### Additional Options

```python
payload_dict = {
    "datasource": True,              # Include datasource info
    "with_meta": True,               # Include metadata
    "with_contents_hash": True,      # Include checksums
    "format": ["policyid", "name"],  # Property filter
    "scope": "global",               # global/vdom/both
    "exclude-default-values": True,  # Omit defaults
}
```

---

## 🚀 Advanced Features

### File Upload/Download

**Upload configuration (Base64):**
```python
import base64

with open("config.conf", "r") as f:
    file_content = base64.b64encode(f.read().encode()).decode()

response = fgt._client.post(
    "monitor",
    "/system/config/restore",
    params={"vdom": "root"},
    data={
        "source": "upload",
        "scope": "global",
        "file_content": file_content
    }
)
```

**Download file:**
```python
response = fgt._client.get(
    "monitor",
    "/system/debug/download",
    raw_json=True
)

# Check if file download
if 'attachment' in response.headers.get('Content-Disposition', ''):
    with open('debug_report.tar.gz', 'wb') as f:
        f.write(response.content)
```

### Batch Transactions

FortiOS supports atomic batch operations:

```python
# Start transaction
fgt._client.post("cmdb", "/system/config?action=batch-start")

try:
    # Multiple operations
    fgt.api.cmdb.firewall.address.post(name="addr1", subnet="10.0.0.0/24")
    fgt.api.cmdb.firewall.address.post(name="addr2", subnet="10.0.1.0/24")
    
    # Commit transaction
    fgt._client.post("cmdb", "/system/config?action=batch-commit")
except Exception:
    # Rollback on error
    fgt._client.post("cmdb", "/system/config?action=batch-abort")
```

### VDOM Support

```python
# Specify VDOM in client
fgt = FortiOS(host="...", token="...", vdom="vdom1")

# Or per-request
fgt.api.cmdb.firewall.policy.get(vdom="vdom1")

# Global scope (all VDOMs)
fgt.api.cmdb.system.global_.get(vdom="global")
```

### Schema Introspection

Get field definitions at runtime:

```python
# Get schema for any CMDB endpoint
schema = fgt.api.cmdb.firewall.policy.get_schema()

# Returns field definitions, types, defaults, enums
print(schema["results"]["name"])  # Field metadata
```

### Special Actions

**Clone an object:**
```python
# Clone address "addr1" to "addr1_copy"
fgt.api.cmdb.firewall.address.clone(
    name="addr1",
    new_name="addr1_copy"
)
```

**Move policy in sequence:**
```python
# Move policy 100 before policy 50
fgt.api.cmdb.firewall.policy.move(
    policyid=100,
    action="before",
    reference_policyid=50
)
```

**Check existence:**
```python
# Returns True/False
exists = fgt.api.cmdb.firewall.address.exists(name="test")
```

---

## 🔗 Related Documentation

- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Generator commands and common patterns
- [EDGE_CASES.md](EDGE_CASES.md) - Known edge cases
- [GENERATOR_DESIGN.md](GENERATOR_DESIGN.md) - Architecture details
