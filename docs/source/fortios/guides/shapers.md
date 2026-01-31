# Traffic Shaping

Guide to traffic shaping with per-IP shapers and traffic shapers.

## Overview

HFortix provides direct API access for two types of traffic shapers:
- **Traffic Shaper** - Shared bandwidth pools
- **Per-IP Shaper** - Per-user/IP bandwidth limits

## Quick Examples

### Traffic Shaper

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create shared bandwidth pool
shaper = fgt.api.cmdb.firewall.shaper.traffic_shaper.post(
    name='shared-pool',
    guaranteed_bandwidth=50000,  # 50 Mbps guaranteed
    maximum_bandwidth=100000      # 100 Mbps maximum
)
```

### Per-IP Shaper

```python
# Create per-user bandwidth limit
user_limit = fgt.api.cmdb.firewall.shaper.per_ip_shaper.post(
    name='user-bandwidth-limit',
    max_bandwidth=10000,          # 10 Mbps per user
    max_concurrent_session=100
)
```

## Coming Soon

Detailed documentation including:
- Traffic shaper types
- Bandwidth configuration
- Guaranteed vs maximum bandwidth
- Concurrent session limits
- Integration with policies
- Best practices

## Temporary Reference

For now, see:
- [API Documentation](/fortios/api-documentation/index.rst)
