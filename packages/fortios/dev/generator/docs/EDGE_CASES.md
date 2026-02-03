# Generator Edge Cases & Capabilities

**Last Updated:** January 3, 2026  
**Status:** ✅ All edge cases handled

---

## Supported Path Patterns

### 1. Normal Paths ✅

**Example:** `firewall/policy`

```python
# Input
endpoint_path = "firewall/policy"

# Output
name     = "policy"
path     = "firewall/policy"
api_path = "firewall/policy"

# File Structure
cmdb/firewall/policy.py

# Usage
fgt.api.cmdb.firewall.policy.get()
```

### 2. Dots in Paths ✅

**Example:** `firewall.ssh/setting`

FortiOS uses dots to denote sub-categories. These must be converted to underscores for Python.

```python
# Input
endpoint_path = "firewall.ssh/setting"

# Output
name     = "ssh_setting"
path     = "firewall/ssh_setting"     # Flat structure
api_path = "firewall.ssh/setting"     # Preserve dot for API

# File Structure
cmdb/firewall/ssh_setting.py          # NOT firewall/ssh/setting.py

# Usage
fgt.api.cmdb.firewall.ssh_setting.get()

# API Call
client.get("cmdb", "firewall.ssh/setting")  # Dot preserved
```

**Other Examples:**
- `firewall.service/custom` → `firewall/service_custom.py`
- `firewall.schedule/recurring` → `firewall/schedule_recurring.py`
- `firewall.ssl/setting` → `firewall/ssl_setting.py`

### 3. Dashes in Paths ✅

**Example:** `casb/saas-application`

Dashes are invalid in Python identifiers. Convert to underscores.

```python
# Input
endpoint_path = "casb/saas-application"

# Output
name     = "saas_application"
path     = "casb/saas_application"
api_path = "casb/saas-application"    # Preserve dash for API

# File Structure
monitor/casb/saas_application.py

# Usage
fgt.api.monitor.casb.saas_application.get()

# API Call
client.get("monitor", "casb/saas-application")  # Dash preserved
```

### 4. Combined: Dots + Dashes ✅

**Example (hypothetical):** `firewall.service/custom-policy`

```python
# Input
endpoint_path = "firewall.service/custom-policy"

# Output
name     = "custom_policy"
path     = "firewall/custom_policy"
api_path = "firewall.service/custom-policy"

# File Structure
cmdb/firewall/custom_policy.py

# Usage
fgt.api.cmdb.firewall.custom_policy.get()
```

### X5. Endpoints with Both GET and Actions ✅

**Example:** `monitor/firewall/policy` (GET endpoint with POST actions)

Some monitor endpoints have BOTH a GET method (for data retrieval) AND POST action methods (like clear-counters, reset, etc.).

```python
# Input
# Base endpoint:  monitor/firewall/policy.json              (http_method: GET)
# Action endpoints: monitor/firewall/policy/clear-counters.json (http_method: POST)
#                  monitor/firewall/policy/reset.json          (http_method: POST)
#                  monitor/firewall/policy/update-global-label.json (http_method: POST)

# Output Structure
monitor/
  firewall/
    policy_base.py          # Base class with GET method
    policy/                 # Subdirectory for actions
      __init__.py           # Wrapper class (inherits from base + adds actions)
      clear_counters.py     # Action endpoint with POST method
      reset.py              # Action endpoint with POST method
      update_global_label.py # Action endpoint with POST method

# Wrapper __init__.py content:
from ..policy_base import Policy as PolicyBase
from .clear_counters import ClearCounters
from .reset import Reset
from .update_global_label import UpdateGlobalLabel

class Policy(PolicyBase):
    """Policy endpoints wrapper - combines GET with actions."""
    
    def __init__(self, client):
        super().__init__(client)  # Initialize base class with get() method
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)
        self.update_global_label = UpdateGlobalLabel(client)

# Usage
fgt.api.monitor.firewall.policy.get()                  # From base class
fgt.api.monitor.firewall.policy.clear_counters.post()  # From action subdir
fgt.api.monitor.firewall.policy.reset.post()           # From action subdir
```

**How Generator Handles This:**

1. **Detects Pattern:** When both `policy_base.py` AND `policy/` directory exist
2. **Base File:** `policy_base.py` has the GET endpoint methods
3. **Action Directory:** `policy/` contains POST action endpoints
4. **Wrapper Generation:** `regenerate_init_files.py` creates `policy/__init__.py` that:
   - Inherits from `PolicyBase` (gets `.get()` method)
   - Adds action attributes (`.clear_counters`, `.reset`, etc.)
5. **Parent Import:** Parent `firewall/__init__.py` imports from `policy` package (not `policy_base`)

**Other Examples:**
- `monitor/azure/application-list` → `.get()` + `.refresh.post()`
- `monitor/casb/saas-application` → `.get()` + `.refresh.post()`
- `service/ldap` → `.get()` + `.test.post()`
- `monitor/switch-controller/managed-switch` → `.get()` + 17 action methods

