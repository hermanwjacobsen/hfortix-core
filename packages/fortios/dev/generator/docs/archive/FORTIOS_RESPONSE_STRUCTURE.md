# FortiOS API Response Structure

**Understanding FortiOS API response format and metadata fields**

This document describes the structure of FortiOS API responses, which is important for generator implementation.

---

## Standard Response Format

All FortiOS API responses follow a consistent structure with metadata and results.

### Complete Response Example

```json
{
    "http_method": "GET",
    "size": 17,
    "limit_reached": false,
    "matched_count": 17,
    "next_idx": 16,
    "revision": "bd002ee1735120907182831e7528dc8b",
    "results": [
        {
            "name": "EMS_ALL_UNKNOWN_CLIENTS",
            "q_origin_key": "EMS_ALL_UNKNOWN_CLIENTS",
            "uuid": "********-****-****-****-************",
            "type": "dynamic",
            "route-tag": 0,
            "sub-type": "ems-tag",
            ...
        },
        {
            "name": "EMS_ALL_UNMANAGEABLE_CLIENTS",
            "q_origin_key": "EMS_ALL_UNMANAGEABLE_CLIENTS",
            ...
        }
    ],
    "vdom": "root",
    "path": "firewall",
    "name": "address",
    "status": "success",
    "http_status": 200,
    "serial": "FG5H1E5818906668",
    "version": "v7.4.1",
    "build": 2296
}
```

---

## Response Fields

### Metadata Fields

| Field | Type | Description |
|-------|------|-------------|
| `http_method` | string | HTTP method used (GET, POST, PUT, DELETE) |
| `http_status` | int | HTTP status code (200, 404, 500, etc.) |
| `status` | string | Operation status ("success", "error") |
| `revision` | string | Configuration revision hash |
| `revision_changed` | bool | Whether this operation changed configuration |
| `vdom` | string | VDOM queried (e.g., "root") |
| `path` | string | API path category (e.g., "firewall", "system") |
| `name` | string | API endpoint name (e.g., "address", "policy") |
| `serial` | string | FortiGate serial number |
| `version` | string | FortiOS version (e.g., "v7.4.1") |
| `build` | int | FortiOS build number |

### Result Fields (for GET operations)

| Field | Type | Description |
|-------|------|-------------|
| `results` | array/object | Actual data returned (array for list, object for single item) |
| `size` | int | Total number of objects in database |
| `matched_count` | int | Number of objects matching filter |
| `next_idx` | int | Index of next result (for pagination) |
| `limit_reached` | bool | Whether result limit was reached |

### Object-Specific Fields

Each object in `results` includes:

| Field | Type | Description |
|-------|------|-------------|
| `q_origin_key` | string | Original key value (mkey) |
| `uuid` | string | Unique identifier for the object |
| ... | various | Object-specific fields based on schema |

---

## Response Variations

### GET All Objects

**Request:**
```
GET /api/v2/cmdb/firewall/address
```

**Response:**
```json
{
    "http_method": "GET",
    "size": 17,
    "matched_count": 17,
    "results": [ /* array of objects */ ],
    "status": "success",
    "http_status": 200
}
```

**Key points:**
- `results` is an **array**
- `size` shows total count
- `matched_count` shows how many matched (same as size if no filter)

### GET Specific Object

**Request:**
```
GET /api/v2/cmdb/firewall/address/server1
```

**Response:**
```json
{
    "http_method": "GET",
    "results": { /* single object */ },
    "status": "success",
    "http_status": 200
}
```

**Key points:**
- `results` is a **single object** (not array)
- No `size`, `matched_count`, or `next_idx` fields

### GET with Filtering

**Request:**
```
GET /api/v2/cmdb/firewall/address?filter=name=@SSLVPN
```

**Response:**
```json
{
    "http_method": "GET",
    "size": 17,
    "matched_count": 1,
    "next_idx": 5,
    "results": [ /* filtered array */ ],
    "status": "success",
    "http_status": 200
}
```

**Key points:**
- `size` shows total objects in database (17)
- `matched_count` shows filtered results (1)
- `results` contains only matching objects

### GET with Formatting

