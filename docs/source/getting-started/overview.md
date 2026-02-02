# HFortix Overview

Modern Python SDK for Fortinet Products.

## What is HFortix?

HFortix is a comprehensive, fully-typed Python SDK for automating Fortinet security infrastructure. It provides a unified interface to interact with FortiOS, FortiManager, and FortiAnalyzer through their REST APIs.

## Supported Products

### FortiOS/FortiGate (Available Now)

Complete FortiOS 7.6.5 API client with:
- ✅ 100% API coverage (1,348 endpoints: 561 CMDB + 490 Monitor + 286 Log + 11 Service)
- ✅ 2,405+ endpoint files with type stubs for excellent IDE autocomplete
- ✅ Full async support
- ✅ Automatic key normalization (hyphens → underscores)
- ✅ Comprehensive validation and error handling
- ✅ 2,566+ test functions across 318 test files
- ✅ Production-ready with extensive test coverage

**[Get Started with FortiOS →](/fortios/getting-started/quickstart.md)**

### FortiManager (Coming Soon)

Centralized management platform client:
- ⏳ Device management
- ⏳ Policy packages
- ⏳ Configuration templates
- ⏳ Multi-device operations

**[FortiManager Docs →](/fortimanager/index.rst)**

### FortiAnalyzer (Coming Soon)

Analytics and logging platform client:
- ⏳ Log queries and analysis
- ⏳ Report generation
- ⏳ Event correlation
- ⏳ Compliance reporting

**[FortiAnalyzer Docs →](/fortianalyzer/index.rst)**

## Architecture

HFortix uses a modular architecture:

```
hfortix (meta-package)
├── hfortix-core          # Shared HTTP client, exceptions, utilities
├── hfortix-fortios       # FortiOS API client (1,348 endpoints)
├── hfortix-fortimanager  # (coming soon)
└── hfortix-fortianalyzer # (coming soon)
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

### Production Ready

- Circuit breaker pattern
- Automatic retries
- Connection pooling
- Comprehensive error handling
- Validation framework

### Developer Friendly

- Dual-pattern interface (dict or kwargs)
- Convenience wrappers
- Extensive documentation
- Rich examples
- Type safety

### Test Coverage

Comprehensive test suite ensures reliability:
- **2,566+ test functions** across 318 test files
- **251 endpoint test files** covering all 1,348 FortiOS API endpoints
- **40 validator test files** ensuring 75+ utility functions work correctly
- **12 unit test files** validating core HTTP client and response processing
- **3 integration test files** testing client lifecycle and hooks
- Parallel execution for validator tests
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

# Connect
fgt = FortiOS(host="192.168.1.99", token="your-token")

# Create firewall address
fgt.api.cmdb.firewall.address.post(
    name="web-server",
    subnet="10.0.1.100/32"
)

# Create firewall policy - simple list format (auto-converted to dicts)
fgt.api.cmdb.firewall.policy.post(
    name="Allow-Web",
    srcintf=["internal"],      # Converted to [{"name": "internal"}]
    dstintf=["wan1"],          # Converted to [{"name": "wan1"}]
    srcaddr=["all"],           # Converted to [{"name": "all"}]
    dstaddr=["web-server"],    # Converted to [{"name": "web-server"}]
    service=["HTTP", "HTTPS"], # Converted to [{"name": "HTTP"}, {"name": "HTTPS"}]
    action="accept"
)
```

## Community

- **GitHub**: https://github.com/hermanwjacobsen/hfortix
- **Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **PyPI**: https://pypi.org/project/hfortix/

## License

Proprietary. See [License](/license.md) for details.
