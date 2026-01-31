# IP/MAC Binding

Guide to managing IP/MAC binding settings and table entries.

## Overview

HFortix provides direct API access for IP/MAC binding:
- **IP/MAC Binding Settings** - Global binding configuration
- **IP/MAC Binding Table** - Individual binding entries

## Quick Examples

### IP/MAC Binding Table Entry

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create IP/MAC binding entry
binding = fgt.api.cmdb.firewall.ipmacbinding.table.post(
    seq_num=1,
    ip='192.168.1.100',
    mac='00:11:22:33:44:55',
    name='workstation-1',
    status='enable'
)

# List all bindings
bindings = fgt.api.cmdb.firewall.ipmacbinding.table.get()

# Check if binding exists
if fgt.api.cmdb.firewall.ipmacbinding.table.exists(seq_num='1'):
    print("Binding exists!")
```

### IP/MAC Binding Settings

```python
# Get global settings
settings = fgt.api.cmdb.firewall.ipmacbinding.setting.get()
```

## Coming Soon

Detailed documentation including:
- Binding table management
- Global settings configuration
- Integration with firewall policies
- Use cases (DHCP snooping, access control)
- Best practices

## Temporary Reference

For now, see:
- [API Documentation](/fortios/api-documentation/index.rst)
