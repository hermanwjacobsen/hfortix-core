# Generator Workflow - Quick Reference

**Successfully tested with:** `cmdb.firewall.policy`, `cmdb.firewall.service/custom` (January 3, 2026)

---

## ⚠️ Generator Scope

**✅ Supported Categories:**
- **CMDB** - Configuration endpoints (full CRUD, schemas available)
- **Monitor** - Monitoring endpoints (GET/POST, limited schemas)
- **Service** - Service endpoints (if schemas available)

**❌ NOT Supported:**
- **Log** - Uses composition pattern, manually implemented in `api/v2/log/`
  - Log endpoints share types across storage backends (disk/memory/fortianalyzer/forticloud)
  - No schemas available
  - Future: Create separate log-specific generator

---

## 🎯 Quick Start

### Generate a Single Endpoint

```bash
cd /app/dev/classes/fortinet/.dev/generator
python generate_firewall_policy.py
```

**What it generates:**
1. **Endpoint class**: `packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/policy.py`
2. **Validator helpers**: `packages/fortios/hfortix_fortios/api/v2/cmdb/firewall/_helpers/policy.py`

**What it creates automatically:**
- All CRUD methods (get, post, put, delete, exists)
- Complete type hints (Union[dict, Coroutine] for sync/async)
- Field validation with enum constraints
- Required fields detection
- Default value handling

---

## 📁 Directory Structure

```
.dev/generator/
├── generate_firewall_policy.py      # Single endpoint generator script
├── schema_parser.py                 # Schema parsing logic
├── generators/
│   ├── endpoint_generator.py        # Generates endpoint classes
│   └── validator_generator.py       # Generates _helpers validators
└── templates/
    ├── endpoint_class.py.j2         # Template for API endpoint (180 lines)
    └── validator.py.j2              # Template for validators (245 lines)

.dev/
├── schema_firewall_policy.json      # Downloaded FortiOS schema
└── schema_firewall_address.json     # Another schema example

packages/fortios/hfortix_fortios/api/v2/
├── cmdb/
│   ├── __init__.py                  # CMDB class with .firewall
│   └── firewall/
│       ├── __init__.py              # Firewall class with .policy
│       ├── policy.py                # Generated endpoint (59KB)
│       └── _helpers/
│           └── policy.py            # Generated validators (67KB)
├── log/
│   └── __init__.py                  # Log stub class
├── monitor/
│   └── __init__.py                  # Monitor stub class
└── service/
    └── __init__.py                  # Service stub class
```

---

## 🔧 Template Configuration

### Jinja2 Environment Settings

```python
env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,      # Remove newline after block tags
    lstrip_blocks=True,    # Remove whitespace before block tags
)
```

**Critical:** Do NOT use `{%-` or `-%}` whitespace control in templates. The environment settings handle all whitespace.

### Custom Filters

```python
def kebab_to_snake(value: str) -> str:
    """Convert kebab-case to snake_case (handles both - and /)."""
    return value.replace("-", "_").replace("/", "_")

env.filters["kebab_to_snake"] = kebab_to_snake
```

---

## ✅ Validated Patterns

### 1. Type Narrowing for Union Types

**Problem:** Pylance can't narrow `Union[dict, Coroutine]` with `hasattr()`

**Solution:** Use `isinstance()`
```python
# ❌ Wrong - doesn't narrow type
if hasattr(response, "get"):
    return response.get("status") == "success"

# ✅ Correct - narrows type properly
if isinstance(response, dict):
    return response.get("status") == "success"
```

### 2. HTTP Client Data Parameter

**Critical:** FortiGate API expects `data=` not `json=`

```python
# ❌ Wrong
self._client.post("cmdb", endpoint, json=payload_dict, ...)

# ✅ Correct
self._client.post("cmdb", endpoint, data=payload_dict, ...)
```

### 3. exists() Method Exception Handling

```python
def exists(self, policyid: int, vdom: str | bool | None = None) -> bool:
    """Check if resource exists."""
    try:
        response = self.get(policyid=policyid, vdom=vdom, raw_json=True)
        
        if isinstance(response, dict):
            return response.get("status") == "success"
        else:
            async def _check() -> bool:
                r = await response
                return r.get("status") == "success"
            return _check()
    except Exception:
        # Resource not found or other error - return False
        return False
```

### 4. List Field Format

FortiGate requires list fields as list of dicts with "name" key:

```python
# ✅ Correct
srcintf=[{"name": "port3"}, {"name": "port4"}]
dstaddr=[{"name": "all"}]
service=[{"name": "HTTP"}, {"name": "HTTPS"}]

# ❌ Wrong
srcintf=["port3", "port4"]
```

