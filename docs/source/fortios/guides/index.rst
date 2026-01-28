Topic Guides
============

Advanced topics, patterns, and techniques for working with HFortix.

.. toctree::
   :maxdepth: 1

   fmg-proxy
   custom-wrappers
   audit-logging
   handler-protocol-system
   observability
   debugging
   rate-limiting
   filtering
   validation
   performance

Overview
--------

Topic guides provide detailed, task-oriented documentation for advanced features and patterns.

Key Topics
----------

**FortiManager Proxy** *(New in v0.5.0)*
   Route FortiOS API calls through FortiManager to manage multiple FortiGate devices.
   Connect to FortiManager once and execute operations on any managed device using
   the same FortiOS API syntax. Supports multiple ADOMs and VDOMs.

**Creating Custom Wrappers** *(New in v0.5.146)*
   Learn how to create your own convenience wrappers, aliases, and helper functions
   tailored to your specific needs. Includes examples for simple aliases, domain-specific
   wrappers, validation wrappers, async operations, and complete custom modules.

Advanced Topics
---------------

**Audit Logging**
   Enterprise audit logging with SIEM integration for compliance (SOC 2, HIPAA, PCI-DSS).
   Built-in handlers for syslog, files, and streams. Automatic data sanitization and
   user context tracking.

**Handler Protocol System** *(New in v0.4.1)*
   Extensible plugin architecture for custom audit handlers. Write handlers that integrate
   with Kafka, databases, webhooks, or any external system without modifying HFortix code.
   Protocol-based design with priority routing, conditional filtering, error aggregation,
   and dynamic management. Includes production-ready examples for Kafka, PostgreSQL/MySQL,
   and Slack/Teams/Discord notifications.

**Observability**
   Structured logging and distributed tracing for production systems. Includes
   ``configure_logging()`` helper, JSON formatters, ``trace_id`` parameter for
   request correlation, and automatic VDOM/ADOM inclusion for multi-tenant environments.
   Integration with ELK, Splunk, CloudWatch, and Datadog.

**Debugging** *(New in v0.4.0)*
   Comprehensive debugging tools and techniques. Covers debug mode (``debug=True``),
   connection pool monitoring (``fgt.connection_stats``), request inspection
   (``fgt.last_request``), DebugSession context manager, performance profiling,
   and structured logging configuration. Includes integration examples for
   ELK, Splunk, and CloudWatch.

**Rate Limiting** *(New in v0.4.0)*
   Complete guide to handling API rate limits and building resilient applications.
   Covers HTTP 429 handling, retry strategies (exponential/linear/fibonacci),
   circuit breaker patterns, connection pool management, and async patterns for
   high throughput. Includes production-ready configuration examples.

**Filtering**
   Complete guide to filtering and querying API results. 50+ examples covering
   simple filters, complex queries, logical operators, and performance optimization.

**Validation**
   Guide to the validation framework with 832 auto-generated validators. Covers
   enum validation, length limits, range checks, pattern matching, and type validation.

**Performance**
   Performance testing guide and optimization strategies. Includes connection pool
   tuning, timeout configuration, and device-specific recommendations.

See Also
--------

- :doc:`/fortios/user-guide/index` - Core concepts and essential features
- :doc:`/fortios/api-reference/index` - Complete API reference
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
