Overview
========

**HFortix-Core** is the foundational library powering the HFortix ecosystem of Fortinet automation tools.
It provides enterprise-grade HTTP clients, logging, debugging, error handling, and utilities used by
all HFortix packages.

Key Features
------------

**CloudSession - Multi-Service OAuth Management**
   Centralized OAuth token management for multiple FortiCloud services with:
   
   - Automatic token sharing and client_id auto-detection
   - Background token refresh with configurable intervals
   - **Pluggable storage backends** (Redis, PostgreSQL, MySQL, SQLite, File, Memcached)
   - **Lifecycle hooks** for monitoring, metrics, and custom behaviors
   - Distributed token sharing across multiple servers
   - Thread-safe concurrent access
   - Comprehensive logging at DEBUG/INFO/WARNING levels

**Rate Limiting**
   Track API call rates across multiple time windows (last minute, 5 minutes, hour) for both
   calls and errors via ``RateLimitStats``. Optional client-side enforcement
   (``RateLimiter``/``AsyncRateLimiter``) is available on all HTTP clients via the opt-in
   ``rate_limit=True`` constructor keyword.

**HTTP Client Framework**
   Production-ready HTTP clients with retry logic, circuit breakers, connection pooling, and both
   synchronous and asynchronous support for FortiOS and FortiManager APIs.

**Enterprise Audit Logging**
   Comprehensive audit logging for compliance (SOC 2, HIPAA, PCI-DSS) with handlers for Syslog,
   files, streams, and multiple formatters (JSON, CEF, RFC 5424).

**Exception Hierarchy**
   Complete exception hierarchy (20+ exception types) for granular error handling including
   retry-able vs non-retry-able errors, circuit breaker states, and API-specific errors.

**Structured Logging**
   Request logging with structured (JSON) and text formatters, integration with enterprise
   logging systems, and detailed performance metrics.

**Debug Utilities**
   Debug sessions, timing decorators, connection statistics, and request inspection tools for
   troubleshooting and performance analysis.

**Type Safety**
   Comprehensive TypedDict definitions for all API responses, configuration, and internal
   structures enabling full IDE autocomplete and type checking.

Architecture
------------

HFortix-Core is organized into functional modules:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Module
     - Purpose
   * - **Session Management**
     - CloudSession for multi-service OAuth, TokenInfo dataclass
   * - **Rate Limiting**
     - RateLimitStats for tracking API call rates across time windows
   * - **HTTP Clients**
     - Base HTTP client, FortiOS client, FortiManager client, async client, protocol interface
   * - **Audit Logging**
     - Handlers (Syslog, File, Stream, Composite), Formatters (JSON, CEF, Syslog)
   * - **Caching**
     - TTL-based cache for readonly reference data
   * - **Logging**
     - Structured and text formatters, request logger, log protocols
   * - **Debugging**
     - Debug sessions, timing utilities, connection stats, request inspection
   * - **Exceptions**
     - 20+ exception classes in a hierarchy (FortinetError → APIError → specific errors)
   * - **Types**
     - TypedDict definitions for responses, stats, debug info, and configurations
   * - **Utilities**
     - Key normalization, deprecation warnings, formatting helpers

Usage
-----

HFortix-Core is typically used as a dependency by higher-level packages like ``hfortix-fortios``,
``hfortix-forticare``, and ``hfortix-fortiztp``. However, you can use it directly for custom integrations:

**CloudSession - Multi-Service OAuth**

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_forticare import FortiCare
   from hfortix_fortiztp import FortiZTP
   
   # Manage tokens for multiple services
   with CloudSession(api_id="...", password="...") as session:
       fc = FortiCare(session=session)    # Uses "assetmanagement" client_id
       fz = FortiZTP(session=session)     # Uses "fortiztp" client_id
       
       # Both share the session, each with their own token
       products = fc.api.products.list.post()
       devices = fz.devices.get()

**Rate Limit Tracking**

.. code-block:: python

   from hfortix_forticare import FortiCare
   
   # Configure rate limits
   fc = FortiCare(
       api_id="...",
       password="...",
       rate_limit_calls_per_min=100,
       rate_limit_calls_per_hour=1000
   )
   
   # Check status
   status = fc.get_rate_limit_status()
   print(f"Calls: {status['calls_last_hour']}/{status['limits']['calls_per_hour']}")

**Direct HTTP Client Usage**

.. code-block:: python

   from hfortix_core.http import HTTPClient
   
   # Create FortiOS HTTP client
   client = HTTPClient(
       url="https://192.168.1.99",
       token="your-api-token",
       verify=True,
       max_retries=3
   )
   
   # Make API requests — the client prepends /api/v2/<api_type>/
   # itself, so pass only the endpoint path
   response = client.get("cmdb", "firewall/policy")

**Audit Logging**

.. code-block:: python

   from hfortix_core.audit import SyslogHandler, CompositeHandler, FileHandler
   
   # Send audit logs to multiple destinations
   audit_handler = CompositeHandler([
       SyslogHandler("siem.company.com:514"),
       FileHandler("/var/log/fortinet-audit.log")
   ])
   
   # Use with FortiOS client (via hfortix-fortios)
   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(
       host="192.168.1.99",
       token="token",
       audit_handler=audit_handler
   )

**Debug Session**

.. code-block:: python

   from hfortix_core import DebugSession
   from hfortix_fortios import FortiOS
   
   with DebugSession() as debug:
       fgt = FortiOS(host="192.168.1.99", token="token")
       
       # All requests are logged with detailed timing
       fgt.api.cmdb.firewall.policy.get()
       fgt.api.monitor.system.status.get()
   
   # Print debug summary
   debug.print_summary()

Dependencies
------------

HFortix-Core is used by:

* **hfortix-fortios** - FortiOS/FortiGate API client (1,348 endpoints)
* **hfortix-fortimanager** - FortiManager API client
* **hfortix** - Meta-package installing all HFortix components

Next Steps
----------

* :doc:`modules` - HTTP clients, caching, logging, debugging, and audit logging
* :doc:`exceptions` - Complete exception hierarchy with examples
* :doc:`types` - TypedDict definitions for responses and configurations
* :doc:`utilities` - Helper functions and formatters

For higher-level FortiOS automation, see:

* `HFortix-FortiOS Documentation <https://hfortix-fortios.readthedocs.io/>`_
* `GitHub Repository <https://github.com/hermanwjacobsen/hfortix-core>`_
