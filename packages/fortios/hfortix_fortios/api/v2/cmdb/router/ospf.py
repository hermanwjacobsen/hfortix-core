"""
FortiOS CMDB - Router ospf

Configuration endpoint for managing cmdb router/ospf objects.

API Endpoints:
    GET    /cmdb/router/ospf
    POST   /cmdb/router/ospf
    PUT    /cmdb/router/ospf/{identifier}
    DELETE /cmdb/router/ospf/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_ospf.get()

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


class Ospf(MetadataMixin):
    """Ospf Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ospf"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ospf endpoint."""
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
        Retrieve router/ospf configuration.

        Configure OSPF.

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
            >>> # Get all router/ospf objects
            >>> result = fgt.api.cmdb.router_ospf.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_ospf.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_ospf.get(action="schema")

        See Also:
            - post(): Create new router/ospf object
            - put(): Update existing router/ospf object
            - delete(): Remove router/ospf object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/ospf/{name}"
        else:
            endpoint = "/router/ospf"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        abr_type: str | None = None,
        auto_cost_ref_bandwidth: int | None = None,
        distance_external: int | None = None,
        distance_inter_area: int | None = None,
        distance_intra_area: int | None = None,
        database_overflow: str | None = None,
        database_overflow_max_lsas: int | None = None,
        database_overflow_time_to_recover: int | None = None,
        default_information_originate: str | None = None,
        default_information_metric: int | None = None,
        default_information_metric_type: str | None = None,
        default_information_route_map: str | None = None,
        default_metric: int | None = None,
        distance: int | None = None,
        lsa_refresh_interval: int | None = None,
        rfc1583_compatible: str | None = None,
        router_id: str | None = None,
        spf_timers: str | None = None,
        bfd: str | None = None,
        log_neighbour_changes: str | None = None,
        distribute_list_in: str | None = None,
        distribute_route_map_in: str | None = None,
        restart_mode: str | None = None,
        restart_period: int | None = None,
        restart_on_topology_change: str | None = None,
        area: str | list | None = None,
        ospf_interface: str | list | None = None,
        network: str | list | None = None,
        neighbor: str | list | None = None,
        passive_interface: str | list | None = None,
        summary_address: str | list | None = None,
        distribute_list: str | list | None = None,
        redistribute: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/ospf object.

        Configure OSPF.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            abr_type: Area border router type.
            auto_cost_ref_bandwidth: Reference bandwidth in terms of megabits per second.
            distance_external: Administrative external distance.
            distance_inter_area: Administrative inter-area distance.
            distance_intra_area: Administrative intra-area distance.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_ospf.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_ospf.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            abr_type=abr_type,
            auto_cost_ref_bandwidth=auto_cost_ref_bandwidth,
            distance_external=distance_external,
            distance_inter_area=distance_inter_area,
            distance_intra_area=distance_intra_area,
            database_overflow=database_overflow,
            database_overflow_max_lsas=database_overflow_max_lsas,
            database_overflow_time_to_recover=database_overflow_time_to_recover,
            default_information_originate=default_information_originate,
            default_information_metric=default_information_metric,
            default_information_metric_type=default_information_metric_type,
            default_information_route_map=default_information_route_map,
            default_metric=default_metric,
            distance=distance,
            lsa_refresh_interval=lsa_refresh_interval,
            rfc1583_compatible=rfc1583_compatible,
            router_id=router_id,
            spf_timers=spf_timers,
            bfd=bfd,
            log_neighbour_changes=log_neighbour_changes,
            distribute_list_in=distribute_list_in,
            distribute_route_map_in=distribute_route_map_in,
            restart_mode=restart_mode,
            restart_period=restart_period,
            restart_on_topology_change=restart_on_topology_change,
            area=area,
            ospf_interface=ospf_interface,
            network=network,
            neighbor=neighbor,
            passive_interface=passive_interface,
            summary_address=summary_address,
            distribute_list=distribute_list,
            redistribute=redistribute,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ospf import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/ospf",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/ospf/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





