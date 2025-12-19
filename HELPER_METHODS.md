# Helper Methods Guide

This document provides comprehensive documentation for helper methods available in the hfortix library.

## Table of Contents

- [Overview](#overview)
- [The .exists() Method](#the-exists-method)
  - [Basic Usage](#basic-usage)
  - [Practical Examples](#practical-examples)
  - [Common Patterns](#common-patterns)
- [Available Endpoints](#available-endpoints)
- [Identifier Types Reference](#identifier-types-reference)

## Overview

Helper methods in hfortix simplify common operations and provide safer alternatives to standard API calls. Currently, the library includes the `.exists()` method on 288 CMDB endpoints that support full CRUD operations.

## The .exists() Method

### What It Does

The `.exists()` method checks if an object exists in the FortiGate configuration without raising an exception. It returns:
- `True` if the object exists
- `False` if the object does not exist

This is safer than using `.get()` which raises a `ResourceNotFoundError` for non-existent objects.

### Method Signature

```python
def exists(self, identifier: str) -> bool:
    """
    Check if an object exists without raising an exception.
    
    Args:
        identifier: The unique identifier for the object (name, policyid, etc.)
    
    Returns:
        bool: True if object exists, False otherwise
    """
```

### Basic Usage

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token', verify=False)

# Check if a firewall address exists
if fgt.api.cmdb.firewall.address.exists('web-server'):
    print("Address exists")
else:
    print("Address not found")

# Check if a firewall policy exists (uses policyid)
if fgt.api.cmdb.firewall.policy.exists('100'):
    print("Policy 100 exists")
else:
    print("Policy 100 not found")

# Check if a user exists
if fgt.api.cmdb.user.local.exists('admin'):
    print("User exists")
else:
    print("User not found")
```

### Practical Examples

#### 1. Safe Object Creation (Idempotent Operations)

```python
# Create object only if it doesn't exist
def ensure_address_exists(fgt, name, subnet):
    """Create firewall address only if it doesn't already exist."""
    if not fgt.api.cmdb.firewall.address.exists(name):
        print(f"Creating address: {name}")
        fgt.api.cmdb.firewall.address.create(
            name=name,
            subnet=subnet
        )
    else:
        print(f"Address already exists: {name}")

# Usage
ensure_address_exists(fgt, 'web-server', '10.0.1.100/32')
ensure_address_exists(fgt, 'db-server', '10.0.2.50/32')
```

#### 2. Conditional Updates

```python
# Update if exists, create if not
def create_or_update_address(fgt, name, subnet, comment=None):
    """Create or update a firewall address."""
    if fgt.api.cmdb.firewall.address.exists(name):
        print(f"Updating existing address: {name}")
        fgt.api.cmdb.firewall.address.update(
            name=name,
            comment=comment or f"Updated {name}"
        )
    else:
        print(f"Creating new address: {name}")
        fgt.api.cmdb.firewall.address.create(
            name=name,
            subnet=subnet,
            comment=comment or f"Created {name}"
        )

# Usage
create_or_update_address(fgt, 'web-server', '10.0.1.100/32', 'Production web server')
```

#### 3. Safe Deletion

```python
# Delete only if object exists
def safe_delete_address(fgt, name):
    """Delete firewall address only if it exists."""
    if fgt.api.cmdb.firewall.address.exists(name):
        print(f"Deleting address: {name}")
        fgt.api.cmdb.firewall.address.delete(name)
        return True
    else:
        print(f"Address not found, nothing to delete: {name}")
        return False

# Usage
safe_delete_address(fgt, 'old-server')
```

#### 4. Bulk Operations with Existence Checks

```python
# Process multiple objects safely
def create_addresses_batch(fgt, addresses):
    """Create multiple addresses, skipping existing ones."""
    created = []
    skipped = []
    
    for addr in addresses:
        if not fgt.api.cmdb.firewall.address.exists(addr['name']):
            fgt.api.cmdb.firewall.address.create(**addr)
            created.append(addr['name'])
        else:
            skipped.append(addr['name'])
    
    print(f"Created: {len(created)}, Skipped: {len(skipped)}")
    return {'created': created, 'skipped': skipped}

# Usage
addresses = [
    {'name': 'web-server-1', 'subnet': '10.0.1.10/32'},
    {'name': 'web-server-2', 'subnet': '10.0.1.11/32'},
    {'name': 'db-server', 'subnet': '10.0.2.50/32'},
]
results = create_addresses_batch(fgt, addresses)
```

#### 5. Configuration Validation

```python
# Validate required objects exist before applying config
def validate_policy_dependencies(fgt, policy_config):
    """Check if all required objects exist before creating a policy."""
    issues = []
    
    # Check source addresses
    for addr in policy_config.get('srcaddr', []):
        if not fgt.api.cmdb.firewall.address.exists(addr):
            issues.append(f"Source address not found: {addr}")
    
    # Check destination addresses
    for addr in policy_config.get('dstaddr', []):
        if not fgt.api.cmdb.firewall.address.exists(addr):
            issues.append(f"Destination address not found: {addr}")
    
    # Check services
    for svc in policy_config.get('service', []):
        if svc != 'ALL' and not fgt.api.cmdb.firewall.service.custom.exists(svc):
            issues.append(f"Service not found: {svc}")
    
    if issues:
        print("Validation failed:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("All dependencies validated successfully")
        return True

# Usage
policy = {
    'policyid': 100,
    'srcintf': ['port1'],
    'dstintf': ['port2'],
    'srcaddr': ['internal-network', 'dmz-network'],
    'dstaddr': ['web-server'],
    'service': ['HTTP', 'HTTPS'],
    'action': 'accept'
}

if validate_policy_dependencies(fgt, policy):
    fgt.api.cmdb.firewall.policy.create(**policy)
```

#### 6. User Management

```python
# Manage local users safely
def ensure_users_exist(fgt, users):
    """Ensure all users exist, create if missing."""
    for user in users:
        username = user['name']
        if not fgt.api.cmdb.user.local.exists(username):
            print(f"Creating user: {username}")
            fgt.api.cmdb.user.local.create(**user)
        else:
            print(f"User already exists: {username}")

# Usage
users = [
    {
        'name': 'alice',
        'type': 'password',
        'passwd': 'SecureP@ss123',
        'two-factor': 'disable'
    },
    {
        'name': 'bob',
        'type': 'password',
        'passwd': 'SecureP@ss456',
        'two-factor': 'fortitoken'
    }
]
ensure_users_exist(fgt, users)
```

#### 7. VPN Configuration

```python
# Manage IPsec tunnels safely
def ensure_ipsec_tunnel(fgt, tunnel_name, config):
    """Create or update IPsec Phase 1 tunnel."""
    if fgt.api.cmdb.vpn.ipsec_phase1_interface.exists(tunnel_name):
        print(f"Updating existing tunnel: {tunnel_name}")
        fgt.api.cmdb.vpn.ipsec_phase1_interface.update(
            name=tunnel_name,
            **config
        )
    else:
        print(f"Creating new tunnel: {tunnel_name}")
        fgt.api.cmdb.vpn.ipsec_phase1_interface.create(
            name=tunnel_name,
            **config
        )

# Usage
tunnel_config = {
    'type': 'static',
    'interface': 'wan1',
    'ike_version': 2,
    'peertype': 'any',
    'proposal': 'aes256-sha256',
    'remote_gw': '203.0.113.50'
}
ensure_ipsec_tunnel(fgt, 'branch-office', tunnel_config)
```

### Common Patterns

#### Pattern 1: Idempotent Configuration

```python
# Configuration that can be run multiple times safely
objects = [
    ('web-server', '10.0.1.100/32'),
    ('db-server', '10.0.2.50/32'),
    ('mail-server', '10.0.3.25/32'),
]

for name, subnet in objects:
    if not fgt.api.cmdb.firewall.address.exists(name):
        fgt.api.cmdb.firewall.address.create(name=name, subnet=subnet)
```

#### Pattern 2: Cleanup Before Creation

```python
# Remove old object if exists, then create new
def recreate_object(fgt, name, config):
    """Delete and recreate an object."""
    if fgt.api.cmdb.firewall.address.exists(name):
        print(f"Removing old object: {name}")
        fgt.api.cmdb.firewall.address.delete(name)
    
    print(f"Creating new object: {name}")
    fgt.api.cmdb.firewall.address.create(name=name, **config)

# Usage
recreate_object(fgt, 'web-server', {'subnet': '10.0.1.100/32'})
```

#### Pattern 3: Error Prevention

```python
# Avoid exceptions in automated scripts
def get_address_info(fgt, name):
    """Get address info only if it exists."""
    if fgt.api.cmdb.firewall.address.exists(name):
        return fgt.api.cmdb.firewall.address.get(name)
    else:
        print(f"Address not found: {name}")
        return None

# Usage
addr = get_address_info(fgt, 'web-server')
if addr:
    print(f"Address subnet: {addr.get('subnet')}")
```

## Available Endpoints

The `.exists()` method is available on **288 CMDB endpoints** that support full CRUD operations (Create, Read, Update, Delete). These include:

### Major Categories

- **Firewall** (89 endpoints): addresses, policies, VIPs, services, schedules, SSL profiles, etc.
- **System** (145 endpoints): interfaces, admins, DNS, DHCP, automation, etc.
- **User** (24 endpoints): local users, groups, LDAP, RADIUS, SAML, etc.
- **VPN** (19 endpoints): IPsec tunnels, certificates, L2TP, PPTP, etc.
- **Router** (26 endpoints): static routes, BGP, OSPF, policies, etc.
- **Switch Controller** (48 endpoints): managed switches, ACLs, QoS, VLANs, etc.
- **Wireless Controller** (44 endpoints): APs, SSIDs, profiles, hotspot20, etc.
- **Application** (5 endpoints): custom apps, groups, lists, etc.
- **Antivirus** (4 endpoints): profiles, quarantine, settings, etc.
- **Web Filter** (14 endpoints): profiles, content filters, URL filters, etc.
- **IPS** (8 endpoints): sensors, custom signatures, decoders, etc.
- **DLP** (8 endpoints): sensors, dictionaries, file patterns, etc.
- **ZTNA** (5 endpoints): web portals, proxies, reverse connectors, etc.

### Full List by Category

See [ENDPOINT_METHODS.md](ENDPOINT_METHODS.md) for the complete list of all 857 endpoints and their available methods.

## Identifier Types Reference

Different endpoints use different types of identifiers. Here's a quick reference:

| Endpoint Category | Identifier Type | Example |
|------------------|----------------|---------|
| Most CMDB objects | `name` | `'web-server'` |
| Firewall policies | `policyid` | `'100'` |
| Static routes | `seq-num` | `'1'` |
| VPN certificates | `name` | `'Fortinet_SSL'` |
| User local | `name` | `'admin'` |
| System admins | `name` | `'api-user'` |
| DHCP servers | Interface `id` | `'1'` |
| DNS database | `name` | `'example.com'` |

### Examples by Endpoint

```python
# Firewall address (uses 'name')
fgt.api.cmdb.firewall.address.exists('web-server')

# Firewall policy (uses 'policyid')
fgt.api.cmdb.firewall.policy.exists('100')

# User local (uses 'name')
fgt.api.cmdb.user.local.exists('testuser')

# Static route (uses 'seq-num')
fgt.api.cmdb.router.static.exists('1')

# VPN IPsec Phase 1 (uses 'name')
fgt.api.cmdb.vpn.ipsec_phase1_interface.exists('tunnel-to-branch')

# System interface (uses 'name')
fgt.api.cmdb.system.interface.exists('port1')

# DHCP server (uses interface 'id')
fgt.api.cmdb.system.dhcp_server.exists('1')

# Address group (uses 'name')
fgt.api.cmdb.firewall.addrgrp.exists('web-servers')

# Service custom (uses 'name')
fgt.api.cmdb.firewall.service.custom.exists('custom-tcp-8080')

# Application custom (uses 'tag')
fgt.api.cmdb.application.custom.exists('custom-app')
```

### Finding the Identifier

If you're unsure what identifier type an endpoint uses:

1. **Check the endpoint's `.get()` method** - it takes the same parameter
2. **Look at the FortiGate API documentation** for that endpoint
3. **List all objects** with `.get()` (no parameters) and examine the results

```python
# Example: Find identifier type for an endpoint
result = fgt.api.cmdb.firewall.address.get()
# Look at the results structure to see what field is the unique key
# Usually it's 'name', 'policyid', 'id', 'seq-num', etc.
```

## Best Practices

1. **Always check existence before deletion** to avoid unnecessary errors
2. **Use `.exists()` in idempotent scripts** that might run multiple times
3. **Validate dependencies** before creating objects that reference others
4. **Batch operations** benefit from existence checks to skip already-processed items
5. **Error handling** becomes simpler when you check existence first

## Comparison with .get()

### Using .get() (raises exception)

```python
from hfortix import FortiOS, ResourceNotFoundError

try:
    addr = fgt.api.cmdb.firewall.address.get('web-server')
    print("Address exists")
except ResourceNotFoundError:
    print("Address not found")
```

### Using .exists() (no exception)

```python
if fgt.api.cmdb.firewall.address.exists('web-server'):
    print("Address exists")
    addr = fgt.api.cmdb.firewall.address.get('web-server')
else:
    print("Address not found")
```

The `.exists()` method is cleaner and more efficient when you only need to check existence.

## Related Documentation

- [ENDPOINT_METHODS.md](ENDPOINT_METHODS.md) - Complete API method reference for all 857 endpoints
- [QUICKSTART.md](QUICKSTART.md) - Getting started guide
- [CHANGELOG.md](CHANGELOG.md) - Version history and changes
- [README.md](README.md) - Main package documentation

## Support

For issues or questions:
- Check the [examples](#practical-examples) above
- Review the [QUICKSTART.md](QUICKSTART.md) guide
- Consult the FortiOS API documentation
- Examine the endpoint-specific test files in the development workspace
