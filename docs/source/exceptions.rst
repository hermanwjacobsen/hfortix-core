Exceptions
==========

Exception Hierarchy
-------------------

All HFortix-Core exceptions inherit from ``FortinetError``:

.. code-block:: text

   FortinetError
   ├── AuthenticationError          (HTTP 401)
   ├── AuthorizationError           (HTTP 403)
   ├── ValidationError
   ├── ConfigurationError
   ├── VDOMError
   ├── OperationNotSupportedError
   ├── ReadOnlyModeError
   ├── CircuitBreakerError
   │   └── CircuitBreakerTimeoutError
   └── APIError
       ├── RetryableError
       │   ├── RateLimitError                  (HTTP 429)
       │   │   ├── RateLimitExceededError
       │   │   ├── RateLimitQueueFullError
       │   │   └── RateLimitQueueTimeoutError
       │   ├── ServerError                     (HTTP 500)
       │   ├── ServiceUnavailableError         (HTTP 503)
       │   ├── CircuitBreakerOpenError
       │   └── TimeoutError
       └── NonRetryableError
           ├── BadRequestError                 (HTTP 400)
           ├── ResourceNotFoundError           (HTTP 404)
           ├── MethodNotAllowedError           (HTTP 405)
           ├── DuplicateEntryError             (error code -5, ...)
           ├── EntryInUseError                 (error code -23, ...)
           ├── InvalidValueError               (error code -651, ...)
           └── PermissionDeniedError           (error code -14, -37)

.. warning::

   ``AuthenticationError`` and ``AuthorizationError`` inherit directly from
   ``FortinetError`` — **not** from ``APIError``. An ``except APIError:``
   handler will *not* catch authentication/authorization failures; catch
   them explicitly or use ``except FortinetError:``.

All exceptions expose a ``message`` property that returns the original error
message without the extra context that ``str(exception)`` may include:

.. code-block:: python

   from hfortix_core import APIError

   try:
       ...
   except APIError as e:
       print(e.message)      # original message only
       print(e)              # message plus endpoint/status/hint context

Base Exception
--------------

.. autoexception:: hfortix_core.FortinetError
   :members:
   :show-inheritance:

API Exceptions
--------------

.. autoexception:: hfortix_core.APIError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.BadRequestError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.AuthenticationError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.AuthorizationError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.PermissionDeniedError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.ResourceNotFoundError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.MethodNotAllowedError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.DuplicateEntryError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.EntryInUseError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.InvalidValueError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.RateLimitError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.exceptions.RateLimitExceededError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.exceptions.RateLimitQueueFullError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.exceptions.RateLimitQueueTimeoutError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.ServerError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.ServiceUnavailableError
   :members:
   :show-inheritance:

Configuration & Operation Exceptions
-------------------------------------

.. autoexception:: hfortix_core.ValidationError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.ConfigurationError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.VDOMError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.OperationNotSupportedError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.ReadOnlyModeError
   :members:
   :show-inheritance:

Retry & Circuit Breaker Exceptions
-----------------------------------

.. autoexception:: hfortix_core.RetryableError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.NonRetryableError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.CircuitBreakerOpenError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.exceptions.CircuitBreakerError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.exceptions.CircuitBreakerTimeoutError
   :members:
   :show-inheritance:

.. autoexception:: hfortix_core.TimeoutError
   :members:
   :show-inheritance:

Helper Functions
----------------

These helpers live in the ``hfortix_core.exceptions`` module:

.. autofunction:: hfortix_core.exceptions.raise_for_status

.. autofunction:: hfortix_core.exceptions.is_retryable_error

.. autofunction:: hfortix_core.exceptions.get_retry_delay

.. autofunction:: hfortix_core.exceptions.get_error_description

.. autofunction:: hfortix_core.exceptions.get_http_status_description