---

## 🧪 Testing Strategy

### Test Organization

Mirror API structure in test directory:

```
.tests/pytests/api/
└── cmdb/
    └── firewall/
        ├── __init__.py
        ├── test_policy.py              # API integration tests (7 tests)
        └── test_policy_validators.py   # Validator unit tests (31 tests)
```

### Test File Pattern

**API Integration Tests:**
- Test live FortiGate API calls
- Validate CRUD operations
- Use numeric prefixes for ordering (test_1_, test_2_)
- Implement autouse fixture for cleanup

**Validator Unit Tests:**
- Test validation functions
- Validate enum constraints
- Check required fields
- Test edge cases

### Running Tests

```bash
# All tests for one endpoint
pytest .tests/pytests/api/cmdb/firewall/ -v

# Just API tests
pytest .tests/pytests/api/cmdb/firewall/test_policy.py -v

# Just validator tests
pytest .tests/pytests/api/cmdb/firewall/test_policy_validators.py -v
```

---

## � Edge Cases & Special Handling

### Endpoints with Dots in Names

**Example:** `firewall.ssh/setting`, `firewall.ssl/setting`

**API Path:** `/cmdb/firewall.ssh/setting` (dot separates subcategory)

**Old Implementation Pattern:**

1. **File Structure**:
   ```
   firewall/
   ├── ssh_setting.py          # File uses underscores, FLAT structure
   ├── ssh_host_key.py
   ├── ssl_setting.py
   └── __init__.py
   ```

2. **Class Naming**:
   ```python
   # In ssh_setting.py
   class SshSetting:
       def get(self, ...):
           endpoint = "/firewall.ssh/setting"  # Dot preserved in API path
   ```

3. **Wrapper Classes for Namespacing**:
   ```python
   # In firewall/__init__.py
   class Ssh:
       """Wrapper for firewall.ssh.* endpoints."""
       def __init__(self, client):
           self.setting = SshSetting(client)
           self.host_key = SshHostKey(client)
           self.local_ca = SshLocalCa(client)
           self.local_key = SshLocalKey(client)
   
   class Ssl:
       """Wrapper for firewall.ssl.* endpoints."""
       def __init__(self, client):
           self.setting = SslSetting(client)
           self.server = SslServer(client)
   
   class Firewall:
       def __init__(self, client):
           # ... other endpoints
           self.ssh = Ssh(client)
           self.ssl = Ssl(client)
   ```

4. **Usage**:
   ```python
   # Clean dot notation access (mirrors API structure)
   fgt.api.cmdb.firewall.ssh.setting.get()  # → /cmdb/firewall.ssh/setting
   fgt.api.cmdb.firewall.ssl.setting.get()  # → /cmdb/firewall.ssl/setting
   ```

**Generator Strategy:**
- Detect dots in endpoint path: `firewall.ssh/setting`
- Split on dot: `["firewall", "ssh/setting"]`
- Create wrapper class: `Ssh` (from second part before `/` - for future __init__.py)
- **File name: `ssh_setting.py`** (replace dot and slash with underscore, KEEP FLAT)
- **Path: `firewall/ssh_setting.py`** (NO subdirectories for dot-separated names)
- Class name: `SshSetting` (PascalCase of `ssh_setting`)
- Preserve dot in endpoint string: `"/firewall.ssh/setting"`

**Critical:** Do NOT create subdirectories for dot-separated names. The old implementation kept all files flat in the parent directory (e.g., `firewall/`), using wrapper classes in `__init__.py` for the dot-notation access pattern.

---

## �📊 Known Issues & Solutions

### Issue 1: Whitespace Control

**Problem:** Using `{%-` and `-%}` in templates strips necessary newlines → 236+ syntax errors

**Solution:** Configure environment with `trim_blocks=True, lstrip_blocks=True` and use plain `{%` tags

### Issue 2: Type Narrowing

**Problem:** `hasattr()` doesn't narrow Union types for Pylance

**Solution:** Use `isinstance(response, dict)` for proper type guards

### Issue 3: GET Response Format

**Problem:** GET returns list directly, not dict with "results" key

**Solution:**
```python
# ✅ Correct - GET returns list
all_policies = fgt.api.cmdb.firewall.policy.get(vdom="test")
for policy in all_policies:
    print(policy["policyid"])

# ❌ Wrong
results = response.get("results")  # KeyError!
```

### Issue 4: Required Fields vs Schema

**Problem:** FortiOS schema marks many optional fields as "required"

**Solution:** Generated validators include REQUIRED_FIELDS list based on actual API testing, not just schema

---

## 🚀 Next Steps Checklist

