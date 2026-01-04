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


class ManagedSwitch:
    """ManagedSwitch Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize ManagedSwitch endpoint."""
        self._client = client

    def get(
        self,
        switch_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve switch_controller/managed_switch configuration.

        Configure FortiSwitch devices that are managed by this FortiGate.

        Args:
            switch_id: String identifier to retrieve specific object.
                If None, returns all objects.
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
            >>> # Get all switch_controller/managed_switch objects
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific switch_controller/managed_switch by switch-id
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get(switch_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_managed_switch.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_managed_switch.get(action="schema")

        See Also:
            - post(): Create new switch_controller/managed_switch object
            - put(): Update existing switch_controller/managed_switch object
            - delete(): Remove switch_controller/managed_switch object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if switch_id:
            endpoint = "/switch-controller/managed-switch/" + str(switch_id)
        else:
            endpoint = "/switch-controller/managed-switch"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        switch_id: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: str | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: str | None = None,
        poe_pre_standard_detection: str | None = None,
        dhcp_server_access_list: str | None = None,
        poe_detection_type: int | None = None,
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
        mclag_igmp_snooping_aware: str | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: str | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: str | None = None,
        radius_nas_ip: str | None = None,
        route_offload: str | None = None,
        route_offload_mclag: str | None = None,
        route_offload_router: str | list | None = None,
        vlan: str | list | None = None,
        type: str | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: str | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: str | None = None,
        ports: str | list | None = None,
        ip_source_guard: str | list | None = None,
        stp_settings: str | None = None,
        stp_instance: str | list | None = None,
        override_snmp_sysinfo: str | None = None,
        snmp_sysinfo: str | None = None,
        override_snmp_trap_threshold: str | None = None,
        snmp_trap_threshold: str | None = None,
        override_snmp_community: str | None = None,
        snmp_community: str | list | None = None,
        override_snmp_user: str | None = None,
        snmp_user: str | list | None = None,
        qos_drop_policy: str | None = None,
        qos_red_probability: int | None = None,
        switch_log: str | None = None,
        remote_log: str | list | None = None,
        storm_control: str | None = None,
        mirror: str | list | None = None,
        static_mac: str | list | None = None,
        custom_command: str | list | None = None,
        dhcp_snooping_static_client: str | list | None = None,
        igmp_snooping: str | None = None,
        x802_1X_settings: str | None = None,
        router_vrf: str | list | None = None,
        system_interface: str | list | None = None,
        router_static: str | list | None = None,
        system_dhcp_server: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
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
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
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
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        switch_id: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: str | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: str | None = None,
        poe_pre_standard_detection: str | None = None,
        dhcp_server_access_list: str | None = None,
        poe_detection_type: int | None = None,
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
        mclag_igmp_snooping_aware: str | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: str | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: str | None = None,
        radius_nas_ip: str | None = None,
        route_offload: str | None = None,
        route_offload_mclag: str | None = None,
        route_offload_router: str | list | None = None,
        vlan: str | list | None = None,
        type: str | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: str | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: str | None = None,
        ports: str | list | None = None,
        ip_source_guard: str | list | None = None,
        stp_settings: str | None = None,
        stp_instance: str | list | None = None,
        override_snmp_sysinfo: str | None = None,
        snmp_sysinfo: str | None = None,
        override_snmp_trap_threshold: str | None = None,
        snmp_trap_threshold: str | None = None,
        override_snmp_community: str | None = None,
        snmp_community: str | list | None = None,
        override_snmp_user: str | None = None,
        snmp_user: str | list | None = None,
        qos_drop_policy: str | None = None,
        qos_red_probability: int | None = None,
        switch_log: str | None = None,
        remote_log: str | list | None = None,
        storm_control: str | None = None,
        mirror: str | list | None = None,
        static_mac: str | list | None = None,
        custom_command: str | list | None = None,
        dhcp_snooping_static_client: str | list | None = None,
        igmp_snooping: str | None = None,
        x802_1X_settings: str | None = None,
        router_vrf: str | list | None = None,
        system_interface: str | list | None = None,
        router_static: str | list | None = None,
        system_dhcp_server: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
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
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
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
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        switch_id: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete switch_controller/managed_switch object.

        Configure FortiSwitch devices that are managed by this FortiGate.

        Args:
            switch_id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
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
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
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
        try:
            response = self.get(switch_id=switch_id, vdom=vdom, raw_json=True)
            
            if isinstance(response, dict):
                # Use helper function to check success
                return is_success(response)
            else:
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception:
            # Resource not found or other error - return False
            return False

    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update switch_controller/managed_switch object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (switch-id) in the payload.

        Args:
            payload_dict: Resource data including switch-id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If switch-id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
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
        if payload_dict is None:
            payload_dict = {}
        
        mkey_value = payload_dict.get("switch-id")
        if not mkey_value:
            raise ValueError("switch-id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(switch_id=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)

    # ========================================================================
    # Metadata Helper Methods
    # Provide easy access to schema metadata without separate imports
    # ========================================================================

    @staticmethod
    def help(field_name: str | None = None) -> str:
        """
        Get help text for endpoint or specific field.

        Args:
            field_name: Optional field name to get help for. If None, shows endpoint help.

        Returns:
            Formatted help text

        Examples:
            >>> # Get endpoint information
            >>> print(ManagedSwitch.help())
            
            >>> # Get field information
            >>> print(ManagedSwitch.help("switch-id"))
        """
        from ._helpers.managed_switch import (
            get_schema_info,
            get_field_metadata,
        )

        if field_name is None:
            # Endpoint help
            info = get_schema_info()
            lines = [
                f"Endpoint: {info['endpoint']}",
                f"Category: {info['category']}",
                f"Help: {info.get('help', 'N/A')}",
                "",
                f"Total Fields: {info['total_fields']}",
                f"Required Fields: {info['required_fields_count']}",
                f"Fields with Defaults: {info['fields_with_defaults_count']}",
            ]
            if 'mkey' in info:
                lines.append(f"\nPrimary Key: {info['mkey']} ({info['mkey_type']})")
            return "\n".join(lines)
        
        # Field help
        meta = get_field_metadata(field_name)
        if meta is None:
            return f"Unknown field: {field_name}"

        lines = [
            f"Field: {meta['name']}",
            f"Type: {meta['type']}",
        ]
        if 'description' in meta:
            lines.append(f"Description: {meta['description']}")
        lines.append(f"Required: {'Yes' if meta.get('required', False) else 'No'}")
        if 'default' in meta:
            lines.append(f"Default: {meta['default']}")
        if 'options' in meta:
            lines.append(f"Options: {', '.join(meta['options'])}")
        if 'constraints' in meta:
            constraints = meta['constraints']
            if 'min' in constraints or 'max' in constraints:
                min_val = constraints.get('min', '?')
                max_val = constraints.get('max', '?')
                lines.append(f"Range: {min_val} - {max_val}")
            if 'max_length' in constraints:
                lines.append(f"Max Length: {constraints['max_length']}")

        return "\n".join(lines)

    @staticmethod
    def fields(detailed: bool = False) -> Union[list[str], dict[str, dict]]:
        """
        Get list of all field names or detailed field information.

        Args:
            detailed: If True, return dict with field metadata

        Returns:
            List of field names or dict of field metadata

        Examples:
            >>> # Simple list
            >>> fields = ManagedSwitch.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = ManagedSwitch.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.managed_switch import get_all_fields, get_field_metadata

        field_names = get_all_fields()

        if not detailed:
            return field_names

        # Build detailed dict
        detailed_fields = {}
        for fname in field_names:
            meta = get_field_metadata(fname)
            if meta:
                detailed_fields[fname] = meta

        return detailed_fields

    @staticmethod
    def field_info(field_name: str) -> dict[str, Any] | None:
        """
        Get complete metadata for a specific field.

        Args:
            field_name: Name of the field

        Returns:
            Field metadata dict or None if field doesn't exist

        Examples:
            >>> info = ManagedSwitch.field_info("switch-id")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.managed_switch import get_field_metadata

        return get_field_metadata(field_name)

    @staticmethod
    def validate_field(field_name: str, value: Any) -> tuple[bool, str | None]:
        """
        Validate a field value against its constraints.

        Args:
            field_name: Name of the field
            value: Value to validate

        Returns:
            Tuple of (is_valid, error_message)

        Examples:
            >>> is_valid, error = ManagedSwitch.validate_field("switch-id", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.managed_switch import validate_field_value

        return validate_field_value(field_name, value)

    @staticmethod
    def required_fields() -> list[str]:
        """
        Get list of required field names.

        Note: Due to FortiOS schema quirks, some fields may be conditionally required.
        Always test with the actual API for authoritative requirements.

        Returns:
            List of required field names

        Examples:
            >>> required = ManagedSwitch.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.managed_switch import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = ManagedSwitch.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.managed_switch import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = ManagedSwitch.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.managed_switch import get_schema_info

        return get_schema_info()
