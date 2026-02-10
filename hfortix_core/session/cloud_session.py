"""
CloudSession - Multi-service OAuth token manager for FortiCloud.

Manages OAuth tokens for multiple FortiCloud services (FortiCare, FortiZTP, etc.)
with automatic token caching, refresh, and lifecycle management.
"""

from __future__ import annotations

import logging
import time
import threading
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
from types import TracebackType

import httpx

from ..ratelimit import RateLimitStats
from .token_storage import TokenStorage, InMemoryTokenStorage, TokenData
from .lifecycle_hooks import TokenLifecycleHooks, TokenEvent

logger = logging.getLogger("hfortix.session.cloud")


@dataclass
class TokenInfo:
    """OAuth token information for a specific client_id."""
    
    access_token: str
    refresh_token: str
    expires_in: int  # Seconds until expiration
    created_at: float  # Unix timestamp
    scope: str = "read write"
    token_type: str = "Bearer"
    
    @property
    def expires_at(self) -> float:
        """Unix timestamp when token expires."""
        return self.created_at + self.expires_in
    
    @property
    def time_remaining(self) -> float:
        """Seconds remaining until token expires."""
        return max(0.0, self.expires_at - time.time())
    
    @property
    def is_expired(self) -> bool:
        """Whether token has expired."""
        return time.time() >= self.expires_at
    
    def is_expiring_soon(self, buffer_seconds: int = 300) -> bool:
        """Whether token will expire within buffer_seconds."""
        return self.time_remaining <= buffer_seconds


class CloudSession:
    """
    Multi-service OAuth session manager for FortiCloud.
    
    Manages authentication tokens for multiple FortiCloud services (FortiCare,
    FortiZTP, FortiFlex, etc.) with automatic caching, refresh, and lifecycle
    management. Each service uses a different client_id and requires a separate
    token.
    
    Usage:
        Simple case (auto-detect client_id):
            with CloudSession(api_id="...", password="...") as session:
                fc = FortiCare(session=session)  # Auto uses "assetmanagement"
                fz = FortiZTP(session=session)   # Auto uses "fortiztp"
        
        Advanced case (override client_id):
            with CloudSession(api_id="...", password="...") as session:
                fc = FortiCare(session=session, client_id="assetmanagement")
                fc_elite = FortiCare(session=session, client_id="fcelite")
                # Session manages 2 separate tokens
        
        With auto-refresh:
            session = CloudSession(
                api_id="...",
                password="...",
                auto_refresh=True,
                refresh_buffer_seconds=300
            )
            fc = FortiCare(session=session)
            # Token automatically refreshes in background when 5 min from expiring
    """
    
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
        token_storage: Optional[TokenStorage] = None,
        lifecycle_hooks: Optional[TokenLifecycleHooks] = None,
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
    ):
        """
        Initialize CloudSession.
        
        Args:
            api_id: FortiCloud API ID / username
            password: FortiCloud API password
            auto_refresh: Enable background token refresh (default: False)
            refresh_buffer_seconds: Refresh tokens this many seconds before expiry (default: 300)
            refresh_check_interval: How often to check for expiring tokens (default: 60)
                                   - Integer > 0: Check interval in seconds (e.g., 30, 60, 120)
                                   - 0, None, or False: Disable background checks
                                   - True: Use default interval (60 seconds)
            check_before_request: Check and refresh token before each HTTP request (default: True)
                                 Set to False to disable pre-request checks (not recommended)
            auth_url: OAuth token endpoint URL
            default_expires_in: Override expires_in from OAuth response (default: None = use response value)
                               Set this if you want to force a specific expiration time (in seconds)
            token_storage: Custom token storage backend (default: InMemoryTokenStorage)
                          Implement TokenStorage protocol for Redis, Memcached, etc.
            lifecycle_hooks: Token lifecycle event hooks for monitoring/metrics
                            Implement TokenLifecycleHooks protocol for callbacks
            
            # Global Rate Limiting (applies to ALL clients using this session)
            rate_limit: Enable rate limiting enforcement (default: False)
            rate_limit_strategy: 'queue' or 'reject' (default: 'queue')
            rate_limit_max_requests: Max requests per window (default: 100)
            rate_limit_window_seconds: Time window in seconds (default: 60.0)
            rate_limit_queue_size: Max queue size (default: 100)
            rate_limit_queue_timeout: Max wait time in queue seconds (default: 30.0)
            rate_limit_queue_overflow: 'block' or 'drop' on overflow (default: 'block')
            circuit_breaker: Enable circuit breaker (default: False)
            circuit_breaker_threshold: Failures before opening (default: 5)
            circuit_breaker_timeout: Seconds before retry (default: 60.0)
            circuit_breaker_half_open_calls: Calls to test in half-open state (default: 3)
        
        Example - With Custom Storage:
            >>> from hfortix_core.session import CloudSession
            >>> from my_storage import RedisTokenStorage
            >>> 
            >>> storage = RedisTokenStorage(redis_url="redis://localhost:6379")
            >>> session = CloudSession(
            ...     api_id="...", password="...",
            ...     token_storage=storage  # Tokens shared across processes
            ... )
        
        Example - With Lifecycle Hooks:
            >>> from hfortix_core.session import CloudSession, SimpleLifecycleHooks
            >>> 
            >>> def on_acquired(event):
            ...     print(f"Token acquired for {event.client_id}, expires in {event.expires_in}s")
            >>> 
            >>> hooks = SimpleLifecycleHooks(on_acquired=on_acquired)
            >>> session = CloudSession(
            ...     api_id="...", password="...",
            ...     lifecycle_hooks=hooks
            ... )
        
        Example - With Global Rate Limiting:
            >>> # All clients using this session will respect rate limits
            >>> session = CloudSession(
            ...     api_id="...", password="...",
            ...     rate_limit=True,
            ...     rate_limit_max_requests=10,
            ...     rate_limit_window_seconds=60.0,
            ... )
            >>> fc = FortiCare(session=session)  # Inherits rate limiting from session
            >>> fz = FortiZTP(session=session)   # Also inherits rate limiting
            >>> # Both clients share the same rate limiter (10 req/min total across both)
        """
        self._api_id = api_id
        self._password = password
        self._auth_url = auth_url
        self._auto_refresh = auto_refresh
        self._refresh_buffer = refresh_buffer_seconds
        
        # Normalize refresh_check_interval
        if refresh_check_interval is True:
            self._refresh_check_interval = 60  # Default
        elif refresh_check_interval is False or refresh_check_interval is None or refresh_check_interval == 0:
            self._refresh_check_interval = 0  # Disabled
        else:
            self._refresh_check_interval = int(refresh_check_interval)  # Custom interval
        
        self._check_before_request = check_before_request
        self._default_expires_in = default_expires_in
        
        # Token storage backend (pluggable)
        self._storage = token_storage if token_storage is not None else InMemoryTokenStorage()
        
        # Lifecycle hooks for monitoring/metrics
        self._lifecycle_hooks = lifecycle_hooks
        
        # Store global rate limiting parameters (can be overridden by individual clients)
        self._rate_limit = rate_limit
        self._rate_limit_strategy = rate_limit_strategy
        self._rate_limit_max_requests = rate_limit_max_requests
        self._rate_limit_window_seconds = rate_limit_window_seconds
        self._rate_limit_queue_size = rate_limit_queue_size
        self._rate_limit_queue_timeout = rate_limit_queue_timeout
        self._rate_limit_queue_overflow = rate_limit_queue_overflow
        self._circuit_breaker = circuit_breaker
        self._circuit_breaker_threshold = circuit_breaker_threshold
        self._circuit_breaker_timeout = circuit_breaker_timeout
        self._circuit_breaker_half_open_calls = circuit_breaker_half_open_calls
        
        # Internal token cache for fast access (TokenInfo objects)
        # Storage backend uses TokenData (serializable), cache uses TokenInfo (rich objects)
        self._tokens: dict[str, TokenInfo] = {}
        self._lock = threading.Lock()
        
        # Rate limit tracking across all services using this session
        # Tracks all API calls across all client_ids
        # Set to None by default - configure as needed
        self._rate_stats = RateLimitStats(
            calls_per_min=None,
            calls_per_5min=None,
            calls_per_hour=None,
            errors_per_min=None,
            errors_per_5min=None,
            errors_per_hour=None,
        )
        
        # Background refresh thread
        self._refresh_thread: threading.Thread | None = None
        self._stop_refresh = threading.Event()
        
        logger.debug(
            f"CloudSession initialized: api_id={api_id[:10] if api_id else 'None'}..., "
            f"auto_refresh={auto_refresh}, refresh_buffer={refresh_buffer_seconds}s, "
            f"check_interval={self._refresh_check_interval}s, check_before_request={check_before_request}"
        )
        
        # Start auto-refresh if enabled
        if auto_refresh:
            self._start_auto_refresh()
            logger.info(f"Auto-refresh enabled: checking every {self._refresh_check_interval}s, refresh buffer {refresh_buffer_seconds}s")
    
    def __enter__(self) -> CloudSession:
        """Context manager entry."""
        return self
    
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        """Context manager exit - cleanup resources."""
        self.close()
    
    def get_token(self, client_id: str) -> str:
        """
        Get access token for a specific client_id.
        
        Acquires new token if not cached, refreshes if expired.
        Thread-safe.
        
        Args:
            client_id: FortiCloud service client_id (e.g., "assetmanagement", "fortiztp")
        
        Returns:
            OAuth access token string
        """
        # Record API call for rate limiting
        self._rate_stats.record_call()
        
        with self._lock:
            # Check internal cache first
            if client_id not in self._tokens:
                # Try loading from storage backend
                token_data = self._storage.get(client_id)
                if token_data:
                    # Found in storage, load into cache
                    token_info = TokenInfo(
                        access_token=token_data.access_token,
                        refresh_token=token_data.refresh_token,
                        expires_in=token_data.expires_in,
                        created_at=token_data.created_at,
                        scope=token_data.scope,
                        token_type=token_data.token_type,
                    )
                    self._tokens[client_id] = token_info
                    logger.debug(f"Loaded token for client_id='{client_id}' from storage backend")
            
            # Get or create token
            if client_id not in self._tokens:
                logger.debug(f"No cached token for client_id='{client_id}', acquiring new token")
                self._acquire_token(client_id)
            elif self._tokens[client_id].is_expired:
                logger.debug(f"Token expired for client_id='{client_id}', refreshing")
                
                # Call expired hook
                if self._lifecycle_hooks:
                    try:
                        self._lifecycle_hooks.on_token_expired(client_id, time.time())
                    except Exception as e:
                        logger.warning(f"Lifecycle hook on_token_expired failed: {e}")
                
                self._refresh_token(client_id)
            else:
                time_remaining = self._tokens[client_id].time_remaining
                logger.debug(f"Using cached token for client_id='{client_id}' (expires in {time_remaining:.0f}s)")
            
            return self._tokens[client_id].access_token
    
    def authenticate(self, client_id: str) -> dict[str, Any]:
        """
        Pre-authenticate for a service (get token now).
        
        Useful for:
        - Getting auth errors early (fail fast)
        - Pre-loading tokens for faster API calls
        
        Args:
            client_id: FortiCloud service client_id
        
        Returns:
            Full OAuth response dict with access_token, refresh_token, etc.
        """
        with self._lock:
            return self._acquire_token(client_id)
    
    def refresh_token(self, client_id: str) -> dict[str, Any]:
        """
        Manually refresh token for a specific client_id.
        
        Args:
            client_id: FortiCloud service client_id
        
        Returns:
            Full OAuth response dict
        """
        with self._lock:
            return self._refresh_token(client_id)
    
    def is_token_expired(self, client_id: str, buffer_seconds: int = 0) -> bool:
        """
        Check if token is expired or will expire within buffer.
        
        Args:
            client_id: FortiCloud service client_id
            buffer_seconds: Consider token expired this many seconds early
        
        Returns:
            True if token is expired or expiring soon
        """
        with self._lock:
            if client_id not in self._tokens:
                return True
            
            if buffer_seconds > 0:
                return self._tokens[client_id].is_expiring_soon(buffer_seconds)
            else:
                return self._tokens[client_id].is_expired
    
    def ensure_token_valid(self, client_id: str, buffer_seconds: int | None = None) -> str:
        """
        Ensure token is valid and refresh if needed before making a request.
        
        This is useful to call before each API request to guarantee a fresh token.
        Automatically uses the session's refresh_buffer_seconds if not specified.
        
        Args:
            client_id: FortiCloud service client_id
            buffer_seconds: Custom buffer for expiration check (default: use session's refresh_buffer)
        
        Returns:
            Valid access token
        
        Raises:
            Exception: If unable to get/refresh token
        """
        buffer = buffer_seconds if buffer_seconds is not None else self._refresh_buffer
        
        with self._lock:
            # Check if token exists and is still valid
            if client_id in self._tokens:
                token = self._tokens[client_id]
                
                # If token is expiring soon, refresh it
                if token.is_expiring_soon(buffer):
                    logger.debug(
                        f"Token expiring soon for client_id='{client_id}' "
                        f"(expires in {token.time_remaining:.0f}s, buffer={buffer}s), refreshing"
                    )
                    try:
                        self._refresh_token(client_id)
                    except Exception as e:
                        logger.warning(f"Token refresh failed for client_id='{client_id}': {e}, acquiring new token")
                        # If refresh fails, try acquiring new token
                        self._acquire_token(client_id)
                else:
                    logger.debug(f"Token valid for client_id='{client_id}' (expires in {token.time_remaining:.0f}s)")
                
                return self._tokens[client_id].access_token
            else:
                # No token exists, acquire new one
                logger.debug(f"No token exists for client_id='{client_id}', acquiring new token")
                self._acquire_token(client_id)
                return self._tokens[client_id].access_token
    
    def get_token_info(self, client_id: str) -> dict[str, Any] | None:
        """
        Get detailed token information for debugging.
        
        Args:
            client_id: FortiCloud service client_id
        
        Returns:
            Dict with token metadata or None if token doesn't exist
        """
        # Internal version without lock (for use within locked context)
        return self._get_token_info_unlocked(client_id)
    
    def _get_token_info_unlocked(self, client_id: str) -> dict[str, Any] | None:
        """Get token info without acquiring lock (internal use only)."""
        if client_id not in self._tokens:
            return None
        
        token = self._tokens[client_id]
        return {
            "client_id": client_id,
            "access_token": token.access_token[:30] + "...",  # Truncated for security
            "token_type": token.token_type,
            "scope": token.scope,
            "expires_in": token.expires_in,
            "created_at": token.created_at,
            "created_at_iso": datetime.fromtimestamp(token.created_at).isoformat(),
            "expires_at": token.expires_at,
            "expires_at_iso": datetime.fromtimestamp(token.expires_at).isoformat(),
            "time_remaining": token.time_remaining,
            "is_expired": token.is_expired,
            "expires_soon": token.is_expiring_soon(self._refresh_buffer)
        }
    
    def get_all_tokens(self) -> dict[str, dict[str, Any]]:
        """
        Get information about all managed tokens.
        
        Returns:
            Dict mapping client_id to token info
        """
        with self._lock:
            result: dict[str, dict[str, Any]] = {}
            for client_id in self._tokens:
                info = self._get_token_info_unlocked(client_id)
                if info is not None:
                    result[client_id] = info
            return result
    
    def clear_token(self, client_id: str) -> None:
        """
        Remove cached token for a client_id (force re-authentication).
        
        Args:
            client_id: FortiCloud service client_id
        """
        with self._lock:
            if client_id in self._tokens:
                del self._tokens[client_id]
            self._storage.delete(client_id)
            logger.info(f"Cleared cached token for client_id='{client_id}'")
    
    def clear_all_tokens(self) -> None:
        """Remove all cached tokens."""
        with self._lock:
            token_count = len(self._tokens)
            self._tokens.clear()
            self._storage.clear()
            logger.info(f"Cleared all cached tokens ({token_count} token(s) removed)")
    
    def get_rate_limit_status(self) -> dict[str, Any]:
        """
        Get rate limit status for this session.
        
        Returns statistics about API calls and errors across all services
        using this session.
        
        Returns:
            Dict with rate limit information including calls/errors per minute/hour
        
        Example:
            >>> session = CloudSession(api_id="...", password="...")
            >>> status = session.get_rate_limit_status()
            >>> print(f"Calls last hour: {status['calls_last_hour']}")
        """
        return self._rate_stats.get_status()
    
    def close(self) -> None:
        """Stop background refresh and cleanup resources."""
        if self._refresh_thread and self._refresh_thread.is_alive():
            logger.debug("Stopping auto-refresh thread")
            self._stop_refresh.set()
            self._refresh_thread.join(timeout=2.0)
        logger.debug(f"CloudSession closed (managed {len(self._tokens)} token(s))")
    
    def _acquire_token(self, client_id: str, is_auto_refresh: bool = False) -> dict[str, Any]:
        """
        Acquire new token via OAuth password grant.
        
        NOT thread-safe - caller must hold self._lock.
        
        Args:
            client_id: FortiCloud service client_id
            is_auto_refresh: Whether this is triggered by auto-refresh thread
        
        Returns:
            Full OAuth response dict
        """
        logger.info(f"Acquiring new OAuth token for client_id='{client_id}'")
        
        try:
            # Prepare OAuth request
            payload = {
                "username": self._api_id,
                "password": self._password,
                "client_id": client_id,
                "grant_type": "password"
            }
            
            # Request token from OAuth server
            with httpx.Client() as client:
                resp = client.post(
                    self._auth_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=10.0
                )
                resp.raise_for_status()
            
            response = resp.json()
            
            # Store token info
            expires_in = self._default_expires_in if self._default_expires_in is not None else response.get("expires_in", 3660)
            created_at = time.time()
            
            # Create TokenInfo for internal cache
            token_info = TokenInfo(
                access_token=response["access_token"],
                refresh_token=response.get("refresh_token", ""),
                expires_in=expires_in,
                created_at=created_at,
                scope=response.get("scope", "read write"),
                token_type=response.get("token_type", "Bearer")
            )
            self._tokens[client_id] = token_info
            
            # Store in backend storage
            token_data = TokenData(
                access_token=response["access_token"],
                refresh_token=response.get("refresh_token", ""),
                expires_in=expires_in,
                created_at=created_at,
                scope=response.get("scope", "read write"),
                token_type=response.get("token_type", "Bearer")
            )
            self._storage.set(client_id, token_data)
            
            logger.info(
                f"✓ OAuth token acquired for client_id='{client_id}' "
                f"(expires_in={expires_in}s, token_type={token_info.token_type})"
            )
            
            # Call lifecycle hook
            if self._lifecycle_hooks:
                try:
                    event = TokenEvent(
                        client_id=client_id,
                        timestamp=created_at,
                        event_type="acquired",
                        access_token=response["access_token"][:30] + "..." if response.get("access_token") else None,
                        expires_in=expires_in,
                        token_type=token_info.token_type,
                        scope=token_info.scope,
                        is_auto_refresh=is_auto_refresh,
                    )
                    self._lifecycle_hooks.on_token_acquired(event)
                except Exception as e:
                    logger.warning(f"Lifecycle hook on_token_acquired failed: {e}")
            
            return response
            
        except Exception as e:
            # Call failure hook
            if self._lifecycle_hooks:
                try:
                    event = TokenEvent(
                        client_id=client_id,
                        timestamp=time.time(),
                        event_type="failed",
                        error=str(e),
                        error_type=type(e).__name__,
                        is_auto_refresh=is_auto_refresh,
                    )
                    self._lifecycle_hooks.on_token_failed(event)
                except Exception as hook_error:
                    logger.warning(f"Lifecycle hook on_token_failed failed: {hook_error}")
            raise
    
    def _refresh_token(self, client_id: str, is_auto_refresh: bool = False) -> dict[str, Any]:
        """
        Refresh token using refresh_token grant.
        
        NOT thread-safe - caller must hold self._lock.
        
        Args:
            client_id: FortiCloud service client_id
            is_auto_refresh: Whether this is triggered by auto-refresh thread
        
        Returns:
            Full OAuth response dict
        """
        if client_id not in self._tokens:
            # No token to refresh, acquire new one
            logger.debug(f"No token to refresh for client_id='{client_id}', acquiring new token instead")
            return self._acquire_token(client_id, is_auto_refresh=is_auto_refresh)
        
        old_token = self._tokens[client_id]
        logger.info(f"Refreshing OAuth token for client_id='{client_id}'")
        
        try:
            # Prepare refresh request
            payload = {
                "username": self._api_id,
                "password": self._password,
                "client_id": client_id,
                "grant_type": "refresh_token",
                "refresh_token": old_token.refresh_token
            }
            
            # Request refreshed token
            with httpx.Client() as client:
                resp = client.post(
                    self._auth_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=10.0
                )
                resp.raise_for_status()
            
            response = resp.json()
            
            # Update token info
            expires_in = self._default_expires_in if self._default_expires_in is not None else response.get("expires_in", 3660)
            created_at = time.time()
            
            token_info = TokenInfo(
                access_token=response["access_token"],
                refresh_token=response.get("refresh_token", old_token.refresh_token),
                expires_in=expires_in,
                created_at=created_at,
                scope=response.get("scope", old_token.scope),
                token_type=response.get("token_type", old_token.token_type)
            )
            self._tokens[client_id] = token_info
            
            # Update storage backend
            token_data = TokenData(
                access_token=response["access_token"],
                refresh_token=response.get("refresh_token", old_token.refresh_token),
                expires_in=expires_in,
                created_at=created_at,
                scope=response.get("scope", old_token.scope),
                token_type=response.get("token_type", old_token.token_type)
            )
            self._storage.set(client_id, token_data)
            
            logger.info(
                f"✓ OAuth token refreshed for client_id='{client_id}' "
                f"(expires_in={expires_in}s)"
            )
            
            # Call lifecycle hook
            if self._lifecycle_hooks:
                try:
                    event = TokenEvent(
                        client_id=client_id,
                        timestamp=created_at,
                        event_type="refreshed",
                        access_token=response["access_token"][:30] + "..." if response.get("access_token") else None,
                        expires_in=expires_in,
                        token_type=token_info.token_type,
                        scope=token_info.scope,
                        is_auto_refresh=is_auto_refresh,
                    )
                    self._lifecycle_hooks.on_token_refreshed(event)
                except Exception as e:
                    logger.warning(f"Lifecycle hook on_token_refreshed failed: {e}")
            
            return response
            
        except Exception as e:
            # Refresh failed, fall back to password grant
            logger.warning(f"Token refresh failed for client_id='{client_id}': {e}, falling back to password grant")
            
            # Call failure hook
            if self._lifecycle_hooks:
                try:
                    event = TokenEvent(
                        client_id=client_id,
                        timestamp=time.time(),
                        event_type="failed",
                        error=str(e),
                        error_type=type(e).__name__,
                        is_auto_refresh=is_auto_refresh,
                    )
                    self._lifecycle_hooks.on_token_failed(event)
                except Exception as hook_error:
                    logger.warning(f"Lifecycle hook on_token_failed failed: {hook_error}")
            
            return self._acquire_token(client_id, is_auto_refresh=is_auto_refresh)
    
    def _start_auto_refresh(self) -> None:
        """Start background thread for automatic token refresh."""
        if self._refresh_thread and self._refresh_thread.is_alive():
            return
        
        self._stop_refresh.clear()
        self._refresh_thread = threading.Thread(
            target=self._auto_refresh_loop,
            daemon=True,
            name="CloudSession-AutoRefresh"
        )
        self._refresh_thread.start()
    
    def _auto_refresh_loop(self) -> None:
        """Background loop that refreshes tokens before they expire."""
        logger.debug("Auto-refresh loop started")
        while not self._stop_refresh.is_set():
            try:
                with self._lock:
                    for client_id, token in list(self._tokens.items()):
                        if token.is_expiring_soon(self._refresh_buffer):
                            logger.debug(
                                f"Auto-refresh: Token expiring soon for client_id='{client_id}' "
                                f"(expires in {token.time_remaining:.0f}s, buffer={self._refresh_buffer}s)"
                            )
                            try:
                                self._refresh_token(client_id, is_auto_refresh=True)
                            except Exception as e:
                                # Ignore refresh errors, will retry next loop
                                logger.warning(f"Auto-refresh failed for client_id='{client_id}': {e}")
            except Exception as e:
                # Ignore errors in refresh loop
                logger.warning(f"Error in auto-refresh loop: {e}")
            
            # Sleep for configured interval between checks (default 60 seconds)
            # If interval is 0, exit the loop (background refresh disabled)
            if self._refresh_check_interval <= 0:
                logger.debug("Auto-refresh disabled (check_interval=0), exiting loop")
                break
            self._stop_refresh.wait(self._refresh_check_interval)
    
    def __repr__(self) -> str:
        """String representation."""
        token_count = len(self._tokens)
        client_ids = list(self._tokens.keys())
        return (
            f"CloudSession(api_id={self._api_id[:10]}..., "
            f"tokens={token_count}, "
            f"client_ids={client_ids}, "
            f"auto_refresh={self._auto_refresh})"
        )
