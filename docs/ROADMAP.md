# hfortix Feature Roadmap

> Last updated: January 9, 2026

## Overview

This document tracks planned features and enhancements for the hfortix SDK.

---

## 🎯 High Priority

### 1. Config Templates & Idempotent Apply
**Status:** Planned  
**Effort:** High

- Declarative configuration management (desired state → actual state)
- Idempotent `apply()` that only makes necessary changes
- Support for YAML/JSON template files
- Variable interpolation and Jinja2 templating

```python
# Example API
template = ConfigTemplate.from_yaml("firewall_baseline.yaml")
result = client.apply(template, dry_run=False)
```

### 2. Config Diff & Change Previews
**Status:** Planned  
**Effort:** Medium

- `diff()` helpers to show before/after payloads
- Per-endpoint and batch operation diffs
- Optional "dry-run" mode that returns diff without applying
- Human-readable and machine-parseable output formats

```python
# Example API
diff = client.cmdb.firewall.policy.diff(name="web-access", data=new_config)
print(diff.added, diff.removed, diff.changed)

# Dry-run mode
result = client.cmdb.firewall.policy.update(name="web-access", data=new_config, dry_run=True)
```

### 3. Backup, Snapshot & Restore Helpers
**Status:** Planned  
**Effort:** High

- Full config backup export/import with checksum verification
- Endpoint-specific "export" helpers for object trees
- Restore with dependency resolution
- Cross-firewall migration support

```python
# Full backup
backup = client.backup.create(include_certificates=True)
backup.save("fw01_backup_2026-01-09.tar.gz")

# Restore
client.backup.restore("fw01_backup_2026-01-09.tar.gz", verify_checksum=True)

# Object tree export (addresses + all references)
export = client.export.firewall_addresses(include_groups=True)
export.save("addresses_export.json")

# Import to another firewall
target_client.import_config(export, merge_strategy="skip_existing")
```

### 4. Reference Finder & Dependency Tracking
**Status:** Planned  
**Effort:** High

- Find all references to an object (where-used)
- Recursive reference tracing (refs of refs)
- Dependency graph visualization
- Safe delete with dependency check

```python
# Find all references to an address object
refs = client.refs.find("firewall.address", name="web-servers")
# Returns: policies, address groups, VIPs, etc.

# Recursive trace
tree = client.refs.trace("firewall.address", name="web-servers", depth=3)

# Safe delete (fails if referenced)
client.cmdb.firewall.address.delete(name="web-servers", safe=True)
# Raises: ObjectInUseError with list of referencing objects

# Force delete with cascade option
client.cmdb.firewall.address.delete(name="web-servers", cascade=True)
```

### 5. VDOM Management Helpers
**Status:** Planned  
**Effort:** Medium

- VDOM creation/deletion with cleanup
- VDOM export/import (migrate VDOM between firewalls)
- Safe VDOM delete (verify empty or force cleanup)

```python
# Delete VDOM with all objects
client.system.vdom.delete(name="customer-a", force=True, cleanup=True)

# Export VDOM config
vdom_export = client.export.vdom("customer-a")

# Import to another firewall
target_client.import_config(vdom_export, target_vdom="customer-a-restored")
```

---

## 🔄 Medium Priority

### 6. Pagination & Bulk Operations
**Status:** Planned  
**Effort:** Medium

- Uniform pagination iterator for monitor/log endpoints
- Batch create/update/delete wrappers
- Partial-failure reporting with rollback options

```python
# Pagination iterator
async for entry in client.log.fortianalyzer.iter_pages(filter="srcip=10.0.0.1"):
    process(entry)

# Bulk create with partial failure handling
results = client.cmdb.firewall.address.bulk_create([
    {"name": "server-1", "subnet": "10.0.1.1/32"},
    {"name": "server-2", "subnet": "10.0.1.2/32"},
    {"name": "server-3", "subnet": "10.0.1.3/32"},
])
print(results.succeeded, results.failed)
```

### 7. CLI Tool
**Status:** Planned  
**Effort:** Medium

- Quick operations from command line
- Interactive mode with autocomplete
- Pipe-friendly JSON output
- Config file for credentials

```bash
# Quick operations
hfortix get cmdb.firewall.policy --filter "name=web-access"
hfortix create cmdb.firewall.address --name "test" --subnet "10.0.0.1/32"
hfortix delete cmdb.firewall.address --name "test"

# Backup/restore
hfortix backup --output fw01_backup.tar.gz
hfortix restore fw01_backup.tar.gz --target 192.168.1.2

# Diff
hfortix diff cmdb.firewall.policy --file new_policy.yaml

# Interactive mode
hfortix shell
```

### 8. Connection Pooling
**Status:** Planned  
**Effort:** Low

- Reuse HTTP connections for better performance
- Configurable pool size
- Connection health checks

---

## 📋 Backlog

### 9. Request Builder Pattern
- Fluent API for complex queries
- Chainable filter/select/format methods

### 10. Schema Validation (Pre-request)
- Validate payloads against FortiOS schema before sending
- Better error messages for invalid configurations

### 11. Rate Limiting Controls
- Configurable rate limits per endpoint
- Automatic backoff on 429 responses

### 12. Webhook Integration
- Subscribe to FortiOS events
- Event-driven automation helpers

---

## ✅ Completed Features

| Feature | Version | Notes |
|---------|---------|-------|
| Full API Coverage (1,348 endpoints) | 0.5.0 | CMDB, Monitor, Log, Service |
| Type Hints & IDE Autocomplete | 0.5.0 | Full typing with .pyi stubs |
| Async Support | 0.5.0 | `FortiOSAsync` client |
| Response Objects | 0.5.0 | `response_mode="object"` |
| Audit Callbacks/Hooks | 0.5.0 | `audit_callback` parameter |
| Error Handling Modes | 0.5.0 | raise/return/print modes |
| Circuit Breaker | 0.5.0 | Built-in resilience |
| Literal Types for Config | 0.5.0 | Type-safe configuration |
| Filter Builder | 0.5.0 | Query construction helpers |

---

## Contributing

Have a feature request? Open an issue on GitHub or submit a PR!

## Version History

- **0.5.50** (2026-01-12): Current stable release - Bug fixes (CEFFormatter, StreamHandler), expanded test suite (366 tests)
- **0.5.49** (2026-01-10): Type stub fixes, comprehensive test suite
- **0.5.48** (2026-01-10): Fixed `.pyi` stub class name generation for multi-word categories
- **0.6.0** (TBD): Config templates, diff helpers
- **0.7.0** (TBD): Backup/restore, reference finder
- **1.0.0** (TBD): CLI tool, full feature set
