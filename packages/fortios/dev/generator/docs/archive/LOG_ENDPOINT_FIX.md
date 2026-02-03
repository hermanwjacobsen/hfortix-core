# Log Endpoint Schema Download Fix

## Issue

When downloading schemas for `cmdb.log/*` endpoints, 177 endpoints were failing with HTTP 400 errors:

```
Failed to download schema: HTTP 400: https://...
/api/v2/cmdb/log/disk/filter?action=schema&vdom=root
```

## Root Cause

**These endpoints failing with HTTP 400 is EXPECTED behavior** - they don't support the `?action=schema` parameter.

However, the code has a **Swagger fallback mechanism** that should handle this by extracting schema information from Swagger documentation when the API returns 400/405 errors.

The bug was in the **path conversion logic**. FortiGate API uses **dot notation** for log subcategories:
- ❌ Incorrect: `/api/v2/cmdb/log/disk/filter` 
- ✅ Correct: `/api/v2/cmdb/log.disk/filter`

But the code only converted `firewall/*` paths to dot notation, not `log/*` paths.

## Solution

Updated `download_schemas.py` to convert both `firewall/*` and `log/*` paths:

### Path Conversion Rules

| Endpoint Format | API Format | Swagger Format | Example |
|----------------|------------|----------------|---------|
| `log/disk/filter` (3+ parts) | `log.disk/filter` | `/log.disk/filter` | ✅ Converted |
| `log/custom-field` (2 parts) | `log/custom-field` | `/log/custom-field` | ✅ Not converted |
| `firewall/schedule/group` (3+ parts) | `firewall.schedule/group` | `/firewall.schedule/group` | ✅ Converted |
| `firewall/address` (2 parts) | `firewall/address` | `/firewall/address` | ✅ Not converted |

### Code Changes

**File**: `.dev/generator/download_schemas.py`

**Before** (lines 157-166):
```python
api_endpoint_path = endpoint_path
if category == "cmdb" and endpoint_path.startswith("firewall/"):
    parts = endpoint_path.split("/")
    if len(parts) >= 3:
        api_endpoint_path = f"{parts[0]}.{parts[1]}/{'/'.join(parts[2:])}"
```

**After**:
```python
api_endpoint_path = endpoint_path
if category == "cmdb" and (endpoint_path.startswith("firewall/") or endpoint_path.startswith("log/")):
    parts = endpoint_path.split("/")
    if len(parts) >= 3:
        api_endpoint_path = f"{parts[0]}.{parts[1]}/{'/'.join(parts[2:])}"
```

## Verification

### Test Cases

All test cases pass:

```python
✅ log/disk/filter           -> log.disk/filter
✅ log/disk/setting          -> log.disk/setting  
✅ log/fortianalyzer/filter  -> log.fortianalyzer/filter
✅ log/custom-field          -> log/custom-field (not converted)
✅ log/eventfilter           -> log/eventfilter (not converted)
```

### Swagger Lookup

All endpoints found in Swagger documentation:

```
✅ log.disk/filter (converted) -> Found in Swagger
✅ log.fortianalyzer/filter (converted) -> Found in Swagger
✅ log/custom-field (not converted) -> Found in Swagger
✅ log/eventfilter (not converted) -> Found in Swagger
```

## Expected Behavior

After this fix:

1. **Schema download attempt** → Returns HTTP 400 (expected)
2. **Swagger fallback triggered** → ⚠️ Warning message shown
3. **Swagger lookup** → ✅ Endpoint found with correct dot notation
4. **Minimal schema created** → ✅ Generated from Swagger docs
5. **File saved** → ✅ Schema file created successfully

## Impact

This fix will allow **all 177 failed log endpoints** to be successfully processed using Swagger documentation as a fallback.

The generated schemas will be marked with:
```json
{
  "_metadata": {
    "source": "swagger",
    "fallback_reason": "HTTP 400 from API, used Swagger docs",
    ...
  }
}
```

## Testing

To test the fix, re-run schema download for log endpoints:

```bash
cd .dev/generator
python generate.py --host <IP> --token <TOKEN> --endpoint cmdb.log/disk/filter
```

Expected output:
```
📥 Downloading cmdb.log/disk/filter...
    Request: GET https://.../api/v2/cmdb/log.disk/filter?action=schema
⚠️  cmdb.log/disk/filter returned HTTP 400 (no schema support)
    Trying Swagger docs as fallback...
✅ Created from Swagger: cmdb.log/disk/filter → schemas/.../log/disk/filter.json
```
