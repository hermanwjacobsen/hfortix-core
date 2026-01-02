Enterprise Audit Logging
========================

.. note::
   **Enterprise Feature**: Built-in compliance auditing for SOC 2, HIPAA, PCI-DSS

   This feature is **unique to HFortix** and not available in Fortinet's official ``fortiosapi`` library.

Overview
--------

HFortix includes enterprise-grade audit logging that automatically tracks all API operations to FortiGate devices. This feature is essential for compliance and provides complete visibility into infrastructure changes.

Why Audit Logging Matters
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Compliance Requirements**
   SOC 2, HIPAA, and PCI-DSS require audit trails of infrastructure changes

**Security**
   Track who changed what, when, and why

**Troubleshooting**
   Complete history of configuration changes

**Accountability**
   Link changes to users, tickets, and applications

Competitive Advantage
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 25 45

   * - Feature
     - HFortix
     - fortiosapi (Official)
   * - Audit Logging
     - ✅ Built-in
     - ❌ None
   * - Multiple Formats
     - ✅ JSON, Syslog, CEF
     - ❌ N/A
   * - SIEM Integration
     - ✅ Yes
     - ❌ No
   * - Compliance Ready
     - ✅ SOC 2, HIPAA, PCI-DSS
     - ❌ Manual implementation required

Quick Start
-----------

Basic File Logging
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix import FortiOS
   from hfortix_core.audit import FileHandler

   # Log all API operations to a file
   handler = FileHandler("/var/log/fortinet-audit.jsonl")
   fgt = FortiOS("192.168.1.99", token="your-token", audit_handler=handler)

   # All operations now automatically logged
   fgt.api.cmdb.firewall.address.create(name="test", subnet="10.0.0.1/32")

**Result**: Every API call logged to ``/var/log/fortinet-audit.jsonl`` in JSON Lines format:

.. code-block:: json

   {"timestamp":"2026-01-02T14:23:45Z","request_id":"a1b2c3d4","method":"POST","endpoint":"/api/v2/cmdb/firewall/address","vdom":"root","action":"create","object_type":"firewall.address","object_name":"test","data":{"name":"test","subnet":"10.0.0.1/32"},"status_code":200,"success":true,"duration_ms":145,"host":"192.168.1.99"}

SIEM Integration (Syslog)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.audit import SyslogHandler

   # Send audit logs to your SIEM
   handler = SyslogHandler("siem.company.com:514")
   fgt = FortiOS("192.168.1.99", token="your-token", audit_handler=handler)

   # All operations sent to SIEM in RFC 5424 format

**Use Cases**:

- Splunk
- ELK Stack (Elasticsearch, Logstash, Kibana)
- QRadar
- ArcSight
- Any syslog-compatible SIEM

Container/Kubernetes Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import sys
   from hfortix_core.audit import StreamHandler

   # Log to stdout (captured by container orchestration)
   handler = StreamHandler(sys.stdout)
   fgt = FortiOS("192.168.1.99", token="your-token", audit_handler=handler)

**Captured by**:

- Docker (``docker logs``)
- Kubernetes (``kubectl logs``)
- AWS ECS (CloudWatch)
- Azure Container Apps (Log Analytics)
- Google Cloud Run (Cloud Logging)

Multiple Destinations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.audit import CompositeHandler, FileHandler, SyslogHandler, StreamHandler

   # Send to multiple destinations simultaneously
   handler = CompositeHandler([
       SyslogHandler("siem.company.com:514"),      # Compliance team
       FileHandler("/var/log/fortinet.jsonl"),      # Local backup
       StreamHandler(sys.stdout),                   # Real-time monitoring
   ])

   fgt = FortiOS("192.168.1.99", token="your-token", audit_handler=handler)

Built-in Handlers
-----------------

FileHandler
~~~~~~~~~~~

Writes audit logs to a file in JSON Lines format with automatic rotation.

.. code-block:: python

   FileHandler(
       filepath="/var/log/fortinet-audit.jsonl",
       max_bytes=10_000_000,  # Rotate at 10MB
       backup_count=5,         # Keep 5 backups
   )

**Features**:

- JSON Lines format (one JSON per line)
- Automatic log rotation
- Compatible with log shippers (Fluentd, Filebeat, Logstash)

SyslogHandler
~~~~~~~~~~~~~

Sends audit logs to a syslog server in RFC 5424 format.

.. code-block:: python

   SyslogHandler(
       server="siem.company.com:514",  # host:port
   )

**Features**:

- RFC 5424 compliant
- UDP transport (fire-and-forget)
- Compatible with all major SIEMs

StreamHandler
~~~~~~~~~~~~~

Writes audit logs to stdout/stderr.

.. code-block:: python

   StreamHandler(
       stream=sys.stdout,  # or sys.stderr
   )

**Features**:

- JSON format
- Captured by container orchestration
- Real-time monitoring

CompositeHandler
~~~~~~~~~~~~~~~~

Sends audit logs to multiple handlers.

.. code-block:: python

   CompositeHandler([
       handler1,
       handler2,
       handler3,
   ])

.. note::
   **✨ NEW in v0.4.1**: CompositeHandler now supports priority-based routing, conditional filtering,
   error aggregation, and dynamic handler management.
   
   See :doc:`handler-protocol-system` for advanced CompositeHandler features and custom handler examples.

**Features**:

- Parallel logging
- Error isolation (one failure doesn't stop others)
- Useful for compliance + debugging

User Context Tracking
----------------------

Add metadata to every audit log to track users, applications, and change tickets:

.. code-block:: python

   from hfortix_core.audit import FileHandler

   handler = FileHandler("/var/log/fortinet-audit.jsonl")

   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       audit_handler=handler,
       user_context={
           "username": "admin",
           "app_name": "backup_automation",
           "change_ticket": "CHG-12345",
           "team": "network_ops",
           "environment": "production",
       }
   )

   # Every audit log now includes user context

