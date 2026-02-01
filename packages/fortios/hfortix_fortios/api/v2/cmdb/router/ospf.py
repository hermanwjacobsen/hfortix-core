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
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.router_ospf.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
    quote_path_param,  # URL encoding for path parameters
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Ospf(CRUDEndpoint, MetadataMixin):
    """Ospf Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ospf"
    
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
        """Initialize Ospf endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve router/ospf configuration.

        Configure OSPF.

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
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            API response as dictionary. Returns Coroutine if using async client.
            Access results via dictionary keys (e.g., result['results'], result['http_status']).
            
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
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.router_ospf.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.router_ospf.get_schema()

        See Also:
            - post(): Create new router/ospf object
            - put(): Update existing router/ospf object
            - delete(): Remove router/ospf object
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
            endpoint = f"/router/ospf/{quote_path_param(name)}"
            unwrap_single = True
        else:
            endpoint = "/router/ospf"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
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
            >>> schema = fgt.api.cmdb.router_ospf.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.router_ospf.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = None,
        auto_cost_ref_bandwidth: int | None = None,
        distance_external: int | None = None,
        distance_inter_area: int | None = None,
        distance_intra_area: int | None = None,
        database_overflow: Literal["enable", "disable"] | None = None,
        database_overflow_max_lsas: int | None = None,
        database_overflow_time_to_recover: int | None = None,
        default_information_originate: Literal["enable", "always", "disable"] | None = None,
        default_information_metric: int | None = None,
        default_information_metric_type: Literal["1", "2"] | None = None,
        default_information_route_map: str | None = None,
        default_metric: int | None = None,
        distance: int | None = None,
        lsa_refresh_interval: int | None = None,
        rfc1583_compatible: Literal["enable", "disable"] | None = None,
        router_id: str | None = None,
        spf_timers: str | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        log_neighbour_changes: Literal["enable", "disable"] | None = None,
        distribute_list_in: str | None = None,
        distribute_route_map_in: str | None = None,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = None,
        restart_period: int | None = None,
        restart_on_topology_change: Literal["enable", "disable"] | None = None,
        area: str | list[str] | list[dict[str, Any]] | None = None,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = None,
        network: str | list[str] | list[dict[str, Any]] | None = None,
        neighbor: str | list[str] | list[dict[str, Any]] | None = None,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = None,
        summary_address: str | list[str] | list[dict[str, Any]] | None = None,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = None,
        redistribute: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
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
            database_overflow: Enable/disable database overflow.
            database_overflow_max_lsas: Database overflow maximum LSAs.
            database_overflow_time_to_recover: Database overflow time to recover (sec).
            default_information_originate: Enable/disable generation of default route.
            default_information_metric: Default information metric.
            default_information_metric_type: Default information metric type.
            default_information_route_map: Default information route map.
            default_metric: Default metric of redistribute routes.
            distance: Distance of the route.
            lsa_refresh_interval: The minimal OSPF LSA update time interval
            rfc1583_compatible: Enable/disable RFC1583 compatibility.
            router_id: Router ID.
            spf_timers: SPF calculation frequency.
            bfd: Bidirectional Forwarding Detection (BFD).
            log_neighbour_changes: Log of OSPF neighbor changes.
            distribute_list_in: Filter incoming routes.
            distribute_route_map_in: Filter incoming external routes by route-map.
            restart_mode: OSPF restart mode (graceful or LLS).
            restart_period: Graceful restart period.
            restart_on_topology_change: Enable/disable continuing graceful restart upon topology change.
            area: OSPF area configuration.
            ospf_interface: OSPF interface configuration.
            network: OSPF network configuration.
            neighbor: OSPF neighbor configuration are used when OSPF runs on non-broadcast media.
            passive_interface: Passive interface configuration.
            summary_address: IP address summary configuration.
            distribute_list: Distribute list configuration.
            redistribute: Redistribute configuration.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            API response as dictionary. Returns Coroutine if using async client.

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
        payload_data = build_api_payload(
            api_type="cmdb",
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
        
        # Singleton endpoint - no identifier needed
        endpoint = "/router/ospf"

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom        )





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
        Move router/ospf object to a new position.
        
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
            >>> fgt.api.cmdb.router_ospf.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/ospf",
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
        Clone router/ospf object.
        
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
            >>> fgt.api.cmdb.router_ospf.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/ospf",
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
        Check if router/ospf object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.router_ospf.exists(name="myobj"):
            ...     fgt.api.cmdb.router_ospf.post(payload_dict=data)
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/router/ospf"
        endpoint = f"{endpoint}/{quote_path_param(name)}"
        
        # Make request with silent=True to suppress 404 error logging
        # (404 is expected when checking existence - it just means "doesn't exist")
        # Use _wrapped_client to access the underlying HTTPClient directly
        # (self._client is ResponseProcessingClient, _wrapped_client is HTTPClient)
        try:
            result = self._client._wrapped_client.get(
                "cmdb",
                endpoint,
                params=None,
                vdom=vdom,
                raw_json=True,
                silent=True,
            )
            
            if isinstance(result, dict):
                # Synchronous response - check status
                return result.get("status") == "success"
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await result
                    return r.get("status") == "success"
                return _check()
        except Exception:
            # Any error (404, network, etc.) means we can't confirm existence
            return False

