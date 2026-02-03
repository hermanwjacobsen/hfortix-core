# HFortix FortiOS

[![PyPI version](https://badge.fury.io/py/hfortix-fortios.svg)](https://pypi.org/project/hfortix-fortios/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Complete Python SDK for FortiOS/FortiGate automation** - 8,000+ API endpoints with full type hints

## 📦 Overview

`hfortix-fortios` provides a comprehensive, production-ready Python client for FortiOS/FortiGate firewalls. Auto-generated from official FortiOS 7.6.5 schemas with complete type safety and IDE autocomplete.

### Key Features

- ✅ **8,000+ API Endpoints** - Complete FortiOS REST API coverage
- 🎯 **Full Type Hints** - Perfect IDE autocomplete with `.pyi` stub files
- 🔄 **Async/Await Support** - High-performance asynchronous operations
- 📘 **Auto-generated** - From official Fortinet schemas (FortiOS 7.6.5)
- 🛡️ **Production Ready** - Transaction support, error handling, retries
- 🎨 **Pythonic API** - Clean, intuitive interface

## 🚀 Installation

```bash
# Install fortios package (includes hfortix-core automatically)
pip install hfortix-fortios

# Or install via meta-package
pip install hfortix[fortios]
```

## 💡 Quick Start

### Basic Usage

```python
from hfortix_fortios import FortiOSClient

# Connect to FortiGate
client = FortiOSClient(
    host="192.168.1.99",
    token="your-api-token",
    verify=False  # Optional: disable SSL verification
)

# Get all firewall policies
policies = client.api.v2.cmdb.firewall.policy.get()

for policy in policies:
    print(f"Policy {policy.policyid}: {policy.name}")

# Create a firewall address
client.api.v2.cmdb.firewall.address.post(
    name="web-server",
    subnet="192.168.1.100 255.255.255.255",
    comment="Production web server"
)

# Update an address
client.api.v2.cmdb.firewall.address.put(
    name="web-server",
    comment="Updated comment"
)

# Delete an address
client.api.v2.cmdb.firewall.address.delete(name="web-server")
```

### Async Usage

```python
from hfortix_fortios import AsyncFortiOSClient

async def main():
    async with AsyncFortiOSClient(
        host="192.168.1.99",
        token="your-api-token"
    ) as client:
        # Get system status
        status = await client.api.v2.monitor.system.status.get()
        print(f"Hostname: {status.hostname}")
        
        # Get all interfaces
        interfaces = await client.api.v2.monitor.system.interface.select().get()
        for iface in interfaces:
            print(f"{iface.name}: {iface.ip}")

asyncio.run(main())
```

### FortiManager Proxy

Manage FortiGate devices through FortiManager:

```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    adom="root"
)

# Get proxied connection to managed device
fgt = fmg.get_device("firewall-01")

# Use same API as direct FortiOS connection
addresses = fgt.api.v2.cmdb.firewall.address.get()

# Clean up
fmg.logout()
```

## 📚 API Structure

The client provides access to all FortiOS API endpoints organized by category:

```python
client.api.v2.cmdb.*       # Configuration Management Database (CMDB)
client.api.v2.monitor.*    # Monitor endpoints (real-time data)
client.api.v2.log.*        # Log endpoints (disk, memory, cloud)
client.api.v2.service.*    # Service endpoints (sniffer, security rating)
```

### Common Endpoints

```python
# Firewall
client.api.v2.cmdb.firewall.policy.*
client.api.v2.cmdb.firewall.address.*
client.api.v2.cmdb.firewall.addrgrp.*
client.api.v2.cmdb.firewall.service.custom.*

# System
client.api.v2.cmdb.system.interface.*
client.api.v2.cmdb.system.global_.*
client.api.v2.monitor.system.status.*
client.api.v2.monitor.system.interface.*

# VPN
client.api.v2.cmdb.vpn.ipsec.phase1_interface.*
client.api.v2.cmdb.vpn.ipsec.phase2_interface.*
client.api.v2.monitor.vpn.ipsec.*

# Router
client.api.v2.cmdb.router.static.*
client.api.v2.monitor.router.ipv4.*
```

## 🎯 API Coverage

**FortiOS 7.6.5 - Schema v1.7.0:**

| Category  | Endpoints | Description                          |
| --------- | --------: | ------------------------------------ |
| CMDB      |       561 | Configuration management             |
| Monitor   |       490 | Real-time monitoring data            |
| Log       |       286 | Log queries and management           |
| Service   |        11 | System services (sniffer, etc.)      |
| **Total** | **1,348** | **Complete API coverage**            |

## 📖 Documentation

### Getting Started

- [Quick Start Guide](./docs/getting-started/quickstart.md) - Installation and basic usage
- [Authentication](./docs/getting-started/authentication.md) - API token setup
- [Async Guide](./docs/fortios/user-guide/async-usage.md) - Async/await patterns

### User Guides

- [Client Overview](./docs/fortios/user-guide/client.rst) - FortiOSClient features
- [Endpoint Methods](./docs/fortios/user-guide/endpoint-methods.md) - Using `.get()`, `.post()`, `.put()`, `.delete()`
- [Response Objects](./docs/fortios/user-guide/response-objects.md) - Working with API responses
- [Error Handling](./docs/fortios/user-guide/error-handling.md) - Exception handling

### Advanced Topics

- [Transactions](./docs/fortios/guides/transactions.rst) - Multi-step operations
- [Filtering & Queries](./docs/fortios/guides/filtering.md) - Advanced filtering
- [Rate Limiting](./docs/fortios/guides/rate-limiting.md) - Request throttling
- [Validation](./docs/fortios/guides/validation.md) - Input validation
- [Debugging](./docs/fortios/guides/debugging.md) - Troubleshooting

### API Reference

- [Firewall Policies](./docs/fortios/guides/firewall-policies.md) - Policy management
- [Services](./docs/fortios/guides/services.md) - Service objects
- [Schedules](./docs/fortios/guides/schedules.md) - Schedule objects
- [Traffic Shapers](./docs/fortios/guides/shapers.md) - QoS configuration

## ✨ Advanced Features

### Transaction Support

```python
with client.transaction():
    # All operations in atomic transaction
    client.api.v2.cmdb.firewall.address.post(name="addr1", subnet="10.0.0.1/32")
    client.api.v2.cmdb.firewall.address.post(name="addr2", subnet="10.0.0.2/32")
    # Automatically committed on success, rolled back on error
```

### Error Handling

```python
from hfortix_core.exceptions import (
    ResourceNotFoundError,
    DuplicateEntryError,
    PermissionDeniedError
)

try:
    policy = client.api.v2.cmdb.firewall.policy.get(policyid=100)
except ResourceNotFoundError:
    print("Policy not found")
except PermissionDeniedError:
    print("Insufficient permissions")
```

### Filtering & Querying

```python
# Filter by multiple conditions
addresses = client.api.v2.cmdb.firewall.address.get(
    filter="subnet==192.168.1.0/24|name==@prod"
)

# Select specific fields
policies = client.api.v2.cmdb.firewall.policy.get(
    select="policyid,name,action"
)
```

## 📋 Requirements

- Python 3.10 or higher
- FortiOS 7.0+ (tested with 7.6.5)
- Network access to FortiGate device

### Dependencies

- `hfortix-core` - Core HTTP client (installed automatically)
- `httpx` >= 0.24.0
- `pydantic` >= 2.0.0

## 🔗 Related Packages

- [hfortix-core](https://github.com/hermanwjacobsen/hfortix-core) - Core HTTP client
- [hfortix](https://github.com/hermanwjacobsen/hfortix) - Meta-package for easy installation

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 💬 Support

- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix-fortios/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix-fortios/discussions)
- 📧 Email: herman@wjacobsen.fo

---

**Author**: Herman W. Jacobsen | [LinkedIn](https://www.linkedin.com/in/hermanwjacobsen/) | [GitHub](https://github.com/hermanwjacobsen)
