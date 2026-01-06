"""
FortiOS CMDB - System fabric_vpn

Configuration endpoint for managing cmdb system/fabric_vpn objects.

API Endpoints:
    GET    /cmdb/system/fabric_vpn
    POST   /cmdb/system/fabric_vpn
    PUT    /cmdb/system/fabric_vpn/{identifier}
    DELETE /cmdb/system/fabric_vpn/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_fabric_vpn.get()

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


class FabricVpn(MetadataMixin):
    """FabricVpn Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fabric_vpn"

    def __init__(self, client: "IHTTPClient"):
        """Initialize FabricVpn endpoint."""
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
        Retrieve system/fabric_vpn configuration.

        Setup for self orchestrated fabric auto discovery VPN.

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
            >>> # Get all system/fabric_vpn objects
            >>> result = fgt.api.cmdb.system_fabric_vpn.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_fabric_vpn.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_fabric_vpn.get(action="schema")

        See Also:
            - post(): Create new system/fabric_vpn object
            - put(): Update existing system/fabric_vpn object
            - delete(): Remove system/fabric_vpn object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/fabric-vpn/{name}"
        else:
            endpoint = "/system/fabric-vpn"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        sync_mode: str | None = None,
        branch_name: str | None = None,
        policy_rule: str | None = None,
        vpn_role: str | None = None,
        overlays: str | list | None = None,
        advertised_subnets: str | list | None = None,
        loopback_address_block: Any | None = None,
        loopback_interface: str | None = None,
        loopback_advertised_subnet: int | None = None,
        psksecret: Any | None = None,
        bgp_as: str | None = None,
        sdwan_zone: str | None = None,
        health_checks: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/fabric_vpn object.

        Setup for self orchestrated fabric auto discovery VPN.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable Fabric VPN.
            sync_mode: Setting synchronized by fabric or manual.
            branch_name: Branch name.
            policy_rule: Policy creation rule.
            vpn_role: Fabric VPN role.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_fabric_vpn.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_fabric_vpn.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            sync_mode=sync_mode,
            branch_name=branch_name,
            policy_rule=policy_rule,
            vpn_role=vpn_role,
            overlays=overlays,
            advertised_subnets=advertised_subnets,
            loopback_address_block=loopback_address_block,
            loopback_interface=loopback_interface,
            loopback_advertised_subnet=loopback_advertised_subnet,
            psksecret=psksecret,
            bgp_as=bgp_as,
            sdwan_zone=sdwan_zone,
            health_checks=health_checks,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fabric_vpn import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/fabric_vpn",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/fabric-vpn/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





