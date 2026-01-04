"""
FortiOS CMDB - Vpn ipsec_phase1

Configuration endpoint for managing cmdb vpn/ipsec_phase1 objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec_phase1
    POST   /cmdb/vpn/ipsec_phase1
    PUT    /cmdb/vpn/ipsec_phase1/{identifier}
    DELETE /cmdb/vpn/ipsec_phase1/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_ipsec_phase1.get()

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


class IpsecPhase1:
    """IpsecPhase1 Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize IpsecPhase1 endpoint."""
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
        Retrieve vpn/ipsec_phase1 configuration.

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
            >>> # Get all vpn/ipsec_phase1 objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec_phase1 by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase1.get(action="schema")

        See Also:
            - post(): Create new vpn/ipsec_phase1 object
            - put(): Update existing vpn/ipsec_phase1 object
            - delete(): Remove vpn/ipsec_phase1 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/vpn.ipsec/phase1/" + str(name)
        else:
            endpoint = "/vpn.ipsec/phase1"
        
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
        ike_version: str | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list | None = None,
        authmethod: str | None = None,
        authmethod_remote: str | None = None,
        mode: str | None = None,
        peertype: str | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
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
        proposal: str | None = None,
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
        dpd: str | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: str | None = None,
        send_cert_chain: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
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
        nattraversal: str | None = None,
        esn: str | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: str | None = None,
        azure_ad_autoconnect: str | None = None,
        client_resume: str | None = None,
        client_resume_interval: int | None = None,
        rekey: str | None = None,
        digital_signature_auth: str | None = None,
        signature_hash_alg: str | None = None,
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
        Update existing vpn/ipsec_phase1 object.

        Configure VPN remote gateway.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IPsec remote gateway name.
            type: Remote gateway type.
            interface: Local physical, aggregate, or VLAN outgoing interface.
            ike_version: IKE protocol version.
            remote_gw: Remote VPN gateway.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.put(payload_dict=payload)

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
            ike_version=ike_version,
            remote_gw=remote_gw,
            local_gw=local_gw,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
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
        from ._helpers.ipsec_phase1 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec_phase1",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/vpn.ipsec/phase1/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        type: str | None = None,
        interface: str | None = None,
        ike_version: str | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list | None = None,
        authmethod: str | None = None,
        authmethod_remote: str | None = None,
        mode: str | None = None,
        peertype: str | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
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
        proposal: str | None = None,
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
        dpd: str | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: str | None = None,
        send_cert_chain: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
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
        nattraversal: str | None = None,
        esn: str | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: str | None = None,
        azure_ad_autoconnect: str | None = None,
        client_resume: str | None = None,
        client_resume_interval: int | None = None,
        rekey: str | None = None,
        digital_signature_auth: str | None = None,
        signature_hash_alg: str | None = None,
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
        Create new vpn/ipsec_phase1 object.

        Configure VPN remote gateway.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IPsec remote gateway name.
            type: Remote gateway type.
            interface: Local physical, aggregate, or VLAN outgoing interface.
            ike_version: IKE protocol version.
            remote_gw: Remote VPN gateway.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = IpsecPhase1.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(IpsecPhase1.required_fields()) }}
            
            Use IpsecPhase1.help('field_name') to get field details.

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
            ike_version=ike_version,
            remote_gw=remote_gw,
            local_gw=local_gw,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
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
        from ._helpers.ipsec_phase1 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec_phase1",
            )

        endpoint = "/vpn.ipsec/phase1"
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
        Delete vpn/ipsec_phase1 object.

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/vpn.ipsec/phase1/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if vpn/ipsec_phase1 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.vpn_ipsec_phase1.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.vpn_ipsec_phase1.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase1.delete(name=1)

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
        Create or update vpn/ipsec_phase1 object (intelligent operation).

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.vpn_ipsec_phase1.set(payload_dict=obj_data)
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
            >>> print(IpsecPhase1.help())
            
            >>> # Get field information
            >>> print(IpsecPhase1.help("name"))
        """
        from ._helpers.ipsec_phase1 import (
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
            >>> fields = IpsecPhase1.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = IpsecPhase1.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.ipsec_phase1 import get_all_fields, get_field_metadata

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
            >>> info = IpsecPhase1.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.ipsec_phase1 import get_field_metadata

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
            >>> is_valid, error = IpsecPhase1.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.ipsec_phase1 import validate_field_value

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
            >>> required = IpsecPhase1.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.ipsec_phase1 import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = IpsecPhase1.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.ipsec_phase1 import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = IpsecPhase1.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.ipsec_phase1 import get_schema_info

        return get_schema_info()
