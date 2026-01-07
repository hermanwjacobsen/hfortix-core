"""
FortiOS CMDB - Router bgp

Configuration endpoint for managing cmdb router/bgp objects.

API Endpoints:
    GET    /cmdb/router/bgp
    POST   /cmdb/router/bgp
    PUT    /cmdb/router/bgp/{identifier}
    DELETE /cmdb/router/bgp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_bgp.get()

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, Literal
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


class Bgp(MetadataMixin):
    """Bgp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "bgp"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Bgp endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve router/bgp configuration.

        Configure BGP.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional query parameters passed directly to API.

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
            >>> # Get all router/bgp objects
            >>> result = fgt.api.cmdb.router_bgp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_bgp.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.router_bgp.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.router_bgp.get_schema()

        See Also:
            - post(): Create new router/bgp object
            - put(): Update existing router/bgp object
            - delete(): Remove router/bgp object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        
        if name:
            endpoint = f"/router/bgp/{name}"
        else:
            endpoint = "/router/bgp"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.router_bgp.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.router_bgp.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        asn: str | None = None,
        router_id: str | None = None,
        keepalive_timer: int | None = None,
        holdtime_timer: int | None = None,
        always_compare_med: Literal["enable", "disable"] | None = None,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = None,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = None,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = None,
        bestpath_med_confed: Literal["enable", "disable"] | None = None,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = None,
        client_to_client_reflection: Literal["enable", "disable"] | None = None,
        dampening: Literal["enable", "disable"] | None = None,
        deterministic_med: Literal["enable", "disable"] | None = None,
        ebgp_multipath: Literal["enable", "disable"] | None = None,
        ibgp_multipath: Literal["enable", "disable"] | None = None,
        enforce_first_as: Literal["enable", "disable"] | None = None,
        fast_external_failover: Literal["enable", "disable"] | None = None,
        log_neighbour_changes: Literal["enable", "disable"] | None = None,
        network_import_check: Literal["enable", "disable"] | None = None,
        ignore_optional_capability: Literal["enable", "disable"] | None = None,
        additional_path: Literal["enable", "disable"] | None = None,
        additional_path6: Literal["enable", "disable"] | None = None,
        additional_path_vpnv4: Literal["enable", "disable"] | None = None,
        additional_path_vpnv6: Literal["enable", "disable"] | None = None,
        multipath_recursive_distance: Literal["enable", "disable"] | None = None,
        recursive_next_hop: Literal["enable", "disable"] | None = None,
        recursive_inherit_priority: Literal["enable", "disable"] | None = None,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = None,
        cluster_id: str | None = None,
        confederation_identifier: int | None = None,
        confederation_peers: str | list | None = None,
        dampening_route_map: str | None = None,
        dampening_reachability_half_life: int | None = None,
        dampening_reuse: int | None = None,
        dampening_suppress: int | None = None,
        dampening_max_suppress_time: int | None = None,
        dampening_unreachability_half_life: int | None = None,
        default_local_preference: int | None = None,
        scan_time: int | None = None,
        distance_external: int | None = None,
        distance_internal: int | None = None,
        distance_local: int | None = None,
        synchronization: Literal["enable", "disable"] | None = None,
        graceful_restart: Literal["enable", "disable"] | None = None,
        graceful_restart_time: int | None = None,
        graceful_stalepath_time: int | None = None,
        graceful_update_delay: int | None = None,
        graceful_end_on_timer: Literal["enable", "disable"] | None = None,
        additional_path_select: int | None = None,
        additional_path_select6: int | None = None,
        additional_path_select_vpnv4: int | None = None,
        additional_path_select_vpnv6: int | None = None,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = None,
        aggregate_address: str | list | None = None,
        aggregate_address6: str | list | None = None,
        neighbor: str | list | None = None,
        neighbor_group: str | list | None = None,
        neighbor_range: str | list | None = None,
        neighbor_range6: str | list | None = None,
        network: str | list | None = None,
        network6: str | list | None = None,
        redistribute: str | list | None = None,
        redistribute6: str | list | None = None,
        admin_distance: str | list | None = None,
        vrf: str | list | None = None,
        vrf6: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/bgp object.

        Configure BGP.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            asn: Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP.
            router_id: Router ID.
            keepalive_timer: Frequency to send keep alive requests.
            holdtime_timer: Number of seconds to mark peer as dead.
            always_compare_med: Enable/disable always compare MED.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_bgp.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_bgp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            asn=asn,
            router_id=router_id,
            keepalive_timer=keepalive_timer,
            holdtime_timer=holdtime_timer,
            always_compare_med=always_compare_med,
            bestpath_as_path_ignore=bestpath_as_path_ignore,
            bestpath_cmp_confed_aspath=bestpath_cmp_confed_aspath,
            bestpath_cmp_routerid=bestpath_cmp_routerid,
            bestpath_med_confed=bestpath_med_confed,
            bestpath_med_missing_as_worst=bestpath_med_missing_as_worst,
            client_to_client_reflection=client_to_client_reflection,
            dampening=dampening,
            deterministic_med=deterministic_med,
            ebgp_multipath=ebgp_multipath,
            ibgp_multipath=ibgp_multipath,
            enforce_first_as=enforce_first_as,
            fast_external_failover=fast_external_failover,
            log_neighbour_changes=log_neighbour_changes,
            network_import_check=network_import_check,
            ignore_optional_capability=ignore_optional_capability,
            additional_path=additional_path,
            additional_path6=additional_path6,
            additional_path_vpnv4=additional_path_vpnv4,
            additional_path_vpnv6=additional_path_vpnv6,
            multipath_recursive_distance=multipath_recursive_distance,
            recursive_next_hop=recursive_next_hop,
            recursive_inherit_priority=recursive_inherit_priority,
            tag_resolve_mode=tag_resolve_mode,
            cluster_id=cluster_id,
            confederation_identifier=confederation_identifier,
            confederation_peers=confederation_peers,
            dampening_route_map=dampening_route_map,
            dampening_reachability_half_life=dampening_reachability_half_life,
            dampening_reuse=dampening_reuse,
            dampening_suppress=dampening_suppress,
            dampening_max_suppress_time=dampening_max_suppress_time,
            dampening_unreachability_half_life=dampening_unreachability_half_life,
            default_local_preference=default_local_preference,
            scan_time=scan_time,
            distance_external=distance_external,
            distance_internal=distance_internal,
            distance_local=distance_local,
            synchronization=synchronization,
            graceful_restart=graceful_restart,
            graceful_restart_time=graceful_restart_time,
            graceful_stalepath_time=graceful_stalepath_time,
            graceful_update_delay=graceful_update_delay,
            graceful_end_on_timer=graceful_end_on_timer,
            additional_path_select=additional_path_select,
            additional_path_select6=additional_path_select6,
            additional_path_select_vpnv4=additional_path_select_vpnv4,
            additional_path_select_vpnv6=additional_path_select_vpnv6,
            cross_family_conditional_adv=cross_family_conditional_adv,
            aggregate_address=aggregate_address,
            aggregate_address6=aggregate_address6,
            neighbor=neighbor,
            neighbor_group=neighbor_group,
            neighbor_range=neighbor_range,
            neighbor_range6=neighbor_range6,
            network=network,
            network6=network6,
            redistribute=redistribute,
            redistribute6=redistribute6,
            admin_distance=admin_distance,
            vrf=vrf,
            vrf6=vrf6,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.bgp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/bgp",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/bgp/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move router/bgp object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.router_bgp.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/bgp",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone router/bgp object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.router_bgp.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/bgp",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if router/bgp object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.router_bgp.exists(name="myobj"):
            ...     fgt.api.cmdb.router_bgp.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
                vdom=vdom,
                raw_json=True
            )
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

