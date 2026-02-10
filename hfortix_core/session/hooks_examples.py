"""
Example Lifecycle Hooks for CloudSession

This module provides reference implementations of the TokenLifecycleHooks protocol
for common use cases: metrics collection, logging, alerting, and custom caching.

These are examples - adapt them to your production requirements!
"""

from __future__ import annotations

import logging
from typing import Optional, Any

from hfortix_core.session import TokenLifecycleHooks, TokenEvent

__all__ = [
    "PrometheusHooks",
    "LoggingHooks",
    "AlertingHooks",
    "MetricsCollectorHooks",
]


class PrometheusHooks:
    """
    Prometheus metrics collection for CloudSession token lifecycle.
    
    Tracks token operations with Prometheus counters and histograms.
    
    Requirements:
        pip install prometheus-client
    
    Metrics Exposed:
        - forticloud_token_acquired_total: Counter of successful token acquisitions
        - forticloud_token_refreshed_total: Counter of successful token refreshes
        - forticloud_token_expired_total: Counter of token expirations
        - forticloud_token_failed_total: Counter of token failures (labeled by error type)
        - forticloud_token_lifetime_seconds: Histogram of token lifetimes
        - forticloud_token_auto_refresh_total: Counter of auto-refresh operations
    
    Example:
        >>> from prometheus_client import start_http_server
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import PrometheusHooks
        >>> 
        >>> # Start Prometheus metrics server
        >>> start_http_server(8000)
        >>> 
        >>> # Create hooks
        >>> hooks = PrometheusHooks(namespace="prod", service="my_app")
        >>> 
        >>> # Use with CloudSession
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     lifecycle_hooks=hooks
        ... )
        >>> 
        >>> # Metrics available at http://localhost:8000/metrics
    """
    
    def __init__(self, namespace: str = "", service: str = ""):
        """
        Initialize Prometheus hooks.
        
        Args:
            namespace: Prometheus namespace (e.g., "prod", "staging")
            service: Service name label (e.g., "my_app", "api_gateway")
        """
        from prometheus_client import Counter, Histogram
        
        self.namespace = namespace
        self.service = service
        
        # Define metrics
        self.acquired_counter = Counter(
            'forticloud_token_acquired_total',
            'Total number of tokens acquired',
            ['client_id', 'namespace', 'service', 'auto_refresh']
        )
        
        self.refreshed_counter = Counter(
            'forticloud_token_refreshed_total',
            'Total number of tokens refreshed',
            ['client_id', 'namespace', 'service', 'auto_refresh']
        )
        
        self.expired_counter = Counter(
            'forticloud_token_expired_total',
            'Total number of token expirations',
            ['client_id', 'namespace', 'service']
        )
        
        self.failed_counter = Counter(
            'forticloud_token_failed_total',
            'Total number of token failures',
            ['client_id', 'namespace', 'service', 'error_type', 'operation']
        )
        
        self.lifetime_histogram = Histogram(
            'forticloud_token_lifetime_seconds',
            'Token lifetime in seconds',
            ['client_id', 'namespace', 'service'],
            buckets=[300, 600, 1800, 3600, 7200, 14400, 28800, 43200, 86400]  # 5m to 24h
        )
    
    def on_token_acquired(self, event: TokenEvent) -> None:
        """Record token acquisition."""
        self.acquired_counter.labels(
            client_id=event.client_id,
            namespace=self.namespace,
            service=self.service,
            auto_refresh=str(event.is_auto_refresh)
        ).inc()
        
        # Record expected lifetime
        if event.expires_in:
            self.lifetime_histogram.labels(
                client_id=event.client_id,
                namespace=self.namespace,
                service=self.service
            ).observe(event.expires_in)
    
    def on_token_refreshed(self, event: TokenEvent) -> None:
        """Record token refresh."""
        self.refreshed_counter.labels(
            client_id=event.client_id,
            namespace=self.namespace,
            service=self.service,
            auto_refresh=str(event.is_auto_refresh)
        ).inc()
        
        # Record new lifetime
        if event.expires_in:
            self.lifetime_histogram.labels(
                client_id=event.client_id,
                namespace=self.namespace,
                service=self.service
            ).observe(event.expires_in)
    
    def on_token_expired(self, event: TokenEvent) -> None:
        """Record token expiration."""
        self.expired_counter.labels(
            client_id=event.client_id,
            namespace=self.namespace,
            service=self.service
        ).inc()
    
    def on_token_failed(self, event: TokenEvent) -> None:
        """Record token failure."""
        error_type = type(event.error).__name__ if event.error else "Unknown"
        operation = event.event_type  # "acquired" or "refreshed"
        
        self.failed_counter.labels(
            client_id=event.client_id,
            namespace=self.namespace,
            service=self.service,
            error_type=error_type,
            operation=operation
        ).inc()


