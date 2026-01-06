"""
FortiOS CMDB - Vpn ipsec phase1

Configuration endpoint for managing cmdb vpn/ipsec/phase1 objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec/phase1
    POST   /cmdb/vpn/ipsec/phase1
    PUT    /cmdb/vpn/ipsec/phase1/{identifier}
    DELETE /cmdb/vpn/ipsec/phase1/{identifier}

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


class Phase1(MetadataMixin):
    """Phase1 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "phase1"
    
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
        """Initialize Phase1 endpoint."""
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
        Retrieve vpn/ipsec/phase1 configuration.

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
            >>> # Get all vpn/ipsec/phase1 objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec/phase1 by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase1.get(action="schema")

        See Also:
            - post(): Create new vpn/ipsec/phase1 object
            - put(): Update existing vpn/ipsec/phase1 object
            - delete(): Remove vpn/ipsec/phase1 object
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
        type: Literal["static", "dynamic", "ddns"] | None = None,
        interface: str | None = None,
        ike_version: Literal["1", "2"] | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list | None = None,
        authmethod: Literal["psk", "signature"] | None = None,
        authmethod_remote: Literal["psk", "signature"] | None = None,
        mode: Literal["aggressive", "main"] | None = None,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: Literal["disable", "enable"] | None = None,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = None,
        assign_ip: Literal["disable", "enable"] | None = None,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: Literal["manual", "auto"] | None = None,
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
        unity_support: Literal["disable", "enable"] | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: Literal["disable", "enable"] | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: Literal["disable", "enable"] | None = None,
        client_auto_negotiate: Literal["disable", "enable"] | None = None,
        client_keep_alive: Literal["disable", "enable"] | None = None,
        backup_gateway: str | list | None = None,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list | None = None,
        add_route: Literal["disable", "enable"] | None = None,
        add_gw_route: Literal["enable", "disable"] | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: Literal["enable", "disable"] | None = None,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: Literal["enable", "disable"] | None = None,
        send_cert_chain: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = None,
        eap: Literal["enable", "disable"] | None = None,
        eap_identity: Literal["use-id-payload", "send-request"] | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: Literal["enable", "disable"] | None = None,
        acct_verify: Literal["enable", "disable"] | None = None,
        ppk: Literal["disable", "allow", "require"] | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = None,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = None,
        reauth: Literal["disable", "enable"] | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: Literal["enable", "disable"] | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = None,
        idle_timeout: Literal["enable", "disable"] | None = None,
        shared_idle_timeout: Literal["enable", "disable"] | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = None,
        fgsp_sync: Literal["enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["enable", "disable"] | None = None,
        nattraversal: Literal["enable", "disable", "forced"] | None = None,
        esn: Literal["require", "allow", "disable"] | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: Literal["enable", "disable"] | None = None,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = None,
        client_resume: Literal["enable", "disable"] | None = None,
        client_resume_interval: int | None = None,
        rekey: Literal["enable", "disable"] | None = None,
        digital_signature_auth: Literal["enable", "disable"] | None = None,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list | None = None,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = None,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = None,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = None,
        cert_id_validation: Literal["enable", "disable"] | None = None,
        fec_egress: Literal["enable", "disable"] | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: Literal["rs", "xor"] | None = None,
        fec_redundant: int | None = None,
        fec_ingress: Literal["enable", "disable"] | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: Literal["disable", "enable"] | None = None,
        network_id: int | None = None,
        dev_id_notification: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        loopback_asymroute: Literal["enable", "disable"] | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = None,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = None,
        ems_sn_check: Literal["enable", "disable"] | None = None,
        cert_trust_store: Literal["local", "ems"] | None = None,
        qkd: Literal["disable", "allow", "require"] | None = None,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = None,
        qkd_profile: str | None = None,
        transport: Literal["udp", "auto", "tcp"] | None = None,
        fortinet_esp: Literal["enable", "disable"] | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list | None = None,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = None,
        cert_peer_username_strip: Literal["disable", "enable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/ipsec/phase1 object.

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
        from ._helpers.phase1 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase1",
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
        type: Literal["static", "dynamic", "ddns"] | None = None,
        interface: str | None = None,
        ike_version: Literal["1", "2"] | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list | None = None,
        authmethod: Literal["psk", "signature"] | None = None,
        authmethod_remote: Literal["psk", "signature"] | None = None,
        mode: Literal["aggressive", "main"] | None = None,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: Literal["disable", "enable"] | None = None,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = None,
        assign_ip: Literal["disable", "enable"] | None = None,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: Literal["manual", "auto"] | None = None,
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
        unity_support: Literal["disable", "enable"] | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: Literal["disable", "enable"] | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: Literal["disable", "enable"] | None = None,
        client_auto_negotiate: Literal["disable", "enable"] | None = None,
        client_keep_alive: Literal["disable", "enable"] | None = None,
        backup_gateway: str | list | None = None,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list | None = None,
        add_route: Literal["disable", "enable"] | None = None,
        add_gw_route: Literal["enable", "disable"] | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: Literal["enable", "disable"] | None = None,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: Literal["enable", "disable"] | None = None,
        send_cert_chain: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list | None = None,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = None,
        eap: Literal["enable", "disable"] | None = None,
        eap_identity: Literal["use-id-payload", "send-request"] | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: Literal["enable", "disable"] | None = None,
        acct_verify: Literal["enable", "disable"] | None = None,
        ppk: Literal["disable", "allow", "require"] | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = None,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = None,
        reauth: Literal["disable", "enable"] | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: Literal["enable", "disable"] | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = None,
        idle_timeout: Literal["enable", "disable"] | None = None,
        shared_idle_timeout: Literal["enable", "disable"] | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = None,
        fgsp_sync: Literal["enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["enable", "disable"] | None = None,
        nattraversal: Literal["enable", "disable", "forced"] | None = None,
        esn: Literal["require", "allow", "disable"] | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: Literal["enable", "disable"] | None = None,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = None,
        client_resume: Literal["enable", "disable"] | None = None,
        client_resume_interval: int | None = None,
        rekey: Literal["enable", "disable"] | None = None,
        digital_signature_auth: Literal["enable", "disable"] | None = None,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list | None = None,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = None,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = None,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = None,
        cert_id_validation: Literal["enable", "disable"] | None = None,
        fec_egress: Literal["enable", "disable"] | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: Literal["rs", "xor"] | None = None,
        fec_redundant: int | None = None,
        fec_ingress: Literal["enable", "disable"] | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: Literal["disable", "enable"] | None = None,
        network_id: int | None = None,
        dev_id_notification: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        loopback_asymroute: Literal["enable", "disable"] | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = None,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = None,
        ems_sn_check: Literal["enable", "disable"] | None = None,
        cert_trust_store: Literal["local", "ems"] | None = None,
        qkd: Literal["disable", "allow", "require"] | None = None,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = None,
        qkd_profile: str | None = None,
        transport: Literal["udp", "auto", "tcp"] | None = None,
        fortinet_esp: Literal["enable", "disable"] | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list | None = None,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = None,
        cert_peer_username_strip: Literal["disable", "enable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new vpn/ipsec/phase1 object.

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
            >>> payload = Phase1.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Phase1.required_fields()) }}
            
            Use Phase1.help('field_name') to get field details.

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
        from ._helpers.phase1 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase1",
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
        Delete vpn/ipsec/phase1 object.

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
        Check if vpn/ipsec/phase1 object exists.

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
        Create or update vpn/ipsec/phase1 object (intelligent operation).

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
        Move vpn/ipsec/phase1 object to a new position.
        
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
            >>> fgt.api.cmdb.vpn_ipsec_phase1.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/vpn.ipsec/phase1",
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
        Clone vpn/ipsec/phase1 object.
        
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
            >>> fgt.api.cmdb.vpn_ipsec_phase1.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/vpn.ipsec/phase1",
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
        Check if vpn/ipsec/phase1 object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.vpn_ipsec_phase1.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase1.post(payload_dict=data)
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

