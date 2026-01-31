# Schedule Management

Guide to managing schedules (recurring, onetime, and groups).

## Overview

HFortix provides direct API access for three types of schedules:
- **Recurring** - Regular schedules (daily, weekly)
- **Onetime** - Single occurrence schedules
- **Groups** - Collections of schedules

## Quick Examples

### Recurring Schedule

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Business hours schedule
schedule = fgt.api.cmdb.firewall.schedule.recurring.post(
    name='business-hours',
    day='monday tuesday wednesday thursday friday',
    start='08:00',
    end='18:00'
)

# Get all recurring schedules
schedules = fgt.api.cmdb.firewall.schedule.recurring.get()
```

### Onetime Schedule

```python
# Maintenance window
maintenance = fgt.api.cmdb.firewall.schedule.onetime.post(
    name='maintenance-window',
    start='2025-12-31 22:00',
    end='2026-01-01 02:00'
)
```

### Schedule Group

```python
# Group multiple schedules - simple list format (auto-converted)
group = fgt.api.cmdb.firewall.schedule.group.post(
    name='all-business-hours',
    member=['business-hours', 'extended-hours']  # Converted to [{"name": "..."}]
)

# Or explicit dict format
group = fgt.api.cmdb.firewall.schedule.group.post(
    name='all-business-hours',
    member=[{"name": "business-hours"}, {"name": "extended-hours"}]
)
```

## Coming Soon

Detailed documentation including:
- All schedule types
- Day and time configurations
- Schedule groups
- Cloning and templating
- Integration with policies
- Best practices

## Temporary Reference

For now, see:
- [API Documentation](/fortios/api-documentation/index.rst)
