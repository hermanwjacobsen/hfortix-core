"""
FortiOS CMDB - System ipam

Configuration endpoint for managing cmdb system/ipam objects.

API Endpoints:
    GET    /cmdb/system/ipam
    POST   /cmdb/system/ipam
    PUT    /cmdb/system/ipam/{identifier}
    DELETE /cmdb/system/ipam/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ipam.get()

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


class Ipam(MetadataMixin):
    """Ipam Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ipam"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ipam endpoint."""
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
        Retrieve system/ipam configuration.

        Configure IP address management services.

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
            >>> # Get all system/ipam objects
            >>> result = fgt.api.cmdb.system_ipam.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ipam.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ipam.get(action="schema")

        See Also:
            - post(): Create new system/ipam object
            - put(): Update existing system/ipam object
            - delete(): Remove system/ipam object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ipam/{name}"
        else:
            endpoint = "/system/ipam"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        server_type: str | None = None,
        automatic_conflict_resolution: str | None = None,
        require_subnet_size_match: str | None = None,
        manage_lan_addresses: str | None = None,
        manage_lan_extension_addresses: str | None = None,
        manage_ssid_addresses: str | None = None,
        pools: str | list | None = None,
        rules: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ipam object.

        Configure IP address management services.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable IP address management services.
            server_type: Configure the type of IPAM server to use.
            automatic_conflict_resolution: Enable/disable automatic conflict resolution.
            require_subnet_size_match: Enable/disable reassignment of subnets to make requested and actual sizes match.
            manage_lan_addresses: Enable/disable default management of LAN interface addresses.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ipam.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ipam.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            server_type=server_type,
            automatic_conflict_resolution=automatic_conflict_resolution,
            require_subnet_size_match=require_subnet_size_match,
            manage_lan_addresses=manage_lan_addresses,
            manage_lan_extension_addresses=manage_lan_extension_addresses,
            manage_ssid_addresses=manage_ssid_addresses,
            pools=pools,
            rules=rules,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ipam import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ipam",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ipam/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