class LoggingHooks:
    """
    Structured logging for CloudSession token lifecycle.
    
    Logs all token events with structured fields for easy parsing.
    Great for centralized logging systems (ELK, Splunk, CloudWatch, etc.).
    
    Example:
        >>> import logging
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import LoggingHooks
        >>> 
        >>> # Configure logging
        >>> logging.basicConfig(
        ...     level=logging.INFO,
        ...     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ... )
        >>> 
        >>> # Create hooks
        >>> hooks = LoggingHooks(
        ...     logger_name="myapp.forticloud",
        ...     log_level=logging.INFO
        ... )
        >>> 
        >>> # Use with CloudSession
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     lifecycle_hooks=hooks
        ... )
    """
    
    def __init__(
        self,
        logger_name: str = "hfortix.session.lifecycle",
        log_level: int = logging.INFO,
        include_token: bool = False  # SECURITY: Don't log tokens by default
    ):
        """
        Initialize logging hooks.
        
        Args:
            logger_name: Name of logger to use
            log_level: Minimum log level (default: INFO)
            include_token: Include access token in logs (INSECURE - only for debugging)
        """
        self.logger = logging.getLogger(logger_name)
        self.log_level = log_level
        self.include_token = include_token
    
    def on_token_acquired(self, event: TokenEvent) -> None:
        """Log token acquisition."""
        extra = {
            "event_type": "token_acquired",
            "client_id": event.client_id,
            "expires_in": event.expires_in,
            "auto_refresh": event.is_auto_refresh,
            "timestamp": event.timestamp,
        }
        
        if self.include_token:
            extra["access_token"] = event.access_token[:10] + "..." if event.access_token else None
        
        self.logger.log(
            self.log_level,
            f"Token acquired for {event.client_id} (expires in {event.expires_in}s, auto_refresh={event.is_auto_refresh})",
            extra=extra
        )
    
    def on_token_refreshed(self, event: TokenEvent) -> None:
        """Log token refresh."""
        extra = {
            "event_type": "token_refreshed",
            "client_id": event.client_id,
            "expires_in": event.expires_in,
            "auto_refresh": event.is_auto_refresh,
            "timestamp": event.timestamp,
        }
        
        if self.include_token:
            extra["access_token"] = event.access_token[:10] + "..." if event.access_token else None
        
        self.logger.log(
            self.log_level,
            f"Token refreshed for {event.client_id} (expires in {event.expires_in}s, auto_refresh={event.is_auto_refresh})",
            extra=extra
        )
    
    def on_token_expired(self, event: TokenEvent) -> None:
        """Log token expiration."""
        extra = {
            "event_type": "token_expired",
            "client_id": event.client_id,
            "timestamp": event.timestamp,
        }
        
        self.logger.log(
            self.log_level,
            f"Token expired for {event.client_id}",
            extra=extra
        )
    
    def on_token_failed(self, event: TokenEvent) -> None:
        """Log token failure."""
        extra = {
            "event_type": "token_failed",
            "client_id": event.client_id,
            "error_type": type(event.error).__name__ if event.error else "Unknown",
            "error_message": str(event.error) if event.error else "",
            "timestamp": event.timestamp,
        }
        
        self.logger.error(
            f"Token operation failed for {event.client_id}: {event.error}",
            extra=extra,
            exc_info=event.error
        )


class AlertingHooks:
    """
    Alerting for critical CloudSession token events.
    
    Sends alerts when tokens fail repeatedly or other critical issues occur.
    Integrates with PagerDuty, Slack, email, or custom alerting systems.
    
    Example:
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import AlertingHooks
        >>> 
        >>> def send_pagerduty_alert(message: str, severity: str):
        ...     # Your PagerDuty integration
        ...     pass
        >>> 
        >>> def send_slack_alert(message: str):
        ...     # Your Slack integration
        ...     pass
        >>> 
        >>> # Create hooks
        >>> hooks = AlertingHooks(
        ...     on_failure=send_pagerduty_alert,
        ...     on_repeated_failure=send_slack_alert,
        ...     failure_threshold=3
        ... )
        >>> 
        >>> # Use with CloudSession
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     lifecycle_hooks=hooks
        ... )
    """
    
    def __init__(
        self,
        on_failure: Optional[callable] = None,
        on_repeated_failure: Optional[callable] = None,
        failure_threshold: int = 3,
        alert_on_expiration: bool = False
    ):
        """
        Initialize alerting hooks.
        
        Args:
            on_failure: Callback for any failure (message, severity)
            on_repeated_failure: Callback for repeated failures (message)
            failure_threshold: Number of failures before triggering repeated failure alert
            alert_on_expiration: Whether to alert on token expiration
        """
        self.on_failure_callback = on_failure
        self.on_repeated_failure_callback = on_repeated_failure
        self.failure_threshold = failure_threshold
        self.alert_on_expiration = alert_on_expiration
        
        # Track failure counts per client_id
        self._failure_counts: dict[str, int] = {}
    
    def on_token_acquired(self, event: TokenEvent) -> None:
        """Reset failure count on successful acquisition."""
        self._failure_counts[event.client_id] = 0
    
    def on_token_refreshed(self, event: TokenEvent) -> None:
        """Reset failure count on successful refresh."""
        self._failure_counts[event.client_id] = 0
    
    def on_token_expired(self, event: TokenEvent) -> None:
        """Alert on token expiration if enabled."""
        if self.alert_on_expiration and self.on_failure_callback:
            message = f"Token expired for client {event.client_id}"
            self.on_failure_callback(message, "warning")
    
    def on_token_failed(self, event: TokenEvent) -> None:
        """Alert on token failure."""
        client_id = event.client_id
        self._failure_counts[client_id] = self._failure_counts.get(client_id, 0) + 1
        
        error_msg = str(event.error) if event.error else "Unknown error"
        
        # Send immediate alert
        if self.on_failure_callback:
            message = f"Token operation failed for {client_id}: {error_msg}"
            self.on_failure_callback(message, "error")
        
        # Send repeated failure alert if threshold reached
        if (self._failure_counts[client_id] >= self.failure_threshold
            and self.on_repeated_failure_callback):
            message = (
                f"Token failures for {client_id} exceeded threshold "
                f"({self._failure_counts[client_id]} failures)"
            )
            self.on_repeated_failure_callback(message)


