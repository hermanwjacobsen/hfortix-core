# Read-Only Endpoint Detection and Test Generation Fix

## Problem
FortiOS has certain endpoints that are **read-only reference tables** (e.g., geography data, timezone information). These endpoints behave differently than standard CRUD endpoints:

- **Standard CRUD endpoints**: `GET /cmdb/firewall/address?name=test1` returns a single item
- **Read-only reference tables**: `GET /cmdb/firewall/region?id=1` returns ALL items (ignores the filter)

This caused test failures because our test generator assumed all endpoints support querying by mkey.

## Examples of Read-Only Endpoints

### Geography Reference Tables
- `cmdb/firewall/region` - List of geographic regions (203 items)
- `cmdb/firewall/city` - List of cities (2 items in test environment)  
- `cmdb/firewall/country` - List of countries (246 items)

### System Reference Tables
- `cmdb/system/timezone` - List of available timezones

## Solution

### 1. Schema Metadata Detection
FortiOS schemas include a `readonly` field for these endpoints:

```json
{
  "http_method": "GET",
  "results": {
    "name": "region",
    "category": "table",
    "help": "Define region table.",
    "readonly": true,     ← Detection flag
    "mkey": "id",
    "mkey_type": "integer",
    ...
  }
}
```

### 2. Schema Parser Enhancement
Added `readonly` field to `EndpointSchema` dataclass:

```python
@dataclass
class EndpointSchema:
    ...
    readonly: bool = False  # True for read-only reference tables
```

Parse from schema JSON:
```python
# Check if endpoint is readonly (e.g., geography reference tables)
readonly = results.get("readonly", False)
```

### 3. Test Template Updates
Skip unsupported tests for readonly endpoints:

**Get Specific Item Test** - Now skipped for readonly endpoints:
```jinja
{% if schema.mkey and schema.category == 'cmdb' and not schema.readonly %}
def auto_test_get_specific_item(self):
    """Test GET - retrieve specific {{ schema.name }} by {{ schema.mkey }}."""
    # ... test code ...
{% endif %}
```

**Exists Method Test** - Also skipped for readonly endpoints:
```jinja
{% if schema.category == 'cmdb' and not schema.readonly %}
class TestAuto{{ schema.class_name }}Exists:
    """Auto-generated exists() tests."""
    # ... test code ...
{% endif %}
```

### 4. Tests Generated for Read-Only Endpoints
Read-only endpoints still get comprehensive testing:

✅ **Included Tests:**
- `auto_test_get_list_all()` - Get all items
- `auto_test_get_with_vdom()` - Get with vdom parameter  
- `auto_test_get_with_filters()` - Get with filter/format parameters
- `auto_test_validator_import()` - Import validators
- `auto_test_validator_create_all_required()` - Validate required fields

❌ **Skipped Tests:**
- `auto_test_get_specific_item()` - Query by mkey (doesn't work for readonly)
- `auto_test_exists_method()` - exists() helper (relies on mkey query)

## Test Results

### Before Fix
```
FAILED auto_test_region.py::TestAutoRegionGet::auto_test_get_specific_item
FAILED auto_test_city.py::TestAutoCityGet::auto_test_get_specific_item  
FAILED auto_test_country.py::TestAutoCountryGet::auto_test_get_specific_item
FAILED auto_test_timezone.py::TestAutoTimezoneGet::auto_test_get_specific_item
FAILED auto_test_timezone.py::TestAutoTimezoneExists::auto_test_exists_method
```

### After Fix
```
✅ 18 passed (region, city, country - 6 tests each)
✅ 3 passed (timezone)
✅ All CMDB tests: 3500 passed, 506 skipped
```

## Files Modified

1. **`.dev/generator/schema_parser.py`**
   - Added `readonly: bool = False` to `EndpointSchema` dataclass
   - Parse `readonly` from schema JSON: `readonly = results.get("readonly", False)`
   - Pass `readonly` to `EndpointSchema` constructor

2. **`.dev/generator/templates/test_basic.py.j2`**
   - Changed `{% if schema.mkey and schema.category == 'cmdb' %}` → `{% if schema.mkey and schema.category == 'cmdb' and not schema.readonly %}`
   - Changed `{% if schema.category == 'cmdb' %}` → `{% if schema.category == 'cmdb' and not schema.readonly %}` for Exists class

## Regeneration Commands
```bash
# Regenerate geography endpoints
python .dev/generator/generate.py --endpoint cmdb.firewall.region
python .dev/generator/generate.py --endpoint cmdb.firewall.city
python .dev/generator/generate.py --endpoint cmdb.firewall.country

# Regenerate system timezone
python .dev/generator/generate.py --endpoint cmdb.system.timezone
```

## Impact on API Usage

The read-only detection is **transparent to users**. These endpoints still work normally:

```python
# Get all regions (works)
regions = fgt.api.cmdb.firewall.region.get()

# Get all timezones (works)
timezones = fgt.api.cmdb.system.timezone.get()

# Query by mkey doesn't filter (returns all items)
# This is FortiOS behavior, not a library limitation
result = fgt.api.cmdb.firewall.region.get(id=1)  # Returns ALL 203 regions
```

## Future Enhancements

1. **Document in endpoint docstrings**: Add "Read-Only Reference Table" note to docstrings
2. **Warn on unsupported operations**: Log warning if POST/PUT/DELETE called on readonly endpoint
3. **Optimize exists()**: Could implement exists() for readonly endpoints by scanning the full list
4. **Cache reference tables**: Read-only data could be cached since it rarely changes

## Related Issues

This fix resolved 5 test failures:
- ✅ firewall/region (get specific, exists)
- ✅ firewall/city (get specific, exists)
- ✅ firewall/country (get specific, exists)
- ✅ system/timezone (get specific, exists)

Remaining test failures (8 total) are unrelated:
- switch_controller/lldp_profile (3 enum tests)
- system/interface (5 validator/enum tests)
