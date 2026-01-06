"""
FortiOS CMDB - Webfilter ips_urlfilter_setting6

Configuration endpoint for managing cmdb webfilter/ips_urlfilter_setting6 objects.

API Endpoints:
    GET    /cmdb/webfilter/ips_urlfilter_setting6
    POST   /cmdb/webfilter/ips_urlfilter_setting6
    PUT    /cmdb/webfilter/ips_urlfilter_setting6/{identifier}
    DELETE /cmdb/webfilter/ips_urlfilter_setting6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.webfilter_ips_urlfilter_setting6.get()

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


class IpsUrlfilterSetting6(MetadataMixin):
    """IpsUrlfilterSetting6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ips_urlfilter_setting6"

    def __init__(self, client: "IHTTPClient"):
        """Initialize IpsUrlfilterSetting6 endpoint."""
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
        Retrieve webfilter/ips_urlfilter_setting6 configuration.

        Configure IPS URL filter settings for IPv6.

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
            >>> # Get all webfilter/ips_urlfilter_setting6 objects
            >>> result = fgt.api.cmdb.webfilter_ips_urlfilter_setting6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.webfilter_ips_urlfilter_setting6.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.webfilter_ips_urlfilter_setting6.get(action="schema")

        See Also:
            - post(): Create new webfilter/ips_urlfilter_setting6 object
            - put(): Update existing webfilter/ips_urlfilter_setting6 object
            - delete(): Remove webfilter/ips_urlfilter_setting6 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/webfilter/ips-urlfilter-setting6/{name}"
        else:
            endpoint = "/webfilter/ips-urlfilter-setting6"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        device: str | None = None,
        distance: int | None = None,
        gateway6: str | None = None,
        geo_filter: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing webfilter/ips_urlfilter_setting6 object.

        Configure IPS URL filter settings for IPv6.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            device: Interface for this route.
            distance: Administrative distance (1 - 255) for this route.
            gateway6: Gateway IPv6 address for this route.
            geo_filter: Filter based on geographical location. Route will NOT be installed if the resolved IPv6 address belongs to the country in the filter.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.webfilter_ips_urlfilter_setting6.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.webfilter_ips_urlfilter_setting6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            device=device,
            distance=distance,
            gateway6=gateway6,
            geo_filter=geo_filter,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ips_urlfilter_setting6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/webfilter/ips_urlfilter_setting6",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/webfilter/ips-urlfilter-setting6/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





