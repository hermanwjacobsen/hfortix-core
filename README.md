# HFortix-Core

[![PyPI version](https://badge.fury.io/py/hfortix-core.svg)](https://pypi.org/project/hfortix-core/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Documentation Status](https://readthedocs.org/projects/hfortix-core/badge/?version=latest)](https://hfortix-core.readthedocs.io/en/latest/)
[![License](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

**HFortix-Core** provides the foundational utilities, protocols, and base classes for the HFortix ecosystem, including HTTP client infrastructure, observability tools, and shared abstractions.

## 🚀 Quick Start

```bash
pip install hfortix-core
```

> **Note:** This is a foundational library. Most users should install `hfortix-fortios` or `hfortix` instead.

```python
from hfortix_core import ObservableHTTPClient, HTTPRequestEvent

# Use the observable HTTP client with event tracking
client = ObservableHTTPClient(base_url="https://api.example.com")

# Subscribe to request events
def log_requests(event: HTTPRequestEvent):
    print(f"{event.method} {event.url} - {event.status_code}")

client.subscribe(log_requests)

# Make requests
response = await client.get("/status")
```

## ✨ Key Features

- **🔌 HTTP Client Infrastructure** - Modern async HTTP client with httpx backend
- **📊 Observability Protocol** - Event-driven architecture for monitoring and debugging
- **🏗️ Base Abstractions** - Shared protocols and interfaces for Fortinet API clients
- **⚡ High Performance** - HTTP/2 support, connection pooling, and async/await
- **🛡️ Production Ready** - Comprehensive error handling and validation

## 📦 What's Included

### HTTP Client Infrastructure
- `ObservableHTTPClient` - Event-driven HTTP client with observability hooks
- Connection pooling and HTTP/2 support via httpx
- Automatic retry logic and error handling
- Session management and authentication helpers

### Observability Protocol
- Event-based monitoring system
- Request/response tracking
- Performance metrics collection
- Debugging and audit trail support

### Base Abstractions
- Protocol definitions for Fortinet API clients
- Shared type definitions and models
- Common utility functions
- Error handling infrastructure

## 🔗 Related Packages

- **[hfortix-fortios](https://pypi.org/project/hfortix-fortios/)** - FortiOS/FortiGate API client
- **[hfortix](https://pypi.org/project/hfortix/)** - Meta-package installing all HFortix packages

## 📚 Documentation

- **[Full Documentation](https://hfortix-core.readthedocs.io/)**
- **[API Reference](https://hfortix-core.readthedocs.io/en/latest/api/)**
- **[GitHub Repository](https://github.com/hermanwjacobsen/hfortix-core)**

## 🤝 Contributing

This is a proprietary library. For support or feature requests, please contact the maintainer.

## 📄 License

Proprietary License - See LICENSE file for details.

---

**Part of the HFortix ecosystem** - Modern Python SDKs for Fortinet automation
