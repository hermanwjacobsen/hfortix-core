# HFortix-Core Examples

> Examples for using `hfortix-core` directly. Most users interact with core
> through the higher-level packages (`hfortix-fortios`, `hfortix-fortimanager`,
> `hfortix-forticare`, `hfortix-fortiztp`) — see those packages for
> device-level examples.

## Table of Contents

1. [HTTP Clients](#http-clients)
2. [FortiCloud OAuth2 (CloudSession)](#forticloud-oauth2-cloudsession)
3. [Exception Handling](#exception-handling)
4. [Rate Limiting & Circuit Breaker](#rate-limiting--circuit-breaker)
5. [Caching](#caching)
6. [Formatting Utilities (fmt)](#formatting-utilities-fmt)

---

## HTTP Clients

### FortiOS REST client (HTTPClient)

```python
from hfortix_core.http import HTTPClient

client = HTTPClient(
    url="https://192.168.1.99",
    token="your-api-token",
    verify=True,            # verify SSL certificates
    max_retries=3,
    connect_timeout=10.0,
    read_timeout=300.0,
)

# get(api_type, path) — the client builds the URL as
# <url>/api/v2/<api_type>/<path>, so pass only the endpoint path:
policies = client.get("cmdb", "firewall/policy")
status = client.get("monitor", "system/status")

# Writes take a data dict
client.post("cmdb", "firewall/address", data={
    "name": "web-server",
    "subnet": "10.0.1.100/32",
})

client.close()
```

### FortiManager / FortiAnalyzer JSON-RPC client (HTTPClientJSONRPC)

```python
from hfortix_core import HTTPClientJSONRPC

# Session authentication (username/password)
fmg = HTTPClientJSONRPC(
    url="https://fmg.example.com",
    username="admin",
    password="password",
    adom="root",
    verify=True,
)

# execute() handles login automatically; explicit login() also works
result = fmg.execute("get", [{"url": "/dvmdb/adom/root/device"}])
fmg.logout()

# API-key authentication (FMG 7.4.7+ / 7.6.2+) — no login/logout needed
fmg = HTTPClientJSONRPC(
    url="https://fmg.example.com",
    api_key="your-api-key",
)

# HTTPClientFMG is a backwards-compatibility alias for HTTPClientJSONRPC
from hfortix_core import HTTPClientFMG  # same class
```

### FortiCloud REST client (CloudHTTPClient)

```python
from hfortix_core.http import CloudHTTPClient, get_oauth_token

# Obtain an OAuth2 token, then create the client
token = get_oauth_token(
    api_id="your-api-id",
    password="your-password",
    client_id="assetmanagement",  # or "fortiztp", ...
)

client = CloudHTTPClient(
    url="https://support.fortinet.com",
    oauth_token=token,
)

response = client.post("/ES/api/registration/v3/products/list", data={})
client.close()
```

---

## FortiCloud OAuth2 (CloudSession)

`CloudSession` manages OAuth2 tokens for multiple FortiCloud services from a
single set of credentials, caching one token per `client_id`:

```python
from hfortix_core.session import CloudSession

with CloudSession(api_id="your-api-id", password="your-password") as session:
    # Tokens are acquired on demand and refreshed when expired
    am_token = session.get_token("assetmanagement")
    ztp_token = session.get_token("fortiztp")

    # Force-check validity (refreshes if within the expiry buffer)
    session.ensure_token_valid("assetmanagement")

# Recommended: share one session across service clients
from hfortix_forticare import FortiCare   # pip install hfortix-forticare
from hfortix_fortiztp import FortiZTP     # pip install hfortix-fortiztp

with CloudSession(api_id="...", password="...") as session:
    fcc = FortiCare(session=session)
    fztp = FortiZTP(session=session)
```

Optional background refresh:

```python
session = CloudSession(
    api_id="...",
    password="...",
    auto_refresh=True,             # refresh tokens in the background
    refresh_buffer_seconds=300,    # refresh 5 min before expiry
)
```

---

## Exception Handling

All exceptions inherit from `FortinetError`. `APIError` splits into
`RetryableError` and `NonRetryableError`:

```text
FortinetError
├── AuthenticationError / AuthorizationError   (NOT under APIError!)
├── ValidationError, ConfigurationError, VDOMError, ...
└── APIError
    ├── RetryableError      (RateLimitError, ServerError,
    │                        ServiceUnavailableError, TimeoutError,
    │                        CircuitBreakerOpenError)
    └── NonRetryableError   (BadRequestError, ResourceNotFoundError,
                             MethodNotAllowedError, DuplicateEntryError,
                             EntryInUseError, InvalidValueError,
                             PermissionDeniedError)
```

```python
from hfortix_core import (
    APIError,
    AuthenticationError,
    FortinetError,
    NonRetryableError,
    ResourceNotFoundError,
    RetryableError,
)

try:
    result = client.get("cmdb", "firewall/address")
except ResourceNotFoundError as e:
    print(f"Not found: {e.message}")          # original message only
    print(e.suggest_recovery())
except RetryableError as e:
    print(f"Transient error (already retried): {e.message}")
except NonRetryableError as e:
    print(f"Permanent error: {e.message} (code {e.error_code})")
except AuthenticationError as e:
    # IMPORTANT: AuthenticationError/AuthorizationError inherit directly
    # from FortinetError — an `except APIError` block will NOT catch them.
    print(f"Login failed: {e.message}")
except FortinetError as e:
    print(f"Other Fortinet error: {e.message}")
```

`APIError` carries rich context:

```python
except APIError as e:
    e.message       # original message, without added context
    str(e)          # message + endpoint/status/hint context
    e.http_status   # e.g. 404
    e.error_code    # FortiOS internal code, e.g. -5
    e.endpoint      # request path
    e.method        # HTTP method
    e.hint          # suggested fix, when available
    e.request_id    # unique id for correlating logs
```

Helper functions (in `hfortix_core.exceptions`):

```python
from hfortix_core.exceptions import (
    get_error_description,
    get_retry_delay,
    is_retryable_error,
    raise_for_status,
)

# Map a FortiOS/FortiCloud response dict to the right exception
raise_for_status(response, endpoint="firewall/address", method="GET")

# Retry helpers
if is_retryable_error(err):
    delay = get_retry_delay(err, attempt=1, base_delay=1.0, max_delay=60.0)

print(get_error_description(-23))  # "Entry is used"
```

---

## Rate Limiting & Circuit Breaker

Both are **opt-in** (disabled by default) and available on every client
constructor (`HTTPClient`, `AsyncHTTPClient`, `HTTPClientJSONRPC`,
`CloudHTTPClient`, and `CloudSession`):

```python
from hfortix_core.http import HTTPClient

client = HTTPClient(
    url="https://192.168.1.99",
    token="...",
    # Client-side rate limiting (enforcement)
    rate_limit=True,
    rate_limit_max_requests=100,        # per window
    rate_limit_window_seconds=60.0,
    rate_limit_strategy="queue",        # "queue" | "drop" | "raise"
    rate_limit_queue_size=100,
    rate_limit_queue_timeout=30.0,
    rate_limit_queue_overflow="block",  # "block" | "drop" | "raise"
    # Circuit breaker (fail fast when the device is down)
    circuit_breaker=True,
    circuit_breaker_threshold=5,        # failures before opening
    circuit_breaker_timeout=60.0,       # seconds before half-open probe
)

print(client.get_rate_limit_status())
print(client.get_circuit_breaker_state())  # {"state": "disabled"} when off
```

When limits are hit, the strategy determines behavior: `"queue"` waits for
the next window (possibly raising `RateLimitQueueFullError` /
`RateLimitQueueTimeoutError`), `"drop"` discards the request, and `"raise"`
raises `RateLimitExceededError` immediately. An open circuit breaker raises
`CircuitBreakerOpenError`.

---

## Caching

`TTLCache` is a simple in-memory time-to-live cache for readonly reference
data. It is **not** thread-safe.

```python
from hfortix_core import TTLCache

cache = TTLCache[dict](default_ttl=3600)  # entries live 1 hour

cache.set("geography/countries", {"US": "United States"})
cache.set("short-lived", {"x": 1}, ttl=5)   # per-entry TTL override

data = cache.get("geography/countries")     # None if missing/expired
"geography/countries" in cache              # membership honors expiry

cache.invalidate("geography/countries")     # drop one key
removed = cache.cleanup()                   # purge expired entries
cache.clear()                               # drop everything

# A shared 24h-TTL instance for reference data:
from hfortix_core import readonly_cache
```

---

## Formatting Utilities (fmt)

`hfortix_core.fmt` converts API results into human-friendly formats:

```python
from hfortix_core import fmt

rows = [
    {"name": "web-server", "subnet": "10.0.1.100/32"},
    {"name": "db-server", "subnet": "10.0.1.200/32"},
]

print(fmt.to_table(rows))            # aligned text table
print(fmt.to_markdown_table(rows))   # GitHub-flavored markdown
print(fmt.to_json(rows, indent=2))   # pretty JSON string
print(fmt.to_yaml(rows))             # YAML string
print(fmt.to_csv(["a", "b", "c"]))   # "a, b, c"
```

Other helpers: `to_dict`, `to_list`, `to_dictlist`, `to_listdict`,
`to_key_value`, `to_multiline`, `to_quoted`, `to_xml`.

---

## More

- Full API documentation: <https://hfortix-core.readthedocs.io/>
- Higher-level packages: `hfortix-fortios`, `hfortix-fortimanager`,
  `hfortix-fortianalyzer`, `hfortix-forticare`, `hfortix-fortiztp`
