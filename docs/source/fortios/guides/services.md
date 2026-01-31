# Service Management

Guide to managing custom services, service groups, and service categories.

## Overview

HFortix provides direct API access for three types of service objects:
- **Custom Services** - User-defined services
- **Service Groups** - Collections of services
- **Service Categories** - Service categorization

## Quick Examples

### Custom Service

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create custom TCP service
service = fgt.api.cmdb.firewall.service.custom.post(
    name='custom-app',
    protocol='TCP/UDP/SCTP',
    tcp_portrange='8080-8090',
    comment='Custom application service'
)

# Create UDP service
dns_service = fgt.api.cmdb.firewall.service.custom.post(
    name='custom-dns',
    protocol='TCP/UDP/SCTP',
    udp_portrange='5353',
    comment='Custom DNS service'
)
```

### Service Group

```python
# Create service group - simple list format (auto-converted)
web_services = fgt.api.cmdb.firewall.service.group.post(
    name='web-services',
    member=['HTTP', 'HTTPS', 'custom-app'],  # Converted to [{"name": "..."}]
    comment='All web-related services'
)
```

### Service Category

```python
# Manage service categories
categories = fgt.api.cmdb.firewall.service.category.get()
```

## Coming Soon

Detailed documentation including:
- Protocol types (TCP, UDP, ICMP, etc.)
- Port range configuration
- Service groups and nesting
- Integration with policies
- Cloning and templating
- Best practices

## Temporary Reference

For now, see:
- [API Documentation](/fortios/api-documentation/index.rst)
