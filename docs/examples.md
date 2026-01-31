# HFortix FortiOS - Quick Start & Examples

Comprehensive examples and documentation for **hfortix-fortios** Python library - A modern, type-safe FortiOS REST API client.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Connection Methods](#connection-methods)
- [Basic Operations](#basic-operations)
- [Response Handling](#response-handling)
- [CMDB Endpoints](#cmdb-endpoints)
- [Monitor Endpoints](#monitor-endpoints)
- [Error Handling](#error-handling)
- [Advanced Features](#advanced-features)
- [Async Operations](#async-operations)
- [Debugging & Logging](#debugging--logging)

---

## Installation

```bash
pip install hfortix-fortios
```

**Requirements:**
- Python 3.8+
- FortiOS 6.0+ (tested on v7.6.4)
- API token or username/password

---

## Quick Start

### Direct FortiGate Connection

```python
from hfortix_fortios import FortiOS

# Create client with API token
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    port=443,
    verify=False,  # Disable SSL verification (not recommended for production)
    vdom="root"    # Default VDOM
)

# Get all firewall addresses
addresses = fgt.api.cmdb.firewall.address.get()

# Create a new address
result = fgt.api.cmdb.firewall.address.post(
    name="test_address1",
    type="ipmask",
    subnet="192.168.100.0/24",
    comment="Test IPv4 address"
)

# Close connection when done
fgt.close()
```

### Using Environment Variables (.env)

```python
# .env file:
# FORTIGATE_HOST=192.168.1.99
# FORTIGATE_TOKEN=your-api-token
# FORTIGATE_PORT=443
# FORTIGATE_VDOM=root

import os
from dotenv import load_dotenv
from hfortix_fortios import FortiOS

load_dotenv()

fgt = FortiOS(
    host=os.getenv("FORTIGATE_HOST"),
    token=os.getenv("FORTIGATE_TOKEN"),
    port=int(os.getenv("FORTIGATE_PORT", "443")),
    verify=False,
    vdom=os.getenv("FORTIGATE_VDOM", "root")
)
```

---

## Connection Methods

### 1. Direct FortiGate Connection (API Token)

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    port=443,
    verify=False,
    vdom="root",
    error_mode="return"  # Return errors instead of raising exceptions
)
```

### 2. FortiManager Proxy Connection

Connect to FortiGate **through** FortiManager:

```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="192.168.1.100",
    username="admin",
    password="your-password",
    verify=False,
    adom="root"  # ADOM name
)

# Login to FortiManager
fmg.login()

# Get proxied FortiGate connection
fgt = fmg.proxy(
    device="my-fortigate",  # Device name in FortiManager
    vdom="root"             # VDOM on FortiGate
)

# Now use fgt exactly like direct connection
addresses = fgt.api.cmdb.firewall.address.get()

# Logout when done
fmg.logout()
```

**Benefits of FMG Proxy:**
- Centralized management
- No direct FortiGate access needed
- Consistent API across multiple devices

---

## Basic Operations

### CRUD Operations (Create, Read, Update, Delete)

```python
# GET - Read all entries
addresses = fgt.api.cmdb.firewall.address.get()

# GET - Read specific entry
address = fgt.api.cmdb.firewall.address.get(name="test_address1")

# POST - Create new entry
result = fgt.api.cmdb.firewall.address.post(
    name="test_address1",
    type="ipmask",
    subnet="192.168.100.0/24",
    comment="Test IPv4 address"
)

# PUT - Update existing entry
result = fgt.api.cmdb.firewall.address.put(
    name="test_address1",
    comment="Updated comment"
)

# DELETE - Remove entry
result = fgt.api.cmdb.firewall.address.delete(name="test_address1")
```

### Firewall Policy Example

```python
# Create firewall policy
result = fgt.api.cmdb.firewall.policy.post(
    policyid=9999990,
    name="test_policy",
    srcintf=[{"name": "port3"}],
    dstintf=[{"name": "port4"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    action="accept",
    schedule="always",
    service=[{"name": "ALL"}],
    nat="disable",
    status="enable",
    logtraffic="all"
)

# Update policy
result = fgt.api.cmdb.firewall.policy.put(
    policyid=9999990,
    name="updated_policy_name",
    comments="Updated comments"
)

# Get specific policy
policy = fgt.api.cmdb.firewall.policy.get(policyid=9999990)

# Delete policy
result = fgt.api.cmdb.firewall.policy.delete(policyid=9999990)
```

---

## Response Handling

### Understanding Response Types

**CMDB endpoints** always return **FortiObject** or **FortiObjectList** with attribute access:

```python
# CMDB: Attribute access works
address = fgt.api.cmdb.firewall.address.get(name="test_address1")
print(address.name)           # ✅ Works - attribute access
print(address.subnet)         # ✅ Works
print(address.comment)        # ✅ Works
```

**Monitor/Log/Service endpoints** may return plain dicts - use dict-style access:

```python
# Monitor: Use dict-style access
switches = fgt.api.monitor.switch_controller.managed_switch.status.get()
switch = switches[0]

# ⚠️ May not work: switch.switch_id
# ✅ Always works: 
switch_dict = switch.to_dict()
switch_id = switch_dict.get('switch-id') or switch_dict.get('switch_id')
```

### Response Formats

Every response has multiple access methods:

```python
result = fgt.api.cmdb.firewall.address.get(name="test_address1")

# 1. Attribute access (CMDB only)
print(result.name)              # "test_address1"
print(result.subnet)            # "192.168.100.0/24"

# 2. Dict-style access (always works)
print(result.get("name"))       # "test_address1"

# 3. Full response as dict
full_dict = result.to_dict()
print(full_dict)                # {'name': 'test_address1', 'subnet': '192.168.100.0/24', ...}

# 4. Also available:
print(result.dict)              # Same as to_dict()
print(result.json)              # JSON string representation
print(result.raw)               # Raw response data
```

### HTTP Status and Metadata

```python
result = fgt.api.cmdb.firewall.address.get()

# HTTP response code
print(result.http_status_code)  # 200

# FortiOS status
print(result.http_status)       # "success"

# VDOM info
print(result.vdom)              # "root"

# Serial number
print(result.serial)            # "FGVM..."

# Version
print(result.version)           # "v7.6.4"
```

### Handling Lists

```python
# Get all addresses (returns list)
addresses = fgt.api.cmdb.firewall.address.get()

# Iterate over results
for addr in addresses:
    print(f"Name: {addr.name}, Subnet: {addr.get('subnet', 'N/A')}")

# Filter addresses
test_addresses = [a for a in addresses if a.name.startswith("test")]

# Count
print(f"Total addresses: {len(addresses)}")
```

---

## CMDB Endpoints

### Firewall Address Objects

```python
# IPv4 address
result = fgt.api.cmdb.firewall.address.post(
    name="server1",
    type="ipmask",
    subnet="10.1.1.10/32",
    comment="Production server"
)

# IPv4 range
result = fgt.api.cmdb.firewall.address.post(
    name="dhcp_range",
    type="iprange",
    start_ip="10.1.1.100",
    end_ip="10.1.1.200"
)

# FQDN address
result = fgt.api.cmdb.firewall.address.post(
    name="google_dns",
    type="fqdn",
    fqdn="dns.google"
)

# Geographic address
result = fgt.api.cmdb.firewall.address.post(
    name="block_country",
    type="geography",
    country="CN"
)
```

### Firewall Services

```python
# TCP service
result = fgt.api.cmdb.firewall.service.custom.post(
    name="custom_web",
    protocol="TCP/UDP/SCTP",
    tcp_portrange="8080-8089"
)

# UDP service
result = fgt.api.cmdb.firewall.service.custom.post(
    name="custom_syslog",
    protocol="TCP/UDP/SCTP",
    udp_portrange="514"
)

# ICMP service
result = fgt.api.cmdb.firewall.service.custom.post(
    name="icmp_echo",
    protocol="ICMP",
    icmptype=8,  # Echo request
    icmpcode=0
)
```

### VPN Configuration

```python
# IPsec Phase 1
result = fgt.api.cmdb.vpn.ipsec.phase1_interface.post(
    name="vpn_tunnel1",
    interface="wan1",
    ike_version=2,
    peertype="any",
    proposal="aes256-sha256",
    remote_gw="203.0.113.1",
    psksecret="your-preshared-key"
)

# IPsec Phase 2
result = fgt.api.cmdb.vpn.ipsec.phase2_interface.post(
    name="vpn_tunnel1_p2",
    phase1name="vpn_tunnel1",
    proposal="aes256-sha256",
    src_subnet="10.1.0.0/16",
    dst_subnet="10.2.0.0/16"
)
```

### Router Configuration

```python
# Static route
result = fgt.api.cmdb.router.static.post(
    dst="0.0.0.0/0",
    gateway="192.168.1.1",
    device="wan1",
    comment="Default route"
)

# BGP neighbor
result = fgt.api.cmdb.router.bgp.neighbor.post(
    ip="10.0.0.1",
    remote_as=65001,
    route_map_in="rm_in",
    route_map_out="rm_out"
)
```

### System Configuration

```python
# Interface configuration
result = fgt.api.cmdb.system.interface.put(
    name="port1",
    ip="192.168.1.99/24",
    allowaccess=["ping", "https", "ssh"],
    description="Management interface"
)

# Admin user
result = fgt.api.cmdb.system.admin.post(
    name="api_user",
    accprofile="super_admin",
    password="SecurePassword123!",
    trusthost1="192.168.1.0/24"
)

# DNS settings
result = fgt.api.cmdb.system.dns.put(
    primary="8.8.8.8",
    secondary="8.8.4.4"
)
```

---

## Monitor Endpoints

Monitor endpoints provide **real-time operational data** (read-only).

### System Status

```python
# System status (use dict access - Monitor fields may not have type hints)
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}")
print(f"Model: {status['model']}")
print(f"Log Disk Status: {status.get('log_disk_status', 'N/A')}")

# Resource usage
resources = fgt.api.monitor.system.resource.usage.get()
print(f"CPU: {resources.get('cpu', 'N/A')}%")
print(f"Memory: {resources.get('memory', 'N/A')}%")
```

### FortiSwitch Management

```python
# Get managed switches
switches = fgt.api.monitor.switch_controller.managed_switch.status.get(vdom="root")

for switch in switches:
    switch_dict = switch.to_dict()
    switch_id = switch_dict.get('switch-id') or switch_dict.get('switch_id')
    status = switch_dict.get('status')
    
    print(f"Switch: {switch_id}, Status: {status}")
    
    # Get port details
    if 'ports' in switch_dict:
        for port in switch_dict['ports']:
            port_name = port.get('interface', port.get('name'))
            port_status = port.get('status')
            print(f"  Port {port_name}: {port_status}")
```

### Bounce FortiSwitch Port

```python
# Bounce a specific port (restart port)
result = fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(
    vdom="root",
    mkey="S124FPTF22004975",  # Switch ID
    port="port1",
    duration=1  # Bounce duration in seconds
)

# Note: Switch must be in "Connected" state for this to work
```

### Active Sessions

```python
# Get active firewall sessions
sessions = fgt.api.monitor.firewall.session.get()

for session in sessions:
    print(f"Source: {session.get('src')}")
    print(f"Destination: {session.get('dst')}")
    print(f"Protocol: {session.get('proto')}")
```

### VPN Status

```python
# IPsec tunnel status
tunnels = fgt.api.monitor.vpn.ipsec.get()

for tunnel in tunnels:
    print(f"Name: {tunnel.get('name')}")
    print(f"Status: {tunnel.get('status')}")
    print(f"Remote Gateway: {tunnel.get('rgwy')}")
```

---

## Error Handling

### Error Modes

```python
# Mode 1: Return errors (default)
fgt = FortiOS(
    host="192.168.1.99",
    token="token",
    error_mode="return"  # Returns error response instead of raising
)

result = fgt.api.cmdb.firewall.address.get(name="nonexistent")
if result.http_status_code == 404:
    print("Address not found")

# Mode 2: Raise exceptions
fgt = FortiOS(
    host="192.168.1.99",
    token="token",
    error_mode="raise"  # Raises exceptions on errors
)

try:
    result = fgt.api.cmdb.firewall.address.get(name="nonexistent")
except ResourceNotFoundError as e:
    print(f"Error: {e}")
```

### Exception Types

```python
from hfortix_core.exceptions import (
    FortinetError,              # Base exception
    APIError,                   # API-related errors
    ResourceNotFoundError,      # 404 errors
    DuplicateEntryError,       # Duplicate resource
    InvalidValueError,         # Invalid parameter
    AuthenticationError,       # 401 errors
    PermissionDeniedError,     # 403 errors
    ServerError,               # 500 errors
    RateLimitError,            # 429 errors
    TimeoutError,              # Request timeout
)

# Example: Handle specific errors
try:
    result = fgt.api.cmdb.firewall.address.post(
        name="duplicate",
        type="ipmask",
        subnet="10.0.0.0/8"
    )
except DuplicateEntryError:
    print("Address already exists")
except InvalidValueError as e:
    print(f"Invalid parameter: {e}")
except AuthenticationError:
    print("Authentication failed - check token")
except ServerError as e:
    print(f"FortiGate error: {e}")
```

### Error Response Details

```python
# With error_mode="return"
result = fgt.api.cmdb.firewall.address.delete(name="nonexistent")

if result.http_status_code != 200:
    print(f"HTTP Status: {result.http_status_code}")
    print(f"Error Code: {result.error}")
    print(f"Message: {result.message}")
    
    # Common FortiOS error codes:
    # -3: Entry not found
    # -5: Duplicate entry
    # -6: Invalid value
    # -10: Object in use
    # -15: Permission denied
```

### Retry Logic

```python
import time

def retry_request(func, max_retries=3, delay=1):
    """Retry a request with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except (ServerError, TimeoutError) as e:
            if attempt == max_retries - 1:
                raise
            wait_time = delay * (2 ** attempt)
            print(f"Retry {attempt + 1}/{max_retries} after {wait_time}s...")
            time.sleep(wait_time)

# Usage
result = retry_request(
    lambda: fgt.api.cmdb.firewall.address.get()
)
```

---

## Advanced Features

### VDOM Support

```python
# Specify VDOM in client creation
fgt = FortiOS(
    host="192.168.1.99",
    token="token",
    vdom="production"  # Default VDOM for all requests
)

# Override VDOM per request
addresses_root = fgt.api.cmdb.firewall.address.get(vdom="root")
addresses_prod = fgt.api.cmdb.firewall.address.get(vdom="production")
addresses_test = fgt.api.cmdb.firewall.address.get(vdom="test")
```

### Filtering and Search

```python
# Get all addresses
all_addresses = fgt.api.cmdb.firewall.address.get()

# Filter in Python
test_addresses = [
    addr for addr in all_addresses 
    if addr.name.startswith("test_")
]

# Filter by type
ipmask_addresses = [
    addr for addr in all_addresses 
    if addr.get('type') == 'ipmask'
]

# Search by subnet
network = [
    addr for addr in all_addresses 
    if addr.get('subnet', '').startswith("10.1.")
]
```

### Bulk Operations

```python
# Create multiple addresses
addresses_to_create = [
    {"name": f"host_{i}", "type": "ipmask", "subnet": f"10.1.1.{i}/32"}
    for i in range(10, 20)
]

for addr in addresses_to_create:
    result = fgt.api.cmdb.firewall.address.post(**addr)
    print(f"Created: {addr['name']}")

# Bulk delete
test_addresses = fgt.api.cmdb.firewall.address.get()
for addr in test_addresses:
    if addr.name.startswith("test_"):
        fgt.api.cmdb.firewall.address.delete(name=addr.name)
        print(f"Deleted: {addr.name}")
```

### Complex Firewall Policies

```python
# Policy with multiple source/destination addresses
result = fgt.api.cmdb.firewall.policy.post(
    policyid=100,
    name="multi_addr_policy",
    srcintf=[{"name": "internal"}],
    dstintf=[{"name": "wan1"}],
    srcaddr=[
        {"name": "server1"},
        {"name": "server2"},
        {"name": "server3"}
    ],
    dstaddr=[
        {"name": "internet_services"}
    ],
    service=[
        {"name": "HTTP"},
        {"name": "HTTPS"}
    ],
    action="accept",
    schedule="business_hours",
    nat="enable",
    logtraffic="all"
)

# Policy with address groups
result = fgt.api.cmdb.firewall.policy.post(
    policyid=101,
    name="group_policy",
    srcintf=[{"name": "internal"}],
    dstintf=[{"name": "dmz"}],
    srcaddr=[{"name": "internal_network"}],  # Address group
    dstaddr=[{"name": "dmz_servers"}],       # Address group
    service=[{"name": "ALL"}],
    action="accept",
    nat="disable"
)
```

### Connection Statistics

```python
# Get connection stats
stats = fgt.get_connection_stats()

print(f"Total requests: {stats.get('requests', 0)}")
print(f"Successful: {stats.get('successful', 0)}")
print(f"Failed: {stats.get('failed', 0)}")
print(f"Average response time: {stats.get('avg_response_time', 0):.2f}s")

# Also available as property
stats = fgt.connection_stats
```

### Audit Logging

```python
# Export audit logs to file
fgt.export_audit_logs(
    filepath="/tmp/audit.json",
    format="json"
)

# Export to string
audit_json = fgt.export_audit_logs(format="json")

# Filter by HTTP method
get_requests = fgt.export_audit_logs(filter_method="GET")
post_requests = fgt.export_audit_logs(filter_method="POST")
```

---

## Async Operations

For **concurrent requests** and better performance with multiple API calls.

### Basic Async Usage

```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    # Create async client
    async with FortiOS(
        host="192.168.1.99",
        token="token",
        mode="async",  # Enable async mode
        verify=False
    ) as fgt:
        # Await API calls
        addresses = await fgt.api.cmdb.firewall.address.get()
        print(f"Found {len(addresses)} addresses")

# Run async code
asyncio.run(main())
```

### Concurrent Requests

```python
import asyncio
from hfortix_fortios import FortiOS

async def fetch_all_data():
    async with FortiOS(
        host="192.168.1.99",
        token="token",
        mode="async"
    ) as fgt:
        # Run multiple requests concurrently
        results = await asyncio.gather(
            fgt.api.cmdb.firewall.address.get(),
            fgt.api.cmdb.firewall.service.custom.get(),
            fgt.api.cmdb.firewall.policy.get(),
            fgt.api.monitor.system.status.get()
        )
        
        addresses, services, policies, status = results
        
        print(f"Addresses: {len(addresses)}")
        print(f"Services: {len(services)}")
        print(f"Policies: {len(policies)}")
        print(f"FortiOS Version: {status.get('version')}")

asyncio.run(fetch_all_data())
```

### Performance Comparison

```python
import time
import asyncio
from hfortix_fortios import FortiOS

# Synchronous (sequential)
def sync_requests():
    fgt = FortiOS(host="192.168.1.99", token="token")
    
    start = time.time()
    for _ in range(5):
        fgt.api.cmdb.firewall.address.get()
    sync_time = time.time() - start
    
    fgt.close()
    return sync_time

# Asynchronous (concurrent)
async def async_requests():
    async with FortiOS(
        host="192.168.1.99",
        token="token",
        mode="async"
    ) as fgt:
        start = time.time()
        await asyncio.gather(*[
            fgt.api.cmdb.firewall.address.get() 
            for _ in range(5)
        ])
        return time.time() - start

# Compare
sync_time = sync_requests()
async_time = asyncio.run(async_requests())

print(f"Sync: {sync_time:.2f}s")
print(f"Async: {async_time:.2f}s")
print(f"Speedup: {sync_time/async_time:.1f}x faster")
```

---

## Debugging & Logging

### Enable Debug Output

```python
from hfortix_core.logging import configure_logging

# Enable debug logging
configure_logging(
    level="DEBUG",           # DEBUG, INFO, WARNING, ERROR
    format="text",           # "text" or "json"
    use_color=True,          # Colorize output
    include_trace=True       # Include stack traces
)

# Now all API calls will show detailed debug info
fgt = FortiOS(host="192.168.1.99", token="token")
result = fgt.api.cmdb.firewall.address.get()
```

### JSON Structured Logging

```python
from hfortix_core.logging import configure_logging

# JSON logging for production
configure_logging(
    level="INFO",
    format="json",
    structured=True,
    output_file="/var/log/hfortix.log"
)
```

### Debug Session

```python
from hfortix_core.debug import DebugSession

# Create debug session
debug = DebugSession(name="troubleshooting")

# Capture request
debug.capture_request(
    method="GET",
    endpoint="/api/v2/cmdb/firewall/address",
    params={"name": "test"},
    response=result
)

# Print summary
debug.print_summary(format="json")

# Get all requests
summary = debug.get_summary()
print(f"Total requests: {summary['total_requests']}")
```

### Request/Response Inspection

```python
# Access last request details
result = fgt.api.cmdb.firewall.address.get()

# Raw response data
print(result.raw)

# HTTP status
print(f"Status: {result.http_status_code}")

# Full response as dict
print(result.to_dict())

# JSON representation
print(result.json)
```

---

## Best Practices

### 1. Always Close Connections

```python
# Using context manager (recommended)
from hfortix_fortios import FortiOS

with FortiOS(host="...", token="...") as fgt:
    addresses = fgt.api.cmdb.firewall.address.get()
    # Connection automatically closed

# Manual close
fgt = FortiOS(host="...", token="...")
try:
    addresses = fgt.api.cmdb.firewall.address.get()
finally:
    fgt.close()
```

### 2. Use Environment Variables

```python
# Don't hardcode credentials
import os
from dotenv import load_dotenv

load_dotenv()

fgt = FortiOS(
    host=os.getenv("FORTIGATE_HOST"),
    token=os.getenv("FORTIGATE_TOKEN"),
    verify=os.getenv("SSL_VERIFY", "false").lower() == "true"
)
```

### 3. Handle Errors Gracefully

```python
from hfortix_core.exceptions import APIError

try:
    result = fgt.api.cmdb.firewall.address.post(
        name="test",
        type="ipmask",
        subnet="10.0.0.0/8"
    )
except DuplicateEntryError:
    # Update instead
    result = fgt.api.cmdb.firewall.address.put(
        name="test",
        comment="Updated"
    )
except APIError as e:
    print(f"API error: {e}")
    # Log, retry, or fail gracefully
```

### 4. Validate Before Creating

```python
# Check if address exists before creating
addresses = fgt.api.cmdb.firewall.address.get()
existing_names = [a.name for a in addresses]

if "new_address" not in existing_names:
    result = fgt.api.cmdb.firewall.address.post(
        name="new_address",
        type="ipmask",
        subnet="10.1.1.0/24"
    )
else:
    print("Address already exists")
```

### 5. Use Type Hints

```python
from hfortix_fortios import FortiOS
from hfortix_fortios.models import FortiObject, FortiObjectList

def get_test_addresses(fgt: FortiOS) -> list[FortiObject]:
    """Get all addresses starting with 'test_'."""
    all_addresses: FortiObjectList = fgt.api.cmdb.firewall.address.get()
    return [addr for addr in all_addresses if addr.name.startswith("test_")]
```

### 6. Cleanup Test Objects

```python
def cleanup_test_objects(fgt: FortiOS) -> int:
    """Delete all test objects."""
    deleted = 0
    
    # Get all addresses
    addresses = fgt.api.cmdb.firewall.address.get()
    
    # Delete test addresses
    for addr in addresses:
        if addr.name.startswith("test_"):
            try:
                fgt.api.cmdb.firewall.address.delete(name=addr.name)
                deleted += 1
            except Exception as e:
                print(f"Failed to delete {addr.name}: {e}")
    
    return deleted
```

---

## Common Patterns

### Backup and Restore Configuration

```python
# Backup configuration
def backup_config(fgt: FortiOS, object_type: str) -> list:
    """Backup configuration objects."""
    if object_type == "firewall.address":
        return fgt.api.cmdb.firewall.address.get()
    elif object_type == "firewall.policy":
        return fgt.api.cmdb.firewall.policy.get()
    # Add more types as needed

# Restore configuration
def restore_config(fgt: FortiOS, backup: list):
    """Restore configuration from backup."""
    for obj in backup:
        obj_dict = obj.to_dict() if hasattr(obj, 'to_dict') else obj
        # Remove metadata fields
        for key in ['q_origin_key', 'uuid']:
            obj_dict.pop(key, None)
        # Recreate object
        # ... (implementation depends on object type)
```

### Monitor for Changes

```python
import time

def watch_firewall_sessions(fgt: FortiOS, interval: int = 10):
    """Monitor active firewall sessions."""
    while True:
        sessions = fgt.api.monitor.firewall.session.get()
        print(f"Active sessions: {len(sessions)}")
        
        for session in sessions[:5]:  # Show first 5
            print(f"  {session.get('src')} -> {session.get('dst')}")
        
        time.sleep(interval)
```

### Batch Import from CSV

```python
import csv

def import_addresses_from_csv(fgt: FortiOS, csv_file: str):
    """Import firewall addresses from CSV file."""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                result = fgt.api.cmdb.firewall.address.post(
                    name=row['name'],
                    type=row['type'],
                    subnet=row['subnet'],
                    comment=row.get('comment', '')
                )
                print(f"✓ Created: {row['name']}")
            except DuplicateEntryError:
                print(f"⊘ Skipped (exists): {row['name']}")
            except Exception as e:
                print(f"✗ Failed: {row['name']} - {e}")
```

---

## Troubleshooting

### Common Issues

**1. SSL Certificate Errors**
```python
# Disable SSL verification (not recommended for production)
fgt = FortiOS(host="...", token="...", verify=False)

# Or provide CA certificate
fgt = FortiOS(host="...", token="...", verify="/path/to/ca.crt")
```

**2. Authentication Failures**
```python
# Check token validity
# Generate new token in FortiGate: System > Administrators > Create New > REST API Admin

# Verify host and port
fgt = FortiOS(
    host="192.168.1.99",  # IP or hostname
    token="your-token",
    port=443              # Default HTTPS port
)
```

**3. Permission Denied Errors**
```python
# Check API admin profile permissions
# The API token needs appropriate permissions for each operation
# Review profile in: System > Admin Profiles
```

**4. VDOM Issues**
```python
# List available VDOMs
vdoms = fgt.api.cmdb.system.vdom.get()
for vdom in vdoms:
    print(vdom.name)

# Use correct VDOM
result = fgt.api.cmdb.firewall.address.get(vdom="root")
```

**5. Timeout Issues**
```python
# Increase timeout (future feature)
# Currently use default timeout
# For long-running operations, consider async mode
```

---

## Additional Resources

- **GitHub**: [hfortix repositories](https://github.com/)
- **FortiOS API Documentation**: Check FortiGate GUI > System > Feature Visibility > REST API
- **PyPI Package**: `pip install hfortix-fortios`
- **Type Stubs**: Full typing support with autocomplete

---

## Version Information

- **Library Version**: 0.5.145+
- **Tested FortiOS Versions**: 6.0+, 7.6.4
- **Python**: 3.8+
- **Dependencies**: httpx, typing-extensions, python-dotenv

---

## License

This documentation is provided as-is for educational and development purposes.

---

**Happy Coding! 🚀**
