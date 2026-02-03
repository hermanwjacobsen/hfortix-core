# HFortix FortiOS Documentation

Complete Python SDK for FortiOS/FortiGate with 100% API coverage (1,348 endpoints).

> **Version 0.5.154** - Production-ready FortiOS client with comprehensive type safety and async support.

## Package Overview

`hfortix-fortios` provides comprehensive FortiOS 7.6.5 REST API support:

- **100% API Coverage**: 1,348 endpoints (561 CMDB, 490 Monitor, 286 Log, 11 Service)
- **2,129 Implementation Files**: Complete endpoint files with type stubs
- **Type-Safe**: Full type hints and IDE autocomplete support
- **Async Support**: All endpoints work in both sync and async modes
- **Production-Ready**: Retry logic, circuit breaker, validation, error handling

## Quick Start

```python
from hfortix_fortios import FortiOS

# Connect to FortiGate
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    verify=False
)

# Create firewall address
fgt.api.cmdb.firewall.address.post(
    name="web-server",
    subnet="192.168.1.100/32"
)

# Create firewall policy
fgt.api.cmdb.firewall.policy.post(
    name="Allow-Web-Traffic",
    srcintf=[{"name": "internal"}],
    dstintf=[{"name": "wan1"}],
    srcaddr=[{"name": "all"}],
    dstaddr=[{"name": "all"}],
    service=[{"name": "HTTP"}],
    action="accept",
    schedule="always"
)

# Monitor endpoints
status = fgt.api.monitor.system.status.get()

# Log queries
logs = fgt.api.log.disk.traffic.forward.get(rows=100)
```

## Documentation

### User Guides

| Document | Description |
|----------|-------------|
| [ASYNC_GUIDE.md](ASYNC_GUIDE.md) | Async/await support for concurrent operations |
| [FILTERING_GUIDE.md](FILTERING_GUIDE.md) | Complete guide to filtering API queries |
| [ERROR_HANDLING_CONFIG.md](ERROR_HANDLING_CONFIG.md) | Configurable error handling options |
| [IDE_QUICKSTART.md](IDE_QUICKSTART.md) | IDE features, types, and autocomplete |

### Reference

| Document | Description |
|----------|-------------|
| [API_COVERAGE.md](API_COVERAGE.md) | Detailed API implementation status |
| [ENDPOINT_METHODS.md](ENDPOINT_METHODS.md) | Method reference for all 1,348 endpoints |
| [VALIDATION_GUIDE.md](VALIDATION_GUIDE.md) | Using the validation framework |

### Enterprise Features

| Document | Description |
|----------|-------------|
| [AUDIT_LOGGING.md](AUDIT_LOGGING.md) | Compliance auditing (SOC 2, HIPAA, PCI-DSS) |
| [OBSERVABILITY.md](OBSERVABILITY.md) | Structured logging and distributed tracing |
| [RATE_LIMITING.md](RATE_LIMITING.md) | Rate limiting and resilience patterns |
| [DEBUGGING.md](DEBUGGING.md) | Debug mode and troubleshooting |
| [HANDLER_PROTOCOL_SYSTEM.md](HANDLER_PROTOCOL_SYSTEM.md) | Custom handlers and extensibility |

## API Coverage

**FortiOS 7.6.5 (Schema v1.7.0):**

| Category | Endpoints | Description |
|----------|-----------|-------------|
| **CMDB** | 561 | Configuration management |
| **Monitor** | 490 | Real-time monitoring |
| **Log** | 286 | Log queries |
| **Service** | 11 | Service operations |
| **Total** | **1,348** | 100% coverage |

## Common Use Cases

### Firewall Management

```python
# Create address
fgt.api.cmdb.firewall.address.post(
    name="web-server",
    subnet="192.168.1.100/32",
    comment="Production web server"
)

# List all policies
policies = fgt.api.cmdb.firewall.policy.get()

# Get specific policy by ID
policy = fgt.api.cmdb.firewall.policy.get(policyid=1)

# Update policy
fgt.api.cmdb.firewall.policy.put(
    policyid=1,
    status="disable"
)

# Delete policy
fgt.api.cmdb.firewall.policy.delete(policyid=1)
```

### Monitoring

```python
# Get system status
status = fgt.api.monitor.system.status.get()

# Monitor firewall sessions
sessions = fgt.api.monitor.firewall.session.get()

# Get interface statistics
interfaces = fgt.api.monitor.system.interface.get()
```

### Log Queries

```python
# Query traffic logs from disk
logs = fgt.api.log.disk.traffic.forward.get(
    rows=100,
    filter="srcip==192.168.1.100"
)

# Query event logs
events = fgt.api.log.disk.event.system.get(rows=50)
```

### Async Operations

```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    async with FortiOS(
        host="192.168.1.99",
        token="your-token",
        mode="async"
    ) as fgt:
        # All operations support await
        addresses = await fgt.api.cmdb.firewall.address.get()
        
        # Concurrent operations
        results = await asyncio.gather(
            fgt.api.monitor.system.status.get(),
            fgt.api.cmdb.firewall.policy.get(),
            fgt.api.cmdb.firewall.address.get()
        )

asyncio.run(main())
```

## Installation

```bash
# Install FortiOS package (includes core)
pip install hfortix-fortios

# Or install via meta-package
pip install hfortix[fortios]  # FortiOS only
pip install hfortix[all]      # All products
```

## Related Documentation

- [Quick Start Guide](../../QUICKSTART.md) - Get started in 5 minutes
- [Package README](../../packages/fortios/README.md) - FortiOS package details
- [Core Documentation](../core/README.md) - Core package (exceptions, formatting)
- [Testing Guide](TESTING.md) - Comprehensive test suite documentation (200+ tests)
