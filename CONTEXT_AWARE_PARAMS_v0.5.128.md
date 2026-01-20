# Context-Aware Parameter Conversion (v0.5.128)

## Problem Summary

The v0.5.125-v0.5.127 whitelist system had a critical architectural flaw:
- **Single global whitelist** for all parameter contexts
- Couldn't handle parameters used in **BOTH** query and body contexts
- 102 parameters were used as both query params (need underscore) AND body fields (need hyphen)

### Example of the Problem

```python
# Same parameter, different contexts:
# As query param: ?ip_version=4       (needs underscore)
# As body field:  {"ip-version": 4}   (needs hyphen)

# v0.5.127 whitelist had ip_version, so:
fgt.api.monitor.firewall.sessions.post(ip_version=4)  # ❌ Sent {"ip_version": 4}
fgt.api.cmdb.icap.server.post(ip_address="192.168.1.1")  # ❌ Sent {"ip_address": "..."}
```

## Solution (v0.5.128)

Split into **context-specific** lists per API type:

### Architecture

For each API type (CMDB, Monitor, Log, Service):
1. `*_QUERY_PARAM_NO_HYPHEN` - Query/path parameters that preserve underscores
2. `*_BODY_FIELD_NO_HYPHEN` - Body fields that exceptionally preserve underscores

### Implementation

```python
# field_overrides.py
CMDB_QUERY_PARAM_NO_HYPHEN = {
    "datasource_format", "find_all_references", "primary_keys", 
    "skip_to", "unfiltered_count", "with_contents_hash", "with_meta"
}
CMDB_BODY_FIELD_NO_HYPHEN = set()  # Empty - all body fields use hyphens

MONITOR_QUERY_PARAM_NO_HYPHEN = {
    "ip_address", "ip_version", "ip_mask", "filter_logic", 
    "timestamp_from", "timestamp_to", # ... 104 total
}
MONITOR_BODY_FIELD_NO_HYPHEN = set()  # Empty - all body fields use hyphens

# builders.py - Updated to use body field lists
def build_cmdb_payload(**params):
    # Uses CMDB_BODY_FIELD_NO_HYPHEN
    
def build_api_payload(**params):
    # Uses MONITOR_BODY_FIELD_NO_HYPHEN (for Monitor/Service)
```

## Results

### Fixed Endpoints

All 102 dual-context parameters now work correctly:

```python
# Body fields now convert to hyphens ✅
fgt.api.monitor.firewall.sessions.post(ip_version=4)
# → {"ip-version": 4}

fgt.api.cmdb.icap.server.post(ip_address="192.168.1.1")
# → {"ip-address": "192.168.1.1"}

fgt.api.monitor.router.charts.post(ip_mask="255.255.255.0")
# → {"ip-mask": "255.255.255.0"}

fgt.api.monitor.user.device.query.post(filter_logic="and")
# → {"filter-logic": "and"}

# Query params still preserve underscores ✅
fgt.api.monitor.firewall.sessions.get(ip_version=4)
# → GET ?ip_version=4
```

### Statistics

- **CMDB**: 7 query params, 0 body field exceptions
- **Monitor**: 104 query params, 0 body field exceptions  
- **Log**: 7 query params, 0 body field exceptions
- **Service**: 0 query params, 0 body field exceptions

## Breaking Changes

None expected! The fix enables parameters to work correctly that were previously broken.

## Future Additions

If we discover body fields that genuinely need underscores (not hyphens):
1. Test and confirm with actual FortiOS API
2. Add to appropriate `*_BODY_FIELD_NO_HYPHEN` set
3. Document why it's an exception

As of v0.5.128, **zero** body field exceptions exist - all body fields use hyphen conversion.
