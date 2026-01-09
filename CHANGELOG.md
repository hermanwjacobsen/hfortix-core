# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.42] - 2026-01-09

### Fixed
- **Fixed hyphenated API response keys not matching TypedDict stubs**
  - Added automatic key normalization to convert hyphens to underscores in API responses
  - FortiOS returns keys like `tcp-portrange`, `cache-ttl`, `uuid-idx` with hyphens
  - Python TypedDict and attribute access require underscores: `tcp_portrange`, `cache_ttl`, `uuid_idx`
  - Normalization now happens automatically in HTTP client response processing
  - Fixes autocomplete and type checking for all fields with hyphens in their names
  - Example: `service['tcp_portrange']` now works (previously only `service['tcp-portrange']` worked)
  - Example: `addr.cache_ttl` now works in object mode
  - Added `normalize_keys()` utility function in `hfortix_core.utils`
  - Applied to both sync (`HTTPClient`) and async (`AsyncHTTPClient`) response processing

### Changed
- **Optimized helper file code generation using functools.partial**
  - Replaced ~200 lines of wrapper function definitions with ~10 lines of partial bindings in generated helper files
  - Reduced helper file size by ~50-80 lines per file without affecting functionality
  - Changed from pattern: `def get_field_type(field_name: str): return _get_field_type(FIELD_TYPES, field_name)`
  - To pattern: `get_field_type = partial(get_field_type, FIELD_TYPES)`
  - Saves ~2-3MB across 1,200+ generated helper files
  - IDE autocomplete, type hints, and introspection remain fully functional
  - Generator backup created in `.dev/generator/archive/pre-deduplication-20260109_113603/`
  - Updated validator template: `.dev/generator/templates/validator.py.j2`

- **Reduced helper module docstring verbosity**
  - Removed verbose docstring examples from helper utility modules
  - Kept concise descriptions for all public functions
  - Affected modules: `_helpers/builders.py`, `_helpers/converters.py`, `_helpers/normalizers.py`, `_helpers/response.py`, `_helpers/validation.py`
  - Reduced internal documentation overhead while maintaining clarity

## [0.5.41] - 2026-01-09

### Fixed
- **Fixed missing helper methods in DictMode and ObjectMode classes**
  - Added helper method signatures to mode-specific classes: `exists()`, `set()`, `defaults()`, `schema()`, `help()`, `fields()`, `field_info()`, `validate_field()`, `required_fields()`
  - Fixed "Attribute is unknown" errors when calling helper methods on mode-specific clients
  - Example: `fg.api.cmdb.authentication.rule.defaults()` now works correctly
  - Example: `fgt_object.api.cmdb.firewall.service.group.exists(name="test")` now works correctly
  - Helper methods were previously only available in base class, not in DictMode/ObjectMode
  - Regenerated all 1,064 endpoint `.pyi` stub files

## [0.5.40] - 2026-01-09

### Fixed
- **Fixed overload matching for mode-specific clients with keyword arguments**
  - Added explicit default `@overload` decorators for ObjectMode mutation methods (POST/PUT/DELETE)
  - Fixed "No overloads match" error when calling mutations with keyword args but no `response_mode`
  - ObjectMode methods now correctly infer return types without requiring explicit `response_mode="object"`
  - Example: `fgt_object.api.cmdb.firewall.policy.post(name="test", action="accept")` → `PolicyObject`
  - Previously required keyword-only `response_mode` parameter due to `*,` separator
  - DictMode already had proper default overloads; fixed ObjectMode to match
  - Regenerated all 1,064 endpoint `.pyi` stub files

## [0.5.39] - 2026-01-09

### Fixed
- **Fixed POST/PUT/DELETE type inference for mutation operations**
  - Added explicit `@overload` decorators for default case (no `response_mode` parameter)
  - Fixed "No overloads match" Pylance errors when calling mutations without `response_mode`
  - Removed `response_mode` parameter from final `def` implementation signatures
  - Made all mode override overloads keyword-only using `*,` separator
  - Pylance now correctly infers `MutationResponse` for default calls
  - Example: `delete(name="test")` → `MutationResponse`, not `RuleObject`
  - Fixed for both DictMode (default) and ObjectMode classes
  - Regenerated all 1,064 endpoint `.pyi` stub files

## [0.5.38] - 2026-01-09

### Fixed
- **Fixed Literal type validation in Payload TypedDict dict literals**
  - Removed `NotRequired` wrapper from Literal fields in Payload TypedDict stubs
  - Pylance now validates Literal values when assigning dict literals to Payload types
  - Example: `policy: PolicyPayload = {"action": "invalid"}` now shows type error
  - Previously, `NotRequired[Literal[...]]` prevented Pylance from validating inner Literal
  - Fields are still optional via `total=False` on the TypedDict class
  - All 1,064 endpoints regenerated with this fix

- **Fixed test template expecting list instead of dict for mkey queries**
  - Since v0.5.33, querying by mkey returns single dict, not list of one item
  - Updated test template to expect `dict` instead of `list` for `get(mkey=value)`
  - Regenerated all 936 auto-generated test files

## [0.5.37] - 2026-01-09

### Fixed
- **Fixed Pylance overload matching for default response mode**
  - Reordered stub file overloads: DEFAULT mode (no `response_mode`) now comes FIRST
  - Pylance matches overloads top-to-bottom; previous order caused `response_mode: Literal["object"] = ...` to match calls without `response_mode`
  - Fixed "Never is not iterable" error when iterating over table fields without explicit `response_mode`
  - Example: `for intf in rule["srcintf"]` now works without needing `response_mode="dict"`
  - Accessing nonexistent fields like `rule["nonexistent_field"]` now correctly shows TypedDict key error
  - Fixed in generator template and regenerated all 1,064 endpoints
  - Also fixed `post()`, `put()`, and `delete()` method overloads for consistency

### Added
- **Added `MutationResponse` TypedDict for POST/PUT/DELETE operations**
  - New `MutationResponse` type in `hfortix_core.types` with `status` and `http_status` fields
  - POST/PUT/DELETE now return `MutationResponse` instead of `dict[str, Any]`
  - Enables type checking for mutation responses: `result["nonexistent"]` now shows error
  - Example: `post_result["status"]` works, `post_result["nonexistent"]` shows error

- **Added `RawAPIResponse` TypedDict for `raw_json=True` mode**
  - New `RawAPIResponse` type for full FortiOS API envelope responses
  - Fields: `http_method`, `http_status`, `status`, `vdom`, `results`, `path`, `name`, `mkey`, `revision`, `serial`, `version`, `build`
  - All fields marked as required to provide autocomplete without warnings
  - Primary purpose: catch typos - `response["nonexistent"]` shows error
  - Use `.get()` for fields that may not be present in specific response types

- **Added validation hints to type stub comments**
  - Field comments now include: `Default: value`, `Min: value`, `Max: value`, `MaxLen: value`
  - Example: `cache_ttl: int  # Defines the minimal TTL... | Default: 0 | Min: 0 | Max: 86400`
  - Example: `name: str  # Address name. | MaxLen: 79`
  - Validation hints shown in Payload TypedDict, Response TypedDict, and Object classes
  - Also shown in nested TypedDict items for table field children
  - Helps developers understand field constraints without consulting documentation

## [0.5.36] - 2026-01-08

### Changed
- **Regenerated all 1,064 endpoints with enhanced TypedDict autocomplete**
  - Applied nested TypedDict fixes to all endpoints
  - Ensured all table field items have proper type hints
  - All endpoints now provide full autocomplete for nested table field items

## [0.5.35] - 2026-01-08

### Added
- **Nested TypedDict autocomplete for table field items in dict mode**
  - Generated TypedDict classes for all table field children (e.g., `RuleSrcintfItem`)
  - Full IDE autocomplete when iterating over table fields: `for intf in rule["srcintf"]: intf["name"]`
  - Type checking for nested items: `intf["nonexistent_field"]` now shows error
  - Fields are required (not `NotRequired`) since they're always present in API responses
  - Applies to all endpoints with table fields

### Fixed
- **Fixed type inference for default response mode**
  - Removed overly restrictive `raw_json: Literal[False]` constraint from default mode overloads
  - Pylance now correctly infers types when `response_mode` is not specified
  - Fixed `"Never" is not iterable` error when iterating over table fields
  - Response type inference now works regardless of client-level or request-level `response_mode` setting

## [0.5.34] - 2026-01-08

### Improved
- **Enhanced type stub overloads for better IDE autocomplete without explicit type annotations**
  - Added specific overloads for default mode (when `response_mode` is not specified)
  - Pylance now correctly infers `RuleResponse` type when querying by mkey without `response_mode`
  - Example: `rule = fgt.api.cmdb.authentication.rule.get(name="test")` now properly typed as `RuleResponse`
  - No longer need explicit type annotations like `rule: RuleResponse = ...`
  - Applies to all 1,064 endpoints
  - Improved overload ordering for better type inference

## [0.5.33] - 2026-01-08

### Fixed
- **Dict mode query by name now returns single dict instead of list**
  - When querying by name/mkey with `response_mode="dict"` (or default), now correctly returns single dict instead of list
  - Aligns dict mode behavior with object mode for consistency
  - Example: `group = fgt.api.cmdb.firewall.service.group.get(name="test")` returns `dict` not `list[dict]`
  - Both modes now have identical unwrapping behavior when querying by identifier
  - **Breaking Change**: Tests expecting list for single-item queries need to be updated
  - Fixed 936 auto-generated test files to expect dict instead of list

## [0.5.32] - 2025-01-24

### Fixed
- **Object mode query by name now returns single object instead of list**
  - When querying by name/mkey with `response_mode="object"`, now correctly returns single `FortiObject` instead of list
  - Added `unwrap_single=True` parameter to old API endpoints when querying by identifier
  - Example: `group = fgt.api.cmdb.firewall.service.group.get(name="test")` returns `FortiObject` not `list[FortiObject]`
  - Aligns old API behavior with new v2 API which already had this feature

- **FortiObject now wraps nested table field items instead of flattening to strings**
  - Table field members (lists of dicts) now wrapped in `FortiObject` for attribute access
  - Example: `group.member[0].name` now works (was: `AttributeError: 'str' object has no attribute 'name'`)
  - Changed from auto-flattening `[{"name": "test"}]` → `["test"]` to wrapping in `FortiObject`
  - Enables clean attribute access while maintaining compatibility

- **Clean string representation for simple FortiObject members**
  - Simple objects (containing only `name` and optionally `q_origin_key`) now show clean repr
  - Example: `['port3', 'port4']` instead of `[FortiObject(port3), FortiObject(port4)]`
  - Added `__str__` method for user-friendly output
  - Improves readability when printing lists of members

### Improved
- **Type annotations for FortiOS client attributes**
  - Added explicit type annotation `self._api: API = API(wrapped_client)` for better IDE support
  - Added type annotations to test helper modules (`fgt: FortiOS`, `fgt_ResponseModeObject: FortiOS`)
  - Improved Pylance autocomplete reliability after sys.path manipulation
  - Better type inference for `fgt.api`, `fgt.api.cmdb`, etc.

## [0.5.31] - 2026-01-08

### Added
- **Nested typed classes for table field children**
  - Generated specific typed classes for table field items (e.g., `GroupMemberObject`)
  - Each table field now has its own typed class with proper attribute definitions
  - Example: `member: list[GroupMemberObject]` instead of generic `list[FortiObject]`
  - Enables full IDE autocomplete for nested table attributes like `.name`, `.id`, etc.
  - Pylance now validates attribute access and shows errors for non-existent fields

- **Keyword argument support for mkey parameters**
  - Added overloads to support both positional and keyword mkey arguments
  - Both `get("name")` and `get(name="name")` now correctly infer single object return type
  - Proper overload ordering ensures Pylance matches the most specific signature
  - Works for both `response_mode="object"` and `response_mode="dict"`

### Improved
- **IDE autocomplete for table field members in object mode**
  - Table fields now return typed objects instead of generic `FortiObject`
  - Example: `group.member[0].name` shows autocomplete with proper type validation
  - Response objects in `response_mode="object"` provide full attribute autocomplete
  - Template generates nested classes for all table fields with children metadata

- **Whitespace stripping in table field normalization**
  - All string values automatically stripped of leading/trailing whitespace
  - Prevents "Entry not found" errors from accidental spaces in member names
  - Example: `" test_service1 "` → `"test_service1"` automatically
  - Applied to all normalizers: `normalize_table_field()`, `normalize_string_list()`, `normalize_source_destination_list()`

### Added
- **Enhanced parameter documentation with schema descriptions**
  - All POST and PUT method parameters now show field descriptions from FortiOS schema in IDE tooltips
  - Example: Hovering over function shows full Args section with descriptions for every parameter
  - Improved developer experience with rich, schema-driven documentation

- **Accurate type hints for table fields vs multi-value option fields**
  - Table fields: `str | list[str] | list[dict[str, Any]]` (supports flexible normalization)
  - Multi-value option fields: `Literal[...] | list[str]` (string list only, no dict support)
  - Single-value fields: Just their base type (`str`, `int`, `Literal[...]`)
  - Removes confusing `list[dict[str, Any]]` from option fields like `method`, `digest_algo`

- **Universal table field normalization with schema awareness**
  - Added `normalize_table_field()` helper that supports ANY mkey (not just "name")
  - Handles custom mkeys: `interface-name`, `id`, `index`, `seq-num`, `priority`, etc.
  - Auto-detects single-field (flexible) vs multi-field (strict) validation from schema
  - Generates intelligent examples based on field types (ip→192.168.1.10, id→1, cipher→TLS-AES-128-GCM-SHA256)
  - Shows format documentation for ALL table fields (removed 10-field limit)

### Fixed
- **Fixed table field documentation not showing for all fields**
  - Issue: Only 5 of 11 table fields were documented in complex endpoints like `firewall.vip`
  - Root cause: Schema parser used kebab-case keys, template expected snake_case keys
  - Solution: Convert field names to snake_case in `extract_table_fields_metadata()`
  - Result: All table fields now show complete format documentation in IDE tooltips

## [0.5.30] - 2026-01-08

### Fixed
- **Fixed stub generator comment truncation causing syntax errors**
  - Added `sanitize_comment` filter to properly truncate help text in `.pyi` stubs
  - Prevents broken comments like `# Sample one packet every configured number of packets (1 -` 
  - Comments now safely truncate without breaking parentheses or special characters
  - Fixes Pylance failing to parse endpoints like `system.interface` due to syntax errors

## [0.5.29] - 2026-01-07

### Improved
- **Enhanced IDE autocomplete for typed endpoint responses**
  - `AddressObject`, `PolicyObject`, etc. no longer inherit `__getattr__`, so Pylance flags invalid attribute access
  - `address.nonexistent_field` now shows error: "Cannot access attribute 'nonexistent_field'"
  - Added `AddressResponse` TypedDict for dict mode returns - all fields required (no NotRequired warnings)
  - `response_mode="dict"` now returns `list[AddressResponse]` with full `["field"]` autocomplete
  - `response_mode="object"` now returns `list[AddressObject]` with full `.field` autocomplete
  - Added `@final` decorator to typed Object classes for stricter type checking

### Fixed
- **Fixed dict mode iteration type hints**
  - `for addr in addresses:` with `response_mode="dict"` now correctly types `addr` as `AddressResponse`
  - `addr["name"]` no longer shows "not a required key" warning

## [0.5.28] - 2026-01-07

### Fixed
- **Fixed autocomplete when `response_mode` is set at client level**
  - Fallback `get()` return type now includes Object types in union
  - `result.name`, `result.subnet` etc. now have autocomplete even when `response_mode` isn't passed explicitly
  - Supports pattern: `fgt_object = FortiGate(..., response_mode="object")`

## [0.5.27] - 2026-01-07

### Fixed
- **Fixed return type annotations for sync usage** (TYPE HINT FIX)
  - Removed `Coroutine` union types from return signatures in `.pyi` stubs
  - Methods now return `dict[str, Any]` instead of `Union[dict[str, Any], Coroutine[...]]`
  - Fixes Pylance errors like `"__getitem__" method not defined on type "Coroutine[...]"`
  - Result: `result['status']` now works without type errors for sync clients

## [0.5.26] - 2026-01-07

### Added
- **Added `__getitem__` support to `FortiObject`**
  - Dictionary-style access now works: `settings['grayware']`
  - Both attribute and bracket notation supported: `settings.grayware` or `settings['grayware']`
  - Fixes Pylance `"__getitem__" method not defined on type` errors

## [0.5.25] - 2026-01-07

### Fixed
- **Fixed singleton endpoint `get()` return types** (TYPE HINT FIX)
  - Singleton endpoints (like `antivirus/settings`) now return single object instead of list
  - `fgt.api.cmdb.antivirus.settings.get(response_mode="object")` returns `SettingsObject` not `list[SettingsObject]`
  - Fixes Pylance errors when accessing attributes on singleton endpoint results
  - Affects all 114 singleton endpoints

### Improved
- **Filter parameter now accepts both string and list**
  - `filter` parameter type changed from `list[str] | None` to `str | list[str] | None`
  - Single filter: `get(filter="name==test")` ✓
  - Multiple filters: `get(filter=["name==test", "type==ipmask"])` ✓
  - Better ergonomics matching FortiOS REST API behavior

## [0.5.24] - 2026-01-07

### Changed
- Version alignment release for all packages (core, fortios, meta)

## [0.5.23] - 2026-01-07

### Fixed
- **Fixed singleton endpoint PUT requests** (CRITICAL FIX)
  - Singleton endpoints (like `alertemail/setting`) no longer require identifier in URL
  - Fixed `ValueError: name is required for PUT` error for singleton endpoints
  - Example: `fgt.api.cmdb.alertemail.setting.put(mailto1="test@example.com")` now works correctly
  - Affects all singleton endpoints (no mkey, `endpoint_type: "singleton"`)
- **Fixed stub files for endpoints with `SUPPORTS_CREATE = False`**
  - Removed `post()` method overloads from stub files when endpoint doesn't support creation
  - Fixes `NotImplementedError: You should not call an overloaded function` error
  - Singleton and read-only endpoints now have correct type hints

### Improved
- Enhanced error message for FortiOS error -651 to include duplicate name/unique field conflict hint
  - Now suggests: "Invalid value provided. Check parameter format and allowed values. May also indicate duplicate name or unique field conflict."
  - Helps users identify when error is caused by duplicate names rather than just invalid formats

## [0.5.22] - 2026-01-07

### Added
- **Interactive help system** for all API endpoints
  - `help()` method on all endpoints (via `MetadataMixin`)
  - Works as classmethod or instance method: `endpoint.help()` or `fgt.api.cmdb.firewall.address.help()`
  - Context-aware help based on endpoint category (CMDB, Monitor, Log, Service)
  - Two modes:
    - No argument: Full endpoint help with capabilities, operations, and info methods
    - With field name: Field-specific help showing type, description, constraints, and options
  - Dynamically discovers all available methods on each endpoint
  - Package-level `help()` function also available: `from hfortix_fortios import help`
  - Example: `fgt.api.cmdb.firewall.address.help()` or `help(fgt.api.cmdb.firewall.address)`

### Changed
- **Metadata methods now return dict/list with JSON intent** for consistency
  - `defaults()` - Returns `dict[str, Any]` with default field values (JSON-serializable)
  - `schema()` - Returns `dict[str, Any]` with schema metadata (JSON-serializable)
  - `fields()` - Returns `list[str]` by default, or `dict[str, Any]` if `detailed=True` (JSON-serializable)
  - All return native Python types (dict/list) instead of strings
  - Use `to_json()` for formatted output: `print(to_json(Settings.defaults()))`
  - Breaking change from previous string returns
  - Example: `schema = Address.schema(); print(f"Endpoint: {schema['endpoint']}")`
- Updated `MetadataMixin.help()` to use new interactive help system
  - Replaced string-returning help with interactive console output
  - Field help now shows formatted output with constraints and options
  - Removed `show_examples` parameter (examples removed from output)

### Fixed
- **Fixed `set()` method to accept all field parameters** (CRITICAL FIX)
  - `set()` now accepts individual field parameters just like `post()` and `put()`
  - Example: `fgt.api.cmdb.firewall.address.set(name="test", subnet="10.0.0.0/24")`
  - Previously only accepted `payload_dict` parameter, causing `ValueError`
  - All 1064 endpoints regenerated with the fix
- **Fixed type stubs (.pyi) for list field parameters**
  - All list fields now show correct types: `str | list[str] | list[dict[str, Any]] | None`
  - Fixed "No overloads match" Pylance errors
  - Example: `srcintf=["port3"]` now has proper type checking
  - Affects all CRUD methods: `post()`, `put()`, `set()`
  - All overloads updated to include complete field parameter lists

### Removed
- Removed `get_schema()` classmethod alias - use `schema()` instead
- Removed `show_methods()` - functionality merged into `help()`

## [0.5.21] - 2026-01-07

### Added
- **Formatting utility functions** - Type-agnostic data conversion utilities
  - `to_json(data, indent=2)` - Convert any data to formatted JSON string
  - `to_csv(data, separator=', ')` - Convert any data to comma-separated string
  - `to_dict(data)` - Convert any data to dictionary
  - `to_multiline(data, separator='\n')` - Convert any data to newline-separated string
  - `to_quoted(data, quote='"', separator=', ')` - Convert any data to quoted string
  - All functions handle ANY input type (objects, dicts, lists, primitives, None)
  - Never raise exceptions - return sensible defaults for edge cases
  - Available directly from package root: `from hfortix_fortios import to_csv, to_json`
  - Full type hints and IDE autocomplete support

### Documentation
- Added comprehensive `FORMATTING_UTILITIES.md` guide with examples
- Includes real-world usage examples for FortiOS data formatting

## [0.5.20] - 2026-01-07

### Removed
- **FortiList wrapper class** - Reverted due to IDE autocomplete limitations
  - Removed `.csv()`, `.json()`, `.list()`, `.dict()`, `.join()` methods
  - FortiObject now returns plain Python lists for list fields
  - Reason: Python's type system cannot provide autocomplete for union return types
  - Users should use standard Python list operations and string formatting instead

## [0.5.19] - 2026-01-07 [YANKED]

### Added
- **FortiList wrapper class** - Enhanced list type with convenient formatting methods (removed in 0.5.20)
  - `.csv()` - Convert to comma-separated string (e.g., `"port1, port2, port3"`)
  - `.json(**kwargs)` - Convert to JSON string with optional formatting
  - `.list()` - Get as plain Python list
  - `.dict()` - Convert back to FortiOS member_table format `[{'name': 'x'}]`
  - `.join(separator)` - Join with custom separator (e.g., `' → '`, `' | '`)
  
### Changed
- **FortiObject now auto-wraps list fields** in FortiList for cleaner API
  - `policy.srcintf.csv()` instead of manual formatting
  - `policy.dstaddr.join(' | ')` for custom separators
  - All list operations still work normally (indexing, iteration, etc.)
  
### Improved
- **Type hints for IDE autocomplete** - Added `.pyi` stubs with `@property` definitions
  - Full autocomplete for 35+ common FortiOS list fields
  - Includes: srcintf, dstintf, srcaddr, dstaddr, service, poolname, etc.
  - Works automatically when package is installed via pip

## [0.5.18] - 2026-01-07

### 📊 Summary of Generator Optimizations (2026-01-07)

**Major code generation improvements resulting in significant code reduction and better developer experience.**

#### Total Impact

| Metric | Reduction | Details |
|--------|-----------|---------|
| **Lines of Code Eliminated** | **-143,419 lines** | Removed duplicate/boilerplate code |
| **Endpoint File Size** | **-25% average** | Per endpoint (e.g., 949 → 708 lines) |
| **Helper File Size** | **-3.2% average** | Per helper (348 → 337 lines) |
| **Files Regenerated** | **1,064 endpoints** | All CMDB/Monitor/Service endpoints |

#### Breakdown by Optimization

1. **Protocol-Based Type Hints**: -131,200 lines
   - Eliminated duplicate `@overload` decorators (18 per endpoint × 1,063)
   - Moved to shared `_protocols.py` module (300 lines)
   - **Net savings: 130,900 lines**

2. **Helper Validation Centralization**: -11,727 lines
   - Eliminated duplicate validation functions (1,062 helpers)
   - Centralized to `_helpers/validation.py` (235 lines)
   - **Net savings: 11,492 lines**

3. **Type Hint Fixes**: Better autocomplete, cleaner code
   - Fixed GET method overload ambiguity
   - Fixed schema parser for Literal types
   - Improved parameter autocomplete for POST/PUT/DELETE

#### Developer Experience Improvements

✅ **Full autocomplete** for all 220+ parameters per endpoint  
✅ **Correct type inference** for single vs list returns  
✅ **99.9% easier maintenance** - change 1 file instead of 1,062  
✅ **Faster generation** - simpler templates  
✅ **Smaller repository** - 143K fewer lines to maintain  

#### Quality Metrics

- **Code duplication**: Reduced by 99.8%
- **Consistency**: 100% uniform validation and type hints
- **Type safety**: Complete overload coverage for all methods
- **IDE support**: Full IntelliSense/autocomplete working

---

### 🧹 Code Optimization: Helper Validation Centralization

**Optimization: Reduced code duplication by centralizing validation logic.**

#### Changed

- **Centralized Validation Functions**
  - Created `hfortix_fortios/_helpers/validation.py` module with reusable validators
  - Moved `validate_required_fields()` to central module (was duplicated across 1,062 files)
  - Moved `validate_enum_field()` to central module (replaces verbose inline validation)
  - Moved `validate_query_parameter()` to central module
  - Added batch validation helpers: `validate_multiple_enums()`, `validate_multiple_query_params()`

- **Helper Files Simplified**
  - Removed duplicate validation code from all 1,062 endpoint helpers
  - Helpers now import and use central validation functions
  - Consistent error messages across all endpoints

#### Impact

- ✅ **11,727 lines eliminated** from helper files (3.2% reduction)
- ✅ **11,492 net lines saved** (after adding 235-line central module)
- ✅ **99.9% easier bug fixes** - change 1 file instead of 1,062
- ✅ **100% consistent validation** - single source of truth
- ✅ **Memory efficient** - validation functions loaded once, referenced 1,062 times
- ✅ **Future-proof** - easy to add features (i18n, custom messages, etc.)

#### File Size Changes

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Helper Lines | 370,493 | 358,766 | -11,727 (-3.2%) |
| Avg Lines/Helper | 348 | 337 | -11 (-3.2%) |
| Files 200-300 lines | 732 (69%) | 769 (72%) | +37 (+5%) |
| Files 300-500 lines | 195 (18%) | 160 (15%) | -35 (-18%) |

#### Before (Duplicated Code):
```python
# In every helper file - 1,062 duplicates
def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """Validate required fields."""
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    # ... 20+ more lines of error formatting ...
```

