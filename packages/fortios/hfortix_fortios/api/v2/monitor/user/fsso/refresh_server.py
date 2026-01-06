"""
FortiOS MONITOR - User fsso refresh_server

Configuration endpoint for managing monitor user/fsso/refresh_server objects.

API Endpoints:
    GET    /monitor/user/fsso/refresh_server
    POST   /monitor/user/fsso/refresh_server
    PUT    /monitor/user/fsso/refresh_server/{identifier}
    DELETE /monitor/user/fsso/refresh_server/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.user_fsso_refresh_server.get()

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


class RefreshServer(MetadataMixin):
    """RefreshServer Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "refresh_server"

    def __init__(self, client: "IHTTPClient"):
        """Initialize RefreshServer endpoint."""
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
        Retrieve user/fsso/refresh_server configuration.

        Refresh remote agent group list for all fsso agents.

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
            >>> # Get all user/fsso/refresh_server objects
            >>> result = fgt.api.monitor.user_fsso_refresh_server.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.user_fsso_refresh_server.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.monitor.user_fsso_refresh_server.get(action="schema")

        See Also:
            - post(): Create new user/fsso/refresh_server object
            - put(): Update existing user/fsso/refresh_server object
            - delete(): Remove user/fsso/refresh_server object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/user/fsso/refresh-server/{name}"
        else:
            endpoint = "/user/fsso/refresh-server"
        
        params.update(kwargs)
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )







