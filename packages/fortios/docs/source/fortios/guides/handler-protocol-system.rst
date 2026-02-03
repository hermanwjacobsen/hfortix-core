Handler Protocol System
=======================

.. note::
   **✨ NEW in v0.4.1**: Extensible plugin architecture for custom audit handlers

   Write custom audit handlers without modifying HFortix code. Integrate with any system using a simple protocol.

Overview
--------

The Handler Protocol System enables you to extend HFortix's audit logging capabilities by writing custom handlers that integrate with any external system. No inheritance required - any class implementing ``log_operation(operation: dict)`` works as an audit handler.

**Key Features:**

- ✅ **No Inheritance Required**: Protocol-based (duck typing)
- ✅ **Priority Ordering**: Execute handlers in priority order
- ✅ **Conditional Routing**: Filter which operations go where
- ✅ **Error Aggregation**: Track handler reliability
- ✅ **Dynamic Management**: Add/remove handlers at runtime
- ✅ **Production Ready**: Kafka, Database, Webhook examples included

Why Protocol-Based?
~~~~~~~~~~~~~~~~~~~

**Zero Coupling**
   Handlers don't depend on HFortix internals

**Type Safety**
   ``@runtime_checkable`` Protocol provides IDE autocomplete

**Testability**
   Mock handlers without inheritance hierarchies

**Flexibility**
   Use any class that implements ``log_operation()``

Quick Start
-----------

Basic Custom Handler
~~~~~~~~~~~~~~~~~~~~

Any class with a ``log_operation(operation: dict)`` method can be an audit handler:

.. code-block:: python

   from typing import Any
   from hfortix import FortiOS

   class SlackNotifier:
       """Send notifications to Slack when firewall rules change"""
       
       def __init__(self, webhook_url: str):
           self.webhook_url = webhook_url
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           """Called after every API operation"""
           if 'firewall.policy' in operation.get('object_type', ''):
               action = operation['action']
               user = operation.get('user_context', {}).get('username', 'Unknown')
               object_name = operation.get('object_name', 'N/A')
               
               message = f"🔥 Firewall changed by {user}: {action} {object_name}"
               self._send_to_slack(message)
       
       def _send_to_slack(self, message: str):
           import requests
           requests.post(self.webhook_url, json={"text": message})

   # Use it
   handler = SlackNotifier("https://hooks.slack.com/services/YOUR/WEBHOOK")
   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

   # Now all firewall policy changes trigger Slack notifications
   fgt.api.cmdb.firewall.policy.post(name="Block-Malware", ...)
   # → Slack: "🔥 Firewall changed by admin: create Block-Malware"

Operation Dictionary Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every ``log_operation()`` call receives a dictionary with:

.. code-block:: python

   {
       "timestamp": "2025-01-08T10:30:45.123456",
       "action": "create",  # create, read, update, delete
       "object_type": "cmdb.firewall.policy",
       "object_name": "Block-Malware",
       "success": True,
       "duration": 0.342,  # seconds
       "request_id": "uuid-...",
       "trace_id": "trace-uuid-...",  # for distributed tracing
       "user_context": {
           "username": "admin",
           "ticket_id": "TICKET-123",
           "application": "automation-script"
       },
       "request": {
           "method": "POST",
           "path": "/api/v2/cmdb/firewall/policy",
           "data": {...}
       },
       "response": {
           "status": 200,
           "data": {...}
       },
       "error": None  # or error details if success=False
   }

Built-in Handler Examples
--------------------------

Kafka Handler
~~~~~~~~~~~~~

Stream audit events to Kafka for distributed systems:

.. code-block:: python

   from examples.custom_handlers.kafka_handler import KafkaHandler

   handler = KafkaHandler(
       bootstrap_servers=["kafka1:9092", "kafka2:9092"],
       topic="fortinet-audit",
       compression_type="gzip"  # or snappy, lz4
   )

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

**Features:**

- Async publishing with callbacks
- Partition key routing by request_id
- Compression support (gzip, snappy, lz4)
- Automatic cleanup with context manager
- Error handling and logging

Database Handler
~~~~~~~~~~~~~~~~

Store audit logs in SQL databases:

.. code-block:: python

   from examples.custom_handlers.database_handler import DatabaseHandler

   # SQLite for development
   handler = DatabaseHandler("sqlite:///audit.db")

   # PostgreSQL for production
   handler = DatabaseHandler("postgresql://user:pass@localhost/audit_db")

   # MySQL for production
   handler = DatabaseHandler("mysql://user:pass@localhost/audit_db")

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

   # Query audit logs
   recent = handler.query_operations(
       start_time="2025-01-01",
       end_time="2025-01-08",
       action="delete"
   )

**Features:**