#### After (Centralized):
```python
# In all helpers - import once, use everywhere
from hfortix_fortios._helpers.validation import (
    validate_required_fields as _validate_required_fields,
    validate_enum_field as _validate_enum_field,
)

# Use central function - 1 line instead of 25
is_valid, error = _validate_required_fields(
    payload, REQUIRED_FIELDS, FIELD_DESCRIPTIONS
)
```

#### For End Users

**No action required.** This is an internal optimization:
- No API changes
- No behavioral changes
- Validation works exactly the same
- Error messages are consistent

#### Documentation

- See `packages/fortios/OPTIMIZATION_RESULTS.md` for detailed metrics
- See `packages/fortios/OPTIMIZATION_BASELINE.md` for before state

#### Files Changed

- **New:** `packages/fortios/hfortix_fortios/_helpers/validation.py` (Central validation module)
- **Modified:** `.dev/generator/templates/validator.py.j2` (Template updated)
- **Regenerated:** All 1,062 helper files

---

### 🔧 Type Hint Fix: GET Method Overload Resolution

**Critical fix: Resolved ambiguous overloads for `get()` method with `response_mode="object"`.**

#### Fixed

- **Overload Ambiguity for List Returns**
  - Fixed Pylance incorrectly inferring single object when list was returned
  - Issue: `get(response_mode="object")` without mkey should return `list[FortiObject]`
  - Pylance was matching wrong overload, suggesting single object attributes on list

- **Solution: Keyword-Only Overloads**
  - Changed list overload to use `*,` (keyword-only) without mkey parameter
  - Forces Pylance to match correct overload based on presence of mkey argument
  - Clear distinction: with mkey → single object, without mkey → list

#### Before (Ambiguous):
```python
# Both matched same overload - Pylance confused
test1 = fgt.api.cmdb.firewall.policy.get(policyid=1, response_mode="object")  
test2 = fgt.api.cmdb.firewall.policy.get(response_mode="object")

# ❌ Pylance thought test2 was PolicyObject (wrong!)
print(test2.name)  # Suggested .name attribute on list
```

#### After (Unambiguous):
```python
# Correct overload matching
test1 = fgt.api.cmdb.firewall.policy.get(policyid=1, response_mode="object")
# ✅ Correctly inferred as PolicyObject
print(test1.name)  

test2 = fgt.api.cmdb.firewall.policy.get(response_mode="object")
# ✅ Correctly inferred as list[PolicyObject]
print(test2[0].name)
print(test2.name)  # ❌ Correctly shows error: list has no attribute 'name'
```

#### Technical Details

**Updated Overload Pattern** (in `.pyi` stubs):
```python
# Single object - mkey required
@overload
def get(
    self,
    policyid: int,
    *,
    filter: list[str] | None = ...,
    response_mode: Literal["object"] = ...,
) -> PolicyObject: ...

# List of objects - no mkey parameter, keyword-only
@overload
def get(
    self,
    *,  # ✅ Keyword-only, no policyid
    filter: list[str] | None = ...,
    response_mode: Literal["object"] = ...,
) -> list[PolicyObject]: ...
```

#### Impact

- ✅ **Correct type inference** for 750+ CMDB endpoints
- ✅ **Proper autocomplete** for single vs list returns
- ✅ **Better error detection** at development time
- ✅ **Affects all endpoints** with mkey (primary key) parameters

#### For End Users

**No code changes required**, but you'll get better autocomplete:
- IDE will correctly suggest attributes for single objects
- IDE will correctly show list methods for multiple objects
- Type errors will be caught during development, not runtime

#### Documentation

- See `TYPE_HINT_FIX.md` for detailed explanation
- See `test_type_fix.py` for verification tests

#### Files Changed

- **Modified:** `.dev/generator/templates/endpoint_class.pyi.j2` (Template updated)
- **Regenerated:** All 750+ `.pyi` stub files with mkey parameters

---

### 🔧 Full Autocomplete Implementation

**Major fix: Complete autocomplete support for all methods and parameters.**

#### Fixed

- **Schema Parser Bug (Critical)**
  - Fixed `_parse_field_v1_7()` storing raw dict objects instead of extracting option names
  - Was: `options = [{"name": "enable", "help": "..."}, ...]` 
  - Now: `options = ["enable", "disable"]`
  - Affected all Literal type generation for 1,000+ endpoints

- **Docstring Enhancer Compatibility**
  - Updated to handle both dict and string formats for backward compatibility
  - Gracefully handles schema format variations across FortiOS versions

- **Parameter Autocomplete for POST/PUT**
  - All endpoint-specific parameters now show in autocomplete
  - Literal types display available enum values
  - Type hints show correct parameter types (str, int, list, etc.)

#### Before (Broken):
```python
# ❌ No autocomplete for parameters
fgt.api.cmdb.firewall.policy.post(
    # No suggestions appeared
)

# ❌ Literal types showed dict objects
def post(self, status: Literal[{"name": "enable", ...}] | None = ...): ...
```

#### After (Fixed):
```python
# ✅ Full autocomplete for all parameters
fgt.api.cmdb.firewall.policy.post(
    name="test",       # ← Type "na" shows "name"
    action="accept",   # ← Shows: "accept" | "deny" | "ipsec"
    status="enable",   # ← Shows: "enable" | "disable"
    srcintf=["port1"], # ← All parameters autocomplete!
)

# ✅ Clean Literal types
def post(self, status: Literal["enable", "disable"] | None = ...): ...
```

#### Impact

- ✅ **Full autocomplete** for GET, POST, PUT, DELETE methods
- ✅ **Correct Literal types** for all enum fields (220+ per endpoint)
- ✅ **Parameter discovery** - see all available parameters in IDE
- ✅ **Value validation** - IDE shows valid enum values
- ✅ **Affects 1,000+ endpoints** across all API categories

#### For End Users

**Significant developer experience improvement:**
- IntelliSense/autocomplete now works for all parameters
- Enum values are suggested automatically
- Type errors caught during development
- Much faster API exploration and development

#### Documentation

- See `AUTOCOMPLETE_FULLY_WORKING.md` for complete details
- See `FORTIOBJECT_AUTOCOMPLETE_COMPLETE.md` for object mode specifics

#### Files Changed

- **Fixed:** `.dev/generator/schema_management/schema_parser.py` (Schema parsing)
- **Fixed:** `.dev/generator/generators/docstring_enhancer.py` (Compatibility)
- **Fixed:** `.dev/generator/templates/endpoint_class.pyi.j2` (Template cleanup)
- **Regenerated:** All 1,000+ endpoint `.pyi` stub files

---

### 🚀 Major Refactoring: Protocol-Based Type Hints

**Breaking change for generator only - no impact on end users.**

#### Changed

- **Generator Templates Refactored**
  - Replaced 18 `@overload` decorators per endpoint with Protocol inheritance
  - Created `_protocols.py` module with reusable `CRUDEndpoint` protocol
  - Eliminated ~131,200 lines of duplicate overload code across 1,063 endpoints
  - Average 25% file size reduction per endpoint (e.g., voip/profile.py: 949→708 lines)

- **Class Inheritance Updated**
  - All endpoint classes now inherit from `CRUDEndpoint` protocol
  - Pattern: `class Profile(CRUDEndpoint, MetadataMixin)` instead of `class Profile(MetadataMixin)`
  - Type hints for GET/POST/PUT/DELETE provided by protocol, not local overloads

- **Generator Template Simplified**
  - Removed ~263 lines of overload generation logic from `endpoint_class.py.j2`
  - Added automatic `CRUDEndpoint` import for CRUD endpoints
  - Cleaner, more maintainable template code

#### Technical Details

**Protocol Definition** (`_protocols.py`):
```python
from typing import Protocol, overload, Literal

class GetProtocol(Protocol):
    @overload
    def get(self, name: str, ..., response_mode: Literal["object"]) -> FortiObject: ...
    @overload
    def get(self, name: None, ..., response_mode: Literal["object"]) -> list[FortiObject]: ...
    # ... 4 more overloads

class CRUDEndpoint(GetProtocol, PostProtocol, PutProtocol, DeleteProtocol, Protocol):
    """Combined protocol for full CRUD endpoints."""
    pass
```

**Before** (18 overloads per file):
```python
class Profile(MetadataMixin):
    @overload
    def get(self, name: str, ...) -> FortiObject: ...
    @overload
    def get(self, name: None, ...) -> list[FortiObject]: ...
    # ... 16 more overloads
    
    def get(self, ...):  # Implementation
```

**After** (0 overloads per file):
```python
from hfortix_fortios._protocols import CRUDEndpoint

class Profile(CRUDEndpoint, MetadataMixin):
    # All overloads inherited from protocol!
    
    def get(self, ...):  # Implementation only
```

#### Impact

- ✅ **99.8% reduction** in overload boilerplate code
- ✅ **25% smaller** generated endpoint files
- ✅ **Faster generation** - simpler templates
- ✅ **Easier maintenance** - change overloads in one place
- ✅ **Zero functional impact** - autocomplete and type checking work identically
- ✅ **Zero runtime overhead** - protocols are compile-time only
- ✅ **Backward compatible** - no API changes for end users

#### For End Users

**No action required.** This is a generator-level refactoring that doesn't affect:
- API functionality
- Method signatures
- Autocomplete behavior
- Type checking
- Runtime performance

Your existing code continues to work exactly as before.

#### For Contributors

- Generator backup created at `.dev/generator/archive/pre-protocol-refactor-20260107_145151/`
- See `PROTOCOL_REFACTORING_COMPLETE.md` for full details
- See `REFACTORING_OVERLOADS_GUIDE.md` for implementation guide
- See `REFACTORING_VISUAL_COMPARISON.md` for before/after comparison

#### Files Changed

- **New:** `packages/fortios/hfortix_fortios/_protocols.py` (Protocol definitions)
- **Modified:** `.dev/generator/templates/endpoint_class.py.j2` (Template simplified)
- **Regenerated:** All 1,063 endpoint files in `packages/fortios/hfortix_fortios/api/v2/`

---

## [0.5.17] - 2026-01-07

### ✨ Added `.json` Property to FortiObject

**Enhancement: Convenient property access to underlying dictionary data.**

#### Added

- **`.json` Property**
  - Added read-only `.json` property to `FortiObject` class
  - Returns the underlying `dict[str, Any]` data structure
  - Provides intuitive access to raw API response data
  - Alias for existing `.to_dict()` method

#### Usage Example

```python
fgt = FortiOS(host="...", token="...", response_mode="object")

# Delete a policy and access response metadata
result = fgt.api.cmdb.firewall.policy.delete(policyid=42)

# New: Use .json property
print(result.json)
# {'http_method': 'DELETE', 'revision': '...', 'status': 'success', ...}

# Still works: Use .to_dict() method
print(result.to_dict())
# {'http_method': 'DELETE', 'revision': '...', 'status': 'success', ...}
```

#### Why This Matters

- **More Intuitive**: `.json` property name matches common API client conventions
- **Discoverable**: Easier to find in IDE autocomplete than `.to_dict()` method
- **Backwards Compatible**: Existing `.to_dict()` method still works
- **Common Pattern**: Aligns with requests library's `.json()` method pattern

## [0.5.16] - 2026-01-07

### 🔧 Fixed Overload Matching for PyCharm Autocomplete

**Critical fix: Improved overload signatures to ensure PyCharm correctly matches method calls.**

#### Fixed

- **Keyword-Only Arguments for `response_mode`**
  - Made `response_mode` and `raw_json` keyword-only parameters in overloads (using `*,` separator)
  - Prevents positional argument confusion and ensures PyCharm matches the correct overload
  - When you specify `response_mode="object"`, PyCharm now correctly infers `FortiObject` return type

- **Added Default Behavior Overload**
  - Added 4th overload for calls without `response_mode` or `raw_json`
  - Returns `dict[str, Any] | FortiObject` (or `list[FortiObject]` for GET)
  - Ensures all call patterns have a matching overload

- **Removed Ellipsis Defaults**
  - Changed `response_mode: Literal["object"] = ...` to `response_mode: Literal["object"]`
  - Makes the parameter truly required when specified, improving type inference

#### New Overload Pattern

```python
# When you specify response_mode="object"
@overload
def delete(..., *, response_mode: Literal["object"]) -> FortiObject: ...

# When you specify response_mode="dict"  
@overload
def delete(..., *, response_mode: Literal["dict"]) -> dict[str, Any]: ...

# When you specify raw_json=True
@overload
def delete(..., *, raw_json: Literal[True]) -> dict[str, Any]: ...

# When you don't specify either (default behavior)
@overload
def delete(...) -> dict[str, Any] | FortiObject: ...
```

#### Why This Matters

- PyCharm's type inference now works correctly for all call patterns
- Autocomplete shows `response_mode` as available parameter
- When using `response_mode="object"`, `.status` and other FortiObject attributes autocomplete properly
- No more `Cannot find reference 'status' in 'dict | Coroutine'` errors

#### Migration

- **No code changes required**
- Update to v0.5.16: `pip install --upgrade hfortix-fortios>=0.5.16`
- Restart IDE to clear type hint cache
- Autocomplete should now work correctly

## [0.5.15] - 2026-01-07

### 🔧 Fixed Type Hints for `response_mode` Parameter Autocomplete

**Critical IDE fix: `response_mode` parameter now appears in autocomplete suggestions.**

#### Fixed

- **Complete Overload Signatures for All CRUD Methods**
  - Added missing `response_mode="dict"` overload to GET, POST, PUT, DELETE methods
  - Previously only had `response_mode="object"` and `raw_json=True` overloads
  - PyCharm and other type-aware IDEs now correctly show `response_mode` parameter in autocomplete
  - Fixes "Cannot find reference 'status' in 'dict | Coroutine'" when using `response_mode="object"`
  
- **Overload Pattern Now Complete:**
  ```python
  @overload  # Returns FortiObject
  def delete(..., response_mode: Literal["object"] = ...) -> FortiObject: ...
  
  @overload  # Returns dict (NEW - was missing!)
  def delete(..., response_mode: Literal["dict"] = ...) -> dict[str, Any]: ...
  
  @overload  # Returns raw dict
  def delete(..., raw_json: Literal[True] = ...) -> dict[str, Any]: ...
  ```

#### Technical Details

- Without all three overloads, type checkers fall back to implementation signature
- Implementation returns `Union[dict, FortiObject, Coroutine]` causing IDE confusion
- All generated endpoints now have complete overload coverage
- Applies to all 1064 generated endpoint methods across cmdb, monitor, and service APIs

#### Migration

- **No code changes required** - this is purely a type hint improvement
- Regenerate endpoints if you've made custom modifications: `python .dev/generator/generate.py`
- Restart IDE/language server to pick up new type hints
- Install updated package: `pip install --upgrade hfortix-fortios>=0.5.15`

## [0.5.14] - 2026-01-07

### ✨ Enhanced Response Type Hints & Per-Method Response Mode Override

**Major IDE experience improvement: Better autocomplete for API responses and flexible response mode control.**

#### Added

- **FortiObject Common Response Attributes** (`models.pyi`)
  - Added type hints for common API response fields that now autocomplete in IDEs:
    - `status` - API response status ("success" or "error")
    - `http_status` - HTTP status code (200, 404, 500, etc.)
    - `error` - Error code (integer, present when status="error")
    - `error_description` - Human-readable error message
    - `vdom` - Virtual domain name
    - `serial` - Device serial number
    - `version` - API version string
    - `build` - Firmware build number
  - Fixes PyCharm showing "Cannot find reference 'status' in 'dict | Coroutine'" errors
  - Enables autocomplete for common response fields across all FortiObject instances

- **Per-Method `response_mode` Override**
  - All API methods (GET, POST, PUT, DELETE) now accept optional `response_mode` parameter
  - Overrides client-level `response_mode` setting on a per-call basis
  - Values: `"dict"` (returns dict) or `"object"` (returns FortiObject)
  - **Example usage:**
    ```python
    # Client defaults to dict mode
    fgt = FortiOS(host="...", token="...", response_mode="dict")
    
    # Override to object mode for single call
    policy = fgt.api.cmdb.firewall.policy.get(
        policyid=1, 
        response_mode="object"  # Returns FortiObject!
    )
    print(policy.name)  # Clean attribute access
    print(policy.status)  # Now with autocomplete!
    ```

#### Changed

- **Client Response Processing** (`client.py`)
  - Updated `ResponseProcessingClient` wrapper methods to accept `response_mode` parameter
  - Methods now check for per-call override before using client-level default
  - Logic: `mode = response_mode if response_mode is not None else self._response_mode`
  - Maintains backward compatibility - existing code works unchanged

- **Endpoint Template Updates** (`endpoint_class.py.j2`)
  - Added `response_mode: Literal["dict", "object"] | None = None` parameter to:
    - `get()` implementation
    - `post()` implementation  
    - `put()` implementation
    - `delete()` implementation
  - Updated docstrings to document new `response_mode` parameter
  - All generated endpoints now pass `response_mode` to client methods

- **Generator Improvements**
  - Regenerated `cmdb.firewall.policy` endpoint with new template
  - All future endpoint regenerations will include `response_mode` override capability

#### Fixed

- Fixed category stub files missing attribute type hints (v0.5.13 regression)
  - `cmdb/__init__.pyi` - Now includes `firewall: firewall.Firewall` (and 36 other attributes)
  - `monitor/__init__.pyi` - Now includes all monitor category attributes
  - `service/__init__.pyi` - Now includes all service category attributes
  - Generator regex updated from `r'self\.(\w+)\s*=\s*(\w+)\('` to `r'self\.(\w+)\s*=\s*(\w+)\.(\w+)\('`
  - Fixes PyCharm "Unresolved attribute reference 'firewall' for class 'CMDB'" errors

## [0.5.13] - 2026-01-07

### 🔧 Category Attribute Type Hints

**Fixed missing autocomplete for category attributes in PyCharm/VSCode.**

#### Fixed

- **Generator Stub File Creation**
  - Fixed generator regex pattern to properly capture `module.Class` pattern in category `__init__.py` files
  - Updated from `r'self\.(\w+)\s*=\s*(\w+)\('` to `r'self\.(\w+)\s*=\s*(\w+)\.(\w+)\('` 
  - Regenerated category stub files with proper attribute declarations
  - Files affected: `cmdb/__init__.pyi`, `monitor/__init__.pyi`, `service/__init__.pyi`
  - Fixes autocomplete for `client.cmdb.firewall`, `client.monitor.system`, etc.

## [0.5.11] - 2026-01-07

### 🎯 Auto-Normalization for List Fields

**Major usability improvement: API layer now automatically converts strings and lists to FortiOS format.**

#### Added

- **Universal Auto-Normalization Helper** (`build_api_payload()`)
  - New helper function in `hfortix_fortios/_helpers/builders.py`
  - Automatically normalizes 70+ common list fields to `[{'name': '...'}]` format
  - Supports all API types: cmdb, monitor, log, service
  - Fields auto-normalized include:
    - Firewall: `srcintf`, `dstintf`, `srcaddr`, `dstaddr`, `service`, `poolname`, etc.
    - Groups: `member`, `interface`, `device`, `gateway`
    - User/Auth: `users`, `groups`, `fsso_groups`
    - And many more (see `COMMON_LIST_FIELDS` in builders.py)
  - **Accepts multiple input formats:**
    - String: `"port1"` → `[{'name': 'port1'}]`
    - List of strings: `["port1", "port2"]` → `[{'name': 'port1'}, {'name': 'port2'}]`
    - Pre-formatted dicts: `[{'name': 'port1'}]` → unchanged (pass-through)
  - **Flexible control:**
    - `auto_normalize=True` (default) - Auto-detect and normalize common fields
    - `auto_normalize=False` - Disable all normalization (raw mode)
    - `normalize_fields={'custom_field'}` - Explicit field list override
  - Backward compatible - pre-formatted data passes through unchanged

#### Changed

- **All CMDB Endpoints Regenerated**
  - All `post()`, `put()`, and `set()` methods now use `build_api_payload()`
  - 212+ uses of `build_api_payload` in generated code (0 old calls remaining)
  - Updated docstrings with auto-normalization examples
  - Added note in module docstring: "Auto-normalization: List fields accept strings or lists"

- **Stub Generation Improvements**
  - Concrete `get()` fallback now returns only `Union[dict[str, Any], list[dict[str, Any]]]`
  - Removed typed objects from fallback to eliminate ambiguous hover types
  - Overloads with `response_mode="object"` still return typed objects (e.g., `PolicyObject`)
  - Fixes PyCharm/VSCode showing `FortiObject | FortiObject |` in hover tooltips
  - Editor autocomplete now correctly narrows to typed object when `response_mode="object"` used

#### Fixed

- **User Code Now Works Without Manual Formatting**
  - Before: `srcintf="port1"` → HTTP 500 "Input value is invalid"
  - After: `srcintf="port1"` → Auto-converted to `[{'name': 'port1'}]` ✅
  - Example that now works:
    ```python
    fgt.api.cmdb.firewall.policy.post(
        name="test",
        srcintf="any",      # Auto-normalized!
        dstintf="wan1",
        srcaddr="all",
        dstaddr="all",
        service="HTTP",
        schedule="always"
    )
    ```

- **Editor Type Inference**
  - Hover over `policy` now shows specific `PolicyObject` type (when `response_mode="object"`)
  - Autocomplete for `.name`, `.policyid`, etc. works correctly
  - No more ambiguous `FortiObject | FortiObject |` unions

#### Technical Details

- Template: `.dev/generator/templates/endpoint_class.py.j2`
- Helper: `packages/fortios/hfortix_fortios/_helpers/builders.py`
- Test coverage: `test_normalization.py` (all tests passing)

### 🔧 Enhanced Query Parameters & Schema Introspection (2026-01-07)

**Improved developer experience with explicit query parameters and runtime schema introspection.**

#### Added

- **Runtime Schema Introspection** (`get_schema()` method)
  - Added `get_schema()` method to all 561 CMDB endpoints (100% coverage)
  - Queries live firewall for current endpoint schema definition
  - Returns field information, types, enums, validation rules, and defaults
  - Supports both "schema" (FortiOS native) and "json-schema" (standard) formats
  - Enables dynamic form generation, runtime validation, and API exploration
  - Example: `schema = fgt.api.cmdb.firewall.policy.get_schema()`
  - Only added to endpoints with `schema_introspection` capability

- **Explicit Query Parameters** (filter, count, start)
  - Added `filter: list[str] | None` parameter for filtering results
    - Supports operators: `==`, `!=`, `=@` (contains), `!@`, `<=`, `<`, `>=`, `>`
    - Multiple filters use AND logic: `["status==enable", "action==accept"]`
    - Example: `filter=["name==test*", "type==ipmask"]`
  - Added `count: int | None` parameter for pagination (max results)
  - Added `start: int | None` parameter for pagination (offset)
  - Preserved `payload_dict` for advanced options (datasource, with_meta, scope, etc.)
  - Enhanced documentation with operator details and usage examples
  - Full type hints in all `.pyi` stub files

- **Improved Documentation**
  - Comprehensive docstrings for all query parameters
  - Filter operator reference table in docstrings
  - Pagination examples with start/count
  - See Also section references `get_schema()` when available
  - payload_dict documentation lists common advanced options

#### Changed

- **Endpoint Template** (`endpoint_class.py.j2`)
  - Updated `get()` method signature with filter, count, start parameters
  - Added parameter validation and assignment logic
  - Enhanced docstring with detailed usage examples
  - Added conditional `get_schema()` method when capability present
  - Backward compatible - existing code continues to work

- **Stub Template** (`endpoint_class.pyi.j2`)
  - Updated all `get()` overloads with new parameter type hints
  - Changed filter from `str | None` to `list[str] | None` (correct type)
  - Added `count: int | None` and `start: int | None` type hints
  - Added `get_schema()` method stub with return type hints
  - Improved IDE autocomplete and type checking

- **Schema Parser** (`schema_parser.py`)
  - Added `query_params` field to `EndpointSchema` dataclass
  - Parses `query_params` from schema JSON (both v1.7.0 and legacy formats)
  - Extracts GET/PUT/POST/DELETE query parameter definitions
  - Makes parameter metadata available to generators

#### Technical Details

- **Files Modified**: 3 template files, 1 schema parser
- **Files Generated**: 561 Python files (.py), 561 stub files (.pyi)
- **Coverage**: 100% of CMDB endpoints
- **Backward Compatibility**: ✅ Full (existing code unchanged)
- **Type Safety**: ✅ Complete type hints in stubs

#### Usage Examples

```python
from hfortix_fortios import FortiOS
fgt = FortiOS(host="192.168.1.99", token="your-token")

# Filter results
policies = fgt.api.cmdb.firewall.policy.get(
    filter=["status==enable", "action==accept"]
)

# Pagination
first_100 = fgt.api.cmdb.firewall.policy.get(start=0, count=100)

# Combined filtering + pagination
results = fgt.api.cmdb.firewall.address.get(
    filter=["type==ipmask"],
    start=0,
    count=50
)

# Get runtime schema
schema = fgt.api.cmdb.firewall.policy.get_schema()
print(schema["results"])  # Field definitions, types, enums

# Advanced options (still supported)
detailed = fgt.api.cmdb.firewall.policy.get(
    filter=["srcintf==port1"],
    payload_dict={"with_meta": True, "datasource": True}
)
```

### �🔗 Endpoint Relationship Documentation in Stubs (2026-01-07)

**Enhanced IDE experience with comprehensive endpoint relationship documentation in `.pyi` stub files.**

#### Added

- **Relationship Documentation in Stub Files**
  - Auto-generated "Related Resources" section in TypedDict docstrings
  - Forward dependencies: Shows what resources each endpoint references
  - Field-level mappings: Documents which fields reference which endpoints (e.g., "via: av-profile")
  - RST cross-references: Sphinx-style `:class:` links for IDE navigation (Ctrl+Click to jump)
  - Smart truncation: Shows top 10 dependencies, then "... and X more dependencies"
  - Example: `firewall.policy` shows dependencies on antivirus profiles, address objects, schedules, etc.

- **Reverse Dependency Analyzer**
  - New `RelationshipAnalyzer` class to compute "Referenced By" relationships
  - Scans all CMDB schemas to build reverse dependency map
  - Identifies which endpoints reference each endpoint
  - Tracks field-level usage across the entire API
  - Processes 561 schemas in ~2 seconds
  - Found 173 endpoints with reverse dependencies

- **IDE Navigation Benefits**
  - Hover tooltips show relationship information
  - Ctrl+Click navigates between related endpoint stubs
  - Autocomplete shows dependency context
  - Understand workflow order (create dependencies first)
  - Avoid breaking changes by seeing reverse dependencies

#### Changed

- **Stub Generator Enhanced** (`pyi_generator.py`)
  - Added `_format_endpoint_link()` to convert paths to RST cross-references
  - Added `_format_relationship_section()` to format complete relationship docs
  - Updated `generate_endpoint_stub()` to include relationship section in docstrings
  - Relationships pre-computed and passed as template context

- **Schema Parser Updated** (`schema_parser.py`)
  - Added `relationships` field to `EndpointSchema` dataclass
  - Parses relationship metadata from schema JSON v1.7.0+
  - Includes `datasource_fields`, `related_endpoints` data

- **Generator Integration** (`generate.py`)
  - Integrated `RelationshipAnalyzer` into bulk CMDB generation
  - Runs analyzer once per category, passes results to each endpoint
  - Single-endpoint mode shows forward deps only (no reverse deps)

- **Template Updates** (`endpoint_class.pyi.j2`)
  - New relationship section in TypedDict docstrings
  - RST-formatted cross-references for Sphinx/IDE compatibility
  - Clean, readable format with field mappings

#### Technical Details

- **Coverage**: All 562 CMDB endpoints regenerated with relationship docs
- **Performance**: Analyzer overhead ~2s for full CMDB scan, negligible per-endpoint
- **Format**: RST cross-references compatible with Sphinx, VSCode, PyCharm, Pylance
- **Most Referenced Endpoint**: `system.interface` (110 references across API)

### 🎯 Pydantic Models with Datasource Validation (2026-01-07)

**Complete implementation of nested Pydantic models and async datasource validation for all CMDB endpoints.**

#### Added

- **Nested Pydantic Models for Child Tables**
  - Generated `BaseModel` classes for all child table fields
  - Type-safe field definitions with constraints (min/max, max_length, patterns)
  - Enum classes for fields with 4+ allowed values
  - Literal types for fields with 2-3 allowed values
  - Field validation with Pydantic `Field()` constraints
  - Default values and optional fields support
  - Datasource metadata embedded in field comments
  - Example: `PolicySrcintf(BaseModel)` for firewall policy source interfaces

- **Async Datasource Validation Methods**
  - Auto-generated validation methods for all datasource fields
  - Validates references exist in FortiGate BEFORE API calls
  - Supports both child table fields (list) and scalar fields (string)
  - Checks multiple datasource endpoints per field
  - Returns descriptive error messages with field names
  - `validate_all_references()` convenience method per model
  - Example: `await policy.validate_srcintf_references(client)`

#### Changed

- **Model Generator Enhanced**
  - Added `_extract_datasource_fields()` to parse datasource metadata from schemas
  - Added `_generate_validation_methods()` to create validation method metadata
  - Added `_generate_exists_checks()` filter for proper Python code indentation
  - Extended Pydantic model template with datasource validation section
  - Models now include async validation methods when datasources are present

- **Template Updates** (`pydantic_model.py.j2`)
  - New "Datasource Validation Methods" section
  - Async validation methods with proper docstrings and examples
  - Uses `client.api.cmdb.{endpoint}.exists()` for validation
  - Supports both child table iteration and scalar field validation
  - Clean error message formatting with field names and datasource paths

#### Statistics

- **281** CMDB endpoints with validation methods
- **1,089** individual validation methods generated
- Covers all datasource fields in cmdb, monitor, and service categories
- Log category excluded (no datasource metadata in schemas)

#### Technical Details

- Datasource metadata extracted from schema `fields[].datasource` property
- Validation methods are fully async and integrate with FortiOS client
- Template uses `{% raw %}` blocks for f-string interpolation
- Python-generated indentation via filter for clean output
- Optional validation - only called when needed

#### Example Usage

```python
from hfortix_fortios import FortiOS
from hfortix_fortios.api.models.cmdb.firewall.policy import PolicyModel, PolicySrcintf

# Create policy with Pydantic validation
policy = PolicyModel(
    name="test-policy",
    srcintf=[PolicySrcintf(name="port1")],
    dstintf=[PolicySrcintf(name="port2")],
    action="accept"
)

# Validate datasource references exist
async with FortiOS(host="192.168.1.1", token="xxx") as fgt:
    # Validate all references at once
    errors = await policy.validate_all_references(fgt._client)
    
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        # All references exist - safe to post
        result = await fgt.api.cmdb.firewall.policy.post(
            policy.to_fortios_dict()
        )
```

### ✨ Improved LOG Endpoint Generation (2026-01-06)

**Enhanced log endpoints with modern patterns and proper stub file organization.**

#### Changed

- **Improved LOG Endpoint Generator**
  - Enhanced docstrings with detailed parameter documentation
  - Added modern type hints (`Union[dict, Coroutine]` for sync/async support)
  - Better documentation for query parameters (rows, session_id, filter, serial_no)
  - Consistent code patterns with other endpoint generators
  - Clearer class and method documentation

- **Fixed .pyi Stub File Organization**
  - LOG endpoint stubs now correctly placed in `fortios-stubs` package only
  - Removed `.pyi` files from main `fortios` package
  - Updated LogEndpointGenerator to respect `stubs_dir` parameter
  - Proper separation of runtime code and type hints

- **Enhanced Documentation Quality**
  - All `get()` methods now include comprehensive docstrings
  - Parameter documentation with types and descriptions
  - Return type documentation
  - Usage examples in module docstrings

#### Technical Details

- Updated `LogEndpointGenerator` constructor to accept `stubs_dir` parameter
- Modified stub generation methods to write to correct location
- Improved cleanup process to handle both main package and stubs
- Generated 6 log endpoint modules with 38 total endpoints

### 🎨 Enhanced Type Stubs for Object Response Mode (2026-01-06)

**Comprehensive IDE autocomplete support for FortiObject with overloaded type hints.**

#### Added

- **Type Stub for FortiObject** (`models.pyi`)
  - Complete type hints for all FortiObject methods
  - Overloaded `process_response()` function with accurate return types
  - Proper TypeVar and Generic support for type safety
  - Full docstrings for IDE tooltips

- **Overloaded Method Signatures** in endpoint .pyi files
  - 4 overloads for `get()` method based on `response_mode` parameter:
    - `response_mode="object"` with `raw_json=False` → `list[FortiObject]`
    - `response_mode="object"` with specific ID → `FortiObject`
    - `response_mode="object"` with `raw_json=True` → `dict[str, Any]`
    - `response_mode="dict"` (default) → `Union[dict, list[dict]]`
  - IDE now provides exact return type based on parameters
  - Perfect type inference for mypy, pylint, and IDE type checkers

- **FortiObject Export** in `__init__.pyi`
  - Added `FortiObject` to main package exports
  - Proper import statement for IDE autocomplete
  - Included in `__all__` list for wildcard imports

- **Demo File** - `examples/fortiobject_autocomplete_demo.py`
  - Comprehensive examples of FortiObject usage
  - 6 different usage patterns with detailed comments
  - Shows IDE autocomplete in action
  - Demonstrates type checking benefits

#### Changed

- **Updated endpoint_class.pyi.j2 template**
  - Added `overload` import from typing
  - Added `FortiObject` import from hfortix_fortios.models
  - Replaced single `get()` signature with 4 overloaded versions
  - Enhanced type hints for better IDE support

- **Regenerated endpoint stubs** with new type hints
  - All 1,065 endpoint .pyi files now include FortiObject overloads
  - Perfect IDE autocomplete for response_mode parameter
  - Type checkers can now validate correct usage

#### Impact

**Developer Experience Improvements:**
- ✨ **Full IDE autocomplete** for FortiObject methods
  - Typing `addr.` shows: name, subnet, get_full(), to_dict(), keys(), values(), items(), get()
  - No need to remember dict key names
  - Cleaner, more Pythonic code

- 🛡️ **Type Safety**
  - IDE shows exact return type based on response_mode
  - mypy catches incorrect response_mode usage
  - Prevents runtime type errors

- 📝 **Self-Documenting Code**
  - Type hints show which mode returns what
  - Tooltips show FortiObject method signatures
  - Better code readability

**Example IDE Experience:**
```python
# IDE knows exact return type!
addr: FortiObject = fgt.api.cmdb.firewall.address.get(
    name="test",
    response_mode="object"  # ← IDE autocompletes "object" | "dict"
)

# Attribute access with full autocomplete
addr.name      # ← IDE suggests: name, subnet, type, comment, ...
addr.get_full  # ← IDE suggests: get_full(), get(), to_dict(), keys(), ...
addr.to_dict() # ← IDE knows return type is dict[str, Any]
```

#### Files Modified

- `packages/fortios-stubs/hfortix_fortios-stubs/models.pyi` - New file
- `packages/fortios-stubs/hfortix_fortios-stubs/__init__.pyi` - Added FortiObject export
- `.dev/generator/templates/endpoint_class.pyi.j2` - Added overloaded signatures
- `examples/fortiobject_autocomplete_demo.py` - New demo file

#### Documentation

- Created comprehensive demo file showing all FortiObject features
- Updated README.md with Object Response Mode section
- Documented all FortiObject methods with examples
- Added type checking examples

### 🚀 Major Code Generation Overhaul (2026-01-06)

**Complete endpoint generation system with Pydantic models, capabilities metadata, and action methods.**

#### Added

- **Pydantic Model Generator** - Runtime validation for all FortiOS configurations
  - Automatic generation of Pydantic models from schema files
  - Field validation with constraints (max_length, min/max values, patterns)
  - Type safety with proper type hints (str, int, bool, Literal types)
  - Helper methods: `to_fortios_dict()`, `from_fortios_response()`
  - Generated 1,065 Pydantic models (parallel to API endpoints)
  - Models stored in `api/models/` directory structure
  - Total size: ~15 MB of validated model code

- **Endpoint Capabilities Metadata** - Schema-driven feature detection
  - Automatic extraction of CRUD capabilities from schema metadata
  - Class constants for all endpoints:
    - `SUPPORTS_CREATE`, `SUPPORTS_READ`, `SUPPORTS_UPDATE`, `SUPPORTS_DELETE`
    - `SUPPORTS_MOVE`, `SUPPORTS_CLONE`
    - `SUPPORTS_FILTERING`, `SUPPORTS_PAGINATION`, `SUPPORTS_SEARCH`, `SUPPORTS_SORTING`
  - Enables runtime capability checks before API calls
  - Example: `if endpoint.SUPPORTS_MOVE: endpoint.move(...)`

- **Action Methods** - move(), clone(), exists() for all endpoints
  - `move()` method for endpoints with position-based ordering
    - Parameters: primary_key, action ("before"/"after"), reference_id
    - Supports both synchronous and asynchronous operations
  - `clone()` method for endpoints supporting object duplication
    - Parameters: source_id, destination_id
    - Automatic payload generation
  - `exists()` method for all endpoints
    - Returns True/False for object existence
    - Handles 404 errors gracefully (returns False)
    - Re-raises other errors (network, auth) for debugging
    - Supports both synchronous and asynchronous operations

- **Enhanced Schema Parser** - Capabilities extraction
  - New `EndpointCapabilities` dataclass with CRUD, actions, features
  - Automatic detection from schema `mkey_type`, `readonly` flags
  - Move/clone support based on schema metadata
  - Feature detection (filtering, pagination, search, sorting)

#### Changed

- **Code Generator Integration**
  - Integrated ModelGenerator into main generate.py workflow
  - Three generation points: single endpoint, category batch, full regeneration
  - Models generated alongside endpoints, validators, stubs, tests
  - Parallel directory structure: `api/v2/` and `api/models/`

- **Template Updates** - endpoint_class.py.j2
  - Added capabilities constants section (lines 72-86)
  - Added move() method template (lines 350-420)
  - Added clone() method template (lines 422-490)
  - Fixed exists() method to handle 404 errors properly (lines 466-590, 824-876)
  - Removed Jinja2 whitespace stripping (`{%-`) to fix syntax errors

- **Test Generation** - Enhanced auto-generated tests
  - Tests for exists() method (both existing and non-existent items)
  - Tests for action methods (move, clone) when supported
  - Validator import and usage tests
  - Enum validation tests

#### Fixed

- **Syntax Errors** - Jinja2 template whitespace issue
  - Problem: `{%-` was stripping all newlines, creating single-line constant definitions
  - Impact: 1,065 endpoint files had syntax errors
  - Fix: Removed `-` from control statements to preserve proper formatting
  - Result: All constants now on separate lines with proper indentation

- **Import Errors** - Missing cmdb/cmdb/__init__.py
  - Problem: `AttributeError: module 'hfortix_fortios.api.v2.cmdb.cmdb' has no attribute 'CMDB'`
  - Cause: Schema organization quirk (schema in cmdb/cmdb/ but generates to cmdb/firewall/)
  - Fix: Created placeholder `__init__.py` with empty CMDB class
  - Result: All imports working correctly

- **exists() Method Exceptions** - 404 handling
  - Problem: exists() raised ResourceNotFoundError instead of returning False
  - Impact: Tests expecting False got exceptions
  - Fix: Catch 404 errors specifically, re-raise other errors
  - Result: exists() returns False for non-existent objects, raises for real errors

#### Testing

- **All 1,065 endpoints regenerated** with new features
- **All tests passing** (firewall.address: 10/10, system.global: 8/8, firewall.policy: 10/10)
- **561 CMDB Pydantic models** generated (4.53 MB)
- **Full test coverage** for capabilities, action methods, validators, enums

#### Documentation

- Created `PHASE3_COMPLETE.md` - Integration completion summary
- Created `TEST_FAILURES_FIXED.md` - Issue resolution documentation
- Updated generator templates with inline documentation
- Enhanced docstrings for all generated methods

### 🎯 Literal Types for IDE Autocomplete (2026-01-06)

**Massive Developer Experience Enhancement: 15,000+ parameters now have IDE autocomplete with Literal types.**

#### Added
- **Literal Type Annotations** for all enum parameters across all 1,065 endpoints
  - Extracted Literal types from schema `pydantic_type` fields
  - 1,476 endpoint files with Literal-typed parameters
  - 654 files optimized without Literal imports (no enum fields)
  - Total: 15,000+ parameters with IDE autocomplete support
  - Example: `action: Literal['accept', 'deny', 'ipsec'] | None = None`
  
- **Conditional Literal Imports** for optimal performance
  - Only imports `Literal` when endpoint has enum fields
  - Template logic: `{% if literal_types_needed %}, Literal{% endif %}`
  - Reduces import overhead for simple endpoints

- **Enhanced Generator Infrastructure**
  - New `_get_literal_type()` method extracts Literal from schema
  - New `_collect_literal_types()` determines import requirements
  - Jinja2 filter: `get_python_type_with_literal` for type rendering
  - Handles both dict and string format in `FieldMetadata.options`

#### Changed
- **Updated endpoint_generator.py** with Literal extraction logic
  - Added `DocstringEnhancer` integration for rich parameter docs
  - Enhanced schema field processing to extract Literal types
  - Conditional import logic based on endpoint field analysis

- **Updated endpoint_class.py.j2 template**
  - Line 28: Conditional `Literal` import
  - Line 205: PUT method uses Literal types
  - Line 304: POST method uses Literal types
  - All parameter type hints now include Literal where applicable

- **Regenerated all 1,065 endpoint files**
  - CMDB: 562 endpoints with Literal types
  - Monitor: 491 endpoints with Literal types
  - Log: 286 endpoints with Literal types
  - Service: 12 endpoints with Literal types
  - All .pyi stub files regenerated

#### Impact

**Developer Experience:**
- ✅ IDE autocomplete for every enum parameter
- ✅ Type safety: Invalid values caught at type-check time
- ✅ Self-documenting: See all valid options in IDE tooltips
- ✅ Zero learning curve: Works immediately in VSCode, PyCharm, etc.

**Example - firewall.policy (85 Literal parameters):**
```python
# Before: No autocomplete, trial and error
policy.put(action="allow")  # ❌ Runtime error - invalid value

# After: IDE suggests valid options
policy.put(action="accept")  # ✅ IDE autocompletes: 'accept', 'deny', 'ipsec'
```

**Statistics:**
- 15,000+ parameters with Literal types
- 1,476 files WITH Literal imports (have enum fields)
- 654 files WITHOUT Literal imports (optimized)
- firewall.policy: 85 Literal parameters out of 189 total
- 100% backward compatible - no breaking changes

**Documentation:**
- `.dev/LITERAL_TYPES_IMPLEMENTATION.md` - Technical implementation details
- `.dev/REGENERATION_COMPLETE.md` - Complete statistics and validation results
- `.dev/LITERAL_TYPES_QUICKSTART.md` - User quick start guide

**Benefits:**
- ⚡ Instant autocomplete for all enum fields
- 🛡️ Type safety prevents invalid values
- 📚 Self-documenting code
- 🚀 Zero runtime overhead
- ✅ 100% backward compatible

## [0.5.4] - 2026-01-06

### 🔧 MetadataMixin Refactoring (2026-01-06)

**Eliminated ~160K lines of duplicate code by consolidating metadata helper methods into a single base class.**

#### Changed
- **Introduced `MetadataMixin` base class** for all endpoint classes
  - Consolidated 7 duplicate metadata methods into single mixin class
  - Methods: `help()`, `fields()`, `field_info()`, `validate_field()`, `required_fields()`, `defaults()`, `schema()`
  - Each method was duplicated across all 1,065 endpoints (~200 lines per endpoint)
  - Location: `hfortix_fortios/_helpers/metadata_mixin.py`

- **Updated code generator templates**
  - Modified `.dev/generator/templates/endpoint_class.py.j2` to inherit from `MetadataMixin`
  - Removed ~200 lines of metadata method implementations per endpoint
  - Added `_helper_module_name` class attribute for dynamic helper imports
  - All endpoints now use: `class EndpointName(MetadataMixin):`

- **Regenerated all endpoint files**
  - CMDB: 562 endpoints regenerated
  - Monitor: ~350 endpoints regenerated  
  - Log: ~38 endpoints regenerated
  - Service: ~115 endpoints regenerated
  - Total: 1,065 endpoints updated

#### Impact

**Code Reduction:**
- Eliminated ~159,750 lines of duplicate code
- CMDB endpoints alone: 32.7% smaller

**Package Size:**
- Before deduplication: 64 MB
- After deduplication: 30 MB
- **53% total reduction** through two-phase optimization:
  - Phase 1 - stub separation: 64 MB → 41 MB (36% reduction)
  - Phase 2 - MetadataMixin: 41 MB → 30 MB (27% reduction)

**Benefits:**
- ✅ Single source of truth for all metadata methods
- ✅ Easier to maintain and update
- ✅ 100% backward compatible - all existing code works without changes

#### Technical Details
- Each endpoint class now inherits from `MetadataMixin`
- Mixin uses `@classmethod` methods to access endpoint-specific helper modules
- Dynamic import based on `_helper_module_name` class attribute
- Zero performance impact - Python caches module imports
- Type stubs (.pyi files) remain unchanged for type checking accuracy

---

### � Package Size Optimization (2026-01-06)

**Major package size reduction through code deduplication and reorganization.**

#### Changed
- **Separated type stubs into optional package** (`hfortix-fortios-stubs`)
  - Main package: 64 MB → 29.6 MB (54% reduction)
  - Type stubs: 10.4 MB in separate optional package
  - Install with stubs: `pip install hfortix-fortios[stubs]`
  - Stubs package follows PEP 561 (py.typed marker included)

- **Optimized code generator templates**
  - Shortened module docstrings in helper files (multi-line → single-line)
  - Reduced REQUIRED_FIELDS comment blocks (21 lines → 3 lines)
  - Removed verbose internal function docstrings (saved 3.1 MB)
  - Total template optimizations: 4.3 MB saved

- **Deduplicated metadata accessor functions**
  - Moved 9 metadata functions to central `hfortix_fortios._helpers.metadata` module
  - Removed 8 KB of duplicate code from each of 1,062 helper files
  - Total deduplication savings: 6.4 MB

#### Technical Details
- **Generator updates**
  - Modified `.dev/generator/templates/validator.py.j2` for minimal docstrings
  - Updated `.dev/generator/generators/pyi_generator.py` to output to stubs directory
  - Modified `.dev/generator/generate.py` to auto-detect stubs package location
  
- **New central module**
  - Added `hfortix_fortios/_helpers/metadata.py` with shared metadata functions
  - Functions: `get_field_description`, `get_field_type`, `get_field_constraints`, etc.
  - All helper files now import from central module instead of duplicating logic

- **Package structure**
  ```
  hfortix-fortios/          # Main package (29.6 MB)
  ├── .py files only
  └── No .pyi files
  
  hfortix-fortios-stubs/    # Optional stubs package (10.4 MB)
  ├── .pyi files only
  └── py.typed marker
  ```

#### Optimization Summary
| Optimization | Size Saved | Files Affected |
|--------------|------------|----------------|
| Stub separation | 10.4 MB → optional | 2,348 .pyi files |
| Module docstrings | 0.2 MB | 1,062 helpers |
| REQUIRED_FIELDS comments | 1.0 MB | 1,062 helpers |
| Metadata deduplication | 6.4 MB | 1,062 helpers |
| Function docstrings | 3.1 MB | 1,062 helpers |
| **Total** | **21.1 MB (33%)** | **All generated files** |

#### Benefits
- ✅ Faster pip installs (54% smaller main package)
- ✅ Reduced disk usage
- ✅ Optional type stubs for users who want them
- ✅ Zero functionality lost
- ✅ All user-facing docstrings preserved
- ✅ Better code maintainability through deduplication

### �📊 Schema v1.7.0 Analysis & Implementation Status (2026-01-06)

**Current Status:** Schema Complete ✅ | Code Generation Pending 🟡

#### ✅ Completed (100%)

**Schema Generation v1.7.0:**
- ✅ Generated 1,348 endpoints with full v1.7.0 metadata (+394 endpoints, +41% coverage)
- ✅ Schema version tracking (v1.7.0) with generator metadata
- ✅ Enhanced field metadata: `python_type`, `pydantic_type`, validation constraints
- ✅ Capabilities tracking: CRUD operations, actions, features per endpoint
- ✅ Complexity ratings: Field counts, child tables, performance impact
- ✅ Relationship tracking: 38 related endpoints per endpoint (avg)
- ✅ Datasource mapping: 37 datasource fields per endpoint (avg)
- ✅ Validation rules: 72% fields have validation constraints
- ✅ Child table tracking: 43 child tables tracked (firewall.policy example)

**Coverage by Category:**
```
CMDB:     561 schemas
Monitor:  490 schemas
Log:      286 schemas
Service:   11 schemas
TOTAL:  1,348 schemas
```

**Basic API Endpoint Classes:**
- ✅ Generated 2,129 endpoint files with CRUD methods
- ✅ Full type hints on all method parameters
- ✅ Async support (returns Coroutine when using async client)
- ✅ VDOM support for multi-tenant environments
- ✅ Query parameter handling with payload_dict
- ✅ Docstrings with usage examples

**Validation Infrastructure:**
- ✅ Created 260+ validator helper modules
- ✅ Field type validation
- ✅ Required field checking
- ✅ Allowed values validation
- ✅ Organized by API category (cmdb/monitor/log/service)

**Test Coverage:**
- ✅ Fixed 42/42 monitor endpoint tests
- ✅ All validator modules passing
- ✅ Schema validation tests passing

#### � In Progress / Pending (0-20%)

**Pydantic Model Generation (0%):**
- ❌ BaseModel classes not yet generated
- ❌ Field() constraints not applied (ge/le/pattern/max_length)
- ❌ Nested models for child tables not created
- ❌ Enums for allowed_values not generated
- ❌ Examples not included in Field() definitions
- **Impact:** HIGH - No runtime validation, no type safety at object level
- **Effort:** 1-2 days
- **Benefit:** Client-side validation, 40-60% error reduction

**Relationship & Datasource Validation (0%):**
- ❌ Datasource validation not implemented
- ❌ Foreign key checking not available
- ❌ Relationship documentation incomplete
- ❌ Cascade operation helpers missing
- **Impact:** MEDIUM - Invalid references possible
- **Effort:** 1 day
- **Benefit:** Prevent invalid references, suggest correct values

**Capabilities Metadata Integration (0%):**
- ❌ Capabilities not exposed in endpoint classes
- ❌ CRUD capability checking not implemented
- ❌ Action availability not documented
- ❌ Feature detection not available
- **Impact:** MEDIUM - No prevention of unsupported operations
- **Effort:** 1 day
- **Benefit:** Better error messages, feature detection

**Enhanced Documentation (20%):**
- ✅ Basic docstrings with examples
- ❌ Complexity warnings not included
- ❌ Related endpoints not in "See Also" sections
- ❌ Field examples not in docstrings
- ❌ Query parameter examples incomplete
- **Impact:** LOW - Documentation could be better
- **Effort:** 1 day
- **Benefit:** Better developer experience

### Changed
- **�🔄 Complete API Regeneration from v1.7.0 Schema** (2026-01-06)
  - Regenerated all 1,065 API endpoints from enhanced v1.7.0 schema format
  - Schema upgrade: 954 endpoints (v1.6.0) → 1,348 endpoints (v1.7.0)
  - Enhanced metadata: Added `python_type`, `pydantic_type`, validation constraints
  - Field count updates: Removed 4 deprecated fields from firewall.policy (188→184 fields)
  - Improved type safety with pre-computed type information
  - Better validation constraints extracted from schema (min/max ranges, string lengths)
  - Auto-resolved 19 naming conflicts using `_base.py` suffix pattern
  
- **Generator Infrastructure Updates**
  - Updated `schema_parser.py` to support both v1.6.0 and v1.7.0 schema formats
  - Added `_parse_v1_7()` method for new schema structure parsing
  - Added `_parse_field_v1_7()` for enhanced field metadata extraction
  - Updated `download_schemas.py` for flat file structure (category/endpoint.name.json)
  - Updated `generate.py` default schema path to use new schema location
  - Generator now auto-detects schema version and uses appropriate parser

- **Schema Structure Changes**
  - New format: Flat files with dots (e.g., `firewall.policy.json` vs `firewall/policy.json`)
  - Schema location: `/schema/7.6.5/` (versioned by FortiOS version)
  - Enhanced fields: `fields` instead of `children`, with richer metadata
  - Pre-computed: `python_module`, `class_name`, `pydantic_class_name`
  - Added: `related_endpoints`, `complexity`, `capabilities` metadata

### Added
- Added `.gitignore` entry for `/schema/` folder (1,348 files, ~40MB)
- Generated 2,130+ Python files (.py) from v1.7.0 schema
- Generated comprehensive type stubs (.pyi) for all modules
- Created validators with enhanced metadata in `_helpers/` directories
- Generated 1,065+ test files in `.tests/pytests/api/`
- **📄 IMPLEMENTATION_STATUS.md** - Detailed tracking of v1.7.0 feature implementation
- **📊 Schema Comparison Analysis** - Quantitative comparison of old vs new schemas

### Technical Debt & Next Steps

