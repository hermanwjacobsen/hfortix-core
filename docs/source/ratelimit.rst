Rate Limit Tracking
===================

Overview
--------

The rate limit tracking system provides visibility into API call patterns across multiple time windows. It's designed for **monitoring only** - no enforcement is performed.

Key Features
------------

* **Multiple time windows**: Tracks last minute, last 5 minutes, and last hour
* **Separate tracking**: Tracks calls and errors independently
* **Configurable limits**: Set custom limits or leave as ``None``
* **Efficient implementation**: Uses ``deque`` with ``maxlen`` for memory efficiency
* **Per-client tracking**: Each service instance has its own ``RateLimitStats``
* **Session-wide tracking**: CloudSession tracks all calls across all services
* **No enforcement**: Informational only - does not block requests

Time Windows
------------

The system tracks statistics across three time windows:

* **Last minute** (60 seconds): Short-term rate monitoring
* **Last 5 minutes** (300 seconds): Medium-term trends
* **Last hour** (3600 seconds): Long-term usage patterns

Both calls and errors are tracked separately for each window.

Basic Usage
-----------

FortiCare Example
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_forticare import FortiCare

   # Configure custom limits (all optional, defaults to None)
   fc = FortiCare(
       api_id="...",
       password="...",
       rate_limit_calls_per_min=100,      # 100 calls per minute
       rate_limit_calls_per_5min=500,     # 500 calls per 5 minutes
       rate_limit_calls_per_hour=1000,    # 1000 calls per hour
       rate_limit_errors_per_hour=10      # 10 errors per hour
   )

   # Make API calls
   products = fc.api.products.list.post()

   # Check rate limit status
   status = fc.get_rate_limit_status()
   print(f"Calls last min: {status['calls_last_min']}/{status['limits']['calls_per_min']}")
   print(f"Calls last 5min: {status['calls_last_5min']}/{status['limits']['calls_per_5min']}")
   print(f"Calls last hour: {status['calls_last_hour']}/{status['limits']['calls_per_hour']}")
   print(f"Within limits: {status['within_limits']}")

FortiZTP Example
~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_fortiztp import FortiZTP

   # FortiZTP: 2000 calls per hour limit
   client = FortiZTP(
       api_id="...",
       password="...",
       rate_limit_calls_per_hour=2000
   )

   # Check status
   status = client.get_rate_limit_status()

Session-Wide Tracking
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hfortix_core.session import CloudSession
   from hfortix_forticare import FortiCare
   from hfortix_fortiztp import FortiZTP

   with CloudSession(api_id="...", password="...") as session:
       fc = FortiCare(session=session)
       fz = FortiZTP(session=session)
       
       # Check per-client stats
       fc_status = fc.get_rate_limit_status()
       fz_status = fz.get_rate_limit_status()
       
       # Check session-wide stats (all services combined)
       session_status = session.get_rate_limit_status()
       print(f"Total calls (all services): {session_status['calls_last_hour']}")

Status Response Format
----------------------

The ``get_rate_limit_status()`` method returns:

.. code-block:: python

   {
       "calls_last_min": 45,       # Calls in last 60 seconds
       "calls_last_5min": 180,     # Calls in last 300 seconds
       "calls_last_hour": 523,     # Calls in last 3600 seconds
       "errors_last_min": 0,       # Errors in last 60 seconds
       "errors_last_5min": 1,      # Errors in last 300 seconds
       "errors_last_hour": 2,      # Errors in last 3600 seconds
       "total_calls": 1247,        # Total since client creation
       "total_errors": 5,          # Total errors since creation
       "limits": {                 # Configured limits
           "calls_per_min": 100,
           "calls_per_5min": 500,
           "calls_per_hour": 1000,
           "errors_per_min": None,
           "errors_per_5min": None,
           "errors_per_hour": 10
       },
       "within_limits": True       # Whether within all set limits
   }

Known API Rate Limits
---------------------

FortiCare Asset Management
~~~~~~~~~~~~~~~~~~~~~~~~~~

* **100 calls per minute**
* **1000 calls per hour**
* **10 errors per hour**
* **Batch operations**: Max 10 units, max 5 errors per batch

FortiZTP
~~~~~~~~

* **2000 calls per hour**

FortiGateCloud
~~~~~~~~~~~~~~

* **100 calls per second**
* **15 errors per minute**

API Reference
-------------

RateLimitStats Class
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: hfortix_core.ratelimit.RateLimitStats
   :members:
   :undoc-members:
   :show-inheritance:

Implementation Details
----------------------

Sliding Window Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~

The system uses ``collections.deque`` with ``maxlen`` to implement efficient sliding windows:

1. Each call/error timestamp is appended to the deque
2. When checking status, timestamps are filtered by time window
3. Old timestamps beyond the window are automatically dropped
4. Memory usage is bounded by ``maxlen``

Thread Safety
~~~~~~~~~~~~~

* ``RateLimitStats`` is **not thread-safe** by itself
* CloudSession uses internal locking for thread-safe access
* Per-client stats don't require locking (single-threaded client usage assumed)

Future Enhancements
-------------------

Planned features for future releases:

* **Enforcement mode**: Optionally block requests when limits exceeded
* **Adaptive throttling**: Automatically slow down when approaching limits
* **Metrics export**: Export statistics to Prometheus, CloudWatch, etc.
* **Historical tracking**: Store and analyze rate limit trends over time

See Also
--------

* :doc:`session` - CloudSession documentation
* FortiCare API documentation
* FortiZTP API documentation
