"""
FortiOS CMDB - System interface

Configuration endpoint for managing cmdb system/interface objects.

API Endpoints:
    GET    /cmdb/system/interface
    POST   /cmdb/system/interface
    PUT    /cmdb/system/interface/{identifier}
    DELETE /cmdb/system/interface/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_interface.get()

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


class Interface(MetadataMixin):
    """Interface Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "interface"
    
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
        """Initialize Interface endpoint."""
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
        Retrieve system/interface configuration.

        Configure interfaces.

        Args:
            name: String identifier to retrieve specific object.
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
            >>> # Get all system/interface objects
            >>> result = fgt.api.cmdb.system_interface.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/interface by name
            >>> result = fgt.api.cmdb.system_interface.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_interface.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_interface.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_interface.get_schema()

        See Also:
            - post(): Create new system/interface object
            - put(): Update existing system/interface object
            - delete(): Remove system/interface object
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
            endpoint = "/system/interface/" + str(name)
        else:
            endpoint = "/system/interface"
        
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
            >>> schema = fgt.api.cmdb.system_interface.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_interface.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: Literal["enable", "disable"] | None = None,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = None,
        mode: Literal["static", "dhcp", "pppoe"] | None = None,
        client_options: str | list | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = None,
        dhcp_relay_service: Literal["disable", "enable"] | None = None,
        dhcp_relay_ip: str | list | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = None,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = None,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = None,
        dhcp_smart_relay: Literal["disable", "enable"] | None = None,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = None,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list | None = None,
        gwdetect: Literal["enable", "disable"] | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list | None = None,
        ha_priority: int | None = None,
        fail_detect: Literal["enable", "disable"] | None = None,
        fail_detect_option: Literal["detectserver", "link-down"] | list | None = None,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = None,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = None,
        fail_alert_interfaces: str | list | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = None,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        multilink: Literal["enable", "disable"] | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: Literal["enable", "disable"] | None = None,
        dns_server_override: Literal["enable", "disable"] | None = None,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list | None = None,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_client: Literal["enable", "disable"] | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_timeout: int | None = None,
        arpforward: Literal["enable", "disable"] | None = None,
        ndiscforward: Literal["enable", "disable"] | None = None,
        broadcast_forward: Literal["enable", "disable"] | None = None,
        bfd: Literal["global", "enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: Literal["enable", "disable"] | None = None,
        icmp_send_redirect: Literal["enable", "disable"] | None = None,
        icmp_accept_redirect: Literal["enable", "disable"] | None = None,
        reachable_time: int | None = None,
        vlanforward: Literal["enable", "disable"] | None = None,
        stpforward: Literal["enable", "disable"] | None = None,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = None,
        ips_sniffer_mode: Literal["enable", "disable"] | None = None,
        ident_accept: Literal["enable", "disable"] | None = None,
        ipmac: Literal["enable", "disable"] | None = None,
        subst: Literal["enable", "disable"] | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = None,
        status: Literal["up", "down"] | None = None,
        netbios_forward: Literal["disable", "enable"] | None = None,
        wins_ip: str | None = None,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = None,
        dedicated_to: Literal["none", "management"] | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: Literal["enable", "disable"] | None = None,
        drop_fragment: Literal["enable", "disable"] | None = None,
        src_check: Literal["enable", "disable"] | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: Literal["tx", "rx", "both"] | None = None,
        explicit_web_proxy: Literal["enable", "disable"] | None = None,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = None,
        proxy_captive_portal: Literal["enable", "disable"] | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: Literal["enable", "disable"] | None = None,
        mtu_override: Literal["enable", "disable"] | None = None,
        mtu: int | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list | None = None,
        lacp_mode: Literal["static", "passive", "active"] | None = None,
        lacp_ha_secondary: Literal["enable", "disable"] | None = None,
        system_id_type: Literal["auto", "user"] | None = None,
        system_id: str | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = None,
        link_up_delay: int | None = None,
        aggregate_type: Literal["physical", "vxlan"] | None = None,
        priority_override: Literal["enable", "disable"] | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = None,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = None,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list | None = None,
        ike_saml_server: str | None = None,
        device_identification: Literal["enable", "disable"] | None = None,
        exclude_signatures: Literal["iot", "ot"] | list | None = None,
        device_user_identification: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = None,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: Literal["enable", "disable"] | None = None,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = None,
        vrrp: str | list | None = None,
        phy_setting: str | None = None,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = None,
        snmp_index: int | None = None,
        secondary_IP: Literal["enable", "disable"] | None = None,
        secondaryip: str | list | None = None,
        preserve_session_route: Literal["enable", "disable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        ap_discover: Literal["enable", "disable"] | None = None,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = None,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = None,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = None,
        fortilink_split_interface: Literal["enable", "disable"] | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = None,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = None,
        dhcp_snooping_server_list: str | list | None = None,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = None,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = None,
        switch_controller_offload: Literal["enable", "disable"] | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list | None = None,
        eap_supplicant: Literal["enable", "disable"] | None = None,
        eap_method: Literal["tls", "peap"] | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        ipv6: str | None = None,
        physical: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/interface object.

        Configure interfaces.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            vdom: Interface is in this virtual domain (VDOM).
            vrf: Virtual Routing Forwarding ID.
            cli_conn_status: CLI connection status.
            fortilink: Enable FortiLink to dedicate this interface to manage other Fortinet devices.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_interface.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_interface.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            vrf=vrf,
            cli_conn_status=cli_conn_status,
            fortilink=fortilink,
            switch_controller_source_ip=switch_controller_source_ip,
            mode=mode,
            client_options=client_options,
            distance=distance,
            priority=priority,
            dhcp_relay_interface_select_method=dhcp_relay_interface_select_method,
            dhcp_relay_interface=dhcp_relay_interface,
            dhcp_relay_vrf_select=dhcp_relay_vrf_select,
            dhcp_broadcast_flag=dhcp_broadcast_flag,
            dhcp_relay_service=dhcp_relay_service,
            dhcp_relay_ip=dhcp_relay_ip,
            dhcp_relay_source_ip=dhcp_relay_source_ip,
            dhcp_relay_circuit_id=dhcp_relay_circuit_id,
            dhcp_relay_link_selection=dhcp_relay_link_selection,
            dhcp_relay_request_all_server=dhcp_relay_request_all_server,
            dhcp_relay_allow_no_end_option=dhcp_relay_allow_no_end_option,
            dhcp_relay_type=dhcp_relay_type,
            dhcp_smart_relay=dhcp_smart_relay,
            dhcp_relay_agent_option=dhcp_relay_agent_option,
            dhcp_classless_route_addition=dhcp_classless_route_addition,
            management_ip=management_ip,
            ip=ip,
            allowaccess=allowaccess,
            gwdetect=gwdetect,
            ping_serv_status=ping_serv_status,
            detectserver=detectserver,
            detectprotocol=detectprotocol,
            ha_priority=ha_priority,
            fail_detect=fail_detect,
            fail_detect_option=fail_detect_option,
            fail_alert_method=fail_alert_method,
            fail_action_on_extender=fail_action_on_extender,
            fail_alert_interfaces=fail_alert_interfaces,
            dhcp_client_identifier=dhcp_client_identifier,
            dhcp_renew_time=dhcp_renew_time,
            ipunnumbered=ipunnumbered,
            username=username,
            pppoe_egress_cos=pppoe_egress_cos,
            pppoe_unnumbered_negotiate=pppoe_unnumbered_negotiate,
            password=password,
            idle_timeout=idle_timeout,
            multilink=multilink,
            mrru=mrru,
            detected_peer_mtu=detected_peer_mtu,
            disc_retry_timeout=disc_retry_timeout,
            padt_retry_timeout=padt_retry_timeout,
            service_name=service_name,
            ac_name=ac_name,
            lcp_echo_interval=lcp_echo_interval,
            lcp_max_echo_fails=lcp_max_echo_fails,
            defaultgw=defaultgw,
            dns_server_override=dns_server_override,
            dns_server_protocol=dns_server_protocol,
            auth_type=auth_type,
            pptp_client=pptp_client,
            pptp_user=pptp_user,
            pptp_password=pptp_password,
            pptp_server_ip=pptp_server_ip,
            pptp_auth_type=pptp_auth_type,
            pptp_timeout=pptp_timeout,
            arpforward=arpforward,
            ndiscforward=ndiscforward,
            broadcast_forward=broadcast_forward,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_required_min_rx=bfd_required_min_rx,
            l2forward=l2forward,
            icmp_send_redirect=icmp_send_redirect,
            icmp_accept_redirect=icmp_accept_redirect,
            reachable_time=reachable_time,
            vlanforward=vlanforward,
            stpforward=stpforward,
            stpforward_mode=stpforward_mode,
            ips_sniffer_mode=ips_sniffer_mode,
            ident_accept=ident_accept,
            ipmac=ipmac,
            subst=subst,
            macaddr=macaddr,
            virtual_mac=virtual_mac,
            substitute_dst_mac=substitute_dst_mac,
            speed=speed,
            status=status,
            netbios_forward=netbios_forward,
            wins_ip=wins_ip,
            type=type,
            dedicated_to=dedicated_to,
            trust_ip_1=trust_ip_1,
            trust_ip_2=trust_ip_2,
            trust_ip_3=trust_ip_3,
            trust_ip6_1=trust_ip6_1,
            trust_ip6_2=trust_ip6_2,
            trust_ip6_3=trust_ip6_3,
            ring_rx=ring_rx,
            ring_tx=ring_tx,
            wccp=wccp,
            netflow_sampler=netflow_sampler,
            netflow_sample_rate=netflow_sample_rate,
            netflow_sampler_id=netflow_sampler_id,
            sflow_sampler=sflow_sampler,
            drop_fragment=drop_fragment,
            src_check=src_check,
            sample_rate=sample_rate,
            polling_interval=polling_interval,
            sample_direction=sample_direction,
            explicit_web_proxy=explicit_web_proxy,
            explicit_ftp_proxy=explicit_ftp_proxy,
            proxy_captive_portal=proxy_captive_portal,
            tcp_mss=tcp_mss,
            inbandwidth=inbandwidth,
            outbandwidth=outbandwidth,
            egress_shaping_profile=egress_shaping_profile,
            ingress_shaping_profile=ingress_shaping_profile,
            spillover_threshold=spillover_threshold,
            ingress_spillover_threshold=ingress_spillover_threshold,
            weight=weight,
            interface=interface,
            external=external,
            mtu_override=mtu_override,
            mtu=mtu,
            vlan_protocol=vlan_protocol,
            vlanid=vlanid,
            forward_domain=forward_domain,
            remote_ip=remote_ip,
            member=member,
            lacp_mode=lacp_mode,
            lacp_ha_secondary=lacp_ha_secondary,
            system_id_type=system_id_type,
            system_id=system_id,
            lacp_speed=lacp_speed,
            min_links=min_links,
            min_links_down=min_links_down,
            algorithm=algorithm,
            link_up_delay=link_up_delay,
            aggregate_type=aggregate_type,
            priority_override=priority_override,
            aggregate=aggregate,
            redundant_interface=redundant_interface,
            devindex=devindex,
            vindex=vindex,
            switch=switch,
            description=description,
            alias=alias,
            security_mode=security_mode,
            security_mac_auth_bypass=security_mac_auth_bypass,
            security_ip_auth_bypass=security_ip_auth_bypass,
            security_external_web=security_external_web,
            security_external_logout=security_external_logout,
            replacemsg_override_group=replacemsg_override_group,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            security_exempt_list=security_exempt_list,
            security_groups=security_groups,
            ike_saml_server=ike_saml_server,
            device_identification=device_identification,
            exclude_signatures=exclude_signatures,
            device_user_identification=device_user_identification,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            lldp_network_policy=lldp_network_policy,
            estimated_upstream_bandwidth=estimated_upstream_bandwidth,
            estimated_downstream_bandwidth=estimated_downstream_bandwidth,
            measured_upstream_bandwidth=measured_upstream_bandwidth,
            measured_downstream_bandwidth=measured_downstream_bandwidth,
            bandwidth_measure_time=bandwidth_measure_time,
            monitor_bandwidth=monitor_bandwidth,
            vrrp_virtual_mac=vrrp_virtual_mac,
            vrrp=vrrp,
            phy_setting=phy_setting,
            role=role,
            snmp_index=snmp_index,
            secondary_IP=secondary_IP,
            secondaryip=secondaryip,
            preserve_session_route=preserve_session_route,
            auto_auth_extension_device=auto_auth_extension_device,
            ap_discover=ap_discover,
            fortilink_neighbor_detect=fortilink_neighbor_detect,
            ip_managed_by_fortiipam=ip_managed_by_fortiipam,
            managed_subnetwork_size=managed_subnetwork_size,
            fortilink_split_interface=fortilink_split_interface,
            internal=internal,
            fortilink_backup_link=fortilink_backup_link,
            switch_controller_access_vlan=switch_controller_access_vlan,
            switch_controller_traffic_policy=switch_controller_traffic_policy,
            switch_controller_rspan_mode=switch_controller_rspan_mode,
            switch_controller_netflow_collect=switch_controller_netflow_collect,
            switch_controller_mgmt_vlan=switch_controller_mgmt_vlan,
            switch_controller_igmp_snooping=switch_controller_igmp_snooping,
            switch_controller_igmp_snooping_proxy=switch_controller_igmp_snooping_proxy,
            switch_controller_igmp_snooping_fast_leave=switch_controller_igmp_snooping_fast_leave,
            switch_controller_dhcp_snooping=switch_controller_dhcp_snooping,
            switch_controller_dhcp_snooping_verify_mac=switch_controller_dhcp_snooping_verify_mac,
            switch_controller_dhcp_snooping_option82=switch_controller_dhcp_snooping_option82,
            dhcp_snooping_server_list=dhcp_snooping_server_list,
            switch_controller_arp_inspection=switch_controller_arp_inspection,
            switch_controller_learning_limit=switch_controller_learning_limit,
            switch_controller_nac=switch_controller_nac,
            switch_controller_dynamic=switch_controller_dynamic,
            switch_controller_feature=switch_controller_feature,
            switch_controller_iot_scanning=switch_controller_iot_scanning,
            switch_controller_offload=switch_controller_offload,
            switch_controller_offload_ip=switch_controller_offload_ip,
            switch_controller_offload_gw=switch_controller_offload_gw,
            swc_vlan=swc_vlan,
            swc_first_create=swc_first_create,
            color=color,
            tagging=tagging,
            eap_supplicant=eap_supplicant,
            eap_method=eap_method,
            eap_identity=eap_identity,
            eap_password=eap_password,
            eap_ca_cert=eap_ca_cert,
            eap_user_cert=eap_user_cert,
            default_purdue_level=default_purdue_level,
            ipv6=ipv6,
            physical=physical,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/interface",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/interface/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: Literal["enable", "disable"] | None = None,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = None,
        mode: Literal["static", "dhcp", "pppoe"] | None = None,
        client_options: str | list | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = None,
        dhcp_relay_service: Literal["disable", "enable"] | None = None,
        dhcp_relay_ip: str | list | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = None,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = None,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = None,
        dhcp_smart_relay: Literal["disable", "enable"] | None = None,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = None,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list | None = None,
        gwdetect: Literal["enable", "disable"] | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list | None = None,
        ha_priority: int | None = None,
        fail_detect: Literal["enable", "disable"] | None = None,
        fail_detect_option: Literal["detectserver", "link-down"] | list | None = None,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = None,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = None,
        fail_alert_interfaces: str | list | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = None,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        multilink: Literal["enable", "disable"] | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: Literal["enable", "disable"] | None = None,
        dns_server_override: Literal["enable", "disable"] | None = None,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list | None = None,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_client: Literal["enable", "disable"] | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_timeout: int | None = None,
        arpforward: Literal["enable", "disable"] | None = None,
        ndiscforward: Literal["enable", "disable"] | None = None,
        broadcast_forward: Literal["enable", "disable"] | None = None,
        bfd: Literal["global", "enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: Literal["enable", "disable"] | None = None,
        icmp_send_redirect: Literal["enable", "disable"] | None = None,
        icmp_accept_redirect: Literal["enable", "disable"] | None = None,
        reachable_time: int | None = None,
        vlanforward: Literal["enable", "disable"] | None = None,
        stpforward: Literal["enable", "disable"] | None = None,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = None,
        ips_sniffer_mode: Literal["enable", "disable"] | None = None,
        ident_accept: Literal["enable", "disable"] | None = None,
        ipmac: Literal["enable", "disable"] | None = None,
        subst: Literal["enable", "disable"] | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = None,
        status: Literal["up", "down"] | None = None,
        netbios_forward: Literal["disable", "enable"] | None = None,
        wins_ip: str | None = None,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = None,
        dedicated_to: Literal["none", "management"] | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: Literal["enable", "disable"] | None = None,
        drop_fragment: Literal["enable", "disable"] | None = None,
        src_check: Literal["enable", "disable"] | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: Literal["tx", "rx", "both"] | None = None,
        explicit_web_proxy: Literal["enable", "disable"] | None = None,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = None,
        proxy_captive_portal: Literal["enable", "disable"] | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: Literal["enable", "disable"] | None = None,
        mtu_override: Literal["enable", "disable"] | None = None,
        mtu: int | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list | None = None,
        lacp_mode: Literal["static", "passive", "active"] | None = None,
        lacp_ha_secondary: Literal["enable", "disable"] | None = None,
        system_id_type: Literal["auto", "user"] | None = None,
        system_id: str | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = None,
        link_up_delay: int | None = None,
        aggregate_type: Literal["physical", "vxlan"] | None = None,
        priority_override: Literal["enable", "disable"] | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = None,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = None,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list | None = None,
        ike_saml_server: str | None = None,
        device_identification: Literal["enable", "disable"] | None = None,
        exclude_signatures: Literal["iot", "ot"] | list | None = None,
        device_user_identification: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = None,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: Literal["enable", "disable"] | None = None,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = None,
        vrrp: str | list | None = None,
        phy_setting: str | None = None,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = None,
        snmp_index: int | None = None,
        secondary_IP: Literal["enable", "disable"] | None = None,
        secondaryip: str | list | None = None,
        preserve_session_route: Literal["enable", "disable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        ap_discover: Literal["enable", "disable"] | None = None,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = None,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = None,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = None,
        fortilink_split_interface: Literal["enable", "disable"] | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = None,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = None,
        dhcp_snooping_server_list: str | list | None = None,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = None,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = None,
        switch_controller_offload: Literal["enable", "disable"] | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list | None = None,
        eap_supplicant: Literal["enable", "disable"] | None = None,
        eap_method: Literal["tls", "peap"] | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        ipv6: str | None = None,
        physical: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/interface object.

        Configure interfaces.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            vdom: Interface is in this virtual domain (VDOM).
            vrf: Virtual Routing Forwarding ID.
            cli_conn_status: CLI connection status.
            fortilink: Enable FortiLink to dedicate this interface to manage other Fortinet devices.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_interface.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Interface.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_interface.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Interface.required_fields()) }}
            
            Use Interface.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            vrf=vrf,
            cli_conn_status=cli_conn_status,
            fortilink=fortilink,
            switch_controller_source_ip=switch_controller_source_ip,
            mode=mode,
            client_options=client_options,
            distance=distance,
            priority=priority,
            dhcp_relay_interface_select_method=dhcp_relay_interface_select_method,
            dhcp_relay_interface=dhcp_relay_interface,
            dhcp_relay_vrf_select=dhcp_relay_vrf_select,
            dhcp_broadcast_flag=dhcp_broadcast_flag,
            dhcp_relay_service=dhcp_relay_service,
            dhcp_relay_ip=dhcp_relay_ip,
            dhcp_relay_source_ip=dhcp_relay_source_ip,
            dhcp_relay_circuit_id=dhcp_relay_circuit_id,
            dhcp_relay_link_selection=dhcp_relay_link_selection,
            dhcp_relay_request_all_server=dhcp_relay_request_all_server,
            dhcp_relay_allow_no_end_option=dhcp_relay_allow_no_end_option,
            dhcp_relay_type=dhcp_relay_type,
            dhcp_smart_relay=dhcp_smart_relay,
            dhcp_relay_agent_option=dhcp_relay_agent_option,
            dhcp_classless_route_addition=dhcp_classless_route_addition,
            management_ip=management_ip,
            ip=ip,
            allowaccess=allowaccess,
            gwdetect=gwdetect,
            ping_serv_status=ping_serv_status,
            detectserver=detectserver,
            detectprotocol=detectprotocol,
            ha_priority=ha_priority,
            fail_detect=fail_detect,
            fail_detect_option=fail_detect_option,
            fail_alert_method=fail_alert_method,
            fail_action_on_extender=fail_action_on_extender,
            fail_alert_interfaces=fail_alert_interfaces,
            dhcp_client_identifier=dhcp_client_identifier,
            dhcp_renew_time=dhcp_renew_time,
            ipunnumbered=ipunnumbered,
            username=username,
            pppoe_egress_cos=pppoe_egress_cos,
            pppoe_unnumbered_negotiate=pppoe_unnumbered_negotiate,
            password=password,
            idle_timeout=idle_timeout,
            multilink=multilink,
            mrru=mrru,
            detected_peer_mtu=detected_peer_mtu,
            disc_retry_timeout=disc_retry_timeout,
            padt_retry_timeout=padt_retry_timeout,
            service_name=service_name,
            ac_name=ac_name,
            lcp_echo_interval=lcp_echo_interval,
            lcp_max_echo_fails=lcp_max_echo_fails,
            defaultgw=defaultgw,
            dns_server_override=dns_server_override,
            dns_server_protocol=dns_server_protocol,
            auth_type=auth_type,
            pptp_client=pptp_client,
            pptp_user=pptp_user,
            pptp_password=pptp_password,
            pptp_server_ip=pptp_server_ip,
            pptp_auth_type=pptp_auth_type,
            pptp_timeout=pptp_timeout,
            arpforward=arpforward,
            ndiscforward=ndiscforward,
            broadcast_forward=broadcast_forward,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_required_min_rx=bfd_required_min_rx,
            l2forward=l2forward,
            icmp_send_redirect=icmp_send_redirect,
            icmp_accept_redirect=icmp_accept_redirect,
            reachable_time=reachable_time,
            vlanforward=vlanforward,
            stpforward=stpforward,
            stpforward_mode=stpforward_mode,
            ips_sniffer_mode=ips_sniffer_mode,
            ident_accept=ident_accept,
            ipmac=ipmac,
            subst=subst,
            macaddr=macaddr,
            virtual_mac=virtual_mac,
            substitute_dst_mac=substitute_dst_mac,
            speed=speed,
            status=status,
            netbios_forward=netbios_forward,
            wins_ip=wins_ip,
            type=type,
            dedicated_to=dedicated_to,
            trust_ip_1=trust_ip_1,
            trust_ip_2=trust_ip_2,
            trust_ip_3=trust_ip_3,
            trust_ip6_1=trust_ip6_1,
            trust_ip6_2=trust_ip6_2,
            trust_ip6_3=trust_ip6_3,
            ring_rx=ring_rx,
            ring_tx=ring_tx,
            wccp=wccp,
            netflow_sampler=netflow_sampler,
            netflow_sample_rate=netflow_sample_rate,
            netflow_sampler_id=netflow_sampler_id,
            sflow_sampler=sflow_sampler,
            drop_fragment=drop_fragment,
            src_check=src_check,
            sample_rate=sample_rate,
            polling_interval=polling_interval,
            sample_direction=sample_direction,
            explicit_web_proxy=explicit_web_proxy,
            explicit_ftp_proxy=explicit_ftp_proxy,
            proxy_captive_portal=proxy_captive_portal,
            tcp_mss=tcp_mss,
            inbandwidth=inbandwidth,
            outbandwidth=outbandwidth,
            egress_shaping_profile=egress_shaping_profile,
            ingress_shaping_profile=ingress_shaping_profile,
            spillover_threshold=spillover_threshold,
            ingress_spillover_threshold=ingress_spillover_threshold,
            weight=weight,
            interface=interface,
            external=external,
            mtu_override=mtu_override,
            mtu=mtu,
            vlan_protocol=vlan_protocol,
            vlanid=vlanid,
            forward_domain=forward_domain,
            remote_ip=remote_ip,
            member=member,
            lacp_mode=lacp_mode,
            lacp_ha_secondary=lacp_ha_secondary,
            system_id_type=system_id_type,
            system_id=system_id,
            lacp_speed=lacp_speed,
            min_links=min_links,
            min_links_down=min_links_down,
            algorithm=algorithm,
            link_up_delay=link_up_delay,
            aggregate_type=aggregate_type,
            priority_override=priority_override,
            aggregate=aggregate,
            redundant_interface=redundant_interface,
            devindex=devindex,
            vindex=vindex,
            switch=switch,
            description=description,
            alias=alias,
            security_mode=security_mode,
            security_mac_auth_bypass=security_mac_auth_bypass,
            security_ip_auth_bypass=security_ip_auth_bypass,
            security_external_web=security_external_web,
            security_external_logout=security_external_logout,
            replacemsg_override_group=replacemsg_override_group,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            security_exempt_list=security_exempt_list,
            security_groups=security_groups,
            ike_saml_server=ike_saml_server,
            device_identification=device_identification,
            exclude_signatures=exclude_signatures,
            device_user_identification=device_user_identification,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            lldp_network_policy=lldp_network_policy,
            estimated_upstream_bandwidth=estimated_upstream_bandwidth,
            estimated_downstream_bandwidth=estimated_downstream_bandwidth,
            measured_upstream_bandwidth=measured_upstream_bandwidth,
            measured_downstream_bandwidth=measured_downstream_bandwidth,
            bandwidth_measure_time=bandwidth_measure_time,
            monitor_bandwidth=monitor_bandwidth,
            vrrp_virtual_mac=vrrp_virtual_mac,
            vrrp=vrrp,
            phy_setting=phy_setting,
            role=role,
            snmp_index=snmp_index,
            secondary_IP=secondary_IP,
            secondaryip=secondaryip,
            preserve_session_route=preserve_session_route,
            auto_auth_extension_device=auto_auth_extension_device,
            ap_discover=ap_discover,
            fortilink_neighbor_detect=fortilink_neighbor_detect,
            ip_managed_by_fortiipam=ip_managed_by_fortiipam,
            managed_subnetwork_size=managed_subnetwork_size,
            fortilink_split_interface=fortilink_split_interface,
            internal=internal,
            fortilink_backup_link=fortilink_backup_link,
            switch_controller_access_vlan=switch_controller_access_vlan,
            switch_controller_traffic_policy=switch_controller_traffic_policy,
            switch_controller_rspan_mode=switch_controller_rspan_mode,
            switch_controller_netflow_collect=switch_controller_netflow_collect,
            switch_controller_mgmt_vlan=switch_controller_mgmt_vlan,
            switch_controller_igmp_snooping=switch_controller_igmp_snooping,
            switch_controller_igmp_snooping_proxy=switch_controller_igmp_snooping_proxy,
            switch_controller_igmp_snooping_fast_leave=switch_controller_igmp_snooping_fast_leave,
            switch_controller_dhcp_snooping=switch_controller_dhcp_snooping,
            switch_controller_dhcp_snooping_verify_mac=switch_controller_dhcp_snooping_verify_mac,
            switch_controller_dhcp_snooping_option82=switch_controller_dhcp_snooping_option82,
            dhcp_snooping_server_list=dhcp_snooping_server_list,
            switch_controller_arp_inspection=switch_controller_arp_inspection,
            switch_controller_learning_limit=switch_controller_learning_limit,
            switch_controller_nac=switch_controller_nac,
            switch_controller_dynamic=switch_controller_dynamic,
            switch_controller_feature=switch_controller_feature,
            switch_controller_iot_scanning=switch_controller_iot_scanning,
            switch_controller_offload=switch_controller_offload,
            switch_controller_offload_ip=switch_controller_offload_ip,
            switch_controller_offload_gw=switch_controller_offload_gw,
            swc_vlan=swc_vlan,
            swc_first_create=swc_first_create,
            color=color,
            tagging=tagging,
            eap_supplicant=eap_supplicant,
            eap_method=eap_method,
            eap_identity=eap_identity,
            eap_password=eap_password,
            eap_ca_cert=eap_ca_cert,
            eap_user_cert=eap_user_cert,
            default_purdue_level=default_purdue_level,
            ipv6=ipv6,
            physical=physical,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/interface",
            )

        endpoint = "/system/interface"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/interface object.

        Configure interfaces.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_interface.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/interface/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/interface object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_interface.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_interface.exists(name=1):
            ...     fgt.api.cmdb.system_interface.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
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
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/interface object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_interface.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_interface.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("name")
        if not mkey_value:
            raise ValueError("name is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)

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
        Move system/interface object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_interface.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/interface",
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
        Clone system/interface object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_interface.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/interface",
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
        Check if system/interface object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_interface.exists(name=1):
            ...     fgt.api.cmdb.system_interface.post(payload_dict=data)
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

