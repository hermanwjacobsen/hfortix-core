# Literal Type Support for Enum Parameters

**Date:** January 21, 2026  
**Version:** v0.5.131 (unreleased)  
**Status:** ✅ Complete

## Overview

Enhanced the code generator to automatically extract enum values from schema descriptions and generate `Literal` type hints for parameters. This provides IDE autocomplete and type checking for parameters with restricted value sets.

## Problem

Previously, parameters with enum values (like `protocol`, `service`, etc.) were typed as generic `str`, even though the schema contained information about allowed values in the `summary` field:

```python
# Before (v0.5.130 and earlier)
def post(
    protocol: str | None = None,  # ❌ No autocomplete
    service: str | None = None,   # ❌ No autocomplete
)
```

## Solution

### 1. Schema Parser Enhancement

Updated `schema_management/schema_parser.py` to extract allowed values from the `summary` field using the existing `extract_allowed_values()` function:

```python
# Extract allowed values from summary field (for Literal types)
summary = field_data.get("summary", "")
allowed_values = extract_allowed_values(summary)
if allowed_values and not field_meta.options:
    # Set options if extracted from summary and not already set
    field_meta.options = allowed_values
```

The `extract_allowed_values()` function supports patterns like:
- `[https | udp | http]` → `["https", "udp", "http"]`
- `['value1', 'value2']` → `["value1", "value2"]`
- `[value1 | value2*]` → `["value1", "value2"]` (asterisk indicates default)

### 2. Generator Integration

The endpoint generator (`generators/endpoint_generator.py`) already had the `_get_python_type_with_literal()` filter that checks for `options` attribute and generates Literal types. No changes needed - it just works!

### 3. Template Usage

Templates (`templates/endpoint_class.py.j2` and `endpoint_class.pyi.j2`) already use the `get_python_type_with_literal` filter. No changes needed!

## Results

### Generated Code (.py)

```python
def post(
    self,
    protocol: Literal["https", "udp", "http"] | None = None,  # ✅ Autocomplete!
    service: Literal["emailfilter", "webfilter"] | None = None,  # ✅ Autocomplete!
    port: int | None = None,
)
```

### Type Stubs (.pyi)

```python
class TestAvailabilityPayload(TypedDict, total=False):
    """Payload type for TestAvailability operations."""
    protocol: Literal["https", "udp", "http"]
    service: Literal["emailfilter", "webfilter"]
    port: int

def post(
    self,
    payload_dict: TestAvailabilityPayload | None = ...,
    protocol: Literal["https", "udp", "http"] | None = ...,
    service: Literal["emailfilter", "webfilter"] | None = ...,
    port: int | None = ...,
) -> TestAvailabilityObject: ...
```

## IDE Experience

### Before
```python
result = fgt.api.monitor.system.fortiguard.test_availability.post(
    protocol="",  # No autocomplete, must check documentation
    service=""    # No autocomplete, must check documentation
)
```

### After
```python
result = fgt.api.monitor.system.fortiguard.test_availability.post(
    protocol="",  # ✅ IDE shows: "https" | "udp" | "http"
    service=""    # ✅ IDE shows: "emailfilter" | "webfilter"
)
```

### Type Checking
```python
# Valid - no errors
result = fgt.api.monitor.system.fortiguard.test_availability.post(
    protocol="http",
    service="webfilter"
)

# Invalid - type checker warns
result = fgt.api.monitor.system.fortiguard.test_availability.post(
    protocol="invalid",  # ❌ Error: "invalid" is not assignable to Literal["https", "udp", "http"]
    service="webfilter"
)
```

## Test Example

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="your-token")

# IDE provides autocomplete for both parameters
result = fgt.api.monitor.system.fortiguard.test_availability.post(
    protocol="http",      # Autocompletes: https, udp, http
    service="webfilter",  # Autocompletes: emailfilter, webfilter
    port=443
)
```

## Schema Example

From `schema/7.6.5/monitor/system.fortiguard.test-availability.json`:

```json
{
  "request_fields": {
    "protocol": {
      "name": "protocol",
      "type": "string",
      "summary": "Protocol to check. [https | udp | http]",
      "required": true
    },
    "service": {
      "name": "service",
      "type": "string",
      "summary": "Service to check. [emailfilter | webfilter]",
      "required": true
    }
  }
}
```

## Coverage

This enhancement works for:
- ✅ **Request fields** (POST/PUT body parameters)
- ✅ **Query parameters** (already had enum extraction in v0.5.130)
- ✅ **Response fields** (TypedDict response types)
- ✅ **All API types** (CMDB, Monitor, Service, Log)

## Benefits

1. **Better IDE Support** - Autocomplete for enum parameters
2. **Type Safety** - Static type checking catches invalid values
3. **Documentation** - Type hints serve as inline documentation
4. **Developer Experience** - No need to check API docs for allowed values
5. **Zero Configuration** - Works automatically for all endpoints

## Implementation Details

### Files Modified

1. `.dev/generator/schema_management/schema_parser.py`
   - Enhanced `_parse_v1_7()` to extract allowed values from `summary` field
   - Sets `field_meta.options` when enum values detected

2. All endpoints regenerated (1,064 endpoints)
   - New Literal types where enum values exist in schema

### Files Already Supporting Literals

1. `.dev/generator/generators/endpoint_generator.py`
   - `_get_python_type_with_literal()` filter (already existed)
   
2. `.dev/generator/templates/endpoint_class.py.j2`
   - Uses `get_python_type_with_literal` filter (already existed)
   
3. `.dev/generator/templates/endpoint_class.pyi.j2`
   - Uses `get_python_type_with_literal` filter (already existed)

## Impact

- **All 1,064 endpoints** regenerated with Literal type support
- **Backward compatible** - existing code continues to work
- **No breaking changes** - only type hints enhanced
- **Immediate benefit** - IDE autocomplete available now

## Future Enhancements

Potential improvements:
1. Extract enum values from Swagger/OpenAPI specs directly
2. Support more description patterns
3. Generate documentation from enum values
4. Validate enum values at runtime (optional)

## Example Endpoints with Literal Types

After regeneration, these endpoints now have Literal types:

- `monitor/system/fortiguard/test-availability` - protocol, service
- Many firewall policy endpoints - action, status, etc.
- User authentication endpoints - type, method, etc.
- DHCP/DNS endpoints - various enum fields
- And hundreds more...

## Verification

```bash
# Check generated code
cat packages/fortios/hfortix_fortios/api/v2/monitor/system/fortiguard/test_availability.py | grep -A5 "def post"

# Verify type stub
cat packages/fortios/hfortix_fortios/api/v2/monitor/system/fortiguard/test_availability.pyi | grep -A5 "def post"
```

## Conclusion

This enhancement significantly improves the developer experience by providing:
- ✅ IDE autocomplete for enum parameters
- ✅ Type safety through static checking
- ✅ Better code readability
- ✅ Reduced need to check documentation

The implementation was seamless because the infrastructure was already in place - we just needed to connect the schema parser's `extract_allowed_values()` function to populate the `options` field that the generator was already checking for!
