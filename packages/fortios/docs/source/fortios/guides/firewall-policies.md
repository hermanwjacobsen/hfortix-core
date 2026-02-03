# Firewall Policy Management

Complete guide to managing firewall policies using direct API access.

```{note}
v0.5.0 removed convenience wrappers. Use `fgt.api.cmdb.firewall.policy.*` methods instead.
```

## Overview

HFortix provides full type-safe access to FortiGate firewall policies with support for 150+ parameters.

## Quick Example

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create firewall policy
policy = fgt.api.cmdb.firewall.policy.post(
    name='Allow-Web-Traffic',
    srcintf=[{"name": "port1"}],
    dstintf=[{"name": "port2"}],
    srcaddr=[{"name": "internal-network"}],
    dstaddr=[{"name": "web-server"}],
    service=[{"name": "HTTP"}, {"name": "HTTPS"}],
    action='accept',
    schedule='always',
    nat='enable'
)

# Check if policy exists
if fgt.api.cmdb.firewall.policy.exists(policyid='1'):
    print("Policy exists!")

# Clone policy
new_policy = fgt.api.cmdb.firewall.policy.clone(
    policyid='1',
    new_name='Allow-Web-Traffic-Copy'
)
```

## Coming Soon

Detailed documentation including:
- All policy parameters
- Address and service object integration
- NAT configuration
- Policy ordering and priorities
- Cloning and templating
- Best practices

## Temporary Reference

For now, see:
- [API Documentation](/fortios/api-documentation/index.rst)