**Important:** The `_base` suffix is ONLY for the filename. The class name is still `Policy`, not `PolicyBase`.

---

## Method Generation

### CMDB Endpoints

**Full CRUD + Helpers:**

```python
class Policy:
    def get(self, ...):       # Retrieve items
    def post(self, ...):      # Create item
    def put(self, ...):       # Update item
    def delete(self, ...):    # Delete item
    def exists(self, ...):    # Check existence
    def set(self, ...):       # Smart create/update (auto-detects)
```

### Monitor Endpoints

**Typically GET, some POST:**

```python
class SaasApplication:
    def get(self, ...):       # Retrieve data (read-only)
    # No POST/PUT/DELETE (monitoring, not configuration)
```

Some monitor endpoints have POST for actions:

```python
class VpnCertificate:
    def post(self, ...):      # Import certificate, generate CSR, etc.
```

---

## NOT Supported by Generator

### Log Endpoints ❌

**Why:** Uses composition pattern, not hierarchical structure.

```python
# Log structure (MANUAL implementation)
fgt.api.log.disk.virus.get()         # Disk storage
fgt.api.log.memory.virus.get()       # Memory storage
fgt.api.log.fortianalyzer.virus.get()  # FortiAnalyzer

# Virus class is SHARED across all storage backends
# This is composition, not generation
```

**See:** `docs/LOG_CATEGORY_NOTES.md` for details.

### Nested Sub-Resources ⚠️

**Status:** Planned, not yet implemented.

**Example:** `monitor/casb/saas-application/details`

```python
# Desired structure (NOT YET SUPPORTED)
class Details:
    def get(self, ...):
        return client.get("monitor", "/casb/saas-application/details")

class SaasApplication:
    def __init__(self, client):
        self.details = Details(client)  # Nested resource

# Usage
fgt.api.monitor.casb.saas_application.details.get()
```

**Workaround:** Currently generates flat structure. Need to add nested class template.

---

## Validation

### Generated Tests

```python
def test_policy_get():
    """Test GET operation"""
    result = fgt.api.cmdb.firewall.policy.get()
    assert result["status"] == "success"

def test_policy_create():
    """Test POST operation"""
    payload = {"name": "test", "srcintf": ["port1"], ...}
    result = fgt.api.cmdb.firewall.policy.post(payload)
    assert result["status"] == "success"

def test_policy_set():
    """Test smart set() method"""
    payload = {"name": "test", ...}
    result = fgt.api.cmdb.firewall.policy.set(payload)
    # Uses POST if new, PUT if exists
```

### Type Safety

```python
# All methods return Union[dict, Coroutine]
def get(self, ...) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
    """Works with both sync and async clients"""
```

---

## File Organization

### Generated Structure

```
packages/fortios/hfortix_fortios/api/v2/
├── cmdb/
│   ├── __init__.py                    # CMDB class
│   └── firewall/
│       ├── __init__.py                # Firewall class
│       ├── policy.py                  # Generated endpoint
│       ├── ssh_setting.py             # Generated (dots → underscore)
│       ├── service_custom.py          # Generated (dots → underscore)
│       └── _helpers/
│           ├── policy.py              # Generated validator
│           ├── ssh_setting.py
│           └── service_custom.py
└── monitor/
    ├── __init__.py
    └── casb/
        ├── __init__.py
        ├── saas_application.py        # Generated (dash → underscore)
        └── _helpers/
            └── saas_application.py
```

### Flat vs Nested

**Always FLAT** for dotted endpoints:

```
✅ CORRECT:
cmdb/firewall/ssh_setting.py

❌ WRONG:
cmdb/firewall/ssh/setting.py    # Don't create ssh/ subdirectory
```

---

## Testing

### Test Files

```
.tests/pytests/api/cmdb/firewall/
├── test_policy.py           # 7 tests (CRUD operations)
├── test_service_custom.py   # 17 tests (including set() method)
└── test_ssh_setting.py      # Future
```

### Test Results

```bash
# All tests passing ✅
pytest .tests/pytests/api/cmdb/firewall/test_policy.py        # 7/7 PASSED
pytest .tests/pytests/api/cmdb/firewall/test_service_custom.py  # 17/17 PASSED

# Total: 24/24 tests passing
```

---

## References

- **Schema Parser:** `.dev/generator/schema_parser.py`
- **Generator:** `.dev/generator/generate_endpoint.py`
- **Templates:** `.dev/generator/templates/`
- **Tests:** `.tests/pytests/api/cmdb/firewall/`
- **Docs:** `.dev/generator/docs/`

---

## Future Enhancements

1. **Nested Sub-Resources** - Support `/details`, `/import`, etc. as nested classes
2. **Log Generator** - Separate generator for log composition pattern
3. **Monitor Schemas** - Better handling of monitor endpoints without schemas
4. **Batch Generation** - Generate entire categories at once
5. **Schema Caching** - Cache downloaded schemas for offline work
