"""
FortiOS CMDB - Wireless_controller vap

Configuration endpoint for managing cmdb wireless_controller/vap objects.

API Endpoints:
    GET    /cmdb/wireless_controller/vap
    POST   /cmdb/wireless_controller/vap
    PUT    /cmdb/wireless_controller/vap/{identifier}
    DELETE /cmdb/wireless_controller/vap/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_vap.get()

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


class Vap:
    """Vap Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vap endpoint."""
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
        Retrieve wireless_controller/vap configuration.

        Configure Virtual Access Points (VAPs).

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
            >>> # Get all wireless_controller/vap objects
            >>> result = fgt.api.cmdb.wireless_controller_vap.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/vap by name
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_vap.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/vap object
            - put(): Update existing wireless_controller/vap object
            - delete(): Remove wireless_controller/vap object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/wireless-controller/vap/" + str(name)
        else:
            endpoint = "/wireless-controller/vap"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        pre_auth: str | None = None,
        external_pre_auth: str | None = None,
        mesh_backhaul: str | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: str | None = None,
        security: str | None = None,
        pmf: str | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: str | None = None,
        okc: str | None = None,
        mbo: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: str | None = None,
        x80211k: str | None = None,
        x80211v: str | None = None,
        neighbor_report_dual_band: str | None = None,
        fast_bss_transition: str | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: str | None = None,
        sae_groups: str | None = None,
        owe_groups: str | None = None,
        owe_transition: str | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: str | None = None,
        eapol_key_retries: str | None = None,
        tkip_counter_measure: str | None = None,
        external_web: str | None = None,
        external_web_format: str | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_calling_station_delimiter: str | None = None,
        mac_called_station_delimiter: str | None = None,
        mac_case: str | None = None,
        called_station_id_type: str | None = None,
        mac_auth_bypass: str | None = None,
        radius_mac_auth: str | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: str | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list | None = None,
        auth: str | None = None,
        encrypt: str | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: str | None = None,
        sae_hnp_only: str | None = None,
        sae_pk: str | None = None,
        sae_private_key: str | None = None,
        akm24_only: str | None = None,
        radius_server: str | None = None,
        nas_filter_rule: str | None = None,
        domain_name_stripping: str | None = None,
        local_standalone: str | None = None,
        local_standalone_nat: str | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: str | None = None,
        local_standalone_dns_ip: str | None = None,
        local_lan_partition: str | None = None,
        local_bridging: str | None = None,
        local_lan: str | None = None,
        local_authentication: str | None = None,
        usergroup: str | list | None = None,
        captive_portal: str | None = None,
        captive_network_assistant_bypass: str | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: str | None = None,
        selected_usergroups: str | list | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: str | None = None,
        schedule: str | list | None = None,
        ldpc: str | None = None,
        high_efficiency: str | None = None,
        target_wake_time: str | None = None,
        port_macauth: str | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: str | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: str | None = None,
        nac: str | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: str | None = None,
        dynamic_vlan: str | None = None,
        captive_portal_fw_accounting: str | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: str | None = None,
        multicast_enhance: str | None = None,
        igmp_snooping: str | None = None,
        dhcp_address_enforcement: str | None = None,
        broadcast_suppression: str | None = None,
        ipv6_rules: str | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: str | None = None,
        probe_resp_suppression: str | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: str | None = None,
        quarantine: str | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list | None = None,
        vlan_pooling: str | None = None,
        vlan_pool: str | list | None = None,
        dhcp_option43_insertion: str | None = None,
        dhcp_option82_insertion: str | None = None,
        dhcp_option82_circuit_id_insertion: str | None = None,
        dhcp_option82_remote_id_insertion: str | None = None,
        ptk_rekey: str | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: str | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: str | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: str | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: str | None = None,
        rates_11bg: str | None = None,
        rates_11n_ss12: str | None = None,
        rates_11n_ss34: str | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: str | None = None,
        utm_log: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: str | None = None,
        address_group: str | None = None,
        address_group_policy: str | None = None,
        sticky_client_remove: str | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: str | None = None,
        beacon_advertising: str | None = None,
        osen: str | None = None,
        application_detection_engine: str | None = None,
        application_dscp_marking: str | None = None,
        application_report_intv: int | None = None,
        l3_roaming: str | None = None,
        l3_roaming_mode: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Virtual AP name.
            pre_auth: Enable/disable pre-authentication, where supported by clients (default = enable).
            external_pre_auth: Enable/disable pre-authentication with external APs not managed by the FortiGate (default = disable).
            mesh_backhaul: Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open.
            atf_weight: Airtime weight in percentage (default = 20).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_vap.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_vap.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            pre_auth=pre_auth,
            external_pre_auth=external_pre_auth,
            mesh_backhaul=mesh_backhaul,
            atf_weight=atf_weight,
            max_clients=max_clients,
            max_clients_ap=max_clients_ap,
            ssid=ssid,
            broadcast_ssid=broadcast_ssid,
            security=security,
            pmf=pmf,
            pmf_assoc_comeback_timeout=pmf_assoc_comeback_timeout,
            pmf_sa_query_retry_timeout=pmf_sa_query_retry_timeout,
            beacon_protection=beacon_protection,
            okc=okc,
            mbo=mbo,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            mbo_cell_data_conn_pref=mbo_cell_data_conn_pref,
            x80211k=x80211k,
            x80211v=x80211v,
            neighbor_report_dual_band=neighbor_report_dual_band,
            fast_bss_transition=fast_bss_transition,
            ft_mobility_domain=ft_mobility_domain,
            ft_r0_key_lifetime=ft_r0_key_lifetime,
            ft_over_ds=ft_over_ds,
            sae_groups=sae_groups,
            owe_groups=owe_groups,
            owe_transition=owe_transition,
            owe_transition_ssid=owe_transition_ssid,
            additional_akms=additional_akms,
            eapol_key_retries=eapol_key_retries,
            tkip_counter_measure=tkip_counter_measure,
            external_web=external_web,
            external_web_format=external_web_format,
            external_logout=external_logout,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_calling_station_delimiter=mac_calling_station_delimiter,
            mac_called_station_delimiter=mac_called_station_delimiter,
            mac_case=mac_case,
            called_station_id_type=called_station_id_type,
            mac_auth_bypass=mac_auth_bypass,
            radius_mac_auth=radius_mac_auth,
            radius_mac_auth_server=radius_mac_auth_server,
            radius_mac_auth_block_interval=radius_mac_auth_block_interval,
            radius_mac_mpsk_auth=radius_mac_mpsk_auth,
            radius_mac_mpsk_timeout=radius_mac_mpsk_timeout,
            radius_mac_auth_usergroups=radius_mac_auth_usergroups,
            auth=auth,
            encrypt=encrypt,
            keyindex=keyindex,
            key=key,
            passphrase=passphrase,
            sae_password=sae_password,
            sae_h2e_only=sae_h2e_only,
            sae_hnp_only=sae_hnp_only,
            sae_pk=sae_pk,
            sae_private_key=sae_private_key,
            akm24_only=akm24_only,
            radius_server=radius_server,
            nas_filter_rule=nas_filter_rule,
            domain_name_stripping=domain_name_stripping,
            local_standalone=local_standalone,
            local_standalone_nat=local_standalone_nat,
            ip=ip,
            dhcp_lease_time=dhcp_lease_time,
            local_standalone_dns=local_standalone_dns,
            local_standalone_dns_ip=local_standalone_dns_ip,
            local_lan_partition=local_lan_partition,
            local_bridging=local_bridging,
            local_lan=local_lan,
            local_authentication=local_authentication,
            usergroup=usergroup,
            captive_portal=captive_portal,
            captive_network_assistant_bypass=captive_network_assistant_bypass,
            portal_message_override_group=portal_message_override_group,
            portal_message_overrides=portal_message_overrides,
            portal_type=portal_type,
            selected_usergroups=selected_usergroups,
            security_exempt_list=security_exempt_list,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            intra_vap_privacy=intra_vap_privacy,
            schedule=schedule,
            ldpc=ldpc,
            high_efficiency=high_efficiency,
            target_wake_time=target_wake_time,
            port_macauth=port_macauth,
            port_macauth_timeout=port_macauth_timeout,
            port_macauth_reauth_timeout=port_macauth_reauth_timeout,
            bss_color_partial=bss_color_partial,
            mpsk_profile=mpsk_profile,
            split_tunneling=split_tunneling,
            nac=nac,
            nac_profile=nac_profile,
            vlanid=vlanid,
            vlan_auto=vlan_auto,
            dynamic_vlan=dynamic_vlan,
            captive_portal_fw_accounting=captive_portal_fw_accounting,
            captive_portal_ac_name=captive_portal_ac_name,
            captive_portal_auth_timeout=captive_portal_auth_timeout,
            multicast_rate=multicast_rate,
            multicast_enhance=multicast_enhance,
            igmp_snooping=igmp_snooping,
            dhcp_address_enforcement=dhcp_address_enforcement,
            broadcast_suppression=broadcast_suppression,
            ipv6_rules=ipv6_rules,
            me_disable_thresh=me_disable_thresh,
            mu_mimo=mu_mimo,
            probe_resp_suppression=probe_resp_suppression,
            probe_resp_threshold=probe_resp_threshold,
            radio_sensitivity=radio_sensitivity,
            quarantine=quarantine,
            radio_5g_threshold=radio_5g_threshold,
            radio_2g_threshold=radio_2g_threshold,
            vlan_name=vlan_name,
            vlan_pooling=vlan_pooling,
            vlan_pool=vlan_pool,
            dhcp_option43_insertion=dhcp_option43_insertion,
            dhcp_option82_insertion=dhcp_option82_insertion,
            dhcp_option82_circuit_id_insertion=dhcp_option82_circuit_id_insertion,
            dhcp_option82_remote_id_insertion=dhcp_option82_remote_id_insertion,
            ptk_rekey=ptk_rekey,
            ptk_rekey_intv=ptk_rekey_intv,
            gtk_rekey=gtk_rekey,
            gtk_rekey_intv=gtk_rekey_intv,
            eap_reauth=eap_reauth,
            eap_reauth_intv=eap_reauth_intv,
            roaming_acct_interim_update=roaming_acct_interim_update,
            qos_profile=qos_profile,
            hotspot20_profile=hotspot20_profile,
            access_control_list=access_control_list,
            primary_wag_profile=primary_wag_profile,
            secondary_wag_profile=secondary_wag_profile,
            tunnel_echo_interval=tunnel_echo_interval,
            tunnel_fallback_interval=tunnel_fallback_interval,
            rates_11a=rates_11a,
            rates_11bg=rates_11bg,
            rates_11n_ss12=rates_11n_ss12,
            rates_11n_ss34=rates_11n_ss34,
            rates_11ac_mcs_map=rates_11ac_mcs_map,
            rates_11ax_mcs_map=rates_11ax_mcs_map,
            rates_11be_mcs_map=rates_11be_mcs_map,
            rates_11be_mcs_map_160=rates_11be_mcs_map_160,
            rates_11be_mcs_map_320=rates_11be_mcs_map_320,
            utm_profile=utm_profile,
            utm_status=utm_status,
            utm_log=utm_log,
            ips_sensor=ips_sensor,
            application_list=application_list,
            antivirus_profile=antivirus_profile,
            webfilter_profile=webfilter_profile,
            scan_botnet_connections=scan_botnet_connections,
            address_group=address_group,
            address_group_policy=address_group_policy,
            sticky_client_remove=sticky_client_remove,
            sticky_client_threshold_5g=sticky_client_threshold_5g,
            sticky_client_threshold_2g=sticky_client_threshold_2g,
            sticky_client_threshold_6g=sticky_client_threshold_6g,
            bstm_rssi_disassoc_timer=bstm_rssi_disassoc_timer,
            bstm_load_balancing_disassoc_timer=bstm_load_balancing_disassoc_timer,
            bstm_disassociation_imminent=bstm_disassociation_imminent,
            beacon_advertising=beacon_advertising,
            osen=osen,
            application_detection_engine=application_detection_engine,
            application_dscp_marking=application_dscp_marking,
            application_report_intv=application_report_intv,
            l3_roaming=l3_roaming,
            l3_roaming_mode=l3_roaming_mode,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vap import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/vap",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/vap/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        pre_auth: str | None = None,
        external_pre_auth: str | None = None,
        mesh_backhaul: str | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: str | None = None,
        security: str | None = None,
        pmf: str | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: str | None = None,
        okc: str | None = None,
        mbo: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: str | None = None,
        x80211k: str | None = None,
        x80211v: str | None = None,
        neighbor_report_dual_band: str | None = None,
        fast_bss_transition: str | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: str | None = None,
        sae_groups: str | None = None,
        owe_groups: str | None = None,
        owe_transition: str | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: str | None = None,
        eapol_key_retries: str | None = None,
        tkip_counter_measure: str | None = None,
        external_web: str | None = None,
        external_web_format: str | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_calling_station_delimiter: str | None = None,
        mac_called_station_delimiter: str | None = None,
        mac_case: str | None = None,
        called_station_id_type: str | None = None,
        mac_auth_bypass: str | None = None,
        radius_mac_auth: str | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: str | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list | None = None,
        auth: str | None = None,
        encrypt: str | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: str | None = None,
        sae_hnp_only: str | None = None,
        sae_pk: str | None = None,
        sae_private_key: str | None = None,
        akm24_only: str | None = None,
        radius_server: str | None = None,
        nas_filter_rule: str | None = None,
        domain_name_stripping: str | None = None,
        local_standalone: str | None = None,
        local_standalone_nat: str | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: str | None = None,
        local_standalone_dns_ip: str | None = None,
        local_lan_partition: str | None = None,
        local_bridging: str | None = None,
        local_lan: str | None = None,
        local_authentication: str | None = None,
        usergroup: str | list | None = None,
        captive_portal: str | None = None,
        captive_network_assistant_bypass: str | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: str | None = None,
        selected_usergroups: str | list | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: str | None = None,
        schedule: str | list | None = None,
        ldpc: str | None = None,
        high_efficiency: str | None = None,
        target_wake_time: str | None = None,
        port_macauth: str | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: str | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: str | None = None,
        nac: str | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: str | None = None,
        dynamic_vlan: str | None = None,
        captive_portal_fw_accounting: str | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: str | None = None,
        multicast_enhance: str | None = None,
        igmp_snooping: str | None = None,
        dhcp_address_enforcement: str | None = None,
        broadcast_suppression: str | None = None,
        ipv6_rules: str | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: str | None = None,
        probe_resp_suppression: str | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: str | None = None,
        quarantine: str | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list | None = None,
        vlan_pooling: str | None = None,
        vlan_pool: str | list | None = None,
        dhcp_option43_insertion: str | None = None,
        dhcp_option82_insertion: str | None = None,
        dhcp_option82_circuit_id_insertion: str | None = None,
        dhcp_option82_remote_id_insertion: str | None = None,
        ptk_rekey: str | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: str | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: str | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: str | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: str | None = None,
        rates_11bg: str | None = None,
        rates_11n_ss12: str | None = None,
        rates_11n_ss34: str | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: str | None = None,
        utm_log: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: str | None = None,
        address_group: str | None = None,
        address_group_policy: str | None = None,
        sticky_client_remove: str | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: str | None = None,
        beacon_advertising: str | None = None,
        osen: str | None = None,
        application_detection_engine: str | None = None,
        application_dscp_marking: str | None = None,
        application_report_intv: int | None = None,
        l3_roaming: str | None = None,
        l3_roaming_mode: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Virtual AP name.
            pre_auth: Enable/disable pre-authentication, where supported by clients (default = enable).
            external_pre_auth: Enable/disable pre-authentication with external APs not managed by the FortiGate (default = disable).
            mesh_backhaul: Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open.
            atf_weight: Airtime weight in percentage (default = 20).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_vap.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Vap.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_vap.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Vap.required_fields()) }}
            
            Use Vap.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            pre_auth=pre_auth,
            external_pre_auth=external_pre_auth,
            mesh_backhaul=mesh_backhaul,
            atf_weight=atf_weight,
            max_clients=max_clients,
            max_clients_ap=max_clients_ap,
            ssid=ssid,
            broadcast_ssid=broadcast_ssid,
            security=security,
            pmf=pmf,
            pmf_assoc_comeback_timeout=pmf_assoc_comeback_timeout,
            pmf_sa_query_retry_timeout=pmf_sa_query_retry_timeout,
            beacon_protection=beacon_protection,
            okc=okc,
            mbo=mbo,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            mbo_cell_data_conn_pref=mbo_cell_data_conn_pref,
            x80211k=x80211k,
            x80211v=x80211v,
            neighbor_report_dual_band=neighbor_report_dual_band,
            fast_bss_transition=fast_bss_transition,
            ft_mobility_domain=ft_mobility_domain,
            ft_r0_key_lifetime=ft_r0_key_lifetime,
            ft_over_ds=ft_over_ds,
            sae_groups=sae_groups,
            owe_groups=owe_groups,
            owe_transition=owe_transition,
            owe_transition_ssid=owe_transition_ssid,
            additional_akms=additional_akms,
            eapol_key_retries=eapol_key_retries,
            tkip_counter_measure=tkip_counter_measure,
            external_web=external_web,
            external_web_format=external_web_format,
            external_logout=external_logout,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_calling_station_delimiter=mac_calling_station_delimiter,
            mac_called_station_delimiter=mac_called_station_delimiter,
            mac_case=mac_case,
            called_station_id_type=called_station_id_type,
            mac_auth_bypass=mac_auth_bypass,
            radius_mac_auth=radius_mac_auth,
            radius_mac_auth_server=radius_mac_auth_server,
            radius_mac_auth_block_interval=radius_mac_auth_block_interval,
            radius_mac_mpsk_auth=radius_mac_mpsk_auth,
            radius_mac_mpsk_timeout=radius_mac_mpsk_timeout,
            radius_mac_auth_usergroups=radius_mac_auth_usergroups,
            auth=auth,
            encrypt=encrypt,
            keyindex=keyindex,
            key=key,
            passphrase=passphrase,
            sae_password=sae_password,
            sae_h2e_only=sae_h2e_only,
            sae_hnp_only=sae_hnp_only,
            sae_pk=sae_pk,
            sae_private_key=sae_private_key,
            akm24_only=akm24_only,
            radius_server=radius_server,
            nas_filter_rule=nas_filter_rule,
            domain_name_stripping=domain_name_stripping,
            local_standalone=local_standalone,
            local_standalone_nat=local_standalone_nat,
            ip=ip,
            dhcp_lease_time=dhcp_lease_time,
            local_standalone_dns=local_standalone_dns,
            local_standalone_dns_ip=local_standalone_dns_ip,
            local_lan_partition=local_lan_partition,
            local_bridging=local_bridging,
            local_lan=local_lan,
            local_authentication=local_authentication,
            usergroup=usergroup,
            captive_portal=captive_portal,
            captive_network_assistant_bypass=captive_network_assistant_bypass,
            portal_message_override_group=portal_message_override_group,
            portal_message_overrides=portal_message_overrides,
            portal_type=portal_type,
            selected_usergroups=selected_usergroups,
            security_exempt_list=security_exempt_list,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            intra_vap_privacy=intra_vap_privacy,
            schedule=schedule,
            ldpc=ldpc,
            high_efficiency=high_efficiency,
            target_wake_time=target_wake_time,
            port_macauth=port_macauth,
            port_macauth_timeout=port_macauth_timeout,
            port_macauth_reauth_timeout=port_macauth_reauth_timeout,
            bss_color_partial=bss_color_partial,
            mpsk_profile=mpsk_profile,
            split_tunneling=split_tunneling,
            nac=nac,
            nac_profile=nac_profile,
            vlanid=vlanid,
            vlan_auto=vlan_auto,
            dynamic_vlan=dynamic_vlan,
            captive_portal_fw_accounting=captive_portal_fw_accounting,
            captive_portal_ac_name=captive_portal_ac_name,
            captive_portal_auth_timeout=captive_portal_auth_timeout,
            multicast_rate=multicast_rate,
            multicast_enhance=multicast_enhance,
            igmp_snooping=igmp_snooping,
            dhcp_address_enforcement=dhcp_address_enforcement,
            broadcast_suppression=broadcast_suppression,
            ipv6_rules=ipv6_rules,
            me_disable_thresh=me_disable_thresh,
            mu_mimo=mu_mimo,
            probe_resp_suppression=probe_resp_suppression,
            probe_resp_threshold=probe_resp_threshold,
            radio_sensitivity=radio_sensitivity,
            quarantine=quarantine,
            radio_5g_threshold=radio_5g_threshold,
            radio_2g_threshold=radio_2g_threshold,
            vlan_name=vlan_name,
            vlan_pooling=vlan_pooling,
            vlan_pool=vlan_pool,
            dhcp_option43_insertion=dhcp_option43_insertion,
            dhcp_option82_insertion=dhcp_option82_insertion,
            dhcp_option82_circuit_id_insertion=dhcp_option82_circuit_id_insertion,
            dhcp_option82_remote_id_insertion=dhcp_option82_remote_id_insertion,
            ptk_rekey=ptk_rekey,
            ptk_rekey_intv=ptk_rekey_intv,
            gtk_rekey=gtk_rekey,
            gtk_rekey_intv=gtk_rekey_intv,
            eap_reauth=eap_reauth,
            eap_reauth_intv=eap_reauth_intv,
            roaming_acct_interim_update=roaming_acct_interim_update,
            qos_profile=qos_profile,
            hotspot20_profile=hotspot20_profile,
            access_control_list=access_control_list,
            primary_wag_profile=primary_wag_profile,
            secondary_wag_profile=secondary_wag_profile,
            tunnel_echo_interval=tunnel_echo_interval,
            tunnel_fallback_interval=tunnel_fallback_interval,
            rates_11a=rates_11a,
            rates_11bg=rates_11bg,
            rates_11n_ss12=rates_11n_ss12,
            rates_11n_ss34=rates_11n_ss34,
            rates_11ac_mcs_map=rates_11ac_mcs_map,
            rates_11ax_mcs_map=rates_11ax_mcs_map,
            rates_11be_mcs_map=rates_11be_mcs_map,
            rates_11be_mcs_map_160=rates_11be_mcs_map_160,
            rates_11be_mcs_map_320=rates_11be_mcs_map_320,
            utm_profile=utm_profile,
            utm_status=utm_status,
            utm_log=utm_log,
            ips_sensor=ips_sensor,
            application_list=application_list,
            antivirus_profile=antivirus_profile,
            webfilter_profile=webfilter_profile,
            scan_botnet_connections=scan_botnet_connections,
            address_group=address_group,
            address_group_policy=address_group_policy,
            sticky_client_remove=sticky_client_remove,
            sticky_client_threshold_5g=sticky_client_threshold_5g,
            sticky_client_threshold_2g=sticky_client_threshold_2g,
            sticky_client_threshold_6g=sticky_client_threshold_6g,
            bstm_rssi_disassoc_timer=bstm_rssi_disassoc_timer,
            bstm_load_balancing_disassoc_timer=bstm_load_balancing_disassoc_timer,
            bstm_disassociation_imminent=bstm_disassociation_imminent,
            beacon_advertising=beacon_advertising,
            osen=osen,
            application_detection_engine=application_detection_engine,
            application_dscp_marking=application_dscp_marking,
            application_report_intv=application_report_intv,
            l3_roaming=l3_roaming,
            l3_roaming_mode=l3_roaming_mode,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.vap import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/vap",
            )

        endpoint = "/wireless-controller/vap"
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
        Delete wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

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
            >>> result = fgt.api.cmdb.wireless_controller_vap.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/vap/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/vap object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_vap.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_vap.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_vap.delete(name=1)

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
        Create or update wireless_controller/vap object (intelligent operation).

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
            >>> result = fgt.api.cmdb.wireless_controller_vap.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_vap.set(payload_dict=obj_data)
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
            >>> print(Vap.help())
            
            >>> # Get field information
            >>> print(Vap.help("name"))
        """
        from ._helpers.vap import (
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
            >>> fields = Vap.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Vap.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.vap import get_all_fields, get_field_metadata

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
            >>> info = Vap.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.vap import get_field_metadata

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
            >>> is_valid, error = Vap.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.vap import validate_field_value

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
            >>> required = Vap.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.vap import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Vap.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.vap import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Vap.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.vap import get_schema_info

        return get_schema_info()
