"""
Cloud HTTP Client for OAuth-based Fortinet Cloud APIs

This module contains the CloudHTTPClient class which handles HTTP communication
with Fortinet cloud services (FortiCare, FortiCloud, etc.) using OAuth 2.0
Bearer token authentication.
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Any, Optional, TypeAlias

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

    Protocol Implementation:
        This class implements the IHTTPClient protocol, allowing interchangeable
        use with HTTPClient and AsyncHTTPClient.
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
        )

        self._oauth_token = oauth_token
        self._user_agent = user_agent or "hfortix-cloud/1.0"
        self._session: Optional[httpx.Client] = None
        
        # Read-only mode and operation tracking
        self._read_only = read_only
        self._track_operations = track_operations
        self._operations: list[dict[str, Any]] = [] if track_operations else []
        
        # Audit logging
        self._audit_handler = audit_handler
        self._audit_callback = audit_callback
        self._user_context = user_context or {}
        
        # Connection pool monitoring
        self._active_requests = 0
        self._total_requests = 0
        self._max_connections = max_connections
        self._max_keepalive_connections = max_keepalive_connections
        
        # Request inspection for debugging
        self._last_request: Optional[dict[str, Any]] = None
        self._last_response: Optional[dict[str, Any]] = None
        self._last_response_time: Optional[float] = None

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
                max_connections=100,
                max_keepalive_connections=20,
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
    ) -> None:
        """
        Log API operation to audit handlers.

        Args:
            method: HTTP method
            path: API endpoint path
            params: Query parameters
            data: Request body
            status_code: HTTP status code
            response_time: Response time in seconds
            success: Whether operation succeeded
            error: Error message if operation failed
        """
        if not self._audit_handler and not self._audit_callback:
            return

        import datetime

        operation = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "method": method,
            "path": path,
            "params": params,
            "data": data,
            "status_code": status_code,
            "success": success,
            "duration_ms": int(response_time * 1000),
            "host": self._url,
            "read_only_mode": self._read_only,
            "user_context": self._user_context,
        }

        if error:
            operation["error"] = error

        # Call audit handler if provided
        if self._audit_handler and hasattr(self._audit_handler, "log_operation"):
            try:
                self._audit_handler.log_operation(operation)
            except Exception as e:
                logger.warning(f"Audit handler failed: {e}")

        # Call audit callback if provided
        if self._audit_callback:
            try:
                self._audit_callback(operation)
            except Exception as e:
                logger.warning(f"Audit callback failed: {e}")

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

        # Track active requests
        self._active_requests += 1
        self._total_requests += 1

        try:
            # Measure response time
            start_time = time.time()
            response = session.get(url, timeout=request_timeout)
            response_time = time.time() - start_time
            
            response.raise_for_status()

            # Store last request for debugging
            self._last_request = {
                "method": "GET",
                "url": url,
                "params": params,
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
        finally:
            self._active_requests -= 1

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

        # Track active requests
        self._active_requests += 1
        self._total_requests += 1

        try:
            # Read-only mode: simulate write operations
            if self._read_only:
                logger.info(f"READ-ONLY: Simulating POST {url}")
                response_time = 0.001  # Simulated

                # Store last request for debugging
                self._last_request = {
                    "method": "POST",
                    "url": url,
                    "params": params,
                    "data": data,
                }
                self._last_response = {
                    "status_code": 200,
                    "body": {"status": 0, "message": "Simulated (read-only mode)"},
                }
                self._last_response_time = response_time

                # Track operation if enabled
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

                # Call audit handlers
                self._log_audit_operation(
                    method="POST",
                    path=path,
                    params=params,
                    data=data,
                    status_code=200,
                    response_time=response_time,
                    success=True,
                )

                return {
                    "data": {"status": 0, "message": "Simulated (read-only mode)"},
                    "http_status_code": 200,
                    "response_time": response_time,
                    "request_info": {
                        "method": "POST",
                        "url": url,
                        "params": params,
                        "data": data,
                    },
                }

            # Measure response time
            start_time = time.time()
            response = session.post(url, json=data, timeout=request_timeout)
            response_time = time.time() - start_time
            
            response.raise_for_status()

            # Store last request for debugging
            self._last_request = {
                "method": "POST",
                "url": url,
                "params": params,
                "data": data,
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
                    "method": "POST",
                    "path": path,
                    "params": params,
                    "data": data,
                    "status_code": response.status_code,
                    "read_only_simulated": False,
                })

            # Call audit handlers
            self._log_audit_operation(
                method="POST",
                path=path,
                params=params,
                data=data,
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
                    "method": "POST",
                    "url": url,
                    "params": params,
                    "data": data,
                },
            }
        finally:
            self._active_requests -= 1

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
        session = self._get_session()

        url = path
        if params:
            clean_params = {k: v for k, v in params.items() if v is not None}
            if clean_params:
                url = f"{path}?{urlencode(clean_params)}"

        logger.debug(f"PUT {url} (read_only={self._read_only})")

        request_timeout = timeout if timeout is not None else self._read_timeout

        # Track active requests
        self._active_requests += 1
        self._total_requests += 1

        try:
            # Read-only mode: simulate write operations
            if self._read_only:
                logger.info(f"READ-ONLY: Simulating PUT {url}")
                response_time = 0.001

                self._last_request = {"method": "PUT", "url": url, "params": params, "data": data}
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

                self._log_audit_operation(
                    method="PUT",
                    path=path,
                    params=params,
                    data=data,
                    status_code=200,
                    response_time=response_time,
                    success=True,
                )

                return {
                    "data": {"status": 0, "message": "Simulated (read-only mode)"},
                    "http_status_code": 200,
                    "response_time": response_time,
                    "request_info": {"method": "PUT", "url": url, "params": params, "data": data},
                }

            # Measure response time
            start_time = time.time()
            response = session.put(url, json=data, timeout=request_timeout)
            response_time = time.time() - start_time
            
            response.raise_for_status()

            self._last_request = {"method": "PUT", "url": url, "params": params, "data": data}
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

            self._log_audit_operation(
                method="PUT",
                path=path,
                params=params,
                data=data,
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
                "method": "PUT",
                "url": url,
                "params": params,
                "data": data,
            },
        }
        finally:
            self._active_requests -= 1

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
        session = self._get_session()

        url = path
        if params:
            clean_params = {k: v for k, v in params.items() if v is not None}
            if clean_params:
                url = f"{path}?{urlencode(clean_params)}"

        logger.debug(f"DELETE {url} (read_only={self._read_only})")

        request_timeout = timeout if timeout is not None else self._read_timeout

        # Track active requests
        self._active_requests += 1
        self._total_requests += 1

        try:
            # Read-only mode: simulate write operations
            if self._read_only:
                logger.info(f"READ-ONLY: Simulating DELETE {url}")
                response_time = 0.001

                self._last_request = {"method": "DELETE", "url": url, "params": params}
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

                self._log_audit_operation(
                    method="DELETE",
                    path=path,
                    params=params,
                    data=None,
                    status_code=200,
                    response_time=response_time,
                    success=True,
                )

                return {
                    "data": {"status": 0, "message": "Simulated (read-only mode)"},
                    "http_status_code": 200,
                    "response_time": response_time,
                    "request_info": {"method": "DELETE", "url": url, "params": params},
                }

            # Measure response time
            start_time = time.time()
            response = session.delete(url, timeout=request_timeout)
            response_time = time.time() - start_time
            
            response.raise_for_status()

            self._last_request = {"method": "DELETE", "url": url, "params": params}
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

            self._log_audit_operation(
                method="DELETE",
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
                    "method": "DELETE",
                    "url": url,
                    "params": params,
                },
            }
        finally:
            self._active_requests -= 1

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
                - active_requests: Number of currently active requests
                - total_requests: Total number of requests made
                - max_connections: Maximum allowed connections
                - max_keepalive_connections: Maximum keepalive connections

        Example:
            >>> client = CloudHTTPClient(url="https://support.fortinet.com", oauth_token="...")
            >>> stats = client.get_connection_stats()
            >>> print(f"Active: {stats['active_requests']}/{stats['max_connections']}")
            Active: 2/100
        """
        return {
            "active_requests": self._active_requests,
            "total_requests": self._total_requests,
            "max_connections": self._max_connections,
            "max_keepalive_connections": self._max_keepalive_connections,
        }

    def inspect_last_request(self) -> Optional[dict[str, Any]]:
        """
        Get detailed information about the last HTTP request/response.

        Useful for debugging and understanding what was sent/received.

        Returns:
            Dictionary with last request details or None if no requests made:
                - request: Request details (method, url, params, data)
                - response: Response details (status_code, body)
                - response_time: Response time in seconds

        Example:
            >>> client = CloudHTTPClient(url="https://support.fortinet.com", oauth_token="...")
            >>> client.get("/api/v3/products/list")
            >>> last = client.inspect_last_request()
            >>> print(f"Last request took {last['response_time']}s")
            Last request took 0.234s
        """
        if self._last_request is None:
            return None

        return {
            "request": self._last_request,
            "response": self._last_response,
            "response_time": self._last_response_time,
        }

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