- Multi-database support (SQLite, PostgreSQL, MySQL)
- Automatic table creation with indexes
- JSON/JSONB column support
- Query API for compliance reporting
- Handles large JSON payloads

Webhook Handler
~~~~~~~~~~~~~~~

Send notifications to Slack, Teams, or Discord:

.. code-block:: python

   from examples.custom_handlers.webhook_handler import (
       SlackNotifier,
       TeamsNotifier,
       DiscordNotifier
   )

   # Slack notifications (only for policy changes)
   slack = SlackNotifier(
       "https://hooks.slack.com/services/YOUR/WEBHOOK",
       filter_fn=lambda op: 'policy' in op.get('object_type', '')
   )

   # Teams alerts (only for failures)
   teams = TeamsNotifier(
       "https://outlook.office.com/webhook/...",
       filter_fn=lambda op: not op['success']
   )

   # Discord notifications
   discord = DiscordNotifier("https://discord.com/api/webhooks/...")

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=slack)

**Features:**

- Rich message formatting with colors
- Platform-specific formatters (Slack, Teams, Discord)
- Automatic retry with backoff
- Filter support for conditional notifications
- Includes error details and stack traces

Enhanced CompositeHandler
--------------------------

Route operations to different handlers based on priority and filters.

Priority-Based Routing
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.audit import CompositeHandler, FileHandler, SyslogHandler

   handler = CompositeHandler([
       # Critical operations to dedicated file (highest priority)
       (FileHandler('/var/log/critical.jsonl'), 100),
       
       # Everything to SIEM (medium priority)
       (SyslogHandler('siem.company.com:514'), 50),
       
       # Everything to general log (lowest priority)
       (FileHandler('/var/log/all.jsonl'), 1),
   ])

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

**Execution Order:**

1. Handlers are sorted by priority (highest first)
2. Each handler receives the operation in order
3. Errors in one handler don't affect others (when ``aggregate_errors=True``)

Conditional Routing with Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.audit import CompositeHandler, FileHandler, SyslogHandler

   # Define filters
   def is_critical(op):
       """Critical: deletes or failures"""
       return op['action'] == 'delete' or not op['success']

   def is_policy_change(op):
       """Policy changes only"""
       return 'policy' in op.get('object_type', '')

   def is_slow(op):
       """Slow operations (>1 second)"""
       return op['duration'] > 1.0

   # Priority + filter routing
   handler = CompositeHandler([
       # Critical operations → dedicated file
       (FileHandler('/var/log/critical.jsonl'), 100, is_critical),
       
       # Policy changes → SIEM
       (SyslogHandler('siem.company.com:514'), 50, is_policy_change),
       
       # Slow operations → performance log
       (FileHandler('/var/log/slow.jsonl'), 25, is_slow),
       
       # Everything → general log
       (FileHandler('/var/log/all.jsonl'), 1, None),
   ])

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

**Filter Functions:**

- Receive the operation dictionary
- Return ``True`` to log, ``False`` to skip
- ``None`` filter = log everything

Error Aggregation
~~~~~~~~~~~~~~~~~

Track handler reliability and troubleshoot issues:

.. code-block:: python

   handler = CompositeHandler([...], aggregate_errors=True)
   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

   # Perform operations...
   fgt.api.cmdb.firewall.policy.post(...)

   # Check error summary
   summary = handler.error_summary
   print(f"Total errors: {summary['total_errors']}")
   print(f"Failed handlers: {summary['failed_handlers']}")
   
   for error in summary['errors']:
       print(f"Handler: {error['handler']}")
       print(f"Error: {error['error']}")
       print(f"Timestamp: {error['timestamp']}")

**Error Summary Format:**

.. code-block:: python

   {
       "total_errors": 3,
       "failed_handlers": ["KafkaHandler", "SyslogHandler"],
       "errors": [
           {
               "handler": "KafkaHandler",
               "error": "Connection refused",
               "timestamp": "2025-01-08T10:30:45.123456",
               "operation": {...}
           },
           ...
       ]
   }

Dynamic Handler Management
~~~~~~~~~~~~~~~~~~~~~~~~~~

Add or remove handlers at runtime:

.. code-block:: python

   handler = CompositeHandler([
       FileHandler('/var/log/all.jsonl')
   ])

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

   # Add Slack notifications for critical events
   slack = SlackNotifier("https://...")
   handler.add_handler(
       slack,
       priority=100,
       filter_fn=lambda op: not op['success']
   )

   # Later: remove Slack handler
   handler.remove_handler(slack)

**Use Cases:**

- Enable/disable notifications based on time of day
- Add temporary debugging handlers
- Dynamically configure based on environment
- A/B testing different handler configurations

Advanced Patterns
-----------------

Multi-Destination Routing
~~~~~~~~~~~~~~~~~~~~~~~~~~

Route different operation types to different systems:

