Core Modules
============

HTTP Client Framework
---------------------

The HTTP client framework provides both synchronous and asynchronous HTTP clients
with built-in retry logic, circuit breakers, connection pooling, and statistics.

Protocol Interface
^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_core.http.IHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

Base Client
^^^^^^^^^^^

.. autoclass:: hfortix_core.http.BaseHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

Synchronous Clients
^^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_core.http.HTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.HTTPClientFMG
   :members:
   :undoc-members:
   :show-inheritance:

Asynchronous Client
^^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_core.http.AsyncHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

Caching
-------

.. autoclass:: hfortix_core.TTLCache
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: hfortix_core.readonly_cache

Logging
-------

Handlers
^^^^^^^^

.. autoclass:: hfortix_core.RequestLogger
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: hfortix_core.log_operation

Formatters
^^^^^^^^^^

.. autoclass:: hfortix_core.StructuredFormatter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.TextFormatter
   :members:
   :undoc-members:
   :show-inheritance:

Protocols & Types
^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_core.logging.LogFormatter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.logging.LogRecord
   :members:
   :undoc-members:
   :show-inheritance:

Debugging
---------

Session & Handlers
^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_core.DebugSession
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: hfortix_core.debug_timer

Formatters & Utilities
^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: hfortix_core.format_connection_stats
.. autofunction:: hfortix_core.format_request_info
.. autofunction:: hfortix_core.print_debug_info

Protocols & Types
^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_core.debug.DebugFormatter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.debug.DebugInfo
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.debug.SessionSummary
   :members:
   :undoc-members:
   :show-inheritance:

Formatting
----------

.. automodule:: hfortix_core.fmt
   :members:
   :undoc-members:

Audit Logging (Enterprise)
---------------------------

Enterprise-grade audit logging for compliance and security monitoring.

Handlers
^^^^^^^^

.. autoclass:: hfortix_core.audit.AuditHandler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.SyslogHandler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.FileHandler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.StreamHandler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.CompositeHandler
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.NullHandler
   :members:
   :undoc-members:
   :show-inheritance:

Formatters
^^^^^^^^^^

.. autoclass:: hfortix_core.audit.AuditFormatter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.JSONFormatter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.SyslogFormatter
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.audit.CEFFormatter
   :members:
   :undoc-members:
   :show-inheritance:

Types
^^^^^

.. autoclass:: hfortix_core.audit.AuditOperation
   :members:
   :undoc-members:
   :show-inheritance:

Request Hooks
-------------

Protocol-based hooks for intercepting and modifying API requests/responses.

.. autoclass:: hfortix_core.hooks.BeforeRequestHook
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.hooks.AfterRequestHook
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hfortix_core.hooks.RequestContext
   :members:
   :undoc-members:
   :show-inheritance:
