"""
Type definitions for HFortix SDK

Provides TypedDict definitions for API responses and common data structures.
These improve IDE autocomplete and type checking.
"""

from typing import Any, Literal, TypedDict

__all__ = [
    "APIResponse",
    "ListResponse",
    "ObjectResponse",
    "ErrorResponse",
    "ConnectionStats",
    "RequestInfo",
    "CircuitBreakerState",
]


class APIResponse(TypedDict, total=False):
    """
    Base API response structure from FortiOS

    Not all fields are present in every response. Use total=False to make
    all fields optional.
    """

    http_status: int
    results: Any  # Can be list, dict, or string depending on endpoint
    revision: str
    revision_changed: bool
    old_revision: str
    vdom: str
    path: str
    name: str
    status: str
    http_method: str
    serial: str
    version: str
    build: int


class ListResponse(TypedDict):
    """Response from list/get operations that return multiple items"""

    http_status: int
    results: list[dict[str, Any]]
    vdom: str
    path: str
    name: str
    status: str
    serial: str
    version: str
    build: int


class ObjectResponse(TypedDict):
    """Response from get operations that return a single item"""

    http_status: int
    results: dict[str, Any]  # Single object, not a list
    vdom: str
    path: str
    name: str
    status: str
    serial: str
    version: str
    build: int


class ErrorResponse(TypedDict):
    """Error response structure from FortiOS API"""

    http_status: int
    error: int
    errorcode: int
    message: str
    vdom: str


CircuitBreakerState = Literal["closed", "open", "half-open"]
"""Circuit breaker state: closed (normal), open (failing), half-open (testing)"""  # noqa: E501


class ConnectionStats(TypedDict):
    """
    Connection pool statistics

    Returned by HTTPClient.get_connection_stats()
    """

    http2_enabled: bool
    max_connections: int
    max_keepalive_connections: int
    active_requests: int
    total_requests: int
    pool_exhaustion_count: int
    circuit_breaker_state: CircuitBreakerState
    consecutive_failures: int
    last_failure_time: float | None


class RequestInfo(TypedDict, total=False):
    """
    Information about a request (for debugging)

    Returned by HTTPClient.inspect_last_request()
    """

    method: str
    endpoint: str
    params: dict[str, Any] | None
    data: dict[str, Any] | None
    response_time_ms: float | None
    status_code: int | None
    timestamp: float
    error: str
