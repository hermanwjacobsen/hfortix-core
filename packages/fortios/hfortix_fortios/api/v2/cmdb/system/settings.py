"""
FortiOS CMDB - System settings

Configuration endpoint for managing cmdb system/settings objects.

API Endpoints:
    GET    /cmdb/system/settings
    POST   /cmdb/system/settings
    PUT    /cmdb/system/settings/{identifier}
    DELETE /cmdb/system/settings/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_settings.get()

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


class Settings:
    """Settings Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Settings endpoint."""
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
        Retrieve system/settings configuration.

        Configure VDOM settings.

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
            >>> # Get all system/settings objects
            >>> result = fgt.api.cmdb.system_settings.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_settings.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_settings.get(action="schema")

        See Also:
            - post(): Create new system/settings object
            - put(): Update existing system/settings object
            - delete(): Remove system/settings object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/settings/{name}"
        else:
            endpoint = "/system/settings"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        comments: str | None = None,
        vdom_type: str | None = None,
        lan_extension_controller_addr: str | None = None,
        lan_extension_controller_port: int | None = None,
        opmode: str | None = None,
        ngfw_mode: str | None = None,
        http_external_dest: str | None = None,
        firewall_session_dirty: str | None = None,
        manageip: str | None = None,
        gateway: str | None = None,
        ip: Any | None = None,
        manageip6: str | None = None,
        gateway6: str | None = None,
        ip6: str | None = None,
        device: str | None = None,
        bfd: str | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_required_min_rx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_dont_enforce_src_port: str | None = None,
        utf8_spam_tagging: str | None = None,
        wccp_cache_engine: str | None = None,
        vpn_stats_log: str | list | None = None,
        vpn_stats_period: int | None = None,
        v4_ecmp_mode: str | None = None,
        mac_ttl: int | None = None,
        fw_session_hairpin: str | None = None,
        prp_trailer_action: str | None = None,
        snat_hairpin_traffic: str | None = None,
        dhcp_proxy: str | None = None,
        dhcp_proxy_interface_select_method: str | None = None,
        dhcp_proxy_interface: str | None = None,
        dhcp_proxy_vrf_select: int | None = None,
        dhcp_server_ip: str | list | None = None,
        dhcp6_server_ip: str | list | None = None,
        central_nat: str | None = None,
        gui_default_policy_columns: str | list | None = None,
        lldp_reception: str | None = None,
        lldp_transmission: str | None = None,
        link_down_access: str | None = None,
        nat46_generate_ipv6_fragment_header: str | None = None,
        nat46_force_ipv4_packet_forwarding: str | None = None,
        nat64_force_ipv6_packet_forwarding: str | None = None,
        detect_unknown_esp: str | None = None,
        intree_ses_best_route: str | None = None,
        auxiliary_session: str | None = None,
        asymroute: str | None = None,
        asymroute_icmp: str | None = None,
        tcp_session_without_syn: str | None = None,
        ses_denied_traffic: str | None = None,
        ses_denied_multicast_traffic: str | None = None,
        strict_src_check: str | None = None,
        allow_linkdown_path: str | None = None,
        asymroute6: str | None = None,
        asymroute6_icmp: str | None = None,
        sctp_session_without_init: str | None = None,
        sip_expectation: str | None = None,
        sip_nat_trace: str | None = None,
        h323_direct_model: str | None = None,
        status: str | None = None,
        sip_tcp_port: int | list | None = None,
        sip_udp_port: int | list | None = None,
        sip_ssl_port: int | None = None,
        sccp_port: int | None = None,
        multicast_forward: str | None = None,
        multicast_ttl_notchange: str | None = None,
        multicast_skip_policy: str | None = None,
        allow_subnet_overlap: str | None = None,
        deny_tcp_with_icmp: str | None = None,
        ecmp_max_paths: int | None = None,
        discovered_device_timeout: int | None = None,
        email_portal_check_dns: str | None = None,
        default_voip_alg_mode: str | None = None,
        gui_icap: str | None = None,
        gui_implicit_policy: str | None = None,
        gui_dns_database: str | None = None,
        gui_load_balance: str | None = None,
        gui_multicast_policy: str | None = None,
        gui_dos_policy: str | None = None,
        gui_object_colors: str | None = None,
        gui_route_tag_address_creation: str | None = None,
        gui_voip_profile: str | None = None,
        gui_ap_profile: str | None = None,
        gui_security_profile_group: str | None = None,
        gui_local_in_policy: str | None = None,
        gui_wanopt_cache: str | None = None,
        gui_explicit_proxy: str | None = None,
        gui_dynamic_routing: str | None = None,
        gui_sslvpn_personal_bookmarks: str | None = None,
        gui_sslvpn_realms: str | None = None,
        gui_policy_based_ipsec: str | None = None,
        gui_threat_weight: str | None = None,
        gui_spamfilter: str | None = None,
        gui_file_filter: str | None = None,
        gui_application_control: str | None = None,
        gui_ips: str | None = None,
        gui_dhcp_advanced: str | None = None,
        gui_vpn: str | None = None,
        gui_sslvpn: str | None = None,
        gui_wireless_controller: str | None = None,
        gui_advanced_wireless_features: str | None = None,
        gui_switch_controller: str | None = None,
        gui_fortiap_split_tunneling: str | None = None,
        gui_webfilter_advanced: str | None = None,
        gui_traffic_shaping: str | None = None,
        gui_wan_load_balancing: str | None = None,
        gui_antivirus: str | None = None,
        gui_webfilter: str | None = None,
        gui_videofilter: str | None = None,
        gui_dnsfilter: str | None = None,
        gui_waf_profile: str | None = None,
        gui_dlp_profile: str | None = None,
        gui_dlp_advanced: str | None = None,
        gui_virtual_patch_profile: str | None = None,
        gui_casb: str | None = None,
        gui_fortiextender_controller: str | None = None,
        gui_advanced_policy: str | None = None,
        gui_allow_unnamed_policy: str | None = None,
        gui_email_collection: str | None = None,
        gui_multiple_interface_policy: str | None = None,
        gui_policy_disclaimer: str | None = None,
        gui_ztna: str | None = None,
        gui_ot: str | None = None,
        gui_dynamic_device_os_id: str | None = None,
        gui_gtp: str | None = None,
        location_id: str | None = None,
        ike_session_resume: str | None = None,
        ike_quick_crash_detect: str | None = None,
        ike_dn_format: str | None = None,
        ike_port: int | None = None,
        ike_tcp_port: int | None = None,
        ike_policy_route: str | None = None,
        ike_detailed_event_logs: str | None = None,
        block_land_attack: str | None = None,
        default_app_port_as_service: str | None = None,
        fqdn_session_check: str | None = None,
        ext_resource_session_check: str | None = None,
        dyn_addr_session_check: str | None = None,
        default_policy_expiry_days: int | None = None,
        gui_enforce_change_summary: str | None = None,
        internet_service_database_cache: str | None = None,
        internet_service_app_ctrl_size: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/settings object.

        Configure VDOM settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            comments: VDOM comments.
            vdom_type: Vdom type (traffic, lan-extension or admin).
            lan_extension_controller_addr: Controller IP address or FQDN to connect.
            lan_extension_controller_port: Controller port to connect.
            opmode: Firewall operation mode (NAT or Transparent).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_settings.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_settings.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            comments=comments,
            vdom_type=vdom_type,
            lan_extension_controller_addr=lan_extension_controller_addr,
            lan_extension_controller_port=lan_extension_controller_port,
            opmode=opmode,
            ngfw_mode=ngfw_mode,
            http_external_dest=http_external_dest,
            firewall_session_dirty=firewall_session_dirty,
            manageip=manageip,
            gateway=gateway,
            ip=ip,
            manageip6=manageip6,
            gateway6=gateway6,
            ip6=ip6,
            device=device,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_required_min_rx=bfd_required_min_rx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_dont_enforce_src_port=bfd_dont_enforce_src_port,
            utf8_spam_tagging=utf8_spam_tagging,
            wccp_cache_engine=wccp_cache_engine,
            vpn_stats_log=vpn_stats_log,
            vpn_stats_period=vpn_stats_period,
            v4_ecmp_mode=v4_ecmp_mode,
            mac_ttl=mac_ttl,
            fw_session_hairpin=fw_session_hairpin,
            prp_trailer_action=prp_trailer_action,
            snat_hairpin_traffic=snat_hairpin_traffic,
            dhcp_proxy=dhcp_proxy,
            dhcp_proxy_interface_select_method=dhcp_proxy_interface_select_method,
            dhcp_proxy_interface=dhcp_proxy_interface,
            dhcp_proxy_vrf_select=dhcp_proxy_vrf_select,
            dhcp_server_ip=dhcp_server_ip,
            dhcp6_server_ip=dhcp6_server_ip,
            central_nat=central_nat,
            gui_default_policy_columns=gui_default_policy_columns,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            link_down_access=link_down_access,
            nat46_generate_ipv6_fragment_header=nat46_generate_ipv6_fragment_header,
            nat46_force_ipv4_packet_forwarding=nat46_force_ipv4_packet_forwarding,
            nat64_force_ipv6_packet_forwarding=nat64_force_ipv6_packet_forwarding,
            detect_unknown_esp=detect_unknown_esp,
            intree_ses_best_route=intree_ses_best_route,
            auxiliary_session=auxiliary_session,
            asymroute=asymroute,
            asymroute_icmp=asymroute_icmp,
            tcp_session_without_syn=tcp_session_without_syn,
            ses_denied_traffic=ses_denied_traffic,
            ses_denied_multicast_traffic=ses_denied_multicast_traffic,
            strict_src_check=strict_src_check,
            allow_linkdown_path=allow_linkdown_path,
            asymroute6=asymroute6,
            asymroute6_icmp=asymroute6_icmp,
            sctp_session_without_init=sctp_session_without_init,
            sip_expectation=sip_expectation,
            sip_nat_trace=sip_nat_trace,
            h323_direct_model=h323_direct_model,
            status=status,
            sip_tcp_port=sip_tcp_port,
            sip_udp_port=sip_udp_port,
            sip_ssl_port=sip_ssl_port,
            sccp_port=sccp_port,
            multicast_forward=multicast_forward,
            multicast_ttl_notchange=multicast_ttl_notchange,
            multicast_skip_policy=multicast_skip_policy,
            allow_subnet_overlap=allow_subnet_overlap,
            deny_tcp_with_icmp=deny_tcp_with_icmp,
            ecmp_max_paths=ecmp_max_paths,
            discovered_device_timeout=discovered_device_timeout,
            email_portal_check_dns=email_portal_check_dns,
            default_voip_alg_mode=default_voip_alg_mode,
            gui_icap=gui_icap,
            gui_implicit_policy=gui_implicit_policy,
            gui_dns_database=gui_dns_database,
            gui_load_balance=gui_load_balance,
            gui_multicast_policy=gui_multicast_policy,
            gui_dos_policy=gui_dos_policy,
            gui_object_colors=gui_object_colors,
            gui_route_tag_address_creation=gui_route_tag_address_creation,
            gui_voip_profile=gui_voip_profile,
            gui_ap_profile=gui_ap_profile,
            gui_security_profile_group=gui_security_profile_group,
            gui_local_in_policy=gui_local_in_policy,
            gui_wanopt_cache=gui_wanopt_cache,
            gui_explicit_proxy=gui_explicit_proxy,
            gui_dynamic_routing=gui_dynamic_routing,
            gui_sslvpn_personal_bookmarks=gui_sslvpn_personal_bookmarks,
            gui_sslvpn_realms=gui_sslvpn_realms,
            gui_policy_based_ipsec=gui_policy_based_ipsec,
            gui_threat_weight=gui_threat_weight,
            gui_spamfilter=gui_spamfilter,
            gui_file_filter=gui_file_filter,
            gui_application_control=gui_application_control,
            gui_ips=gui_ips,
            gui_dhcp_advanced=gui_dhcp_advanced,
            gui_vpn=gui_vpn,
            gui_sslvpn=gui_sslvpn,
            gui_wireless_controller=gui_wireless_controller,
            gui_advanced_wireless_features=gui_advanced_wireless_features,
            gui_switch_controller=gui_switch_controller,
            gui_fortiap_split_tunneling=gui_fortiap_split_tunneling,
            gui_webfilter_advanced=gui_webfilter_advanced,
            gui_traffic_shaping=gui_traffic_shaping,
            gui_wan_load_balancing=gui_wan_load_balancing,
            gui_antivirus=gui_antivirus,
            gui_webfilter=gui_webfilter,
            gui_videofilter=gui_videofilter,
            gui_dnsfilter=gui_dnsfilter,
            gui_waf_profile=gui_waf_profile,
            gui_dlp_profile=gui_dlp_profile,
            gui_dlp_advanced=gui_dlp_advanced,
            gui_virtual_patch_profile=gui_virtual_patch_profile,
            gui_casb=gui_casb,
            gui_fortiextender_controller=gui_fortiextender_controller,
            gui_advanced_policy=gui_advanced_policy,
            gui_allow_unnamed_policy=gui_allow_unnamed_policy,
            gui_email_collection=gui_email_collection,
            gui_multiple_interface_policy=gui_multiple_interface_policy,
            gui_policy_disclaimer=gui_policy_disclaimer,
            gui_ztna=gui_ztna,
            gui_ot=gui_ot,
            gui_dynamic_device_os_id=gui_dynamic_device_os_id,
            gui_gtp=gui_gtp,
            location_id=location_id,
            ike_session_resume=ike_session_resume,
            ike_quick_crash_detect=ike_quick_crash_detect,
            ike_dn_format=ike_dn_format,
            ike_port=ike_port,
            ike_tcp_port=ike_tcp_port,
            ike_policy_route=ike_policy_route,
            ike_detailed_event_logs=ike_detailed_event_logs,
            block_land_attack=block_land_attack,
            default_app_port_as_service=default_app_port_as_service,
            fqdn_session_check=fqdn_session_check,
            ext_resource_session_check=ext_resource_session_check,
            dyn_addr_session_check=dyn_addr_session_check,
            default_policy_expiry_days=default_policy_expiry_days,
            gui_enforce_change_summary=gui_enforce_change_summary,
            internet_service_database_cache=internet_service_database_cache,
            internet_service_app_ctrl_size=internet_service_app_ctrl_size,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.settings import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/settings",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/settings/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





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
            >>> print(Settings.help())
            
            >>> # Get field information
            >>> print(Settings.help("comments"))
        """
        from ._helpers.settings import (
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
            >>> fields = Settings.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Settings.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.settings import get_all_fields, get_field_metadata

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
            >>> info = Settings.field_info("comments")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.settings import get_field_metadata

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
            >>> is_valid, error = Settings.validate_field("comments", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.settings import validate_field_value

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
            >>> required = Settings.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.settings import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Settings.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.settings import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Settings.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.settings import get_schema_info

        return get_schema_info()
