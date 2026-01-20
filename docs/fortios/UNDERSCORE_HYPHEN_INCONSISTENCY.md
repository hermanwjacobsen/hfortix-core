# FortiOS API Field Name Inconsistency: Underscores vs Hyphens

## The Problem

The FortiOS API is **inconsistent** in how it handles field names with multiple words:

- **Most fields**: Use kebab-case (hyphens), e.g., `ems-id`, `source-ip`, `https-port`
- **Some fields**: Use snake_case (underscores), e.g., `id_list`, `file_content`, `ems_id`

This is **not a bug in HFortix** - it's how Fortinet's API is designed. The same logical parameter can exist in different formats depending on the API endpoint type:

### Example: `ems_id` vs `ems-id`

```python
# CMDB endpoint (uses hyphen)
fgt.api.cmdb.endpoint_control.fctems.put(
    ems_id=1  # Python parameter → API expects "ems-id"
)

# Monitor endpoint (uses underscore) 
fgt.api.monitor.endpoint_control.ems.status.get(
    ems_id=5  # Python parameter → API expects "ems_id"
)
```

## Why This Happens

Fortinet's API evolved over time:
- **CMDB endpoints** (configuration): Consistently use kebab-case
- **Monitor endpoints** (runtime data): Mix of both formats
- **Log endpoints**: Mostly kebab-case
- **Service endpoints**: Varies

## HFortix Solution

HFortix automatically handles this complexity using **schema-driven field mapping**:

### 1. Auto-Generated Field Lists

During code generation, we scan all 1,800+ schema files to identify fields with underscores:

```python
# From field_overrides.py

MONITOR_BODY_FIELD_NO_HYPHEN = {
    "id_list",          # system/config-script/delete
    "file_content",     # File upload endpoints
    "ems_id",           # EMS status endpoints
    "account_id",       # Account operations
    # ... 196 more fields
}

CMDB_BODY_FIELD_NO_HYPHEN = {
    "block_ack_flood",
    "block_ack_flood_thresh",
    "block_ack_flood_time",
    "switch_dhcp_opt43_key",
}
```

### 2. Intelligent Conversion

The payload builders check these lists before converting:

```python
# build_api_payload() logic:
if param_name in MONITOR_BODY_FIELD_NO_HYPHEN:
    api_key = param_name  # Keep underscore
else:
    api_key = param_name.replace("_", "-")  # Convert to hyphen
```

## For Users

**You don't need to worry about this!** Just use Python-style snake_case for all parameters:

```python
# Works correctly - HFortix handles the conversion
fgt.api.monitor.system.config_script.delete.post(
    id_list=["1", "2", "3"]  # Stays as "id_list" (monitor endpoint)
)

fgt.api.cmdb.firewall.address.post(
    name="test",
    source_ip="192.168.1.1"  # Converts to "source-ip" (CMDB endpoint)
)
```

## Statistics

Based on FortiOS 7.6.5 schema analysis:

| API Type | Total Endpoints | Fields with Underscores | Percentage |
|----------|----------------|------------------------|------------|
| CMDB     | ~800           | 4 body fields          | <1%        |
| Monitor  | ~600           | 200 body fields        | ~10%       |
| Log      | ~100           | 0 body fields          | 0%         |
| Service  | ~50            | 0 body fields          | 0%         |

## Common Fields with Underscores

### Monitor Endpoints
```python
# Delete operations
id_list = ["1", "2", "3"]

# File uploads
file_content = "base64_encoded_data"
key_file_content = "base64_cert_data"

# Filters and queries
filter_logic = "and"
ip_version = 4
timestamp_from = 1234567890
timestamp_to = 1234567999

# Account operations
account_id = "user@example.com"
account_password = "secret"

# Network parameters
ip_address = "192.168.1.1"
mac_address = "00:11:22:33:44:55"
source_port = 8080
destination_port = 443

# And 180+ more...
```

### CMDB Endpoints
```python
# Wireless controller settings (rare!)
block_ack_flood = "enable"
block_ack_flood_thresh = 50
switch_dhcp_opt43_key = "value"
```

## For Developers

If you find a field that's being incorrectly converted:

1. **Verify the API expects underscores**: Check Fortinet's API documentation or test with raw API calls
2. **Update the generator**: If it's a new field not in schemas, update `scan_underscore_fields.py` and regenerate
3. **Report it**: Create an issue so we can update the field lists

## Technical Details

### Schema Detection

We use the schema's `name` field (API's original field name) vs `python_name` to detect mismatches:

```json
{
  "name": "id_list",        // API expects underscore
  "python_name": "id_list", // Python uses underscore
  // → Add to NO_HYPHEN list
}

{
  "name": "source-ip",      // API expects hyphen
  "python_name": "source_ip", // Python uses underscore
  // → Convert underscore to hyphen
}
```

### Conversion Flow

```
Python Code:
    fgt.api.monitor.system.config_script.delete.post(id_list=[...])
         ↓
build_api_payload(id_list=[...]):
    1. Check PYTHON_KEYWORD_TO_API_FIELD (no match)
    2. Check MONITOR_BODY_FIELD_NO_HYPHEN (match!)
    3. Keep as "id_list" (don't convert)
         ↓
HTTP Request Body:
    {"id_list": ["1", "2", "3"]}
         ↓
FortiOS API:
    ✓ Accepts correctly
```

## History

- **v0.5.129** (2026-01-20): Auto-generated comprehensive field lists from schemas
  - Scanned 1,800+ schemas
  - Found 200 monitor fields + 4 CMDB fields with underscores
  - Fixes `id_list` bug in `system/config-script/delete`
  
- **v0.5.128** (2026-01-19): Separated query params vs body fields
  - Different handling for URL parameters vs request body
  
- **v0.5.122** (2026-01-15): Added `file_content` and `key_file_content`
  - Fixed file upload endpoints

## See Also

- [Python Keyword Handling](PYTHON_KEYWORD_HANDLING.md) - Similar issue with Python reserved words
- `packages/fortios/hfortix_fortios/_helpers/field_overrides.py` - Field mapping implementation
- `scripts/scan_underscore_fields.py` - Schema scanner script
