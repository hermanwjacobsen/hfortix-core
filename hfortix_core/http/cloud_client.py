"""
Cloud HTTP Client for OAuth-based Fortinet Cloud APIs

This module contains the CloudHTTPClient class which handles HTTP communication
with Fortinet cloud services (FortiCare, FortiCloud, etc.) using OAuth 2.0
Bearer token authentication.
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeAlias

if TYPE_CHECKING:
    from collections.abc import Coroutine

from urllib.parse import urlencode

import httpx
from hfortix_core.http.base import BaseHTTPClient

logger = logging.getLogger("hfortix.http.cloud")

# Type alias for API responses
HTTPResponse: TypeAlias = dict[str, Any]

__all__ = ["CloudHTTPClient", "HTTPResponse"]


class CloudHTTPClient(BaseHTTPClient):
    """
    HTTP client for Fortinet Cloud APIs with OAuth 2.0 authentication.

    Designed for cloud services like FortiCare Asset Management API v3,
    FortiCloud, and other OAuth-protected Fortinet cloud endpoints.

    Key Differences from HTTPClient:
    - Uses OAuth 2.0 Bearer tokens (Authorization: Bearer <token>)
    - No API key authentication
    - No VDOM support
    - Cloud-specific error handling
    - Rate limiting aware (100/min, 1000/hour for FortiCare)

    Authentication:
        The client expects an OAuth access token obtained from:
        https://customerapiauth.fortinet.com/api/v1/oauth/token

    Rate Limits (FortiCare Asset Management):
        - 100 calls per minute
        - 1000 calls per hour
        - 10 errors per hour
        - Batch operations: max 10 units, max 5 errors per batch

    Example:
        >>> client = CloudHTTPClient(
        ...     url="https://support.fortinet.com",
        ...     oauth_token="your_oauth_token_here"
        ... )
        >>> response = client.get("/ES/api/registration/v3/products/list")
        >>> client.logout()

    Note:
        The interface differs from HTTPClient — no vdom/api_type params, and
        methods return a response envelope dict rather than the raw JSON body.
    """

    def __init__(
        self,
        url: str,
        oauth_token: str,
        verify: bool = True,
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
        user_agent: Optional[str] = None,
        read_only: bool = False,
        track_operations: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
        token_callback: Optional[Callable[[], str]] = None,
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
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
    ) -> None:
        """
        Initialize Cloud HTTP client.

        Args:
            url: Base URL of the cloud service (e.g., "https://support.fortinet.com")
            oauth_token: OAuth 2.0 Bearer token for authentication
            verify: Enable SSL certificate verification (default: True)
            max_retries: Maximum number of retry attempts (default: 3)
            connect_timeout: Connection timeout in seconds (default: 10.0)
            read_timeout: Read timeout in seconds (default: 300.0)
            circuit_breaker_threshold: Failures before circuit opens (default: 5)
            circuit_breaker_timeout: Circuit breaker timeout in seconds (default: 60.0)
            max_connections: Maximum number of connections (default: 100)
            max_keepalive_connections: Max keepalive connections (default: 20)
            adaptive_retry: Enable adaptive retry based on response times
            retry_strategy: 'exponential' or 'linear' backoff
            retry_jitter: Add random jitter to retry delays
            user_agent: Custom User-Agent header (optional)
            read_only: Enable read-only mode - simulate write operations without executing (default: False)
            track_operations: Enable operation tracking - maintain audit log of all API calls (default: False)
            audit_handler: Handler for audit logging (implements AuditHandler protocol)
            audit_callback: Custom callback function for audit logging (alternative to audit_handler)
            user_context: Optional dict with user/application context to include in audit logs
            token_callback: Optional callback to get fresh token before each request (returns str)
                           Useful with CloudSession to ensure token is valid before each request
            rate_limit: Enable rate limiting enforcement (default: False)
            rate_limit_strategy: 'queue', 'drop', or 'raise' (default: 'queue')
            rate_limit_max_requests: Max requests per window (default: 100)
            rate_limit_window_seconds: Time window in seconds (default: 60.0)
            rate_limit_queue_size: Max queue size (default: 100)
            rate_limit_queue_timeout: Max wait time in queue (default: 30.0)
            rate_limit_queue_overflow: 'block' or 'drop' on overflow (default: 'block')
            circuit_breaker: Enable circuit breaker (default: False)
            circuit_breaker_half_open_calls: Calls to test in half-open state (default: 3)
            circuit_breaker_auto_retry: Wait and retry instead of raising immediately when
                                       circuit breaker is open (default: False)
            circuit_breaker_max_retries: Max auto-retry attempts when circuit open (default: 3)
            circuit_breaker_retry_delay: Seconds between auto-retry attempts (default: 5.0)

        Raises:
            ValueError: If oauth_token is empty or invalid parameters
        """
        if not oauth_token:
            raise ValueError("oauth_token is required for cloud authentication")

        # Initialize base client (no vdom for cloud APIs)
        super().__init__(
            url=url,
            verify=verify,
            vdom=None,  # Cloud APIs don't use VDOMs
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

        self._oauth_token = oauth_token
        self._token_callback = token_callback
        if user_agent is None:
            from hfortix_core import __version__
            user_agent = f"hfortix/{__version__}"
        self._user_agent = user_agent
        self._session: Optional[httpx.Client] = None

        # Operation tracking (read_only and audit already set in parent)
        self._track_operations = track_operations
        self._operations: list[dict[str, Any]] = []

        # Connection pool monitoring
        self._active_requests = 0
        self._total_requests = 0
        self._max_connections = max_connections
        self._max_keepalive_connections = max_keepalive_connections
        self._pool_exhaustion_count = 0
        self._pool_exhaustion_timestamps: list[float] = []

        # Request inspection for debugging
        self._last_request: Optional[dict[str, Any]] = None
        self._last_response: Optional[dict[str, Any]] = None
        self._last_response_time: Optional[float] = None

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
        else:
            self._rate_limiter = None
    
    def _refresh_token_if_needed(self) -> None:
        """
        Call token_callback to get fresh token if callback is configured.
        
        This is called before each request to ensure token is valid.
        Used with CloudSession.ensure_token_valid() to auto-refresh expiring tokens.
        """
        if self._token_callback:
            fresh_token = self._token_callback()
            if fresh_token != self._oauth_token:
                self._oauth_token = fresh_token
                # Update session headers if session exists
                if self._session:
                    self._session.headers["Authorization"] = f"Bearer {fresh_token}"

    def _get_session(self) -> httpx.Client:
        """
        Get or create HTTP session with OAuth authentication.

        Returns:
            Configured httpx.Client instance

        Note:
            Sessions are created lazily and reused for connection pooling.
        """
        if self._session is None:
            # Build timeout configuration
            timeout = httpx.Timeout(
                connect=self._connect_timeout,
                read=self._read_timeout,
                write=30.0,
                pool=5.0,
            )

            # Configure connection limits
            limits = httpx.Limits(
                max_connections=self._max_connections,
                max_keepalive_connections=self._max_keepalive_connections,
                keepalive_expiry=30.0,
            )

            # Build headers with OAuth Bearer token
            headers = {
                "Authorization": f"Bearer {self._oauth_token}",
                "User-Agent": self._user_agent,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

            self._session = httpx.Client(
                base_url=self._url,
                verify=self._verify,
                timeout=timeout,
                limits=limits,
                headers=headers,
                http2=True,  # Enable HTTP/2 for better performance
                follow_redirects=True,
            )

        return self._session

    def _log_audit_operation(
        self,
        method: str,
        path: str,
        params: Optional[dict[str, Any]],
        data: Optional[dict[str, Any]],
        status_code: int,
        response_time: float,
        success: bool,
        error: Optional[str] = None,
        request_id: Optional[str] = None,
    ) -> None:
        """
        Log API operation via the base class audit infrastructure.

        Delegates to _log_audit() so all audit handlers (syslog, file,
        stream, composite) and callbacks are called consistently.

        Args:
            method: HTTP method
            path: API endpoint path
            params: Query parameters
            data: Request body
            status_code: HTTP status code
            response_time: Response time in seconds
            success: Whether operation succeeded
            error: Error message if operation failed
            request_id: Request ID (generated if not provided)
        """
        import uuid
        self._log_audit(
            method=method,
            endpoint=f"{self._url}{path}",
            api_type="cloud",
            path=path,
            data=data,
            params=params,
            status_code=status_code,
            success=success,
            duration_ms=int(response_time * 1000),
            request_id=request_id or str(uuid.uuid4())[:8],
            error=error,
        )

    def get(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> HTTPResponse:
        """
        Send GET request to cloud API.

        Args:
            path: API endpoint path (e.g., "/ES/api/registration/v3/products/list")
            params: Query parameters (optional)
            timeout: Override default timeout in seconds (optional)

        Returns:
            Response envelope containing:
            - data: JSON response body
            - http_status_code: HTTP status code
            - response_time: Response time in seconds
            - request_info: Request metadata (method, url, params)

        Raises:
            httpx.HTTPStatusError: For HTTP error responses
            httpx.TimeoutException: If request times out
            httpx.RequestError: For network errors
        """
        # Refresh token if callback configured (CloudSession integration)
        self._refresh_token_if_needed()

        session = self._get_session()

        # Build query string if params provided
        url = path
        if params:
            # Filter out None values
            clean_params = {k: v for k, v in params.items() if v is not None}
            if clean_params:
                url = f"{path}?{urlencode(clean_params)}"

        logger.debug(f"GET {url}")

        # Override timeout if specified
        request_timeout = timeout if timeout is not None else self._read_timeout

        # Rate limiting enforcement
        if self._rate_limiter is not None:
            if not self._rate_limiter.acquire():
                logger.warning("Cloud GET %s dropped by rate limiter", path)
                return {"status": "error", "message": "Rate limit exceeded - request dropped"}

        try:
            # Circuit breaker check
            try:
                self._check_circuit_breaker(path)
            except Exception:
                logger.error("Circuit breaker blocked cloud GET %s", path)
                raise
        finally:
            if self._rate_limiter is not None:
                self._rate_limiter.release()

        # Track counters
        self._active_requests += 1
        self._total_requests += 1
        self._rate_stats.record_call()

        last_error: Optional[Exception] = None
        try:
            for attempt in range(self._max_retries + 1):
                try:
                    start_time = time.time()
                    response = session.get(url, timeout=request_timeout)
                    response_time = time.time() - start_time

                    response.raise_for_status()

                    # Record circuit breaker success
                    self._record_circuit_breaker_success()

                    # Store last request for debugging
                    self._last_request = {
                        "method": "GET",
                        "endpoint": path,
                        "url": url,
                        "params": params,
                        "timestamp": time.time(),
                    }
                    self._last_response = {
                        "status_code": response.status_code,
                        "body": response.json(),
                    }
                    self._last_response_time = response_time

                    # Track operation if enabled
                    if self._track_operations:
                        import datetime
                        self._operations.append({
                            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                            "method": "GET",
                            "path": path,
                            "params": params,
                            "data": None,
                            "status_code": response.status_code,
                            "read_only_simulated": False,
                        })

                    # Call audit handlers if configured
                    self._log_audit_operation(
                        method="GET",
                        path=path,
                        params=params,
                        data=None,
                        status_code=response.status_code,
                        response_time=response_time,
                        success=True,
                    )

                    # Return envelope with metadata
                    return {
                        "data": response.json(),
                        "http_status_code": response.status_code,
                        "response_time": response_time,
                        "request_info": {
                            "method": "GET",
                            "url": url,
                            "params": params,
                        },
                    }

                except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError) as e:
                    last_error = e
                    self._record_circuit_breaker_failure(path)
                    if self._should_retry(e, attempt, path):
                        delay = self._get_retry_delay(attempt, endpoint=path)
                        logger.warning(
                            "Cloud GET %s failed (attempt %d/%d), retrying in %.1fs: %s",
                            path, attempt + 1, self._max_retries + 1, delay, e,
                        )
                        time.sleep(delay)
                        continue
                    raise
        finally:
            self._active_requests -= 1

        # All retries exhausted
        if last_error is not None:
            raise last_error

    def post(
        self,
        path: str,
        data: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> HTTPResponse:
        """
        Send POST request to cloud API.

        Args:
            path: API endpoint path
            data: Request body data (will be JSON-encoded)
            params: Query parameters (optional)
            timeout: Override default timeout in seconds (optional)

        Returns:
            Response envelope containing:
            - data: JSON response body
            - http_status_code: HTTP status code
            - response_time: Response time in seconds
            - request_info: Request metadata (method, url, params, data)

        Raises:
            httpx.HTTPStatusError: For HTTP error responses
            httpx.TimeoutException: If request times out
            httpx.RequestError: For network errors
        """
        # Refresh token if callback configured (CloudSession integration)
        self._refresh_token_if_needed()

        session = self._get_session()

        # Build query string if params provided
        url = path
        if params:
            clean_params = {k: v for k, v in params.items() if v is not None}
            if clean_params:
                url = f"{path}?{urlencode(clean_params)}"

        logger.debug(f"POST {url} (read_only={self._read_only})")

        # Override timeout if specified
        request_timeout = timeout if timeout is not None else self._read_timeout

        # Read-only mode: simulate write operations (no network, no CB/rate limiter)
        if self._read_only:
            logger.info(f"READ-ONLY: Simulating POST {url}")
            response_time = 0.001
            self._last_request = {
                "method": "POST",
                "endpoint": path,
                "url": url,
                "params": params,
                "data": data,
                "timestamp": time.time(),
            }
            self._last_response = {"status_code": 200, "body": {"status": 0, "message": "Simulated (read-only mode)"}}
            self._last_response_time = response_time
            if self._track_operations:
                import datetime
                self._operations.append({
                    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "method": "POST",
                    "path": path,
                    "params": params,
                    "data": data,
                    "status_code": 200,
                    "read_only_simulated": True,
                })
            self._log_audit_operation(method="POST", path=path, params=params, data=data, status_code=200, response_time=response_time, success=True)
            return {"data": {"status": 0, "message": "Simulated (read-only mode)"}, "http_status_code": 200, "response_time": response_time, "request_info": {"method": "POST", "url": url, "params": params, "data": data}}

        # Rate limiting enforcement
        if self._rate_limiter is not None:
            if not self._rate_limiter.acquire():
                logger.warning("Cloud POST %s dropped by rate limiter", path)
                return {"status": "error", "message": "Rate limit exceeded - request dropped"}

        try:
            try:
                self._check_circuit_breaker(path)
            except Exception:
                logger.error("Circuit breaker blocked cloud POST %s", path)
                raise
        finally:
            if self._rate_limiter is not None:
                self._rate_limiter.release()

        # Track counters
        self._active_requests += 1
        self._total_requests += 1
        self._rate_stats.record_call()

        last_error: Optional[Exception] = None
        try:
            for attempt in range(self._max_retries + 1):
                try:
                    start_time = time.time()
                    response = session.post(url, json=data, timeout=request_timeout)
                    response_time = time.time() - start_time

                    response.raise_for_status()

                    self._record_circuit_breaker_success()

                    self._last_request = {
                        "method": "POST",
                        "endpoint": path,
                        "url": url,
                        "params": params,
                        "data": data,
                        "timestamp": time.time(),
                    }
                    self._last_response = {"status_code": response.status_code, "body": response.json()}
                    self._last_response_time = response_time

                    if self._track_operations:
                        import datetime
                        self._operations.append({
                            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                            "method": "POST",
                            "path": path,
                            "params": params,
                            "data": data,
                            "status_code": response.status_code,
                            "read_only_simulated": False,
                        })

                    self._log_audit_operation(method="POST", path=path, params=params, data=data, status_code=response.status_code, response_time=response_time, success=True)

                    return {
                        "data": response.json(),
                        "http_status_code": response.status_code,
                        "response_time": response_time,
                        "request_info": {"method": "POST", "url": url, "params": params, "data": data},
                    }

                except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError) as e:
                    last_error = e
                    self._record_circuit_breaker_failure(path)
                    if self._should_retry(e, attempt, path):
                        delay = self._get_retry_delay(attempt, endpoint=path)
                        logger.warning("Cloud POST %s failed (attempt %d/%d), retrying in %.1fs: %s", path, attempt + 1, self._max_retries + 1, delay, e)
                        time.sleep(delay)
                        continue
                    raise
        finally:
            self._active_requests -= 1

        if last_error is not None:
            raise last_error

    def put(
        self,
        path: str,
        data: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> HTTPResponse:
        """
        Send PUT request to cloud API.

        Args:
            path: API endpoint path
            data: Request body data (will be JSON-encoded)
            params: Query parameters (optional)
            timeout: Override default timeout in seconds (optional)

        Returns:
            Response envelope containing:
            - data: JSON response body
            - http_status_code: HTTP status code
            - response_time: Response time in seconds
            - request_info: Request metadata (method, url, params, data)

        Raises:
            httpx.HTTPStatusError: For HTTP error responses
            httpx.TimeoutException: If request times out
            httpx.RequestError: For network errors
        """
        # Refresh token if callback configured (CloudSession integration)
        self._refresh_token_if_needed()
        
        session = self._get_session()

        url = path
        if params:
            clean_params = {k: v for k, v in params.items() if v is not None}
            if clean_params:
                url = f"{path}?{urlencode(clean_params)}"

        logger.debug(f"PUT {url} (read_only={self._read_only})")

        request_timeout = timeout if timeout is not None else self._read_timeout

        # Read-only mode: simulate write operations (no network, no CB/rate limiter)
        if self._read_only:
            logger.info(f"READ-ONLY: Simulating PUT {url}")
            response_time = 0.001
            self._last_request = {"method": "PUT", "endpoint": path, "url": url, "params": params, "data": data, "timestamp": time.time()}
            self._last_response = {"status_code": 200, "body": {"status": 0, "message": "Simulated (read-only mode)"}}
            self._last_response_time = response_time
            if self._track_operations:
                import datetime
                self._operations.append({
                    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "method": "PUT",
                    "path": path,
                    "params": params,
                    "data": data,
                    "status_code": 200,
                    "read_only_simulated": True,
                })
            self._log_audit_operation(method="PUT", path=path, params=params, data=data, status_code=200, response_time=response_time, success=True)
            return {"data": {"status": 0, "message": "Simulated (read-only mode)"}, "http_status_code": 200, "response_time": response_time, "request_info": {"method": "PUT", "url": url, "params": params, "data": data}}

        # Rate limiting enforcement
        if self._rate_limiter is not None:
            if not self._rate_limiter.acquire():
                logger.warning("Cloud PUT %s dropped by rate limiter", path)
                return {"status": "error", "message": "Rate limit exceeded - request dropped"}

        try:
            try:
                self._check_circuit_breaker(path)
            except Exception:
                logger.error("Circuit breaker blocked cloud PUT %s", path)
                raise
        finally:
            if self._rate_limiter is not None:
                self._rate_limiter.release()

        # Track counters
        self._active_requests += 1
        self._total_requests += 1
        self._rate_stats.record_call()

        last_error: Optional[Exception] = None
        try:
            for attempt in range(self._max_retries + 1):
                try:
                    start_time = time.time()
                    response = session.put(url, json=data, timeout=request_timeout)
                    response_time = time.time() - start_time

                    response.raise_for_status()

                    self._record_circuit_breaker_success()

                    self._last_request = {"method": "PUT", "endpoint": path, "url": url, "params": params, "data": data, "timestamp": time.time()}
                    self._last_response = {"status_code": response.status_code, "body": response.json()}
                    self._last_response_time = response_time

                    if self._track_operations:
                        import datetime
                        self._operations.append({
                            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                            "method": "PUT",
                            "path": path,
                            "params": params,
                            "data": data,
                            "status_code": response.status_code,
                            "read_only_simulated": False,
                        })

                    self._log_audit_operation(method="PUT", path=path, params=params, data=data, status_code=response.status_code, response_time=response_time, success=True)

                    return {
                        "data": response.json(),
                        "http_status_code": response.status_code,
                        "response_time": response_time,
                        "request_info": {"method": "PUT", "url": url, "params": params, "data": data},
                    }

                except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError) as e:
                    last_error = e
                    self._record_circuit_breaker_failure(path)
                    if self._should_retry(e, attempt, path):
                        delay = self._get_retry_delay(attempt, endpoint=path)
                        logger.warning("Cloud PUT %s failed (attempt %d/%d), retrying in %.1fs: %s", path, attempt + 1, self._max_retries + 1, delay, e)
                        time.sleep(delay)
                        continue
                    raise
        finally:
            self._active_requests -= 1

        if last_error is not None:
            raise last_error

    def delete(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> HTTPResponse:
        """
        Send DELETE request to cloud API.

        Args:
            path: API endpoint path
            params: Query parameters (optional)
            timeout: Override default timeout in seconds (optional)

        Returns:
            Response envelope containing:
            - data: JSON response body
            - http_status_code: HTTP status code
            - response_time: Response time in seconds
            - request_info: Request metadata (method, url, params)

        Raises:
            httpx.HTTPStatusError: For HTTP error responses
            httpx.TimeoutException: If request times out
            httpx.RequestError: For network errors
        """
        # Refresh token if callback configured (CloudSession integration)
        self._refresh_token_if_needed()
        
        session = self._get_session()

        url = path
        if params:
            clean_params = {k: v for k, v in params.items() if v is not None}
            if clean_params:
                url = f"{path}?{urlencode(clean_params)}"

        logger.debug(f"DELETE {url} (read_only={self._read_only})")

        request_timeout = timeout if timeout is not None else self._read_timeout

        # Read-only mode: simulate write operations (no network, no CB/rate limiter)
        if self._read_only:
            logger.info(f"READ-ONLY: Simulating DELETE {url}")
            response_time = 0.001
            self._last_request = {"method": "DELETE", "endpoint": path, "url": url, "params": params, "timestamp": time.time()}
            self._last_response = {"status_code": 200, "body": {"status": 0, "message": "Simulated (read-only mode)"}}
            self._last_response_time = response_time
            if self._track_operations:
                import datetime
                self._operations.append({
                    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "method": "DELETE",
                    "path": path,
                    "params": params,
                    "data": None,
                    "status_code": 200,
                    "read_only_simulated": True,
                })
            self._log_audit_operation(method="DELETE", path=path, params=params, data=None, status_code=200, response_time=response_time, success=True)
            return {"data": {"status": 0, "message": "Simulated (read-only mode)"}, "http_status_code": 200, "response_time": response_time, "request_info": {"method": "DELETE", "url": url, "params": params}}

        # Rate limiting enforcement
        if self._rate_limiter is not None:
            if not self._rate_limiter.acquire():
                logger.warning("Cloud DELETE %s dropped by rate limiter", path)
                return {"status": "error", "message": "Rate limit exceeded - request dropped"}

        try:
            try:
                self._check_circuit_breaker(path)
            except Exception:
                logger.error("Circuit breaker blocked cloud DELETE %s", path)
                raise
        finally:
            if self._rate_limiter is not None:
                self._rate_limiter.release()

        # Track counters
        self._active_requests += 1
        self._total_requests += 1
        self._rate_stats.record_call()

        last_error: Optional[Exception] = None
        try:
            for attempt in range(self._max_retries + 1):
                try:
                    start_time = time.time()
                    response = session.delete(url, timeout=request_timeout)
                    response_time = time.time() - start_time

                    response.raise_for_status()

                    self._record_circuit_breaker_success()

                    self._last_request = {"method": "DELETE", "endpoint": path, "url": url, "params": params, "timestamp": time.time()}
                    self._last_response = {"status_code": response.status_code, "body": response.json()}
                    self._last_response_time = response_time

                    if self._track_operations:
                        import datetime
                        self._operations.append({
                            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                            "method": "DELETE",
                            "path": path,
                            "params": params,
                            "data": None,
                            "status_code": response.status_code,
                            "read_only_simulated": False,
                        })

                    self._log_audit_operation(method="DELETE", path=path, params=params, data=None, status_code=response.status_code, response_time=response_time, success=True)

                    return {
                        "data": response.json(),
                        "http_status_code": response.status_code,
                        "response_time": response_time,
                        "request_info": {"method": "DELETE", "url": url, "params": params},
                    }

                except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError) as e:
                    last_error = e
                    self._record_circuit_breaker_failure(path)
                    if self._should_retry(e, attempt, path):
                        delay = self._get_retry_delay(attempt, endpoint=path)
                        logger.warning("Cloud DELETE %s failed (attempt %d/%d), retrying in %.1fs: %s", path, attempt + 1, self._max_retries + 1, delay, e)
                        time.sleep(delay)
                        continue
                    raise
        finally:
            self._active_requests -= 1

        if last_error is not None:
            raise last_error

    def get_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of all tracked API operations.

        Returns all tracked operations (GET/POST/PUT/DELETE) in chronological order.
        Only available when track_operations=True was passed to constructor.

        Returns:
            List of operation dictionaries with keys:
                - timestamp: ISO 8601 timestamp
                - method: HTTP method (GET/POST/PUT/DELETE)
                - path: API endpoint path
                - data: Request payload (for POST/PUT), None otherwise
                - status_code: HTTP response status code
                - read_only_simulated: True if operation was simulated in read-only mode

        Example:
            >>> client = CloudHTTPClient(
            ...     url="https://support.fortinet.com",
            ...     oauth_token="...",
            ...     track_operations=True
            ... )
            >>> client.post("/api/v3/products/list", data={"serial_number": "FGT*"})
            >>> ops = client.get_operations()
            >>> print(ops[0])
            {
                'timestamp': '2026-02-06T10:30:15Z',
                'method': 'POST',
                'path': '/api/v3/products/list',
                'data': {'serial_number': 'FGT*'},
                'status_code': 200,
                'read_only_simulated': False
            }
        """
        return self._operations.copy()

    def get_write_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of write operations only (POST/PUT/DELETE).

        Filters tracked operations to return only write operations, excluding GET requests.

        Returns:
            List of write operation dictionaries (same format as get_operations())

        Example:
            >>> client = CloudHTTPClient(
            ...     url="https://support.fortinet.com",
            ...     oauth_token="...",
            ...     track_operations=True
            ... )
            >>> client.get("/api/v3/products/list")  # GET - excluded
            >>> client.post("/api/v3/products/register", data={...})  # POST - included
            >>> client.delete("/api/v3/products/123")  # DELETE - included
            >>> write_ops = client.get_write_operations()
            >>> len(write_ops)  # Returns 2 (POST and DELETE only)
            2
        """
        return [
            op
            for op in self._operations
            if op["method"] in ("POST", "PUT", "DELETE")
        ]

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get connection pool statistics.

        Returns:
            Dictionary with connection pool metrics:
                - http2_enabled: Whether HTTP/2 is enabled
                - max_connections: Maximum allowed connections
                - max_keepalive_connections: Maximum keepalive connections
                - active_requests: Number of currently active requests
                - total_requests: Total number of requests made
                - client_active: Whether HTTP session is initialized
                - circuit_breaker_state: Current circuit breaker state
                - consecutive_failures: Number of consecutive failures
                - last_failure_time: Timestamp of last failure

        Example:
            >>> client = CloudHTTPClient(url="https://support.fortinet.com", oauth_token="...")
            >>> stats = client.get_connection_stats()
            >>> print(f"Active: {stats['active_requests']}/{stats['max_connections']}")
            Active: 2/100
        """
        return {
            "http2_enabled": True,
            "max_connections": self._max_connections,
            "max_keepalive_connections": self._max_keepalive_connections,
            "active_requests": self._active_requests,
            "total_requests": self._total_requests,
            "pool_exhaustion_count": self._pool_exhaustion_count,
            "client_active": self._session is not None,
            "circuit_breaker_state": self._circuit_breaker["state"],
            "consecutive_failures": self._circuit_breaker["consecutive_failures"],
            "last_failure_time": self._circuit_breaker["last_failure_time"],
        }

    def inspect_last_request(self) -> dict[str, Any]:
        """
        Get detailed information about the last HTTP request/response.

        Useful for debugging and understanding what was sent/received.

        Returns:
            Dictionary with last request details:
                - method: HTTP method (GET/POST/PUT/DELETE)
                - endpoint: API endpoint path (without query string)
                - url: Full URL with query string
                - params: Query parameters
                - response_time_ms: Response time in milliseconds
                - status_code: HTTP status code (if response available)
            Or {"error": "..."} if no requests have been made yet.

        Example:
            >>> client = CloudHTTPClient(url="https://support.fortinet.com", oauth_token="...")
            >>> client.get("/api/v3/products/list")
            >>> last = client.inspect_last_request()
            >>> print(f"Last request took {last['response_time_ms']}ms")
            Last request took 234.5ms
        """
        if not self._last_request:
            return {"error": "No requests have been made yet"}

        result = {
            "method": self._last_request.get("method"),
            "endpoint": self._last_request.get("endpoint"),
            "url": self._last_request.get("url"),
            "params": self._last_request.get("params"),
            "response_time_ms": round(self._last_response_time * 1000, 2) if self._last_response_time is not None else None,
        }
        if self._last_response:
            result["status_code"] = self._last_response.get("status_code")
        return result

    def close(self) -> None:
        """
        Close the HTTP session and clean up resources.

        Alias for logout() — conforms to the standard client interface.
        """
        self.logout()

    def logout(self) -> None:
        """
        Close the HTTP session and clean up resources.

        Note:
            OAuth token revocation should be handled separately via the
            authentication service. This method only closes the HTTP connection.
        """
        if self._session is not None:
            self._session.close()
            self._session = None
            logger.debug("Cloud HTTP session closed")

    def __enter__(self) -> CloudHTTPClient:
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit - ensures session is closed."""
        self.logout()

    def __del__(self) -> None:
        """Destructor - cleanup session if not already closed."""
        if self._session is not None:
            try:
                self._session.close()
            except Exception:
                pass  # Ignore errors during cleanup
