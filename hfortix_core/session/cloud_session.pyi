"""Type stubs for CloudSession."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from types import TracebackType

@dataclass
class TokenInfo:
    """OAuth token information for a specific client_id."""
    access_token: str
    refresh_token: str
    expires_in: int
    created_at: float
    scope: str = ...
    token_type: str = ...
    
    @property
    def expires_at(self) -> float: ...
    
    @property
    def time_remaining(self) -> float: ...
    
    @property
    def is_expired(self) -> bool: ...
    
    def is_expiring_soon(self, buffer_seconds: int = 300) -> bool: ...

class CloudSession:
    """Multi-service OAuth session manager for FortiCloud."""
    
    _check_before_request: bool
    _rate_limit: bool
    _rate_limit_strategy: str
    _rate_limit_max_requests: int
    _rate_limit_window_seconds: float
    _rate_limit_queue_size: int
    _rate_limit_queue_timeout: float
    _rate_limit_queue_overflow: str
    _circuit_breaker: bool
    _circuit_breaker_threshold: int
    _circuit_breaker_timeout: float
    _circuit_breaker_half_open_calls: int
    
    def __init__(
        self,
        api_id: str,
        password: str,
        auto_refresh: bool = False,
        refresh_buffer_seconds: int = 300,
        refresh_check_interval: int | bool | None = 60,
        check_before_request: bool = True,
        auth_url: str = "https://customerapiauth.fortinet.com/api/v1/oauth/token/",
        default_expires_in: int | None = None,
        token_storage: Any = None,
        lifecycle_hooks: Any = None,
        # Global rate limiting for all clients using this session
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        circuit_breaker_half_open_calls: int = 3,
    ) -> None: ...
    
    def __enter__(self) -> CloudSession: ...
    
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None: ...
    
    def get_token(self, client_id: str) -> str: ...
    
    def authenticate(self, client_id: str) -> dict[str, Any]: ...
    
    def refresh_token(self, client_id: str) -> dict[str, Any]: ...
    
    def is_token_expired(self, client_id: str, buffer_seconds: int = 0) -> bool: ...
    
    def ensure_token_valid(self, client_id: str, buffer_seconds: int | None = None) -> str: ...
    
    def get_token_info(self, client_id: str) -> dict[str, Any] | None: ...
    
    def get_all_tokens(self) -> dict[str, dict[str, Any]]: ...
    
    def clear_token(self, client_id: str) -> None: ...
    
    def clear_all_tokens(self) -> None: ...
    
    def close(self) -> None: ...
    
    def __repr__(self) -> str: ...
