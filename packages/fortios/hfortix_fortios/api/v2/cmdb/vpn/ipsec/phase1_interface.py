"""
FortiOS CMDB - Vpn ipsec phase1_interface

Configuration endpoint for managing cmdb vpn/ipsec/phase1_interface objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec/phase1_interface
    POST   /cmdb/vpn/ipsec/phase1_interface
    PUT    /cmdb/vpn/ipsec/phase1_interface/{identifier}
    DELETE /cmdb/vpn/ipsec/phase1_interface/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_ipsec_phase1_interface.get()

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


class Phase1Interface(MetadataMixin):
    """Phase1Interface Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "phase1_interface"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Phase1Interface endpoint."""
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
        Retrieve vpn/ipsec/phase1_interface configuration.

        Configure VPN remote gateway.

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
            >>> # Get all vpn/ipsec/phase1_interface objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec/phase1_interface by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase1_interface.get(action="schema")

        See Also:
            - post(): Create new vpn/ipsec/phase1_interface object
            - put(): Update existing vpn/ipsec/phase1_interface object
            - delete(): Remove vpn/ipsec/phase1_interface object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/vpn.ipsec/phase1-interface/" + str(name)
        else:
            endpoint = "/vpn.ipsec/phase1-interface"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        type: str | None = None,
        interface: str | None = None,
        ip_version: str | None = None,
        ike_version: str | None = None,
        local_gw: str | None = None,
        local_gw6: str | None = None,
        remote_gw: str | None = None,
        remote_gw6: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list | None = None,
        authmethod: str | None = None,
        authmethod_remote: str | None = None,
        mode: str | None = None,
        peertype: str | None = None,
        peerid: str | None = None,
        default_gw: str | None = None,
        default_gw_priority: int | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        monitor: str | list | None = None,
        monitor_min: int | None = None,
        monitor_hold_down_type: str | None = None,
        monitor_hold_down_delay: int | None = None,
        monitor_hold_down_weekday: str | None = None,
        monitor_hold_down_time: str | None = None,
        net_device: str | None = None,
        passive_mode: str | None = None,
        exchange_interface_ip: str | None = None,
        exchange_ip_addr4: str | None = None,
        exchange_ip_addr6: str | None = None,
        aggregate_member: str | None = None,
        aggregate_weight: int | None = None,
        packet_redistribution: str | None = None,
        peer_egress_shaping: str | None = None,
        peer_egress_shaping_value: int | None = None,
        mode_cfg: str | None = None,
        mode_cfg_allow_client_selector: str | None = None,
        assign_ip: str | None = None,
        assign_ip_from: str | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: str | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: str | list | None = None,
        dns_suffix_search: str | list | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: str | list | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: str | list | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: str | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: str | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: str | None = None,
        client_auto_negotiate: str | None = None,
        client_keep_alive: str | None = None,
        backup_gateway: str | list | None = None,
        proposal: str | list | None = None,
        add_route: str | None = None,
        add_gw_route: str | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: str | None = None,
        auto_negotiate: str | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: str | None = None,
        ip_fragmentation: str | None = None,
        dpd: str | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: str | None = None,
        send_cert_chain: str | None = None,
        dhgrp: str | list | None = None,
        addke1: str | list | None = None,
        addke2: str | list | None = None,
        addke3: str | list | None = None,
        addke4: str | list | None = None,
        addke5: str | list | None = None,
        addke6: str | list | None = None,
        addke7: str | list | None = None,
        suite_b: str | None = None,
        eap: str | None = None,
        eap_identity: str | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: str | None = None,
        acct_verify: str | None = None,
        ppk: str | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: str | None = None,
        xauthtype: str | None = None,
        reauth: str | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: str | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: str | None = None,
        idle_timeout: str | None = None,
        shared_idle_timeout: str | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: str | None = None,
        fgsp_sync: str | None = None,
        inbound_dscp_copy: str | None = None,
        auto_discovery_sender: str | None = None,
        auto_discovery_receiver: str | None = None,
        auto_discovery_forwarder: str | None = None,
        auto_discovery_psk: str | None = None,
        auto_discovery_shortcuts: str | None = None,
        auto_discovery_crossover: str | None = None,
        auto_discovery_offer_interval: int | None = None,
        auto_discovery_dialup_placeholder: str | None = None,
        encapsulation: str | None = None,
        encapsulation_address: str | None = None,
        encap_local_gw4: str | None = None,
        encap_local_gw6: str | None = None,
        encap_remote_gw4: str | None = None,
        encap_remote_gw6: str | None = None,
        vni: int | None = None,
        nattraversal: str | None = None,
        esn: str | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: str | None = None,
        azure_ad_autoconnect: str | None = None,
        client_resume: str | None = None,
        client_resume_interval: int | None = None,
        rekey: str | None = None,
        digital_signature_auth: str | None = None,
        signature_hash_alg: str | list | None = None,
        rsa_signature_format: str | None = None,
        rsa_signature_hash_override: str | None = None,
        enforce_unique_id: str | None = None,
        cert_id_validation: str | None = None,
        fec_egress: str | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: str | None = None,
        fec_redundant: int | None = None,
        fec_ingress: str | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: str | None = None,
        network_id: int | None = None,
        dev_id_notification: str | None = None,
        dev_id: str | None = None,
        loopback_asymroute: str | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: str | None = None,
        ipv6_auto_linklocal: str | None = None,
        ems_sn_check: str | None = None,
        cert_trust_store: str | None = None,
        qkd: str | None = None,
        qkd_hybrid: str | None = None,
        qkd_profile: str | None = None,
        transport: str | None = None,
        fortinet_esp: str | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: str | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list | None = None,
        remote_gw6_match: str | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: str | None = None,
        cert_peer_username_strip: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/ipsec/phase1_interface object.

        Configure VPN remote gateway.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IPsec remote gateway name.
            type: Remote gateway type.
            interface: Local physical, aggregate, or VLAN outgoing interface.
            ip_version: IP version to use for VPN interface.
            ike_version: IKE protocol version.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            type=type,
            interface=interface,
            ip_version=ip_version,
            ike_version=ike_version,
            local_gw=local_gw,
            local_gw6=local_gw6,
            remote_gw=remote_gw,
            remote_gw6=remote_gw6,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            default_gw=default_gw,
            default_gw_priority=default_gw_priority,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
            monitor=monitor,
            monitor_min=monitor_min,
            monitor_hold_down_type=monitor_hold_down_type,
            monitor_hold_down_delay=monitor_hold_down_delay,
            monitor_hold_down_weekday=monitor_hold_down_weekday,
            monitor_hold_down_time=monitor_hold_down_time,
            net_device=net_device,
            passive_mode=passive_mode,
            exchange_interface_ip=exchange_interface_ip,
            exchange_ip_addr4=exchange_ip_addr4,
            exchange_ip_addr6=exchange_ip_addr6,
            aggregate_member=aggregate_member,
            aggregate_weight=aggregate_weight,
            packet_redistribution=packet_redistribution,
            peer_egress_shaping=peer_egress_shaping,
            peer_egress_shaping_value=peer_egress_shaping_value,
            mode_cfg=mode_cfg,
            mode_cfg_allow_client_selector=mode_cfg_allow_client_selector,
            assign_ip=assign_ip,
            assign_ip_from=assign_ip_from,
            ipv4_start_ip=ipv4_start_ip,
            ipv4_end_ip=ipv4_end_ip,
            ipv4_netmask=ipv4_netmask,
            dhcp_ra_giaddr=dhcp_ra_giaddr,
            dhcp6_ra_linkaddr=dhcp6_ra_linkaddr,
            dns_mode=dns_mode,
            ipv4_dns_server1=ipv4_dns_server1,
            ipv4_dns_server2=ipv4_dns_server2,
            ipv4_dns_server3=ipv4_dns_server3,
            internal_domain_list=internal_domain_list,
            dns_suffix_search=dns_suffix_search,
            ipv4_wins_server1=ipv4_wins_server1,
            ipv4_wins_server2=ipv4_wins_server2,
            ipv4_exclude_range=ipv4_exclude_range,
            ipv4_split_include=ipv4_split_include,
            split_include_service=split_include_service,
            ipv4_name=ipv4_name,
            ipv6_start_ip=ipv6_start_ip,
            ipv6_end_ip=ipv6_end_ip,
            ipv6_prefix=ipv6_prefix,
            ipv6_dns_server1=ipv6_dns_server1,
            ipv6_dns_server2=ipv6_dns_server2,
            ipv6_dns_server3=ipv6_dns_server3,
            ipv6_exclude_range=ipv6_exclude_range,
            ipv6_split_include=ipv6_split_include,
            ipv6_name=ipv6_name,
            ip_delay_interval=ip_delay_interval,
            unity_support=unity_support,
            domain=domain,
            banner=banner,
            include_local_lan=include_local_lan,
            ipv4_split_exclude=ipv4_split_exclude,
            ipv6_split_exclude=ipv6_split_exclude,
            save_password=save_password,
            client_auto_negotiate=client_auto_negotiate,
            client_keep_alive=client_keep_alive,
            backup_gateway=backup_gateway,
            proposal=proposal,
            add_route=add_route,
            add_gw_route=add_gw_route,
            psksecret=psksecret,
            psksecret_remote=psksecret_remote,
            keepalive=keepalive,
            distance=distance,
            priority=priority,
            localid=localid,
            localid_type=localid_type,
            auto_negotiate=auto_negotiate,
            negotiate_timeout=negotiate_timeout,
            fragmentation=fragmentation,
            ip_fragmentation=ip_fragmentation,
            dpd=dpd,
            dpd_retrycount=dpd_retrycount,
            dpd_retryinterval=dpd_retryinterval,
            comments=comments,
            npu_offload=npu_offload,
            send_cert_chain=send_cert_chain,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            suite_b=suite_b,
            eap=eap,
            eap_identity=eap_identity,
            eap_exclude_peergrp=eap_exclude_peergrp,
            eap_cert_auth=eap_cert_auth,
            acct_verify=acct_verify,
            ppk=ppk,
            ppk_secret=ppk_secret,
            ppk_identity=ppk_identity,
            wizard_type=wizard_type,
            xauthtype=xauthtype,
            reauth=reauth,
            authusr=authusr,
            authpasswd=authpasswd,
            group_authentication=group_authentication,
            group_authentication_secret=group_authentication_secret,
            authusrgrp=authusrgrp,
            mesh_selector_type=mesh_selector_type,
            idle_timeout=idle_timeout,
            shared_idle_timeout=shared_idle_timeout,
            idle_timeoutinterval=idle_timeoutinterval,
            ha_sync_esp_seqno=ha_sync_esp_seqno,
            fgsp_sync=fgsp_sync,
            inbound_dscp_copy=inbound_dscp_copy,
            auto_discovery_sender=auto_discovery_sender,
            auto_discovery_receiver=auto_discovery_receiver,
            auto_discovery_forwarder=auto_discovery_forwarder,
            auto_discovery_psk=auto_discovery_psk,
            auto_discovery_shortcuts=auto_discovery_shortcuts,
            auto_discovery_crossover=auto_discovery_crossover,
            auto_discovery_offer_interval=auto_discovery_offer_interval,
            auto_discovery_dialup_placeholder=auto_discovery_dialup_placeholder,
            encapsulation=encapsulation,
            encapsulation_address=encapsulation_address,
            encap_local_gw4=encap_local_gw4,
            encap_local_gw6=encap_local_gw6,
            encap_remote_gw4=encap_remote_gw4,
            encap_remote_gw6=encap_remote_gw6,
            vni=vni,
            nattraversal=nattraversal,
            esn=esn,
            fragmentation_mtu=fragmentation_mtu,
            childless_ike=childless_ike,
            azure_ad_autoconnect=azure_ad_autoconnect,
            client_resume=client_resume,
            client_resume_interval=client_resume_interval,
            rekey=rekey,
            digital_signature_auth=digital_signature_auth,
            signature_hash_alg=signature_hash_alg,
            rsa_signature_format=rsa_signature_format,
            rsa_signature_hash_override=rsa_signature_hash_override,
            enforce_unique_id=enforce_unique_id,
            cert_id_validation=cert_id_validation,
            fec_egress=fec_egress,
            fec_send_timeout=fec_send_timeout,
            fec_base=fec_base,
            fec_codec=fec_codec,
            fec_redundant=fec_redundant,
            fec_ingress=fec_ingress,
            fec_receive_timeout=fec_receive_timeout,
            fec_health_check=fec_health_check,
            fec_mapping_profile=fec_mapping_profile,
            network_overlay=network_overlay,
            network_id=network_id,
            dev_id_notification=dev_id_notification,
            dev_id=dev_id,
            loopback_asymroute=loopback_asymroute,
            link_cost=link_cost,
            kms=kms,
            exchange_fgt_device_id=exchange_fgt_device_id,
            ipv6_auto_linklocal=ipv6_auto_linklocal,
            ems_sn_check=ems_sn_check,
            cert_trust_store=cert_trust_store,
            qkd=qkd,
            qkd_hybrid=qkd_hybrid,
            qkd_profile=qkd_profile,
            transport=transport,
            fortinet_esp=fortinet_esp,
            auto_transport_threshold=auto_transport_threshold,
            remote_gw_match=remote_gw_match,
            remote_gw_subnet=remote_gw_subnet,
            remote_gw_start_ip=remote_gw_start_ip,
            remote_gw_end_ip=remote_gw_end_ip,
            remote_gw_country=remote_gw_country,
            remote_gw_ztna_tags=remote_gw_ztna_tags,
            remote_gw6_match=remote_gw6_match,
            remote_gw6_subnet=remote_gw6_subnet,
            remote_gw6_start_ip=remote_gw6_start_ip,
            remote_gw6_end_ip=remote_gw6_end_ip,
            remote_gw6_country=remote_gw6_country,
            cert_peer_username_validation=cert_peer_username_validation,
            cert_peer_username_strip=cert_peer_username_strip,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.phase1_interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase1_interface",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/vpn.ipsec/phase1-interface/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        type: str | None = None,
        interface: str | None = None,
        ip_version: str | None = None,
        ike_version: str | None = None,
        local_gw: str | None = None,
        local_gw6: str | None = None,
        remote_gw: str | None = None,
        remote_gw6: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list | None = None,
        authmethod: str | None = None,
        authmethod_remote: str | None = None,
        mode: str | None = None,
        peertype: str | None = None,
        peerid: str | None = None,
        default_gw: str | None = None,
        default_gw_priority: int | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        monitor: str | list | None = None,
        monitor_min: int | None = None,
        monitor_hold_down_type: str | None = None,
        monitor_hold_down_delay: int | None = None,
        monitor_hold_down_weekday: str | None = None,
        monitor_hold_down_time: str | None = None,
        net_device: str | None = None,
        passive_mode: str | None = None,
        exchange_interface_ip: str | None = None,
        exchange_ip_addr4: str | None = None,
        exchange_ip_addr6: str | None = None,
        aggregate_member: str | None = None,
        aggregate_weight: int | None = None,
        packet_redistribution: str | None = None,
        peer_egress_shaping: str | None = None,
        peer_egress_shaping_value: int | None = None,
        mode_cfg: str | None = None,
        mode_cfg_allow_client_selector: str | None = None,
        assign_ip: str | None = None,
        assign_ip_from: str | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: str | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: str | list | None = None,
        dns_suffix_search: str | list | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: str | list | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: str | list | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: str | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: str | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: str | None = None,
        client_auto_negotiate: str | None = None,
        client_keep_alive: str | None = None,
        backup_gateway: str | list | None = None,
        proposal: str | list | None = None,
        add_route: str | None = None,
        add_gw_route: str | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: str | None = None,
        auto_negotiate: str | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: str | None = None,
        ip_fragmentation: str | None = None,
        dpd: str | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: str | None = None,
        send_cert_chain: str | None = None,
        dhgrp: str | list | None = None,
        addke1: str | list | None = None,
        addke2: str | list | None = None,
        addke3: str | list | None = None,
        addke4: str | list | None = None,
        addke5: str | list | None = None,
        addke6: str | list | None = None,
        addke7: str | list | None = None,
        suite_b: str | None = None,
        eap: str | None = None,
        eap_identity: str | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: str | None = None,
        acct_verify: str | None = None,
        ppk: str | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: str | None = None,
        xauthtype: str | None = None,
        reauth: str | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: str | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: str | None = None,
        idle_timeout: str | None = None,
        shared_idle_timeout: str | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: str | None = None,
        fgsp_sync: str | None = None,
        inbound_dscp_copy: str | None = None,
        auto_discovery_sender: str | None = None,
        auto_discovery_receiver: str | None = None,
        auto_discovery_forwarder: str | None = None,
        auto_discovery_psk: str | None = None,
        auto_discovery_shortcuts: str | None = None,
        auto_discovery_crossover: str | None = None,
        auto_discovery_offer_interval: int | None = None,
        auto_discovery_dialup_placeholder: str | None = None,
        encapsulation: str | None = None,
        encapsulation_address: str | None = None,
        encap_local_gw4: str | None = None,
        encap_local_gw6: str | None = None,
        encap_remote_gw4: str | None = None,
        encap_remote_gw6: str | None = None,
        vni: int | None = None,
        nattraversal: str | None = None,
        esn: str | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: str | None = None,
        azure_ad_autoconnect: str | None = None,
        client_resume: str | None = None,
        client_resume_interval: int | None = None,
        rekey: str | None = None,
        digital_signature_auth: str | None = None,
        signature_hash_alg: str | list | None = None,
        rsa_signature_format: str | None = None,
        rsa_signature_hash_override: str | None = None,
        enforce_unique_id: str | None = None,
        cert_id_validation: str | None = None,
        fec_egress: str | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: str | None = None,
        fec_redundant: int | None = None,
        fec_ingress: str | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: str | None = None,
        network_id: int | None = None,
        dev_id_notification: str | None = None,
        dev_id: str | None = None,
        loopback_asymroute: str | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: str | None = None,
        ipv6_auto_linklocal: str | None = None,
        ems_sn_check: str | None = None,
        cert_trust_store: str | None = None,
        qkd: str | None = None,
        qkd_hybrid: str | None = None,
        qkd_profile: str | None = None,
        transport: str | None = None,
        fortinet_esp: str | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: str | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list | None = None,
        remote_gw6_match: str | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: str | None = None,
        cert_peer_username_strip: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new vpn/ipsec/phase1_interface object.

        Configure VPN remote gateway.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IPsec remote gateway name.
            type: Remote gateway type.
            interface: Local physical, aggregate, or VLAN outgoing interface.
            ip_version: IP version to use for VPN interface.
            ike_version: IKE protocol version.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Phase1Interface.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Phase1Interface.required_fields()) }}
            
            Use Phase1Interface.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            type=type,
            interface=interface,
            ip_version=ip_version,
            ike_version=ike_version,
            local_gw=local_gw,
            local_gw6=local_gw6,
            remote_gw=remote_gw,
            remote_gw6=remote_gw6,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            default_gw=default_gw,
            default_gw_priority=default_gw_priority,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
            monitor=monitor,
            monitor_min=monitor_min,
            monitor_hold_down_type=monitor_hold_down_type,
            monitor_hold_down_delay=monitor_hold_down_delay,
            monitor_hold_down_weekday=monitor_hold_down_weekday,
            monitor_hold_down_time=monitor_hold_down_time,
            net_device=net_device,
            passive_mode=passive_mode,
            exchange_interface_ip=exchange_interface_ip,
            exchange_ip_addr4=exchange_ip_addr4,
            exchange_ip_addr6=exchange_ip_addr6,
            aggregate_member=aggregate_member,
            aggregate_weight=aggregate_weight,
            packet_redistribution=packet_redistribution,
            peer_egress_shaping=peer_egress_shaping,
            peer_egress_shaping_value=peer_egress_shaping_value,
            mode_cfg=mode_cfg,
            mode_cfg_allow_client_selector=mode_cfg_allow_client_selector,
            assign_ip=assign_ip,
            assign_ip_from=assign_ip_from,
            ipv4_start_ip=ipv4_start_ip,
            ipv4_end_ip=ipv4_end_ip,
            ipv4_netmask=ipv4_netmask,
            dhcp_ra_giaddr=dhcp_ra_giaddr,
            dhcp6_ra_linkaddr=dhcp6_ra_linkaddr,
            dns_mode=dns_mode,
            ipv4_dns_server1=ipv4_dns_server1,
            ipv4_dns_server2=ipv4_dns_server2,
            ipv4_dns_server3=ipv4_dns_server3,
            internal_domain_list=internal_domain_list,
            dns_suffix_search=dns_suffix_search,
            ipv4_wins_server1=ipv4_wins_server1,
            ipv4_wins_server2=ipv4_wins_server2,
            ipv4_exclude_range=ipv4_exclude_range,
            ipv4_split_include=ipv4_split_include,
            split_include_service=split_include_service,
            ipv4_name=ipv4_name,
            ipv6_start_ip=ipv6_start_ip,
            ipv6_end_ip=ipv6_end_ip,
            ipv6_prefix=ipv6_prefix,
            ipv6_dns_server1=ipv6_dns_server1,
            ipv6_dns_server2=ipv6_dns_server2,
            ipv6_dns_server3=ipv6_dns_server3,
            ipv6_exclude_range=ipv6_exclude_range,
            ipv6_split_include=ipv6_split_include,
            ipv6_name=ipv6_name,
            ip_delay_interval=ip_delay_interval,
            unity_support=unity_support,
            domain=domain,
            banner=banner,
            include_local_lan=include_local_lan,
            ipv4_split_exclude=ipv4_split_exclude,
            ipv6_split_exclude=ipv6_split_exclude,
            save_password=save_password,
            client_auto_negotiate=client_auto_negotiate,
            client_keep_alive=client_keep_alive,
            backup_gateway=backup_gateway,
            proposal=proposal,
            add_route=add_route,
            add_gw_route=add_gw_route,
            psksecret=psksecret,
            psksecret_remote=psksecret_remote,
            keepalive=keepalive,
            distance=distance,
            priority=priority,
            localid=localid,
            localid_type=localid_type,
            auto_negotiate=auto_negotiate,
            negotiate_timeout=negotiate_timeout,
            fragmentation=fragmentation,
            ip_fragmentation=ip_fragmentation,
            dpd=dpd,
            dpd_retrycount=dpd_retrycount,
            dpd_retryinterval=dpd_retryinterval,
            comments=comments,
            npu_offload=npu_offload,
            send_cert_chain=send_cert_chain,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            suite_b=suite_b,
            eap=eap,
            eap_identity=eap_identity,
            eap_exclude_peergrp=eap_exclude_peergrp,
            eap_cert_auth=eap_cert_auth,
            acct_verify=acct_verify,
            ppk=ppk,
            ppk_secret=ppk_secret,
            ppk_identity=ppk_identity,
            wizard_type=wizard_type,
            xauthtype=xauthtype,
            reauth=reauth,
            authusr=authusr,
            authpasswd=authpasswd,
            group_authentication=group_authentication,
            group_authentication_secret=group_authentication_secret,
            authusrgrp=authusrgrp,
            mesh_selector_type=mesh_selector_type,
            idle_timeout=idle_timeout,
            shared_idle_timeout=shared_idle_timeout,
            idle_timeoutinterval=idle_timeoutinterval,
            ha_sync_esp_seqno=ha_sync_esp_seqno,
            fgsp_sync=fgsp_sync,
            inbound_dscp_copy=inbound_dscp_copy,
            auto_discovery_sender=auto_discovery_sender,
            auto_discovery_receiver=auto_discovery_receiver,
            auto_discovery_forwarder=auto_discovery_forwarder,
            auto_discovery_psk=auto_discovery_psk,
            auto_discovery_shortcuts=auto_discovery_shortcuts,
            auto_discovery_crossover=auto_discovery_crossover,
            auto_discovery_offer_interval=auto_discovery_offer_interval,
            auto_discovery_dialup_placeholder=auto_discovery_dialup_placeholder,
            encapsulation=encapsulation,
            encapsulation_address=encapsulation_address,
            encap_local_gw4=encap_local_gw4,
            encap_local_gw6=encap_local_gw6,
            encap_remote_gw4=encap_remote_gw4,
            encap_remote_gw6=encap_remote_gw6,
            vni=vni,
            nattraversal=nattraversal,
            esn=esn,
            fragmentation_mtu=fragmentation_mtu,
            childless_ike=childless_ike,
            azure_ad_autoconnect=azure_ad_autoconnect,
            client_resume=client_resume,
            client_resume_interval=client_resume_interval,
            rekey=rekey,
            digital_signature_auth=digital_signature_auth,
            signature_hash_alg=signature_hash_alg,
            rsa_signature_format=rsa_signature_format,
            rsa_signature_hash_override=rsa_signature_hash_override,
            enforce_unique_id=enforce_unique_id,
            cert_id_validation=cert_id_validation,
            fec_egress=fec_egress,
            fec_send_timeout=fec_send_timeout,
            fec_base=fec_base,
            fec_codec=fec_codec,
            fec_redundant=fec_redundant,
            fec_ingress=fec_ingress,
            fec_receive_timeout=fec_receive_timeout,
            fec_health_check=fec_health_check,
            fec_mapping_profile=fec_mapping_profile,
            network_overlay=network_overlay,
            network_id=network_id,
            dev_id_notification=dev_id_notification,
            dev_id=dev_id,
            loopback_asymroute=loopback_asymroute,
            link_cost=link_cost,
            kms=kms,
            exchange_fgt_device_id=exchange_fgt_device_id,
            ipv6_auto_linklocal=ipv6_auto_linklocal,
            ems_sn_check=ems_sn_check,
            cert_trust_store=cert_trust_store,
            qkd=qkd,
            qkd_hybrid=qkd_hybrid,
            qkd_profile=qkd_profile,
            transport=transport,
            fortinet_esp=fortinet_esp,
            auto_transport_threshold=auto_transport_threshold,
            remote_gw_match=remote_gw_match,
            remote_gw_subnet=remote_gw_subnet,
            remote_gw_start_ip=remote_gw_start_ip,
            remote_gw_end_ip=remote_gw_end_ip,
            remote_gw_country=remote_gw_country,
            remote_gw_ztna_tags=remote_gw_ztna_tags,
            remote_gw6_match=remote_gw6_match,
            remote_gw6_subnet=remote_gw6_subnet,
            remote_gw6_start_ip=remote_gw6_start_ip,
            remote_gw6_end_ip=remote_gw6_end_ip,
            remote_gw6_country=remote_gw6_country,
            cert_peer_username_validation=cert_peer_username_validation,
            cert_peer_username_strip=cert_peer_username_strip,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.phase1_interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase1_interface",
            )

        endpoint = "/vpn.ipsec/phase1-interface"
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
        Delete vpn/ipsec/phase1_interface object.

        Configure VPN remote gateway.

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/vpn.ipsec/phase1-interface/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if vpn/ipsec/phase1_interface object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.vpn_ipsec_phase1_interface.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.vpn_ipsec_phase1_interface.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase1_interface.delete(name=1)

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
        Create or update vpn/ipsec/phase1_interface object (intelligent operation).

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1_interface.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.vpn_ipsec_phase1_interface.set(payload_dict=obj_data)
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