class MetricsCollectorHooks:
    """
    Simple in-memory metrics collector for CloudSession.
    
    Tracks basic statistics about token operations.
    Useful for debugging, testing, or simple monitoring without external dependencies.
    
    Example:
        >>> from hfortix_core.session import CloudSession
        >>> from hfortix_core.session.examples import MetricsCollectorHooks
        >>> 
        >>> # Create hooks
        >>> hooks = MetricsCollectorHooks()
        >>> 
        >>> # Use with CloudSession
        >>> session = CloudSession(
        ...     api_id="...",
        ...     password="...",
        ...     lifecycle_hooks=hooks
        ... )
        >>> 
        >>> # ... use session ...
        >>> 
        >>> # Print metrics
        >>> print(hooks.get_metrics())
        >>> # {
        >>> #   "total_acquired": 5,
        >>> #   "total_refreshed": 10,
        >>> #   "total_expired": 2,
        >>> #   "total_failed": 1,
        >>> #   "auto_refresh_count": 8,
        >>> #   "manual_refresh_count": 2,
        >>> #   "failure_rate": 0.0625
        >>> # }
    """
    
    def __init__(self):
        """Initialize metrics collector."""
        self.total_acquired = 0
        self.total_refreshed = 0
        self.total_expired = 0
        self.total_failed = 0
        self.auto_refresh_count = 0
        self.manual_refresh_count = 0
        self.failures_by_type: dict[str, int] = {}
    
    def on_token_acquired(self, event: TokenEvent) -> None:
        """Count token acquisition."""
        self.total_acquired += 1
        if event.is_auto_refresh:
            self.auto_refresh_count += 1
    
    def on_token_refreshed(self, event: TokenEvent) -> None:
        """Count token refresh."""
        self.total_refreshed += 1
        if event.is_auto_refresh:
            self.auto_refresh_count += 1
        else:
            self.manual_refresh_count += 1
    
    def on_token_expired(self, event: TokenEvent) -> None:
        """Count token expiration."""
        self.total_expired += 1
    
    def on_token_failed(self, event: TokenEvent) -> None:
        """Count token failure."""
        self.total_failed += 1
        
        error_type = type(event.error).__name__ if event.error else "Unknown"
        self.failures_by_type[error_type] = self.failures_by_type.get(error_type, 0) + 1
    
    def get_metrics(self) -> dict[str, Any]:
        """
        Get current metrics snapshot.
        
        Returns:
            Dictionary of metrics with counts and calculated rates
        """
        total_operations = self.total_acquired + self.total_refreshed
        failure_rate = (
            self.total_failed / total_operations if total_operations > 0 else 0.0
        )
        
        return {
            "total_acquired": self.total_acquired,
            "total_refreshed": self.total_refreshed,
            "total_expired": self.total_expired,
            "total_failed": self.total_failed,
            "auto_refresh_count": self.auto_refresh_count,
            "manual_refresh_count": self.manual_refresh_count,
            "failure_rate": failure_rate,
            "failures_by_type": dict(self.failures_by_type),
        }
    
    def reset(self) -> None:
        """Reset all metrics to zero."""
        self.total_acquired = 0
        self.total_refreshed = 0
        self.total_expired = 0
        self.total_failed = 0
        self.auto_refresh_count = 0
        self.manual_refresh_count = 0
        self.failures_by_type.clear()
