"""
FortiManager HTTP Client

HTTP client for FortiManager JSON-RPC API with session-based authentication.
Shares retry logic, circuit breaker, and connection pooling with HTTPClient.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Literal, Optional

import httpx

from .base import BaseHTTPClient

logger = logging.getLogger("hfortix.http.fmg")

__all__ = ["HTTPClientJSONRPC"]


class HTTPClientJSONRPC(BaseHTTPClient):
    """
    HTTP client for Fortinet JSON-RPC API (FortiManager, FortiAnalyzer, FortiOS FMG Proxy).
    
    Supports two authentication methods:
    1. Session-based: username/password with login/logout (traditional)
    2. API key: Direct Bearer token authentication (FMG 7.4.7+/7.6.2+)
    
    Provides session-based or API key authentication and JSON-RPC request handling
    while reusing the retry logic, circuit breaker, connection pooling,
    and statistics from BaseHTTPClient.
    
    This client is used by:
    - FortiManager: JSON-RPC API for device management
    - FortiAnalyzer: JSON-RPC API for analytics and logging
    - FortiOS FMG Proxy: JSON-RPC API for VDOM operations
    
    Note: JSON-RPC is different from FortiOS REST API:
    - FortiOS: REST API with Bearer token in headers
    - JSON-RPC: Session token in request body OR Bearer token in headers
    
    Example (Session-based):
        >>> client = HTTPClientJSONRPC(
        ...     url="https://fmg.example.com",
        ...     username="admin",
        ...     password="password",
        ... )
        >>> client.login()
        >>> response = client.execute("get", [{"url": "/dvmdb/device"}])
        >>> client.logout()
    
    Example (API key):
        >>> client = HTTPClientJSONRPC(
        ...     url="https://fmg.example.com",
        ...     api_key="your-api-key-here",
        ... )
        >>> # No login needed - API key is used directly
        >>> response = client.execute("get", [{"url": "/dvmdb/device"}])
    """
    
    def __init__(
        self,
        url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        api_key: Optional[str] = None,
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
        # NEW: Rate limiting enforcement parameters
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_half_open_calls: int = 3,
        session_idle_timeout: float = 900.0,  # Session idle timeout in seconds (default: 15 min, 10% threshold, min 60s)
    ) -> None:
        """
        Initialize Fortinet JSON-RPC HTTP client.
        
        Supports two authentication methods:
        1. Session-based: username + password (requires login/logout)
        2. API key: Direct Bearer token authentication (no session needed)
        
        Args:
            url: Base URL for JSON-RPC API (e.g., "https://fmg.example.com" or "https://faz.example.com")
            username: Admin username (required for session-based auth)
            password: Admin password (required for session-based auth)
            api_key: API key for direct authentication (alternative to username/password)
            verify: Verify SSL certificates (default: True)
            adom: Default ADOM for operations
            max_retries: Maximum retry attempts on transient failures
            connect_timeout: Connection timeout in seconds
            read_timeout: Read timeout in seconds
            circuit_breaker_threshold: Failures before opening circuit
            circuit_breaker_timeout: Seconds before retrying after circuit opens
            max_connections: Maximum connection pool size
            max_keepalive_connections: Maximum keepalive connections
            adaptive_retry: Enable adaptive retry with backpressure detection
            retry_strategy: 'exponential' or 'linear' backoff
            retry_jitter: Add random jitter to retry delays
            read_only: Enable read-only mode - simulate write operations
                      without executing (default: False)
            audit_handler: Handler for audit logging (implements AuditHandler
                          protocol). Essential for compliance.
            audit_callback: Custom callback function for audit logging.
                           Alternative to audit_handler.
            user_context: Optional dict with user/application context to
                         include in audit logs.
            rate_limit: Enable rate limiting enforcement (default: False)
            rate_limit_strategy: 'queue' or 'reject' (default: 'queue')
            rate_limit_max_requests: Max requests per window (default: 100)
            rate_limit_window_seconds: Time window in seconds (default: 60.0)
            rate_limit_queue_size: Max queue size (default: 100)
            rate_limit_queue_timeout: Max wait time in queue (default: 30.0)
            rate_limit_queue_overflow: 'block' or 'drop' on overflow (default: 'block')
            circuit_breaker: Enable circuit breaker (default: False)
            circuit_breaker_half_open_calls: Calls to test in half-open state (default: 3)
            session_idle_timeout: Session idle timeout in seconds (default: 900 = 15 min).
                                 Used to proactively re-login before session expires.
                                 Can be adjusted based on FortiManager/FortiAnalyzer settings.
        
        Note:
            Either provide (username + password) OR api_key, not both.
            API key authentication is recommended for FMG 7.4.7+/7.6.2+.
            
            Session Timeout: FortiManager/FortiAnalyzer sessions expire after idle time.
            The default is 15 minutes, but can be configured on the server.
            Set session_idle_timeout to match your server's configuration.
        """
        # Validate authentication parameters
        if api_key and (username or password):
            raise ValueError("Provide either (username + password) OR api_key, not both")
        if not api_key and not (username and password):
            raise ValueError("Must provide either (username + password) OR api_key")
        
        super().__init__(
            url=url,
            verify=verify,
            vdom=None,  # FMG uses ADOM, not VDOM
            max_retries=max_retries,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            circuit_breaker_threshold=circuit_breaker_threshold,
            circuit_breaker_timeout=circuit_breaker_timeout,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            adaptive_retry=adaptive_retry,
            retry_strategy=retry_strategy,
            retry_jitter=retry_jitter,
            read_only=read_only,
            audit_handler=audit_handler,
            audit_callback=audit_callback,
            user_context=user_context,
            rate_limit_calls_per_min=rate_limit_calls_per_min,
            rate_limit_calls_per_5min=rate_limit_calls_per_5min,
            rate_limit_calls_per_hour=rate_limit_calls_per_hour,
            rate_limit_errors_per_min=rate_limit_errors_per_min,
            rate_limit_errors_per_5min=rate_limit_errors_per_5min,
            rate_limit_errors_per_hour=rate_limit_errors_per_hour,
            # NEW: Pass rate limiting parameters
            rate_limit=rate_limit,
            rate_limit_strategy=rate_limit_strategy,
            rate_limit_max_requests=rate_limit_max_requests,
            rate_limit_window_seconds=rate_limit_window_seconds,
            rate_limit_queue_size=rate_limit_queue_size,
            rate_limit_queue_timeout=rate_limit_queue_timeout,
            rate_limit_queue_overflow=rate_limit_queue_overflow,
            circuit_breaker=circuit_breaker,
            circuit_breaker_half_open_calls=circuit_breaker_half_open_calls,
        )
        
        self._username = username
        self._password = password
        self._api_key = api_key
        self._adom = adom  # For logging context
        
        self._session_token: str | None = None
        self._session_login_time: float | None = None
        self._session_idle_timeout: float = session_idle_timeout
        self._session_last_used: float | None = None
        self._request_id: int = 0
        
        # HTTP client with connection pooling
        self._http_client: httpx.Client | None = None
        self._max_connections = max_connections
        self._max_keepalive = max_keepalive_connections
    
    @property
    def jsonrpc_url(self) -> str:
        """JSON-RPC endpoint URL."""
        return f"{self._url}/jsonrpc"
    
    @property
    def is_authenticated(self) -> bool:
        """Check if we have a valid session or API key."""
        return self._session_token is not None or self._api_key is not None
    
    @property
    def uses_api_key(self) -> bool:
        """Check if using API key authentication."""
        return self._api_key is not None
    
    @property
    def adom(self) -> str | None:
        """Default ADOM."""
        return self._adom
    
    @property
    def session_idle_timeout(self) -> float:
        """Session idle timeout in seconds."""
        return self._session_idle_timeout
    
    @session_idle_timeout.setter
    def session_idle_timeout(self, value: float) -> None:
        """
        Set session idle timeout.
        
        Args:
            value: Timeout in seconds
        """
        self._session_idle_timeout = value
    
    @property
    def is_session_expired(self) -> bool:
        """
        Check if session has expired based on idle timeout.
        
        Returns:
            True if session appears to be expired (based on last use time)
        """
        if self._api_key:
            return False  # API keys don't expire
        
        if not self._session_token or not self._session_last_used:
            return True  # No session or never used
        
        idle_time = time.perf_counter() - self._session_last_used
        return idle_time >= self._session_idle_timeout
    
    @property
    def session_time_remaining(self) -> float | None:
        """
        Get estimated time remaining before session expires (seconds).
        
        Returns:
            Seconds until expiration, or None if using API key or no session
        """
        if self._api_key or not self._session_token or not self._session_last_used:
            return None
        
        idle_time = time.perf_counter() - self._session_last_used
        return max(0.0, self._session_idle_timeout - idle_time)
    
    def _get_http_client(self) -> httpx.Client:
        """Get or create HTTP client with connection pooling."""
        if self._http_client is None:
            limits = httpx.Limits(
                max_connections=self._max_connections,
                max_keepalive_connections=self._max_keepalive,
            )
            timeout = httpx.Timeout(
                connect=self._connect_timeout,
                read=self._read_timeout,
                write=30.0,
                pool=10.0,
            )
            self._http_client = httpx.Client(
                verify=self._verify,
                limits=limits,
                timeout=timeout,
            )
        return self._http_client
    
    def _next_id(self) -> int:
        """Get next request ID."""
        self._request_id += 1
        return self._request_id
    
    def login(self) -> dict[str, Any]:
        """
        Authenticate with FortiManager using username/password.
        
        Not needed when using API key authentication.
        
        Returns:
            FMG login response dict with session and status information
        
        Raises:
            RuntimeError: If authentication fails or using API key
        """
        if self._api_key:
            # API key authentication doesn't require login
            return {
                "result": [{"status": {"code": 0, "message": "Using API key authentication"}}],
            }
        
        if self._session_token:
            # Already logged in - return success status
            logger.info("Already authenticated with active session token")
            return {
                "result": [{"status": {"code": 0, "message": "Already authenticated"}}],
                "session": self._session_token
            }
        
        if not self._username or not self._password:
            raise RuntimeError("Username and password required for session-based authentication")
        
        request = {
            "id": self._next_id(),
            "method": "exec",
            "params": [
                {
                    "url": "/sys/login/user",
                    "data": {
                        "user": self._username,
                        "passwd": self._password,
                    }
                }
            ],
        }
        
        logger.info("🔐 Logging in to FortiManager at %s", self._url)
        
        client = self._get_http_client()
        response = client.post(self.jsonrpc_url, json=request)
        response.raise_for_status()
        
        data = response.json()
        
        # Check for successful login
        result = data.get("result", [{}])[0]
        status = result.get("status", {})
        
        if status.get("code") != 0:
            error_msg = status.get("message", "Unknown error")
            logger.error("FMG login failed: %s", error_msg)
            raise RuntimeError(f"FMG login failed: {error_msg}")
        
        self._session_token = data.get("session")
        if not self._session_token:
            raise RuntimeError("FMG login succeeded but no session token received")
        
        # Track session timing
        now = time.perf_counter()
        self._session_login_time = now
        self._session_last_used = now
        
        logger.info("✅ Successfully logged in to FortiManager (session token: %s...)", self._session_token[:20])
        logger.info("   Session timeout: %.0fs, Refresh threshold: %.0fs", 
                   self._session_idle_timeout, 
                   max(60.0, self._session_idle_timeout * 0.1))
        return data
    
    def logout(self) -> dict[str, Any]:
        """
        End FortiManager session.
        
        Not applicable when using API key authentication.
        
        Returns:
            FMG logout response dict with status information
        """
        if self._api_key:
            return {"status": {"code": 0, "message": "API key authentication - no logout needed"}}
        
        if not self._session_token:
            return {"status": {"code": 0, "message": "Not logged in"}}
        
        try:
            request = {
                "id": self._next_id(),
                "method": "exec",
                "params": [{"url": "/sys/logout"}],
                "session": self._session_token,
            }
            
            client = self._get_http_client()
            response = client.post(self.jsonrpc_url, json=request)
            result = response.json()
            logger.debug("Logged out from FortiManager")
            return result
        except Exception as e:
            logger.debug("Logout error: %s", e)
            return {"status": {"code": -1, "message": str(e)}}
        finally:
            self._session_token = None
            self._session_login_time = None
            self._session_last_used = None
    
    def execute(
        self,
        method: Literal["exec", "get", "set", "add", "update", "delete"],
        params: list[dict[str, Any]],
        verbose: int = 1,
    ) -> dict[str, Any]:
        """
        Execute a FortiManager JSON-RPC request.
        
        Automatically handles authentication:
        - Session-based: Ensures login before request
        - API key: Adds Bearer token to headers
        
        Args:
            method: JSON-RPC method
            params: Request parameters
            verbose: Verbosity level (0 or 1)
            
        Returns:
            FMG response dict
            
        Raises:
            RuntimeError: If not authenticated or request fails
        """
        # Ensure authentication for session-based
        if not self._api_key and not self._session_token:
            self.login()
        
        # Check if session has already expired (time since last use > timeout)
        if not self._api_key and self._session_token and self.is_session_expired:
            logger.warning("⚠️  Session expired (idle timeout reached), re-logging in")
            self._session_token = None
            self.login()
        elif not self._api_key and self._session_token:
            time_remaining = self.session_time_remaining
            # Refresh threshold: 10% of timeout, but minimum 60 seconds
            # Examples: 300s → 60s (not 30s), 900s → 90s, 3600s → 360s
            refresh_threshold = max(60.0, self._session_idle_timeout * 0.1)
            if time_remaining is not None and time_remaining < refresh_threshold:
                logger.warning(
                    "⏰ Session expiring soon (%.1fs remaining, threshold: %.1fs), proactively re-logging in",
                    time_remaining,
                    refresh_threshold
                )
                self._session_token = None
                self.login()
        
        endpoint = params[0].get("url", "/unknown") if params else "/unknown"
        
        # Check circuit breaker
        self._check_circuit_breaker(endpoint)
        
        # Build request
        request = {
            "id": self._next_id(),
            "method": method,
            "params": params,
            "verbose": verbose,
        }
        
        # Add session token if using session-based auth
        if self._session_token:
            request["session"] = self._session_token
        
        # Prepare headers for API key auth
        headers: dict[str, str] = {"Content-Type": "application/json"}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"
        
        start_time = time.perf_counter()
        attempt = 0
        last_error: Exception | None = None
        
        while attempt <= self._max_retries:
            try:
                client = self._get_http_client()
                response = client.post(
                    self.jsonrpc_url, 
                    json=request,
                    headers=headers if self._api_key else None,
                )
                response.raise_for_status()
                
                data = response.json()
                
                # Check for FMG-level errors
                result = data.get("result", [{}])[0] if data.get("result") else {}
                status = result.get("status", {})
                
                if status.get("code") != 0:
                    error_msg = status.get("message", "Unknown error")
                    # Session expired - try to re-login (only for session-based auth)
                    if not self._api_key and ("session" in error_msg.lower() or status.get("code") == -11):
                        self._session_token = None
                        self.login()
                        request["session"] = self._session_token
                        continue
                    
                    raise RuntimeError(f"FMG request failed: {error_msg}")
                
                # Success
                duration = time.perf_counter() - start_time
                self._record_circuit_breaker_success()
                self._retry_stats["successful_requests"] += 1
                self._retry_stats["total_requests"] += 1
                
                # Track session usage time (for idle timeout calculation)
                if self._session_token:
                    self._session_last_used = time.perf_counter()
                
                # Track rate limit statistics
                self._rate_stats.record_call()
                
                logger.debug(
                    "FMG request completed in %.3fs",
                    duration,
                    extra=self._log_context(endpoint=endpoint, duration_seconds=duration),
                )
                
                # Add HTTP metadata to response (for FortiManagerResponse wrapper)
                # This metadata is added at the transport layer for visibility
                data["_http_metadata"] = {
                    "status_code": response.status_code,
                    "method": "POST",  # JSON-RPC always uses POST
                    "url": self.jsonrpc_url,
                    "response_time": round(duration * 1000, 2),  # Convert to milliseconds
                }
                
                return data
                
            except httpx.TimeoutException as e:
                last_error = e
                if self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    self._record_retry("timeout", endpoint)
                    delay = self._calculate_retry_delay(attempt)
                    logger.warning(
                        "Request timeout, retrying in %.1fs (attempt %d/%d)",
                        delay, attempt, self._max_retries + 1,
                    )
                    time.sleep(delay)
                    continue
                raise
                
            except httpx.HTTPStatusError as e:
                last_error = e
                if e.response.status_code >= 500 and self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    self._record_retry("server_error", endpoint)
                    delay = self._calculate_retry_delay(attempt)
                    logger.warning(
                        "Server error %d, retrying in %.1fs (attempt %d/%d)",
                        e.response.status_code, delay, attempt, self._max_retries + 1,
                    )
                    time.sleep(delay)
                    continue
                raise
                
            except Exception as e:
                last_error = e
                self._record_circuit_breaker_failure(endpoint)
                raise
        
        # All retries exhausted
        self._retry_stats["failed_requests"] += 1
        self._retry_stats["total_requests"] += 1
        self._record_circuit_breaker_failure(endpoint)
        
        # Track rate limit error
        self._rate_stats.record_error()
        
        if last_error:
            raise last_error
        raise RuntimeError("Request failed after all retries")
    
    def _calculate_retry_delay(self, attempt: int) -> float:
        """Calculate retry delay based on strategy."""
        if self._retry_strategy == "exponential":
            delay = min(2 ** (attempt - 1), 30.0)  # Max 30 seconds
        else:  # linear
            delay = min(attempt, 5.0)  # Max 5 seconds
        
        if self._retry_jitter:
            import random
            jitter = random.uniform(0, delay * 0.25)
            delay += jitter
        
        return delay
    
    def proxy_request(
        self,
        action: Literal["get", "post", "put", "delete"],
        resource: str,
        targets: list[str],
        payload: dict[str, Any] | None = None,
        timeout: int = 60,
    ) -> dict[str, Any]:
        """
        Execute a FortiOS API call through the FMG proxy endpoint.
        
        This is the core method for routing FortiOS REST API calls
        through FortiManager to managed devices.
        
        Args:
            action: HTTP method (get, post, put, delete)
            resource: FortiOS API resource path (e.g., "/api/v2/cmdb/firewall/address")
            targets: List of target devices/groups (e.g., ["adom/root/device/fw-01"])
            payload: Request body for POST/PUT
            timeout: Request timeout in seconds
            
        Returns:
            FMG response dict containing results from each target device
        """
        data: dict[str, Any] = {
            "action": action,
            "resource": resource,
            "target": targets,
            "timeout": timeout,
        }
        
        if payload:
            data["payload"] = payload
        
        params = [
            {
                "url": "/sys/proxy/json",
                "data": data,
            }
        ]
        
        return self.execute("exec", params)
    
    def close(self) -> None:
        """Close the session and HTTP client."""
        self.logout()
        if self._http_client:
            self._http_client.close()
            self._http_client = None
    
    def __enter__(self) -> "HTTPClientJSONRPC":
        """Context manager entry."""
        self.login()
        return self
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()
    
    # ========================================================================
    # Statistics and Health Methods (from BaseHTTPClient)
    # ========================================================================
    
    def get_health_metrics(self) -> dict[str, Any]:
        """Get health metrics for monitoring."""
        return {
            "authenticated": self.is_authenticated,
            "auth_method": "api_key" if self._api_key else "session",
            "circuit_breaker": self.get_circuit_breaker_state(),
            "retry_stats": self.get_retry_stats(),
            "adom": self._adom,
        }
    
    def get_connection_stats(self) -> dict[str, Any]:
        """Get connection pool statistics."""
        stats: dict[str, Any] = {
            "max_connections": self._max_connections,
            "max_keepalive": self._max_keepalive,
        }
        
        if self._http_client:
            # httpx doesn't expose detailed pool stats, but we can track
            stats["client_active"] = True
        else:
            stats["client_active"] = False
        
        return stats
