Exceptions
==========

Exception Hierarchy
-------------------

All HFortix-Core exceptions inherit from ``FortinetError``:

.. code-block:: text

   FortinetError
   ├── APIError
   │   ├── BadRequestError
   │   ├── AuthenticationError
   │   ├── AuthorizationError
   │   ├── PermissionDeniedError
   │   ├── ResourceNotFoundError
   │   ├── MethodNotAllowedError
   │   ├── DuplicateEntryError
   │   ├── EntryInUseError
   │   ├── InvalidValueError
   │   ├── RateLimitError
   │   ├── ServerError
   │   └── ServiceUnavailableError
   ├── ValidationError
   ├── ConfigurationError
   ├── VDOMError
   ├── OperationNotSupportedError
   ├── ReadOnlyModeError
   ├── RetryableError
   ├── NonRetryableError
   ├── CircuitBreakerOpenError
   └── TimeoutError

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

.. autoexception:: hfortix_core.TimeoutError
   :members:
   :show-inheritance:
