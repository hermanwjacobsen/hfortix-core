# Generator Development Changelog

## January 3, 2026 - v0.5.2 Helper Functions Integration 🔧

### Summary
Integrated central `hfortix_fortios._helpers` module into generated code to reduce duplication and improve consistency.

### Changes Made

#### 1. **Endpoint Class Template** (`endpoint_class.py.j2`)
**Imports Added:**
```python
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)
```

**Methods Updated:**
- `put()` - Now uses `build_cmdb_payload()` instead of manual dict building
  - **Before:** 15+ lines of `if field is not None: payload_dict["field"] = field`
  - **After:** Single call to `build_cmdb_payload(field=field, ..., data=payload_dict)`
  - **Benefit:** ~30% code reduction, automatic snake_case → kebab-case conversion

- `post()` - Same as PUT, uses `build_cmdb_payload()`
  - **Benefit:** Consistent payload building across all methods

- `exists()` - Now uses `is_success(response)` instead of `response.get("status") == "success"`
  - **Benefit:** More robust error handling, consistent response checking

#### 2. **Validator Template** (`validator.py.j2`)
**Imports Added:**
```python
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)
```

**Benefit:**
- Validators can now reuse common validation functions
- Reduces duplicated validation logic
- Ensures consistent validation across all endpoints

#### 3. **Documentation Created**
- **HELPER_FUNCTIONS.md** - Comprehensive guide to helper integration
  - Lists all available helper functions from `_helpers` module
  - Shows before/after code examples
  - Documents benefits and usage patterns
  - 400+ lines of detailed documentation

### Code Impact

**Per Endpoint:**
- ~30 lines reduced in PUT/POST methods
- ~5-10 lines reduced in exists() method
- Cleaner, more maintainable code
- Single source of truth for common operations

**Across 1,219 Endpoints:**
- Estimated 36,000+ lines of code reduction
- More consistent error handling
- Easier to add new features (change in one place)

### Helper Functions Integrated

From `hfortix_fortios._helpers`:

1. **builders.py:**
   - `build_cmdb_payload()` - Payload building with auto-conversion

2. **response.py:**
   - `is_success()` - Response validation

3. **validators.py** (available for import):
   - Generic validators: `validate_enable_disable`, `validate_string_length`, `validate_integer_range`
   - Network validators: `validate_ip_address`, `validate_ipv6_address`, `validate_mac_address`, `validate_port_number`
   - Firewall validators: `validate_policy_id`, `validate_address_pairs`, `validate_seq_num`

4. **normalizers.py** (for future wrapper layer):
   - `normalize_to_name_list()` - List normalization for flexible inputs
   - `normalize_member_list()` - Member list normalization

### Files Modified
- `templates/endpoint_class.py.j2` - Added imports and updated PUT/POST/exists methods
- `templates/validator.py.j2` - Added common validator imports
- `HELPER_FUNCTIONS.md` - New comprehensive documentation
- `README.md` - Added link to HELPER_FUNCTIONS.md

### Validation
✅ Templates updated with proper imports  
✅ build_cmdb_payload() integrated in PUT/POST methods  
✅ is_success() integrated in exists() method  
✅ Common validators available for validator files  
✅ Documentation complete with examples  

### Benefits

**Code Quality:**
- Reduced duplication
- Consistent patterns
- Single source of truth

**Maintainability:**
- Bug fixes in one place
- Easier to add features
- Clear separation of concerns

**Testability:**
- Helper functions tested independently
- Smaller test surface area
- Generated code focuses on endpoint logic

### Next Steps
- Regenerate existing endpoints to use new helpers
- Add auto-detection of which validators to import based on field types
- Consider wrapper layer generation with `build_cmdb_payload_normalized()`

### References
- **Helper Module Location:** `packages/fortios/hfortix_fortios/_helpers/`
- **Migration Guide:** `docs/fortios/HELPER_MIGRATION_GUIDE.md`
- **GitHub Source:** `https://github.com/hermanwjacobsen/hfortix/tree/main/packages/fortios/hfortix_fortios/_helpers`

---

## January 3, 2026 - v0.5.1 Edge Case Support ✅

### Summary
Added support for endpoints with dots in their paths (e.g., `firewall.ssh/setting`, `firewall.ssl/setting`).

### Edge Case Pattern
**API Path**: `/cmdb/firewall.ssh/setting` (dot separates subcategory)

**Implementation:**
1. **Schema Parser** - Detects dots in endpoint path and creates separate `api_path` and `path` properties
2. **File Structure** - FLAT structure: `firewall/ssh_setting.py` (no subdirectories)
3. **API Calls** - Preserves dot notation: `endpoint = "/firewall.ssh/setting"`
4. **Class Naming** - `SshSetting` (from `ssh_setting`)

