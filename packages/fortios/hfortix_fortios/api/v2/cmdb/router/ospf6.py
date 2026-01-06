"""
FortiOS CMDB - Router ospf6

Configuration endpoint for managing cmdb router/ospf6 objects.

API Endpoints:
    GET    /cmdb/router/ospf6
    POST   /cmdb/router/ospf6
    PUT    /cmdb/router/ospf6/{identifier}
    DELETE /cmdb/router/ospf6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_ospf6.get()

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


class Ospf6(MetadataMixin):
    """Ospf6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ospf6"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ospf6 endpoint."""
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
        Retrieve router/ospf6 configuration.

        Configure IPv6 OSPF.

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
            >>> # Get all router/ospf6 objects
            >>> result = fgt.api.cmdb.router_ospf6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_ospf6.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_ospf6.get(action="schema")

        See Also:
            - post(): Create new router/ospf6 object
            - put(): Update existing router/ospf6 object
            - delete(): Remove router/ospf6 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/ospf6/{name}"
        else:
            endpoint = "/router/ospf6"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        abr_type: str | None = None,
        auto_cost_ref_bandwidth: int | None = None,
        default_information_originate: str | None = None,
        log_neighbour_changes: str | None = None,
        default_information_metric: int | None = None,
        default_information_metric_type: str | None = None,
        default_information_route_map: str | None = None,
        default_metric: int | None = None,
        router_id: str | None = None,
        spf_timers: str | None = None,
        bfd: str | None = None,
        restart_mode: str | None = None,
        restart_period: int | None = None,
        restart_on_topology_change: str | None = None,
        area: str | list | None = None,
        ospf6_interface: str | list | None = None,
        redistribute: str | list | None = None,
        passive_interface: str | list | None = None,
        summary_address: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/ospf6 object.

        Configure IPv6 OSPF.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            abr_type: Area border router type.
            auto_cost_ref_bandwidth: Reference bandwidth in terms of megabits per second.
            default_information_originate: Enable/disable generation of default route.
            log_neighbour_changes: Log OSPFv3 neighbor changes.
            default_information_metric: Default information metric.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_ospf6.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_ospf6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            abr_type=abr_type,
            auto_cost_ref_bandwidth=auto_cost_ref_bandwidth,
            default_information_originate=default_information_originate,
            log_neighbour_changes=log_neighbour_changes,
            default_information_metric=default_information_metric,
            default_information_metric_type=default_information_metric_type,
            default_information_route_map=default_information_route_map,
            default_metric=default_metric,
            router_id=router_id,
            spf_timers=spf_timers,
            bfd=bfd,
            restart_mode=restart_mode,
            restart_period=restart_period,
            restart_on_topology_change=restart_on_topology_change,
            area=area,
            ospf6_interface=ospf6_interface,
            redistribute=redistribute,
            passive_interface=passive_interface,
            summary_address=summary_address,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ospf6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/ospf6",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/ospf6/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