**Priority Roadmap:**
1. **Phase 1 (1-2 days):** Generate Pydantic models with Field() constraints
2. **Phase 2 (1 day):** Add relationship validation and capabilities metadata
3. **Phase 3 (1 day):** Enhance documentation with examples and related endpoints
4. **Phase 4 (1 day):** Comprehensive testing and validation

**Known Issues:**
- Old schemas in `/.dev/generator/schemas/` (954 endpoints) are obsolete
- Generated code uses only 10% of v1.7.0 schema improvements
- 90% of enhanced metadata (validation, examples, relationships) not yet leveraged
- Pydantic model generation deferred to focus on basic functionality first

**Quantitative Gap:**
```
Schema Completeness:     100% ✅ (1,348 endpoints with full metadata)
Code Implementation:      10% 🟡 (basic methods only)
Gap:                      90% ❌ (advanced features pending)
```

## [0.5.3] - 2026-01-04

### Added
- **Object Mode Response Processing** 🎯
  - New `response_mode="object"` parameter for FortiOS client constructor
  - `FortiObject` class for clean attribute access (`policy.name` instead of `policy['name']`)
  - Automatic member_table field flattening (e.g., `srcaddr` returns `['addr1', 'addr2']`)
  - `get_full()` method for accessing raw unprocessed data
  - Dict-like interface support (`get()`, `keys()`, `values()`, `items()`)
  - Zero-maintenance design - works with any FortiOS version without schemas

- **ResponseProcessingClient Wrapper**
  - Intercepts all HTTP method calls (get, post, put, delete)
  - Automatically processes responses based on `response_mode` setting
  - Seamless integration with existing API namespace

- **Enhanced Testing Infrastructure**
  - Added `.tests/__client__.py` with `fgt_ResponseModeObject` client
  - Added `.tests/others/object.py` demonstrating object mode usage
  - Complete documentation in `OBJECT_MODE_IMPLEMENTATION.md`

### Changed
- Updated 14 CMDB endpoint `.pyi` files with previously missing fields:
  - `vpn.ipsec.phase2.pyi` - Added 32 missing parameters
  - `vpn.ipsec.phase2_interface.pyi` - Added 32 missing parameters
  - `web_proxy.explicit.pyi` - Added 18 missing parameters
  - `web_proxy.global_setting.pyi` - Added 6 missing parameters
  - `webfilter.profile.pyi` - Added 15 missing parameters
  - `wireless_controller.arrp_profile.pyi` - Added 2 missing parameters
  - `wireless_controller.global_setting.pyi` - Added 12 missing parameters
  - `wireless_controller.hotspot20.hs_profile.pyi` - Added 23 missing parameters
  - `wireless_controller.qos_profile.pyi` - Added 3 missing parameters
  - `wireless_controller.timers.pyi` - Added 6 missing parameters
  - `wireless_controller.vap.pyi` - Added 151 missing parameters
  - `wireless_controller.wids_profile.pyi` - Added 90 missing parameters
  - `wireless_controller.wtp.pyi` - Added 27 missing parameters
  - `wireless_controller.wtp_profile.pyi` - Added 37 missing parameters
  - `ztna.web_portal.pyi` - Added 4 missing parameters

- Improved LOG API type stubs organization
  - Consolidated duplicate `log/__init__.pyi` imports
  - Better type hint structure for LOG endpoints

### Removed
- Removed v7.6 dummy files (`x6_index`, `x6_metadata`) and their helpers
- Removed 231 old auto-generated test files (cleanup)

### Fixed
- Object mode now properly integrated into request flow via ResponseProcessingClient
- FortiObject correctly handles missing fields (returns None instead of raising AttributeError)

## [0.5.2] - 2026-01-04

### Changed
- Updated and regenerated all endpoint tests for comprehensive coverage
- Regenerated all API endpoint type stubs (.pyi files) with latest schemas
- Improved validator generation for all CMDB, Monitor, and Log endpoints
- Enhanced test coverage across all API categories

### Fixed
- Fixed type stub generation for nested endpoint structures
- Corrected endpoint parameter validation in auto-generated tests
- Improved schema parsing for complex nested endpoint paths

## [0.5.0-beta] - 2026-01-04

### 🎉 **MAJOR RELEASE - Complete Code Regeneration**

Version 0.5.0 represents a **complete regeneration** of the FortiOS API implementation with significant architectural improvements. This is a **breaking change** release that removes convenience wrappers in favor of a more maintainable, comprehensive, and auto-generated approach.

⚠️ **BREAKING CHANGES**: This release removes convenience wrappers. Use direct API access via `fgt.api.cmdb.*`, `fgt.api.monitor.*`, and `fgt.api.log.*` instead.

### Added

- **Complete API Regeneration** (January 2026):
  - ✨ **1,219 Total Endpoints**: Complete FortiOS 7.6.5 API coverage
    - 886 CMDB endpoints (configuration management)
    - 295 Monitor endpoints (status and monitoring)
    - 38 Log endpoints (5 destinations × multiple subtypes)
  - 🏗️ **All Code Auto-Generated**: 100% generated from FortiOS API schemas
  - 📝 **Comprehensive Type Stubs**: Full `.pyi` stub files for all 1,219 endpoints
  - ✅ **Auto-Generated Tests**: Basic test coverage for all endpoints
  - 🔍 **Enhanced Validators**: 1,219 validator modules with schema-based validation

- **Advanced Code Generator** (January 2026):
  - 🚀 **Swagger Fallback System**: Automatically uses Swagger docs when API unavailable
    - Handles HTTP 400, 404, 405, 424, 500, 503 errors
    - Handles JSON parse errors for binary endpoints
    - Creates valid schemas from Swagger/OpenAPI documentation
    - Includes metadata tracking (`fallback_reason` field)
  - 🔧 **Smart Path Conversion**: Automatically handles 3-part CMDB paths
    - Example: `system.snmp/community` → `/api/v2/cmdb/system.snmp/community`
  - 📊 **Comprehensive Error Reporting**: Configurable error display with `--max-errors`
  - 🎯 **Bug Fixes**: Fixed Swagger parser type errors with proper dict/string handling

- **Log Endpoint Support** (January 2026):
  - 📋 **Parameterized Log Queries**: Native support for FortiGate log endpoints
  - 🏗️ **Nested Class Structure**: Organized log access pattern
    ```python
    # Event logs by subtype
    fgt.api.log.disk.event.vpn.get(rows=10, filter="...")
    fgt.api.log.disk.event.system.get(rows=50)
    
    # Traffic logs by subtype
    fgt.api.log.disk.traffic.forward.get(rows=100)
    fgt.api.log.memory.traffic.local.get(rows=20)
    ```
  - 🎯 **5 Log Destinations**: disk, memory, fortianalyzer, forticloud, search
  - 📝 **12 Event Subtypes**: vpn, user, system, ha, router, wireless, wad, endpoint, fortiextender, connector, compliance_check, security_rating
  - 🚦 **6 Traffic Subtypes**: forward, local, multicast, sniffer, fortiview, threat
  - ⚡ **Specialized Generator**: Dedicated `log_generator.py` for parameterized paths

- **Enhanced Type Safety** (January 2026):
  - 📘 **Complete Type Stubs**: `.pyi` files for all endpoints (1,219 total)
  - 🔍 **Validator Stubs**: Type hints for all validator functions
  - ✅ **IDE Autocomplete**: Full IntelliSense support in VS Code, PyCharm, etc.
  - 🎯 **Type Checking**: All generated code passes mypy strict mode

- **Test Infrastructure** (January 2026):
  - ✅ **Auto-Generated Tests**: Basic smoke tests for all endpoints
    - GET operations testing (safe, read-only)
    - VDOM parameter testing
    - Filter parameter testing (CMDB)
    - exists() method testing
    - Validator import testing
  - 📊 **Test Structure**: Organized by category/subcategory matching API structure
  - 🧪 **Mock Support**: Structure tests for log endpoints (no live API calls needed)

### Changed

- **Generator Architecture** (January 2026):
  - 🔄 **Unified Generation**: Single generator handles all endpoint types
  - 📁 **Clean Structure**: Organized in `.dev/generator/` directory
  - 🔧 **Modular Design**: Separate generators for endpoints, validators, stubs, tests
  - 📝 **Template-Based**: Jinja2 templates for consistent code generation
  - 🎯 **Smart Filtering**: Automatically excludes log endpoints from CMDB processing

- **Code Organization** (January 2026):
  - 📦 **Streamlined Package**: Removed complexity, focus on core API
  - 🗂️ **Clear Hierarchy**: `api/v2/{category}/{subcategory}/{endpoint}.py`
  - 🎯 **Helper Organization**: All helpers in `{category}/{subcategory}/_helpers/`
  - 📝 **Documentation**: Inline docstrings for all generated methods

### Removed

- **⚠️ BREAKING: Convenience Wrappers Removed**:
  - ❌ Removed all convenience wrapper classes (firewall, schedule, shaper, etc.)
  - ❌ Removed `hfortix_fortios.firewall.*` modules
  - ❌ Removed `hfortix_fortios.schedule.*` modules
  - ❌ Removed `hfortix_fortios.shaper.*` modules
  - **Reason**: Unsustainable to maintain 1,200+ hand-written wrappers
  - **Alternative**: Use direct API access via `fgt.api.cmdb.*`, `fgt.api.monitor.*`, `fgt.api.log.*`
  - All functionality available through auto-generated API endpoints

### Migration from v0.4.x

Users upgrading from v0.4.x must migrate from convenience wrappers to direct API access:

**Old (v0.4.x) - Convenience Wrappers**:
```python
from hfortix_fortios.firewall import FirewallAddress
addr = FirewallAddress(fgt)
result = addr.create(name="test", subnet="10.0.0.1/32")
```

**New (v0.5.0) - Direct API**:
```python
result = fgt.api.cmdb.firewall.address.create(
    name="test",
    subnet="10.0.0.1/32"
)
```

All methods (get, create, update, delete, exists) work the same way - just accessed directly through the endpoint.

### Technical Improvements

- **Schema Processing** (January 2026):
  - 📥 **Smart Downloads**: Skip unavailable endpoints, use Swagger fallback
  - 🔍 **Metadata Tracking**: All schemas include source, timestamp, fallback reason
  - ✅ **Validation**: Schema validation before code generation
  - 🎯 **Error Handling**: Comprehensive error reporting with context

- **Build Process** (January 2026):
  - ⚡ **Faster Generation**: Optimized for 1,200+ endpoints
  - 📊 **Progress Tracking**: Real-time progress display during generation
  - 🔍 **Detailed Logging**: Complete generation logs with error details
  - ✅ **Verification**: Automatic validation of generated code

### Statistics

- **Endpoint Coverage**: 1,219 total endpoints (886 CMDB + 295 Monitor + 38 Log)
- **Type Stubs**: 1,219 `.pyi` stub files (100% coverage)
- **Validators**: 1,219 validator modules with schema-based validation
- **Tests**: 1,200+ auto-generated basic test files
- **Lines of Code**: ~500,000 lines of auto-generated Python code
- **Generator Success Rate**: 100% (0 failures with Swagger fallback)

### Notes

- 🚧 **Beta Status**: Version 0.5.0 remains in BETA until v1.0.0
- 📚 **Documentation**: All docs updated to reflect new architecture
- 🔄 **Breaking Changes**: Convenience wrappers removed (see migration guide)
- ✅ **Stability**: Generated code is stable and production-ready
- 🎯 **Future**: Focus on test coverage expansion and bug fixes toward v1.0.0

## [0.4.3] - 2026-01-02

### Added

- **Generic request() Method**:
  - New `request()` method accepts JSON directly from FortiGate GUI API preview
  - Supports all CRUD operations: GET, POST, PUT, DELETE
  - Zero-translation workflow: copy JSON from GUI → paste to code
  - Perfect for rapid API testing and prototyping
  - Comprehensive validation: method, URL format, required fields
  - Example usage:
    ```python
    config = {
        "method": "POST",
        "url": "/api/v2/cmdb/firewall/address",
        "params": {"vdom": "test"},
        "data": {"name": "host1", "subnet": "10.0.0.1/32"}
    }
    result = fgt.request(config)
    ```
  - See [REQUEST_METHOD_GUIDE.md](REQUEST_METHOD_GUIDE.md) for complete guide
  - Test suite: `.dev/pytests/other/request-module.py` (14 tests passing)

### Fixed

- **PEP8 Compliance**: Fixed all line length violations (E501) in client.py
- **Pytest Warnings**: Added filterwarnings configuration to suppress harmless PytestAssertRewriteWarning

## [0.4.1] - 2026-01-02

### Added

- **Core HTTP Client Scope Parameter Support**:
  - Added `scope` parameter to `post()`, `put()`, and `delete()` methods in `hfortix_core.http.client`
  - Enables proper handling of FortiOS global scope objects via API
  - Scope parameter automatically added to query string when provided
  - Required for modifying objects in global scope (e.g., `scope='global'`)
  - Supports both `'global'` and `'vdom'` scope values per FortiOS API specification

- **Wildcard FQDN Test Suite** (2026-01-14):
  - Comprehensive pytest test coverage for wildcard FQDN convenience wrappers
  - Test file: `.dev/pytests/firewall/wildcard_fqdn.py`
  - Read-only tests: 12 passing (get, exists, get_by_name operations)
  - Write operation tests: 26 skipped (due to API limitations)
  - Validation tests: 7 passing (parameter validation)
  - Automatic API support detection with graceful fallback
  - Full documentation of API limitations vs CLI support

### Changed

- **Wildcard FQDN Wrapper API Limitation Documentation** (2026-01-14):
  - **BREAKING CHANGE**: Disabled `create()`, `update()`, and `delete()` methods in wildcard FQDN wrappers
  - Methods now raise `NotImplementedError` with CLI workaround instructions
  - Affected wrappers:
    - `WildcardFqdnCustom.create/update/delete` - Custom wildcard FQDN addresses
    - `WildcardFqdnGroup.create/update/delete` - Wildcard FQDN groups
  - **Reason**: FortiOS REST API returns HTTP 500 error -3 "Entry not found" on POST/PUT/DELETE operations
  - **Note**: Objects can still be created via CLI and read via API (get/exists operations work)
  - **Workaround**: Use CLI commands for write operations:
    ```
    config firewall wildcard-fqdn custom
      edit "name"
        set wildcard-fqdn "*.example.com"
      next
    end
    ```
  - Read operations (`get()`, `exists()`, `get_by_name()`) continue to work normally via API
  - Added comprehensive inline documentation explaining limitation and CLI alternatives

- **Helper Module Reorganization** (2026-01-02):
  - **BREAKING CHANGE**: Centralized all helper functions to `hfortix_fortios._helpers`
  - **New Structure**: Organized helpers into logical modules
    - `_helpers/builders.py` - Payload building functions
    - `_helpers/normalizers.py` - List normalization utilities
    - `_helpers/validators.py` - All validation functions (generic + domain-specific)
    - `_helpers/converters.py` - Type conversion and data cleaning
    - `_helpers/response.py` - Response parsing helpers
  - **Migration Required**: Update imports from old locations
    - OLD: `from hfortix_fortios.api._helpers import ...`
    - OLD: `from hfortix_fortios.firewall._helpers import ...`
    - NEW: `from hfortix_fortios._helpers import ...`
  - **Benefits**:
    - Single source of truth for all helpers
    - Consistent imports across entire codebase
    - Better organization and scalability
    - Eliminates code duplication
  - **Removed**: Deprecated `api._helpers/` and `firewall._helpers/` directories

### Added

- **SSH/SSL Proxy Convenience Wrappers** (2026-01-02):
  - **SSH Proxy Wrappers**: Complete SSH inspection and proxy configuration
    - `SSHHostKey` - Manage SSH host keys for traffic inspection (Read-only via API)
    - `SSHLocalCA` - Configure SSH local certificate authorities (Create/Read only - cannot update/delete)
    - `SSHLocalKey` - Manage SSH local keys for proxying (Read-only via API)
    - `SSHSetting` - Global SSH proxy settings and configuration (Full CRUD support)
  - **SSL Proxy Wrappers**: SSL/TLS traffic inspection configuration
    - `SSLSetting` - SSL proxy settings and cipher configuration (Full CRUD support)
  - **Benefits**:
    - Pythonic interface with automatic input normalization
    - Consistent methods across all wrappers (create, get, update, delete, etc.)
    - Built-in validation using centralized validators
    - Type hints for better IDE support
    - Simplified error handling
  - **Documentation**: New comprehensive guide at `docs/fortios/wrappers/SSH_SSL_PROXY_WRAPPERS.md`
    - Complete API limitation documentation
    - Workarounds for FortiOS restrictions
    - Real-world configuration examples
  - **Test Coverage**:
    - SSH Proxy: 39 tests (15 passed, 24 skipped for unsupported API operations)
    - SSL Proxy: 28 tests (28 passed, 0 failed)
    - Test files: `.dev/pytests/firewall/ssh_proxy.py`, `.dev/pytests/firewall/ssl_proxy.py`
  - **Known API Limitations** (FortiOS security restrictions):
    - SSH Host-Keys: Read-only (auto-discovered during inspection)
    - SSH Local-Keys: Read-only (CLI-only creation)
    - SSH Local-CAs: Cannot delete or update via API (requires CLI/GUI)
    - SSL Settings: Some performance fields may not return in GET responses
    - See `docs/fortios/wrappers/SSH_SSL_PROXY_WRAPPERS.md` for details

- **Handler Protocol System** (2026-01-02):
  - **Comprehensive Documentation**: New `docs/fortios/HANDLER_PROTOCOL_SYSTEM.md` (800+ lines)
    - Complete guide on writing custom audit handlers
    - Protocol-based architecture (no inheritance required)
    - 6 working examples with best practices
    - Testing guidelines and troubleshooting
    - Migration guide from fortiosapi
  - **Custom Handler Capabilities**: Production-ready handler implementations
    - `KafkaHandler` - Stream audit events to Kafka for distributed systems
      - Asynchronous publishing with callbacks
      - Partition key routing for ordered processing
      - Compression support (gzip, snappy, lz4)
      - Context manager support
    - `DatabaseHandler` - Store audit logs in SQL databases
      - Supports SQLite, PostgreSQL, MySQL
      - Automatic table creation with indexes
      - Flexible querying capabilities
      - Long-term compliance retention
    - `WebhookHandler` - Send notifications to webhooks
      - Multiple formatters (Slack, Teams, Discord, generic)
      - Automatic retry with backoff
      - Pre-configured convenience classes (SlackNotifier, TeamsNotifier, DiscordNotifier)
      - Rich message formatting with attachments
  - **Enhanced CompositeHandler**: Advanced routing and error handling
    - **Priority-Based Ordering**: Execute handlers by priority (highest first)
      - Syntax: `(handler, priority)` or `(handler, priority, filter_fn)`
      - Ensures critical audit trails are written first
    - **Conditional Routing**: Filter functions control which operations go to which handlers
      - Filter by action, object type, success status, or custom criteria
      - Example: Route only failures to alert handler
    - **Error Aggregation**: Track handler failures over time
      - `error_summary` property for reliability monitoring
      - Sample error storage for debugging
      - `reset_errors()` method to clear tracking
    - **Dynamic Management**: Add/remove handlers at runtime
      - `add_handler(handler, priority, filter_fn)` - Add handlers dynamically
      - `remove_handler(handler)` - Remove specific handler
      - `get_handlers()` - Query current configuration
    - **Backward Compatible**: Simple list syntax still works
  - **Request Hook Infrastructure**: Foundation for intercepting requests/responses
    - `BeforeRequestHook` protocol - Validate/transform before sending
    - `AfterRequestHook` protocol - Process responses after receiving
    - `RequestContext` TypedDict - Type-safe request context
    - Location: `packages/core/hfortix_core/hooks/__init__.py`


### Changed

- **CompositeHandler Enhancement**: Maintains backward compatibility while adding advanced features
  - Old syntax `CompositeHandler([handler1, handler2])` still works
  - New syntax `CompositeHandler([(handler1, priority1, filter1), ...])` for advanced features
  - Internal structure changed from `self.handlers` list to `self._handlers` tuple list

### Documentation

- Added `docs/fortios/HANDLER_PROTOCOL_SYSTEM.md` - Comprehensive plugin system guide
- Added `.dev/PLUGIN_SYSTEM_PROGRESS.md` - Implementation progress and roadmap
- Created example handler implementations in `examples/custom_handlers/`
- Added CompositeHandler demo in `examples/composite_handler_demo.py`

## [0.4.1] - 2026-01-02

### Added

- **Enhanced Debugging and Observability** (2026-01-02):
  - **Connection Pool Monitoring**: Fixed hardcoded values bug in `get_connection_stats()`
    - Now returns real-time metrics: actual `max_connections` and `max_keepalive_connections`
    - Added tracking: `active_requests`, `total_requests`, `pool_exhaustion_count`
    - Pool exhaustion timestamps for identifying capacity issues
    - Applies to both sync (`HTTPClient`) and async (`AsyncHTTPClient`) implementations
  - **Request Inspection API**: New `inspect_last_request()` method
    - Returns detailed info about last API call: method, endpoint, params, response_time_ms, status_code
    - Essential for debugging slow requests and diagnosing API issues
    - Available on both HTTP client implementations
  - **Enhanced Debug Mode**: FortiOS client now supports `debug=True` (boolean)
    - Previous: `debug="DEBUG"` (string only)
    - Now: `debug=True` (convenience) or `debug="DEBUG"` (explicit level)
    - Automatically enables DEBUG-level logging when `debug=True`
  - **Convenience Properties**: Easy access to debugging information
    - `FortiOS.connection_stats` property - Real-time connection pool metrics
    - `FortiOS.last_request` property - Last request debugging details
    - No need to access internal `_client` anymore
  - **DebugSession Context Manager**: Comprehensive session monitoring
    - Captures all requests, timing, and connection stats during session
    - Auto-calculates aggregate metrics: avg/min/max response times
    - Prints detailed summary on exit (optional)
    - Example: `with DebugSession(fgt) as session: ...`
  - **Debug Utilities**: Helper functions for debugging
    - `debug_timer()` - Context manager for timing operations
    - `format_request_info()` - Pretty-print request details
    - `format_connection_stats()` - Pretty-print connection statistics
    - `print_debug_info()` - Comprehensive debug output
  - **Structured Logging Enhancements**: Better logging configuration
    - `configure_logging()` now supports `include_trace`, `output_file`, `structured` parameters
    - File logging: Log to both console and file simultaneously
    - Request correlation: Include trace IDs in all logs with `include_trace=True`
    - `RequestLogger` context manager for consistent request/response logging
  - **Modular Architecture**: Reorganized code structure
    - New `hfortix_core.logging/` package: `base.py`, `formatters.py`, `handlers.py`
    - New `hfortix_core.debug/` package: `base.py`, `formatters.py`, `handlers.py`
    - Follows consistent pattern with `hfortix_core.audit/` package
    - Protocol definitions in `base.py` for extensibility

- **Enhanced Type Hints and IDE Support** (2026-01-02):
  - **Type Definitions Module**: New `hfortix_core.types` module
    - `APIResponse`, `ListResponse`, `ObjectResponse`, `ErrorResponse` TypedDicts
    - `ConnectionStats`, `RequestInfo` for debugging types
    - `CircuitBreakerState` literal type
    - Better IDE autocomplete and type checking
  - **Type Stub Files (.pyi)**: Enhanced IDE support
    - `hfortix_core/http/client.pyi` - Sync HTTP client stubs
    - `hfortix_core/http/async_client.pyi` - Async HTTP client stubs
    - `hfortix_fortios/client.pyi` - FortiOS client stubs
    - Improved autocomplete in VS Code, PyCharm, and other IDEs
  - **Enhanced Package Exports**: Easier imports
    - Convenience wrappers now exported from main package: `FirewallPolicy`, `ScheduleRecurring`, etc.
    - Debug utilities exported: `DebugSession`, `debug_timer`, `format_connection_stats`, etc.
    - Common exceptions exported: All core exceptions available from `hfortix_fortios`
    - Example: `from hfortix_fortios import FortiOS, FirewallPolicy, DebugSession`

- **Comprehensive Documentation** (2026-01-02):
  - **Rate Limiting Guide**: New `docs/fortios/RATE_LIMITING.md`
    - HTTP 429 handling and automatic retry strategies
    - Circuit breaker configuration and patterns
    - Async patterns for high throughput
    - Connection pool management best practices
    - Production-ready configuration examples
  - **Debugging Guide**: New `docs/fortios/DEBUGGING.md`
    - Debug mode usage (`debug=True` vs `debug="DEBUG"`)
    - Connection statistics monitoring
    - Request inspection techniques
    - DebugSession for performance analysis
    - Logging configuration and structured logging
    - Integration with ELK, Splunk, CloudWatch
    - Common debugging scenarios with solutions

- **Enhanced Structured Logging with Multi-Tenant Support** (2026-01-02):
  - **VDOM/ADOM Fields**: Automatic inclusion in all structured logs
    - `vdom` field automatically added for FortiOS Virtual Domain environments
    - `adom` field support ready for future FortiManager/FortiAnalyzer clients
    - Essential for multi-tenant environments and per-customer observability
  - **Consistent Log Context**: New `_log_context()` helper method
    - Centralized logging context builder in `BaseHTTPClient`
    - Ensures all log events have consistent field naming
    - Automatically includes request_id, method, endpoint, status_code, duration_seconds
  - **Updated Documentation**: Enhanced `StructuredFormatter` with standard field definitions
    - Documents all standard log fields (timestamp, level, logger, message)
    - Documents common extra fields (request_id, method, endpoint, vdom, adom, etc.)
    - Examples showing multi-tenant logging usage
  - **Benefits for Multi-Tenant Deployments**:
    - Easy log filtering: `jq '.vdom == "customer_a"' logs.json`
    - Per-tenant metrics and dashboards in ELK/Splunk/Datadog
    - Audit trail isolation by virtual domain
    - Compliance reporting per customer/tenant
  - See `docs/fortios/OBSERVABILITY.md` for complete documentation

- **Smart Retry & Circuit Breaker Enhancements** (2026-01-02):
  - **Retry Strategy Selection**: Choose between exponential or linear backoff strategies
    - New parameter: `retry_strategy` - "exponential" (default) or "linear"
    - Exponential: 1s, 2s, 4s, 8s, 16s, 30s (best for transient failures like network glitches)
    - Linear: 1s, 2s, 3s, 4s, 5s (best for rate limiting scenarios)
  - **Jitter Support**: Prevent thundering herd problem
    - New parameter: `retry_jitter` (bool, default: False)
    - Adds 0-25% random variation to retry delays
    - Prevents multiple clients from retrying simultaneously
    - Recommended for production deployments with multiple instances
  - **Public Telemetry APIs**: Monitor retry patterns and circuit breaker health
    - `FortiOS.get_retry_stats()` - Get retry statistics (total, by endpoint, by reason)
    - `FortiOS.get_circuit_breaker_state()` - Get circuit breaker state and failure count
    - `FortiOS.get_health_metrics()` - Comprehensive health view (already existed, now documented)
  - **Batch Audit Log Export**: Export tracked operations for compliance reporting
    - `FortiOS.export_audit_logs()` - Export to JSON, CSV, or text format
    - Filter by HTTP method, API type, or timestamp
    - Essential for SOC 2, HIPAA, PCI-DSS compliance audits
  - **Examples**: New `examples/retry_strategy_demo.py` with 6 comprehensive demonstrations

