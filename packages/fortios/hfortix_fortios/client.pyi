"""Type stubs for hfortix_fortios.client module."""

from __future__ import annotations

from typing import Any, Literal, Optional, Union, overload

from hfortix_core.http.interface import IHTTPClient
from hfortix_fortios.api import API
from hfortix_fortios.firewall import (
    FirewallPolicy,
    IPMACBindingSetting,
    IPMACBindingTable,
    ScheduleGroup,
    ScheduleOnetime,
    ScheduleRecurring,
    ServiceCategory,
    ServiceCustom,
    ServiceGroup,
    ShaperPerIp,
    TrafficShaper,
)

class FirewallNamespace:
    """Namespace for firewall convenience wrappers."""
    
    policy: FirewallPolicy
    ipmac_binding_setting: IPMACBindingSetting
    ipmac_binding_table: IPMACBindingTable
    schedule_recurring: ScheduleRecurring
    schedule_onetime: ScheduleOnetime
    schedule_group: ScheduleGroup
    service_category: ServiceCategory
    service_custom: ServiceCustom
    service_group: ServiceGroup
    shaper_per_ip: ShaperPerIp
    traffic_shaper: TrafficShaper
    
    def __init__(self, fortios_instance: FortiOS) -> None: ...

class FortiOS:
    """FortiOS REST API Client.
    
    Python client for interacting with Fortinet FortiGate firewalls via REST API.
    Supports configuration management (CMDB), monitoring, logging, and services.
    """
    
    # Overloads for different initialization patterns
    @overload
    def __init__(
        self,
        *,
        host: str,
        token: str,
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None,
        debug: Union[str, bool, None] = None,
        debug_options: Optional[dict[str, Any]] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        mode: Literal["sync", "async"] = "sync",
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
    ) -> None:
        """Initialize with token authentication."""
        ...
    
    @overload
    def __init__(
        self,
        *,
        host: str,
        username: str,
        password: str,
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None,
        debug: Union[str, bool, None] = None,
        debug_options: Optional[dict[str, Any]] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        mode: Literal["sync", "async"] = "sync",
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
    ) -> None:
        """Initialize with username/password authentication."""
        ...
    
    def __init__(
        self,
        *,
        host: Optional[str] = None,
        token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client: Optional[IHTTPClient] = None,
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None,
        debug: Union[str, bool, None] = None,
        debug_options: Optional[dict[str, Any]] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        mode: Literal["sync", "async"] = "sync",
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
    ) -> None:
        """Initialize FortiOS client with custom client or authentication."""
        ...
    
    # Properties
    @property
    def api(self) -> API:
        """Primary entry point to FortiOS endpoints (cmdb/monitor/log/service)."""
        ...
    
    @property
    def cmdb(self) -> Any:
        """Shortcut to CMDB API (configuration management)."""
        ...
    
    @property
    def monitor(self) -> Any:
        """Shortcut to Monitor API (runtime data)."""
        ...
    
    @property
    def log(self) -> Any:
        """Shortcut to Log API (log queries)."""
        ...
    
    @property
    def firewall(self) -> FirewallNamespace:
        """Convenience wrappers for firewall operations."""
        ...
    
    @property
    def host(self) -> Optional[str]:
        """FortiGate hostname or IP address."""
        ...
    
    @property
    def port(self) -> Optional[int]:
        """HTTPS port number."""
        ...
    
    @property
    def vdom(self) -> Optional[str]:
        """Active virtual domain."""
        ...
    
    @property
    def error_mode(self) -> Literal["raise", "return", "print"]:
        """Default error handling mode for convenience wrappers."""
        ...
    
    @property
    def error_format(self) -> Literal["detailed", "simple", "code_only"]:
        """Default error message format for convenience wrappers."""
        ...
    
    @property
    def connection_stats(self) -> dict[str, Any]:
        """Get real-time connection pool statistics.
        
        Returns:
            Dictionary with connection metrics including:
            - max_connections: Maximum allowed connections
            - max_keepalive_connections: Maximum keepalive connections
            - active_requests: Currently active requests
            - total_requests: Total requests made
            - pool_exhaustion_count: Number of pool exhaustion events
            - pool_exhaustion_timestamps: Timestamps of exhaustion events
        
        Example:
            >>> fgt = FortiOS(host="192.168.1.99", token="your-token")
            >>> stats = fgt.connection_stats
            >>> print(f"Active: {stats['active_requests']}, Total: {stats['total_requests']}")
        """
        ...
    
    @property
    def last_request(self) -> dict[str, Any] | None:
        """Get detailed information about the last API request.
        
        Returns:
            Dictionary with request details including:
            - method: HTTP method (GET, POST, etc.)
            - endpoint: API endpoint path
            - params: Request parameters
            - response_time_ms: Response time in milliseconds
            - status_code: HTTP status code
            Returns None if no requests have been made yet.
        
        Example:
            >>> fgt = FortiOS(host="192.168.1.99", token="your-token")
            >>> fgt.cmdb.firewall.address.get()
            >>> info = fgt.last_request
            >>> print(f"Last request took {info['response_time_ms']:.1f}ms")
        """
        ...
    
    # Methods
    def get_connection_stats(self) -> dict[str, Any]:
        """Get HTTP connection pool statistics and metrics (deprecated - use connection_stats property)."""
        ...
    
    def get_write_operations(self) -> list[dict[str, Any]]:
        """Get list of write operations performed.
        
        Returns:
            List of dictionaries with operation details (only if track_operations=True)
        """
        ...
    
    def close(self) -> None:
        """Close HTTP client connection and release resources."""
        ...
    
    # Context manager
    def __enter__(self) -> FortiOS: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
