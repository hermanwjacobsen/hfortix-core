# HFortix Overview

Modern Python SDK for Fortinet Products.

## What is HFortix?

HFortix is a comprehensive, fully-typed Python SDK for automating Fortinet security infrastructure. Currently focused on FortiOS/FortiGate, with plans to expand to FortiManager and FortiAnalyzer.

## Supported Products

### FortiOS/FortiGate (Available Now)

Complete FortiOS 7.6.5 API client with:
- ✅ 100% API coverage (1,348 endpoints: 561 CMDB + 490 Monitor + 286 Log + 11 Service)
- ✅ 2,405+ endpoint files with type stubs for excellent IDE autocomplete
- ✅ Full async support
- ✅ Automatic key normalization (hyphens → underscores)
- ✅ Comprehensive validation and error handling
- ✅ 1,447+ schema validator tests (100% endpoint coverage)
- ✅ Batch transactions with commit/rollback (v0.5.152+)
- ✅ API request inspection for debugging and auditing (v0.5.152+)
- ✅ Beta status until v1.0.0, production-ready and stable

**[Get Started with FortiOS →](/fortios/getting-started/quickstart.md)**

### FortiManager & FortiAnalyzer (Coming Soon)

Additional Fortinet product support is planned for future releases.

## Architecture

HFortix uses a modular architecture:

```
hfortix (meta-package)
├── hfortix-core          # Shared HTTP client, exceptions, utilities
└── hfortix-fortios       # FortiOS API client (1,348 endpoints)
```

## Key Features

### Fully Typed

Complete type hints for excellent IDE support:

```python
from hfortix_fortios import FortiOS

fgt: FortiOS = FortiOS(host="192.168.1.99", token="...")
addresses: list[dict] = fgt.api.cmdb.firewall.address.get()
```

### Async Support

All endpoints support async/await:

```python
async def get_status():
    status = await fgt.api.monitor.system.status.get_async()
    return status
```

### Production Ready (Beta until v1.0.0)

- Circuit breaker pattern
- Automatic retries
- Connection pooling
- Comprehensive error handling
- Validation framework
- Batch transactions (v0.5.152+)
- API request inspection (v0.5.152+)

### Developer Friendly

- Dual-pattern interface (dict or kwargs)
- Convenience wrappers
- Extensive documentation
- Rich examples
- Type safety

### Test Coverage

Comprehensive test suite ensures reliability:
- **1,447 schema validator tests** - 100% coverage of all 1,348 endpoints (offline, fast execution)
- **80+ live integration tests** - Real API testing with FortiGate/FortiManager
- **40 validator test files** - ensuring 75+ utility functions work correctly
- **Unit tests** - HTTP client, response processing, error handling
- **Integration tests** - Client lifecycle, hooks system, statistics tracking
- Parallel execution for validator tests (no API calls)
- Sequential execution for endpoint tests (respects API rate limits)

## Installation

```bash
# Install everything
pip install hfortix

# Or install specific packages
pip install hfortix-fortios
```

**[Detailed Installation Guide →](/getting-started/installation.md)**

## Quick Example

```python
from hfortix_fortios import FortiOS

# Connect with context manager (automatic cleanup)
with FortiOS(host="192.168.1.99", token="your-token") as fgt:
    # Create firewall address
    fgt.api.cmdb.firewall.address.post(
        name="web-server",
        subnet="10.0.1.100/32"
    )

    # Create firewall policy - simple list format (auto-converted)
    fgt.api.cmdb.firewall.policy.post(
        name="Allow-Web",
        srcintf=["internal"],      # Converted to [{"name": "internal"}]
        dstintf=["wan1"],          # Converted to [{"name": "wan1"}]
        srcaddr=["all"],           # Converted to [{"name": "all"}]
        dstaddr=["web-server"],    # Converted to [{"name": "web-server"}]
        service=["HTTP", "HTTPS"], # Converted to [{"name": "..."}]
        action="accept"
    )
```

## Community

- **GitHub**: https://github.com/hermanwjacobsen/hfortix
- **Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **PyPI**: https://pypi.org/project/hfortix/

## License

Proprietary. See [License](/license.md) for details.
