"""
Token Lifecycle Hooks for CloudSession

Defines protocols and types for token lifecycle event callbacks.
Enables monitoring, metrics, custom caching, and debugging of token operations.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable, Any, Callable, Optional
from dataclasses import dataclass

__all__ = [
    "TokenLifecycleHooks",
    "TokenAcquiredCallback",
    "TokenRefreshedCallback",
    "TokenExpiredCallback",
    "TokenFailedCallback",
    "TokenEvent",
]


@dataclass
class TokenEvent:
    """
    Token lifecycle event data.
    
    Passed to lifecycle hook callbacks with context about the event.
    """
    client_id: str
    timestamp: float  # Unix timestamp
    event_type: str  # "acquired", "refreshed", "expired", "failed"
    
    # Token data (if available)
    access_token: Optional[str] = None  # Truncated for security
    expires_in: Optional[int] = None
    token_type: Optional[str] = None
    scope: Optional[str] = None
    
    # Error data (for failed events)
    error: Optional[str] = None
    error_type: Optional[str] = None
    
    # Additional context
    is_auto_refresh: bool = False  # True if triggered by background thread
    retry_count: int = 0


# Type aliases for callback functions
TokenAcquiredCallback = Callable[[TokenEvent], None]
TokenRefreshedCallback = Callable[[TokenEvent], None]
TokenExpiredCallback = Callable[[str, float], None]  # client_id, timestamp
TokenFailedCallback = Callable[[TokenEvent], None]


@runtime_checkable
class TokenLifecycleHooks(Protocol):
    """
    Protocol for token lifecycle event hooks.
    
    Implement this protocol to receive callbacks for token lifecycle events.
    Useful for monitoring, metrics collection, custom caching, and debugging.
    
    Example - Metrics Collection:
        >>> import time
        >>> from prometheus_client import Counter, Gauge
        >>> 
        >>> class TokenMetricsHooks:
        ...     def __init__(self):
        ...         self.acquired = Counter('tokens_acquired', 'Tokens acquired', ['client_id'])
        ...         self.refreshed = Counter('tokens_refreshed', 'Tokens refreshed', ['client_id'])
        ...         self.failed = Counter('tokens_failed', 'Token failures', ['client_id', 'error'])
        ...         self.ttl = Gauge('token_ttl_seconds', 'Token TTL', ['client_id'])
        ...     
        ...     def on_token_acquired(self, event: TokenEvent) -> None:
        ...         self.acquired.labels(client_id=event.client_id).inc()
        ...         if event.expires_in:
        ...             self.ttl.labels(client_id=event.client_id).set(event.expires_in)
        ...     
        ...     def on_token_refreshed(self, event: TokenEvent) -> None:
        ...         self.refreshed.labels(client_id=event.client_id).inc()
        ...         if event.expires_in:
        ...             self.ttl.labels(client_id=event.client_id).set(event.expires_in)
        ...     
        ...     def on_token_failed(self, event: TokenEvent) -> None:
        ...         error = event.error_type or 'unknown'
        ...         self.failed.labels(client_id=event.client_id, error=error).inc()
        >>> 
        >>> hooks = TokenMetricsHooks()
        >>> session = CloudSession(
        ...     api_id="...", password="...",
        ...     lifecycle_hooks=hooks
        ... )
    
    Example - Custom Token Cache:
        >>> import redis
        >>> 
        >>> class RedisCacheHooks:
        ...     def __init__(self, redis_client):
        ...         self.redis = redis_client
        ...     
        ...     def on_token_acquired(self, event: TokenEvent) -> None:
        ...         # Cache token in Redis for distributed access
        ...         key = f"token:{event.client_id}"
        ...         if event.access_token and event.expires_in:
        ...             self.redis.setex(key, event.expires_in, event.access_token)
        ...     
        ...     def on_token_refreshed(self, event: TokenEvent) -> None:
        ...         # Update cache with new token
        ...         key = f"token:{event.client_id}"
        ...         if event.access_token and event.expires_in:
        ...             self.redis.setex(key, event.expires_in, event.access_token)
    
    Thread Safety:
        - Hooks may be called from background refresh thread
        - Implementations must be thread-safe
        - Exceptions in hooks are caught and logged (won't break CloudSession)
    
    Performance:
        - Keep hooks lightweight - they run in token acquisition path
        - Use async/background processing for expensive operations
        - Don't block on I/O in hooks
    """
    
    def on_token_acquired(self, event: TokenEvent) -> None:
        """
        Called when a new token is acquired via password grant.
        
        Args:
            event: Token event with acquisition details
        
        Note:
            - event.access_token is truncated for security (first 30 chars)
            - Use this for metrics, logging, or custom caching
            - Exceptions are caught and logged
        """
        ...
    
    def on_token_refreshed(self, event: TokenEvent) -> None:
        """
        Called when a token is refreshed via refresh_token grant.
        
        Args:
            event: Token event with refresh details
        
        Note:
            - event.is_auto_refresh indicates background refresh
            - Use this for metrics, logging, or cache updates
            - Exceptions are caught and logged
        """
        ...
    
    def on_token_expired(self, client_id: str, timestamp: float) -> None:
        """
        Called when a token is detected as expired.
        
        Args:
            client_id: Client ID of expired token
            timestamp: Unix timestamp when expiration was detected
        
        Note:
            - Token will be automatically refreshed after this
            - Use this for alerts or metrics
            - Exceptions are caught and logged
        """
        ...
    
    def on_token_failed(self, event: TokenEvent) -> None:
        """
        Called when token acquisition or refresh fails.
        
        Args:
            event: Token event with failure details
        
        Note:
            - event.error contains error message
            - event.error_type contains exception class name
            - Use this for error tracking and alerting
            - Exceptions are caught and logged
        """
        ...


class SimpleLifecycleHooks:
    """
    Simple callback-based lifecycle hooks.
    
    Convenience class for using simple callback functions without
    implementing the full protocol.
    
    Example:
        >>> def log_acquisition(event: TokenEvent):
        ...     print(f"Token acquired for {event.client_id}, expires in {event.expires_in}s")
        >>> 
        >>> def log_refresh(event: TokenEvent):
        ...     print(f"Token refreshed for {event.client_id}")
        >>> 
        >>> hooks = SimpleLifecycleHooks(
        ...     on_acquired=log_acquisition,
        ...     on_refreshed=log_refresh
        ... )
        >>> 
        >>> session = CloudSession(
        ...     api_id="...", password="...",
        ...     lifecycle_hooks=hooks
        ... )
    """
    
    def __init__(
        self,
        on_acquired: Optional[TokenAcquiredCallback] = None,
        on_refreshed: Optional[TokenRefreshedCallback] = None,
        on_expired: Optional[TokenExpiredCallback] = None,
        on_failed: Optional[TokenFailedCallback] = None,
    ):
        """
        Initialize with optional callbacks.
        
        Args:
            on_acquired: Called when token is acquired
            on_refreshed: Called when token is refreshed
            on_expired: Called when token expires
            on_failed: Called when token operation fails
        """
        self._on_acquired = on_acquired
        self._on_refreshed = on_refreshed
        self._on_expired = on_expired
        self._on_failed = on_failed
    
    def on_token_acquired(self, event: TokenEvent) -> None:
        """Call on_acquired callback if set."""
        if self._on_acquired:
            self._on_acquired(event)
    
    def on_token_refreshed(self, event: TokenEvent) -> None:
        """Call on_refreshed callback if set."""
        if self._on_refreshed:
            self._on_refreshed(event)
    
    def on_token_expired(self, event: TokenEvent) -> None:
        """Call on_expired callback if set."""
        if self._on_expired:
            self._on_expired(event)
    
    def on_token_failed(self, event: TokenEvent) -> None:
        """Call on_failed callback if set."""
        if self._on_failed:
            self._on_failed(event)
