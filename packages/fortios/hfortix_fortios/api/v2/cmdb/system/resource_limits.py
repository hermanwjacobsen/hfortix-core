"""
FortiOS CMDB - System resource_limits

Configuration endpoint for managing cmdb system/resource_limits objects.

API Endpoints:
    GET    /cmdb/system/resource_limits
    POST   /cmdb/system/resource_limits
    PUT    /cmdb/system/resource_limits/{identifier}
    DELETE /cmdb/system/resource_limits/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_resource_limits.get()

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


class ResourceLimits(MetadataMixin):
    """ResourceLimits Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "resource_limits"

    def __init__(self, client: "IHTTPClient"):
        """Initialize ResourceLimits endpoint."""
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
        Retrieve system/resource_limits configuration.

        Configure resource limits.

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
            >>> # Get all system/resource_limits objects
            >>> result = fgt.api.cmdb.system_resource_limits.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_resource_limits.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_resource_limits.get(action="schema")

        See Also:
            - post(): Create new system/resource_limits object
            - put(): Update existing system/resource_limits object
            - delete(): Remove system/resource_limits object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/resource-limits/{name}"
        else:
            endpoint = "/system/resource-limits"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        session: int | None = None,
        ipsec_phase1: int | None = None,
        ipsec_phase2: int | None = None,
        ipsec_phase1_interface: int | None = None,
        ipsec_phase2_interface: int | None = None,
        dialup_tunnel: int | None = None,
        firewall_policy: int | None = None,
        firewall_address: int | None = None,
        firewall_addrgrp: int | None = None,
        custom_service: int | None = None,
        service_group: int | None = None,
        onetime_schedule: int | None = None,
        recurring_schedule: int | None = None,
        user: int | None = None,
        user_group: int | None = None,
        sslvpn: int | None = None,
        proxy: int | None = None,
        log_disk_quota: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/resource_limits object.

        Configure resource limits.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            session: Maximum number of sessions.
            ipsec_phase1: Maximum number of VPN IPsec phase1 tunnels.
            ipsec_phase2: Maximum number of VPN IPsec phase2 tunnels.
            ipsec_phase1_interface: Maximum number of VPN IPsec phase1 interface tunnels.
            ipsec_phase2_interface: Maximum number of VPN IPsec phase2 interface tunnels.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_resource_limits.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_resource_limits.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            session=session,
            ipsec_phase1=ipsec_phase1,
            ipsec_phase2=ipsec_phase2,
            ipsec_phase1_interface=ipsec_phase1_interface,
            ipsec_phase2_interface=ipsec_phase2_interface,
            dialup_tunnel=dialup_tunnel,
            firewall_policy=firewall_policy,
            firewall_address=firewall_address,
            firewall_addrgrp=firewall_addrgrp,
            custom_service=custom_service,
            service_group=service_group,
            onetime_schedule=onetime_schedule,
            recurring_schedule=recurring_schedule,
            user=user,
            user_group=user_group,
            sslvpn=sslvpn,
            proxy=proxy,
            log_disk_quota=log_disk_quota,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.resource_limits import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/resource_limits",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/resource-limits/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