.. code-block:: python

   from examples.custom_handlers import KafkaHandler, DatabaseHandler, SlackNotifier

   # Define routing filters
   def is_audit_event(op):
       """Security-relevant events"""
       return op['action'] in ('create', 'update', 'delete')

   def is_monitoring(op):
       """Read-only monitoring"""
       return op['action'] == 'read'

   # Route based on operation type
   handler = CompositeHandler([
       # Audit events → Kafka (for real-time processing)
       (KafkaHandler(["kafka:9092"], "audit"), 100, is_audit_event),
       
       # Audit events → Database (for compliance queries)
       (DatabaseHandler("postgresql://..."), 90, is_audit_event),
       
       # Failures → Slack (for immediate alerts)
       (SlackNotifier("https://..."), 80, lambda op: not op['success']),
       
       # Monitoring → separate log file
       (FileHandler('/var/log/monitoring.jsonl'), 50, is_monitoring),
       
       # Everything → archive
       (FileHandler('/var/log/archive.jsonl'), 1, None),
   ])

Environment-Based Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different handlers for dev/staging/production:

.. code-block:: python

   import os
   from hfortix_core.audit import CompositeHandler, FileHandler

   env = os.getenv("ENVIRONMENT", "dev")

   if env == "production":
       handler = CompositeHandler([
           KafkaHandler(["kafka-prod:9092"], "audit"),
           DatabaseHandler("postgresql://prod-db/audit"),
           SlackNotifier("https://hooks.slack.com/production"),
       ])
   elif env == "staging":
       handler = CompositeHandler([
           DatabaseHandler("postgresql://staging-db/audit"),
           FileHandler('/var/log/staging-audit.jsonl'),
       ])
   else:  # development
       handler = FileHandler('/var/log/dev-audit.jsonl')

   fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

Time-Based Filtering
~~~~~~~~~~~~~~~~~~~~~

Different behavior during business hours vs off-hours:

.. code-block:: python

   from datetime import datetime

   def is_business_hours(op):
       """9 AM - 5 PM weekdays"""
       now = datetime.fromisoformat(op['timestamp'])
       return (
           now.weekday() < 5 and  # Monday-Friday
           9 <= now.hour < 17      # 9 AM - 5 PM
       )

   def is_after_hours(op):
       """Nights and weekends"""
       return not is_business_hours(op)

   handler = CompositeHandler([
       # Business hours: quiet logging
       (FileHandler('/var/log/business.jsonl'), 50, is_business_hours),
       
       # After hours: loud alerts (shouldn't be changes!)
       (SlackNotifier("https://..."), 100, is_after_hours),
       (FileHandler('/var/log/after-hours.jsonl'), 90, is_after_hours),
   ])

Compliance-Focused Handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Track changes for SOC 2, HIPAA, PCI-DSS compliance:

.. code-block:: python

   class ComplianceHandler:
       """Enforce compliance requirements"""
       
       def __init__(self, db_connection_string: str):
           self.db = DatabaseHandler(db_connection_string)
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           """Validate and log with compliance metadata"""
           
           # Ensure user context is present
           if not operation.get('user_context'):
               raise ValueError("Compliance requires user_context")
           
           user_ctx = operation['user_context']
           
           # SOC 2: Require ticket_id for changes
           if operation['action'] in ('create', 'update', 'delete'):
               if not user_ctx.get('ticket_id'):
                   raise ValueError("Change requires ticket_id for SOC 2")
           
           # Add compliance metadata
           operation['compliance'] = {
               'soc2_compliant': True,
               'approved_change': user_ctx.get('ticket_id') is not None,
               'authorized_user': user_ctx.get('username'),
               'audit_timestamp': operation['timestamp'],
           }
           
           # Store in tamper-proof database
           self.db.log_operation(operation)

   handler = ComplianceHandler("postgresql://audit-db/compliance")
   fgt = FortiOS(
       "192.168.1.99",
       token="token",
       audit_handler=handler,
       user_context={"username": "admin", "ticket_id": "TICKET-123"}
   )

Testing Custom Handlers
------------------------

Unit Testing
~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from typing import Any

   class TestSlackNotifier:
       def test_filters_non_policy_changes(self):
           """Should only notify for policy changes"""
           messages = []
           
           class MockSlack(SlackNotifier):
               def _send_to_slack(self, message: str):
                   messages.append(message)
           
           handler = MockSlack("https://fake")
           
           # Non-policy change (should be ignored)
           handler.log_operation({
               'action': 'create',
               'object_type': 'cmdb.system.interface',
               'object_name': 'port1',
           })
           assert len(messages) == 0
           
           # Policy change (should notify)
           handler.log_operation({
               'action': 'create',
               'object_type': 'cmdb.firewall.policy',
               'object_name': 'Block-Malware',
               'user_context': {'username': 'admin'},
           })
           assert len(messages) == 1
           assert 'Block-Malware' in messages[0]

