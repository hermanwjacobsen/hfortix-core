# HFortix-Core

[![PyPI version](https://badge.fury.io/py/hfortix-core.svg)](https://pypi.org/project/hfortix-core/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Documentation Status](https://readthedocs.org/projects/hfortix-core/badge/?version=latest)](https://hfortix-core.readthedocs.io/en/latest/)
[![License](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

**HFortix-Core** is the shared foundation for the HFortix ecosystem: HTTP
client infrastructure (REST, JSON-RPC, and FortiCloud OAuth2), a complete
exception hierarchy, retry/circuit-breaker/rate-limit resilience, audit and
structured logging, caching, and formatting utilities.

## 🚀 Quick Start

```bash
pip install hfortix-core
```

> **Note:** This is a foundational library. Most users should install
> [`hfortix-fortios`](https://pypi.org/project/hfortix-fortios/) (FortiGate),
> [`hfortix-fortimanager`](https://pypi.org/project/hfortix-fortimanager/),
> [`hfortix-forticare`](https://pypi.org/project/hfortix-forticare/),
> [`hfortix-fortiztp`](https://pypi.org/project/hfortix-fortiztp/), or the
> [`hfortix`](https://pypi.org/project/hfortix/) meta-package instead.

Direct usage — FortiOS REST client:

```python
from hfortix_core.http import HTTPClient
from hfortix_core import APIError, RetryableError

client = HTTPClient(
    url="https://192.168.1.99",
    token="your-api-token",
    verify=True,
    max_retries=3,
)

try:
    # The client prepends /api/v2/<api_type>/ — pass only the endpoint path
    response = client.get("cmdb", "firewall/policy")
except RetryableError as e:
    print(f"Transient failure after retries: {e.message}")
except APIError as e:
    print(f"API error: {e.message} (HTTP {e.http_status})")
finally:
    client.close()
```

FortiManager / FortiAnalyzer JSON-RPC client:

```python
from hfortix_core import HTTPClientJSONRPC

fmg = HTTPClientJSONRPC(
    url="https://fmg.example.com",
    username="admin",
    password="password",
)
fmg.login()
result = fmg.execute("get", [{"url": "/dvmdb/adom/root/device"}])
fmg.logout()
```

FortiCloud (FortiCare / FortiZTP) OAuth2 session:

```python
from hfortix_core.session import CloudSession

with CloudSession(api_id="your-api-id", password="your-password") as session:
    token = session.get_token("assetmanagement")  # per-service OAuth2 token
```

## 📦 What's Included

### HTTP Client Framework (`hfortix_core.http`)

All clients subclass `BaseHTTPClient` and share retry logic, opt-in
circuit breaker and rate limiting, connection pooling (HTTP/2 via httpx),
audit/debug hooks, and request statistics:

- `HTTPClient` / `AsyncHTTPClient` — FortiOS REST (used by `hfortix-fortios`)
- `HTTPClientJSONRPC` — FortiManager/FortiAnalyzer JSON-RPC
  (`HTTPClientFMG` remains as a backwards-compatibility alias)
- `CloudHTTPClient` — FortiCloud REST with OAuth2 bearer tokens
  (used by `hfortix-forticare` and `hfortix-fortiztp`)
- `FortiCloudAuth` / `get_oauth_token` — FortiCloud OAuth2 token acquisition
- `IHTTPClient` — protocol interface for injecting custom clients

### Resilience (opt-in)

Both features are **disabled by default** and enabled via constructor
keywords on any client:

```python
client = HTTPClient(
    url="https://192.168.1.99",
    token="...",
    rate_limit=True,                 # client-side throttling
    rate_limit_max_requests=100,
    rate_limit_window_seconds=60.0,
    rate_limit_strategy="queue",     # "queue" | "drop" | "raise"
    circuit_breaker=True,            # fail fast when the device is down
    circuit_breaker_threshold=5,
    circuit_breaker_timeout=60.0,
)
```

`RateLimitStats` additionally provides enforcement-free tracking of call and
error rates across 1-minute/5-minute/1-hour windows.

### Exception Hierarchy (`hfortix_core.exceptions`)

One hierarchy for every HFortix package, rooted at `FortinetError`, with an
explicit retry split under `APIError`:

- `RetryableError` — `RateLimitError` (429), `ServerError` (500),
  `ServiceUnavailableError` (503), `TimeoutError`, `CircuitBreakerOpenError`
- `NonRetryableError` — `BadRequestError` (400), `ResourceNotFoundError`
  (404), `MethodNotAllowedError` (405), `DuplicateEntryError`,
  `EntryInUseError`, `InvalidValueError`, `PermissionDeniedError`
- `AuthenticationError` / `AuthorizationError` inherit directly from
  `FortinetError` (not `APIError`) — catch them explicitly
- Every exception exposes `.message` (original message) plus rich context
  (`http_status`, `error_code`, `endpoint`, `hint`, ...) on `APIError`
- Helpers: `raise_for_status()` (maps ~300 FortiOS error codes),
  `is_retryable_error()`, `get_retry_delay()`, `get_error_description()`

### Session Management (`hfortix_core.session`)

- `CloudSession` — multi-service OAuth2 token management with per-`client_id`
  token sharing, optional background refresh, pluggable token storage
  backends, and lifecycle hooks

### Utilities

- `TTLCache` — simple in-memory TTL cache for readonly reference data
- `fmt` — output formatting helpers (`to_table`, `to_json`, `to_yaml`,
  `to_csv`, `to_markdown_table`, `to_xml`, and more)
- Audit logging (`hfortix_core.audit`) — Syslog/File/Stream/Composite
  handlers with JSON/CEF/Syslog formatters for compliance logging
- Structured logging (`hfortix_core.logging`) and debug tooling
  (`hfortix_core.debug`)
- TypedDict definitions (`hfortix_core.types`) — PEP 561 typed distribution

## 🔗 Related Packages

- **[hfortix-fortios](https://pypi.org/project/hfortix-fortios/)** - FortiOS/FortiGate API client
- **[hfortix-fortimanager](https://pypi.org/project/hfortix-fortimanager/)** - FortiManager JSON-RPC client
- **[hfortix-fortianalyzer](https://pypi.org/project/hfortix-fortianalyzer/)** - FortiAnalyzer JSON-RPC client
- **[hfortix-forticare](https://pypi.org/project/hfortix-forticare/)** - FortiCare asset management client
- **[hfortix-fortiztp](https://pypi.org/project/hfortix-fortiztp/)** - FortiZTP provisioning client
- **[hfortix](https://pypi.org/project/hfortix/)** - Meta-package installing the common HFortix packages

## 📚 Documentation

- **[Full Documentation](https://hfortix-core.readthedocs.io/)**
- **[Examples](EXAMPLES.md)**
- **[GitHub Repository](https://github.com/hermanwjacobsen/hfortix-core)**

## 🤝 Contributing

This is a proprietary library. For support or feature requests, please contact the maintainer.

## 📄 License

Proprietary License - See LICENSE file for details.

---

**Part of the HFortix ecosystem** - Modern Python SDKs for Fortinet automation
