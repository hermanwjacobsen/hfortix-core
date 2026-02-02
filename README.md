# HFortix - Fortinet Python SDK

**Fully-typed Python SDK for Fortinet FortiOS, FortiManager, and FortiAnalyzer**

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

## Quick Start

```bash
pip install hfortix-fortios
```

```python
from hfortix_fortios import FortiOS

# Connect to FortiGate
fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# Get system status (Monitor endpoint - use dict access for untyped fields)
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}, Model: {status['model']}")

# Create firewall address
fgt.api.cmdb.firewall.address.post(
    name="webserver",
    subnet="10.0.1.100 255.255.255.255",
    comment="Production web server"
)

# Query with filters
addresses = fgt.api.cmdb.firewall.address.get(
    filter="subnet==10.0.0.0/8"
)

# Close connection
fgt.close()
```

## Features

### ✅ Complete API Coverage
- **1,348 FortiOS 7.6.5 endpoints** - All CMDB, Monitor, Log, and Service endpoints
- **FortiManager JSON-RPC proxy** - Manage multiple devices through FortiManager
- **FortiAnalyzer** (coming soon)

### ✅ Type Safety & IDE Support
- **100% type coverage for CMDB endpoints** - Full autocomplete and validation
- **Partial coverage for Monitor/Log endpoints** - Some response fields documented
- **`.pyi` stub files** for excellent IDE integration
- **Pydantic validation** for request payloads

### ✅ Flexible Response Access
```python
# FortiObject - Multiple access methods
addr = fgt.api.cmdb.firewall.address.get(name="server1")

# Attribute access (recommended)
print(addr.subnet)  # Full autocomplete ✅

# Dictionary access
print(addr['subnet'])  # Also works

# Convert to dict/JSON
print(addr.dict)      # Dictionary representation
print(addr.json)      # Pretty-printed JSON string
print(addr.raw)       # Full API envelope with metadata

# Query by mkey returns SINGLE object (not list)
addr = fgt.api.cmdb.firewall.address.get(name="server1")
print(addr.subnet)  # Direct access, no need for addr[0]

# Nested objects fully supported
group = fgt.api.cmdb.firewall.service.group.get(name="MyGroup")
for member in group.member:
    print(member.name)  # FortiObjects all the way down
```

> **Note**: Monitor and Log endpoints have incomplete response field types due to FortiOS API schema limitations. Attribute access (e.g., `status.hostname`) works at runtime but may show type errors in your IDE. Use dictionary access (`status['hostname']`) to avoid IDE warnings, or use `.json`/`.raw` to inspect the full response. Field names match FNDN documentation with hyphens (`-`) converted to underscores (`_`).

### ✅ Modern Python Features
- **Async/await support** for concurrent operations
- **Synchronous API** for simple scripts
- **Context managers** for automatic cleanup
- **Type hints** throughout
- **Python 3.10+** with modern syntax

### ✅ Production Ready
- **Comprehensive error handling** with detailed exceptions
- **Audit logging** with pluggable handlers (Kafka, webhooks, databases)
- **Rate limiting** and exponential backoff retry
- **Circuit breaker** pattern for resilience
- **Request/response debugging** tools

### ✅ Developer Experience
- **No string manipulation** - everything is a method call
- **IDE autocomplete** for all endpoints and parameters
- **Built-in validation** catches errors before API calls
- **Extensive documentation** with examples
- **Custom wrappers** - easily create your own convenience methods  

## Current Status

> **⚠️ BETA STATUS**  
> Version 0.5.151 is production-ready but remains in beta until v1.0.0. Breaking changes are possible before v1.0.0, however after v0.5.150 breaking changes are not expected at this time (if any). The SDK is stable and suitable for production use with comprehensive test coverage.
> 
> **Recommended**: Stay on version 0.5.150+ for maximum stability.

**Version**: 0.5.151 (Released: February 2, 2026)  
**FortiOS Coverage**: 7.6.5 (1,348 endpoints)  
**Package Size**: ~30 MB (with type stubs)  
**Status**: Production Ready ✅

### Test Coverage Summary

**Comprehensive test suite** with 2,566+ test functions across 67 test files:

| Category | Test Files | Test Functions | Coverage |
|----------|-----------|----------------|----------|
| **Live Endpoint Tests** | 251 | ~1,800+ | CMDB (180), Monitor (63), Log (4), Service (4) |
| **Validators & Helpers** | 40 | ~650+ | 75+ utility functions tested |
| **Unit Tests** | 12 | ~100+ | Core HTTP, response processing, utils |
| **Integration Tests** | 3 | ~15+ | Client lifecycle, hooks, stats |
| **Total** | **318** | **2,566+** | **Extensive coverage across all layers** |

