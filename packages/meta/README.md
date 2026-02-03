# HFortix - Fortinet Python SDK

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Meta-package for the HFortix ecosystem** - Convenient installation for Fortinet automation in Python.

## 📦 Package Structure

This is a **meta-package** that provides convenient installation patterns. The actual functionality is in these packages:

| Package           | Repository                                                                 | Description                              |
| ----------------- | -------------------------------------------------------------------------- | ---------------------------------------- |
| **hfortix-core**  | [hfortix-core](https://github.com/hermanwjacobsen/hfortix-core)           | Core HTTP client and shared utilities    |
| **hfortix-fortios** | [hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios) | FortiOS/FortiGate API client (8,000+ endpoints) |

## 🚀 Installation Options

### Everything (Recommended)

```bash
pip install hfortix[all]
```

Installs all current and future Fortinet product packages.

### FortiOS/FortiGate Only

```bash
pip install hfortix[fortios]
```

Installs `hfortix-core` + `hfortix-fortios`.

### Core Only

```bash
pip install hfortix
```

Installs only `hfortix-core` - the shared foundation.

### Individual Packages

```bash
# Install specific packages directly
pip install hfortix-fortios  # Automatically includes hfortix-core
pip install hfortix-core     # Just the core utilities
```

## 💡 Quick Start

```python
from hfortix_fortios import FortiOSClient

# Connect to FortiGate
client = FortiOSClient(
    host="192.168.1.99",
    token="your-api-token"
)

# Get firewall policies
policies = client.api.v2.cmdb.firewall.policy.get()

for policy in policies:
    print(f"Policy {policy.policyid}: {policy.name}")
```

## 📚 Documentation

| Package           | Documentation Link                                                   |
| ----------------- | -------------------------------------------------------------------- |
| **hfortix-fortios** | [FortiOS Documentation](https://github.com/hermanwjacobsen/hfortix-fortios) |
| **hfortix-core**  | [Core API Reference](https://github.com/hermanwjacobsen/hfortix-core) |

## ✨ Features

### Comprehensive Coverage

- 8,000+ FortiOS API endpoints
- Full type hints and IDE autocomplete
- Auto-generated from official FortiOS schemas

### Developer Experience

- Pythonic API design
- Extensive inline documentation
- Type-safe request/response models

### Production Ready

- Transaction support
- Error handling and retries
- Async/await support
- Rate limiting

## 📋 Requirements

- Python 3.10 or higher
- FortiOS 7.0+ (for FortiGate devices)

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Related Projects

- [hfortix-core](https://github.com/hermanwjacobsen/hfortix-core) - Core HTTP client
- [hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios) - FortiOS automation

## 💬 Support

- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix-fortios/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix-fortios/discussions)

---

**Author**: Herman W. Jacobsen | [LinkedIn](https://www.linkedin.com/in/hermanwjacobsen/) | [GitHub](https://github.com/hermanwjacobsen)
