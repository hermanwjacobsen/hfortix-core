"""
HFortix Core - Shared foundation for Fortinet SDKs

Provides:
- Common exception hierarchy
- HTTP client framework (sync and async)
- Shared utilities and type definitions
"""

from .exceptions import (
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    CircuitBreakerOpenError,
    ConfigurationError,
    DuplicateEntryError,
    EntryInUseError,
    FortinetError,
    InvalidValueError,
    MethodNotAllowedError,
    NonRetryableError,
    OperationNotSupportedError,
    PermissionDeniedError,
    RateLimitError,
    ReadOnlyModeError,
    ResourceNotFoundError,
    RetryableError,
    ServerError,
    ServiceUnavailableError,
    TimeoutError,
    VDOMError,
)
from .types import (
    APIResponse,
    CircuitBreakerState,
    ConnectionStats,
    ErrorResponse,
    ListResponse,
    ObjectResponse,
    RequestInfo,
)
from .logging import (
    RequestLogger,
    log_operation,
    StructuredFormatter,
    TextFormatter,
)
from .debug import (
    DebugSession,
    debug_timer,
    format_connection_stats,
    format_request_info,
    print_debug_info,
)

__version__ = "0.4.0"
__all__ = [
    # Exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
    "RetryableError",
    "NonRetryableError",
    "ConfigurationError",
    "VDOMError",
    "OperationNotSupportedError",
    "ReadOnlyModeError",
    "BadRequestError",
    "ResourceNotFoundError",
    "MethodNotAllowedError",
    "RateLimitError",
    "ServerError",
    "ServiceUnavailableError",
    "CircuitBreakerOpenError",
    "TimeoutError",
    "DuplicateEntryError",
    "EntryInUseError",
    "InvalidValueError",
    "PermissionDeniedError",
    # Type definitions
    "APIResponse",
    "ListResponse",
    "ObjectResponse",
    "ErrorResponse",
    "ConnectionStats",
    "RequestInfo",
    "CircuitBreakerState",
    # Logging utilities
    "RequestLogger",
    "log_operation",
    "StructuredFormatter",
    "TextFormatter",
    # Debug utilities
    "DebugSession",
    "debug_timer",
    "format_connection_stats",
    "format_request_info",
    "print_debug_info",
]