**Critical Design Decision:**
- **Do NOT create subdirectories** for dot-separated names (e.g., NO `firewall/ssh/` folder)
- Keep files flat in parent directory: `firewall/ssh_setting.py`
- Matches old implementation pattern
- Wrapper classes for dot-notation access will be in `__init__.py` (future work)

**Old Pattern (referenced from archive):**
- All files flat in `firewall/` directory
- Created wrapper classes (`Ssh`, `Ssl`) in `__init__.py` for dot-notation access
- Usage: `fgt.api.cmdb.firewall.ssh.setting.get()`
- This will be handled by `__init__.py` generation in future

### Files Modified
- `schema_parser.py` - Added `api_path` property to EndpointSchema, added dot detection logic
- `endpoint_generator.py` - Uses `schema.file_name` for file naming
- `validator_generator.py` - Uses `schema.file_name` for file naming
- `endpoint_class.py.j2` - Uses `schema.api_path` instead of `schema.path` for API calls
- `WORKFLOW_GUIDE.md` - Documented edge case pattern

### Validation
✅ **firewall/policy** - 38/38 tests still passing (7 API + 31 validators)  
✅ **firewall.ssh/setting** - Generated successfully with 0 Pylance errors  
✅ API paths correct: `/firewall.ssh/setting` (dot preserved)  
✅ File structure correct: `firewall/ssh_setting.py` (FLAT, no subdirs)  
✅ Matches old implementation pattern (flat file structure)  

### Next Steps
- Generate `__init__.py` files with wrapper classes for dot-notation access
- Test with live FortiGate API (if available)
- Add automated tests for edge case endpoints

---

## January 3, 2026 - v0.5.0 Prototype Validated ✅

### Summary
Successfully validated end-to-end generator workflow with `cmdb.firewall.policy` endpoint. All critical patterns proven and documented.

### Generated Code
- **Endpoint**: `packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py` (59,978 bytes, 188 fields)
- **Validators**: `packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/_helpers/policy.py` (67,924 bytes)
- **API Hierarchy**: CMDB, Log, Monitor, Service classes with proper structure

### Templates Created
- `templates/endpoint_class.py.j2` (180 lines) - Generates endpoint classes with CRUD operations
- `templates/validator.py.j2` (245 lines) - Generates validation helpers with constraints

### Key Fixes Applied

#### 1. Template Whitespace Control
**Problem**: Using `{%-` and `-%}` whitespace markers stripped newlines → 236+ syntax errors

**Solution**: 
```python
env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)
# Use plain {% %} tags in templates
```

#### 2. Type Narrowing for Union Types
**Problem**: Pylance couldn't narrow `Union[dict, Coroutine]` with `hasattr()`

**Solution**:
```python
# ❌ Wrong
if hasattr(response, "get"):

# ✅ Correct
if isinstance(response, dict):
```

#### 3. HTTP Client Data Parameter
**Problem**: Templates used `json=` parameter, FortiGate expects `data=`

**Solution**:
```python
self._client.post("cmdb", endpoint, data=payload_dict, ...)
```

#### 4. exists() Exception Handling
**Problem**: exists() raised exceptions on 404 instead of returning False

**Solution**:
```python
def exists(self, policyid: int, ...) -> bool:
    try:
        response = self.get(policyid=policyid, ...)
        # ... check response
    except Exception:
        return False  # Not found
```

#### 5. Kebab-Case Path Conversion
**Problem**: Path `firewall/policy` not converted properly to `firewall_policy`

**Solution**:
```python
def kebab_to_snake(value: str) -> str:
    return value.replace("-", "_").replace("/", "_")
```

### Test Suite Created

#### API Integration Tests (7 tests)
Location: `.tests/pytests/api/cmdb/firewall/test_policy.py`

- test_1_list_all_policies - List all policies
- test_2_get_specific_policy - Get by ID
- test_3_create_policy - Create new policy
- test_4_exists_method - Test exists() helper
- test_delete_policy - Delete policy
- test_exists_method - Full exists lifecycle
- test_payload_dict_method - Alternative creation

**Features:**
- Numeric prefixes for logical ordering
- Autouse fixture for automatic cleanup
- Tests against live FortiGate (192.168.1.99)
- All policies created are automatically deleted

#### Validator Unit Tests (31 tests)
Location: `.tests/pytests/api/cmdb/firewall/test_policy_validators.py`

**Coverage:**
- Required fields validation (5 tests)
- GET request validation (5 tests)
- POST request validation (6 tests)
- PUT request validation (3 tests)
- Enum constants validation (4 tests)
- Field constants validation (4 tests)
- Edge cases (4 tests)

