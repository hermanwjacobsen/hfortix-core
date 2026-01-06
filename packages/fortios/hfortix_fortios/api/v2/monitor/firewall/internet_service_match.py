"""
FortiOS MONITOR - Firewall internet_service_match

Configuration endpoint for managing monitor firewall/internet_service_match objects.

API Endpoints:
    GET    /monitor/firewall/internet_service_match
    POST   /monitor/firewall/internet_service_match
    PUT    /monitor/firewall/internet_service_match/{identifier}
    DELETE /monitor/firewall/internet_service_match/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.firewall_internet_service_match.get()

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


class InternetServiceMatch(MetadataMixin):
    """InternetServiceMatch Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "internet_service_match"

    def __init__(self, client: "IHTTPClient"):
        """Initialize InternetServiceMatch endpoint."""
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
        Retrieve firewall/internet_service_match configuration.

        List internet services that exist at a given IP or Subnet.

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
            >>> # Get all firewall/internet_service_match objects
            >>> result = fgt.api.monitor.firewall_internet_service_match.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.firewall_internet_service_match.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.monitor.firewall_internet_service_match.get(action="schema")

        See Also:
            - post(): Create new firewall/internet_service_match object
            - put(): Update existing firewall/internet_service_match object
            - delete(): Remove firewall/internet_service_match object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/firewall/internet-service-match/{name}"
        else:
            endpoint = "/firewall/internet-service-match"
        
        params.update(kwargs)
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )







