"""
FortiOS CMDB - Firewall policy

Configuration endpoint for managing cmdb firewall/policy objects.

API Endpoints:
    GET    /cmdb/firewall/policy
    POST   /cmdb/firewall/policy
    PUT    /cmdb/firewall/policy/{identifier}
    DELETE /cmdb/firewall/policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_policy.get()

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


class Policy(MetadataMixin):
    """Policy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "policy"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Policy endpoint."""
        self._client = client

    def get(
        self,
        policyid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve firewall/policy configuration.

        Configure IPv4/IPv6 policies.

        Args:
            policyid: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/policy objects
            >>> result = fgt.api.cmdb.firewall_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/policy by policyid
            >>> result = fgt.api.cmdb.firewall_policy.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_policy.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_policy.get(action="schema")

        See Also:
            - post(): Create new firewall/policy object
            - put(): Update existing firewall/policy object
            - delete(): Remove firewall/policy object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if policyid:
            endpoint = "/firewall/policy/" + str(policyid)
        else:
            endpoint = "/firewall/policy"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        policyid: int | None = None,
        status: str | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        action: str | None = None,
        nat64: str | None = None,
        nat46: str | None = None,
        ztna_status: str | None = None,
        ztna_device_ownership: str | None = None,
        srcaddr: str | list | None = None,
        dstaddr: str | list | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        ztna_ems_tag: str | list | None = None,
        ztna_ems_tag_secondary: str | list | None = None,
        ztna_tags_match_logic: str | None = None,
        ztna_geo_tag: str | list | None = None,
        internet_service: str | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        network_service_dynamic: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: str | list | None = None,
        internet_service_src_group: str | list | None = None,
        internet_service_src_custom: str | list | None = None,
        network_service_src_dynamic: str | list | None = None,
        internet_service_src_custom_group: str | list | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: str | None = None,
        src_vendor_mac: str | list | None = None,
        internet_service6: str | None = None,
        internet_service6_name: str | list | None = None,
        internet_service6_group: str | list | None = None,
        internet_service6_custom: str | list | None = None,
        internet_service6_custom_group: str | list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: str | list | None = None,
        internet_service6_src_group: str | list | None = None,
        internet_service6_src_custom: str | list | None = None,
        internet_service6_src_custom_group: str | list | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: str | None = None,
        rtp_nat: str | None = None,
        rtp_addr: str | list | None = None,
        send_deny_packet: str | None = None,
        firewall_session_dirty: str | None = None,
        schedule: str | None = None,
        schedule_timeout: str | None = None,
        policy_expiry: str | None = None,
        policy_expiry_date: Any | None = None,
        policy_expiry_date_utc: str | None = None,
        service: str | list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        anti_replay: str | None = None,
        tcp_session_without_syn: str | None = None,
        geoip_anycast: str | None = None,
        geoip_match: str | None = None,
        dynamic_shaping: str | None = None,
        passive_wan_health_measurement: str | None = None,
        app_monitor: str | None = None,
        utm_status: str | None = None,
        inspection_mode: str | None = None,
        http_policy_redirect: str | None = None,
        ssh_policy_redirect: str | None = None,
        ztna_policy_redirect: str | None = None,
        webproxy_profile: str | None = None,
        profile_type: str | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: str | None = None,
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        capture_packet: str | None = None,
        auto_asic_offload: str | None = None,
        wanopt: str | None = None,
        wanopt_detection: str | None = None,
        wanopt_passive_opt: str | None = None,
        wanopt_profile: str | None = None,
        wanopt_peer: str | None = None,
        webcache: str | None = None,
        webcache_https: str | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: str | None = None,
        pcp_outbound: str | None = None,
        pcp_inbound: str | None = None,
        pcp_poolname: str | list | None = None,
        permit_any_host: str | None = None,
        permit_stun_host: str | None = None,
        fixedport: str | None = None,
        port_preserve: str | None = None,
        port_random: str | None = None,
        ippool: str | None = None,
        poolname: str | list | None = None,
        poolname6: str | list | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: str | None = None,
        outbound: str | None = None,
        natinbound: str | None = None,
        natoutbound: str | None = None,
        fec: str | None = None,
        wccp: str | None = None,
        ntlm: str | None = None,
        ntlm_guest: str | None = None,
        ntlm_enabled_browsers: str | list | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: str | list | None = None,
        users: str | list | None = None,
        fsso_groups: str | list | None = None,
        auth_path: str | None = None,
        disclaimer: str | None = None,
        email_collect: str | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: str | None = None,
        match_vip_only: str | None = None,
        diffserv_copy: str | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: str | None = None,
        custom_log_fields: str | list | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: str | None = None,
        srcaddr6_negate: str | None = None,
        dstaddr_negate: str | None = None,
        dstaddr6_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_src_negate: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_src_negate: str | None = None,
        timeout_send_rst: str | None = None,
        captive_portal_exempt: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: str | None = None,
        radius_mac_auth_bypass: str | None = None,
        radius_ip_auth_bypass: str | None = None,
        delay_tcp_npu_session: str | None = None,
        vlan_filter: str | None = None,
        sgt_check: str | None = None,
        sgt: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service_src_fortiguard: str | list | None = None,
        internet_service6_fortiguard: str | list | None = None,
        internet_service6_src_fortiguard: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/policy object.

        Configure IPv4/IPv6 policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            policyid: Policy ID (0 - 4294967294).
            status: Enable or disable this policy.
            name: Policy name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            srcintf: Incoming (ingress) interface.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_policy.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            action=action,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            wanopt=wanopt,
            wanopt_detection=wanopt_detection,
            wanopt_passive_opt=wanopt_passive_opt,
            wanopt_profile=wanopt_profile,
            wanopt_peer=wanopt_peer,
            webcache=webcache,
            webcache_https=webcache_https,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/policy",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/policy/" + str(policyid_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        policyid: int | None = None,
        status: str | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        action: str | None = None,
        nat64: str | None = None,
        nat46: str | None = None,
        ztna_status: str | None = None,
        ztna_device_ownership: str | None = None,
        srcaddr: str | list | None = None,
        dstaddr: str | list | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        ztna_ems_tag: str | list | None = None,
        ztna_ems_tag_secondary: str | list | None = None,
        ztna_tags_match_logic: str | None = None,
        ztna_geo_tag: str | list | None = None,
        internet_service: str | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        network_service_dynamic: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: str | list | None = None,
        internet_service_src_group: str | list | None = None,
        internet_service_src_custom: str | list | None = None,
        network_service_src_dynamic: str | list | None = None,
        internet_service_src_custom_group: str | list | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: str | None = None,
        src_vendor_mac: str | list | None = None,
        internet_service6: str | None = None,
        internet_service6_name: str | list | None = None,
        internet_service6_group: str | list | None = None,
        internet_service6_custom: str | list | None = None,
        internet_service6_custom_group: str | list | None = None,
        internet_service6_src: str | None = None,
        internet_service6_src_name: str | list | None = None,
        internet_service6_src_group: str | list | None = None,
        internet_service6_src_custom: str | list | None = None,
        internet_service6_src_custom_group: str | list | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: str | None = None,
        rtp_nat: str | None = None,
        rtp_addr: str | list | None = None,
        send_deny_packet: str | None = None,
        firewall_session_dirty: str | None = None,
        schedule: str | None = None,
        schedule_timeout: str | None = None,
        policy_expiry: str | None = None,
        policy_expiry_date: Any | None = None,
        policy_expiry_date_utc: str | None = None,
        service: str | list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        anti_replay: str | None = None,
        tcp_session_without_syn: str | None = None,
        geoip_anycast: str | None = None,
        geoip_match: str | None = None,
        dynamic_shaping: str | None = None,
        passive_wan_health_measurement: str | None = None,
        app_monitor: str | None = None,
        utm_status: str | None = None,
        inspection_mode: str | None = None,
        http_policy_redirect: str | None = None,
        ssh_policy_redirect: str | None = None,
        ztna_policy_redirect: str | None = None,
        webproxy_profile: str | None = None,
        profile_type: str | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: str | None = None,
        logtraffic_start: str | None = None,
        log_http_transaction: str | None = None,
        capture_packet: str | None = None,
        auto_asic_offload: str | None = None,
        wanopt: str | None = None,
        wanopt_detection: str | None = None,
        wanopt_passive_opt: str | None = None,
        wanopt_profile: str | None = None,
        wanopt_peer: str | None = None,
        webcache: str | None = None,
        webcache_https: str | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: str | None = None,
        pcp_outbound: str | None = None,
        pcp_inbound: str | None = None,
        pcp_poolname: str | list | None = None,
        permit_any_host: str | None = None,
        permit_stun_host: str | None = None,
        fixedport: str | None = None,
        port_preserve: str | None = None,
        port_random: str | None = None,
        ippool: str | None = None,
        poolname: str | list | None = None,
        poolname6: str | list | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: str | None = None,
        outbound: str | None = None,
        natinbound: str | None = None,
        natoutbound: str | None = None,
        fec: str | None = None,
        wccp: str | None = None,
        ntlm: str | None = None,
        ntlm_guest: str | None = None,
        ntlm_enabled_browsers: str | list | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: str | list | None = None,
        users: str | list | None = None,
        fsso_groups: str | list | None = None,
        auth_path: str | None = None,
        disclaimer: str | None = None,
        email_collect: str | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: str | None = None,
        match_vip_only: str | None = None,
        diffserv_copy: str | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: str | None = None,
        custom_log_fields: str | list | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: str | None = None,
        srcaddr6_negate: str | None = None,
        dstaddr_negate: str | None = None,
        dstaddr6_negate: str | None = None,
        ztna_ems_tag_negate: str | None = None,
        service_negate: str | None = None,
        internet_service_negate: str | None = None,
        internet_service_src_negate: str | None = None,
        internet_service6_negate: str | None = None,
        internet_service6_src_negate: str | None = None,
        timeout_send_rst: str | None = None,
        captive_portal_exempt: str | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: str | None = None,
        radius_mac_auth_bypass: str | None = None,
        radius_ip_auth_bypass: str | None = None,
        delay_tcp_npu_session: str | None = None,
        vlan_filter: str | None = None,
        sgt_check: str | None = None,
        sgt: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service_src_fortiguard: str | list | None = None,
        internet_service6_fortiguard: str | list | None = None,
        internet_service6_src_fortiguard: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/policy object.

        Configure IPv4/IPv6 policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            policyid: Policy ID (0 - 4294967294).
            status: Enable or disable this policy.
            name: Policy name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            srcintf: Incoming (ingress) interface.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned policyid.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Policy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Policy.required_fields()) }}
            
            Use Policy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            action=action,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            wanopt=wanopt,
            wanopt_detection=wanopt_detection,
            wanopt_passive_opt=wanopt_passive_opt,
            wanopt_profile=wanopt_profile,
            wanopt_peer=wanopt_peer,
            webcache=webcache,
            webcache_https=webcache_https,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/policy",
            )

        endpoint = "/firewall/policy"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        policyid: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/policy object.

        Configure IPv4/IPv6 policies.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If policyid is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_policy.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/policy/" + str(policyid)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_policy.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_policy.delete(policyid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(policyid=policyid, vdom=vdom, raw_json=True)
            
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
        Create or update firewall/policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (policyid) in the payload.

        Args:
            payload_dict: Resource data including policyid (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_policy.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("policyid")
        if not mkey_value:
            raise ValueError("policyid is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(policyid=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


