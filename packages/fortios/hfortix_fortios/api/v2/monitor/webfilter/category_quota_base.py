"""
FortiOS MONITOR - Webfilter category_quota

Configuration endpoint for managing monitor webfilter/category_quota objects.

API Endpoints:
    GET    /monitor/webfilter/category_quota
    POST   /monitor/webfilter/category_quota
    PUT    /monitor/webfilter/category_quota/{identifier}
    DELETE /monitor/webfilter/category_quota/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.webfilter_category_quota.get()

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


class CategoryQuota(MetadataMixin):
    """CategoryQuota Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "category_quota"

    def __init__(self, client: "IHTTPClient"):
        """Initialize CategoryQuota endpoint."""
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
        Retrieve webfilter/category_quota configuration.

        Retrieve quota usage statistics for webfilter categories.

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
            >>> # Get all webfilter/category_quota objects
            >>> result = fgt.api.monitor.webfilter_category_quota.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.webfilter_category_quota.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.monitor.webfilter_category_quota.get(action="schema")

        See Also:
            - post(): Create new webfilter/category_quota object
            - put(): Update existing webfilter/category_quota object
            - delete(): Remove webfilter/category_quota object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/webfilter/category-quota/{name}"
        else:
            endpoint = "/webfilter/category-quota"
        
        params.update(kwargs)
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )







