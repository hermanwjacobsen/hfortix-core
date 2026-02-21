"""
Base HTTP Client - Shared Logic for Sync and Async Clients

This module contains BaseHTTPClient with shared validation, retry logic,
circuit breaker, statistics, and utilities used by both HTTPClient and
AsyncHTTPClient.
"""

from __future__ import annotations

import fnmatch
import logging
import time
from collections import deque
from typing import Any, Optional, TypeAlias, Union
from urllib.parse import quote

import httpx

from hfortix_core.ratelimit import RateLimitStats

logger = logging.getLogger("hfortix.http.base")

# Type alias for API responses
HTTPResponse: TypeAlias = dict[str, Any]

__all__ = ["BaseHTTPClient", "HTTPResponse"]


class BaseHTTPClient:
    """
    Base class for HTTP clients with shared logic.

    Provides:
    - Parameter validation
    - URL building
    - Retry statistics
    - Circuit breaker state management
    - Endpoint timeout configuration
    - Path normalization and encoding
    - Data sanitization
    """

    def __init__(
        self,
        url: str,
        verify: bool = True,
        vdom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        # Legacy circuit breaker params (deprecated, use circuit_breaker=True instead)
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
        # Rate limiting enforcement (NEW)
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        # Circuit breaker (NEW - replaces always-on behavior)
        circuit_breaker: bool = False,
        circuit_breaker_half_open_calls: int = 3,
    ) -> None:
        """Initialize base HTTP client with shared configuration

        Args:
            url: Base URL for the API (required)
            verify: Enable SSL certificate verification (default: True)
            vdom: Virtual domain name (optional)
            max_retries: Maximum retry attempts (default: 3)
            connect_timeout: Connection timeout in seconds (default: 10.0)
            read_timeout: Read timeout in seconds (default: 300.0)
            circuit_breaker_threshold: DEPRECATED - use circuit_breaker=True
            circuit_breaker_timeout: DEPRECATED - use circuit_breaker=True
            max_connections: Maximum concurrent connections (default: 100)
            max_keepalive_connections: Maximum keepalive connections (default: 20)
            adaptive_retry: Enable adaptive retry with backpressure detection
                          (default: False). Monitors response times and adjusts
                          retry delays based on FortiGate health signals.
            retry_strategy: Retry backoff strategy - 'exponential' (default)
                          or 'linear'. Exponential: 1s, 2s, 4s, 8s, 16s, 30s.
                          Linear: 1s, 2s, 3s, 4s, 5s.
            retry_jitter: Add random jitter (0-25% of delay) to retry delays
                         to prevent thundering herd problem when multiple
                         clients retry simultaneously (default: False).
            read_only: Enable read-only mode - simulate write operations
                      without executing (default: False)
            audit_handler: Handler for audit logging (implements AuditHandler
                          protocol). Essential for compliance.
            audit_callback: Custom callback function for audit logging.
                           Alternative to audit_handler.
            user_context: Optional dict with user/application context to
                         include in audit logs.
            rate_limit_calls_per_min: Track calls per minute (tracking only)
            rate_limit_calls_per_5min: Track calls per 5 minutes (tracking only)
            rate_limit_calls_per_hour: Track calls per hour (tracking only)
            rate_limit_errors_per_min: Track errors per minute (tracking only)
            rate_limit_errors_per_5min: Track errors per 5 minutes (tracking only)
            rate_limit_errors_per_hour: Track errors per hour (tracking only)
            
            # Rate Limiting Enforcement (NEW - default disabled)
            rate_limit: Enable rate limiting enforcement (default: False).
                       When enabled, enforces request rate limits with queue.
            rate_limit_strategy: How to handle rate limit exceeded:
                               "queue" - Queue requests (default)
                               "drop" - Drop requests silently
                               "raise" - Raise RateLimitExceededError
            rate_limit_max_requests: Max requests per window (default: 100)
            rate_limit_window_seconds: Time window in seconds (default: 60.0)
            rate_limit_queue_size: Max queued requests (default: 100)
            rate_limit_queue_timeout: Max wait time in queue (default: 30.0)
            rate_limit_queue_overflow: What to do when queue is full:
                                     "block" - Wait for space (default)
                                     "drop" - Drop request silently
                                     "raise" - Raise RateLimitQueueFullError
            
            # Circuit Breaker (NEW - default disabled, breaking change)
            circuit_breaker: Enable circuit breaker (default: False).
                           When disabled, no overhead. When enabled, trips
                           open after consecutive failures to protect service.
            circuit_breaker_half_open_calls: Test calls in half-open state
                                            (default: 3)
        """
        # Validate parameters
        if not url:
            raise ValueError("URL is required")
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        if max_retries > 100:
            raise ValueError("max_retries must be <= 100")
        if connect_timeout <= 0:
            raise ValueError("connect_timeout must be > 0")
        if read_timeout <= 0:
            raise ValueError("read_timeout must be > 0")
        if circuit_breaker_threshold <= 0:
            raise ValueError("circuit_breaker_threshold must be > 0")
        if circuit_breaker_timeout <= 0:
            raise ValueError("circuit_breaker_timeout must be > 0")
        if max_connections <= 0:
            raise ValueError("max_connections must be > 0")
        if max_keepalive_connections < 0:
            raise ValueError("max_keepalive_connections must be >= 0")
        if retry_strategy not in ("exponential", "linear"):
            raise ValueError(
                "retry_strategy must be 'exponential' or 'linear'"
            )
        
        # Validate new rate limiting parameters
        if rate_limit:
            if rate_limit_strategy not in ("queue", "drop", "raise"):
                raise ValueError(
                    "rate_limit_strategy must be 'queue', 'drop', or 'raise'"
                )
            if rate_limit_max_requests <= 0:
                raise ValueError("rate_limit_max_requests must be > 0")
            if rate_limit_window_seconds <= 0:
                raise ValueError("rate_limit_window_seconds must be > 0")
            if rate_limit_queue_size < 0:
                raise ValueError("rate_limit_queue_size must be >= 0")
            if rate_limit_queue_timeout <= 0:
                raise ValueError("rate_limit_queue_timeout must be > 0")
            if rate_limit_queue_overflow not in ("block", "drop", "raise"):
                raise ValueError(
                    "rate_limit_queue_overflow must be 'block', 'drop', or 'raise'"
                )
        
        # Validate circuit breaker parameters
        if circuit_breaker:
            if circuit_breaker_half_open_calls <= 0:
                raise ValueError("circuit_breaker_half_open_calls must be > 0")

        # Auto-adjust keepalive connections if needed (don't error)
        # httpx and other libraries allow these to be independent, but we'll
        # adjust
        # to be safe while not blocking legitimate configurations
        if max_keepalive_connections > max_connections:
            logger.warning(
                f"max_keepalive_connections ({max_keepalive_connections}) > "
                f"max_connections ({max_connections}). "
                f"Adjusting max_keepalive_connections to {max_connections}."
            )
            max_keepalive_connections = max_connections

        # Store configuration
        self._url = url.rstrip("/")
        self._verify = verify
        self._vdom = vdom
        self._max_retries = max_retries
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout

        # Initialize retry statistics
        self._retry_stats: dict[str, Any] = {
            "total_retries": 0,
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "retry_by_reason": {},
            "retry_by_endpoint": {},
            "last_retry_time": None,
        }

        # Circuit breaker - now configurable (default disabled)
        self._circuit_breaker_enabled = circuit_breaker
        # Initialize circuit breaker dict (always present for backward compatibility)
        self._circuit_breaker: dict[str, Any] = {}
        
        if circuit_breaker:
            # Initialize circuit breaker state (only when enabled)
            self._circuit_breaker = {
                "consecutive_failures": 0,
                "last_failure_time": None,
                "state": "closed",  # closed, open, half_open
                "failure_threshold": circuit_breaker_threshold,
                "timeout": circuit_breaker_timeout,
                "half_open_calls": circuit_breaker_half_open_calls,
                "half_open_successes": 0,
            }
            logger.info(
                f"Circuit breaker enabled: threshold={circuit_breaker_threshold}, "
                f"timeout={circuit_breaker_timeout}s, half_open_calls={circuit_breaker_half_open_calls}"
            )
        else:
            # Keep a minimal dict for backward compatibility with get_circuit_breaker_state()
            self._circuit_breaker = {
                "state": "disabled",
                "consecutive_failures": 0,
                "last_failure_time": None,
                "failure_threshold": circuit_breaker_threshold,
                "timeout": circuit_breaker_timeout,
            }

        # Rate limiting - now with enforcement (default disabled, zero overhead)
        self._rate_limit_enabled = rate_limit
        self._rate_limiter: Optional[Any] = None  # Will be initialized in subclasses (sync vs async)
        self._rate_limit_config: Optional[dict[str, Any]] = None
        
        if rate_limit:
            # Store config for subclass initialization
            self._rate_limit_config = {
                "max_requests": rate_limit_max_requests,
                "window_seconds": rate_limit_window_seconds,
                "strategy": rate_limit_strategy,
                "queue_size": rate_limit_queue_size,
                "queue_timeout": rate_limit_queue_timeout,
                "queue_overflow": rate_limit_queue_overflow,
            }
            logger.info(
                f"Rate limiting enabled: {rate_limit_max_requests} req/{rate_limit_window_seconds}s, "
                f"strategy={rate_limit_strategy}, queue_size={rate_limit_queue_size}"
            )

        # Initialize per-endpoint timeout configuration
        self._endpoint_timeouts: dict[str, httpx.Timeout] = {}

        # Adaptive retry configuration
        self._adaptive_retry = adaptive_retry
        self._retry_strategy = retry_strategy
        self._retry_jitter = retry_jitter
        # endpoint -> deque of response times
        self._response_times: dict[str, deque] = {}
        # 500ms baseline
        self._baseline_response_time = 0.5
        # Endpoint is slow if 3x baseline
        self._slowdown_multiplier = 3.0

        # Read-only mode and audit logging
        self._read_only = read_only
        self._audit_handler = audit_handler
        self._audit_callback = audit_callback
        self._user_context = user_context or {}

        # Rate limit tracking (informational only, no enforcement)
        self._rate_stats = RateLimitStats(
            calls_per_min=rate_limit_calls_per_min,
            calls_per_5min=rate_limit_calls_per_5min,
            calls_per_hour=rate_limit_calls_per_hour,
            errors_per_min=rate_limit_errors_per_min,
            errors_per_5min=rate_limit_errors_per_5min,
            errors_per_hour=rate_limit_errors_per_hour,
        )

    # ========================================================================
    # Shared Utility Methods
    # ========================================================================

    @staticmethod
    def _sanitize_data(data: Optional[dict[str, Any]]) -> dict[str, Any]:
        """
        Remove sensitive fields from data before logging (recursive)

        Recursively sanitizes nested dictionaries and lists to prevent
        logging sensitive information like passwords, tokens, keys, VDOMs, etc.

        Args:
            data: Data to sanitize (can be dict, list, or any value)

        Returns:
            Sanitized copy of data with sensitive values redacted

        Examples:
            >>> _sanitize_data({'password': 'secret123', 'name': 'test'})
            {'password': '***REDACTED***', 'name': 'test'}
            >>> _sanitize_data({'users': [{'name': 'admin', 'key': 'abc'}]})
            {'users': [{'name': 'admin', 'key': '***REDACTED***'}]}
        """
        if not data:
            return {}

        sensitive_keys = [
            "password",
            "passwd",
            "secret",
            "token",
            "key",
            "private-key",
            "passphrase",
            "psk",
            "api_key",
            "api-key",
            "apikey",
            "auth",
            "authorization",
            "vdom",  # Virtual domain names can reveal customer/tenant info
        ]

        def sanitize_recursive(obj: Any) -> Any:
            """Recursively sanitize nested structures"""
            if isinstance(obj, dict):
                result = {}
                for k, v in obj.items():
                    if any(s in k.lower() for s in sensitive_keys):
                        result[k] = "***REDACTED***"
                    else:
                        result[k] = sanitize_recursive(v)
                return result
            elif isinstance(obj, list):
                return [sanitize_recursive(item) for item in obj]
            else:
                return obj

        return sanitize_recursive(data)

    def _log_context(
        self,
        request_id: Optional[str] = None,
        **extra_fields: Any,
    ) -> dict[str, Any]:
        """
        Build consistent logging context for structured logging

        Provides standard fields for all log events, ensuring consistency
        across the codebase. Automatically includes vdom/adom for multi-tenant
        environments.

        Args:
            request_id: Optional request ID for correlation
            **extra_fields: Additional fields to include (endpoint, method,
                          status_code, duration_seconds, etc.)

        Returns:
            Dictionary with logging context ready for logger.info(extra=...)

        Examples:
            >>> ctx = self._log_context(request_id="abc123",
            ...                        endpoint="/api/v2/cmdb/firewall/policy",
            ...                        method="GET")
            >>> logger.info("Request started", extra=ctx)
        """
        context: dict[str, Any] = {}

        # Add request_id if provided
        if request_id:
            context["request_id"] = request_id

        # Add vdom for FortiOS multi-tenancy (if configured)
        if self._vdom:
            context["vdom"] = self._vdom

        # Add adom for FortiManager/FortiAnalyzer (future support)
        # This allows FortiManager/FortiAnalyzer clients to set _adom
        # Using getattr to avoid type checker errors for optional attribute
        adom = getattr(self, "_adom", None)
        if adom:
            context["adom"] = adom

        # Add all extra fields
        context.update(extra_fields)

        return context

    @staticmethod
    def _normalize_path(path: str) -> str:
        """Normalize API path by removing leading slashes"""
        if isinstance(path, str):
            return path.lstrip("/")
        return path

    def _build_url(self, api_type: str, path: str) -> str:
        """Build complete API URL from components"""
        path = self._normalize_path(path)
        encoded_path = quote(str(path), safe="/%")
        return f"{self._url}/api/v2/{api_type}/{encoded_path}"

    # ========================================================================
    # Statistics Methods
    # ========================================================================

    def get_retry_stats(self) -> dict[str, Any]:
        """Get retry statistics"""
        return self._retry_stats.copy()

    def get_circuit_breaker_state(self) -> dict[str, Any]:
        """Get current circuit breaker state"""
        return self._circuit_breaker.copy()

    def _record_retry(self, reason: str, endpoint: str) -> None:
        """Record retry attempt in statistics"""
        self._retry_stats["total_retries"] += 1
        self._retry_stats["last_retry_time"] = time.time()

        # Track by reason
        if reason not in self._retry_stats["retry_by_reason"]:
            self._retry_stats["retry_by_reason"][reason] = 0
        self._retry_stats["retry_by_reason"][reason] += 1

        # Track by endpoint
        if endpoint not in self._retry_stats["retry_by_endpoint"]:
            self._retry_stats["retry_by_endpoint"][endpoint] = 0
        self._retry_stats["retry_by_endpoint"][endpoint] += 1

    # ========================================================================
    # Endpoint Timeout Configuration
    # ========================================================================

    def configure_endpoint_timeout(
        self,
        endpoint_pattern: str,
        connect_timeout: Optional[float] = None,
        read_timeout: Optional[float] = None,
    ) -> None:
        """Configure custom timeout for specific endpoints"""
        timeout = httpx.Timeout(
            connect=connect_timeout or self._connect_timeout,
            read=read_timeout or self._read_timeout,
            write=30.0,
            pool=10.0,
        )
        self._endpoint_timeouts[endpoint_pattern] = timeout
        logger.info(
            "Configured custom timeout for endpoint pattern '%s': connect=%.1fs, read=%.1fs",  # noqa: E501
            endpoint_pattern,
            timeout.connect,
            timeout.read,
        )

    def _get_endpoint_timeout(self, endpoint: str) -> Optional[httpx.Timeout]:
        """Get custom timeout for specific endpoint if configured"""
        for pattern, timeout in self._endpoint_timeouts.items():
            if fnmatch.fnmatch(endpoint, pattern):
                return timeout
        return None

    # ========================================================================
    # Circuit Breaker Methods
    # ========================================================================

    def _check_circuit_breaker(self, endpoint: str) -> None:
        """Check circuit breaker state before making request"""
        # Skip if circuit breaker is disabled (zero overhead)
        if not self._circuit_breaker_enabled:
            return
            
        if self._circuit_breaker["state"] == "open":
            elapsed = time.time() - (
                self._circuit_breaker["last_failure_time"] or 0
            )
            if elapsed < self._circuit_breaker["timeout"]:
                remaining = self._circuit_breaker["timeout"] - elapsed
                logger.error(
                    "Circuit breaker is OPEN - service unavailable (retry in %.1fs)",  # noqa: E501
                    remaining,
                )
                from hfortix_core.exceptions import CircuitBreakerOpenError

                raise CircuitBreakerOpenError(
                    f"Circuit breaker is OPEN for {endpoint}. "
                    f"Service appears to be down. Retry in {remaining:.1f}s"
                )
            else:
                self._circuit_breaker["state"] = "half_open"
                self._circuit_breaker["half_open_successes"] = 0
                logger.info("Circuit breaker transitioning to HALF_OPEN state")

    def _record_circuit_breaker_success(self) -> None:
        """Record successful request in circuit breaker"""
        # Skip if circuit breaker is disabled (zero overhead)
        if not self._circuit_breaker_enabled:
            return
            
        if self._circuit_breaker["state"] == "half_open":
            # Count successful calls in half-open state
            self._circuit_breaker["half_open_successes"] += 1
            required = self._circuit_breaker.get("half_open_calls", 3)
            
            if self._circuit_breaker["half_open_successes"] >= required:
                # Enough successful test calls - close the circuit
                self._circuit_breaker["state"] = "closed"
                self._circuit_breaker["consecutive_failures"] = 0
                self._circuit_breaker["half_open_successes"] = 0
                logger.info(
                    f"Circuit breaker CLOSED after {required} successful test calls"
                )
        elif self._circuit_breaker["state"] == "closed":
            self._circuit_breaker["consecutive_failures"] = 0

    def _record_circuit_breaker_failure(self, endpoint: str) -> None:
        """Record failed request in circuit breaker"""
        # Skip if circuit breaker is disabled (zero overhead)
        if not self._circuit_breaker_enabled:
            return
            
        self._circuit_breaker["consecutive_failures"] += 1
        self._circuit_breaker["last_failure_time"] = time.time()

        failures = self._circuit_breaker["consecutive_failures"]
        threshold = self._circuit_breaker["failure_threshold"]

        # If in half-open and failure occurs, immediately reopen
        if self._circuit_breaker["state"] == "half_open":
            self._circuit_breaker["state"] = "open"
            self._circuit_breaker["half_open_successes"] = 0
            logger.error(
                "Circuit breaker REOPENED after failure in half-open state for endpoint %s",
                endpoint,
            )
        elif failures >= threshold and self._circuit_breaker["state"] != "open":
            self._circuit_breaker["state"] = "open"
            self._circuit_breaker["half_open_successes"] = 0
            logger.error(
                (
                    "Circuit breaker OPENED after %d consecutive "
                    "failures for endpoint %s"
                ),
                failures,
                endpoint,
            )

    def reset_circuit_breaker(self) -> None:
        """Reset circuit breaker to closed state"""
        self._circuit_breaker["state"] = "closed"
        self._circuit_breaker["consecutive_failures"] = 0
        self._circuit_breaker["last_failure_time"] = None
        logger.info("Circuit breaker manually reset to CLOSED state")

    # ========================================================================
    # Retry Logic
    # ========================================================================

    def _should_retry(
        self, error: Exception, attempt: int, endpoint: str = ""
    ) -> bool:
        """Determine if a request should be retried"""
        if attempt >= self._max_retries:
            return False

        # Don't retry SSL/certificate errors - these are permanent failures
        # that won't resolve with retries
        if isinstance(error, (httpx.ConnectError, httpx.NetworkError)):
            error_msg = str(error).lower()
            ssl_indicators = [
                "certificate_verify_failed",
                "ssl:",
                "certificate",
                "cert verification",
                "handshake",
                "certificate is not valid",
            ]
            if any(indicator in error_msg for indicator in ssl_indicators):
                logger.error(
                    "SSL/Certificate error (not retrying) for %s: %s",
                    endpoint,
                    error,
                )
                return False

        # Retry on connection errors and timeouts
        if isinstance(error, (httpx.ConnectError, httpx.NetworkError)):
            self._record_retry("connection_error", endpoint)
            logger.warning(
                "Connection error on attempt %d/%d for %s: %s",
                attempt + 1,
                self._max_retries,
                endpoint,
                error,
            )
            return True

        if isinstance(
            error, (httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout)
        ):
            self._record_retry("timeout", endpoint)
            logger.warning(
                "Timeout on attempt %d/%d for %s: %s",
                attempt + 1,
                self._max_retries,
                endpoint,
                error,
            )
            return True

        # Retry on HTTP status errors (429, 500-504)
        if isinstance(error, httpx.HTTPStatusError):
            status = error.response.status_code
            if status == 429:  # Rate limit
                self._record_retry("rate_limit", endpoint)
                logger.warning(
                    "Rate limit hit on attempt %d/%d for %s",
                    attempt + 1,
                    self._max_retries,
                    endpoint,
                )
                return True
            elif 500 <= status <= 504:  # Server errors
                self._record_retry("server_error", endpoint)
                logger.warning(
                    "Server error %d on attempt %d/%d for %s",
                    status,
                    attempt + 1,
                    self._max_retries,
                    endpoint,
                )
                return True

        return False

    def _get_retry_delay(
        self,
        attempt: int,
        response: Optional[httpx.Response] = None,
        endpoint: Optional[str] = None,
    ) -> float:
        """
        Calculate retry delay with optional adaptive backpressure

        Args:
            attempt: Current retry attempt number (0-indexed)
            response: HTTP response object (if available)
            endpoint: Endpoint being retried (for adaptive logic)

        Returns:
            Delay in seconds before next retry
        """
        # Check for Retry-After header (FortiGate explicitly telling us when to
        # retry)
        if response and "Retry-After" in response.headers:
            try:
                return float(response.headers["Retry-After"])
            except ValueError:
                pass

        # Calculate base delay based on retry strategy
        if self._retry_strategy == "exponential":
            # Exponential backoff: 1s, 2s, 4s, 8s, 16s, max 30s
            delay = min(2**attempt, 30.0)
        else:  # linear
            # Linear backoff: 1s, 2s, 3s, 4s, 5s, max 30s
            delay = min((attempt + 1) * 1.0, 30.0)

        # Apply adaptive backpressure if enabled
        if self._adaptive_retry and endpoint:
            delay = self._apply_adaptive_backpressure(
                delay, response, endpoint
            )

        # Add jitter if enabled (0-25% random variation)
        if self._retry_jitter:
            import random

            jitter_amount = delay * random.uniform(0, 0.25)  # nosec B311
            delay = delay + jitter_amount
            logger.debug(
                "Applied jitter to retry delay: %.2fs + %.2fs jitter = %.2fs",
                delay - jitter_amount,
                jitter_amount,
                delay,
            )

        return delay

    def _apply_adaptive_backpressure(
        self,
        base_delay: float,
        response: Optional[httpx.Response],
        endpoint: str,
    ) -> float:
        """
        Apply adaptive backpressure based on FortiGate health signals

        Args:
            base_delay: Base exponential backoff delay
            response: HTTP response (if available)
            endpoint: Endpoint being retried

        Returns:
            Adjusted delay with backpressure multiplier applied
        """
        multiplier = 1.0

        # Signal 1: Explicit 503 Service Unavailable (FortiGate overloaded)
        if response and response.status_code == 503:
            multiplier = 3.0
            logger.warning(
                (
                    "FortiGate returned 503 (overloaded), applying 3x "
                    "backpressure multiplier"
                )
            )

        # Signal 2: Endpoint showing slow response times (early warning)
        elif self._is_endpoint_slow(endpoint):
            multiplier = 2.0
            avg_time = self._get_avg_response_time(endpoint)
            logger.warning(
                (
                    "Endpoint %s showing backpressure (avg response: "
                    "%.2fs, baseline: %.2fs), applying 2x multiplier"
                ),
                endpoint,
                avg_time,
                self._baseline_response_time,
            )

        adjusted_delay = base_delay * multiplier

        # Cap maximum delay at 2 minutes
        return min(adjusted_delay, 120.0)

    def _record_response_time(self, endpoint: str, duration: float) -> None:
        """
        Record response time for adaptive backpressure detection

        Args:
            endpoint: API endpoint (e.g., 'cmdb/firewall/address')
            duration: Response time in seconds
        """
        if not self._adaptive_retry:
            return  # Zero overhead when disabled

        if endpoint not in self._response_times:
            # Keep last 100 response times per endpoint
            self._response_times[endpoint] = deque(maxlen=100)

        self._response_times[endpoint].append(duration)

    def _get_avg_response_time(self, endpoint: str) -> float:
        """
        Get average response time for endpoint

        Args:
            endpoint: API endpoint

        Returns:
            Average response time in seconds, or 0.0 if no data
        """
        times = self._response_times.get(endpoint, deque())
        if not times:
            return 0.0
        return sum(times) / len(times)

    def _is_endpoint_slow(self, endpoint: str) -> bool:
        """
        Detect if endpoint is responding slowly (backpressure signal)

        Args:
            endpoint: API endpoint to check

        Returns:
            True if endpoint average response time exceeds baseline threshold
        """
        avg_time = self._get_avg_response_time(endpoint)

        # No data yet, assume healthy
        if avg_time == 0.0:
            return False

        # Slow if average > baseline * multiplier
        threshold = self._baseline_response_time * self._slowdown_multiplier
        return avg_time > threshold

    def get_health_metrics(self) -> dict[str, Any]:
        """
        Get comprehensive health metrics including adaptive retry stats

        Returns:
            Dictionary with health score, response times, circuit state, etc.
        """
        metrics: dict[str, Any] = {
            "circuit_breaker": {
                "state": self._circuit_breaker["state"],
                "consecutive_failures": self._circuit_breaker[
                    "consecutive_failures"
                ],
                "threshold": self._circuit_breaker["failure_threshold"],
            },
            "retry_stats": self._retry_stats.copy(),
            "adaptive_retry_enabled": self._adaptive_retry,
        }

        # Add response time metrics if adaptive retry is enabled
        if self._adaptive_retry and self._response_times:
            metrics["response_times"] = {}
            for endpoint, times in self._response_times.items():
                if times:
                    sorted_times = sorted(times)
                    count = len(sorted_times)
                    metrics["response_times"][endpoint] = {
                        "count": count,
                        "avg_ms": round(sum(sorted_times) / count * 1000, 2),
                        "min_ms": round(min(sorted_times) * 1000, 2),
                        "max_ms": round(max(sorted_times) * 1000, 2),
                        "p50_ms": round(sorted_times[count // 2] * 1000, 2),
                        "p95_ms": (
                            round(sorted_times[int(count * 0.95)] * 1000, 2)
                            if count > 20
                            else None
                        ),
                        "is_slow": self._is_endpoint_slow(endpoint),
                    }

        return metrics

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get HTTP connection pool statistics (base implementation)
        
        Base class provides minimal stats. Child classes override this
        to provide detailed connection pool metrics.
        
        Returns:
            Dictionary with basic connection statistics:
                - circuit_breaker_state: Current circuit breaker state
                - consecutive_failures: Number of consecutive failures
                - last_failure_time: Timestamp of last failure
                
        Note:
            Child classes (HTTPClient, AsyncHTTPClient, etc.) override this
            to include additional metrics like active_requests, pool_exhaustion, etc.
            
        Example:
            >>> stats = client.get_connection_stats()
            >>> if stats['circuit_breaker_state'] == 'open':
            ...     print("Circuit breaker is open!")
        """
        return {
            "circuit_breaker_state": self._circuit_breaker["state"],
            "consecutive_failures": self._circuit_breaker[
                "consecutive_failures"
            ],
            "last_failure_time": self._circuit_breaker["last_failure_time"],
        }

    def get_rate_limit_status(self) -> dict[str, Any]:
        """
        Get current rate limit tracking status
        
        Returns detailed rate limit statistics including:
        - Call counts in different time windows (last min, 5min, hour)
        - Error counts in different time windows
        - Total calls and errors since client creation
        - Configured limits
        - Whether current usage is within limits
        
        Returns:
            Dictionary with rate limit statistics:
                - calls_last_min: API calls in last 60 seconds
                - calls_last_5min: API calls in last 300 seconds
                - calls_last_hour: API calls in last 3600 seconds
                - errors_last_min: Errors in last 60 seconds
                - errors_last_5min: Errors in last 300 seconds
                - errors_last_hour: Errors in last 3600 seconds
                - total_calls: Total API calls since creation
                - total_errors: Total errors since creation
                - limits: Dict of configured limits
                - within_limits: Boolean, True if all limits respected
                
        Note:
            This is for monitoring only - does NOT enforce rate limits.
            Configure limits via rate_limit_* parameters in __init__().
            
        Example:
            >>> client = HTTPClient(
            ...     url="...",
            ...     token="...",
            ...     rate_limit_calls_per_min=100,
            ...     rate_limit_calls_per_hour=1000
            ... )
            >>> status = client.get_rate_limit_status()
            >>> print(f"Calls/min: {status['calls_last_min']}/100")
            >>> print(f"Within limits: {status['within_limits']}")
        """
        return self._rate_stats.get_status()

    # ========================================================================
    # Validation Helper Methods
    # ========================================================================

    @staticmethod
    def _validate_api_type(api_type: str) -> None:
        """Validate API type parameter"""
        valid_types = {"cmdb", "monitor", "log", "service"}
        if api_type not in valid_types:
            raise ValueError(
                f"Invalid api_type '{api_type}'. Must be one of: "
                f"{', '.join(sorted(valid_types))}"
            )

    @staticmethod
    def _validate_path(path: str) -> None:
        """Validate path parameter"""
        if not path or not isinstance(path, str):
            raise ValueError("path must be a non-empty string")

    @staticmethod
    def _validate_data(data: Any) -> None:
        """Validate data parameter for POST/PUT"""
        if not isinstance(data, dict):
            raise TypeError(
                f"data must be a dictionary, got {type(data).__name__}"
            )

    # ========================================================================
    # Audit Logging Methods
    # ========================================================================

    def _log_audit(
        self,
        method: str,
        endpoint: str,
        api_type: str,
        path: str,
        data: Optional[dict[str, Any]],
        params: Optional[dict[str, Any]],
        status_code: int,
        success: bool,
        duration_ms: int,
        request_id: str,
        error: Optional[str] = None,
    ) -> None:
        """
        Log API operation to audit handlers

        Args:
            method: HTTP method
            endpoint: Full API endpoint
            api_type: API type (cmdb, monitor, etc.)
            path: Relative path
            data: Request data (will be sanitized)
            params: Request params (will be sanitized)
            status_code: HTTP status code
            success: Whether operation succeeded
            duration_ms: Duration in milliseconds
            request_id: Request ID
            error: Error message if failed
        """
        # Skip if no audit handler or callback configured
        if not self._audit_handler and not self._audit_callback:
            return

        try:
            from datetime import datetime, timezone

            # Determine action from method and path
            action = self._infer_action(method, path)

            # Extract object type and name from path
            object_type, object_name = self._extract_object_info(path, data)

            # Build operation dict
            operation: dict[str, Any] = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "request_id": request_id,
                "method": method.upper(),
                "endpoint": endpoint,
                "api_type": api_type,
                "path": path,
                "vdom": params.get("vdom") if params else self._vdom,
                "action": action,
                "object_type": object_type,
                "object_name": object_name,
                "data": self._sanitize_data(data) if data else None,
                "params": self._sanitize_data(params) if params else None,
                "status_code": status_code,
                "success": success,
                "duration_ms": duration_ms,
                "host": self._url.replace("https://", "").replace(
                    "http://", ""
                ),
                "read_only_mode": self._read_only
                and method in ("POST", "PUT", "DELETE"),
            }

            # Add error if present
            if error:
                operation["error"] = error

            # Add user context if provided
            if self._user_context:
                operation["user_context"] = self._user_context

            # Call audit handler if configured
            if self._audit_handler:
                try:
                    self._audit_handler.log_operation(operation)
                except Exception as e:
                    logger.error(
                        f"Audit handler failed: {e}",
                        extra={
                            "error": str(e),
                            "request_id": request_id,
                        },
                        exc_info=True,
                    )

            # Call audit callback if configured
            if self._audit_callback:
                try:
                    self._audit_callback(operation)
                except Exception as e:
                    logger.error(
                        f"Audit callback failed: {e}",
                        extra={
                            "error": str(e),
                            "request_id": request_id,
                        },
                        exc_info=True,
                    )

        except Exception as e:
            # Don't let audit logging break the main request flow
            logger.error(
                f"Audit logging failed: {e}",
                extra={"error": str(e), "request_id": request_id},
                exc_info=True,
            )

    @staticmethod
    def _infer_action(method: str, path: str) -> str:
        """Infer high-level action from method and path"""
        method = method.upper()

        if method == "GET":
            # Heuristic: if path ends with a specific name, it's a read,
            # otherwise it's a list
            parts = path.strip("/").split("/")
            if len(parts) > 0 and parts[-1] and not parts[-1].startswith("?"):
                # Has a trailing identifier
                return "read"
            return "list"
        elif method == "POST":
            return "create"
        elif method == "PUT":
            return "update"
        elif method == "DELETE":
            return "delete"
        else:
            return "unknown"

    @staticmethod
    def _extract_object_info(
        path: str, data: Optional[dict[str, Any]]
    ) -> tuple[str, Optional[str]]:
        """
        Extract object type and name from path and data

        Returns:
            Tuple of (object_type, object_name)
        """
        # Clean path
        path = path.strip("/")

        # Object type is the full path with dots instead of slashes
        # e.g., "firewall/address" -> "firewall.address"
        object_type = path.replace("/", ".")

        # Try to extract object name from:
        # 1. Last path component (if it looks like a name)
        # 2. 'name' field in data
        # 3. 'mkey' field in data
        object_name = None

        parts = path.split("/")
        if len(parts) > 0:
            last_part = parts[-1]
            # If last part doesn't look like an endpoint, use it as name
            if last_part and not last_part.startswith("?"):
                object_name = last_part

        # Override with data if available
        if data:
            if "name" in data:
                object_name = str(data["name"])
            elif "mkey" in data:
                object_name = str(data["mkey"])

        return object_type, object_name

    @staticmethod
    def _validate_vdom(vdom: Optional[Union[str, bool]]) -> None:
        """Validate vdom parameter"""
        if vdom is not None and not isinstance(vdom, (str, bool)):
            raise TypeError(
                f"vdom must be str, bool, or None, got {type(vdom).__name__}"
            )

    @staticmethod
    def _validate_params(params: Optional[dict[str, Any]]) -> None:
        """Validate params parameter"""
        if params is not None and not isinstance(params, dict):
            raise TypeError(
                f"params must be a dictionary or None, got "
                f"{type(params).__name__}"
            )
