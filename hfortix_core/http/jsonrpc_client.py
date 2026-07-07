"""
Fortinet JSON-RPC HTTP Client

HTTP client for the FortiManager/FortiAnalyzer JSON-RPC API with
session-based authentication.
Shares retry logic, circuit breaker, and connection pooling with HTTPClient.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Literal, Optional
from urllib.parse import urlparse, urlunparse

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
        api_user: Optional[str] = None,
        port: Optional[int] = None,
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
        # Rate limiting enforcement parameters
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_half_open_calls: int = 3,
        # Circuit breaker auto-retry (matches FortiOS client)
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        # Operation audit log (matches FortiOS client)
        track_operations: bool = False,
        session_idle_timeout: float = 900.0,  # Session idle timeout in seconds (default: 15 min, 10% threshold, min 60s)
        user_agent: Optional[str] = None,
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
            rate_limit_strategy: 'queue', 'drop', or 'raise' (default: 'queue')
            rate_limit_max_requests: Max requests per window (default: 100)
            rate_limit_window_seconds: Time window in seconds (default: 60.0)
            rate_limit_queue_size: Max queue size (default: 100)
            rate_limit_queue_timeout: Max wait time in queue (default: 30.0)
            rate_limit_queue_overflow: 'block' or 'drop' on overflow (default: 'block')
            circuit_breaker: Enable circuit breaker (default: False)
            circuit_breaker_half_open_calls: Calls to test in half-open state (default: 3)
            circuit_breaker_auto_retry: Enable automatic retry when circuit breaker opens
                       (default: False). When enabled, waits circuit_breaker_retry_delay
                       seconds between retries instead of immediately raising exception.
            circuit_breaker_max_retries: Maximum auto-retry attempts when circuit open
                       (default: 3)
            circuit_breaker_retry_delay: Delay in seconds between auto-retry attempts
                       (default: 5.0)
            track_operations: Enable operation tracking - maintain audit log of all API
                       calls (default: False). Retrieve with get_operations().
            session_idle_timeout: Session idle timeout in seconds (default: 900 = 15 min).
                                 Used to proactively re-login before session expires.
                                 Can be adjusted based on FortiManager/FortiAnalyzer settings.
            user_agent: Custom User-Agent header value. Defaults to "hfortix/<version>".

        Note:
            Either provide (username + password) OR api_key, not both.
            API key authentication is recommended for FMG 7.4.7+/7.6.2+.

            Session Timeout: FortiManager/FortiAnalyzer sessions expire after idle time.
            The default is 15 minutes, but can be configured on the server.
            Set session_idle_timeout to match your server's configuration.
        """
        # Normalize URL: accept any of these forms:
        #   fmg.example.com          → https://fmg.example.com
        #   http://fmg.example.com   → http://fmg.example.com
        #   fmg.example.com:8443     → https://fmg.example.com:8443
        #   https://fmg.example.com/jsonrpc → https://fmg.example.com
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            url = f"https://{url}"
        parsed = urlparse(url)
        path = parsed.path.rstrip("/")
        path = "" if path == "/jsonrpc" else path
        # Explicit port parameter overrides any port embedded in the URL
        if port is not None:
            netloc = f"{parsed.hostname}:{port}"
        else:
            netloc = parsed.netloc
        url = urlunparse((parsed.scheme, netloc, path, "", "", ""))

        # Validate authentication parameters
        if api_key and (username or password):
            raise ValueError(
                "Provide either (username + password) OR api_key, not both"
            )
        if not api_key and not (username and password):
            raise ValueError("Must provide either (username + password) OR api_key")

        super().__init__(
            url=url,
            verify=verify,
            vdom=None,  # FMG/FAZ use ADOM, not VDOM
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
            circuit_breaker_auto_retry=circuit_breaker_auto_retry,
            circuit_breaker_max_retries=circuit_breaker_max_retries,
            circuit_breaker_retry_delay=circuit_breaker_retry_delay,
        )

        # Initialize synchronous rate limiter if enabled
        if self._rate_limit_enabled and self._rate_limit_config:
            from hfortix_core.rate_limiter import RateLimiter

            self._rate_limiter = RateLimiter(
                max_requests=self._rate_limit_config["max_requests"],
                window_seconds=self._rate_limit_config["window_seconds"],
                strategy=self._rate_limit_config["strategy"],
                queue_size=self._rate_limit_config["queue_size"],
                queue_timeout=self._rate_limit_config["queue_timeout"],
                queue_overflow=self._rate_limit_config["queue_overflow"],
            )
            logger.info("Synchronous rate limiter initialized")
        else:
            self._rate_limiter = None

        if user_agent is None:
            from hfortix_core import __version__

            user_agent = f"hfortix/{__version__}"
        self._user_agent = user_agent

        self._username = username
        self._password = password
        self._api_key = api_key
        self._api_user = api_user
        self._adom = adom  # For logging context

        self._session_token: str | None = None
        self._session_login_time: float | None = None
        self._session_idle_timeout: float = session_idle_timeout
        self._session_last_used: float | None = None
        self._request_id: int = 0

        # HTTP client with connection pooling
        self._http_client: httpx.Client | None = None
        self._max_connections = max_connections
        self._max_keepalive_connections = max_keepalive_connections

        # Connection pool monitoring
        self._active_requests: int = 0
        self._total_requests: int = 0
        self._pool_exhaustion_count: int = 0
        self._pool_exhaustion_timestamps: list[float] = []

        # Request inspection for debugging
        self._last_request: Optional[dict[str, Any]] = None
        self._last_response: Optional[dict[str, Any]] = None
        self._last_response_time: Optional[float] = None

        # Operation audit log
        self._track_operations = track_operations
        self._operations: list[dict[str, Any]] = [] if track_operations else []

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
        """Get or create HTTP client with connection pooling and HTTP/2."""
        if self._http_client is None:
            limits = httpx.Limits(
                max_connections=self._max_connections,
                max_keepalive_connections=self._max_keepalive_connections,
            )
            timeout = httpx.Timeout(
                connect=self._connect_timeout,
                read=self._read_timeout,
                write=30.0,
                pool=10.0,
            )
            self._http_client = httpx.Client(
                headers={"User-Agent": self._user_agent},
                verify=self._verify,
                limits=limits,
                timeout=timeout,
                http2=True,
            )
        return self._http_client

    def _next_id(self) -> int:
        """Get next request ID."""
        self._request_id += 1
        return self._request_id

    def login(self) -> dict[str, Any]:
        """
        Authenticate with FortiManager/FortiAnalyzer using username/password.

        Not needed when using API key authentication.

        Returns:
            JSON-RPC login response dict with session and status information

        Raises:
            RuntimeError: If authentication fails or using API key
        """
        if self._api_key:
            # API key authentication doesn't require login
            return {
                "result": [
                    {"status": {"code": 0, "message": "Using API key authentication"}}
                ],
            }

        if self._session_token:
            # Already logged in - return success status
            logger.info("Already authenticated with active session token")
            return {
                "result": [{"status": {"code": 0, "message": "Already authenticated"}}],
                "session": self._session_token,
            }

        if not self._username or not self._password:
            raise RuntimeError(
                "Username and password required for session-based authentication"
            )

        request = {
            "id": self._next_id(),
            "method": "exec",
            "params": [
                {
                    "url": "/sys/login/user",
                    "data": {
                        "user": self._username,
                        "passwd": self._password,
                    },
                }
            ],
        }

        logger.info("Logging in to JSON-RPC API at %s", self._url)

        client = self._get_http_client()
        response = client.post(self.jsonrpc_url, json=request)
        response.raise_for_status()

        data = response.json()

        # Check for successful login
        result = data.get("result", [{}])[0]
        status = result.get("status", {})

        if status.get("code") != 0:
            error_msg = status.get("message", "Unknown error")
            logger.error("JSON-RPC login failed: %s", error_msg)
            raise RuntimeError(f"JSON-RPC login failed: {error_msg}")

        self._session_token = data.get("session")
        if not self._session_token:
            raise RuntimeError("JSON-RPC login succeeded but no session token received")

        # Track session timing
        now = time.perf_counter()
        self._session_login_time = now
        self._session_last_used = now

        logger.info(
            "Successfully logged in to JSON-RPC API (session token: %s...)",
            self._session_token[:20],
        )
        logger.info(
            "   Session timeout: %.0fs, Refresh threshold: %.0fs",
            self._session_idle_timeout,
            max(60.0, self._session_idle_timeout * 0.1),
        )
        return data

    def logout(self) -> dict[str, Any]:
        """
        End FortiManager/FortiAnalyzer session.

        Not applicable when using API key authentication.

        Returns:
            JSON-RPC logout response dict with status information
        """
        if self._api_key:
            return {
                "status": {
                    "code": 0,
                    "message": "API key authentication - no logout needed",
                }
            }

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
            logger.debug("Logged out from JSON-RPC API")
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
        Execute a JSON-RPC request (FortiManager/FortiAnalyzer).

        Automatically handles authentication:
        - Session-based: Ensures login before request
        - API key: Adds Bearer token to headers

        Args:
            method: JSON-RPC method
            params: Request parameters
            verbose: Verbosity level (0 or 1)

        Returns:
            JSON-RPC response dict with '_http_metadata' key added at
            the transport layer

        Raises:
            RuntimeError: If not authenticated or request fails
        """
        # Ensure authentication for session-based
        if not self._api_key and not self._session_token:
            self.login()

        # Check if session has already expired (time since last use > timeout)
        if not self._api_key and self._session_token and self.is_session_expired:
            logger.warning("Session expired (idle timeout reached), re-logging in")
            self._session_token = None
            self.login()
        elif not self._api_key and self._session_token:
            time_remaining = self.session_time_remaining
            # Refresh threshold: 10% of timeout, but minimum 60 seconds
            refresh_threshold = max(60.0, self._session_idle_timeout * 0.1)
            if time_remaining is not None and time_remaining < refresh_threshold:
                logger.warning(
                    "Session expiring soon (%.1fs remaining, threshold: %.1fs), proactively re-logging in",
                    time_remaining,
                    refresh_threshold,
                )
                self._session_token = None
                self.login()

        endpoint = params[0].get("url", "/unknown") if params else "/unknown"

        # Rate limiting enforcement (zero overhead when disabled)
        import uuid

        request_id = str(uuid.uuid4())[:8]
        if self._rate_limiter is not None:
            if not self._rate_limiter.acquire():
                # acquire() returns False only for strategy="drop" — request silently dropped
                logger.warning(
                    "Request dropped by rate limiter",
                    extra=self._log_context(request_id=request_id, endpoint=endpoint),
                )
                return {
                    "id": self._next_id(),
                    "result": [
                        {
                            "status": {
                                "code": -1,
                                "message": "Rate limit exceeded - request dropped",
                            }
                        }
                    ],
                }

        try:
            # Check circuit breaker
            self._check_circuit_breaker(endpoint)
        finally:
            # Release rate limiter slot after circuit breaker check
            if self._rate_limiter is not None:
                self._rate_limiter.release()

        # Per-endpoint timeout configuration
        endpoint_timeout = self._get_endpoint_timeout(endpoint)

        # Build request
        request = {
            "id": self._next_id(),
            "method": method,
            "params": params,
            "verbose": verbose,
        }

        # FortiAnalyzer v3-dialect endpoints (apiver in params) require a
        # strict JSON-RPC 2.0 envelope and answer in kind. Legacy
        # FMG-style endpoints use the loose envelope, so the member is
        # added only when apiver is present.
        is_v3 = any(isinstance(p, dict) and "apiver" in p for p in params)
        if is_v3:
            request["jsonrpc"] = "2.0"

        # Session token goes in the JSON-RPC "session" field (session-based auth only).
        # API keys go in the Authorization: Bearer header — NOT the session field.
        if self._session_token:
            request["session"] = self._session_token

        # Build headers: Bearer token for API key auth, optional access_user for FMG 7.6.6+
        headers: dict[str, str] = {"Content-Type": "application/json"}
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"
            if self._api_user:
                headers["access_user"] = self._api_user

        # Track rate limit statistics (informational)
        self._rate_stats.record_call()
        self._retry_stats["total_requests"] += 1
        self._total_requests += 1

        start_time = time.perf_counter()
        attempt = 0
        last_error: Exception | None = None

        while attempt <= self._max_retries:
            try:
                client = self._get_http_client()

                # Store request details for debugging
                self._last_request = {
                    "method": method,
                    "endpoint": endpoint,
                    "url": self.jsonrpc_url,
                    "params": params,
                    "data": params[0].get("data") if params else None,
                    "timestamp": time.time(),
                }

                # Apply per-endpoint timeout if configured
                if endpoint_timeout and self._http_client:
                    original_timeout = self._http_client.timeout
                    self._http_client.timeout = endpoint_timeout
                else:
                    original_timeout = None

                self._active_requests += 1
                try:
                    response = client.post(
                        self.jsonrpc_url,
                        json=request,
                        headers=headers,
                    )
                except httpx.PoolTimeout:
                    self._pool_exhaustion_count += 1
                    self._pool_exhaustion_timestamps.append(time.perf_counter())
                    logger.warning(
                        "Connection pool exhausted for %s (total: %d)",
                        endpoint,
                        self._pool_exhaustion_count,
                        extra=self._log_context(
                            request_id=request_id,
                            endpoint=endpoint,
                            active_requests=self._active_requests,
                            max_connections=self._max_connections,
                        ),
                    )
                    raise
                finally:
                    self._active_requests -= 1
                    if original_timeout is not None and self._http_client:
                        self._http_client.timeout = original_timeout

                # Store response details
                self._last_response = {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                }

                response.raise_for_status()

                data = response.json()

                # Normalize JSON-RPC 2.0 (apiver-3) responses to the legacy
                # result-list shape so downstream handling stays uniform:
                # errors arrive as a top-level "error" object, success as a
                # "result" object (not a list with per-entry status).
                if is_v3 and isinstance(data, dict) and "jsonrpc" in data:
                    if "error" in data:
                        err = data["error"] or {}
                        v3_code = err.get("code", "?")
                        v3_msg = err.get("message", "Unknown error")
                        if not self._api_key and "session" in str(v3_msg).lower():
                            self._session_token = None
                            self.login()
                            request["session"] = self._session_token
                            continue
                        raise RuntimeError(
                            f"JSON-RPC request failed " f"(code {v3_code}): {v3_msg}"
                        )
                    v3_result = data.get("result")
                    if isinstance(v3_result, dict):
                        entry: dict[str, Any] = dict(v3_result)
                    else:
                        entry = {"data": v3_result}
                    entry["status"] = {"code": 0, "message": "OK"}
                    entry.setdefault("url", endpoint)
                    data = {"id": data.get("id"), "result": [entry]}

                # Check for API-level errors in the JSON-RPC result
                result = data.get("result", [{}])[0] if data.get("result") else {}
                status = result.get("status", {})

                if status.get("code") != 0:
                    error_code = status.get("code", "?")
                    error_msg = status.get("message", "Unknown error")
                    # Session expired - try to re-login (only for session-based auth)
                    if not self._api_key and (
                        "session" in error_msg.lower() or error_code == -11
                    ):
                        self._session_token = None
                        self.login()
                        request["session"] = self._session_token
                        continue

                    raise RuntimeError(
                        f"JSON-RPC request failed " f"(code {error_code}): {error_msg}"
                    )

                # Success
                duration = time.perf_counter() - start_time
                self._last_response_time = duration

                # Record response time for adaptive backpressure detection
                self._record_response_time(endpoint, duration)

                self._record_circuit_breaker_success()
                self._retry_stats["successful_requests"] += 1

                # Track session usage time (for idle timeout calculation)
                if self._session_token:
                    self._session_last_used = time.perf_counter()

                logger.debug(
                    "JSON-RPC %s %s completed in %.3fs",
                    method,
                    endpoint,
                    duration,
                    extra=self._log_context(
                        request_id=request_id,
                        endpoint=endpoint,
                        duration_seconds=round(duration, 3),
                    ),
                )

                # Add HTTP metadata to response (transport-layer visibility)
                data["_http_metadata"] = {
                    "status_code": response.status_code,
                    "method": "POST",  # JSON-RPC always uses POST
                    "url": self.jsonrpc_url,
                    "response_time": round(duration * 1000, 2),  # milliseconds
                }

                # Operation audit log
                if self._track_operations:
                    from datetime import datetime, timezone

                    self._operations.append(
                        {
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                            "request_id": request_id,
                            "method": method,
                            "api_type": "jsonrpc",
                            "path": endpoint,
                            "data": params[0].get("data") if params else None,
                            "status_code": response.status_code,
                            "success": True,
                            "adom": self._adom,
                        }
                    )

                # Audit logging via handler/callback
                self._log_audit(
                    method=method.upper(),
                    endpoint=self.jsonrpc_url,
                    api_type="jsonrpc",
                    path=endpoint,
                    data=params[0].get("data") if params else None,
                    params=None,
                    status_code=response.status_code,
                    success=True,
                    duration_ms=int(duration * 1000),
                    request_id=request_id,
                )

                return data

            except httpx.TimeoutException as e:
                last_error = e
                self._record_circuit_breaker_failure(endpoint)
                if self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    delay = self._get_retry_delay(attempt - 1, endpoint=endpoint)
                    logger.warning(
                        "Request timeout, retrying in %.1fs (attempt %d/%d)",
                        delay,
                        attempt,
                        self._max_retries + 1,
                    )
                    time.sleep(delay)
                    continue
                raise

            except httpx.HTTPStatusError as e:
                last_error = e
                self._record_circuit_breaker_failure(endpoint)
                # _should_retry handles both 429 and 5xx; pass response for Retry-After
                if self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    delay = self._get_retry_delay(
                        attempt - 1, response=e.response, endpoint=endpoint
                    )
                    logger.warning(
                        "HTTP error %d, retrying in %.1fs (attempt %d/%d)",
                        e.response.status_code,
                        delay,
                        attempt,
                        self._max_retries + 1,
                    )
                    time.sleep(delay)
                    continue
                raise

            except Exception as e:
                last_error = e
                self._record_circuit_breaker_failure(endpoint)
                if self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    delay = self._get_retry_delay(attempt - 1, endpoint=endpoint)
                    logger.warning(
                        "Request error, retrying in %.1fs (attempt %d/%d): %s",
                        delay,
                        attempt,
                        self._max_retries + 1,
                        e,
                    )
                    time.sleep(delay)
                    continue
                raise

        # All retries exhausted (CB failure already recorded on each attempt)
        self._retry_stats["failed_requests"] += 1
        self._rate_stats.record_error()

        # Audit log the failure
        if last_error is not None:
            duration = time.perf_counter() - start_time
            self._log_audit(
                method=method.upper(),
                endpoint=self.jsonrpc_url,
                api_type="jsonrpc",
                path=endpoint,
                data=params[0].get("data") if params else None,
                params=None,
                status_code=0,
                success=False,
                duration_ms=int(duration * 1000),
                request_id=request_id,
                error=str(last_error),
            )
            raise last_error

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
            "adaptive_retry_enabled": self._adaptive_retry,
        }

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get HTTP connection pool statistics.

        Returns:
            dict with http2_enabled, pool sizes, active requests, pool
            exhaustion count, and circuit breaker state.
        """
        return {
            "http2_enabled": True,
            "max_connections": self._max_connections,
            "max_keepalive_connections": self._max_keepalive_connections,
            "active_requests": self._active_requests,
            "total_requests": self._total_requests,
            "pool_exhaustion_count": self._pool_exhaustion_count,
            "client_active": self._http_client is not None,
            "circuit_breaker_state": self._circuit_breaker["state"],
            "consecutive_failures": self._circuit_breaker["consecutive_failures"],
            "last_failure_time": self._circuit_breaker["last_failure_time"],
        }

    def inspect_last_request(self) -> dict[str, Any]:
        """
        Get details of the last API request for debugging.

        Returns:
            dict with method, endpoint, params, response_time_ms,
            and status_code. Returns error key if no requests yet.

        Example:
            >>> client.execute("get", [{"url": "/dvmdb/device"}])
            >>> info = client.inspect_last_request()
            >>> print(f"Last request took {info['response_time_ms']:.2f}ms")
        """
        if not self._last_request:
            return {"error": "No requests have been made yet"}

        result: dict[str, Any] = {
            "method": self._last_request.get("method"),
            "endpoint": self._last_request.get("endpoint"),
            "url": self._last_request.get("url"),
            "params": self._last_request.get("params"),
            "response_time_ms": (
                round(self._last_response_time * 1000, 2)
                if self._last_response_time
                else None
            ),
        }

        if self._last_response:
            result["status_code"] = self._last_response.get("status_code")

        return result

    def get_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of all tracked API operations.

        Only populated when track_operations=True was passed to constructor.

        Returns:
            List of operation dicts with timestamp, request_id, method,
            api_type, path, data, status_code, success, adom.
        """
        return self._operations.copy()

    def get_write_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of write operations only (add/set/update/delete/exec).

        Returns:
            List of write operation dicts (same format as get_operations()).
        """
        return [
            op
            for op in self._operations
            if op.get("method") in ("add", "set", "update", "delete", "exec")
        ]
