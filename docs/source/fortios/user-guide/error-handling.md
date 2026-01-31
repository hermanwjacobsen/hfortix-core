# Error Handling

Comprehensive guide to error handling in HFortix.

```{note}
This content will be migrated from `docs/fortios/ERROR_HANDLING_CONFIG.md`
```

## Overview

HFortix provides configurable error handling with three modes:

- **raise** (default) - Raise exceptions
- **return** - Return error dict
- **print** - Print errors and continue

## Quick Example

```python
from hfortix import FortiOS, APIError, DuplicateEntryError

fgt = FortiOS(host='192.168.1.99', token='token')

# Default: raise exceptions
try:
    fgt.api.cmdb.firewall.address.post(name='test', subnet='10.0.0.1/32')
except DuplicateEntryError:
    print("Address already exists!")
except APIError as e:
    print(f"Error: {e.message}")

# Return error dict (error_mode parameter)
fgt_return = FortiOS(host='192.168.1.99', token='token', error_mode='return')
result = fgt_return.api.cmdb.firewall.policy.post(
    name='test',
    srcintf=[{"name": "internal"}],
    dstintf=[{"name": "wan1"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "ALL"}],
    action="accept"
)
if result.get('error'):
    print(f"Error: {result['error']}")
```

## Coming Soon

Detailed documentation including:
- All exception types
- Error handling modes
- Configuring global error handling
- Per-operation error handling
- Best practices

## Temporary Reference

For now, see:
- [Exception Reference](/fortios/api-reference/exceptions.rst)
- Current docs: `docs/fortios/ERROR_HANDLING_CONFIG.md` in repository
