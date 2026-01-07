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


class Settings(MetadataMixin):
    """Settings Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "settings"
    
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
        """Initialize Settings endpoint."""
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
        Retrieve system/settings configuration.

        Configure VDOM settings.

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
            >>> # Get all system/settings objects
            >>> result = fgt.api.cmdb.system_settings.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_settings.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_settings.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_settings.get_schema()

        See Also:
            - post(): Create new system/settings object
            - put(): Update existing system/settings object
            - delete(): Remove system/settings object
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
            endpoint = f"/system/settings/{name}"
        else:
            endpoint = "/system/settings"
        
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
            >>> schema = fgt.api.cmdb.system_settings.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_settings.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        comments: str | None = None,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = None,
        lan_extension_controller_addr: str | None = None,
        lan_extension_controller_port: int | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = None,
        http_external_dest: Literal["fortiweb", "forticache"] | None = None,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = None,
        manageip: str | None = None,
        gateway: str | None = None,
        ip: Any | None = None,
        manageip6: str | None = None,
        gateway6: str | None = None,
        ip6: str | None = None,
        device: str | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_required_min_rx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = None,
        utf8_spam_tagging: Literal["enable", "disable"] | None = None,
        wccp_cache_engine: Literal["enable", "disable"] | None = None,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list | None = None,
        vpn_stats_period: int | None = None,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = None,
        mac_ttl: int | None = None,
        fw_session_hairpin: Literal["enable", "disable"] | None = None,
        prp_trailer_action: Literal["enable", "disable"] | None = None,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = None,
        dhcp_proxy: Literal["enable", "disable"] | None = None,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_proxy_interface: str | None = None,
        dhcp_proxy_vrf_select: int | None = None,
        dhcp_server_ip: str | list | None = None,
        dhcp6_server_ip: str | list | None = None,
        central_nat: Literal["enable", "disable"] | None = None,
        gui_default_policy_columns: str | list | None = None,
        lldp_reception: Literal["enable", "disable", "global"] | None = None,
        lldp_transmission: Literal["enable", "disable", "global"] | None = None,
        link_down_access: Literal["enable", "disable"] | None = None,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = None,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = None,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = None,
        detect_unknown_esp: Literal["enable", "disable"] | None = None,
        intree_ses_best_route: Literal["force", "disable"] | None = None,
        auxiliary_session: Literal["enable", "disable"] | None = None,
        asymroute: Literal["enable", "disable"] | None = None,
        asymroute_icmp: Literal["enable", "disable"] | None = None,
        tcp_session_without_syn: Literal["enable", "disable"] | None = None,
        ses_denied_traffic: Literal["enable", "disable"] | None = None,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = None,
        strict_src_check: Literal["enable", "disable"] | None = None,
        allow_linkdown_path: Literal["enable", "disable"] | None = None,
        asymroute6: Literal["enable", "disable"] | None = None,
        asymroute6_icmp: Literal["enable", "disable"] | None = None,
        sctp_session_without_init: Literal["enable", "disable"] | None = None,
        sip_expectation: Literal["enable", "disable"] | None = None,
        sip_nat_trace: Literal["enable", "disable"] | None = None,
        h323_direct_model: Literal["disable", "enable"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        sip_tcp_port: int | list | None = None,
        sip_udp_port: int | list | None = None,
        sip_ssl_port: int | None = None,
        sccp_port: int | None = None,
        multicast_forward: Literal["enable", "disable"] | None = None,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = None,
        multicast_skip_policy: Literal["enable", "disable"] | None = None,
        allow_subnet_overlap: Literal["enable", "disable"] | None = None,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = None,
        ecmp_max_paths: int | None = None,
        discovered_device_timeout: int | None = None,
        email_portal_check_dns: Literal["disable", "enable"] | None = None,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = None,
        gui_icap: Literal["enable", "disable"] | None = None,
        gui_implicit_policy: Literal["enable", "disable"] | None = None,
        gui_dns_database: Literal["enable", "disable"] | None = None,
        gui_load_balance: Literal["enable", "disable"] | None = None,
        gui_multicast_policy: Literal["enable", "disable"] | None = None,
        gui_dos_policy: Literal["enable", "disable"] | None = None,
        gui_object_colors: Literal["enable", "disable"] | None = None,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = None,
        gui_voip_profile: Literal["enable", "disable"] | None = None,
        gui_ap_profile: Literal["enable", "disable"] | None = None,
        gui_security_profile_group: Literal["enable", "disable"] | None = None,
        gui_local_in_policy: Literal["enable", "disable"] | None = None,
        gui_wanopt_cache: Literal["enable", "disable"] | None = None,
        gui_explicit_proxy: Literal["enable", "disable"] | None = None,
        gui_dynamic_routing: Literal["enable", "disable"] | None = None,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = None,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = None,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = None,
        gui_threat_weight: Literal["enable", "disable"] | None = None,
        gui_spamfilter: Literal["enable", "disable"] | None = None,
        gui_file_filter: Literal["enable", "disable"] | None = None,
        gui_application_control: Literal["enable", "disable"] | None = None,
        gui_ips: Literal["enable", "disable"] | None = None,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = None,
        gui_vpn: Literal["enable", "disable"] | None = None,
        gui_sslvpn: Literal["enable", "disable"] | None = None,
        gui_wireless_controller: Literal["enable", "disable"] | None = None,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = None,
        gui_switch_controller: Literal["enable", "disable"] | None = None,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = None,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = None,
        gui_traffic_shaping: Literal["enable", "disable"] | None = None,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = None,
        gui_antivirus: Literal["enable", "disable"] | None = None,
        gui_webfilter: Literal["enable", "disable"] | None = None,
        gui_videofilter: Literal["enable", "disable"] | None = None,
        gui_dnsfilter: Literal["enable", "disable"] | None = None,
        gui_waf_profile: Literal["enable", "disable"] | None = None,
        gui_dlp_profile: Literal["enable", "disable"] | None = None,
        gui_dlp_advanced: Literal["enable", "disable"] | None = None,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = None,
        gui_casb: Literal["enable", "disable"] | None = None,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = None,
        gui_advanced_policy: Literal["enable", "disable"] | None = None,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = None,
        gui_email_collection: Literal["enable", "disable"] | None = None,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = None,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = None,
        gui_ztna: Literal["enable", "disable"] | None = None,
        gui_ot: Literal["enable", "disable"] | None = None,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = None,
        gui_gtp: Literal["enable", "disable"] | None = None,
        location_id: str | None = None,
        ike_session_resume: Literal["enable", "disable"] | None = None,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = None,
        ike_dn_format: Literal["with-space", "no-space"] | None = None,
        ike_port: int | None = None,
        ike_tcp_port: int | None = None,
        ike_policy_route: Literal["enable", "disable"] | None = None,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = None,
        block_land_attack: Literal["disable", "enable"] | None = None,
        default_app_port_as_service: Literal["enable", "disable"] | None = None,
        fqdn_session_check: Literal["enable", "disable"] | None = None,
        ext_resource_session_check: Literal["enable", "disable"] | None = None,
        dyn_addr_session_check: Literal["enable", "disable"] | None = None,
        default_policy_expiry_days: int | None = None,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = None,
        internet_service_database_cache: Literal["disable", "enable"] | None = None,
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
        Move system/settings object to a new position.
        
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
            >>> fgt.api.cmdb.system_settings.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/settings",
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
        Clone system/settings object.
        
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
            >>> fgt.api.cmdb.system_settings.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/settings",
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
        Check if system/settings object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_settings.exists(name="myobj"):
            ...     fgt.api.cmdb.system_settings.post(payload_dict=data)
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