**Test Results**: 38/38 passing (100%)

### FortiGate API Learnings

1. **GET Response Format**: Returns list directly, not dict with "results"
   ```python
   policies = fgt.api.cmdb.firewall.policy.get()  # Returns list
   for policy in policies:  # Not policies["results"]
   ```

2. **List Field Format**: Requires list of dicts with "name" key
   ```python
   srcintf=[{"name": "port3"}, {"name": "port4"}]  # ✅ Correct
   srcintf=["port3", "port4"]  # ❌ Wrong
   ```

3. **Required Fields vs Schema**: Schema marks many optional fields as required
   - Actual required: 7 fields (srcintf, dstintf, schedule, etc.)
   - Schema claims: Many more
   - Solution: REQUIRED_FIELDS based on API testing, not just schema

4. **Enum Case Sensitivity**: All enums are case-sensitive
   ```python
   status="enable"   # ✅ Correct
   status="ENABLE"   # ❌ Wrong
   ```

### Documentation Created

1. **WORKFLOW_GUIDE.md** - Comprehensive guide with validated patterns
2. **VALIDATOR_TEST_SUMMARY.md** - Test coverage documentation
3. **Updated README.md** - Current status and next steps
4. **This CHANGELOG.md** - Development history

### File Structure

```
.dev/generator/
├── WORKFLOW_GUIDE.md              # ✅ NEW - Validated workflow
├── CHANGELOG.md                   # ✅ NEW - This file
├── generate_firewall_policy.py    # Working generator script
├── schema_parser.py               # Schema parsing logic
├── generators/
│   ├── endpoint_generator.py      # Endpoint class generator
│   └── validator_generator.py     # Validator generator
└── templates/
    ├── endpoint_class.py.j2       # Endpoint template
    └── validator.py.j2            # Validator template

packages/fortios/hfortix_fortios/api/v2/
├── __init__.py                    # API class
├── cmdb/
│   ├── __init__.py               # CMDB class
│   └── firewall/
│       ├── __init__.py           # Firewall class
│       ├── policy.py             # ✅ Generated endpoint
│       └── _helpers/
│           └── policy.py         # ✅ Generated validators

.tests/pytests/api/cmdb/firewall/
├── __init__.py
├── test_policy.py                # ✅ API integration tests
├── test_policy_validators.py     # ✅ Validator unit tests
└── VALIDATOR_TEST_SUMMARY.md     # ✅ Test documentation
```

### Metrics

**Code Generated:**
- Endpoint: 59,978 bytes (1,500+ lines)
- Validators: 67,924 bytes (1,882 lines)
- Total: ~128 KB of production-ready code

**Test Coverage:**
- 38 tests total
- 7 API integration tests (with live FortiGate)
- 31 validator unit tests
- 100% pass rate
- ~600 lines of test code

**Field Coverage:**
- 188 fields supported in endpoint
- 7 required fields identified
- 141 fields with defaults
- 60+ enum validators
- 4+ main validation functions

### Generator Performance

- **Template rendering**: < 1 second
- **File writing**: < 1 second
- **Total generation time**: < 2 seconds
- **Pylance validation**: 0 errors, 0 warnings
- **Test execution**: 5.4 seconds for all 38 tests

### Validation Criteria Met

✅ Templates generate syntactically correct Python  
✅ Generated code passes Pylance type checking (0 errors)  
✅ All CRUD operations work against live FortiGate  
✅ Validators catch invalid inputs  
✅ Type hints support both sync and async usage  
✅ Exception handling prevents crashes  
✅ Tests provide comprehensive coverage  
✅ Cleanup prevents FortiGate pollution  
✅ Documentation captures all learnings  

### Ready for Next Phase

**Proven Patterns:**
- Template syntax and configuration
- Type safety approach
- HTTP client integration
- Error handling strategy
- Test organization
- Cleanup mechanisms

**Next Endpoints to Generate:**
1. `cmdb.firewall.address` - Validate reusability
2. `cmdb.system.interface` - Different category
3. `cmdb.router.static` - Routing config
4. `cmdb.user.local` - User management

**Remaining Work:**
- Generic generate.py orchestrator
- Automated __init__.py generation
- Schema downloader for bulk operations
- CI/CD integration for regeneration
- Version tracking in generated files

### Breaking Changes

None - this is new functionality.

### Deprecations

None.

### Security

No security issues identified. Generated code uses existing hfortix_core security features (token auth, TLS).

---

**Status**: ✅ Production Ready for Single Endpoint Generation  
**Next Milestone**: Multi-endpoint generation automation  
**Confidence Level**: High - all critical patterns validated
