"""
FortiOS CMDB - Switch_controller managed_switch

Configuration endpoint for managing cmdb switch_controller/managed_switch objects.

API Endpoints:
    GET    /cmdb/switch_controller/managed_switch
    POST   /cmdb/switch_controller/managed_switch
    PUT    /cmdb/switch_controller/managed_switch/{identifier}
    DELETE /cmdb/switch_controller/managed_switch/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_managed_switch.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.switch_controller_managed_switch.post(
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

from typing import TYPE_CHECKING, Any, Union, Literal
if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class ManagedSwitch(CRUDEndpoint, MetadataMixin):
    """ManagedSwitch Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "managed_switch"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize ManagedSwitch endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        switch_id: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve switch_controller/managed_switch configuration.

        Configure FortiSwitch devices that are managed by this FortiGate.

        Args:
            switch_id: String identifier to retrieve specific object.
                If None, returns all objects.
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
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
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
            >>> # Get all switch_controller/managed_switch objects
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific switch_controller/managed_switch by switch-id
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get(switch_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.switch_controller_managed_switch.get_schema()

        See Also:
            - post(): Create new switch_controller/managed_switch object
            - put(): Update existing switch_controller/managed_switch object
            - delete(): Remove switch_controller/managed_switch object
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
        
        if switch_id:
            endpoint = "/switch-controller/managed-switch/" + str(switch_id)
        else:
            endpoint = "/switch-controller/managed-switch"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json, response_mode=response_mode
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
            >>> schema = fgt.api.cmdb.switch_controller_managed_switch.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.switch_controller_managed_switch.get_schema(format="json-schema")
        
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
        switch_id: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = None,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = None,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = None,
        poe_detection_type: int | None = None,
        max_poe_budget: int | None = None,
        directly_connected: int | None = None,
        version: int | None = None,
        max_allowed_trunk_members: int | None = None,
        pre_provisioned: int | None = None,
        l3_discovered: int | None = None,
        mgmt_mode: int | None = None,
        tunnel_discovered: int | None = None,
        tdr_supported: str | None = None,
        dynamic_capability: str | None = None,
        switch_device_tag: str | None = None,
        switch_dhcp_opt43_key: str | None = None,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: Literal["disable", "enable"] | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: Literal["disable", "enable"] | None = None,
        radius_nas_ip: str | None = None,
        route_offload: Literal["disable", "enable"] | None = None,
        route_offload_mclag: Literal["disable", "enable"] | None = None,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = None,
        vlan: str | list[str] | list[dict[str, Any]] | None = None,
        type: Literal["virtual", "physical"] | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: Literal["enable", "disable"] | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        ports: str | list[str] | list[dict[str, Any]] | None = None,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = None,
        stp_settings: str | None = None,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = None,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = None,
        snmp_sysinfo: str | None = None,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = None,
        snmp_trap_threshold: str | None = None,
        override_snmp_community: Literal["enable", "disable"] | None = None,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = None,
        override_snmp_user: Literal["enable", "disable"] | None = None,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = None,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = None,
        qos_red_probability: int | None = None,
        switch_log: str | None = None,
        remote_log: str | list[str] | list[dict[str, Any]] | None = None,
        storm_control: str | None = None,
        mirror: str | list[str] | list[dict[str, Any]] | None = None,
        static_mac: str | list[str] | list[dict[str, Any]] | None = None,
        custom_command: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = None,
        igmp_snooping: str | None = None,
        x802_1X_settings: str | None = None,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = None,
        system_interface: str | list[str] | list[dict[str, Any]] | None = None,
        router_static: str | list[str] | list[dict[str, Any]] | None = None,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing switch_controller/managed_switch object.

        Configure FortiSwitch devices that are managed by this FortiGate.

        Args:
            payload_dict: Object data as dict. Must include switch-id (primary key).
            switch_id: Managed-switch name.
            sn: Managed-switch serial number.
            description: Description.
            switch_profile: FortiSwitch profile.
            access_profile: FortiSwitch access profile.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If switch-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.put(
            ...     switch_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "switch-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            switch_id=switch_id,
            sn=sn,
            description=description,
            switch_profile=switch_profile,
            access_profile=access_profile,
            purdue_level=purdue_level,
            fsw_wan1_peer=fsw_wan1_peer,
            fsw_wan1_admin=fsw_wan1_admin,
            poe_pre_standard_detection=poe_pre_standard_detection,
            dhcp_server_access_list=dhcp_server_access_list,
            poe_detection_type=poe_detection_type,
            max_poe_budget=max_poe_budget,
            directly_connected=directly_connected,
            version=version,
            max_allowed_trunk_members=max_allowed_trunk_members,
            pre_provisioned=pre_provisioned,
            l3_discovered=l3_discovered,
            mgmt_mode=mgmt_mode,
            tunnel_discovered=tunnel_discovered,
            tdr_supported=tdr_supported,
            dynamic_capability=dynamic_capability,
            switch_device_tag=switch_device_tag,
            switch_dhcp_opt43_key=switch_dhcp_opt43_key,
            mclag_igmp_snooping_aware=mclag_igmp_snooping_aware,
            dynamically_discovered=dynamically_discovered,
            ptp_status=ptp_status,
            ptp_profile=ptp_profile,
            radius_nas_ip_override=radius_nas_ip_override,
            radius_nas_ip=radius_nas_ip,
            route_offload=route_offload,
            route_offload_mclag=route_offload_mclag,
            route_offload_router=route_offload_router,
            vlan=vlan,
            type=type,
            owner_vdom=owner_vdom,
            flow_identity=flow_identity,
            staged_image_version=staged_image_version,
            delayed_restart_trigger=delayed_restart_trigger,
            firmware_provision=firmware_provision,
            firmware_provision_version=firmware_provision_version,
            firmware_provision_latest=firmware_provision_latest,
            ports=ports,
            ip_source_guard=ip_source_guard,
            stp_settings=stp_settings,
            stp_instance=stp_instance,
            override_snmp_sysinfo=override_snmp_sysinfo,
            snmp_sysinfo=snmp_sysinfo,
            override_snmp_trap_threshold=override_snmp_trap_threshold,
            snmp_trap_threshold=snmp_trap_threshold,
            override_snmp_community=override_snmp_community,
            snmp_community=snmp_community,
            override_snmp_user=override_snmp_user,
            snmp_user=snmp_user,
            qos_drop_policy=qos_drop_policy,
            qos_red_probability=qos_red_probability,
            switch_log=switch_log,
            remote_log=remote_log,
            storm_control=storm_control,
            mirror=mirror,
            static_mac=static_mac,
            custom_command=custom_command,
            dhcp_snooping_static_client=dhcp_snooping_static_client,
            igmp_snooping=igmp_snooping,
            x802_1X_settings=x802_1X_settings,
            router_vrf=router_vrf,
            system_interface=system_interface,
            router_static=router_static,
            system_dhcp_server=system_dhcp_server,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.managed_switch import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/managed_switch",
            )
        
        switch_id_value = payload_data.get("switch-id")
        if not switch_id_value:
            raise ValueError("switch-id is required for PUT")
        endpoint = "/switch-controller/managed-switch/" + str(switch_id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
        )

    # ========================================================================
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        switch_id: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = None,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = None,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = None,
        poe_detection_type: int | None = None,
        max_poe_budget: int | None = None,
        directly_connected: int | None = None,
        version: int | None = None,
        max_allowed_trunk_members: int | None = None,
        pre_provisioned: int | None = None,
        l3_discovered: int | None = None,
        mgmt_mode: int | None = None,
        tunnel_discovered: int | None = None,
        tdr_supported: str | None = None,
        dynamic_capability: str | None = None,
        switch_device_tag: str | None = None,
        switch_dhcp_opt43_key: str | None = None,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: Literal["disable", "enable"] | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: Literal["disable", "enable"] | None = None,
        radius_nas_ip: str | None = None,
        route_offload: Literal["disable", "enable"] | None = None,
        route_offload_mclag: Literal["disable", "enable"] | None = None,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = None,
        vlan: str | list[str] | list[dict[str, Any]] | None = None,
        type: Literal["virtual", "physical"] | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: Literal["enable", "disable"] | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        ports: str | list[str] | list[dict[str, Any]] | None = None,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = None,
        stp_settings: str | None = None,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = None,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = None,
        snmp_sysinfo: str | None = None,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = None,
        snmp_trap_threshold: str | None = None,
        override_snmp_community: Literal["enable", "disable"] | None = None,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = None,
        override_snmp_user: Literal["enable", "disable"] | None = None,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = None,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = None,
        qos_red_probability: int | None = None,
        switch_log: str | None = None,
        remote_log: str | list[str] | list[dict[str, Any]] | None = None,
        storm_control: str | None = None,
        mirror: str | list[str] | list[dict[str, Any]] | None = None,
        static_mac: str | list[str] | list[dict[str, Any]] | None = None,
        custom_command: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = None,
        igmp_snooping: str | None = None,
        x802_1X_settings: str | None = None,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = None,
        system_interface: str | list[str] | list[dict[str, Any]] | None = None,
        router_static: str | list[str] | list[dict[str, Any]] | None = None,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Create new switch_controller/managed_switch object.

        Configure FortiSwitch devices that are managed by this FortiGate.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            switch_id: Managed-switch name.
            sn: Managed-switch serial number.
            description: Description.
            switch_profile: FortiSwitch profile.
            access_profile: FortiSwitch access profile.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned switch-id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created switch-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ManagedSwitch.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ManagedSwitch.required_fields()) }}
            
            Use ManagedSwitch.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            switch_id=switch_id,
            sn=sn,
            description=description,
            switch_profile=switch_profile,
            access_profile=access_profile,
            purdue_level=purdue_level,
            fsw_wan1_peer=fsw_wan1_peer,
            fsw_wan1_admin=fsw_wan1_admin,
            poe_pre_standard_detection=poe_pre_standard_detection,
            dhcp_server_access_list=dhcp_server_access_list,
            poe_detection_type=poe_detection_type,
            max_poe_budget=max_poe_budget,
            directly_connected=directly_connected,
            version=version,
            max_allowed_trunk_members=max_allowed_trunk_members,
            pre_provisioned=pre_provisioned,
            l3_discovered=l3_discovered,
            mgmt_mode=mgmt_mode,
            tunnel_discovered=tunnel_discovered,
            tdr_supported=tdr_supported,
            dynamic_capability=dynamic_capability,
            switch_device_tag=switch_device_tag,
            switch_dhcp_opt43_key=switch_dhcp_opt43_key,
            mclag_igmp_snooping_aware=mclag_igmp_snooping_aware,
            dynamically_discovered=dynamically_discovered,
            ptp_status=ptp_status,
            ptp_profile=ptp_profile,
            radius_nas_ip_override=radius_nas_ip_override,
            radius_nas_ip=radius_nas_ip,
            route_offload=route_offload,
            route_offload_mclag=route_offload_mclag,
            route_offload_router=route_offload_router,
            vlan=vlan,
            type=type,
            owner_vdom=owner_vdom,
            flow_identity=flow_identity,
            staged_image_version=staged_image_version,
            delayed_restart_trigger=delayed_restart_trigger,
            firmware_provision=firmware_provision,
            firmware_provision_version=firmware_provision_version,
            firmware_provision_latest=firmware_provision_latest,
            ports=ports,
            ip_source_guard=ip_source_guard,
            stp_settings=stp_settings,
            stp_instance=stp_instance,
            override_snmp_sysinfo=override_snmp_sysinfo,
            snmp_sysinfo=snmp_sysinfo,
            override_snmp_trap_threshold=override_snmp_trap_threshold,
            snmp_trap_threshold=snmp_trap_threshold,
            override_snmp_community=override_snmp_community,
            snmp_community=snmp_community,
            override_snmp_user=override_snmp_user,
            snmp_user=snmp_user,
            qos_drop_policy=qos_drop_policy,
            qos_red_probability=qos_red_probability,
            switch_log=switch_log,
            remote_log=remote_log,
            storm_control=storm_control,
            mirror=mirror,
            static_mac=static_mac,
            custom_command=custom_command,
            dhcp_snooping_static_client=dhcp_snooping_static_client,
            igmp_snooping=igmp_snooping,
            x802_1X_settings=x802_1X_settings,
            router_vrf=router_vrf,
            system_interface=system_interface,
            router_static=router_static,
            system_dhcp_server=system_dhcp_server,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.managed_switch import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/managed_switch",
            )

        endpoint = "/switch-controller/managed-switch"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        switch_id: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Delete switch_controller/managed_switch object.

        Configure FortiSwitch devices that are managed by this FortiGate.

        Args:
            switch_id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If switch-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.delete(switch_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not switch_id:
            raise ValueError("switch-id is required for DELETE")
        endpoint = "/switch-controller/managed-switch/" + str(switch_id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
        )

    def exists(
        self,
        switch_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if switch_controller/managed_switch object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            switch_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.switch_controller_managed_switch.exists(switch_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.switch_controller_managed_switch.exists(switch_id=1):
            ...     fgt.api.cmdb.switch_controller_managed_switch.delete(switch_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                switch_id=switch_id,
                vdom=vdom,
                raw_json=True
            )
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        switch_id: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = None,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = None,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = None,
        poe_detection_type: int | None = None,
        max_poe_budget: int | None = None,
        directly_connected: int | None = None,
        version: int | None = None,
        max_allowed_trunk_members: int | None = None,
        pre_provisioned: int | None = None,
        l3_discovered: int | None = None,
        mgmt_mode: int | None = None,
        tunnel_discovered: int | None = None,
        tdr_supported: str | None = None,
        dynamic_capability: str | None = None,
        switch_device_tag: str | None = None,
        switch_dhcp_opt43_key: str | None = None,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: Literal["disable", "enable"] | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: Literal["disable", "enable"] | None = None,
        radius_nas_ip: str | None = None,
        route_offload: Literal["disable", "enable"] | None = None,
        route_offload_mclag: Literal["disable", "enable"] | None = None,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = None,
        vlan: str | list[str] | list[dict[str, Any]] | None = None,
        type: Literal["virtual", "physical"] | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: Literal["enable", "disable"] | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        ports: str | list[str] | list[dict[str, Any]] | None = None,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = None,
        stp_settings: str | None = None,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = None,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = None,
        snmp_sysinfo: str | None = None,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = None,
        snmp_trap_threshold: str | None = None,
        override_snmp_community: Literal["enable", "disable"] | None = None,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = None,
        override_snmp_user: Literal["enable", "disable"] | None = None,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = None,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = None,
        qos_red_probability: int | None = None,
        switch_log: str | None = None,
        remote_log: str | list[str] | list[dict[str, Any]] | None = None,
        storm_control: str | None = None,
        mirror: str | list[str] | list[dict[str, Any]] | None = None,
        static_mac: str | list[str] | list[dict[str, Any]] | None = None,
        custom_command: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = None,
        igmp_snooping: str | None = None,
        x802_1X_settings: str | None = None,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = None,
        system_interface: str | list[str] | list[dict[str, Any]] | None = None,
        router_static: str | list[str] | list[dict[str, Any]] | None = None,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update switch_controller/managed_switch object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (switch-id) in the payload.

        Args:
            payload_dict: Resource data including switch-id (primary key)
            switch_id: Field switch-id
            sn: Field sn
            description: Field description
            switch_profile: Field switch-profile
            access_profile: Field access-profile
            purdue_level: Field purdue-level
            fsw_wan1_peer: Field fsw-wan1-peer
            fsw_wan1_admin: Field fsw-wan1-admin
            poe_pre_standard_detection: Field poe-pre-standard-detection
            dhcp_server_access_list: Field dhcp-server-access-list
            poe_detection_type: Field poe-detection-type
            max_poe_budget: Field max-poe-budget
            directly_connected: Field directly-connected
            version: Field version
            max_allowed_trunk_members: Field max-allowed-trunk-members
            pre_provisioned: Field pre-provisioned
            l3_discovered: Field l3-discovered
            mgmt_mode: Field mgmt-mode
            tunnel_discovered: Field tunnel-discovered
            tdr_supported: Field tdr-supported
            dynamic_capability: Field dynamic-capability
            switch_device_tag: Field switch-device-tag
            switch_dhcp_opt43_key: Field switch-dhcp_opt43_key
            mclag_igmp_snooping_aware: Field mclag-igmp-snooping-aware
            dynamically_discovered: Field dynamically-discovered
            ptp_status: Field ptp-status
            ptp_profile: Field ptp-profile
            radius_nas_ip_override: Field radius-nas-ip-override
            radius_nas_ip: Field radius-nas-ip
            route_offload: Field route-offload
            route_offload_mclag: Field route-offload-mclag
            route_offload_router: Field route-offload-router
            vlan: Field vlan
            type: Field type
            owner_vdom: Field owner-vdom
            flow_identity: Field flow-identity
            staged_image_version: Field staged-image-version
            delayed_restart_trigger: Field delayed-restart-trigger
            firmware_provision: Field firmware-provision
            firmware_provision_version: Field firmware-provision-version
            firmware_provision_latest: Field firmware-provision-latest
            ports: Field ports
            ip_source_guard: Field ip-source-guard
            stp_settings: Field stp-settings
            stp_instance: Field stp-instance
            override_snmp_sysinfo: Field override-snmp-sysinfo
            snmp_sysinfo: Field snmp-sysinfo
            override_snmp_trap_threshold: Field override-snmp-trap-threshold
            snmp_trap_threshold: Field snmp-trap-threshold
            override_snmp_community: Field override-snmp-community
            snmp_community: Field snmp-community
            override_snmp_user: Field override-snmp-user
            snmp_user: Field snmp-user
            qos_drop_policy: Field qos-drop-policy
            qos_red_probability: Field qos-red-probability
            switch_log: Field switch-log
            remote_log: Field remote-log
            storm_control: Field storm-control
            mirror: Field mirror
            static_mac: Field static-mac
            custom_command: Field custom-command
            dhcp_snooping_static_client: Field dhcp-snooping-static-client
            igmp_snooping: Field igmp-snooping
            x802_1X_settings: Field 802-1X-settings
            router_vrf: Field router-vrf
            system_interface: Field system-interface
            router_static: Field router-static
            system_dhcp_server: Field system-dhcp-server
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            response_mode: Override client-level response_mode
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If switch-id is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.set(
            ...     switch_id=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "switch-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.switch_controller_managed_switch.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        # Build payload using helper function with auto-normalization
        payload_data = build_api_payload(
            switch_id=switch_id,
            sn=sn,
            description=description,
            switch_profile=switch_profile,
            access_profile=access_profile,
            purdue_level=purdue_level,
            fsw_wan1_peer=fsw_wan1_peer,
            fsw_wan1_admin=fsw_wan1_admin,
            poe_pre_standard_detection=poe_pre_standard_detection,
            dhcp_server_access_list=dhcp_server_access_list,
            poe_detection_type=poe_detection_type,
            max_poe_budget=max_poe_budget,
            directly_connected=directly_connected,
            version=version,
            max_allowed_trunk_members=max_allowed_trunk_members,
            pre_provisioned=pre_provisioned,
            l3_discovered=l3_discovered,
            mgmt_mode=mgmt_mode,
            tunnel_discovered=tunnel_discovered,
            tdr_supported=tdr_supported,
            dynamic_capability=dynamic_capability,
            switch_device_tag=switch_device_tag,
            switch_dhcp_opt43_key=switch_dhcp_opt43_key,
            mclag_igmp_snooping_aware=mclag_igmp_snooping_aware,
            dynamically_discovered=dynamically_discovered,
            ptp_status=ptp_status,
            ptp_profile=ptp_profile,
            radius_nas_ip_override=radius_nas_ip_override,
            radius_nas_ip=radius_nas_ip,
            route_offload=route_offload,
            route_offload_mclag=route_offload_mclag,
            route_offload_router=route_offload_router,
            vlan=vlan,
            type=type,
            owner_vdom=owner_vdom,
            flow_identity=flow_identity,
            staged_image_version=staged_image_version,
            delayed_restart_trigger=delayed_restart_trigger,
            firmware_provision=firmware_provision,
            firmware_provision_version=firmware_provision_version,
            firmware_provision_latest=firmware_provision_latest,
            ports=ports,
            ip_source_guard=ip_source_guard,
            stp_settings=stp_settings,
            stp_instance=stp_instance,
            override_snmp_sysinfo=override_snmp_sysinfo,
            snmp_sysinfo=snmp_sysinfo,
            override_snmp_trap_threshold=override_snmp_trap_threshold,
            snmp_trap_threshold=snmp_trap_threshold,
            override_snmp_community=override_snmp_community,
            snmp_community=snmp_community,
            override_snmp_user=override_snmp_user,
            snmp_user=snmp_user,
            qos_drop_policy=qos_drop_policy,
            qos_red_probability=qos_red_probability,
            switch_log=switch_log,
            remote_log=remote_log,
            storm_control=storm_control,
            mirror=mirror,
            static_mac=static_mac,
            custom_command=custom_command,
            dhcp_snooping_static_client=dhcp_snooping_static_client,
            igmp_snooping=igmp_snooping,
            x802_1X_settings=x802_1X_settings,
            router_vrf=router_vrf,
            system_interface=system_interface,
            router_static=router_static,
            system_dhcp_server=system_dhcp_server,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("switch-id")
        if not mkey_value:
            raise ValueError("switch-id is required for set()")
        
        # Check if resource exists
        if self.exists(switch_id=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_data, vdom=vdom, raw_json=raw_json, response_mode=response_mode, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_data, vdom=vdom, raw_json=raw_json, response_mode=response_mode, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        switch_id: str,
        action: Literal["before", "after"],
        reference_switch_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move switch_controller/managed_switch object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            switch_id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_switch_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.switch_controller_managed_switch.move(
            ...     switch_id=100,
            ...     action="before",
            ...     reference_switch_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/switch-controller/managed-switch",
            params={
                "switch-id": switch_id,
                "action": "move",
                action: reference_switch_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        switch_id: str,
        new_switch_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone switch_controller/managed_switch object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            switch_id: Identifier of object to clone
            new_switch_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.switch_controller_managed_switch.clone(
            ...     switch_id=1,
            ...     new_switch_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/switch-controller/managed-switch",
            params={
                "switch-id": switch_id,
                "new_switch-id": new_switch_id,
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
        switch_id: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if switch_controller/managed_switch object exists.
        
        Args:
            switch_id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.switch_controller_managed_switch.exists(switch_id=1):
            ...     fgt.api.cmdb.switch_controller_managed_switch.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                switch_id=switch_id,
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

