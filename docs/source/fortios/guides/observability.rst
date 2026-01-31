Logging & Observability
=======================

.. note::
   For detailed markdown documentation with extensive examples, see:
   `docs/fortios/OBSERVABILITY.md <https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/OBSERVABILITY.md>`_

Enterprise-grade logging and observability for production systems.

Overview
--------

HFortix provides comprehensive logging and observability features designed for modern distributed systems:

* **Structured Logging** - Machine-readable JSON logs for log aggregation
* **Distributed Tracing** - ``trace_id`` parameter for request correlation
* **Easy Configuration** - One-line setup with ``configure_logging()``
* **Multiple Formats** - Text (human-readable) or JSON (machine-readable)
* **Integration Ready** - Works with ELK Stack, Splunk, CloudWatch, Datadog

Quick Start
-----------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import FortiOS, configure_logging

   # Configure logging (one time, at application startup)
   configure_logging(level="INFO", format="text")

   # Create client - logs automatically configured
   fgt = FortiOS("192.168.1.99", token="your-token")

Production Configuration (JSON)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import configure_logging, FortiOS

   # Configure JSON logging for production
   configure_logging(level="INFO", format="json")

   # All logs now in structured JSON format
   fgt = FortiOS("192.168.1.99", token="your-token")

**Output Example**:

.. code-block:: json

   {
     "timestamp": "2026-01-02T10:30:15.123456+00:00",
     "level": "INFO",
     "logger": "hfortix.http",
     "message": "Request completed successfully",
     "request_id": "a1b2c3d4",
     "method": "GET",
     "endpoint": "/api/v2/monitor/system/status",
     "status_code": 200,
     "duration_seconds": 0.234,
     "attempts": 1
   }

configure_logging() Function
-----------------------------

The ``configure_logging()`` function provides one-stop setup for all hfortix logging.

Signature
~~~~~~~~~

.. code-block:: python

   def configure_logging(
       level: str | int = "INFO",
       format: Literal["json", "text"] = "text",
       handler: logging.Handler | None = None,
       use_color: bool = False,
   ) -> None:
       """Configure logging for HFortix library"""

Parameters
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Default
     - Description
   * - ``level``
     - str | int
     - ``"INFO"``
     - Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
   * - ``format``
     - str
     - ``"text"``
     - Output format: "text" or "json"
   * - ``handler``
     - Handler
     - None
     - Custom logging handler (optional)
   * - ``use_color``
     - bool
     - False
     - Use ANSI colors in text format

Examples
~~~~~~~~

Development: Colored Text Logs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   configure_logging(level="DEBUG", format="text", use_color=True)

Production: JSON to File
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import logging

   # Create file handler
   file_handler = logging.FileHandler("/var/log/hfortix.json")

   # Configure JSON logging to file
   configure_logging(
       level="INFO",
       format="json",
       handler=file_handler
   )

Distributed Tracing with trace_id
----------------------------------

The ``trace_id`` parameter enables request correlation across your entire stack.

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Pass trace_id to correlate this request
   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       trace_id="req-abc-123-xyz"
   )

   # All API calls include this trace_id in logs
   fgt.api.monitor.system.status.get()

**Log Output**:

.. code-block:: json

   {
     "timestamp": "2026-01-02T10:30:15Z",
     "level": "INFO",
     "logger": "hfortix.http",
     "message": "Request completed successfully",
     "trace_id": "req-abc-123-xyz",
     "request_id": "a1b2c3d4",
     "method": "GET",
     "endpoint": "/api/v2/monitor/system/status"
   }

Microservices Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, request
   from hfortix_fortios import FortiOS

   app = Flask(__name__)

   @app.route('/api/firewall/address')
   def create_address():
       # Extract trace_id from incoming request
       trace_id = request.headers.get('X-Trace-ID')
       
       # Pass it to FortiOS client
       fgt = FortiOS(
           "192.168.1.99",
           token="token",
           trace_id=trace_id
       )
       
       # Now you can correlate across your entire stack
       result = fgt.api.cmdb.firewall.address.post(
           name="test-host",
           subnet="10.0.0.1/32"
       )
       
       return {"status": "created", "trace_id": trace_id}

User Context for Change Management
-----------------------------------

The ``user_context`` parameter adds custom metadata to every log entry and audit record.

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   fgt = FortiOS(
       "192.168.1.99",
       token="your-token",
       user_context={
           "username": "john.doe",
           "ticket": "CHG-12345",
           "app": "firewall-manager",
           "environment": "production"
       }
   )

**Log Output**:

.. code-block:: json

   {
     "timestamp": "2026-01-02T10:30:15Z",
     "user_context": {
       "username": "john.doe",
       "ticket": "CHG-12345",
       "app": "firewall-manager",
       "environment": "production"
     },
     "method": "POST",
     "endpoint": "/api/v2/cmdb/firewall/address"
   }

Use Cases
~~~~~~~~~

Change Management
^^^^^^^^^^^^^^^^^

.. code-block:: python

   fgt = FortiOS(
       "192.168.1.99",
       token="token",
       user_context={
           "username": "jane.smith",
           "ticket": "CHG-67890",
           "change_type": "firewall_policy",
           "approver": "security-team",
           "scheduled_time": "2026-01-02T22:00:00Z"
       }
   )

CI/CD Pipelines
^^^^^^^^^^^^^^^

.. code-block:: python

   import os

   fgt = FortiOS(
       "192.168.1.99",
       token="token",
       user_context={
           "pipeline": os.getenv("CI_PIPELINE_ID"),
           "commit": os.getenv("CI_COMMIT_SHA"),
           "branch": os.getenv("CI_COMMIT_BRANCH"),
           "triggered_by": os.getenv("GITLAB_USER_LOGIN")
       }
   )

Integration Examples
--------------------

ELK Stack
~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import configure_logging, FortiOS

   # Configure JSON logging
   configure_logging(level="INFO", format="json")

   # Create client with context
   fgt = FortiOS(
       "192.168.1.99",
       token="token",
       trace_id="req-abc-123",
       user_context={
           "service": "firewall-automation",
           "version": "1.2.3",
           "environment": "production"
       }
   )

   # Logs flow to Filebeat → Logstash → Elasticsearch
   # Query in Kibana: trace_id:"req-abc-123"

AWS CloudWatch Logs
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortios import configure_logging, FortiOS
   import watchtower
   import logging

   # Configure CloudWatch handler
   cloudwatch_handler = watchtower.CloudWatchLogHandler(
       log_group="/aws/ecs/firewall-automation",
       stream_name="hfortix"
   )

   configure_logging(
       level="INFO",
       format="json",
       handler=cloudwatch_handler
   )

   fgt = FortiOS(
       "192.168.1.99",
       token="token",
       trace_id="req-abc-123",
       user_context={
           "task_arn": os.getenv("ECS_TASK_ARN"),
           "cluster": os.getenv("ECS_CLUSTER")
       }
   )

Best Practices
--------------

1. Configure Once at Startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # ✅ Good: Configure at application startup
   if __name__ == "__main__":
       configure_logging(level="INFO", format="json")
       main()

   # ❌ Bad: Configuring in every function
   def process_request():
       configure_logging(...)  # Don't do this

2. Use JSON in Production
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # ✅ Production: JSON format
   configure_logging(level="INFO", format="json")

   # ✅ Development: Text with colors
   configure_logging(level="DEBUG", format="text", use_color=True)

3. Always Include trace_id in Distributed Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # ✅ Good: Propagate trace_id
   def handle_request(request):
       trace_id = request.headers.get('X-Trace-ID') or generate_trace_id()
       fgt = FortiOS("host", token="token", trace_id=trace_id)
       
   # ❌ Bad: No trace_id
   def handle_request(request):
       fgt = FortiOS("host", token="token")  # Can't correlate

See Also
--------

* **Detailed Guide**: `docs/fortios/OBSERVABILITY.md <https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/OBSERVABILITY.md>`_
* **Audit Logging**: :doc:`audit-logging`
* **Examples**: ``examples/observability_demo.py``
* **API Reference**: :doc:`/fortios/api-reference/index`

Summary
-------

Key Features:

* ✅ **Easy Configuration** - One-line setup with ``configure_logging()``
* ✅ **Structured Logging** - JSON format for ELK/Splunk/CloudWatch
* ✅ **Distributed Tracing** - ``trace_id`` for request correlation
* ✅ **Change Management** - ``user_context`` for compliance
* ✅ **Production Ready** - Integration with major log aggregation platforms

Next Steps:

1. Use ``configure_logging()`` in your applications
2. Add ``trace_id`` to API requests for distributed tracing
3. Include ``user_context`` for compliance tracking
4. Set up log aggregation (ELK, Splunk, CloudWatch)
5. Review the comprehensive guide at `docs/fortios/OBSERVABILITY.md <https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/OBSERVABILITY.md>`_
