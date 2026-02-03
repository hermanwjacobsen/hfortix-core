# HFortix Core

[![PyPI version](https://badge.fury.io/py/hfortix-core.svg)](https://pypi.org/project/hfortix-core/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Core HTTP client and shared utilities for the HFortix ecosystem**

## 📦 Overview

`hfortix-core` is the foundational package for all HFortix Fortinet automation tools. It provides:

- 🔌 **HTTP Client Framework** - Async and sync HTTP client with retry logic
- ⚠️ **Exception System** - Comprehensive error handling for Fortinet APIs
- 🛠️ **Utilities** - Common functions used across all Fortinet product packages
- 📘 **Type Definitions** - Shared TypedDict and Protocol definitions

## 🚀 Installation

```bash
pip install hfortix-core
```

**Note**: This package is usually installed automatically as a dependency of other HFortix packages like `hfortix-fortios`.

## 📚 Usage

This package is typically not used directly. Instead, it provides the foundation for product-specific packages:

```python
# Instead of using core directly...
# from hfortix_core import HTTPClient

# Use a product package that includes core:
from hfortix_fortios import FortiOSClient
```

## 🏗️ What's Included

### Exception System

Comprehensive error handling with specific exceptions for all Fortinet API error codes:

```python
from hfortix_core.exceptions import (
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError,
    PermissionDeniedError,
    ValidationError
)
```

### HTTP Client

- Sync and async HTTP client implementations
- Automatic retry with exponential backoff
- Connection pooling and HTTP/2 support
- Request/response logging
- Timeout handling

### Utilities

- Data formatting functions
- Response parsing
- Parameter normalization
- Type conversions

## 🔗 Related Packages

This core package is used by:

- [hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios) - FortiOS/FortiGate client
- [hfortix](https://github.com/hermanwjacobsen/hfortix) - Meta-package for easy installation

## 📋 Requirements

- Python 3.10 or higher
- httpx >= 0.24.0
- pydantic >= 2.0.0

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 💬 Support

- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix-fortios/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix-fortios/discussions)
- 📖 [Documentation](https://github.com/hermanwjacobsen/hfortix)

---

**Author**: Herman W. Jacobsen | [LinkedIn](https://www.linkedin.com/in/hermanwjacobsen/) | [GitHub](https://github.com/hermanwjacobsen)
