"""
FortiOS CMDB - Webfilter fortiguard

Configuration endpoint for managing cmdb webfilter/fortiguard objects.

API Endpoints:
    GET    /cmdb/webfilter/fortiguard
    POST   /cmdb/webfilter/fortiguard
    PUT    /cmdb/webfilter/fortiguard/{identifier}
    DELETE /cmdb/webfilter/fortiguard/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.webfilter_fortiguard.get()

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


class Fortiguard(MetadataMixin):
    """Fortiguard Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fortiguard"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortiguard endpoint."""
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
        Retrieve webfilter/fortiguard configuration.

        Configure FortiGuard Web Filter service.

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
            >>> # Get all webfilter/fortiguard objects
            >>> result = fgt.api.cmdb.webfilter_fortiguard.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.webfilter_fortiguard.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.webfilter_fortiguard.get(action="schema")

        See Also:
            - post(): Create new webfilter/fortiguard object
            - put(): Update existing webfilter/fortiguard object
            - delete(): Remove webfilter/fortiguard object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/webfilter/fortiguard/{name}"
        else:
            endpoint = "/webfilter/fortiguard"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        cache_mode: str | None = None,
        cache_prefix_match: str | None = None,
        cache_mem_permille: int | None = None,
        ovrd_auth_port_http: int | None = None,
        ovrd_auth_port_https: int | None = None,
        ovrd_auth_port_https_flow: int | None = None,
        ovrd_auth_port_warning: int | None = None,
        ovrd_auth_https: str | None = None,
        warn_auth_https: str | None = None,
        close_ports: str | None = None,
        request_packet_size_limit: int | None = None,
        embed_image: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing webfilter/fortiguard object.

        Configure FortiGuard Web Filter service.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            cache_mode: Cache entry expiration mode.
            cache_prefix_match: Enable/disable prefix matching in the cache.
            cache_mem_permille: Maximum permille of available memory allocated to caching (1 - 150).
            ovrd_auth_port_http: Port to use for FortiGuard Web Filter HTTP override authentication.
            ovrd_auth_port_https: Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mode.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.webfilter_fortiguard.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.webfilter_fortiguard.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            cache_mode=cache_mode,
            cache_prefix_match=cache_prefix_match,
            cache_mem_permille=cache_mem_permille,
            ovrd_auth_port_http=ovrd_auth_port_http,
            ovrd_auth_port_https=ovrd_auth_port_https,
            ovrd_auth_port_https_flow=ovrd_auth_port_https_flow,
            ovrd_auth_port_warning=ovrd_auth_port_warning,
            ovrd_auth_https=ovrd_auth_https,
            warn_auth_https=warn_auth_https,
            close_ports=close_ports,
            request_packet_size_limit=request_packet_size_limit,
            embed_image=embed_image,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fortiguard import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/webfilter/fortiguard",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/webfilter/fortiguard/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





