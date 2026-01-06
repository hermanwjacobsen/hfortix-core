"""
FortiOS CMDB - System vdom_dns

Configuration endpoint for managing cmdb system/vdom_dns objects.

API Endpoints:
    GET    /cmdb/system/vdom_dns
    POST   /cmdb/system/vdom_dns
    PUT    /cmdb/system/vdom_dns/{identifier}
    DELETE /cmdb/system/vdom_dns/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_vdom_dns.get()

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


class VdomDns(MetadataMixin):
    """VdomDns Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vdom_dns"

    def __init__(self, client: "IHTTPClient"):
        """Initialize VdomDns endpoint."""
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
        Retrieve system/vdom_dns configuration.

        Configure DNS servers for a non-management VDOM.

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
            >>> # Get all system/vdom_dns objects
            >>> result = fgt.api.cmdb.system_vdom_dns.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_vdom_dns.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_vdom_dns.get(action="schema")

        See Also:
            - post(): Create new system/vdom_dns object
            - put(): Update existing system/vdom_dns object
            - delete(): Remove system/vdom_dns object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/vdom-dns/{name}"
        else:
            endpoint = "/system/vdom-dns"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom_dns: str | None = None,
        primary: str | None = None,
        secondary: str | None = None,
        protocol: str | list | None = None,
        ssl_certificate: str | None = None,
        server_hostname: str | list | None = None,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        server_select_method: str | None = None,
        alt_primary: str | None = None,
        alt_secondary: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/vdom_dns object.

        Configure DNS servers for a non-management VDOM.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            vdom_dns: Enable/disable configuring DNS servers for the current VDOM.
            primary: Primary DNS server IP address for the VDOM.
            secondary: Secondary DNS server IP address for the VDOM.
            protocol: DNS transport protocols.
            ssl_certificate: Name of local certificate for SSL connections.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_vdom_dns.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_vdom_dns.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            vdom_dns=vdom_dns,
            primary=primary,
            secondary=secondary,
            protocol=protocol,
            ssl_certificate=ssl_certificate,
            server_hostname=server_hostname,
            ip6_primary=ip6_primary,
            ip6_secondary=ip6_secondary,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            server_select_method=server_select_method,
            alt_primary=alt_primary,
            alt_secondary=alt_secondary,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vdom_dns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/vdom_dns",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/vdom-dns/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