**Request:**
```
GET /api/v2/cmdb/firewall/address?format=name|comment
```

**Response:**
```json
{
    "http_method": "GET",
    "size": 17,
    "matched_count": 17,
    "results": [
        {
            "name": "EMS_ALL_UNKNOWN_CLIENTS",
            "q_origin_key": "EMS_ALL_UNKNOWN_CLIENTS",
            "comment": ""
        }
    ],
    "status": "success",
    "http_status": 200
}
```

**Key points:**
- `results` objects contain **only requested fields**
- `q_origin_key` always included (mkey reference)

### POST (Create)

**Response:**
```json
{
    "http_method": "POST",
    "mkey": "server1",
    "path": "firewall",
    "name": "address",
    "status": "success",
    "http_status": 200,
    "revision": "c63617e0167c28ac6b3dba21da9ffdac",
    "revision_changed": true
}
```

**Key points:**
- `mkey` contains the created object's key
- `revision_changed` is `true`
- No `results` field

### PUT (Update)

**Response:**
```json
{
    "http_method": "PUT",
    "mkey": "server1",
    "path": "firewall",
    "name": "address",
    "status": "success",
    "http_status": 200,
    "revision": "c63617e0167c28ac6b3dba21da9ffdac",
    "revision_changed": true
}
```

**Key points:**
- Similar to POST
- `mkey` contains updated object's key

### DELETE

**Response:**
```json
{
    "http_method": "DELETE",
    "mkey": "server1",
    "path": "firewall",
    "name": "address",
    "status": "success",
    "http_status": 200,
    "revision": "c63617e0167c28ac6b3dba21da9ffdac",
    "revision_changed": true
}
```

**Key points:**
- `mkey` contains deleted object's key
- No `results` field

### Error Response

**Response:**
```json
{
    "http_method": "POST",
    "revision": "d9f174eeccad1f0bddaa7e92983f6ce7",
    "revision_changed": false,
    "cli_error": "node_check_object fail! for name homeNetwork\n\nvalue parse error before 'homeNetwork'\nCommand fail. Return code -651\n",
    "error": -651,
    "status": "error",
    "http_status": 500,
    "vdom": "root",
    "path": "firewall",
    "name": "policy"
}
```

**Key points:**
- `status` is `"error"`
- `http_status` indicates error type (404, 500, etc.)
- `error` contains numeric error code
- `cli_error` contains detailed error message

---

## Implementation Implications

### For Generator (v0.5.0)

#### 1. Response Type Handling

Generated methods must handle different response structures:

```python
def get(
    self,
    name: str | None = None,
    ...
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Get address configuration.
    
    Returns:
        Response structure depends on parameters:
        
        - No name parameter (list all):
          {
            "results": [...],  # Array of objects
            "size": 17,
            "matched_count": 17,
            "status": "success",
            ...
          }
        
        - With name parameter (get specific):
          {
            "results": {...},  # Single object
            "status": "success",
            ...
          }
    """
```

#### 2. raw_json Parameter

The `raw_json` parameter determines what's returned:

```python
# raw_json=False (default) - Return only results
addresses = fgt.api.cmdb.firewall.address.get()
# Returns: [...] (just the array)

# raw_json=True - Return full response
response = fgt.api.cmdb.firewall.address.get(raw_json=True)
# Returns: {"results": [...], "size": 17, "status": "success", ...}
```

**Already implemented in core:**
```python
# From HTTPClient.get()
if not raw_json:
    return response.get("results", response)
else:
    return response
```

#### 3. Pagination Metadata

For large datasets, use pagination metadata:

```python
response = fgt.api.cmdb.firewall.address.get(
    start=0,
    count=100,
    raw_json=True  # Need metadata
)

total_size = response["size"]
matched = response["matched_count"]
next_index = response.get("next_idx")
limit_reached = response.get("limit_reached", False)

if limit_reached:
    # Fetch next page
    next_response = fgt.api.cmdb.firewall.address.get(
        start=next_index,
        count=100,
        raw_json=True
    )
```

#### 4. Error Handling

Check `status` field and handle errors:

```python
response = fgt.api.cmdb.firewall.address.post(name="test", ...)

if response.get("status") == "error":
    error_code = response.get("error")
    cli_error = response.get("cli_error", "")
    http_status = response.get("http_status")
    
    # Core already raises appropriate exceptions
    # This is just for illustration
```

**Note:** `hfortix_core.HTTPClient` already handles this and raises appropriate exceptions.

#### 5. Revision Tracking

Track configuration changes:

```python
response = fgt.api.cmdb.firewall.address.post(
    name="server1",
    ...,
    raw_json=True
)

if response.get("revision_changed"):
    new_revision = response["revision"]
    # Configuration was modified
```

---

## Documentation in Generated Code

### Example: Generated Docstring

```python
def get(
    self,
    name: str | None = None,
    payload_dict: dict[str, Any] | None = None,
    vdom: str | bool | None = None,
    raw_json: bool = False,
    **kwargs: Any,
) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """
    Get address configuration.
    
    Args:
        name: Address name (optional for list, required for specific)
        vdom: Virtual domain name
        raw_json: If False (default), returns only results.
                  If True, returns full response with metadata.
        **kwargs: Query parameters (filter, sort, start, count, format)
    
    Returns:
        When raw_json=False (default):
            - If name provided: Single address object (dict)
            - If name not provided: List of address objects (list)
        
        When raw_json=True:
            Full API response (dict) with structure:
            {
                "http_method": "GET",
                "results": [...] or {...},
                "size": 17,              # Total objects (list only)
                "matched_count": 17,     # Matching objects (list only)
                "next_idx": 16,          # Next page index (list only)
                "limit_reached": false,  # Pagination flag (list only)
                "status": "success",
                "http_status": 200,
                "vdom": "root",
                "path": "firewall",
                "name": "address",
                "revision": "bd002ee1735120907182831e7528dc8b",
                "serial": "FG5H1E5818906668",
                "version": "v7.4.1",
                "build": 2296
            }
    
    Response Metadata Fields:
        size: Total number of objects in database
        matched_count: Number of objects matching filter
        next_idx: Index for next pagination request
        limit_reached: True if result limit was hit
        revision: Current configuration revision hash
        q_origin_key: Original key value in each result object
    
    Examples:
        # Get all addresses (returns list)
        >>> addresses = fgt.api.cmdb.firewall.address.get()
        >>> print(len(addresses))  # Number of addresses
        
        # Get specific address (returns dict)
        >>> address = fgt.api.cmdb.firewall.address.get(name="server1")
        >>> print(address["type"])  # Access field directly
        
        # Get with metadata
        >>> response = fgt.api.cmdb.firewall.address.get(raw_json=True)
        >>> total = response["size"]
        >>> addresses = response["results"]
        
        # Pagination with metadata
        >>> response = fgt.api.cmdb.firewall.address.get(
        ...     start=0,
        ...     count=100,
        ...     raw_json=True
        ... )
        >>> if response["limit_reached"]:
        ...     next_page = fgt.api.cmdb.firewall.address.get(
        ...         start=response["next_idx"],
        ...         count=100
        ...     )
    """
```

---

## Summary

### Key Response Characteristics

1. **Consistent structure** across all endpoints
2. **Rich metadata** (size, matched_count, next_idx, revision)
3. **Different results format:**
   - List operations → `results` is array
   - Specific object → `results` is object
4. **Always includes:** http_method, status, http_status, vdom, path, name
5. **Error responses:** Include `cli_error` and `error` code

### Generator Responsibilities

1. ✅ **Document response structure** in generated docstrings
2. ✅ **Explain raw_json parameter** clearly
3. ✅ **Show pagination examples** using metadata fields
4. ✅ **Reference core error handling** (already implemented)
5. ❌ **Don't re-implement** response parsing (core handles it)

### Already Implemented in Core

- ✅ Response parsing (`raw_json` parameter)
- ✅ Error detection and exception raising
- ✅ Metadata extraction
- ✅ Results extraction

**Just document it in generated code!**

---

## References

- FortiOS REST API Documentation
- FORTIOS_FILTERING.md - Query parameters
- CORE_FEATURES_REFERENCE.md - Existing core features
- GENERATOR_DESIGN.md - Main architecture