Integration Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_composite_handler_priority():
       """Handlers execute in priority order"""
       execution_order = []
       
       class OrderedHandler:
           def __init__(self, name: str):
               self.name = name
           
           def log_operation(self, operation: dict[str, Any]) -> None:
               execution_order.append(self.name)
       
       handler = CompositeHandler([
           (OrderedHandler("low"), 1),
           (OrderedHandler("high"), 100),
           (OrderedHandler("medium"), 50),
       ])
       
       handler.log_operation({'action': 'test'})
       
       assert execution_order == ["high", "medium", "low"]

Mock Handlers for Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   class MockHandler:
       """Collect operations without side effects"""
       
       def __init__(self):
           self.operations = []
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           self.operations.append(operation.copy())
       
       def get_operations(self, **filters):
           """Query collected operations"""
           results = self.operations
           
           if 'action' in filters:
               results = [op for op in results if op['action'] == filters['action']]
           
           if 'success' in filters:
               results = [op for op in results if op['success'] == filters['success']]
           
           return results

   # Use in tests
   mock = MockHandler()
   fgt = FortiOS("192.168.1.99", token="token", audit_handler=mock)

   fgt.api.cmdb.firewall.policy.post(...)

   # Verify behavior
   creates = mock.get_operations(action='create')
   assert len(creates) == 1
   assert creates[0]['object_type'] == 'cmdb.firewall.policy'

Best Practices
--------------

Error Handling
~~~~~~~~~~~~~~

Always handle errors gracefully in handlers:

.. code-block:: python

   import logging

   class RobustHandler:
       def __init__(self):
           self.logger = logging.getLogger(__name__)
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           try:
               self._do_logging(operation)
           except Exception as e:
               # Log the error but don't crash the application
               self.logger.error(f"Handler failed: {e}", exc_info=True)
               # Optionally re-raise if you want CompositeHandler to track it
               # raise

Performance Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Async Operations**: Use async publishing for I/O-bound handlers:

.. code-block:: python

   from concurrent.futures import ThreadPoolExecutor

   class AsyncHandler:
       def __init__(self):
           self.executor = ThreadPoolExecutor(max_workers=5)
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           # Don't block the main thread
           self.executor.submit(self._async_log, operation)
       
       def _async_log(self, operation: dict[str, Any]) -> None:
           # Slow I/O operation here
           ...

**Batching**: Batch operations for efficiency:

.. code-block:: python

   class BatchHandler:
       def __init__(self, batch_size=100, flush_interval=60):
           self.batch = []
           self.batch_size = batch_size
           self.flush_interval = flush_interval
           self.last_flush = time.time()
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           self.batch.append(operation)
           
           if (len(self.batch) >= self.batch_size or
               time.time() - self.last_flush > self.flush_interval):
               self._flush_batch()
       
       def _flush_batch(self):
           if self.batch:
               # Send batch to external system
               self._send_batch(self.batch)
               self.batch = []
               self.last_flush = time.time()

Security Considerations
~~~~~~~~~~~~~~~~~~~~~~~

**Credentials**: Never log sensitive data:

.. code-block:: python

   class SecureHandler:
       def log_operation(self, operation: dict[str, Any]) -> None:
           # Make a copy to avoid modifying the original
           safe_op = operation.copy()
           
           # Redact sensitive fields
           if 'request' in safe_op and 'data' in safe_op['request']:
               data = safe_op['request']['data']
               for sensitive_field in ('password', 'token', 'secret', 'api_key'):
                   if sensitive_field in data:
                       data[sensitive_field] = '***REDACTED***'
           
           self._log_safely(safe_op)

**Data Retention**: Implement retention policies:

.. code-block:: python

   class RetentionHandler:
       def __init__(self, db: DatabaseHandler, retention_days=90):
           self.db = db
           self.retention_days = retention_days
       
       def log_operation(self, operation: dict[str, Any]) -> None:
           # Log current operation
           self.db.log_operation(operation)
           
           # Periodically clean old data
           if random.random() < 0.01:  # 1% of operations
               self._cleanup_old_data()
       
       def _cleanup_old_data(self):
           cutoff = datetime.now() - timedelta(days=self.retention_days)
           # Delete operations older than retention period
           ...

See Also
--------

- :doc:`audit-logging` - Built-in audit logging features
- :doc:`observability` - Monitoring and telemetry
- :doc:`debugging` - Debug logging and troubleshooting
- Example handlers: ``examples/custom_handlers/``
- Demo script: ``examples/composite_handler_demo.py``
- Full documentation: `HANDLER_PROTOCOL_SYSTEM.md <https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/HANDLER_PROTOCOL_SYSTEM.md>`_