**Test Categories:**
- ✅ **Endpoint Tests**: 251 files testing real API endpoints (CMDB, Monitor, Log, Service)
- ✅ **Validator Tests**: 40 files covering 75+ validation functions (network, firewall, schedules, SSH/SSL)
- ✅ **Unit Tests**: Core HTTP client, response processing, error handling, formatting
- ✅ **Integration Tests**: FortiOS client lifecycle, hooks system, statistics tracking
- ✅ **Edge Cases**: Special scenarios, list handling, parameter normalization

**Key Testing Features:**
- 🔬 Parallel execution support for validator tests (no API calls)
- 🎯 Sequential execution for endpoint tests (respects API rate limits)
- 📊 Comprehensive coverage of all 1,348+ FortiOS API endpoints
- 🛡️ Validation testing for 75+ helper functions and validators
- 🔄 Integration testing for async/sync clients and proxy functionality

## Documentation

📚 **Full documentation**: https://hfortix.readthedocs.io/

- [Quick Start Guide](https://hfortix.readthedocs.io/en/latest/fortios/getting-started/quickstart.html) / [QUICKSTART.md](QUICKSTART.md)
- [API Reference](https://hfortix.readthedocs.io/en/latest/fortios/api-documentation/)
- [FortiManager Proxy](https://hfortix.readthedocs.io/en/latest/fortios/guides/fmg-proxy.html)
- [Custom Wrappers Guide](https://hfortix.readthedocs.io/en/latest/fortios/guides/custom-wrappers.html)
- [Error Handling](https://hfortix.readthedocs.io/en/latest/fortios/guides/error-handling.html)
- [Filtering & Queries](https://hfortix.readthedocs.io/en/latest/fortios/guides/filtering.html)
- [Async Guide](docs/fortios/ASYNC_GUIDE.md)
- [Performance Testing](docs/fortios/PERFORMANCE_TESTING.md)
- [Test Coverage](TESTING.md) - Detailed test suite documentation
- [Security Best Practices](docs/SECURITY.md)
- [Changelog](CHANGELOG.md)

## Installation

### Standard Installation
```bash
pip install hfortix-fortios
# or
pip install hfortix[fortios]  # Meta-package
```

### Alternative Packages
```bash
pip install hfortix           # Core only (minimal)
pip install hfortix[all]      # Everything
```

### Minimal Installation (No Stubs)
```bash
pip install hfortix-fortios[minimal]
# Smaller package, basic type hints only
```

## Examples

### Authentication Options

```python
from hfortix_fortios import FortiOS

# Option 1: API Token (recommended)
fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# Option 2: Username/Password (session-based)
fgt = FortiOS(host="192.168.1.99", username="admin", password="password")

# Option 3: Environment Variables
# Set: FORTIOS_HOST, FORTIOS_TOKEN (or FORTIOS_USERNAME, FORTIOS_PASSWORD)
fgt = FortiOS()  # Automatically loads from environment

# Close connection when done
fgt.close()
```

### Basic Operations

```python
from hfortix_fortios import FortiOS

# Connect to FortiGate
fgt = FortiOS(host="192.168.1.99", token="your-api-token")

# Create
fgt.api.cmdb.firewall.address.post(
    name="server1",
    subnet="10.0.1.50 255.255.255.255"
)

# Read
addr = fgt.api.cmdb.firewall.address.get(name="server1")
print(f"Address: {addr.subnet}")

# Update
fgt.api.cmdb.firewall.address.put(
    name="server1",
    comment="Updated comment"
)

# Delete
fgt.api.cmdb.firewall.address.delete(name="server1")

# Close connection
fgt.close()
```

### FortiManager Proxy

```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password"
)

# Login to target device
fmg.login(device="fw-branch-01", adom="production")

# Use same API as FortiOS
addresses = fmg.api.cmdb.firewall.address.get()

# Monitor operations (use dict access for untyped fields)
status = fmg.api.monitor.system.status.get()
print(status['hostname'])

# Logout and close
fmg.logout()
fmg.close()
```

### Error Handling

```python
from hfortix_core.exceptions import (
    APIError,
    ResourceNotFoundError,
    ValidationError
)

try:
    addr = fgt.api.cmdb.firewall.address.get(name="notfound")
except ResourceNotFoundError as e:
    print(f"Address not found: {e}")
except APIError as e:
    print(f"HTTP {e.http_status}: {e.message}")
```

### Advanced Features

```python
# Pydantic model validation
from hfortix_fortios.api.models.cmdb.firewall.address import AddressModel

addr_model = AddressModel(
    name="server1",
    subnet="10.0.1.50 255.255.255.255",
    comment="Validated address"
)
fgt.api.cmdb.firewall.address.post(payload_dict=addr_model.to_fortios_dict())

# Action methods
if fgt.api.cmdb.firewall.address.exists(name="server1"):
    print("Address exists!")

# Move policy
fgt.api.cmdb.firewall.policy.move(
    policyid=10,
    action="before",
    reference_policyid=5
)

# Clone object
fgt.api.cmdb.firewall.address.clone(
    name="original",
    new_name="cloned"
)

# Read-only mode (safe testing)
fgt_readonly = FortiOS(host="...", token="...", read_only=True)
# All write operations will raise exceptions

# Track operations (audit logging)
fgt_tracked = FortiOS(host="...", token="...", track_operations=True)
operations = fgt_tracked.get_operations()
```

## API Coverage

| Category | Endpoints | Endpoint Coverage | Response Field Types |
|----------|-----------|-------------------|----------------------|
| **CMDB** (Configuration) | 561 | ✅ 100% | ✅ 100% autocomplete |
| **Monitor** (Status/Stats) | 490 | ✅ 100% | ⚠️ Partial autocomplete |
| **Log** (Query Logs) | 286 | ✅ 100% | ⚠️ Partial autocomplete |
| **Service** (Operations) | 11 | ✅ 100% | ✅ 100% autocomplete |
| **Total** | **1,348** | ✅ **100%** | **886 fully typed** |

> **All 1,348 endpoints are fully implemented and functional.** Response field types indicate IDE autocomplete availability for response fields. CMDB endpoints have complete field documentation, while Monitor/Log have partial coverage due to FortiOS API schema limitations.

## Key Capabilities

### Type Safety
- **100% CMDB type coverage** - Full IDE autocomplete for all configuration endpoints
- **Partial Monitor/Log coverage** - Use dictionary access for undocumented fields
- **Pydantic validation** for request payloads
- **Literal types** for enum parameters
- **`.json` and `.raw`** always available for response inspection

### Advanced Features
- **Capabilities detection** - Query endpoint support at runtime (`SUPPORTS_CREATE`, `SUPPORTS_MOVE`, etc.)
- **Action methods** - `move()`, `clone()`, `exists()` helpers for common operations
- **Schema introspection** - Runtime `get_schema()` for all endpoints
- **Query parameters** - Advanced filtering, sorting, pagination
- **Pydantic models** - 1,065+ models for request validation
- **Read-only mode** - Safe testing with `read_only=True`
- **Operation tracking** - Audit logging with `track_operations=True`
- **Custom HTTP clients** - Implement `IHTTPClient` protocol for custom behavior
- **Performance testing** - Built-in `performance_test()` utility


### Enterprise Ready
- **Comprehensive error handling** with typed exceptions
- **Circuit breaker** pattern for resilience
- **Exponential backoff** retry logic
- **Rate limiting** support
- **Async/await** support for concurrency
- **Context managers** for automatic cleanup
- **Audit logging** with pluggable handlers

## Requirements

- Python 3.10 or higher
- FortiOS 7.x (tested on 7.6.5)
- FortiManager 7.x (for proxy features)

## Support & Development

- **Issues**: [GitHub Issues](https://github.com/hermanwjacobsen/hfortix/issues)
- **Documentation**: [ReadTheDocs](https://hfortix.readthedocs.io/)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)
- **License**: Proprietary (see [LICENSE](LICENSE))

## Latest Release (v0.5.151)

**February 2, 2026**

- ✅ Added comprehensive test coverage documentation (2,566+ tests across 318 files)
- ✅ Added `py.typed` marker to meta package for mypy support
- ✅ Updated documentation with test coverage summary
- ✅ Enhanced beta status messaging with stability guarantees

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

## Project Structure

```
hfortix/
├── packages/
│   ├── core/          # hfortix-core (HTTP client, exceptions)
│   ├── fortios/       # hfortix-fortios (FortiOS/FMG client)
│   └── meta/          # hfortix (meta-package)
```

## Contributing

This is a proprietary project. For feature requests or bug reports, please open an issue on GitHub.

---

**Made with ❤️ for the Fortinet community**
