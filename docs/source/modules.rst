Core Modules
============

HTTP Client Framework
---------------------

The HTTP client framework provides both synchronous and asynchronous HTTP clients
with built-in retry logic, circuit breakers, connection pooling, and statistics.

IHTTPClient (Protocol Interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.http.IHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

BaseHTTPClient (Base Client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.http.BaseHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

HTTPClient (Synchronous FortiOS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.http.HTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

HTTPClientJSONRPC (Synchronous JSON-RPC, FortiManager/FortiAnalyzer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.HTTPClientJSONRPC
   :members:
   :undoc-members:
   :show-inheritance:

``hfortix_core.HTTPClientFMG`` is a backwards-compatibility alias for
``HTTPClientJSONRPC``.

AsyncHTTPClient (Asynchronous)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.http.AsyncHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

CloudHTTPClient (FortiCloud REST)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Used by ``hfortix-forticare`` and ``hfortix-fortiztp`` for
OAuth2-authenticated FortiCloud REST APIs.

.. autoclass:: hfortix_core.http.CloudHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

FortiCloudAuth (OAuth2 Authentication)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.http.FortiCloudAuth
   :members:
   :undoc-members:
   :show-inheritance:

get_oauth_token
~~~~~~~~~~~~~~~

.. autofunction:: hfortix_core.http.get_oauth_token

Caching
-------

TTLCache
~~~~~~~~

.. autoclass:: hfortix_core.TTLCache
   :members:
   :undoc-members:
   :show-inheritance:

readonly_cache
~~~~~~~~~~~~~~

.. autodata:: hfortix_core.readonly_cache

Logging
-------

RequestLogger
~~~~~~~~~~~~~

.. autoclass:: hfortix_core.RequestLogger
   :members:
   :undoc-members:
   :show-inheritance:

log_operation
~~~~~~~~~~~~~

.. autofunction:: hfortix_core.log_operation

StructuredFormatter
~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.StructuredFormatter
   :members:
   :undoc-members:
   :show-inheritance:

TextFormatter
~~~~~~~~~~~~~

.. autoclass:: hfortix_core.TextFormatter
   :members:
   :undoc-members:
   :show-inheritance:

LogFormatter (Protocol)
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.logging.LogFormatter
   :members:
   :undoc-members:
   :show-inheritance:

LogRecord (TypedDict)
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.logging.LogRecord
   :members:
   :undoc-members:
   :show-inheritance:

Debugging
---------

DebugSession
~~~~~~~~~~~~

.. autoclass:: hfortix_core.DebugSession
   :members:
   :undoc-members:
   :show-inheritance:

debug_timer
~~~~~~~~~~~

.. autofunction:: hfortix_core.debug_timer

format_connection_stats
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: hfortix_core.format_connection_stats

format_request_info
~~~~~~~~~~~~~~~~~~~

.. autofunction:: hfortix_core.format_request_info

print_debug_info
~~~~~~~~~~~~~~~~

.. autofunction:: hfortix_core.print_debug_info

DebugFormatter (Protocol)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.debug.DebugFormatter
   :members:
   :undoc-members:
   :show-inheritance:

DebugInfo (TypedDict)
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.debug.DebugInfo
   :members:
   :undoc-members:
   :show-inheritance:

SessionSummary (TypedDict)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.debug.SessionSummary
   :members:
   :undoc-members:
   :show-inheritance:

Formatting
----------

fmt Module
~~~~~~~~~~

.. automodule:: hfortix_core.fmt
   :members:
   :undoc-members:

Audit Logging
-------------

Enterprise-grade audit logging for compliance and security monitoring.

AuditHandler (Protocol)
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.AuditHandler
   :members:
   :undoc-members:
   :show-inheritance:

SyslogHandler
~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.SyslogHandler
   :members:
   :undoc-members:
   :show-inheritance:

FileHandler
~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.FileHandler
   :members:
   :undoc-members:
   :show-inheritance:

StreamHandler
~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.StreamHandler
   :members:
   :undoc-members:
   :show-inheritance:

CompositeHandler
~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.CompositeHandler
   :members:
   :undoc-members:
   :show-inheritance:

NullHandler
~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.NullHandler
   :members:
   :undoc-members:
   :show-inheritance:

AuditFormatter (Protocol)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.AuditFormatter
   :members:
   :undoc-members:
   :show-inheritance:

JSONFormatter
~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.JSONFormatter
   :members:
   :undoc-members:
   :show-inheritance:

SyslogFormatter
~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.SyslogFormatter
   :members:
   :undoc-members:
   :show-inheritance:

CEFFormatter
~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.CEFFormatter
   :members:
   :undoc-members:
   :show-inheritance:

AuditOperation (TypedDict)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.audit.AuditOperation
   :members:
   :undoc-members:
   :show-inheritance:

Request Hooks
-------------

The ``hfortix_core.hooks`` module defines protocol classes
(``BeforeRequestHook``, ``AfterRequestHook``, ``RequestContext``) that are
reserved for a future request-interception feature. They are **not yet
consumed by any HTTP client** — passing hook objects to client constructors
has no effect in the current release.
