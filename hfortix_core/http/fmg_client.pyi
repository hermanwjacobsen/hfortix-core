"""Type stubs for FortiManager HTTP Client."""

from typing import Any, Literal, Optional

from .base import BaseHTTPClient


class HTTPClientFMG(BaseHTTPClient):
    """
    HTTP client for FortiManager JSON-RPC API.
    
    Provides session-based authentication and JSON-RPC request handling
    while reusing the retry logic, circuit breaker, connection pooling,
    and statistics from BaseHTTPClient.
    """
    
    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        verify: bool = True,
        adom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
        read_only: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
        rate_limit_calls_per_min: Optional[int] = None,
        rate_limit_calls_per_5min: Optional[int] = None,
        rate_limit_calls_per_hour: Optional[int] = None,
        rate_limit_errors_per_min: Optional[int] = None,
        rate_limit_errors_per_5min: Optional[int] = None,
        rate_limit_errors_per_hour: Optional[int] = None,
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_half_open_calls: int = 3,
    ) -> None: ...
    
    @property
    def jsonrpc_url(self) -> str: ...
    
    @property
    def is_authenticated(self) -> bool: ...
    
    @property
    def adom(self) -> str | None: ...
    
    def login(self) -> dict[str, Any]: ...
    
    def logout(self) -> dict[str, Any]: ...
    
    def execute(
        self,
        method: Literal["exec", "get", "set", "add", "update", "delete"],
        params: list[dict[str, Any]],
        verbose: int = 1,
    ) -> dict[str, Any]: ...
    
    def proxy_request(
        self,
        action: Literal["get", "post", "put", "delete"],
        resource: str,
        targets: list[str],
        payload: dict[str, Any] | None = None,
        timeout: int = 60,
    ) -> dict[str, Any]: ...
    
    def close(self) -> None: ...
    
    def get_health_metrics(self) -> dict[str, Any]: ...
    
    def get_connection_stats(self) -> dict[str, Any]: ...
    
    def __enter__(self) -> "HTTPClientFMG": ...
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