### Before Generating Next Endpoint

- [x] Template syntax validated (no whitespace control markers)
- [x] Type narrowing patterns verified
- [x] HTTP client parameters correct (data not json)
- [x] exists() exception handling implemented
- [x] Test structure established
- [x] Cleanup mechanism working

### To Generate New Endpoint (e.g., firewall.address)

1. **Get Schema**
   ```bash
   # Download schema for firewall.address
   # (or use existing schema_firewall_address.json)
   ```

2. **Copy Generator Script**
   ```bash
   cp generate_firewall_policy.py generate_firewall_address.py
   # Update endpoint path to firewall/address
   ```

3. **Run Generator**
   ```bash
   python generate_firewall_address.py
   ```

4. **Create Tests**
   ```bash
   # Create test file
   .tests/pytests/api/cmdb/firewall/test_address.py
   .tests/pytests/api/cmdb/firewall/test_address_validators.py
   ```

5. **Run Tests**
   ```bash
   pytest .tests/pytests/api/cmdb/firewall/test_address*.py -v
   ```

---

## 📝 Template Reference

### endpoint_class.py.j2 Key Sections

1. **Imports & Type Hints**
   ```python
   from typing import TYPE_CHECKING, Any, Union
   if TYPE_CHECKING:
       from collections.abc import Coroutine
   ```

2. **GET Method**
   - Builds endpoint path with/without ID
   - Uses `params=` for query parameters
   - Returns Union[dict, Coroutine]

3. **POST/PUT Methods**
   - Builds payload_dict from kwargs
   - Uses `data=` parameter (not json)
   - Converts Python param names to FortiGate kebab-case

4. **DELETE Method**
   - Requires ID parameter
   - Validates ID presence

5. **exists() Helper**
   - Wraps get() in try/except
   - Returns bool (or Coroutine[bool])
   - Returns False on any exception

### validator.py.j2 Key Sections

1. **Constants**
   - REQUIRED_FIELDS (list)
   - FIELDS_WITH_DEFAULTS (dict)
   - VALID_BODY_* (enum lists)
   - VALID_QUERY_* (enum lists)

2. **Validation Functions**
   - validate_{endpoint}_get()
   - validate_{endpoint}_post()
   - validate_{endpoint}_put()
   - validate_required_fields()

3. **Return Format**
   - All return `tuple[bool, str | None]`
   - `(True, None)` = valid
   - `(False, "error")` = invalid

---

## 💡 Lessons Learned

### Template Design
1. Keep templates clean - let environment handle whitespace
2. Use custom filters for common transformations
3. Generate complete files - don't rely on manual edits
4. Include comprehensive docstrings in templates

### Type Safety
1. Union types need isinstance() checks
2. Async methods complicate type hints
3. Always include TYPE_CHECKING guards
4. Use proper return type annotations

### FortiGate API Quirks
1. GET returns list directly (not wrapped)
2. List fields need [{"name": "value"}] format
3. Enums are case-sensitive
4. Many "required" fields actually have defaults
5. Extra fields are silently ignored

### Testing
1. Mirror API structure in test directories
2. Separate integration tests from unit tests
3. Use numeric prefixes for test ordering
4. Implement cleanup fixtures
5. Test both sync and async patterns (future)

---

## 📈 Current Status

### Completed ✅
- **Generator**: Templates working, 0 errors
- **Endpoint**: cmdb.firewall.policy fully functional (59KB, 188 fields)
- **Validators**: Complete validation suite (67KB, 7 required, 141 defaults)
- **Tests**: 38/38 passing (7 API + 31 validators)
- **Cleanup**: Automatic policy deletion working
- **Documentation**: This guide + test summaries

### Ready for Production ✅
- Template syntax validated
- Type safety verified
- HTTP client integration working
- Test patterns established
- Organization structure defined

### Next Endpoint Candidates
1. `cmdb.firewall.address` - Similar to policy, good second test
2. `cmdb.system.interface` - Core system config
3. `cmdb.router.static` - Routing configuration
4. `cmdb.user.local` - User management

---

## 🔗 Related Documentation

- **Template Design**: `.dev/generator/templates/` (actual templates)
- **Generator Code**: `.dev/generator/generators/` (Python generators)
- **Schema Examples**: `.dev/schema_*.json` (FortiOS schemas)
- **Test Examples**: `.tests/pytests/api/cmdb/firewall/` (working tests)
- **Design Docs**: `.dev/generator/docs/` (architectural documentation)

---

**Last Updated:** January 3, 2026  
**Tested With:** FortiGate v7.6.1 (192.168.1.99)  
**Generator Version:** 0.5.0 (in development)
