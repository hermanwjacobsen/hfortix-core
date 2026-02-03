# HFortix Examples - Real-World Use Cases

> **For AI Assistants**: This file contains copy-paste ready examples for common Fortinet automation tasks using HFortix.

## Table of Contents

1. [Basic Connection & Authentication](#basic-connection--authentication)
2. [Firewall Policy Management](#firewall-policy-management)
3. [Network Interface Configuration](#network-interface-configuration)
4. [VPN Configuration](#vpn-configuration)
5. [Address & Service Objects](#address--service-objects)
6. [Monitoring & Diagnostics](#monitoring--diagnostics)
7. [Backup & Restore](#backup--restore)
8. [Batch Operations with Transactions](#batch-operations-with-transactions)
9. [Async Operations](#async-operations)
10. [FortiManager Proxy](#fortimanager-proxy)

---

## Basic Connection & Authentication

### Simple Connection
```python
from hfortix_fortios import FortiOS

# Using API token (recommended)
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token"
)

# Check connection
status = fgt.api.monitor.system.status.get()
print(f"Connected to: {status['hostname']} (Model: {status['model']})")

# Always close when done
fgt.close()
```

### Context Manager (Auto-close)
```python
from hfortix_fortios import FortiOS

with FortiOS(host="192.168.1.99", token="token") as fgt:
    status = fgt.api.monitor.system.status.get()
    print(f"Hostname: {status['hostname']}")
    # Automatically closed on exit
```

### With Custom Settings
```python
fgt = FortiOS(
    host="192.168.1.99",
    token="token",
    verify_ssl=False,          # Disable SSL verification
    timeout=30,                # Request timeout
    rate_limit=10,             # Max 10 requests/second
    max_retries=3,             # Retry failed requests
    retry_delay=1.0            # Wait 1s between retries
)
```

---

## Firewall Policy Management

### Create Firewall Policy
```python
# Create a new firewall policy
fgt.api.cmdb.firewall.policy.post(
    policyid=100,
    name="Allow-Web-Traffic",
    srcintf=[{"name": "port1"}],
    dstintf=[{"name": "port2"}],
    srcaddr=[{"name": "LAN-Subnet"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "HTTP"}, {"name": "HTTPS"}],
    action="accept",
    schedule="always",
    nat="enable",
    logtraffic="all",
    comments="Allow internal users to browse internet"
)
```

### Update Existing Policy
```python
# Update policy by ID
fgt.api.cmdb.firewall.policy.put(
    policyid=100,
    name="Allow-Web-Traffic-Updated",
    logtraffic="disable"  # Only changed fields needed
)
```

### Delete Policy
```python
# Delete by ID
fgt.api.cmdb.firewall.policy.delete(policyid=100)
```

### Get All Policies
```python
# Get all firewall policies
policies = fgt.api.cmdb.firewall.policy.get()

for policy in policies:
    print(f"Policy {policy.policyid}: {policy.name}")
    print(f"  Action: {policy.action}")
    print(f"  Source: {[i.name for i in policy.srcintf]}")
    print(f"  Destination: {[i.name for i in policy.dstintf]}")
```

### Get Specific Policy
```python
# Get single policy by ID
policy = fgt.api.cmdb.firewall.policy.get(policyid=100)
print(f"Policy: {policy.name}")
print(f"Status: {policy.status}")
```

### Filter Policies
```python
# Find policies with specific criteria
policies = fgt.api.cmdb.firewall.policy.get(
    filter="action==accept&nat==enable"
)

for policy in policies:
    print(f"{policy.policyid}: {policy.name} - NAT enabled")
```

### Move Policy Position
```python
# Move policy to specific position
fgt.api.cmdb.firewall.policy.move(
    policyid=100,
    action="after",
    after=50  # Move policy 100 after policy 50
)
```

---

## Network Interface Configuration

### Create VLAN Interface
```python
fgt.api.cmdb.system.interface.post(
    name="vlan100",
    type="vlan",
    vlanid=100,
    interface="port1",
    ip="10.0.100.1 255.255.255.0",
    allowaccess=["ping", "https"],
    description="Management VLAN"
)
```

### Configure Physical Interface
```python
fgt.api.cmdb.system.interface.put(
    name="port1",
    mode="static",
    ip="192.168.1.1 255.255.255.0",
    allowaccess=["ping", "https", "ssh"],
    description="WAN Interface"
)
```

### Create Loopback Interface
```python
fgt.api.cmdb.system.interface.post(
    name="loopback0",
    type="loopback",
    ip="10.255.255.1 255.255.255.255",
    description="Router ID for BGP"
)
```

### Get Interface Status
```python
# Get real-time interface statistics
interfaces = fgt.api.monitor.system.interface.get()

for iface in interfaces:
    print(f"Interface: {iface['name']}")
    print(f"  Status: {iface['link']}")
    print(f"  Speed: {iface['speed']}")
    print(f"  RX: {iface['rx_bytes']} bytes")
    print(f"  TX: {iface['tx_bytes']} bytes")
```

---

## VPN Configuration

### IPsec Phase 1
```python
fgt.api.cmdb.vpn.ipsec.phase1_interface.post(
    name="HQ-to-Branch",
    interface="wan1",
    ike_version=2,
    peertype="any",
    net_device="disable",
    mode="main",
    proposal="aes256-sha256",
    dhgrp="14 5",
    remote_gw="203.0.113.10",
    psksecret="YourPreSharedKey123!",
    dpd="on-idle",
    dpd_retryinterval=5
)
```

### IPsec Phase 2
```python
fgt.api.cmdb.vpn.ipsec.phase2_interface.post(
    name="HQ-to-Branch-P2",
    phase1name="HQ-to-Branch",
    proposal="aes256-sha256",
    dhgrp="14 5",
    replay="enable",
    pfs="enable",
    src_subnet="10.0.0.0 255.255.0.0",
    dst_subnet="10.1.0.0 255.255.0.0"
)
```

### SSL VPN Settings
```python
fgt.api.cmdb.vpn.ssl.settings.put(
    servercert="Fortinet_Factory",
    tunnel_ip_pools=[{"name": "SSLVPN_TUNNEL_ADDR1"}],
    port=10443,
    source_interface=[{"name": "wan1"}],
    default_portal="full-access"
)
```

### SSL VPN Portal
```python
fgt.api.cmdb.vpn.ssl.web.portal.post(
    name="remote-workers",
    tunnel_mode="enable",
    web_mode="enable",
    ip_pools=[{"name": "SSLVPN_TUNNEL_ADDR1"}],
    split_tunneling="enable",
    split_tunneling_routing_address=[
        {"name": "Internal-Subnets"}
    ]
)
```

---

## Address & Service Objects

### Create Address Object
```python
# Single IP
fgt.api.cmdb.firewall.address.post(
    name="webserver",
    subnet="10.0.1.100 255.255.255.255",
    comment="Production web server"
)

# Subnet
fgt.api.cmdb.firewall.address.post(
    name="LAN-Subnet",
    subnet="10.0.0.0 255.255.255.0",
    comment="Internal LAN"
)

# FQDN
fgt.api.cmdb.firewall.address.post(
    name="github",
    type="fqdn",
    fqdn="github.com",
    comment="GitHub servers"
)

# IP Range
fgt.api.cmdb.firewall.address.post(
    name="DHCP-Range",
    type="iprange",
    start_ip="10.0.0.100",
    end_ip="10.0.0.200"
)
```

### Create Address Group
```python
fgt.api.cmdb.firewall.addrgrp.post(
    name="Servers",
    member=[
        {"name": "webserver"},
        {"name": "database"},
        {"name": "fileserver"}
    ],
    comment="All production servers"
)
```

### Create Custom Service
```python
# TCP service
fgt.api.cmdb.firewall.service.custom.post(
    name="Custom-App-8080",
    category="General",
    protocol="TCP/UDP/SCTP",
    tcp_portrange="8080",
    comment="Custom application port"
)

# UDP service
fgt.api.cmdb.firewall.service.custom.post(
    name="Custom-VPN-4500",
    protocol="TCP/UDP/SCTP",
    udp_portrange="4500"
)
```

### Create Service Group
```python
fgt.api.cmdb.firewall.service.group.post(
    name="Web-Services",
    member=[
        {"name": "HTTP"},
        {"name": "HTTPS"},
        {"name": "Custom-App-8080"}
    ]
)
```

---

## Monitoring & Diagnostics

### System Status
```python
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}")
print(f"Model: {status['model']}")
print(f"Version: {status['version']}")
print(f"Serial: {status['serial']}")
print(f"Uptime: {status['uptime']} seconds")
```

### Active Sessions
```python
sessions = fgt.api.monitor.firewall.session.get()
print(f"Total active sessions: {len(sessions)}")

for session in sessions[:10]:  # First 10
    print(f"{session['src']}:{session['srcport']} -> "
          f"{session['dst']}:{session['dstport']} "
          f"({session['proto']})")
```

### Interface Statistics
```python
interfaces = fgt.api.monitor.system.interface.get()

for iface in interfaces:
    print(f"\n{iface['name']}:")
    print(f"  Link: {iface['link']}")
    print(f"  RX Packets: {iface['rx_packets']}")
    print(f"  TX Packets: {iface['tx_packets']}")
    print(f"  RX Errors: {iface['rx_errors']}")
    print(f"  TX Errors: {iface['tx_errors']}")
```

### Execute Ping
```python
result = fgt.api.monitor.system.ping.post(
    host="8.8.8.8",
    count=4
)
print(result.raw)  # Ping output
```

### Execute Traceroute
```python
result = fgt.api.monitor.system.traceroute.post(
    host="8.8.8.8"
)
print(result.raw)
```

### Check VPN Status
```python
# IPsec tunnels
tunnels = fgt.api.monitor.vpn.ipsec.get()
for tunnel in tunnels:
    print(f"Tunnel: {tunnel['name']}")
    print(f"  Status: {tunnel['status']}")

# SSL VPN sessions
ssl_sessions = fgt.api.monitor.vpn.ssl.get()
print(f"Active SSL VPN users: {len(ssl_sessions)}")
```

### System Resources
```python
resources = fgt.api.monitor.system.resource.usage.get()
print(f"CPU Usage: {resources['cpu']}%")
print(f"Memory: {resources['mem_used']} / {resources['mem_total']} MB")
print(f"Disk: {resources['disk_used']}%")
```

---

## Backup & Restore

### Backup Configuration
```python
# Full backup
backup = fgt.api.monitor.system.config.backup.get(
    scope="global"
)

# Save to file
with open("fortigate-backup.conf", "w") as f:
    f.write(backup.raw_text)

print("Configuration backed up successfully")
```

### Restore Configuration
```python
# Read backup file
with open("fortigate-backup.conf", "r") as f:
    config = f.read()

# Restore
fgt.api.monitor.system.config.restore.post(
    source="upload",
    file_content=config,
    scope="global"
)
```

### Export Specific Configuration
```python
# Export only firewall addresses
addresses_backup = fgt.api.cmdb.firewall.address.get()

import json
with open("addresses-backup.json", "w") as f:
    json.dump([addr.dict for addr in addresses_backup], f, indent=2)
```

---

## Batch Operations with Transactions

### Atomic Configuration Changes
```python
# All changes succeed or all fail
try:
    with fgt.transaction() as txn:
        # Create address
        fgt.api.cmdb.firewall.address.post(
            name="new-server",
            subnet="10.0.1.50 255.255.255.255"
        )
        
        # Create policy
        fgt.api.cmdb.firewall.policy.post(
            policyid=150,
            name="New-Server-Access",
            srcintf=[{"name": "port1"}],
            dstintf=[{"name": "port2"}],
            srcaddr=[{"name": "all"}],
            dstaddr=[{"name": "new-server"}],
            service=[{"name": "ALL"}],
            action="accept"
        )
        
        # Create route
        fgt.api.cmdb.router.static.post(
            dst="10.0.1.0 255.255.255.0",
            gateway="192.168.1.1",
            device="port1"
        )
        
    print("All changes committed successfully")
    
except Exception as e:
    print(f"Transaction failed, all changes rolled back: {e}")
```

### Transactional Function Decorator
```python
@fgt.transactional(timeout=120)
def deploy_branch_office():
    """Deploy complete branch office configuration atomically"""
    
    # VLANs
    for vlan_id in [100, 200, 300]:
        fgt.api.cmdb.system.interface.post(
            name=f"vlan{vlan_id}",
            type="vlan",
            vlanid=vlan_id,
            interface="port1",
            ip=f"10.0.{vlan_id}.1 255.255.255.0"
        )
    
    # Address objects
    fgt.api.cmdb.firewall.address.post(
        name="HQ-Network",
        subnet="10.1.0.0 255.255.0.0"
    )
    
    # VPN tunnel
    fgt.api.cmdb.vpn.ipsec.phase1_interface.post(
        name="Branch-to-HQ",
        interface="wan1",
        ike_version=2,
        remote_gw="203.0.113.1",
        psksecret="SecureKey123"
    )
    
    return {"status": "success", "site": "Branch Office"}

# Execute - automatically wrapped in transaction
result = deploy_branch_office()
print(result)
```

---

## Async Operations

### Basic Async
```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    async with FortiOS(host="192.168.1.99", token="token") as fgt:
        # Single async call
        status = await fgt.api.monitor.system.status.get_async()
        print(f"Hostname: {status['hostname']}")

asyncio.run(main())
```

### Concurrent Operations
```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    async with FortiOS(host="192.168.1.99", token="token") as fgt:
        # Run multiple queries concurrently
        results = await asyncio.gather(
            fgt.api.cmdb.firewall.address.get_async(),
            fgt.api.cmdb.firewall.policy.get_async(),
            fgt.api.cmdb.system.interface.get_async(),
            fgt.api.monitor.system.status.get_async()
        )
        
        addresses, policies, interfaces, status = results
        
        print(f"Addresses: {len(addresses)}")
        print(f"Policies: {len(policies)}")
        print(f"Interfaces: {len(interfaces)}")
        print(f"Hostname: {status['hostname']}")

asyncio.run(main())
```

### Async Batch Processing
```python
async def create_multiple_addresses():
    async with FortiOS(host="192.168.1.99", token="token") as fgt:
        # Prepare data
        servers = [
            {"name": f"server-{i}", "subnet": f"10.0.1.{i} 255.255.255.255"}
            for i in range(10, 20)
        ]
        
        # Create all concurrently
        tasks = [
            fgt.api.cmdb.firewall.address.post_async(**server)
            for server in servers
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Failed to create server-{i+10}: {result}")
            else:
                print(f"Created server-{i+10}")

asyncio.run(create_multiple_addresses())
```

---

## FortiManager Proxy

### Connect Through FortiManager
```python
from hfortix_fortios import FortiOS

# Manage FortiGate through FortiManager
fgt = FortiOS(
    host="192.168.1.10",  # FortiGate IP
    token="fortigate-api-token",
    fmg_proxy={
        "host": "fortimanager.example.com",
        "username": "admin",
        "password": "fmg-password",
        "adom": "root"  # Optional, defaults to "root"
    }
)

# All API calls now go through FortiManager
status = fgt.api.monitor.system.status.get()
print(f"Managed device: {status['hostname']}")

# Create policy via FortiManager
fgt.api.cmdb.firewall.policy.post(
    policyid=200,
    name="FMG-Managed-Policy",
    srcintf=[{"name": "any"}],
    dstintf=[{"name": "any"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "ALL"}],
    action="accept"
)

fgt.close()
```

### Manage Multiple Devices
```python
devices = [
    {"host": "192.168.1.10", "name": "Branch-1"},
    {"host": "192.168.1.20", "name": "Branch-2"},
    {"host": "192.168.1.30", "name": "Branch-3"}
]

fmg_config = {
    "host": "fortimanager.example.com",
    "username": "admin",
    "password": "password"
}

for device in devices:
    with FortiOS(
        host=device["host"],
        token="api-token",
        fmg_proxy=fmg_config
    ) as fgt:
        status = fgt.api.monitor.system.status.get()
        print(f"{device['name']}: {status['hostname']} - {status['version']}")
        
        # Deploy same configuration to all
        fgt.api.cmdb.firewall.address.post(
            name="Corporate-Network",
            subnet="10.0.0.0 255.255.0.0"
        )
```

---

## Error Handling

### Basic Error Handling
```python
from hfortix_fortios import FortiOS, FortiOSError

fgt = FortiOS(host="192.168.1.99", token="token")

try:
    fgt.api.cmdb.firewall.address.post(
        name="test",
        subnet="invalid-subnet"
    )
except FortiOSError as e:
    print(f"Error: {e.message}")
    print(f"Status Code: {e.status_code}")
    print(f"HTTP Method: {e.http_method}")
    print(f"Path: {e.path}")
```

### Retry on Specific Errors
```python
import time
from hfortix_fortios import FortiOS, FortiOSError

def create_address_with_retry(name, subnet, max_retries=3):
    fgt = FortiOS(host="192.168.1.99", token="token")
    
    for attempt in range(max_retries):
        try:
            fgt.api.cmdb.firewall.address.post(
                name=name,
                subnet=subnet
            )
            print(f"Successfully created address: {name}")
            break
            
        except FortiOSError as e:
            if e.status_code == 424 and attempt < max_retries - 1:
                # Object already exists, retry
                print(f"Attempt {attempt + 1} failed, retrying...")
                time.sleep(2)
            else:
                raise
    
    fgt.close()
```

---

**For AI Assistants**: These are production-ready examples. When a user asks about Fortinet automation, reference these patterns and adapt them to their specific use case.
