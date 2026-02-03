# Log Category - Special Implementation Notes

**Status:** Manual implementation (NOT generated)  
**Location:** `api/v2/log/`  
**Date:** January 3, 2026

---

## Why Log Endpoints Are NOT Generated

The `log` category uses a **composition pattern** that is fundamentally different from CMDB/Monitor endpoints:

### 1. Storage-Based Hierarchy

Log endpoints are organized by **storage backend** first:
- `/log/disk/...`
- `/log/memory/...`
- `/log/fortianalyzer/...`
- `/log/forticloud/...`

### 2. Shared Log Types

Each storage backend can access the **same log types**:
```
/log/disk/virus
/log/memory/virus
/log/fortianalyzer/virus
/log/forticloud/virus
```

The `Virus` class is **shared** across all storage backends via composition.

### 3. Implementation Pattern

```python
# File: api/v2/log/disk/disk.py
from api.v2.log.virus import Virus
from api.v2.log.traffic import Traffic

class Disk:
    def __init__(self, client):
        # Instantiate shared log type classes with storage parameter
        self.virus = Virus(client, storage="disk")
        self.traffic = Traffic(client, storage="disk")
        self.ips = IPS(client, storage="disk")
        # ... etc
```

```python
# File: api/v2.log/virus.py
class Virus:
    def __init__(self, client, storage="disk"):
        self._client = client
        self._storage = storage
        self.raw = RawResource(client, "virus", storage)
        self.archive = ArchiveResource(client, "virus", storage)
    
    def get(self, ...):
        # Uses self._storage to build path: /log/{storage}/virus
        return self._client.get("log", f"/{self._storage}/virus", ...)
```

### 4. No Schemas Available

Unlike CMDB endpoints, log endpoints do **not have schemas**:

```bash
# CMDB has schemas ✅
curl 'https://host/api/v2/cmdb/firewall/policy?action=schema'

# Log does NOT ❌
curl 'https://host/api/v2/log/disk/virus?action=schema'
# Returns actual log data, not schema
```

### 5. Complex Sub-Resources

Different log types have different sub-resources:

| Log Type | Sub-Resources |
|----------|---------------|
| `virus` | `archive` (special endpoint) |
| `ips` | `archive`, `archive-download` |
| `app-ctrl` | `archive`, `archive-download` |
| `traffic` | `raw`, subtypes (`forward`, `local`, `multicast`, etc.) |
| `event` | `raw`, subtypes (`vpn`, `user`, `router`, etc.) |
| `webfilter` | `raw` |

---

## Current Implementation

The log category is **manually implemented** in:

```
api/v2/log/
├── __init__.py          # Log class - initializes storage backends
├── base.py              # Shared base classes (RawResource, ArchiveResource, etc.)
├── virus.py             # Virus + VirusArchive classes
├── traffic.py           # Traffic + subtypes (TrafficForward, etc.)
├── event.py             # Event + subtypes (EventVPN, EventUser, etc.)
├── ips.py               # IPS class
├── app_ctrl.py          # AppCtrl class
└── disk/
    ├── __init__.py
    ├── disk.py          # Disk container - composes all log types
    └── _helpers/        # Validation helpers
```

### Usage

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(host="192.168.1.99", token="...")

# Access via storage backend
logs = fgt.api.log.disk.virus.get()
logs = fgt.api.log.memory.traffic.get()
logs = fgt.api.log.disk.ips.archive.get()

# Sub-resources
raw = fgt.api.log.disk.virus.raw.get()
archive = fgt.api.log.disk.virus_archive.get()
```

---

## Future: Log Generator

If we create a **log-specific generator** in the future, it would need to:

1. **Parse log type definitions** (manually defined, not from schemas)
2. **Generate shared log type classes** (`virus.py`, `traffic.py`, etc.)
3. **Generate storage container classes** (`disk.py`, `memory.py`, etc.)
4. **Handle composition pattern** - containers instantiate log types with storage parameter
5. **Map sub-resources** - know which log types have which sub-resources
6. **Generate base classes** - `RawResource`, `ArchiveResource`, etc.

### Proposed Structure

```
.dev/log_generator/
├── README.md
├── log_type_definitions.yaml     # Manual definitions of log types
├── generate_log.py                # Main log generator
├── templates/
│   ├── log_type_class.py.j2      # Template for shared log type
│   ├── storage_container.py.j2   # Template for Disk, Memory, etc.
│   └── base_resources.py.j2      # Template for base classes
└── definitions/
    ├── virus.yaml                # Log type definition
    ├── traffic.yaml
    ├── event.yaml
    └── storage_backends.yaml     # List of storage backends
```

---

## References

- **Old Implementation:** `archive_pre_schema_regen_20260103_090431/api/v2/log/`
- **FortiOS API Docs:** https://docs.fortinet.com/document/fortigate/7.6.0/fortios-rest-api/1/rest-api-reference
- **Log Endpoints:** `/api/v2/log/{storage}/{type}[/{subtype}][/raw|/archive]`

---

## Decision

**Current:** Keep log endpoints **manually implemented** (copy from old code)  
**Future:** Consider dedicated log generator if patterns stabilize  
**Rationale:** Composition pattern + no schemas + complex sub-resources = not suitable for schema-driven generator
