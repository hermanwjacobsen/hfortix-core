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

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)


class Interface:
    """Interface Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Interface endpoint."""
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
        Retrieve system/interface configuration.

        Configure interfaces.

        Args:
            name: String identifier to retrieve specific object.
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
            >>> # Get all system/interface objects
            >>> result = fgt.api.cmdb.system_interface.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/interface by name
            >>> result = fgt.api.cmdb.system_interface.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_interface.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_interface.get(action="schema")

        See Also:
            - post(): Create new system/interface object
            - put(): Update existing system/interface object
            - delete(): Remove system/interface object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/system/interface/" + str(name)
        else:
            endpoint = "/system/interface"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: str | None = None,
        switch_controller_source_ip: str | None = None,
        mode: str | None = None,
        client_options: str | list | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: str | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: str | None = None,
        dhcp_relay_service: str | None = None,
        dhcp_relay_ip: str | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: str | None = None,
        dhcp_relay_allow_no_end_option: str | None = None,
        dhcp_relay_type: str | None = None,
        dhcp_smart_relay: str | None = None,
        dhcp_relay_agent_option: str | None = None,
        dhcp_classless_route_addition: str | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: str | None = None,
        gwdetect: str | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: str | None = None,
        ha_priority: int | None = None,
        fail_detect: str | None = None,
        fail_detect_option: str | None = None,
        fail_alert_method: str | None = None,
        fail_action_on_extender: str | None = None,
        fail_alert_interfaces: str | list | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: str | None = None,
        pppoe_unnumbered_negotiate: str | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: str | None = None,
        dns_server_override: str | None = None,
        dns_server_protocol: str | None = None,
        auth_type: str | None = None,
        pptp_client: str | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: str | None = None,
        pptp_timeout: int | None = None,
        arpforward: str | None = None,
        ndiscforward: str | None = None,
        broadcast_forward: str | None = None,
        bfd: str | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: str | None = None,
        icmp_send_redirect: str | None = None,
        icmp_accept_redirect: str | None = None,
        reachable_time: int | None = None,
        vlanforward: str | None = None,
        stpforward: str | None = None,
        stpforward_mode: str | None = None,
        ips_sniffer_mode: str | None = None,
        ident_accept: str | None = None,
        ipmac: str | None = None,
        subst: str | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: str | None = None,
        status: str | None = None,
        netbios_forward: str | None = None,
        wins_ip: str | None = None,
        type: str | None = None,
        dedicated_to: str | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: str | None = None,
        netflow_sampler: str | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: str | None = None,
        drop_fragment: str | None = None,
        src_check: str | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: str | None = None,
        explicit_web_proxy: str | None = None,
        explicit_ftp_proxy: str | None = None,
        proxy_captive_portal: str | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: str | None = None,
        mtu_override: str | None = None,
        mtu: int | None = None,
        vlan_protocol: str | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list | None = None,
        lacp_mode: str | None = None,
        lacp_ha_secondary: str | None = None,
        system_id_type: str | None = None,
        system_id: str | None = None,
        lacp_speed: str | None = None,
        min_links: int | None = None,
        min_links_down: str | None = None,
        algorithm: str | None = None,
        link_up_delay: int | None = None,
        aggregate_type: str | None = None,
        priority_override: str | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: str | None = None,
        security_mac_auth_bypass: str | None = None,
        security_ip_auth_bypass: str | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list | None = None,
        ike_saml_server: str | None = None,
        device_identification: str | None = None,
        exclude_signatures: str | None = None,
        device_user_identification: str | None = None,
        lldp_reception: str | None = None,
        lldp_transmission: str | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: str | None = None,
        vrrp_virtual_mac: str | None = None,
        vrrp: str | list | None = None,
        role: str | None = None,
        snmp_index: int | None = None,
        secondary_IP: str | None = None,
        secondaryip: str | list | None = None,
        preserve_session_route: str | None = None,
        auto_auth_extension_device: str | None = None,
        ap_discover: str | None = None,
        fortilink_neighbor_detect: str | None = None,
        ip_managed_by_fortiipam: str | None = None,
        managed_subnetwork_size: str | None = None,
        fortilink_split_interface: str | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: str | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: str | None = None,
        switch_controller_netflow_collect: str | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: str | None = None,
        switch_controller_igmp_snooping_proxy: str | None = None,
        switch_controller_igmp_snooping_fast_leave: str | None = None,
        switch_controller_dhcp_snooping: str | None = None,
        switch_controller_dhcp_snooping_verify_mac: str | None = None,
        switch_controller_dhcp_snooping_option82: str | None = None,
        dhcp_snooping_server_list: str | list | None = None,
        switch_controller_arp_inspection: str | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: str | None = None,
        switch_controller_iot_scanning: str | None = None,
        switch_controller_offload: str | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: str | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list | None = None,
        eap_supplicant: str | None = None,
        eap_method: str | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: str | None = None,
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
        fortilink: str | None = None,
        switch_controller_source_ip: str | None = None,
        mode: str | None = None,
        client_options: str | list | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: str | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: str | None = None,
        dhcp_relay_service: str | None = None,
        dhcp_relay_ip: str | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: str | None = None,
        dhcp_relay_allow_no_end_option: str | None = None,
        dhcp_relay_type: str | None = None,
        dhcp_smart_relay: str | None = None,
        dhcp_relay_agent_option: str | None = None,
        dhcp_classless_route_addition: str | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: str | None = None,
        gwdetect: str | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: str | None = None,
        ha_priority: int | None = None,
        fail_detect: str | None = None,
        fail_detect_option: str | None = None,
        fail_alert_method: str | None = None,
        fail_action_on_extender: str | None = None,
        fail_alert_interfaces: str | list | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: str | None = None,
        pppoe_unnumbered_negotiate: str | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: str | None = None,
        dns_server_override: str | None = None,
        dns_server_protocol: str | None = None,
        auth_type: str | None = None,
        pptp_client: str | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: str | None = None,
        pptp_timeout: int | None = None,
        arpforward: str | None = None,
        ndiscforward: str | None = None,
        broadcast_forward: str | None = None,
        bfd: str | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: str | None = None,
        icmp_send_redirect: str | None = None,
        icmp_accept_redirect: str | None = None,
        reachable_time: int | None = None,
        vlanforward: str | None = None,
        stpforward: str | None = None,
        stpforward_mode: str | None = None,
        ips_sniffer_mode: str | None = None,
        ident_accept: str | None = None,
        ipmac: str | None = None,
        subst: str | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: str | None = None,
        status: str | None = None,
        netbios_forward: str | None = None,
        wins_ip: str | None = None,
        type: str | None = None,
        dedicated_to: str | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: str | None = None,
        netflow_sampler: str | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: str | None = None,
        drop_fragment: str | None = None,
        src_check: str | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: str | None = None,
        explicit_web_proxy: str | None = None,
        explicit_ftp_proxy: str | None = None,
        proxy_captive_portal: str | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: str | None = None,
        mtu_override: str | None = None,
        mtu: int | None = None,
        vlan_protocol: str | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list | None = None,
        lacp_mode: str | None = None,
        lacp_ha_secondary: str | None = None,
        system_id_type: str | None = None,
        system_id: str | None = None,
        lacp_speed: str | None = None,
        min_links: int | None = None,
        min_links_down: str | None = None,
        algorithm: str | None = None,
        link_up_delay: int | None = None,
        aggregate_type: str | None = None,
        priority_override: str | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: str | None = None,
        security_mac_auth_bypass: str | None = None,
        security_ip_auth_bypass: str | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list | None = None,
        ike_saml_server: str | None = None,
        device_identification: str | None = None,
        exclude_signatures: str | None = None,
        device_user_identification: str | None = None,
        lldp_reception: str | None = None,
        lldp_transmission: str | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: str | None = None,
        vrrp_virtual_mac: str | None = None,
        vrrp: str | list | None = None,
        role: str | None = None,
        snmp_index: int | None = None,
        secondary_IP: str | None = None,
        secondaryip: str | list | None = None,
        preserve_session_route: str | None = None,
        auto_auth_extension_device: str | None = None,
        ap_discover: str | None = None,
        fortilink_neighbor_detect: str | None = None,
        ip_managed_by_fortiipam: str | None = None,
        managed_subnetwork_size: str | None = None,
        fortilink_split_interface: str | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: str | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: str | None = None,
        switch_controller_netflow_collect: str | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: str | None = None,
        switch_controller_igmp_snooping_proxy: str | None = None,
        switch_controller_igmp_snooping_fast_leave: str | None = None,
        switch_controller_dhcp_snooping: str | None = None,
        switch_controller_dhcp_snooping_verify_mac: str | None = None,
        switch_controller_dhcp_snooping_option82: str | None = None,
        dhcp_snooping_server_list: str | list | None = None,
        switch_controller_arp_inspection: str | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: str | None = None,
        switch_controller_iot_scanning: str | None = None,
        switch_controller_offload: str | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: str | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list | None = None,
        eap_supplicant: str | None = None,
        eap_method: str | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: str | None = None,
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
        try:
            response = self.get(name=name, vdom=vdom, raw_json=True)
            
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
            >>> print(Interface.help())
            
            >>> # Get field information
            >>> print(Interface.help("name"))
        """
        from ._helpers.interface import (
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
            >>> fields = Interface.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Interface.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.interface import get_all_fields, get_field_metadata

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
            >>> info = Interface.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.interface import get_field_metadata

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
            >>> is_valid, error = Interface.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.interface import validate_field_value

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
            >>> required = Interface.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.interface import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Interface.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.interface import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Interface.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.interface import get_schema_info

        return get_schema_info()