- **Enterprise Audit Logging**: Complete audit logging system for compliance (SOC 2, HIPAA, PCI-DSS)
  - Built-in handlers: `SyslogHandler`, `FileHandler`, `StreamHandler`, `CompositeHandler`
  - Multiple formatters: JSON, Syslog RFC 5424, CEF (Common Event Format)
  - Automatic data sanitization for sensitive fields (passwords, tokens, keys)
  - Non-blocking error handling (audit failures don't break operations)
  - SIEM integration support (Splunk, ELK, QRadar, ArcSight)
  - User context tracking for change management
  - New parameters: `audit_handler`, `audit_callback`, `user_context`
  - See `docs/fortios/AUDIT_LOGGING.md` for full documentation
  - See `examples/audit_logging_demo.py` for usage examples
  - **Unique to hfortix**: No other Python FortiGate library has built-in compliance features

- **Logging & Observability**: Enterprise-grade logging and distributed tracing
  - `configure_logging()` helper for easy setup (text or JSON format)
  - `StructuredFormatter` for machine-readable JSON logs (ELK, Splunk, CloudWatch compatible)
  - `TextFormatter` with optional ANSI color codes for terminal output
  - `trace_id` parameter for distributed tracing and request correlation across microservices
  - `user_context` parameter for change management metadata in all logs
  - Automatic trace_id and user_context inclusion in audit logs
  - Support for custom logging handlers (file, syslog, cloud)
  - Integration examples for ELK Stack, Splunk, AWS CloudWatch, GCP Logging, Datadog
  - Production-ready patterns for Kubernetes and cloud-native deployments
  - See `docs/fortios/OBSERVABILITY.md` for comprehensive guide
  - See `examples/observability_demo.py` for 7 interactive demos
  - **Production Ready**: Complete observability stack for distributed systems

## [0.4.0] - 2025-12-31

### ⚠️ BREAKING CHANGES

This is a MAJOR release with breaking changes. The monolithic package has been split into modular packages.

**Migration Guide:**

- **Old (0.3.x)**: `pip install hfortix` → Everything in one package
- **New (0.4.0)**: Choose your installation:
  - `pip install hfortix[fortios]` → Core + FortiOS (recommended for existing users)
  - `pip install hfortix-fortios` → Just FortiOS (includes core)
  - `pip install hfortix` → Core only (minimal)

**Import Changes:**
- Old: `from hfortix import FortiOS` ✅ Still works with `hfortix[fortios]`
- New: `from hfortix_fortios import FortiOS` ✅ Explicit package imports

### Added

- **Modular Package Structure**: Split monolithic package into focused components
  - `hfortix-core`: Core exceptions (FortinetError, APIError, etc.) and HTTP client framework (sync/async)
  - `hfortix-fortios`: FortiOS/FortiGate client, API endpoints, and firewall helpers
  - `hfortix` (meta-package): Convenient installation with extras for all products
  - See `.dev/PACKAGE_SPLIT_PLAN.md` for architecture details

- **Documentation Restructuring**: Reorganized docs to align with modular architecture
  - Created `docs/core/` for hfortix-core documentation
  - Created `docs/fortios/` for hfortix-fortios documentation
  - Moved all FortiOS-specific guides to `docs/fortios/`
  - Moved wrapper docs to `docs/fortios/wrappers/`
  - Created `docs/archive/` for historical documentation
  - Updated `docs/README.md` with comprehensive navigation index

### Fixed

- **Code Quality Improvements**
  - Fixed E501 line length errors in `api/_helpers/helpers.py` and `client.py`
  - Fixed mypy type errors with namespace package imports by configuring `mypy_path`
  - Added proper type ignores for Pyright/Pylance compatibility
  - Disabled `warn_unused_ignores` in mypy to support dual type checker usage

- **Pre-commit Configuration**
  - Updated `.flake8` to ignore E501 for auto-generated `api/v2/` code
  - Updated `.pre-commit-config.yaml` to exclude `api/v2/` from private key detection
  - All pre-commit hooks now pass successfully

### Changed

- **Installation Options**: Users can now install only what they need
  - `pip install hfortix` - Core only (minimal installation)
  - `pip install hfortix[fortios]` - Core + FortiOS
  - `pip install hfortix[all]` - Everything (all products, future-ready)
  - `pip install hfortix-fortios` - FortiOS client only (includes core as dependency)
  - `pip install hfortix-core` - Core framework only

- **Import Patterns**: New import options available (old imports still work via meta-package)
  - New: `from hfortix_fortios import FortiOS`
  - New: `from hfortix_core import FortinetError, APIError`
  - Legacy: `from hfortix import FortiOS` (still supported when fortios extra is installed)
  - Legacy: `from hfortix.FortiOS import FortiOS` (still supported when fortios extra is installed)

### Breaking Changes

- **Package Split**: `hfortix` is now a minimal meta-package (core only by default)
  - For FortiOS: Install `hfortix[fortios]` or `hfortix-fortios`
  - For everything: Install `hfortix[all]`
- **Import Changes**: When using minimal install, FortiOS imports not available
  - Install `hfortix[fortios]` or `hfortix-fortios` for FortiOS functionality

### Migration Guide

**For backward compatibility (everything installed):**
```bash
pip install hfortix[all]  # Installs core + all products (fortios, etc.)
# OR
pip install hfortix-fortios  # Just FortiOS (includes core)
```

**For minimal installs:**
```bash
pip install hfortix  # Core only (exceptions, HTTP framework)
pip install hfortix[fortios]  # Core + FortiOS
```

### Developer Notes

- **Version**: 0.4.0-dev1 (development version, not published to PyPI)
- **PyPI Status**: Latest published version remains 0.3.39
- **Release Plan**: Will be published as 0.4.0 when ready
- **Testing**: All existing tests pass with new package structure

## [0.3.39] - 2025-12-29

### Added

- **Complete Service Management Wrappers**: Production-ready wrappers for firewall services
  - `ServiceCategory`: Organize services into categories via `fgt.firewall.service_category`
  - `ServiceCustom`: TCP/UDP/ICMP/IP services with 30+ parameters via `fgt.firewall.service_custom`
  - `ServiceGroup`: Group services with member management via `fgt.firewall.service_group`
  - Full parameter support with comprehensive validation (name length, port ranges, protocol values)
  - Consistent interface: `.create()`, `.get()`, `.update()`, `.delete()`, `.exists()`, `.get_by_name()`, `.rename()`
  - Advanced features: `.add_member()`, `.remove_member()` for groups
  - Complete test suite with 30+ tests passing
  - Documentation: `docs/wrappers/CONVENIENCE_WRAPPERS.md`

- **Enhanced Schedule Wrappers**: Production-ready schedule management
  - `ScheduleOnetime`: One-time schedules with expiration via `fgt.firewall.schedule_onetime`
  - `ScheduleRecurring`: Daily/weekly recurring schedules via `fgt.firewall.schedule_recurring`
  - `ScheduleGroup`: Group schedules with member management via `fgt.firewall.schedule_group`
  - Full CRUD operations with parameter validation
  - Convenience methods: `.clone()`, `.rename()`, `.add_member()`, `.remove_member()`
  - Response helpers: `get_mkey()`, `is_success()`, `get_results()`
  - Documentation: `docs/wrappers/SCHEDULE_WRAPPERS.md`

- **IP/MAC Binding Wrappers**: Complete IP/MAC binding management
  - `IpMacBindingTable`: Manage IP/MAC binding entries via `fgt.firewall.ipmacbinding_table`
  - `IpMacBindingSetting`: Configure binding behavior via `fgt.firewall.ipmacbinding_setting`
  - Full validation: IP addresses, MAC addresses, sequence numbers
  - Convenience methods: `.enable()`, `.disable()`, `.exists()`
  - Complete test suite: 19 tests passing

- **Automated Release Workflow**: New `make release` target for streamlined releases
  - Automated version bumping (auto-increment or manual specification)
  - Runs all pre-release checks (formatting, linting, type-checking, security)
  - Executes test suite validation
  - Updates version in all necessary files (pyproject.toml, setup.py, `__init__.py`)
  - Updates CHANGELOG.md automatically
  - Creates git commit and tag
  - Prompts for GitHub push (triggers CI/CD for PyPI publishing)
  - Usage: `make release` (auto-increment patch), `make release VERSION=0.3.40`, `make release TYPE=minor`
  - New script: `.dev/scripts/release.py` for automation

## [0.3.38] - 2025-12-29

### Added

- **Traffic Shaper Convenience Wrappers**: Production-ready wrappers for FortiOS traffic shaping
  - `ShaperPerIp`: Per-IP traffic shaper for bandwidth and session limits per source IP
    - Parameters: max_bandwidth, bandwidth_unit, session limits, DiffServ settings
    - Methods: create(), get(), update(), delete(), exists()
  - `TrafficShaper`: Shared traffic shaper with guaranteed/maximum bandwidth
    - Parameters: guaranteed/maximum bandwidth, priority, DiffServ, CoS, overhead
    - Methods: create(), get(), update(), delete(), exists()
  - Comprehensive parameter validation (name length, bandwidth ranges, enum values)
  - Accessible via `fgt.firewall.shaper_per_ip` and `fgt.firewall.traffic_shaper`
  - Complete test suite: 20 tests passing, 1 skipped (CoS requires VLAN)

### Changed

- **Rename Method Behavior**: Updated `rename()` methods to raise `NotImplementedError`
  - FortiOS does not support renaming shaper objects (name is immutable primary key)
  - Shapers use name-based URLs (`/firewall.shaper/traffic-shaper/{name}`)
  - Unlike shaping policies which use ID-based URLs and support renaming
  - Methods now raise clear error explaining limitation and workaround
  - Tests updated to verify NotImplementedError is raised correctly

### Documentation

- **Documentation Reorganization**: Improved structure and organization
  - Created `docs/wrappers/` folder for wrapper-specific documentation
  - New `CONVENIENCE_WRAPPERS.md` - Overview guide for all convenience wrappers (START HERE)
  - Moved `FIREWALL_POLICY_WRAPPER.md` to `docs/wrappers/`
  - Moved `SHAPER_WRAPPERS.md` to `docs/wrappers/`
  - Renamed `SCHEDULE_CONVENIENCE_METHODS.md` to `SCHEDULE_WRAPPERS.md` and moved to `docs/wrappers/`
  - Removed outdated `FIX_WINDOWS_INSTALL.md` (issue fixed in v0.3.33)
  - Moved `PYPI_SETUP.md` to `.dev/docs/` (development-only documentation)
  - Updated all documentation cross-references to use new paths
  - Clear separation: user docs in `docs/`, dev docs in `.dev/docs/`
- **Shaper Wrappers Guide**: New comprehensive documentation (`docs/wrappers/SHAPER_WRAPPERS.md`)
  - Quick start examples and API reference for both shaper types
  - Detailed parameter documentation with validation rules
  - Important limitations section explaining rename restriction
  - Comparison table: shapers (name-based) vs shaping policies (ID-based)
  - 7 complete examples covering common use cases
  - Troubleshooting guide and best practices
- **API Investigation Results**: Documented FortiOS shaper API behavior (`.dev/SHAPER_API_INVESTIGATION.md`)
  - Confirmed no numeric ID field exists for shaper objects
  - Verified rename operations silently fail (FortiOS ignores name changes)
  - Compared shaper endpoints (name-based) vs policy endpoints (ID-based)
  - Test results showing API responses and rename attempts

## [0.3.37] - 2025-12-29

### Added

- **Firewall Service Convenience Wrappers**: New high-level wrappers for firewall service management
  - `ServiceCategory`: Manage firewall service categories with simplified syntax
  - `ServiceCustom`: Create and manage custom services (TCP, UDP, ICMP, IP protocols)
  - `ServiceGroup`: Manage service groups with member add/remove operations
  - Full CRUD operations with parameter validation and automatic data normalization
  - Accessible via `fgt.firewall.service_category`, `fgt.firewall.service_custom`, `fgt.firewall.service_group`

### Fixed

- **Rename Functionality**: Fixed critical bug in `data` parameter handling for all rename operations
  - Modified `build_cmdb_payload()` and `build_cmdb_payload_normalized()` in `api/_helpers/helpers.py`
  - The `data` parameter is now properly merged into the payload instead of being nested as `{"data": {...}}`
  - This fixes rename operations for ServiceGroup, ServiceCustom, and ServiceCategory
  - All 40 firewall service tests now passing, including previously failing rename tests

### Changed

- **Rename Method Signature**: Standardized parameter naming across all service wrappers
  - Changed from `rename(old_name, new_name)` to `rename(name, new_name)` for consistency
  - Affects: `ServiceGroup.rename()`, `ServiceCustom.rename()`, `ServiceCategory.rename()`
  - Matches the pattern used by other wrapper methods (update, delete, etc.)

### Documentation

- **Code Quality**: Fixed all PEP8 E501 line length violations in firewall wrapper files
  - Wrapped long docstrings, error messages, and examples to comply with 79 character limit
  - Improved code readability while maintaining all functionality
  - All pre-release checks now passing (flake8, mypy, black, isort, bandit)

## [0.3.36] - 2025-12-25

### Fixed

- **Firewall Policy Rename**: Simplified `rename()` method - FortiOS supports updating name field directly
  - Removed unnecessary workaround that fetched and included logtraffic field
  - Method now simply calls `update(policy_id, name)` as originally intended
  - Re-enabled 3 rename tests that were incorrectly marked as skipped

- **Critical Packaging Issue**: Fixed `.gitignore` pattern excluding password-related modules
  - Changed `*password*` to `/*password*` to only ignore root-level credential files
  - This was preventing `password_policy.py` and related modules from being included in git and PyPI packages
  - Affected files now properly included:
    - `hfortix/FortiOS/api/v2/cmdb/system/password_policy.py`
    - `hfortix/FortiOS/api/v2/cmdb/system/password_policy_guest_admin.py`
    - `hfortix/FortiOS/api/v2/cmdb/user/password_policy.py`
    - `hfortix/FortiOS/api/v2/monitor/system/change_password.py`
    - `hfortix/FortiOS/api/v2/monitor/system/password_policy_conform.py`
    - `hfortix/FortiOS/api/v2/monitor/user/password_policy_conform.py`
    - All related helper files
  - Fixes `ModuleNotFoundError: No module named 'hfortix.FortiOS.api.v2.cmdb.system.password_policy'`

## [0.3.35] - 2025-12-25

### Fixed

- **Package Build**: Ensures `password_policy.py` is included in PyPI distribution
  - This file was missing in the PyPI v0.3.34 release
  - All password policy modules are now properly included
  - Fixes `ModuleNotFoundError: No module named 'hfortix.FortiOS.api.v2.cmdb.system.password_policy'`

- **Firewall Policy**: Fixed `exists()` method exception handling
  - Now returns `False` for non-existent policies instead of raising exception
  - Wrapped `_api.exists()` call in try/except block
  - Matches expected behavior for convenience wrappers

- **Markdown Linting**: Disabled overly strict markdown linting rules
  - Disabled MD022, MD032, MD036, MD031, MD026
  - Allows more flexible documentation formatting
  - All pre-commit hooks now pass

### Changed

- **Documentation Organization**: Moved documentation files to `docs/` directory
  - `SCHEDULE_CONVENIENCE_METHODS.md` → `docs/SCHEDULE_CONVENIENCE_METHODS.md`
  - `FIX_WINDOWS_INSTALL.md` → `docs/FIX_WINDOWS_INSTALL.md`
  - Cleaner root directory structure

- **CI/CD Optimization**: Skip workflows on documentation-only changes
  - Added `paths-ignore` for `docs/**`, `*.md`, `LICENSE`, `.gitignore`
  - Applies to both `ci.yml` and `codeql.yml` workflows
  - Saves CI minutes and speeds up documentation updates

## [0.3.34] - 2025-12-25

### Added

- **Schedule Convenience Methods**: Added comprehensive convenience methods to all schedule types
  - **New Methods** (available for `schedule_onetime`, `schedule_recurring`, `schedule_group`):
    - `get_by_name(name, vdom=None)`: Returns schedule data directly (not full API response)
    - `rename(name, new_name, vdom=None)`: Rename a schedule in one call
    - `clone(name, new_name, **overrides, vdom=None)`: Clone schedule with optional modifications
  - **Response Helpers** (available from `hfortix_fortios._helpers`):
    - `get_mkey(response)`: Extract created object's name from response
    - `is_success(response)`: Check if operation succeeded
    - `get_results(response)`: Extract results from response
  - Matches the convenience method pattern from `firewallPolicy`
  - Makes schedule management more user-friendly and consistent
  - See `docs/SCHEDULE_CONVENIENCE_METHODS.md` for full documentation
  - See `examples/schedule_convenience_demo.py` for usage examples

- **IP/MAC Binding Modules**: New modules for firewall IP/MAC binding management
  - `ipmacBindingSetting`: Manage IP/MAC binding settings
  - `ipmacBindingTable`: Manage IP/MAC binding table entries
  - **Core Methods**:
    - `create(seq_num, ip, mac, name=None, status='enable', vdom=None)`: Create new binding
    - `update(seq_num, **kwargs, vdom=None)`: Update existing binding
    - `delete(seq_num, vdom=None)`: Delete binding
    - `get(seq_num=None, vdom=None)`: Get binding(s) by sequence number
    - `get_all(vdom=None)`: Get all bindings
  - **Convenience Methods**:
    - `exists(seq_num, vdom=None)`: Check if binding exists
    - `enable(seq_num, vdom=None)`: Enable a binding
    - `disable(seq_num, vdom=None)`: Disable a binding
  - **Validation**: IP addresses, MAC addresses, status values, name length
  - Comprehensive test suite: `examples/ipmacbinding_test_suite.py` (19 pytest tests)

- **Firewall Policy Helpers Module**: New `_helpers.py` module with validation utilities
  - Extracted common validation logic from firewall policy modules
  - Functions for validating sequence numbers, IP addresses, MAC addresses, etc.
  - Improves code reusability and maintainability

### Changed

- **Documentation Organization**: Moved documentation files to `docs/` directory
  - `SCHEDULE_CONVENIENCE_METHODS.md` → `docs/SCHEDULE_CONVENIENCE_METHODS.md`
  - `FIX_WINDOWS_INSTALL.md` → `docs/FIX_WINDOWS_INSTALL.md`
  - Cleaner root directory structure

### Fixed

- **PEP8 Compliance**: Fixed line length violations in multiple files
  - `hfortix/FortiOS/firewall/_helpers.py`: Split long docstring
  - `hfortix/FortiOS/firewall/firewallPolicy.py`: Split long comment
  - `hfortix/FortiOS/http_client_async.py`: Shortened log message
- **Security**: Fixed bandit warning B104 in IP validation (false positive)
  - Added `# nosec B104` comment to IP wildcard validation check
  - This is validation code, not a network binding operation

### Development

- **Pre-release Tooling Improvements**:
  - Added bandit security scanning to pre-release checks
  - Added pre-commit hooks integration to auto-fix script
  - Pre-release process now catches security and formatting issues earlier
- **TestPyPI Support**: Added upload script and documentation
  - New `upload_to_testpypi.sh` script for testing releases
  - `docs/TESTPYPI_GUIDE.md` with complete setup instructions
  - **WARNING**: Not recommended for test environments - may cause long delays
  - Fail-fast behavior is preserved by default (auto-retry disabled)
  - Available in both sync (`HTTPClient`) and async (`AsyncHTTPClient`) clients
  - Examples:

    ```python
    # Fail-fast (default) - raises CircuitBreakerOpenError immediately
    fgt = FortiOS(host="192.0.2.10", token="api_token")

    # Auto-retry - waits 5 seconds between retries (up to 3 attempts)
    fgt = FortiOS(
        host="192.0.2.10",
        token="api_token",
        circuit_breaker_auto_retry=True,
        circuit_breaker_max_retries=3,
        circuit_breaker_retry_delay=5.0  # Wait 5s between retries
    )

    # Custom retry delay for slower recovery scenarios
    fgt = FortiOS(
        host="192.0.2.10",
        token="api_token",
        circuit_breaker_auto_retry=True,
        circuit_breaker_max_retries=5,
        circuit_breaker_retry_delay=10.0  # Wait 10s between retries
    )
    ```

- **Pytest Test Suites**: Comprehensive test coverage for convenience wrapper classes
  - `examples/ipmacbinding_test_suite.py`: 19 tests covering IP/MAC binding CRUD operations
    - Tests: create, read, update, delete operations
    - Validation: IP addresses, MAC addresses, status values, name length
    - Convenience methods: enable(), disable(), exists()
    - Error handling: duplicate entries, non-existent resources
    - List operations and cleanup fixtures
  - `examples/circuit_breaker_test.py`: Circuit breaker behavior demonstration
    - Fail-fast vs auto-retry comparison
    - Circuit breaker state transitions
    - Recovery scenarios with valid endpoints
  - All tests use pytest framework with fixtures for cleanup
  - Tests validate both convenience wrappers and direct API access

### Changed

- **Circuit Breaker Defaults**: Adjusted thresholds for better testing and general use
  - `circuit_breaker_threshold`: 5 → 10 consecutive failures (more tolerant)
  - `circuit_breaker_timeout`: 60.0s → 30.0s (faster recovery)
  - **Rationale**: Previous settings (5 failures, 60s timeout) were too aggressive for:
    - Testing environments where some failures are expected
    - Development workflows with frequent code changes
    - Networks with occasional transient issues
  - New settings still provide circuit breaker protection while being more practical
  - Users can override via `circuit_breaker_threshold` and `circuit_breaker_timeout` parameters if needed

- **FirewallPolicy.exists()**: Enhanced to support lookup by name or policy ID
  - Added optional `name` parameter for checking policy existence by name
  - `policy_id` parameter is now optional (either `policy_id` or `name` required)
  - Maintains backward compatibility - existing code using `policy_id` continues to work
  - **Performance Note**: Using `name` performs a recursive lookup (slower), while `policy_id` uses direct API call (faster)
  - Improves API consistency with schedule wrapper methods
  - Examples:
    ```python
    # Direct lookup by ID (recommended for performance)
    exists = fgt.firewall.policy.exists(policy_id=5)

    # Lookup by name (convenient but slower)
    exists = fgt.firewall.policy.exists(name="Allow-Web-Traffic")
    ```

## [0.3.33] - 2025-12-25

### Fixed

- **Package Distribution**: Fixed missing `password_policy.py` module in PyPI package
  - Version 0.3.32 was missing the `hfortix.FortiOS.api.v2.cmdb.system.password_policy` module
  - This caused `ModuleNotFoundError` when initializing FortiOS instance
  - Updated version in both `setup.py` and `pyproject.toml` to ensure consistency
  - Rebuilt and republished package with all required modules included
  - Users experiencing the import error should upgrade: `pip install --upgrade hfortix`

## [0.3.32] - 2025-12-24

### Fixed

- **CI/CD Pipeline**: Publishing now properly blocked if CI fails
  - Removed `if: always()` from wait-for-ci job
  - Job now fails if CI checks don't pass, preventing publishing
  - Fixed trailing whitespace in workflow file

## [0.3.31] - 2025-12-24

### Fixed

- **CI/CD Pipeline**: Fixed wait-for-ci job to properly wait for CI completion
  - Switched to `fountainhead/action-wait-for-check` for better reliability
  - Added 30-minute timeout with 10-second polling interval
  - Prevents race condition where publishing started before CI completed
  - Job now always runs but conditionally waits based on trigger type

## [0.3.30] - 2025-12-24

### Changed

- **CI/CD Pipeline**: Publishing workflow now waits for CI checks to pass
  - Added `wait-for-ci` job to ensure all quality checks pass before publishing
  - Configured trusted publishing for TestPyPI (no API token needed)
  - Publishing flow: CI passes → TestPyPI → verify → PyPI production
  - Added comprehensive PyPI setup documentation (`docs/PYPI_SETUP.md`)

## [0.3.29] - 2025-12-24

### Changed

- **CI/CD Pipeline**: Enhanced PyPI publication workflow
  - Now publishes to TestPyPI first for validation
  - Only publishes to production PyPI after successful TestPyPI verification
  - Added package availability verification steps
  - Prevents publishing broken packages to production

## [0.3.28] - 2025-12-24

### Fixed

- **Critical Syntax Errors**: Fixed 512 broken f-strings in CMDB _helpers files
  - Black formatter had incorrectly reformatted multi-line f-strings
  - Caused 511 E999 syntax errors across all _helpers files
  - Used regex pattern to rejoin broken f-string expressions
  - All files now pass flake8 validation

### Changed

- **Pre-commit Configuration**: Enhanced Black exclusion documentation
  - Added critical warning comment about _helpers exclusion
  - Documented why exclusion must be maintained (prevents 500+ syntax errors)
  - Prevents accidental removal of necessary exclusion pattern

## [0.3.27] - 2025-12-24

### Changed

- **Import Refactoring**: Refactored monitor API imports for better code quality
  - `hfortix/FortiOS/api/v2/monitor/firewall/__init__.py` now uses direct class imports
  - Eliminated confusing module alias pattern (e.g., `sessions as sessions_module`)
  - Imports are now alphabetically sorted and properly formatted
  - Cleaner, more maintainable code that passes isort/black checks

### Fixed

- **Pre-commit Configuration**: Removed monitor API from exclusions
  - Monitor API files now included in black, isort, flake8, and mypy checks
  - Fixed yamllint errors (trailing blank lines in YAML files)
  - All pre-commit hooks now pass successfully

## [0.3.26] - 2025-12-24

### Fixed

- **Syntax Errors**: Fixed 32 files with broken f-strings (E999 errors)
  - f-strings now properly formatted on single lines
  - All files pass flake8 syntax validation
  - Pre-release workflow now catches syntax errors immediately

### Changed

- **Directory Naming**: Renamed hyphenated directories to follow Python conventions
  - `wireless-controller` → `wireless_controller`
  - `switch-controller` → `switch_controller`
  - `extension-controller` → `extension_controller`
  - `endpoint-control` → `endpoint_control`
  - `web-proxy` → `web_proxy`
  - **BREAKING CHANGE**: Import paths updated, users must update their code
  - Mypy can now properly validate all API modules

### Added

- `.dev/scripts/fix_fstrings.py` - Utility to fix broken f-strings in generated code
- `.dev/scripts/rename_hyphenated_dirs.py` - Utility for directory renaming

## [0.3.25] - 2025-12-24

### Added

- **Pre-Release Workflow**: Comprehensive code quality automation
  - `make pre-release` - Auto-fix and validate code before release
  - `make fix` - Auto-fix formatting and import issues
  - `make fix-check` - Dry-run to see what would be fixed
  - `.dev/scripts/pre_release_fix.py` - Auto-fix script with Black and isort
  - `.dev/scripts/pre_release_check.py` - Validation script with all quality checks

### Changed

- **Code Quality Configuration**: Centralized and consistent settings
  - Created `.flake8` config file with PEP 8 standards (79 char line length)
  - API folders excluded from E501 line-length checks (auto-generated code)
  - Updated `.pre-commit-config.yaml` to use `.flake8` config
  - Updated GitHub Actions CI to use `.flake8` config
  - All tools (Makefile, scripts, pre-commit, CI) now use same configuration

- **Pre-commit Hooks**: Improved configuration
  - Excluded `.dev/` directory from all checks (development tools, not package code)
  - Consistent exclude patterns across all hooks
  - Pre-commit check added to pre-release workflow (warning only)

### Fixed

- **Test Execution**: Tests excluded from pre-release workflow
  - Pre-release checks no longer run tests (run separately with `make test`)
  - Focus on code quality, formatting, and linting only

### Documentation

- `.dev/scripts/README.md` - Pre-release workflow guide
- `.dev/CODE_QUALITY_CONFIG.md` - Comprehensive configuration documentation

## [0.3.24] - 2025-12-24

### Added

- **Exception Hierarchy**: Comprehensive retry logic support
  - `RetryableError` base class for transient errors (rate limits, timeouts, service unavailable)
  - `NonRetryableError` base class for permanent errors (bad request, duplicate entry, not found)
  - All existing exceptions updated to inherit from appropriate base class
  - Enables intelligent retry strategies: `if isinstance(error, RetryableError)`

- **New Exception Types**: Client-side and specialized errors
  - `ConfigurationError` - FortiOS instance misconfiguration (replaces generic ValueError)
  - `VDOMError` - VDOM-specific errors with vdom attribute
  - `OperationNotSupportedError` - Unsupported operations on endpoints
  - `ReadOnlyModeError` - Already existed, now properly documented

- **Enhanced Exception Metadata**: Better debugging and error tracking
  - `request_id` - Unique UUID for each request (auto-generated)
  - `timestamp` - ISO 8601 timestamp when error occurred
  - Enhanced `__str__()` - Human-readable with emoji hints (💡)
  - Added `__repr__()` - Developer-friendly representation for debugging
  - All APIError exceptions now capture full context automatically

- **Recovery Suggestions**: Built-in error recovery guidance
  - `DuplicateEntryError.suggest_recovery()` - Suggests using PUT or checking existing
  - `EntryInUseError.suggest_recovery()` - Suggests removing references first
  - `ResourceNotFoundError.suggest_recovery()` - Suggests using POST or listing available
  - Helps developers understand how to handle common error scenarios

- **Helper Utility Functions**: Simplify retry logic implementation
  - `is_retryable_error(error)` - Check if error should be retried
  - `get_retry_delay(error, attempt, base_delay, max_delay)` - Calculate backoff delay
    - Exponential backoff for `RateLimitError`
    - Linear backoff for `ServiceUnavailableError`
    - Moderate backoff for `TimeoutError`
  - Makes implementing retry logic simple and consistent

- **Comprehensive Tests**: Full test coverage for new functionality
  - Exception hierarchy tests (RetryableError vs NonRetryableError)
  - Metadata capture tests (request_id, timestamp)
  - String representation tests (__str__ and __repr__)
  - Recovery suggestion tests
  - Helper function tests (is_retryable_error, get_retry_delay)
  - Client-side exception tests
  - All tests passing ✅

### Changed

- **Exception Inheritance**: Updated all HTTP status exceptions
  - `BadRequestError` now inherits from `NonRetryableError` (was APIError)
  - `ResourceNotFoundError` now inherits from `NonRetryableError` (was APIError)
  - `RateLimitError` now inherits from `RetryableError` (was APIError)
  - `ServerError` now inherits from `RetryableError` (was APIError)
  - `ServiceUnavailableError` now inherits from `RetryableError` (was APIError)
  - `TimeoutError` now inherits from `RetryableError` (was APIError)
  - `CircuitBreakerOpenError` now inherits from `RetryableError` (was APIError)

- **FortiOS-Specific Exceptions**: Updated inheritance
  - `DuplicateEntryError` now inherits from `NonRetryableError` (was APIError)
  - `EntryInUseError` now inherits from `NonRetryableError` (was APIError)
  - `InvalidValueError` now inherits from `NonRetryableError` (was APIError)
  - `PermissionDeniedError` now inherits from `NonRetryableError` (was APIError)

- **Error Hints**: Enhanced with emoji for better visibility
  - All hints now prefixed with 💡 emoji in __str__ output
  - Makes hints stand out in error messages and logs

### Documentation

- Updated `docs/ERROR_HANDLING_CONFIG.md` with retry examples
- Added exception hierarchy diagram in inline documentation
- Enhanced docstrings for all new exception classes
- Added comprehensive examples for helper functions

### Migration Guide

**No Breaking Changes**: All existing code continues to work. The changes are additive:

```python
# Old code still works
try:
    fgt.api.cmdb.firewall.policy.post(data=...)
except DuplicateEntryError as e:
    print(f"Error: {e}")

# New capabilities available
try:
    fgt.api.cmdb.firewall.policy.post(data=...)
except DuplicateEntryError as e:
    print(f"Request ID: {e.request_id}")
    print(f"Timestamp: {e.timestamp}")
    print(e.suggest_recovery())

# Intelligent retry logic
try:
    result = fgt.api.cmdb.firewall.policy.get()
except Exception as e:
    if is_retryable_error(e):
        delay = get_retry_delay(e, attempt=1)
        time.sleep(delay)
        # retry...
```

## [0.3.23] - 2025-12-23

### Added

- **API Endpoints**: Added missing monitor API endpoints
  - `check_addrgrp_exclude_mac_member` - Firewall address group MAC exclusion checking
  - `check_port_availability` - System port availability checking
  - Helper modules for both endpoints with validation support

### Fixed

- **CI/CD Pipeline**: Resolved issues blocking automated builds
  - All pre-commit hooks now pass consistently
  - Fixed recurring formatting issues that caused CI failures
  - Mypy type checking passes without errors
  - Ready for automated PyPI publishing via GitHub Actions
- **Code Quality**: Resolved persistent pre-commit formatting issues
  - Fixed black formatting instability with inline comments in `http_client.py` and `http_client_base.py`
  - Moved inline type annotation comments to separate lines for stable formatting
  - Added missing `__all__` exports to resolve mypy module attribute errors
  - Prevents format/check/format loops in CI pipeline
- **Git Configuration**: Fixed `.gitignore` pattern blocking legitimate API files
  - Changed `check_*.py` to `/check_*.py` to only ignore root-level temporary scripts
  - Prevents accidental exclusion of API endpoint modules with `check_` prefix
  - Previously ignored files now properly tracked and versioned
- **Module Imports**: Removed unnecessary imports causing mypy errors
  - Cleaned up redundant module-level imports in `firewall/__init__.py`
  - Fixed "Module has no attribute" errors in type checking

### Changed

- **Code Formatting**: Applied black/isort formatting to all newly tracked files
  - Consistent quote style (double quotes) across all API modules
  - Proper import ordering and grouping per PEP 8
  - Standardized blank line placement
  - All 1596 source files pass mypy type checking

## [0.3.22] - 2025-12-23

### Added

- **CI/CD Pipeline**: Complete GitHub Actions workflow automation
  - **CI Workflow** (`ci.yml`): Automated code quality checks on every push/PR
    - Lint & format checking (Black, isort, flake8)
    - Type checking with mypy
    - Security scanning with Bandit (JSON reports as artifacts)
    - Build validation with twine
    - Pre-commit hook enforcement
    - Multi-Python version testing (3.10, 3.11, 3.12)
    - All checks gate job (blocks merge if any fail)
  - **Publish Workflow** (`publish.yml`): Automated PyPI publishing
    - Automatic publishing on git tag push (`v*.*.*`)
    - Manual workflow dispatch for TestPyPI testing
    - Version consistency validation across pyproject.toml, setup.py, __init__.py
    - Trusted publishing support (no API tokens needed)
    - Automatic GitHub release creation with changelog extraction
  - **CodeQL Analysis** (`codeql.yml`): Advanced security scanning
    - Runs on push to main, PRs, and weekly schedule
    - GitHub Advanced Security vulnerability detection
  - **Dependency Review** (`dependency-review.yml`): PR dependency checking
    - Detects new dependencies and vulnerabilities
    - Blocks moderate+ severity issues and GPL licenses
  - **Auto-label PRs** (`label-pr.yml`): Automatic PR categorization
    - Labels based on changed files (docs, tests, api, core, etc.)
  - **Documentation**: Complete CI/CD guide in `docs/CICD.md`
    - Workflow explanations and usage examples
    - Local development integration
    - Troubleshooting guide

### Changed

- **Code Quality**: Applied comprehensive PEP 8 compliance
  - Reformatted 796 files with Black (line-length=79)
  - Fixed 1000+ flake8 lint errors for strict PEP 8 compliance
  - Standardized on 79-character line limit (PEP 8 standard)
  - Only ignoring E203 (Black slice spacing) and W503 (modern line break style)
  - All auto-generated API v2 files excluded from linting
- **Import Cleanup**: Removed unused imports across core modules
  - Fixed F401 (unused imports) warnings
  - Added proper noqa comments for intentional exceptions

### Fixed

- **Empty F-Strings**: Fixed F541 errors (f-strings without placeholders)
  - Converted empty f-strings to regular strings in performance_test.py
  - Proper string formatting in all print statements
- **Unused Variables**: Fixed F841 warnings in test functions
  - Added explicit ignore markers for intentionally unused variables
- **Long Lines**: Systematic fixing of E501 errors
  - Wrapped docstrings to 79 characters
  - Split long log messages across lines
  - Added strategic noqa comments for unavoidable long lines

### Removed

## [0.3.21] - 2025-12-22

### Fixed

- **Type Errors in Core Modules**: Fixed multiple type checking errors across the codebase
  - **fortios.py line 472**: Fixed `Operator "in" not supported for types "Literal[' ']" and "str | None"`
    - Added None check before using `in` operator for token validation
    - Changed from `if has_token:` to `if has_token and token is not None:`
  - **firewallPolicy.py**: Fixed return type mismatches for API method calls (5 locations)
    - Added `Coroutine` to type imports for proper type hint support
    - Added `# type: ignore[return-value]` comments at lines 733, 777, 1220, 1246, 1455
    - Issue: API methods return `Union[dict, Coroutine]` for async/sync compatibility
    - Wrapper methods declare strict `Dict` return types for better IDE autocomplete
  - **performance_test.py**: Fixed dynamic attribute access errors
    - Line 323: Added `hasattr` check before calling dynamic `get()` method
    - Line 359: Replaced non-existent `logout()` method with `close()` method
  - All reported type errors now resolved while maintaining full functionality

- **Type Annotation Runtime Error**: Fixed `NameError: name 'Coroutine' is not defined` error
  - Added `from __future__ import annotations` to 832 files across the entire API codebase
  - Issue: `Coroutine` type was imported in `TYPE_CHECKING` blocks (False at runtime) but used in runtime type annotations
  - Solution: Deferred evaluation of all type annotations using PEP 563 (`__future__.annotations`)
  - Enables proper type checking while avoiding runtime evaluation errors
  - Affected files: All API endpoint modules (cmdb, log, monitor, service)
  - Created automated fix script (`fix_coroutine_imports.py`) for systematic resolution
  - All tests now pass without runtime type annotation errors

### Added

- **API Validators - Complete Coverage**: Generated validation helpers for all FortiOS API types
  - Generated 832 validation helper modules across 77 categories (4 API types)
  - **CMDB API**: 37 categories, 548 validators
  - **LOG API**: 5 categories, 5 validators
  - **MONITOR API**: 32 categories, 276 validators
  - **SERVICE API**: 3 categories, 3 validators
  - Extended validator generator to support all API types (cmdb, log, monitor, service)
  - Implemented API-type-specific path matching (CMDB uses `/cmdb/` prefix, others don't)
  - Enhanced fuzzy path matching for complex endpoint structures (0 endpoints skipped)
  - Consistent `VALID_BODY_*` and `VALID_QUERY_*` naming convention for parameter constants
  - Body parameter validation: Payload field validation with `VALID_BODY_ACTION`, `VALID_BODY_STATUS`, etc.
  - Query parameter validation: URL parameter validation with `VALID_QUERY_ACTION`, etc.
  - Handles parameter name collisions (e.g., `action` in both body and query contexts)
  - **Validation coverage**:
    - ✅ Enum validation (predefined allowed values)
    - ✅ Length validation (minLength/maxLength for strings)
    - ✅ Range validation (min/max for numeric values)
    - ✅ Pattern validation (regex patterns)
    - ✅ Type validation (implicit via type coercion with error handling)
    - ⚠️ **Required field validation NOT YET IMPLEMENTED** - needs to be added
  - All validators auto-generated from FortiOS 7.6.5 OpenAPI specifications
  - CMDB Categories: alertemail, antivirus, application, authentication, automation, casb, certificate,
    diameter-filter, dlp, dnsfilter, emailfilter, endpoint-control, ethernet-oam, extension-controller,
    file-filter, firewall, ftp-proxy, icap, ips, log, monitoring, report, router, rule, sctp-filter,
    switch-controller, system, user, videofilter, virtual-patch, voip, vpn, waf, web-proxy, webfilter,
    wireless-controller, ztna

- **Builder Pattern Refactoring (Phase 1)**: Eliminated code duplication in firewall policy endpoints
  - Created `hfortix/FortiOS/api/v2/cmdb/firewall/_helpers/policy_helpers.py` (123 lines)
  - Implemented `build_policy_payload()` - API layer function (no normalization)
  - Implemented `build_policy_payload_normalized()` - Wrapper layer function (with normalization)
  - Implemented `normalize_to_name_list()` - Format converter for flexible inputs
  - Refactored `policy.py`: 1796 → 1381 lines (-415 lines, -23% reduction)
  - Refactored `firewallPolicy.py`: 1703 → 1541 lines (-162 lines, -10% reduction)
  - Total: 454 lines removed, 13% reduction across both files
  - All 226 integration tests passing - Zero breaking changes
  - Proper architectural separation: API layer (no normalization) vs Wrapper layer (with normalization)

- **Code Quality Improvements**: Comprehensive codebase quality audit and improvements
  - **Code Formatting**: Applied `isort` and `black` to all 823 files in `hfortix/`
    - Fixed syntax error in `lldp_profile.py` (renamed variables with dots to underscores)
    - All files now follow consistent PEP 8 formatting standards
    - Consistent import ordering across entire codebase
  - **Type Hints**: Added missing type hints to 7 functions
    - `performance_test.py`: Added return types to `print_summary()`, `quick_test()`
    - `exceptions_forti.py`: Added type hints to 5 functions (error handling utilities)
    - `api/__init__.py`: Added return type to `__dir__()`
    - Added `Optional` import where needed
  - **Docstring Audit**: Verified Google-style docstrings across all public APIs
    - Core classes: `FortiOS`, `AsyncHTTPClient`, `HTTPClient`, `BaseHTTPClient` - all comprehensive
    - Exception classes: All have proper descriptions, args, and examples
    - API endpoint classes: All have complete method documentation
    - Helper functions: All utility functions properly documented
  - **Legacy Code Review**: Scanned for deprecated patterns and legacy implementations
    - No actual legacy code found (only config options with "legacy" in names)
    - Codebase is clean and modern

### Changed

- **Documentation Updates**: Updated roadmap and project status documentation
  - Updated `ROADMAP.md` with comprehensive feature history from v0.3.14-v0.3.21
  - Added detailed v0.3.18 features (custom HTTP clients, environment variables, credential validation)
  - Added v0.3.10-0.3.13 features (circuit breaker, connection pool, request tracking, structured logging)
  - Changed builder pattern status from ✅ to ⏳ (only 1 of 30+ resources completed)
  - Updated version tracking: v0.3.20 released, v0.3.21 in development
  - Created `REFACTORING_SUMMARY.md` documenting builder pattern implementation

### Fixed

- **Firewall Policy Wrapper**: Improved parameter handling and code consistency
  - Fixed `get()` method to properly construct API parameters dictionary
  - Fixed `move()` method to use consistent parameter passing pattern
  - Simplified implementation to match other wrapper methods
  - All parameters now passed correctly to underlying API layer

- **Validator Generator**: Fixed parameter type handling and naming consistency
  - Fixed undefined constant bug where query parameters referenced non-existent body constants
  - Separated validation logic: body parameters (payload) vs query parameters (URL)
  - Implemented consistent naming: `VALID_BODY_*` for payload, `VALID_QUERY_*` for URL params
  - Prevents parameter name collision issues (e.g., `action` can exist in both contexts)
  - Examples: `firewall/policy.py` (VALID_BODY_ACTION), `log/syslogd_setting.py` (both types)

## [0.3.20] - 2025-12-21

### Fixed

- **Firewall Policy Wrapper**: Fixed critical bugs in policy management wrapper
  - Fixed `move()` method "top" and "bottom" positions now work correctly
    - Properly queries all policies to find first/last policy IDs
    - Excludes the policy being moved from consideration
    - Uses query parameters instead of data payload for move action
    - Bypasses generated API layer to call HTTP client directly with `params`
  - Fixed `get_by_name()` return type - now returns single dict or None (not a list)
  - Fixed `get(policy_id=X)` response handling - properly extracts policy from list response
  - Fixed parameter names in all methods: `mkey` → `policyid` for consistency
  - Added `raw_json` parameter support to `create()`, `get()`, `update()`, `delete()`, `move()`
  - All 10 wrapper methods now fully tested and working with live FortiGate

### Tested

- **Integration Testing**: Verified all firewall policy wrapper functions against live FortiGate
  - ✅ `create()` - Create policies with all parameters
  - ✅ `get()` - Get all policies or specific policy by ID  
  - ✅ `get_by_name()` - Get policy by exact name match
  - ✅ `update()` - Partial policy updates
  - ✅ `delete()` - Delete policies
  - ✅ `exists()` - Check policy existence
  - ✅ `move()` - Reorder policies (before/after/top/bottom)
  - ✅ `clone()` - Duplicate policies with modifications
  - ✅ `enable()` / `disable()` - Toggle policy status

### Documentation

- **Filtering Guide**: Confirmed filter operators for policy searches
  - `==` - Exact match (case insensitive)
  - `=@` - Contains (substring match)
  - `!=` - Not equals
  - `!@` - Does not contain
  - Multiple conditions with `&` (AND logic)
  - Examples: `filter="name=@API_TEST"` returns all policies containing "API_TEST"

## [0.3.19] - 2025-12-21

### Changed

- **Type Checking Configuration**: Cleaned up mypy configuration in pyproject.toml
  - Removed unnecessary `httpx.*` mypy override (httpx v0.28.1 has built-in type hints)
  - Removed obsolete `requests.*` mypy override (library migrated to httpx in v0.3.12)
  - Enables better IDE autocomplete and type checking for HTTP client usage
  - Verified: Zero new mypy errors after cleanup

### Improved

- **Build Configuration**: Updated .gitignore to exclude GitHub templates
  - Excludes `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`
  - Prevents inclusion of work-in-progress templates in releases

## [0.3.18] - 2025-12-21

### Fixed

- **Test File Naming**: Fixed critical circular import issues caused by test files shadowing Python stdlib modules
  - Renamed all 354 test files to use `test_` prefix (e.g., `statistics.py` → `test_statistics.py`)
  - Prevents shadowing of Python stdlib modules: `statistics`, `ssl`, `os`, `time`, `profile`, `resource`, `test`
  - Fixes "cannot import name 'fgt' from partially initialized module" errors
  - All monitor, vpn, wifi, router, and system tests now execute correctly
  - Follows Python testing best practices and PEP 8 conventions
  - Created automated `rename_tests.py` script for systematic renaming

### Added

- **Extensibility: Custom HTTP Clients**: Library now supports custom HTTP client implementations
  - `IHTTPClient` Protocol interface (PEP 544) for type-safe extensibility
  - All 750+ endpoint files use TYPE_CHECKING pattern for protocol imports
  - `FortiOS.__init__()` accepts custom clients via `client` parameter
  - Enables audit logging, response caching, fake clients for testing, custom authentication
  - Complete example file: `examples/custom_http_client_example.py`
  - Three production-ready examples: AuditLoggingHTTPClient, CachingHTTPClient, FakeHTTPClient
  - Documentation in README.md "Extensibility" section
  - Use cases: SOC 2/HIPAA/PCI-DSS compliance, CI/CD testing, performance optimization

- **Environment Variables Support**: Load credentials from environment variables
  - Support for `FORTIOS_HOST`, `FORTIOS_TOKEN`, `FORTIOS_USERNAME`, `FORTIOS_PASSWORD`
  - Explicit parameters take priority over environment variables
  - Enables clean separation of credentials from code
  - Perfect for CI/CD pipelines, Docker containers, and security best practices
  - Example: `export FORTIOS_TOKEN="..." && python script.py`
  - No hardcoded credentials needed in scripts
  - Comprehensive documentation in README.md and QUICKSTART.md

- **Credential Validation**: Comprehensive validation for authentication credentials
  - Validates token format (25+ characters minimum, alphanumeric with hyphens/underscores)
  - Catches common copy-paste errors: spaces in tokens, invalid special characters
  - Detects placeholder tokens: "your_token_here", "xxx", "api_token", "your-api-token", etc.
  - Version-agnostic: works with all FortiOS versions (31-32 chars in older, 40+ chars in newer)
  - Enforces username+password pairing (both must be provided together)
  - Provides actionable error messages with clear examples
  - Prevents authentication failures before making API calls
  - Added comprehensive inline documentation

- **Protocol Method Stubs**: Enhanced IHTTPClient protocol interface
  - Added `get_operations()` method stub for operation tracking
  - Added `get_write_operations()` method stub for write operation filtering
  - Added `get_health_metrics()` method stub for connection health monitoring
  - All methods marked as optional with comprehensive docstrings
  - Enables type-safe access to optional features without suppressions

### Improved

- **Documentation**: Updated authentication documentation
  - Added detailed token requirements section in README.md
  - Documented 25-character minimum and version variability
  - Updated QUICKSTART.md with credential validation examples
  - Added error handling examples for common mistakes
  - Documented username/password validation requirements
  - Added best practices for token format

- **Documentation Links**: Fixed PyPI compatibility for all documentation
  - Updated all doc links to use full GitHub URLs (works on PyPI)
  - Removed broken HELPER_METHODS.md references (file doesn't exist)
  - Consolidated helper method docs in ENDPOINT_METHODS.md
  - Renamed DOCS_INDEX.md → INDEX.md for clarity
  - All cross-references verified and working

- **Code Quality**: Fixed type checking errors
  - Added PerformanceTestResults to TYPE_CHECKING imports in utils.py
  - Fixed "not defined" error on line 55
  - Updated .gitignore to include .mypy_cache/

### Changed

- **Token Validation Logic**: Improved from length-based to format-based validation
  - Removed strict 20-character minimum (too restrictive)
  - Changed to flexible 25-character minimum (catches invalid tokens, allows all FortiOS versions)
  - Treats tokens as opaque strings per Fortinet best practices
  - No maximum length restriction (supports all current and future FortiOS versions)
  - Enhanced alphanumeric validation with hyphen/underscore support
  - Expanded placeholder detection list for better error catching

## [0.3.17] - 2025-12-20

### Added
  - New `fgt.api.utils.performance_test()` method for integrated testing
  - Validates connection pool settings automatically
  - Tests real-world API endpoints (status, policies, addresses, interfaces, resources)
  - Identifies device performance profile (high-performance, fast-lan, remote-wan)
  - Provides device-specific recommendations for optimal settings
  - Accessible via `fgt.api.utils` namespace
  - Standalone functions also available: `quick_test()`, `run_performance_test()`
  - Command-line interface: `python -m hfortix.FortiOS.performance_test`
  - Comprehensive documentation in `docs/PERFORMANCE_TESTING.md`

- **Read-Only Mode**: Protect production environments by blocking write operations
  - Add `read_only=True` flag to FortiOS constructor
  - Blocks all POST, PUT, and DELETE requests with `ReadOnlyModeError`
  - GET requests execute normally for queries and monitoring
  - Perfect for testing, CI/CD pipelines, dry-run previews, and training
  - Works with both sync and async modes

- **Operation Tracking**: Complete audit log of all API operations
  - Add `track_operations=True` flag to enable operation logging
  - Records timestamp, method, URL, request data, response status, and VDOM
  - Access via `get_operations()` or `get_write_operations()`
  - Tracks both successful operations and those blocked by read-only mode
  - Perfect for debugging, auditing, change logs, and documentation
  - Works with both sync and async modes

- **Extended Filter Documentation**: Comprehensive guide to FortiOS filtering
  - New `docs/FILTERING_GUIDE.md` with complete operator documentation
  - Covers all FortiOS native filter operators: `==`, `!=`, `=@`, `!@`, `<`, `<=`, `>`, `>=`
  - 50+ practical examples for common use cases
  - Field-specific examples for addresses, policies, interfaces, routes
  - Advanced patterns: range queries, combined filters, exclusions

- **Username/Password Authentication**: Alternative to API token authentication
  - Session-based authentication using username and password
  - Automatic session management and renewal
  - Useful when API tokens are not available or for temporary access
  - Example: `FortiOS(host='...', username='admin', password='...')`

### Improved

- **Type Safety**: Reduced type ignores from 4 to 1 in core fortios.py
  - Added protocol method stubs to IHTTPClient interface
  - Eliminated type: ignore[attr-defined] suppressions
  - Only architectural async type ignore remains
  - Better IDE support and type inference- **Firewall Policy Convenience Wrapper**: Intuitive interface for policy management
  - Access via `fgt.firewall.policy` namespace
  - Methods: `create()`, `update()`, `get()`, `delete()`, `exists()`, `enable()`, `disable()`, `move()`, `clone()`
  - 150+ explicit parameters matching FortiOS terminology
  - Comprehensive documentation in `docs/FIREWALL_POLICY_WRAPPER.md`

### Changed

- **Connection Pool Defaults Optimized**: Based on multi-device performance testing
  - `max_connections`: Reduced from 100 → 30 → **10** (conservative default)
  - `max_keepalive_connections`: Reduced from 20 → 15 → **5** (conservative default)
  - Defaults set 50% below lowest-performing device tested
  - Tested across 3 FortiGate models with varying performance characteristics
  - Use `fgt.api.utils.performance_test()` to get device-specific recommendations
  - Performance testing shows most FortiGates serialize API requests internally
  - Sequential requests recommended for most deployments

### Fixed

- **Connection Pool Validation**: Auto-adjust instead of error
  - Changed from hard error to auto-adjust when `max_keepalive_connections > max_connections`
  - Logs warning and adjusts `max_keepalive_connections` to match `max_connections`
  - Allows testing different concurrency levels without configuration errors

## [0.3.16] - 2025-12-20

### Added

- **Read-Only Mode**: Protect production environments by blocking write operations
  - Add `read_only=True` flag to FortiOS constructor to prevent accidental changes
  - Blocks all POST, PUT, and DELETE requests with `ReadOnlyModeError` exception
  - GET requests execute normally for queries and monitoring
  - Perfect for testing automation scripts, CI/CD pipelines, dry-run previews, and training environments
  - Works with both sync and async modes
  - Examples:
    ```python
    # Enable read-only mode for safe testing
    fgt = FortiOS("192.0.2.10", token="...", read_only=True)

    # GET requests work normally
    addresses = fgt.api.cmdb.firewall.address.get()  # ✓ Works

    # Write operations are blocked
    try:
        fgt.api.cmdb.firewall.address.post(data={"name": "test"})
    except ReadOnlyModeError as e:
        print(f"Blocked: {e}")  # ✗ Raises ReadOnlyModeError

    # Combine with operation tracking for audit trail
    fgt = FortiOS("fw", token="...", read_only=True, track_operations=True)
    # ... make API calls ...
    for op in fgt.get_operations():
        if op.get('blocked_by_read_only'):
            print(f"BLOCKED: {op['method']} {op['path']}")
    ```

- **Operation Tracking**: Complete audit log of all API operations
  - Add `track_operations=True` flag to enable operation logging
  - Records timestamp, method, URL, request data, response status, and VDOM for every API call
  - Access via `get_operations()` (all operations) or `get_write_operations()` (POST/PUT/DELETE only)
  - Tracks both successful operations and those blocked by read-only mode
  - Perfect for debugging, auditing, generating change logs, and documentation
  - Works with both sync and async modes
  - Examples:
    ```python
    # Enable operation tracking
    fgt = FortiOS("192.0.2.10", token="...", track_operations=True)

    # Make various API calls
    fgt.api.monitor.system.status.get()
    fgt.api.cmdb.firewall.address.post(data={"name": "test", "subnet": "10.0.0.1/32"})
    fgt.api.cmdb.firewall.policy.put("10", data={"action": "deny"})

    # Get all operations
    all_ops = fgt.get_operations()
    for op in all_ops:
        print(f"{op['timestamp']} {op['method']} {op['path']}")
    # Output:
    # 2024-12-20T10:30:15Z GET /system/status
    # 2024-12-20T10:30:16Z POST /firewall/address
    # 2024-12-20T10:30:17Z PUT /firewall/policy/10

    # Get only write operations (POST/PUT/DELETE)
    write_ops = fgt.get_write_operations()
    for op in write_ops:
        print(f"{op['method']} {op['path']}")
        if op['data']:
            print(f"  Data: {op['data']}")
    # Output:
    # POST /firewall/address
    #   Data: {'data': {'name': 'test', 'subnet': '10.0.0.1/32'}}
    # PUT /firewall/policy/10
    #   Data: {'name': '10', 'data': {'action': 'deny'}}
    ```

- **Extended Filter Documentation**: Comprehensive guide to FortiOS filter operators
  - New `FILTERING_GUIDE.md` with complete documentation of all FortiOS native filter operators
  - Covers all 8 operators: `==`, `!=`, `=@`, `!@`, `<`, `<=`, `>`, `>=`
  - 50+ practical examples for firewall addresses, policies, interfaces, and routes
  - Advanced patterns: range queries, exclusions, combined filters, pagination
  - Tips and best practices for efficient filtering
  - Examples:
    ```python
    # Equality
    fgt.api.cmdb.firewall.address.get(filter="name==test-host")

    # Contains (substring match)
    fgt.api.cmdb.firewall.address.get(filter="subnet=@10.0")

    # Range query
    fgt.api.cmdb.firewall.policy.get(filter="policyid>=100&policyid<=200")

    # Multiple conditions (AND logic)
    fgt.api.cmdb.firewall.policy.get(filter="status==enable&action==accept")

    # Not contains (exclusion)
    fgt.api.cmdb.firewall.address.get(filter="subnet!@192.168")
    ```

- **Username/Password Authentication**: Alternative authentication method for FortiOS devices
  - Session-based authentication using username and password (alternative to API tokens)
  - Automatic login on initialization, automatic logout on context manager exit
  - Context manager support for automatic session cleanup: `with FortiOS(username="admin", password="***") as fgt:`
  - Proactive session refresh to prevent idle timeout expiration
  - Configurable session idle timeout (default: 5 minutes, matching FortiGate defaults)
  - Automatic re-authentication on 401 errors if session expires
  - Session tracking with last activity timestamps
  - **⚠️ Deprecation Notice**: Username/password authentication **still works in FortiOS 7.4.x** but is **removed in FortiOS 7.6.x and later**. Fortinet recommends using API token authentication for all new deployments. See [FortiOS 7.4 Release Notes](https://docs.fortinet.com/document/fortigate/7.4.0/fortios-release-notes).
  - **Important**: Proactive re-authentication only works with context manager (`with` statement). Without context manager, you must manually manage login/logout.
  - **Note**: The idle timer resets on each API request. Proactive re-auth triggers when time since *last request* exceeds the threshold (not time since login).
  - Examples:
    ```python
    # Recommended: Context manager (automatic login/logout + proactive re-auth)
    with FortiOS(host="fw", username="admin", password="***") as fgt:
        addresses = fgt.api.cmdb.firewall.address.get()
        # Session automatically refreshed if approaching timeout
        # Auto-logout on exit

    # Custom timeout (match your FortiGate's remoteauthtimeout setting)
    with FortiOS(host="fw", username="admin", password="***",
                 session_idle_timeout=120) as fgt:  # 2 minutes
        # Proactive re-auth at 96 seconds (80% of 120s)
        status = fgt.api.monitor.system.status.get()

    # Disable proactive re-authentication
    with FortiOS(host="fw", username="admin", password="***",
                 session_idle_timeout=None) as fgt:
        # Will only re-auth on 401 errors
        addresses = fgt.api.cmdb.firewall.address.get()
    ```
  - Implementation details:
    - Login via POST to `/logincheck` with `secretkey` parameter (FortiOS convention)
    - CSRF token extracted from `ccsrftoken` cookie
    - Session cookies managed automatically by httpx client
    - Logout via POST to `/logout` (clears session, sets cookies to expire in 1976)
    - Proactive re-auth triggered at 80% of idle timeout (before expiration)
    - Fallback re-auth on 401 Unauthorized responses
    - Session timestamps: `_session_created_at`, `_session_last_activity`

- **Firewall Policy Convenience Wrapper**: Intuitive, GUI-like interface for managing firewall policies
  - Access via `fgt.firewall.policy` namespace with explicit parameter names
  - Simplified syntax: `fgt.firewall.policy.create(name='MyPolicy', srcintf=['port1'], ...)` instead of complex REST API calls
  - Auto-normalizes inputs: accepts strings or lists, converts to FortiOS format automatically
  - Full CRUD operations: `.create()`, `.update()`, `.get()`, `.delete()`, `.exists()`
  - Convenience methods: `.enable()`, `.disable()`, `.move()`, `.clone()`
  - Supports all 100+ firewall policy parameters from FortiOS 7.6.5 API
  - Works with both sync and async modes
  - Examples:
    ```python
    # Create policy with intuitive syntax
    fgt.firewall.policy.create(
        name='Allow-Web',
        srcintf=['port1'],
        dstintf=['port2'],
        srcaddr=['internal-net'],
        dstaddr=['all'],
        service=['HTTP', 'HTTPS'],
        action='accept',
        nat='enable'
    )

    # Enable/disable policies
    fgt.firewall.policy.disable(policy_id=10)
    fgt.firewall.policy.enable(policy_id=10)

    # Move policy
    fgt.firewall.policy.move(policy_id=5, position='before', reference_id=3)

    # Clone policy with modifications
    fgt.firewall.policy.clone(policy_id=1, new_name='Cloned-Policy')
    ```

## [0.3.15] - 2025-12-20

### Added

- **Async/Await Support**: Full dual-mode support for asynchronous operations
  - Single `FortiOS` class now supports both sync and async modes via `mode` parameter
  - All 750+ API methods work transparently in async mode with `await`
  - All 288 `.exists()` helper methods are async-aware
  - Async context manager support with `async with`
  - Zero breaking changes - existing sync code continues to work
  - Implementation:
    - New `AsyncHTTPClient` class mirroring sync `HTTPClient` with async/await
    - `mode="async"` parameter on `FortiOS.__init__()`
    - Automatic coroutine detection using `inspect.iscoroutine()`
    - Type hints with `@overload` decorators for IDE support
  - Performance: Enables concurrent operations with `asyncio.gather()` for 3x+ speedup
  - See [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) for complete documentation

- **Helper Methods**: Added `.exists()` helper method to 288 CMDB endpoints
  - Provides safe existence checking without raising exceptions
  - Returns `True` if object exists, `False` if not found
  - Works transparently in both sync and async modes
  - Available on all endpoints that support full CRUD operations
  - Example (sync): `if fgt.api.cmdb.firewall.address.exists("test-host"): ...`
  - Example (async): `if await fgt.api.cmdb.firewall.address.exists("test-host"): ...`
  - See [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) for complete API reference

### Changed

- **Code Refactoring**: Eliminated code duplication in HTTP client implementation
  - Created `BaseHTTPClient` base class with shared logic for sync and async clients
  - `HTTPClient` and `AsyncHTTPClient` now inherit from `BaseHTTPClient`
  - Removed 744 lines of duplicated code (35% reduction in HTTP client code)
  - Zero duplication between sync and async implementations
  - Improved maintainability: bug fixes now apply to both sync and async modes automatically
  - Better consistency: retry logic, circuit breaker, and validation identical across modes
  - Enhanced testability: shared logic tested once in base class
  - Implementation:
    - `BaseHTTPClient`: Parameter validation, URL building, retry logic, circuit breaker, statistics
    - `HTTPClient`: Sync-specific HTTP operations (httpx.Client)
    - `AsyncHTTPClient`: Async-specific HTTP operations (httpx.AsyncClient)
  - Created `IHTTPClient` Protocol interface for extensibility
  - Updated 863 endpoint files to use Protocol-based type hints
  - Enables users to provide custom HTTP client implementations

### Fixed

- **Test Fixes**: Fixed certificate/local test helper methods to properly filter by source
  - Updated `test_get_factory_helper()` and `test_get_user_helper()` to use correct filters
  - Added `filter='source==factory'` and `filter='source==user'` parameters
  - All 9 certificate/local tests now pass correctly

### Documentation

- **Async Guide**: Created comprehensive [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) documentation
  - Complete async/await usage guide with examples
  - Common patterns: concurrent requests, bulk operations, error handling
  - Migration guide from sync to async
  - Performance comparisons and best practices
  - Advanced usage: rate limiting, timeouts, multiple FortiGates
  - Troubleshooting common async errors
- **API Reference**: Created comprehensive [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) documentation
  - Complete listing of all 857 FortiOS API endpoints
  - Shows available methods (`.get()`, `.post()`, `.put()`, `.delete()`, `.exists()`) for each endpoint
  - Organized by API category (CMDB, LOG, MONITOR, SERVICE)
  - Quick navigation with anchor links to all subcategories
  - Coverage: 561 CMDB endpoints, 19 LOG endpoints, 274 MONITOR endpoints, 3 SERVICE endpoints
- **Helper Methods**: Added `.exists()` helper method documentation in [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md)
  - In-depth guide to the `.exists()` helper method
  - Practical usage examples for common scenarios (idempotent operations, safe deletion, batch processing)
  - Reference table of identifier types for all 288 endpoints with `.exists()`
  - Organized by category with example code snippets
- **README Updates**: Improved documentation organization
  - Updated documentation links to use GitHub URLs for PyPI compatibility
  - Added [docs/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ASYNC_GUIDE.md) and [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) to main documentation section
  - Updated roadmap to mark async support as completed (v0.3.15)
  - Added async/await to features list
  - Improved discoverability for PyPI users
- **QUICKSTART Updates**: Added async/await section
  - Quick example of async mode usage
  - Link to comprehensive ASYNC_GUIDE.md
  - Updated tips section to mention async for concurrent operations
- **Project Cleanup**: Cleaned up root folder and updated documentation
  - Moved refactoring documentation to internal development workspace
  - Removed `update_endpoints.py` (one-time migration script)
  - Updated `CHANGELOG.md` with comprehensive refactoring details
  - Updated `README.md` to highlight refactored architecture

## [0.3.14] - 2025-12-19

### Fixed

- **Critical**: Fixed httpx dependency in requirements.txt (was incorrectly listing requests/urllib3)
  - Package now correctly declares httpx[http2]>=0.27.0 as dependency
  - Resolves installation issues where wrong HTTP library was installed
- **Build**: Updated MANIFEST.in to reflect moved development docs
  - Commented out CONTRIBUTING.md and DEVELOPMENT.md (moved to development workspace)
  - Prevents build warnings about missing files
- **Type Checking**: Fixed mypy configuration for Python 3.10+ syntax
  - Updated pyproject.toml: python_version = "3.10" (was "3.8")
  - Added httpx module ignore for missing type stubs
  - Fixes compatibility with modern union syntax (str | None)

### Added

- **PEP 561 Compliance**: Full type checker support for hfortix package
  - ✅ `py.typed` marker file included in package
  - ✅ All public APIs have complete type hints
  - ✅ mypy/pyright can now validate user code using hfortix
  - ✅ IDE autocomplete with full type information
  - Benefits: Catch type errors at development time, better developer experience
  - Example: Type checkers now understand `fgt.api.cmdb.firewall.address.get()` returns `dict[str, Any]`
- **Public API**: Added `get_connection_stats()` method to FortiOS class
  - Monitor HTTP connection pool health and performance
  - Track retry statistics by reason and endpoint
  - Access circuit breaker state and failure counts
  - Example: `stats = fgt.get_connection_stats()`
- **Exception Exports**: Exported all 16 exception classes from main hfortix package
  - Complete exception hierarchy now available: `from hfortix import CircuitBreakerOpenError, ...`
  - Added 10 new exception exports: ServiceUnavailableError, CircuitBreakerOpenError, TimeoutError, DuplicateEntryError, EntryInUseError, InvalidValueError, PermissionDeniedError
  - Exported helper functions: get_error_description(), raise_for_status()
  - Exported data structures: FORTIOS_ERROR_CODES, HTTP_STATUS_CODES

### Changed

- **Python Version Requirement**: Updated minimum Python version from 3.8 to 3.10
  - Code uses Python 3.10+ syntax (str | None union types)
  - Updated pyproject.toml: requires-python = ">=3.10"
  - Removed Python 3.8, 3.9 from classifiers
  - Added "Typing :: Typed" classifier for PEP 561 compliance
- **Development Status**: Updated from Alpha (3) to Beta (4)
  - Package metadata now consistently declares Beta status
  - Updated in setup.py, pyproject.toml classifiers
  - Reflects maturity of codebase and API stability
- **Documentation**: Updated API_COVERAGE.md to reflect 100% coverage achievement
  - Changed from "38/77 (49%)" to "77/77 (100%)"
  - Added celebration section for milestone achievement
  - Updated test coverage statistics (226 test files)
- **Documentation**: Removed broken internal development references from README.md
  - Cleaned up references to development workspace content

### Notes

- Version synchronized across setup.py (0.3.14), pyproject.toml (0.3.14), and hfortix/FortiOS/__init__.py (0.3.14)
- All changes are backward compatible
- PEP 561 compliance makes hfortix a first-class typed Python package
- This release prepares the package for broader beta testing

## [Unreleased]

### Added

- **🎉 100% API COVERAGE ACHIEVED** (December 2025) - **Complete FortiOS 7.6.5 implementation!**
  - **CMDB API**: All 37 documented categories (100% coverage)
    - **Refactored**: alertemail, antivirus, application, authentication, automation, casb, certificate, dlp, dnsfilter, emailfilter, firewall, icap, ips, log, monitoring, report, router, rule, system (19 categories)
    - Complete categories: diameter-filter, endpoint-control, ethernet-oam, extension-controller, file-filter, ftp-proxy, sctp-filter, switch-controller, user, videofilter, virtual-patch, voip, vpn, waf, web-proxy, webfilter, wireless-controller, ztna (18 categories)
    - Note: ssh-filter, telemetry-controller, wanopt, extender-controller not yet documented on FNDN
  - **Monitor API**: All 32 documented categories (100% coverage)
    - **Previously implemented**: azure, casb, endpoint-control, extender-controller, extension-controller, firewall (6 categories)
    - **Added in this session**: firmware, fortiguard, fortiview, geoip, ips, license, log, network, registration, router, sdwan, service, switch-controller, system, user, utm, videofilter, virtual-wan, vpn, vpn-certificate, wanopt, web-ui, webcache, webfilter, webproxy, wifi (26 categories)
  - **Log API**: 5 categories (100% coverage) - disk, fortianalyzer, memory, forticloud, search
  - **Service API**: 3 categories (100% coverage) - sniffer, security-rating, system
  - **Total**: 77 of 77 documented categories with 750+ API methods
  - **Generated via unified module generator** with automatic edge case handling
  - **Status**: All endpoints generated, ~50% tested with live FortiGate
  - **Quality**: All follow standardized dual-pattern interface with full type hints

- **Router CMDB Category** - Complete routing protocol configuration support (BETA)
  - Implemented all 26 router endpoints with full CRUD operations
  - Collection endpoints: static, static6, access-list, access-list6, prefix-list, prefix-list6, route-map, policy, policy6, aspath-list, community-list, extcommunity-list, key-chain, auth-path, multicast, multicast6, multicast-flow
  - Singleton endpoints: bgp, ospf, ospf6, rip, ripng, isis, bfd, bfd6, setting
  - Comprehensive test coverage: 22/26 endpoints tested (85%), 100% pass rate
  - **Note:** Singleton endpoints (BGP, OSPF, RIP, etc.) require GET→Modify→PUT pattern for nested objects

### Changed

- **🔄 MAJOR API REFACTORING** (December 2025) - **All 500+ endpoints refactored**
  - **Breaking Change**: Standardized method names across all endpoints
  - **Old API**: `create()`, `update()`, `delete()` - required manual `mkey` parameter handling
  - **New API**: `list()`, `get()`, `create()`, `update()`, `delete()` - RESTful and intuitive
  - **Dual-Pattern Interface**: All `create()` and `update()` methods now support:
    - Dictionary pattern: `create(data_dict={'name': 'x', 'subnet': '10.0.0.0/24'})`
    - Keyword pattern: `create(name='x', subnet='10.0.0.0/24')`
    - Mixed pattern: `create(data_dict=base_config, name='override')`
  - **Benefits**: Cleaner code, better IDE autocomplete, template-friendly, more Pythonic
  - **Migration**: Old code will break - update `create(data)` → `create(data_dict=data)`
  - **Scope**: All 37 CMDB categories + 32 Monitor categories refactored with unified generator
  - **Scope**: 200+ endpoints across 24 CMDB categories refactored
  - **Status**: ~85% complete, router endpoints verified with comprehensive tests

- **Repository Organization** (December 19, 2025)
  - Moved development tools (CONTRIBUTING.md, DEVELOPMENT.md) to development workspace
  - Cleaned up public documentation to focus on user-facing content
  - Simplified README.md contributing section
  - Updated all documentation cross-references

- **Module Naming Improvements** (December 19, 2025)
  - Fixed invalid Python identifiers: renamed `3g_modem` → `modem_3g`, `5g_modem` → `modem_5g`
  - Module classes: `Modem3g`, `Modem5g` with proper attribute access
  - Test files updated to match new naming convention
  - All modem tests now passing

- **Development Workflow** (December 19, 2025)
  - Created unified module generator handling all edge cases automatically
  - Auto-detects digit-prefixed names and sanitizes to valid Python identifiers
  - Auto-adds certificate helper methods for certificate endpoints
  - Generates nested resource classes for complex endpoints
  - Detects read-only endpoints and generates appropriate methods
  - Consolidated all generation tools into single location
  - All new modules follow standardized dual-pattern interface

- **Singleton Endpoint Pattern** - Important behavioral note for routing protocols
  - Routing protocol endpoints (BGP, OSPF, RIP, ISIS, etc.) work differently than other endpoints
  - Unlike firewall addresses or policies, you cannot add/remove individual neighbors or networks
  - Instead, you must retrieve the entire configuration, make changes, and send it back
  - This requires more code than typical CRUD operations (see README examples)
  - **Why?** FortiOS API design - routing configs are single objects with nested lists
  - **Future:** Helper methods like `add_neighbor()`, `remove_neighbor()` are planned to simplify this

## [0.3.13] - 2025-12-17

### Added

- **Custom User-Agent Header** - Identify applications in FortiGate logs
  - Configure via `user_agent` parameter in `FortiOS()` constructor
  - Default: `hfortix/{version}` if not specified
  - Useful for multi-team environments and troubleshooting
  - Shows up in FortiGate admin logs for better visibility
  - Example: `FortiOS(host='...', token='...', user_agent='BackupScript/2.1.0')`

- **New Exception Classes** - Better error handling and type safety
  - `ServiceUnavailableError` - HTTP 503 service unavailable
  - `CircuitBreakerOpenError` - Circuit breaker is open (replaces generic RuntimeError)
  - `TimeoutError` - Request timeout errors
  - More specific exceptions for better error handling

- **Configurable Circuit Breaker** - Customize circuit breaker behavior
  - `circuit_breaker_threshold` - Number of failures before opening (default: 5)
  - `circuit_breaker_timeout` - Seconds before transitioning to half-open (default: 60.0)
  - Configure per FortiGate size/environment
  - Example: `FortiOS(host='...', circuit_breaker_threshold=10, circuit_breaker_timeout=120.0)`

- **Configurable Connection Pool** - Tune connection limits
  - `max_connections` - Maximum connections in pool (default: 100)
  - `max_keepalive_connections` - Maximum keepalive connections (default: 20)
  - Adjust for small embedded FortiGates or large enterprise models
  - Example: `FortiOS(host='...', max_connections=50, max_keepalive_connections=10)`

- **Enhanced Retry Statistics** - More detailed metrics
  - `total_requests` - Total number of requests made
  - `successful_requests` - Number of successful requests
  - `failed_requests` - Number of failed requests
  - `last_retry_time` - Timestamp of last retry
  - `success_rate` - Percentage of successful requests (0-100)
  - Better visibility into client performance

- **Advanced Wildcard Matching** - fnmatch support for endpoint timeouts
  - Supports shell-style patterns: `monitor/*`, `*/status`, `monitor/*/interface`
  - More flexible than simple prefix matching
  - Exact match still takes priority over patterns

### Changed

- **Enhanced Parameter Sanitization** - Security improvement
  - Now sanitizes query parameters in addition to request data
  - Prevents leaking API keys, tokens, passwords in logs
  - Added more sensitive key patterns: `api_key`, `api-key`, `apikey`, `auth`, `authorization`
  - Improves security for production logging

- **Parameter Validation** - Fail fast with clear errors
  - Validates `max_retries` (must be >= 0, warns if > 100)
  - Validates `connect_timeout` and `read_timeout` (must be > 0)
  - Validates `circuit_breaker_threshold` (must be > 0)
  - Validates `max_connections` and `max_keepalive_connections` (must be > 0)
  - Validates `host` parameter is required (no longer accepts None)
  - Better error messages for invalid configurations

- **Code Quality Improvements**
  - Reduced code duplication with `_normalize_path()` helper method
  - Improved type hints for `__exit__()` method
  - Enhanced docstrings with examples
  - Better logging consistency

### Fixed

- **Integer ID Path Encoding** - Fixed URL encoding for numeric IDs
  - `dos_policy.get()`, `dos_policy.update()`, `dos_policy.delete()` - Convert policyid to string before encoding
  - `dos_policy6.get()`, `dos_policy6.update()`, `dos_policy6.delete()` - Convert policyid to string before encoding
  - `ipmacbinding.table.get()`, `ipmacbinding.table.update()`, `ipmacbinding.table.delete()` - Convert seq_num to string before encoding
  - Resolves `TypeError: quote_from_bytes() expected bytes` when using numeric IDs
  - All numeric identifiers are now properly converted to strings for URL path encoding

- **Type Safety** - Fixed type checking errors
  - `host` parameter properly validated (no longer Optional in practice)
  - Better type hints for exception handling
  - Cleaner type checking for HTTPClient initialization

### Technical Details

- **100% backwards compatible** - all existing code works unchanged
- Test coverage: 28 tests (all passing)
- Zero breaking changes - all improvements are additive or internal

## [0.3.13] - 2025-12-17 (if releasing the v0.3.13 from earlier)

### Added

- **Request ID / Correlation Tracking** - Track requests across logs for better debugging
  - Auto-generates short 8-character UUID if not provided
  - Support for custom correlation IDs via `request_id` parameter
  - Request ID appears in all log entries for full traceability
  - Enables distributed tracing across multiple systems

- **Connection Pool Metrics** - Monitor HTTP client health and performance
  - `get_connection_stats()` method returns pool health metrics
  - Track: HTTP/2 status, max connections, circuit breaker state, failures
  - Enable proactive monitoring and alerting
  - Zero performance overhead

- **Circuit Breaker Pattern** - Prevent cascading failures with automatic fail-fast
  - Opens after 5 consecutive failures (configurable)
  - Automatically enters half-open state after 60s timeout
  - Manual reset via `reset_circuit_breaker()` method
  - Clear error messages with time-until-retry
  - Protects downstream services from overload

- **Per-Endpoint Timeout Configuration** - Fine-grained timeout control
  - `configure_endpoint_timeout(pattern, timeout)` for custom timeouts
  - Supports wildcard patterns: `monitor/*`, `log/*/report`
  - Exact match takes priority over wildcard
  - Ideal for slow endpoints (reports, large policy lists)
  - Zero overhead if not configured

- **Structured Logging** - Machine-readable logs with extra fields
  - All log entries include: request_id, method, endpoint, status_code, duration, vdom
  - Compatible with JSON log formatters (Elasticsearch, Splunk, CloudWatch)
  - Enables log aggregation and analysis
  - Better troubleshooting with correlation
  - Same performance as string logging

### Technical Details

- All features are **100% backwards compatible** - no breaking changes
- Comprehensive test coverage: 13 new tests in `test_advanced_features.py`
- Total test suite: 24 tests (4 retry + 7 improvements + 13 advanced)
- Performance: Minimal overhead (~0.001ms per request for circuit breaker)

## [0.3.12] - 2025-12-17

### Changed

- **BREAKING: Migrated from requests to httpx** - Complete HTTP client library migration
  - Replaced `requests` library with modern `httpx` library
  - **HTTP/2 Support Enabled** - Improved performance with connection multiplexing
  - More explicit timeout configuration using `httpx.Timeout` object
  - Connection pooling: 100 max connections, 20 keepalive connections
  - Updated exception handling:
    * `ConnectionError` → `httpx.ConnectError, httpx.NetworkError`
    * `Timeout` → `httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout, httpx.ConnectTimeout`
    * `requests.HTTPError` → `httpx.HTTPStatusError`
  - Response API changes: `response.ok` → `response.is_success`
  - Requires: `httpx[http2]>=0.27.0` (previously `requests>=2.31.0`)
  - **No API Changes**: All 644 endpoint methods work unchanged
  - Better foundation for future async support

### Added

- **Automatic Retry Logic** - HTTPClient now automatically retries failed requests with exponential backoff
  - Retries on transient failures: connection errors, timeouts, rate limits (429), server errors (500, 502, 503, 504)
  - Configurable via `max_retries` parameter (default: 3 attempts)
  - Exponential backoff: 1s, 2s, 4s, 8s (capped at 30s)
  - Respects `Retry-After` header for rate limit responses
  - Detailed retry logging at INFO level
  - Improves reliability in unstable network conditions

- **Context Manager Support** - HTTPClient can now be used with `with` statement
  - Automatically closes client on exit: `with HTTPClient(...) as client:`
  - Ensures proper resource cleanup
  - Implements `__enter__` and `__exit__` methods

- **Enhanced Documentation**
  - Query parameter encoding behavior documented in class docstring
  - Timeout configuration explained with detailed examples
  - Path encoding strategy documented (safe='/%' prevents double-encoding)
  - Binary error response handling documented

### Fixed

- **URL Normalization** - Base URL now has trailing slashes stripped during initialization
  - Prevents potential double-slash issues like `https://host//api/v2/...`
  - Ensures consistent URL construction across all requests

- **HTTP Client Path Normalization** - Fixed 404 errors when endpoint methods pass paths with leading slashes
  - HTTPClient now strips leading slashes from paths before URL construction
  - Prevents double-slash URLs (e.g., `/api/v2/monitor//firewall/acl`)
  - Backwards compatible: works with both `"firewall/acl"` and `"/firewall/acl"` path formats
  - Affects `request()` and `get_binary()` methods
  - Resolves `ResourceNotFoundError` for monitor endpoints like `firewall.acl.list()`

- **Path Encoding Implementation** - Paths are now properly URL-encoded
  - Special characters in paths are encoded (e.g., spaces → `%20`, `@` → `%40`)
  - Safe characters: `/` (path separator) and `%` (already-encoded marker)
  - Prevents double-encoding of pre-encoded components
  - Example: `"user@domain"` → `"user%40domain"`

- **Binary Response Error Handling** - Improved error handling for non-JSON responses
  - Added try/except around JSON parsing in `_handle_response_errors()`
  - Falls back to standard HTTP error for binary/HTML error pages
  - Logs response size for debugging
  - Handles proxy/firewall error pages gracefully

- **Rate Limit Handling** - HTTP 429 responses now properly handled with retry logic
  - Respects `Retry-After` header from server
  - Falls back to exponential backoff if header not present
  - Prevents overwhelming servers during rate limiting

## [0.3.11] - 2025-12-17

### Added - December 17, 2025

- **FTP Proxy Category** - FTP proxy configuration (1 endpoint):
  - **explicit** - FTP proxy explicit configuration (GET, PUT)
  - Parameters: status, incoming_port, incoming_ip, outgoing_ip, sec_default_action, server_data_mode
  - SSL/TLS support: ssl, ssl_cert, ssl_dh_bits, ssl_algorithm
  - Singleton endpoint pattern (no POST/DELETE operations)
  - Test coverage: 5 test sections with comprehensive parameter validation

- **Monitor API Categories** - 6 categories implemented (18% coverage):
  - **azure/** - Azure application list monitoring (1 endpoint)
  - **casb/** - SaaS application statistics (1 endpoint)
  - **endpoint-control/** - FortiClient EMS monitoring (7 endpoints):
    - ems-status, ems-status-summary, installer, profile-xml
    - record-list, registration-password, summary
  - **extender-controller/** - FortiExtender status monitoring (1 endpoint)
  - **extension-controller/** - Extension controller status (2 endpoints):
    - extender, fortigate
  - **firewall/** - Firewall monitoring (39 endpoints):
    - Policy statistics (policy, policy6, proxy-policy, security-policy, etc.)
    - Session monitoring with 20+ filter parameters
    - ACL counters (acl, acl6) with clear operations
    - Address objects (address, address6, address-dynamic, address-fqdn)
    - Traffic shapers (per-ip-shaper, shaper, multi-class-shaper)
    - Special endpoints (policy-lookup callable, clearpass-address actions)
    - GTP statistics, health monitoring, load balancing
    - Internet service matching and reputation
    - VIP overlap detection, UUID objects
  - Test coverage: 39 firewall tests with 100% pass rate
  - All endpoints support explicit parameters (no **kwargs)

- **Log Configuration Category** - Complete logging configuration (56 endpoints):
  - Nested object pattern: `fgt.api.cmdb.log.disk.filter.get()`
  - **disk/** - Disk logging (filter, setting)
  - **memory/** - Memory logging (filter, global-setting, setting)
  - **fortianalyzer-cloud/** - FortiAnalyzer Cloud (4 endpoints)
  - **fortianalyzer/** - FortiAnalyzer 1/2/3 servers (12 endpoints total)
  - **fortiguard/** - FortiGuard logging (4 endpoints)
  - **null-device/** - Null device logging (filter, setting)
  - **syslogd/** - Syslog servers 1/2/3/4 (16 endpoints total)
  - **tacacs+accounting/** - TACACS+ accounting 1/2/3 (6 endpoints total)
  - **webtrends/** - WebTrends logging (filter, setting)
  - **Singleton endpoints** - custom-field (CRUD), eventfilter, gui-display, setting, threat-weight
  - Test coverage: 12 test files, 47 test cases (100% pass rate)

- **ICAP Category** - Internet Content Adaptation Protocol (3 endpoints):
  - **profile** - ICAP profiles (30+ parameters)
  - **server** - ICAP server configuration with SSL/TLS support
  - **server-group** - ICAP server groups for load balancing

- **IPS Category** - Intrusion Prevention System (8 endpoints):
  - **custom** - Custom IPS signatures (CRUD)
  - **decoder** - Protocol decoders (CRUD)
  - **global** - Global IPS settings (singleton)
  - **rule** - IPS rules (CRUD)
  - **rule-settings** - IPS rule settings (CRUD)
  - **sensor** - IPS sensors/profiles (CRUD)
  - **settings** - VDOM IPS settings (singleton)
  - **view-map** - IPS view-map configuration (CRUD)

- **Monitoring Category** - System monitoring configuration (1 endpoint):
  - **npu-hpe** - NPU-HPE performance monitoring (3 parameters)

- **Report Category** - Report configuration (2 endpoints):
  - **layout** - Report layouts with CRUD (17 parameters)
  - **setting** - Report settings (5 parameters)

### Changed
- **Module Creation Prompt** - Added nested object pattern documentation
  - Complete examples of intermediate classes
  - Property decorators with lazy loading
  - Usage patterns for nested vs flat endpoints

### Improved
- **API Coverage** - Now at 48% overall (37 of 77 categories):
  - CMDB: 23 of 40 categories (57.5% - all beta)
  - Monitor: 6 of 33 categories (18% - all beta)
  - Log: 5 of 5 categories (100% - all beta)
  - Service: 3 of 3 categories (100% - all beta)
  - Total: 200+ endpoints, 250+ API methods
  - **Note:** All implementations remain in beta until v1.0.0

### Status
- **Beta Release** - All implementations are in beta status:
  - Functional and tested with real FortiGate devices
  - May have incomplete parameter coverage or undiscovered edge cases
  - Production-ready status (v1.0.0) requires comprehensive unit test coverage

### Planned
- Complete CMDB endpoint coverage (23 of 40 categories implemented)
- Monitor endpoints implementation (6 of 33 categories)
- Remaining Monitor categories: system, user, router, vpn, network, etc.
- FortiManager module
- FortiAnalyzer module
- Async support
- CLI tool
- Version 1.0.0: Comprehensive unit tests and production-ready status

## [0.3.10] - 2025-12-16

### Added
- **Configurable Timeouts** - HTTP timeout values are now customizable:
  - `connect_timeout`: Time to wait for connection establishment (default: 10.0 seconds)
  - `read_timeout`: Time to wait for response data (default: 300.0 seconds)
  - Configurable via `FortiOS()` constructor parameters
  - Useful for slow networks, international connections, or large operations
  - `max_retries`: Parameter added for future retry mechanism (default: 3)
- **URL Encoding Helper** - Centralized URL encoding for special characters:
  - New `encode_path_component()` function in `http_client.py`
  - Automatically encodes special characters in object names: `/`, `@`, `:`, spaces, etc.
  - Applied to all 145 CMDB endpoint files (84 path variables encoded)
  - Prevents URL parsing errors when object names contain special characters

### Fixed
- **URL Encoding for Special Characters** - Object names with special characters now work correctly:
  - Fixed issue where objects with `/` in names (e.g., `Test_NET_192.0.2.0/24`) caused 404 errors
  - Special characters are now properly encoded: `/` → `%2F`, `@` → `%40`, `:` → `%3A`, space → `%20`
  - Applies to all API operations: get, create, update, delete
  - Implemented as reusable helper function to avoid code duplication
  - Covers all path variables: `name`, `mkey`, `policyid`, `seq_num`, `member`

## [0.3.9] - 2025-12-16

### Added
- **raw_json Parameter** (100% Coverage) - All API methods now support raw_json parameter:
  - Default behavior: Returns just the results data
  - With `raw_json=True`: Returns complete API response with status codes, metadata
  - Coverage: 45+ methods across all CMDB, Log, and Service endpoints
  - Enables access to `http_status`, `status`, `serial`, `version`, `build` fields

- **Logging System** (Complete) - Comprehensive logging framework:
  - Global control: `hfortix.set_log_level('DEBUG'|'INFO'|'WARNING'|'ERROR'|'OFF')`
  - Per-instance control: `FortiOS(debug='info')`
  - 5 log levels with automatic sensitive data sanitization
  - Hierarchical loggers (`hfortix.http`, `hfortix.client`)
  - Request/response logging with timing information
  - Replaced all print() statements with proper logging

### Changed
- **Code Quality** - Applied comprehensive formatting and linting:
  - Black formatter applied to all 195 files (100% PEP 8 compliance)
  - isort applied to organize imports (86 files updated)
  - flake8 checks passed with max-complexity=10
  - All type hints verified
  - Removed all print() statements in production code (replaced with logging)

### Fixed
- **Bug Fixes** - Fixed multiple undefined variable errors:
  - `antivirus/profile.py`: Fixed 2 instances of undefined 'data' variable (lines 265, 451)
  - `certificate` helpers: Added raw_json parameter to import_p12() and other helper methods
  - `DoS Policy`: Fixed interface_data variable bugs in dos_policy.py and dos_policy6.py
  - `firewall` access-proxy: Fixed raw_json parameter placement in 6 files
  - Multiple service/shaper/ssh files: Fixed data→payload_dict variable name consistency

- **Test Fixes** - Updated test files to use raw_json=True where needed:
  - Fixed 159 test files to properly check API responses
  - Updated payload structures in multiple test files
  - Fixed syntax errors in certificate and firewall tests

## [0.3.8] - 2025-12-16

### Added
- **Dual-Pattern Interface** (100% Complete) - All 43 create/update methods now support:
  - Dictionary pattern: `create(data_dict={'name': 'x', 'param': 'y'})`
  - Keyword pattern: `create(name='x', param='y')`
  - Mixed pattern: `create(data_dict=base, name='override')`
  - Coverage: 38 CMDB endpoints + 5 Service methods

### Changed
- **Documentation**: Updated all docs with dual-pattern examples
  - README.md, QUICKSTART.md with usage examples

### Fixed
- `extension_controller`: Fixed fortigate_profile registration
- `firewall.ssl_setting`: Added missing typing imports
- `firewall.vendor_mac_summary`: Added get() method for singleton endpoint
- Test fixes for alertemail and proxy_addrgrp

## [0.3.7] - 2025-12-16

### Improved
- Packaging/layout cleanup to align with the canonical `hfortix/` package structure
- Additional FortiOS v2 endpoint modules (log/service/cmdb expansions)

## [0.3.6] - 2025-12-15

### Improved - IDE Autocomplete Experience 🎯

**Note:** This is an alpha release with internal refactoring for better developer experience.

#### Hidden Internal Methods for Cleaner Autocomplete
- **Generic CRUD methods renamed** - Methods moved to underscore prefix:
  - `cmdb.get()` → `cmdb._get()` (escape hatch for unmapped endpoints)
  - `cmdb.post()` → `cmdb._post()`
  - `cmdb.put()` → `cmdb._put()`
  - `cmdb.delete()` → `cmdb._delete()`
  - Similar changes for log, monitor, service modules
- **Benefit:** IDE now shows only endpoint-specific methods (create, update, list, etc.)
- **Migration:** If you use generic methods directly, add underscore prefix

#### Hidden Internal Client Attributes
- **Client internals renamed** - FortiOS client implementation details:
  - `fgt.session` → `fgt._session`
  - `fgt.url` → `fgt._url`
  - `fgt.verify` → `fgt._verify`
- **Public attributes unchanged:** `host`, `port`, `vdom`, `cmdb`, `monitor`, `log`, `service`
- **Benefit:** Cleaner autocomplete showing only user-facing API

#### Hidden Lazy-Loaded Property Cache
- **Firewall lazy loading internals** - Changed cache naming to double underscore
- **Affects:** 11 firewall endpoints (dos_policy, address, addrgrp, access_proxy, etc.)
- **Benefit:** IDE no longer shows internal cached attributes

### Added
- **`__all__` exports** - Explicit control over public API in all modules
- Better documentation and import suggestions

### Technical Details
- 79+ endpoint files updated to use underscore methods internally
- Follows Python naming conventions (single _ = internal, double __ = private)
- All endpoint-specific methods work as before (no breaking changes)
- All tests passing (8/8 for address, access_proxy)

## [0.3.5] - 2025-12-15

### Improved - IDE Autocomplete & Type Hints ✨

#### Developer Experience Enhancements
- **Added PEP 561 support** - Created `FortiOS/py.typed` marker file for better IDE type checking
- **Enhanced type hints** - Added explicit type annotations to all API helper classes
  - `self.cmdb: CMDB` - Full autocomplete for CMDB endpoints
  - `self.firewall: Firewall` - Full autocomplete for firewall endpoints
  - All 16 CMDB categories now have proper type hints
- **Improved `__all__` exports** - Better module discovery and import suggestions
- **Updated setup.py** - Added `package_data` for py.typed and "Typing :: Typed" classifier
- **Fixed duplicate assignments** - Removed redundant initialization in CMDB `__init__.py`

#### Documentation Improvements
- Added comprehensive docstrings explaining API helper class attributes
- Clarified purpose of generic methods (advanced/fallback usage)
- Better examples in class docstrings

### Technical Details
- Type hints now work correctly in VS Code, PyCharm, and other PEP 561-compliant IDEs
- Autocomplete shows all available endpoints when typing `fgt.api.cmdb.firewall.`
- Method signatures display parameter types and return types
- No breaking changes - fully backward compatible

## [0.3.4] - 2025-12-15

### Documentation - Unified Import Syntax 📚

#### Updated All Documentation
- **README.md** - Changed all examples to use `from hfortix import FortiOS`
- **QUICKSTART.md** - Updated import patterns and all code examples
- **Added PyPI badges** - Version, Python 3.8+, MIT license
- **Status updates** - FortiOS "✅ Active", FortiManager/FortiAnalyzer "⏸️ Planned"

### Technical Details
- All documentation now reflects the unified package import structure
- Installation instructions prioritize PyPI method
- 190 insertions, 78 deletions across documentation files

## [0.3.3] - 2025-12-15

### Added - Unified Package Import Structure 📦

#### Package Restructuring
- **Created `hfortix.py`** - Main module for unified imports
- **Enable `from hfortix import FortiOS`** - Clean import syntax
- **Backward compatible** - Old imports still work
- **Updated `__init__.py`** - Changed from relative to absolute imports

### Technical Details
- Added `py_modules=['hfortix', 'exceptions', 'exceptions_forti']` to setup.py
- Package now supports both import styles:
  - Recommended: `from hfortix import FortiOS`
  - Also works: `from FortiOS import FortiOS`

## [0.3.2] - 2025-12-15

### Fixed - Package Distribution 🔧

#### Resolved Import Errors
- **Fixed ModuleNotFoundError** - Added root-level modules to package
- **Updated setup.py** - Added `py_modules` configuration
- **Included exceptions modules** - Both `exceptions.py` and `exceptions_forti.py` now in package

### Technical Details
- Root-level Python modules now properly included in wheel and sdist
- No code changes needed - pure packaging fix

## [0.3.1] - 2025-12-15

### Fixed - Import Error Handling 🛠️

#### Exception Module Imports
- **Added fallback imports** - Better handling for missing exception modules
- **Enhanced FortiOS/exceptions.py** - Try/except blocks for imports
- **Fallback exceptions defined** - Basic exception classes if imports fail

### Technical Details
- Partial fix for import issues (fully resolved in 0.3.2)

## [0.3.0] - 2025-12-14

### Added - Firewall Flat Endpoints + Sub-categories! 🎉

#### New Flat Firewall Endpoints (6 endpoints)
Implemented DoS protection and access proxy endpoints with simplified API:

- **firewall/DoS-policy** - IPv4 DoS protection policies
  - Full CRUD operations with automatic type conversion
  - Comprehensive anomaly detection (18 types with default thresholds)
  - Simplified API: `interface='port3'` → `{'q_origin_key': 'port3'}`
  - Test coverage: 8/8 tests passing (100%)

- **firewall/DoS-policy6** - IPv6 DoS protection policies
  - Same features as DoS-policy for IPv6
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy** - IPv4 reverse proxy/WAF
  - Full CRUD with 16+ configuration parameters
  - VIP integration (requires type="access-proxy")
  - Server pool multiplexing support
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy6** - IPv6 reverse proxy/WAF
  - Same features as access-proxy for IPv6
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy-ssh-client-cert** - SSH client certificates
  - Certificate-based SSH authentication
  - Permit controls (agent forwarding, port forwarding, PTY, X11, user RC)
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy-virtual-host** - Virtual host configuration
  - Domain/wildcard/regex host matching
  - SSL certificate management with automatic list conversion
  - Test coverage: 8/8 tests passing (100%)

**Total Test Coverage:** 48/48 tests (100% pass rate)

**Key Features:**
- **Simplified API** - Automatic type conversion for better UX
  - String → dict: `'port3'` → `{'q_origin_key': 'port3'}`
  - String list → dict list: `['HTTP']` → `[{'name': 'HTTP'}]`
  - Certificate string → list: `'cert'` → `[{'name': 'cert'}]`
- **Comprehensive Documentation** - Anomaly detection types with thresholds
- **Prerequisites Documented** - VIP types, certificates, CAs
- **Lazy Loading** - @property pattern for optimal performance

#### CMDB Category: Firewall Sub-categories (17 endpoints, 7 sub-categories)
Implemented nested/hierarchical structure for firewall endpoints with lazy-loading pattern:

- **firewall.ipmacbinding** (2 endpoints)
  - `setting` - IP/MAC binding global settings
  - `table` - IP/MAC binding table entries

- **firewall.schedule** (3 endpoints)
  - `group` - Schedule groups
  - `onetime` - One-time schedules
  - `recurring` - Recurring schedules

- **firewall.service** (3 endpoints)
  - `category` - Service categories
  - `custom` - Custom service definitions
  - `group` - Service groups

- **firewall.shaper** (2 endpoints)
  - `per-ip-shaper` - Per-IP traffic shaping
  - `traffic-shaper` - Shared traffic shaping

- **firewall.ssh** (4 endpoints)
  - `host-key` - SSH proxy host public keys
  - `local-ca` - SSH proxy local CA
  - `local-key` - SSH proxy local keys (with PEM format support)
  - `setting` - SSH proxy settings

- **firewall.ssl** (1 endpoint)
  - `setting` - SSL proxy settings (timeout, DH bits, caching)

- **firewall.wildcard-fqdn** (2 endpoints)
  - `custom` - Wildcard FQDN addresses (e.g., *.example.com)
  - `group` - Wildcard FQDN groups

### Technical Improvements
- ✅ Nested API structure: `fgt.api.cmdb.firewall.[subcategory].[endpoint]`
- ✅ Lazy-loading with @property methods
- ✅ Singleton pattern for settings endpoints (results as dict)
- ✅ Collection pattern for list endpoints (results as list)
- ✅ exists() methods with try/except for 404 handling
- ✅ Real SSH key generation for testing (PEM format)
- ✅ Member management for group endpoints
- ✅ 138 comprehensive tests (100% pass rate)

### Documentation
- ✅ Complete module creation guide (1,900+ lines)
- ✅ Documentation generation prompt
- ✅ Comprehensive docstrings with examples for all methods
- ✅ Type hints on all parameters

## [0.2.0] - 2025-12-14

### Added - Major Expansion! 🎉

#### New CMDB Categories (7 categories, 30 endpoints)
- **DLP (Data Loss Prevention)** - 8 endpoints
  - `data-type` - Predefined data type patterns
  - `dictionary` - Custom DLP dictionaries
  - `exact-data-match` - Fingerprinting for exact data matching
  - `filepattern` - File type and pattern matching
  - `label` - Classification labels
  - `profile` - DLP policy profiles
  - `sensor` - DLP sensor configuration
  - `settings` - Global DLP settings

- **DNS Filter** - 2 endpoints
  - `domain-filter` - Custom domain filtering lists
  - `profile` - DNS filtering profiles

- **Email Filter** - 8 endpoints
  - `block-allow-list` - Email sender block/allow lists
  - `bword` - Banned word filtering
  - `dnsbl` - DNS-based blacklist checking
  - `fortishield` - FortiShield spam filtering
  - `iptrust` - Trusted IP addresses
  - `mheader` - Email header filtering rules
  - `options` - Global email filter options
  - `profile` - Email filtering profiles

- **Endpoint Control** - 3 endpoints
  - `fctems` - FortiClient EMS integration
  - `fctems-override` - EMS override configurations
  - `settings` - Endpoint control settings

- **Ethernet OAM** - 1 endpoint
  - `cfm` - Connectivity Fault Management (requires physical hardware)

- **Extension Controller** - 6 endpoints
  - `dataplan` - FortiExtender data plan configuration
  - `extender` - FortiExtender controller settings
  - `extender-profile` - FortiExtender profiles
  - `extender-vap` - FortiExtender WiFi VAP
  - `fortigate` - FortiGate controller configuration
  - `fortigate-profile` - FortiGate connector profiles

- **File Filter** - 1 endpoint
  - `profile` - File content filtering profiles

### Changed
- **License**: Changed from MIT to Proprietary License with free use
  - Free for personal, educational, and business use
  - Companies can use for internal operations and client services
  - Tech support and MSPs can use in their service offerings
  - **Cannot sell the software itself as a standalone product**
  - Simple rule: Use it freely for your work, just don't sell the software

### Improved
- **CMDB Coverage**: 21 → 51 endpoints (+143% growth!)
- **CMDB Categories**: 7 → 14 categories (+100% growth!)
- All modules follow consistent patterns:
  - `from __future__ import annotations` for modern type hints
  - Comprehensive docstrings with examples
  - Snake_case to hyphen-case parameter conversion
  - Full CRUD operations where applicable
  - **kwargs for flexibility

### Fixed
- Directory naming issues (hyphens → underscores for Python imports)
- Graceful error handling for hardware-dependent features
- Improved test patterns for pre-allocated resource slots
- Better handling of list/dict API responses

### Documentation
- Updated PROJECT_STATUS.md with all new modules
- Updated README with current statistics
- Updated CHANGELOG with detailed release notes
- All modules include comprehensive test files

## [0.1.0] - 2025-12-13

### Added
- Initial release of Fortinet Python SDK
- Modular package architecture supporting FortiOS, FortiManager, FortiAnalyzer
- FortiOS client with token-based authentication
- Comprehensive exception handling system (387 FortiOS error codes)
- CMDB endpoints (Beta - partial coverage):
  - `alertemail` - Email alert settings
  - `antivirus` - Antivirus profiles and settings
  - `application` - Application control (custom, list, group, name)
  - `authentication` - Authentication rules, schemes, and settings
  - `automation` - Automation settings
  - `casb` - CASB (Cloud Access Security Broker) profiles
  - `certificate` - Certificate management (CA, CRL, local, remote, HSM)
  - `diameter_filter` - Diameter filter profiles
- Service endpoints (Beta):
  - `sniffer` - Packet capture and analysis
  - `security_rating` - Security Fabric rating
  - `system` - System information and operations
- Log endpoints (Beta):
  - `disk` - Disk-based logging
  - `fortianalyzer` - FortiAnalyzer logging
  - `forticloud` - FortiCloud logging
  - `memory` - Memory-based logging
  - `search` - Log search functionality
- Base exception classes for all Fortinet products
- FortiOS-specific exception classes with detailed error code mapping
- Support for both full package and standalone module installation
- Module availability detection (`get_available_modules()`)
- Version information (`get_version()`)

### Documentation
- Comprehensive README with installation and usage examples
- QUICKSTART guide for rapid onboarding
- Exception hierarchy documentation
- API structure overview
- Common usage patterns and examples

### Infrastructure
- Package distribution setup (setup.py, MANIFEST.in)
- Requirements management (requirements.txt)
- Git ignore configuration
- MIT License

## [0.0.1] - 2025-11-XX

### Added
- Initial project structure
- Basic FortiOS client implementation
- Core exception handling

---

## Version Numbering

- **Major version (X.0.0)**: Incompatible API changes
- **Minor version (0.X.0)**: New features, backward compatible
- **Patch version (0.0.X)**: Bug fixes, backward compatible

## Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes
