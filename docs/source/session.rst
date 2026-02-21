CloudSession - Multi-Service OAuth Management
=============================================

Overview
--------

``CloudSession`` provides centralized OAuth token management for multiple FortiCloud services. It enables efficient token sharing across different service clients while maintaining separate tokens for different ``client_id`` values.

Key Features
------------

* **Auto-detect client_id**: Services use their ``DEFAULT_CLIENT_ID`` automatically
* **Token caching**: Multiple clients with same ``client_id`` share tokens efficiently
* **Token sharing**: Different services can use the same session
* **Background refresh**: Optional auto-refresh thread to renew tokens before expiration
* **Thread-safe**: Concurrent access from multiple services
* **Context manager**: Auto-cleanup with ``with`` statement

Basic Usage
-----------

Simple Multi-Service Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_forticare import FortiCare
   from hfortix_fortiztp import FortiZTP

   # Simple usage - auto-detects client_id for each service
   with CloudSession(api_id="your_api_id", password="your_password") as session:
       fc = FortiCare(session=session)    # Uses "assetmanagement" client_id
       fz = FortiZTP(session=session)     # Uses "fortiztp" client_id
       
       # Both services share the session, each with their own token
       products = fc.api.products.list.post()
       devices = fz.devices.get()

Override Client ID
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Override client_id for specialized access
   with CloudSession(api_id="...", password="...") as session:
       fc_standard = FortiCare(session=session)                      # "assetmanagement"
       fc_elite = FortiCare(session=session, client_id="fcelite")   # "fcelite"
       # Each gets its own token

Auto-Refresh Mode
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Enable background token refresh
   session = CloudSession(
       api_id="...",
       password="...",
       auto_refresh=True,                 # Enable background refresh
       refresh_buffer_seconds=300,        # Refresh 5 min before expiry
       refresh_check_interval=60,         # Check every 60 seconds (default)
       check_before_request=True,         # Check before each request (default)
   )
   fc = FortiCare(session=session)
   # Tokens refresh automatically in background AND before each request
   
   # Don't forget to close when done
   session.close()

Advanced Refresh Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Option 1: Fast background checks + pre-request checks (most reliable)
   session = CloudSession(
       api_id="...",
       password="...",
       auto_refresh=True,
       refresh_check_interval=10,         # Check every 10 seconds
       check_before_request=True,         # Also check before each request
   )
   
   # Option 2: Pre-request checks only (no background thread)
   # All of these are equivalent ways to disable background refresh:
   session = CloudSession(
       api_id="...",
       password="...",
       auto_refresh=True,
       refresh_check_interval=0,          # Disable with 0
       # OR refresh_check_interval=None,  # Disable with None
       # OR refresh_check_interval=False, # Disable with False
       check_before_request=True,         # Only check before requests
   )
   
   # Option 3: Use default background interval
   session = CloudSession(
       api_id="...",
       password="...",
       auto_refresh=True,
       refresh_check_interval=True,       # Use default (60 seconds)
       check_before_request=True,
   )
   
   # Option 4: Manual control (advanced users only)
   session = CloudSession(
       api_id="...",
       password="...",
       auto_refresh=True,
       refresh_check_interval=False,      # No background checks
       check_before_request=False,        # No pre-request checks
   )
   # You must manually call ensure_token_valid() before requests!
   token = session.ensure_token_valid("assetmanagement")
   
   # Option 5: Custom expiration override (testing/debugging)
   session = CloudSession(
       api_id="...",
       password="...",
       default_expires_in=1800,           # Force 30-minute expiration
   )

Manual Token Management
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   session = CloudSession(api_id="...", password="...")
   
   # Get token for specific client_id
   fc_token = session.get_token("assetmanagement")
   
   # Check token expiration
   token_info = session.get_token_info("assetmanagement")
   print(f"Token expires in {token_info['time_remaining']}s")
   
   # Get all managed tokens
   all_tokens = session.get_all_tokens()
   for client_id, info in all_tokens.items():
       print(f"{client_id}: {info['time_remaining']}s remaining")

Enterprise Features
-------------------

Distributed Token Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~

Share tokens across multiple servers using pluggable storage backends:

**Redis (Recommended for Production Multi-Server)**

.. code-block:: python

   import redis
   from hfortix_core.session import CloudSession
   from hfortix_core.session.storage_examples import RedisTokenStorage

   # All servers share tokens via Redis
   r = redis.Redis(host='redis-cluster', port=6379)
   storage = RedisTokenStorage(r, namespace="prod:forticloud")

   session = CloudSession(
       api_id="...",
       password="...",
       token_storage=storage  # Tokens shared across all processes
   )

**PostgreSQL/MySQL (Persistent, ACID-Compliant)**

.. code-block:: python

   from sqlalchemy import create_engine
   from hfortix_core.session.storage_examples import DatabaseTokenStorage

   # PostgreSQL
   engine = create_engine('postgresql://user:pass@localhost/fortinet')
   
   # MySQL
   # engine = create_engine('mysql+pymysql://user:pass@localhost/fortinet')
   
   # SQLite (good for single-server)
   # engine = create_engine('sqlite:///tokens.db')

   storage = DatabaseTokenStorage(engine)
   session = CloudSession(
       api_id="...",
       password="...",
       token_storage=storage  # Tokens persist in database
   )

**File-Based (Simple, No External Dependencies)**

.. code-block:: python

   from hfortix_core.session.storage_examples import FileTokenStorage

   # Tokens stored in JSON files
   storage = FileTokenStorage(directory="/var/lib/forticloud/tokens")
   
   session = CloudSession(
       api_id="...",
       password="...",
       token_storage=storage  # Tokens persist in files
   )

**Storage Backend Comparison**

+-------------------+---------------------------+------------------------------+------------+--------------+
| Backend           | Best For                  | Requirements                 | Persistent | Distributed  |
+===================+===========================+==============================+============+==============+
| Redis             | Production multi-server   | ``pip install redis``        | No         | Yes          |
+-------------------+---------------------------+------------------------------+------------+--------------+
| PostgreSQL/MySQL  | Production clusters       | ``pip install sqlalchemy``   | Yes        | Yes          |
+-------------------+---------------------------+------------------------------+------------+--------------+
| SQLite            | Single-server production  | ``pip install sqlalchemy``   | Yes        | No           |
+-------------------+---------------------------+------------------------------+------------+--------------+
| File (JSON)       | Development, simple       | None (built-in)              | Yes        | No           |
+-------------------+---------------------------+------------------------------+------------+--------------+
| Memcached         | Lightweight caching       | ``pip install pymemcache``   | No         | Yes          |
+-------------------+---------------------------+------------------------------+------------+--------------+
| In-Memory         | Default, simple           | None (built-in)              | No         | No           |
+-------------------+---------------------------+------------------------------+------------+--------------+

Token Lifecycle Hooks
~~~~~~~~~~~~~~~~~~~~~~

Monitor token operations with callbacks for metrics, logging, and alerting:

**Prometheus Metrics**

.. code-block:: python

   from prometheus_client import start_http_server
   from hfortix_core.session.hooks_examples import PrometheusHooks

   # Expose metrics at :8000/metrics
   start_http_server(8000)
   hooks = PrometheusHooks(namespace="prod", service="api")

   session = CloudSession(
       api_id="...",
       password="...",
       lifecycle_hooks=hooks  # Automatic metrics collection
   )

   # Metrics available:
   # - forticloud_token_acquired_total
   # - forticloud_token_refreshed_total
   # - forticloud_token_expired_total
   # - forticloud_token_failed_total
   # - forticloud_token_lifetime_seconds

**Simple Callbacks**

.. code-block:: python

   from hfortix_core.session import SimpleLifecycleHooks

   def log_acquisition(event):
       print(f"Token acquired: {event.client_id}, expires {event.expires_in}s")

   def alert_failure(event):
       send_alert(f"Token failed: {event.error}")

   hooks = SimpleLifecycleHooks(
       on_acquired=log_acquisition,
       on_failed=alert_failure
   )

   session = CloudSession(
       api_id="...",
       password="...",
       lifecycle_hooks=hooks
   )

**Custom Hooks**

.. code-block:: python

   from hfortix_core.session import TokenLifecycleHooks, TokenEvent

   class MyHooks:
       def on_token_acquired(self, event: TokenEvent) -> None:
           # Called when token is acquired
           send_metrics("token.acquired", 1)
       
       def on_token_refreshed(self, event: TokenEvent) -> None:
           # Called when token is refreshed
           send_metrics("token.refreshed", 1)
       
       def on_token_expired(self, event: TokenEvent) -> None:
           # Called when token expires
           send_metrics("token.expired", 1)
       
       def on_token_failed(self, event: TokenEvent) -> None:
           # Called when token operation fails
           send_alert(f"Token error: {event.error}")

   session = CloudSession(
       api_id="...",
       password="...",
       lifecycle_hooks=MyHooks()
   )

Full Enterprise Setup
~~~~~~~~~~~~~~~~~~~~~~

Combine distributed storage and lifecycle hooks:

.. code-block:: python

   import redis
   from prometheus_client import start_http_server
   from hfortix_core.session import CloudSession
   from hfortix_core.session.storage_examples import RedisTokenStorage
   from hfortix_core.session.hooks_examples import PrometheusHooks

   # Metrics server
   start_http_server(8000)

   # Distributed storage
   r = redis.Redis(host='redis', port=6379)
   storage = RedisTokenStorage(r, namespace="prod")

   # Metrics collection
   hooks = PrometheusHooks(namespace="prod", service="gateway")

   # Enterprise-ready session
   session = CloudSession(
       api_id="...",
       password="...",
       token_storage=storage,      # Distributed caching
       lifecycle_hooks=hooks,      # Prometheus metrics
       auto_refresh=True           # Background refresh
   )

   # Benefits:
   # - Tokens shared across all servers (via Redis)
   # - Prometheus metrics at :8000/metrics
   # - Automatic token refresh
   # - High availability

API Reference
-------------

CloudSession Class
~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.session.CloudSession
   :members:
   :undoc-members:
   :show-inheritance:

TokenInfo Dataclass
~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.session.TokenInfo
   :members:
   :undoc-members:
   :show-inheritance:

Rate Limit Tracking
-------------------

CloudSession includes session-wide rate limit tracking:

.. code-block:: python

   with CloudSession(api_id="...", password="...") as session:
       fc = FortiCare(session=session)
       fz = FortiZTP(session=session)
       
       # Make some API calls
       fc.api.products.list.post()
       fz.devices.get()
       
       # Check session-wide stats (all services combined)
       session_status = session.get_rate_limit_status()
       print(f"Total calls: {session_status['calls_last_hour']}")

See Also
--------

* :doc:`ratelimit` - Rate limit tracking details
* FortiCare documentation
* FortiZTP documentation