Audit Log Format
----------------

Every audit log contains:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Field
     - Type
     - Description
   * - ``timestamp``
     - string
     - ISO 8601 timestamp
   * - ``request_id``
     - string
     - Unique request identifier
   * - ``method``
     - string
     - HTTP method (GET, POST, PUT, DELETE)
   * - ``endpoint``
     - string
     - Full API endpoint path
   * - ``api_type``
     - string
     - API category (cmdb, monitor, log, service)
   * - ``path``
     - string
     - Relative path
   * - ``vdom``
     - string
     - Virtual domain
   * - ``action``
     - string
     - High-level action (create, update, delete, read, list)
   * - ``object_type``
     - string
     - Object type (e.g., "firewall.address")
   * - ``object_name``
     - string
     - Object name (if available)
   * - ``data``
     - object
     - Request payload (sanitized)
   * - ``params``
     - object
     - Query parameters (sanitized)
   * - ``status_code``
     - integer
     - HTTP status code
   * - ``success``
     - boolean
     - Whether operation succeeded
   * - ``duration_ms``
     - integer
     - Operation duration in milliseconds
   * - ``host``
     - string
     - FortiGate IP/hostname
   * - ``error``
     - string
     - Error message (if failed)
   * - ``user_context``
     - object
     - User-provided context
   * - ``read_only_mode``
     - boolean
     - Whether simulated in read-only mode

Security Features
-----------------

Automatic Data Sanitization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sensitive fields are automatically redacted:

.. code-block:: python

   # Input data
   data = {
       "name": "vpn-user",
       "password": "secret123",
       "api_key": "abc123def456",
   }

   # Audit log (sanitized)
   {
       "data": {
           "name": "vpn-user",
           "password": "***REDACTED***",
           "api_key": "***REDACTED***",
       }
   }

**Automatically redacted**: ``password``, ``secret``, ``token``, ``api_key``, ``key``, ``private``, ``credential``

Non-Blocking
~~~~~~~~~~~~

Audit logging failures **never** break API operations:

.. code-block:: python

   # If syslog server is down, operation still succeeds
   fgt.api.cmdb.firewall.address.create(...)  # ✅ Succeeds

   # Error logged but doesn't raise exception
   # ERROR: Audit handler failed: Connection refused

Compliance Use Cases
--------------------

SOC 2
~~~~~

.. code-block:: python

   from hfortix_core.audit import CompositeHandler, SyslogHandler, FileHandler

   # SOC 2 requires audit trail of infrastructure changes
   handler = CompositeHandler([
       SyslogHandler("siem.company.com:514"),        # Real-time SIEM
       FileHandler("/archive/fortinet-audit.jsonl"), # Long-term storage
   ])

   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       audit_handler=handler,
       user_context={"auditor": "SOC2", "period": "Q1-2026"}
   )

HIPAA
~~~~~

.. code-block:: python

   # HIPAA requires tracking who accessed/modified what and when
   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       audit_handler=SyslogHandler("hipaa-siem.hospital.com:514"),
       user_context={
           "operator": "john.doe@hospital.com",
           "department": "IT Security",
           "compliance": "HIPAA",
       }
   )

PCI-DSS
~~~~~~~

.. code-block:: python

   # PCI-DSS 10.2: Track all access to cardholder data environment
   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       audit_handler=FileHandler("/pci/audit-trail.jsonl"),
       user_context={
           "pci_zone": "cardholder_data_environment",
           "compliance": "PCI-DSS v4.0",
       }
   )

Real-World Examples
-------------------

Multi-Team Environment
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Track which team made changes
   teams = {
       "network": {"handler": FileHandler("/logs/network-team.jsonl")},
       "security": {"handler": FileHandler("/logs/security-team.jsonl")},
   }

   # Network team
   fgt_network = FortiOS(
       "192.168.1.99",
       token="network-token",
       audit_handler=teams["network"]["handler"],
       user_context={"team": "network", "shift": "day"}
   )

   # Security team
   fgt_security = FortiOS(
       "192.168.1.99",
       token="security-token",
       audit_handler=teams["security"]["handler"],
       user_context={"team": "security", "shift": "night"}
   )

Change Management Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_change_ticket():
       """Get current change ticket from environment or system"""
       import os
       return os.getenv("CHANGE_TICKET", "NO-TICKET")

   ticket = get_change_ticket()

   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       audit_handler=SyslogHandler("siem.company.com:514"),
       user_context={
           "change_ticket": ticket,
           "approved_by": "change-board",
           "window": "2026-01-02 02:00-04:00 UTC",
       }
   )

   # All changes now linked to change ticket

Performance Impact
------------------

**Near Zero**: Audit logging is non-blocking and uses minimal CPU/memory.

- Logging happens **after** API response
- Failed audit logs don't retry (fire-and-forget)
- No performance penalty on API operations

Demo Script
-----------

Run the included demo to see all features:

.. code-block:: bash

   python3 examples/audit_logging_demo.py

See Also
--------

- :doc:`handler-protocol-system` - Custom audit handlers and plugin architecture *(New in v0.4.1)*
- :doc:`observability` - Structured logging and distributed tracing
- :doc:`/fortios/examples/basic-usage` - Basic FortiOS usage examples
- :doc:`/fortios/guides/validation` - Input validation guide
- :doc:`/fortios/guides/performance` - Performance optimization guide
