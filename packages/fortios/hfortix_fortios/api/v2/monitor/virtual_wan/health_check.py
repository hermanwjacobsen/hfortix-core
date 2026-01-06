"""
FortiOS MONITOR - Virtual_wan health_check

Configuration endpoint for managing monitor virtual_wan/health_check objects.

API Endpoints:
    GET    /monitor/virtual_wan/health_check
    POST   /monitor/virtual_wan/health_check
    PUT    /monitor/virtual_wan/health_check/{identifier}
    DELETE /monitor/virtual_wan/health_check/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.virtual_wan_health_check.get()

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin


class HealthCheck(MetadataMixin):
    """HealthCheck Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "health_check"

    def __init__(self, client: "IHTTPClient"):
        """Initialize HealthCheck endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve virtual_wan/health_check configuration.

        Retrieve health-check statistics for each SD-WAN link. To be deprecated and replaced by /api/v2/monitor/virtual-wan/sla-log?latest=1&sla=<sla_name> for SLA health metrics 

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            payload_dict: Additional query parameters (filters, format, etc.)
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional query parameters (action, format, etc.)

        Returns:
            Configuration data as dict. Returns Coroutine if using async client.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all virtual_wan/health_check objects
            >>> result = fgt.api.monitor.virtual_wan_health_check.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.virtual_wan_health_check.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.monitor.virtual_wan_health_check.get(action="schema")

        See Also:
            - post(): Create new virtual_wan/health_check object
            - put(): Update existing virtual_wan/health_check object
            - delete(): Remove virtual_wan/health_check object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/virtual-wan/health-check/{name}"
        else:
            endpoint = "/virtual-wan/health-check"
        
        params.update(kwargs)
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )







