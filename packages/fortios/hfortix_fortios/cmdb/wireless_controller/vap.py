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
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.wireless_controller_vap.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, Literal
if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Vap(CRUDEndpoint, MetadataMixin):
    """Vap Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vap"
    
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
        """Initialize Vap endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve wireless_controller/vap configuration.

        Configure Virtual Access Points (VAPs).

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
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
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
            >>> # Get all wireless_controller/vap objects
            >>> result = fgt.api.cmdb.wireless_controller_vap.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/vap by name
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_vap.get_schema()

        See Also:
            - post(): Create new wireless_controller/vap object
            - put(): Update existing wireless_controller/vap object
            - delete(): Remove wireless_controller/vap object
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
            endpoint = "/wireless-controller/vap/" + str(name)
        else:
            endpoint = "/wireless-controller/vap"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json, response_mode=response_mode
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
            >>> schema = fgt.api.cmdb.wireless_controller_vap.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_vap.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        pre_auth: Literal["enable", "disable"] | None = None,
        external_pre_auth: Literal["enable", "disable"] | None = None,
        mesh_backhaul: Literal["enable", "disable"] | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: Literal["enable", "disable"] | None = None,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = None,
        pmf: Literal["disable", "enable", "optional"] | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: Literal["disable", "enable"] | None = None,
        okc: Literal["disable", "enable"] | None = None,
        mbo: Literal["disable", "enable"] | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = None,
        x80211k: Literal["disable", "enable"] | None = None,
        x80211v: Literal["disable", "enable"] | None = None,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = None,
        fast_bss_transition: Literal["disable", "enable"] | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: Literal["disable", "enable"] | None = None,
        sae_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_transition: Literal["disable", "enable"] | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: Literal["akm6", "akm24"] | list[str] | list[dict[str, Any]] | None = None,
        eapol_key_retries: Literal["disable", "enable"] | None = None,
        tkip_counter_measure: Literal["enable", "disable"] | None = None,
        external_web: str | None = None,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_case: Literal["uppercase", "lowercase"] | None = None,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = None,
        mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_mac_auth: Literal["enable", "disable"] | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        auth: Literal["radius", "usergroup"] | None = None,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: Literal["enable", "disable"] | None = None,
        sae_hnp_only: Literal["enable", "disable"] | None = None,
        sae_pk: Literal["enable", "disable"] | None = None,
        sae_private_key: str | None = None,
        akm24_only: Literal["disable", "enable"] | None = None,
        radius_server: str | None = None,
        nas_filter_rule: Literal["enable", "disable"] | None = None,
        domain_name_stripping: Literal["disable", "enable"] | None = None,
        mlo: Literal["disable", "enable"] | None = None,
        local_standalone: Literal["enable", "disable"] | None = None,
        local_standalone_nat: Literal["enable", "disable"] | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: Literal["enable", "disable"] | None = None,
        local_standalone_dns_ip: str | list[str] | list[dict[str, Any]] | None = None,
        local_lan_partition: Literal["enable", "disable"] | None = None,
        local_bridging: Literal["enable", "disable"] | None = None,
        local_lan: Literal["allow", "deny"] | None = None,
        local_authentication: Literal["enable", "disable"] | None = None,
        usergroup: str | list[str] | list[dict[str, Any]] | None = None,
        captive_portal: Literal["enable", "disable"] | None = None,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = None,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: Literal["enable", "disable"] | None = None,
        schedule: str | list[str] | list[dict[str, Any]] | None = None,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = None,
        high_efficiency: Literal["enable", "disable"] | None = None,
        target_wake_time: Literal["enable", "disable"] | None = None,
        port_macauth: Literal["disable", "radius", "address-group"] | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: Literal["enable", "disable"] | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: Literal["enable", "disable"] | None = None,
        nac: Literal["enable", "disable"] | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: Literal["enable", "disable"] | None = None,
        dynamic_vlan: Literal["enable", "disable"] | None = None,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = None,
        multicast_enhance: Literal["enable", "disable"] | None = None,
        igmp_snooping: Literal["enable", "disable"] | None = None,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = None,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | list[dict[str, Any]] | None = None,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | list[dict[str, Any]] | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: Literal["enable", "disable"] | None = None,
        probe_resp_suppression: Literal["enable", "disable"] | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: Literal["enable", "disable"] | None = None,
        quarantine: Literal["enable", "disable"] | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = None,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = None,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = None,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = None,
        ptk_rekey: Literal["enable", "disable"] | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: Literal["enable", "disable"] | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: Literal["enable", "disable"] | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        utm_log: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = None,
        address_group: str | None = None,
        address_group_policy: Literal["disable", "allow", "deny"] | None = None,
        sticky_client_remove: Literal["enable", "disable"] | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = None,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | list[dict[str, Any]] | None = None,
        osen: Literal["enable", "disable"] | None = None,
        application_detection_engine: Literal["enable", "disable"] | None = None,
        application_dscp_marking: Literal["enable", "disable"] | None = None,
        application_report_intv: int | None = None,
        l3_roaming: Literal["enable", "disable"] | None = None,
        l3_roaming_mode: Literal["direct", "indirect"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
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
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
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
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
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
            mlo=mlo,
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
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
        )

    # ========================================================================
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        pre_auth: Literal["enable", "disable"] | None = None,
        external_pre_auth: Literal["enable", "disable"] | None = None,
        mesh_backhaul: Literal["enable", "disable"] | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: Literal["enable", "disable"] | None = None,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = None,
        pmf: Literal["disable", "enable", "optional"] | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: Literal["disable", "enable"] | None = None,
        okc: Literal["disable", "enable"] | None = None,
        mbo: Literal["disable", "enable"] | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = None,
        x80211k: Literal["disable", "enable"] | None = None,
        x80211v: Literal["disable", "enable"] | None = None,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = None,
        fast_bss_transition: Literal["disable", "enable"] | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: Literal["disable", "enable"] | None = None,
        sae_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_transition: Literal["disable", "enable"] | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: Literal["akm6", "akm24"] | list[str] | list[dict[str, Any]] | None = None,
        eapol_key_retries: Literal["disable", "enable"] | None = None,
        tkip_counter_measure: Literal["enable", "disable"] | None = None,
        external_web: str | None = None,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_case: Literal["uppercase", "lowercase"] | None = None,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = None,
        mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_mac_auth: Literal["enable", "disable"] | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        auth: Literal["radius", "usergroup"] | None = None,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: Literal["enable", "disable"] | None = None,
        sae_hnp_only: Literal["enable", "disable"] | None = None,
        sae_pk: Literal["enable", "disable"] | None = None,
        sae_private_key: str | None = None,
        akm24_only: Literal["disable", "enable"] | None = None,
        radius_server: str | None = None,
        nas_filter_rule: Literal["enable", "disable"] | None = None,
        domain_name_stripping: Literal["disable", "enable"] | None = None,
        mlo: Literal["disable", "enable"] | None = None,
        local_standalone: Literal["enable", "disable"] | None = None,
        local_standalone_nat: Literal["enable", "disable"] | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: Literal["enable", "disable"] | None = None,
        local_standalone_dns_ip: str | list[str] | list[dict[str, Any]] | None = None,
        local_lan_partition: Literal["enable", "disable"] | None = None,
        local_bridging: Literal["enable", "disable"] | None = None,
        local_lan: Literal["allow", "deny"] | None = None,
        local_authentication: Literal["enable", "disable"] | None = None,
        usergroup: str | list[str] | list[dict[str, Any]] | None = None,
        captive_portal: Literal["enable", "disable"] | None = None,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = None,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: Literal["enable", "disable"] | None = None,
        schedule: str | list[str] | list[dict[str, Any]] | None = None,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = None,
        high_efficiency: Literal["enable", "disable"] | None = None,
        target_wake_time: Literal["enable", "disable"] | None = None,
        port_macauth: Literal["disable", "radius", "address-group"] | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: Literal["enable", "disable"] | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: Literal["enable", "disable"] | None = None,
        nac: Literal["enable", "disable"] | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: Literal["enable", "disable"] | None = None,
        dynamic_vlan: Literal["enable", "disable"] | None = None,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = None,
        multicast_enhance: Literal["enable", "disable"] | None = None,
        igmp_snooping: Literal["enable", "disable"] | None = None,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = None,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | list[dict[str, Any]] | None = None,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | list[dict[str, Any]] | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: Literal["enable", "disable"] | None = None,
        probe_resp_suppression: Literal["enable", "disable"] | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: Literal["enable", "disable"] | None = None,
        quarantine: Literal["enable", "disable"] | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = None,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = None,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = None,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = None,
        ptk_rekey: Literal["enable", "disable"] | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: Literal["enable", "disable"] | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: Literal["enable", "disable"] | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        utm_log: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = None,
        address_group: str | None = None,
        address_group_policy: Literal["disable", "allow", "deny"] | None = None,
        sticky_client_remove: Literal["enable", "disable"] | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = None,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | list[dict[str, Any]] | None = None,
        osen: Literal["enable", "disable"] | None = None,
        application_detection_engine: Literal["enable", "disable"] | None = None,
        application_dscp_marking: Literal["enable", "disable"] | None = None,
        application_report_intv: int | None = None,
        l3_roaming: Literal["enable", "disable"] | None = None,
        l3_roaming_mode: Literal["direct", "indirect"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
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
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
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
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
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
            mlo=mlo,
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
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Delete wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            response_mode: Override client-level response_mode. "dict" returns dict, "object" returns FortiObject.
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
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
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
        name: str | None = None,
        pre_auth: Literal["enable", "disable"] | None = None,
        external_pre_auth: Literal["enable", "disable"] | None = None,
        mesh_backhaul: Literal["enable", "disable"] | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: Literal["enable", "disable"] | None = None,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = None,
        pmf: Literal["disable", "enable", "optional"] | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: Literal["disable", "enable"] | None = None,
        okc: Literal["disable", "enable"] | None = None,
        mbo: Literal["disable", "enable"] | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = None,
        x80211k: Literal["disable", "enable"] | None = None,
        x80211v: Literal["disable", "enable"] | None = None,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = None,
        fast_bss_transition: Literal["disable", "enable"] | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: Literal["disable", "enable"] | None = None,
        sae_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_transition: Literal["disable", "enable"] | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: Literal["akm6", "akm24"] | list[str] | list[dict[str, Any]] | None = None,
        eapol_key_retries: Literal["disable", "enable"] | None = None,
        tkip_counter_measure: Literal["enable", "disable"] | None = None,
        external_web: str | None = None,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_case: Literal["uppercase", "lowercase"] | None = None,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = None,
        mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_mac_auth: Literal["enable", "disable"] | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        auth: Literal["radius", "usergroup"] | None = None,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: Literal["enable", "disable"] | None = None,
        sae_hnp_only: Literal["enable", "disable"] | None = None,
        sae_pk: Literal["enable", "disable"] | None = None,
        sae_private_key: str | None = None,
        akm24_only: Literal["disable", "enable"] | None = None,
        radius_server: str | None = None,
        nas_filter_rule: Literal["enable", "disable"] | None = None,
        domain_name_stripping: Literal["disable", "enable"] | None = None,
        mlo: Literal["disable", "enable"] | None = None,
        local_standalone: Literal["enable", "disable"] | None = None,
        local_standalone_nat: Literal["enable", "disable"] | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: Literal["enable", "disable"] | None = None,
        local_standalone_dns_ip: str | list[str] | list[dict[str, Any]] | None = None,
        local_lan_partition: Literal["enable", "disable"] | None = None,
        local_bridging: Literal["enable", "disable"] | None = None,
        local_lan: Literal["allow", "deny"] | None = None,
        local_authentication: Literal["enable", "disable"] | None = None,
        usergroup: str | list[str] | list[dict[str, Any]] | None = None,
        captive_portal: Literal["enable", "disable"] | None = None,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = None,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: Literal["enable", "disable"] | None = None,
        schedule: str | list[str] | list[dict[str, Any]] | None = None,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = None,
        high_efficiency: Literal["enable", "disable"] | None = None,
        target_wake_time: Literal["enable", "disable"] | None = None,
        port_macauth: Literal["disable", "radius", "address-group"] | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: Literal["enable", "disable"] | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: Literal["enable", "disable"] | None = None,
        nac: Literal["enable", "disable"] | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: Literal["enable", "disable"] | None = None,
        dynamic_vlan: Literal["enable", "disable"] | None = None,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = None,
        multicast_enhance: Literal["enable", "disable"] | None = None,
        igmp_snooping: Literal["enable", "disable"] | None = None,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = None,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | list[dict[str, Any]] | None = None,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | list[dict[str, Any]] | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: Literal["enable", "disable"] | None = None,
        probe_resp_suppression: Literal["enable", "disable"] | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: Literal["enable", "disable"] | None = None,
        quarantine: Literal["enable", "disable"] | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = None,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = None,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = None,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = None,
        ptk_rekey: Literal["enable", "disable"] | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: Literal["enable", "disable"] | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: Literal["enable", "disable"] | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        utm_log: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = None,
        address_group: str | None = None,
        address_group_policy: Literal["disable", "allow", "deny"] | None = None,
        sticky_client_remove: Literal["enable", "disable"] | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = None,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | list[dict[str, Any]] | None = None,
        osen: Literal["enable", "disable"] | None = None,
        application_detection_engine: Literal["enable", "disable"] | None = None,
        application_dscp_marking: Literal["enable", "disable"] | None = None,
        application_report_intv: int | None = None,
        l3_roaming: Literal["enable", "disable"] | None = None,
        l3_roaming_mode: Literal["direct", "indirect"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update wireless_controller/vap object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            pre_auth: Field pre-auth
            external_pre_auth: Field external-pre-auth
            mesh_backhaul: Field mesh-backhaul
            atf_weight: Field atf-weight
            max_clients: Field max-clients
            max_clients_ap: Field max-clients-ap
            ssid: Field ssid
            broadcast_ssid: Field broadcast-ssid
            security: Field security
            pmf: Field pmf
            pmf_assoc_comeback_timeout: Field pmf-assoc-comeback-timeout
            pmf_sa_query_retry_timeout: Field pmf-sa-query-retry-timeout
            beacon_protection: Field beacon-protection
            okc: Field okc
            mbo: Field mbo
            gas_comeback_delay: Field gas-comeback-delay
            gas_fragmentation_limit: Field gas-fragmentation-limit
            mbo_cell_data_conn_pref: Field mbo-cell-data-conn-pref
            x80211k: Field 80211k
            x80211v: Field 80211v
            neighbor_report_dual_band: Field neighbor-report-dual-band
            fast_bss_transition: Field fast-bss-transition
            ft_mobility_domain: Field ft-mobility-domain
            ft_r0_key_lifetime: Field ft-r0-key-lifetime
            ft_over_ds: Field ft-over-ds
            sae_groups: Field sae-groups
            owe_groups: Field owe-groups
            owe_transition: Field owe-transition
            owe_transition_ssid: Field owe-transition-ssid
            additional_akms: Field additional-akms
            eapol_key_retries: Field eapol-key-retries
            tkip_counter_measure: Field tkip-counter-measure
            external_web: Field external-web
            external_web_format: Field external-web-format
            external_logout: Field external-logout
            mac_username_delimiter: Field mac-username-delimiter
            mac_password_delimiter: Field mac-password-delimiter
            mac_calling_station_delimiter: Field mac-calling-station-delimiter
            mac_called_station_delimiter: Field mac-called-station-delimiter
            mac_case: Field mac-case
            called_station_id_type: Field called-station-id-type
            mac_auth_bypass: Field mac-auth-bypass
            radius_mac_auth: Field radius-mac-auth
            radius_mac_auth_server: Field radius-mac-auth-server
            radius_mac_auth_block_interval: Field radius-mac-auth-block-interval
            radius_mac_mpsk_auth: Field radius-mac-mpsk-auth
            radius_mac_mpsk_timeout: Field radius-mac-mpsk-timeout
            radius_mac_auth_usergroups: Field radius-mac-auth-usergroups
            auth: Field auth
            encrypt: Field encrypt
            keyindex: Field keyindex
            key: Field key
            passphrase: Field passphrase
            sae_password: Field sae-password
            sae_h2e_only: Field sae-h2e-only
            sae_hnp_only: Field sae-hnp-only
            sae_pk: Field sae-pk
            sae_private_key: Field sae-private-key
            akm24_only: Field akm24-only
            radius_server: Field radius-server
            nas_filter_rule: Field nas-filter-rule
            domain_name_stripping: Field domain-name-stripping
            mlo: Field mlo
            local_standalone: Field local-standalone
            local_standalone_nat: Field local-standalone-nat
            ip: Field ip
            dhcp_lease_time: Field dhcp-lease-time
            local_standalone_dns: Field local-standalone-dns
            local_standalone_dns_ip: Field local-standalone-dns-ip
            local_lan_partition: Field local-lan-partition
            local_bridging: Field local-bridging
            local_lan: Field local-lan
            local_authentication: Field local-authentication
            usergroup: Field usergroup
            captive_portal: Field captive-portal
            captive_network_assistant_bypass: Field captive-network-assistant-bypass
            portal_message_override_group: Field portal-message-override-group
            portal_message_overrides: Field portal-message-overrides
            portal_type: Field portal-type
            selected_usergroups: Field selected-usergroups
            security_exempt_list: Field security-exempt-list
            security_redirect_url: Field security-redirect-url
            auth_cert: Field auth-cert
            auth_portal_addr: Field auth-portal-addr
            intra_vap_privacy: Field intra-vap-privacy
            schedule: Field schedule
            ldpc: Field ldpc
            high_efficiency: Field high-efficiency
            target_wake_time: Field target-wake-time
            port_macauth: Field port-macauth
            port_macauth_timeout: Field port-macauth-timeout
            port_macauth_reauth_timeout: Field port-macauth-reauth-timeout
            bss_color_partial: Field bss-color-partial
            mpsk_profile: Field mpsk-profile
            split_tunneling: Field split-tunneling
            nac: Field nac
            nac_profile: Field nac-profile
            vlanid: Field vlanid
            vlan_auto: Field vlan-auto
            dynamic_vlan: Field dynamic-vlan
            captive_portal_fw_accounting: Field captive-portal-fw-accounting
            captive_portal_ac_name: Field captive-portal-ac-name
            captive_portal_auth_timeout: Field captive-portal-auth-timeout
            multicast_rate: Field multicast-rate
            multicast_enhance: Field multicast-enhance
            igmp_snooping: Field igmp-snooping
            dhcp_address_enforcement: Field dhcp-address-enforcement
            broadcast_suppression: Field broadcast-suppression
            ipv6_rules: Field ipv6-rules
            me_disable_thresh: Field me-disable-thresh
            mu_mimo: Field mu-mimo
            probe_resp_suppression: Field probe-resp-suppression
            probe_resp_threshold: Field probe-resp-threshold
            radio_sensitivity: Field radio-sensitivity
            quarantine: Field quarantine
            radio_5g_threshold: Field radio-5g-threshold
            radio_2g_threshold: Field radio-2g-threshold
            vlan_name: Field vlan-name
            vlan_pooling: Field vlan-pooling
            vlan_pool: Field vlan-pool
            dhcp_option43_insertion: Field dhcp-option43-insertion
            dhcp_option82_insertion: Field dhcp-option82-insertion
            dhcp_option82_circuit_id_insertion: Field dhcp-option82-circuit-id-insertion
            dhcp_option82_remote_id_insertion: Field dhcp-option82-remote-id-insertion
            ptk_rekey: Field ptk-rekey
            ptk_rekey_intv: Field ptk-rekey-intv
            gtk_rekey: Field gtk-rekey
            gtk_rekey_intv: Field gtk-rekey-intv
            eap_reauth: Field eap-reauth
            eap_reauth_intv: Field eap-reauth-intv
            roaming_acct_interim_update: Field roaming-acct-interim-update
            qos_profile: Field qos-profile
            hotspot20_profile: Field hotspot20-profile
            access_control_list: Field access-control-list
            primary_wag_profile: Field primary-wag-profile
            secondary_wag_profile: Field secondary-wag-profile
            tunnel_echo_interval: Field tunnel-echo-interval
            tunnel_fallback_interval: Field tunnel-fallback-interval
            rates_11a: Field rates-11a
            rates_11bg: Field rates-11bg
            rates_11n_ss12: Field rates-11n-ss12
            rates_11n_ss34: Field rates-11n-ss34
            rates_11ac_mcs_map: Field rates-11ac-mcs-map
            rates_11ax_mcs_map: Field rates-11ax-mcs-map
            rates_11be_mcs_map: Field rates-11be-mcs-map
            rates_11be_mcs_map_160: Field rates-11be-mcs-map-160
            rates_11be_mcs_map_320: Field rates-11be-mcs-map-320
            utm_profile: Field utm-profile
            utm_status: Field utm-status
            utm_log: Field utm-log
            ips_sensor: Field ips-sensor
            application_list: Field application-list
            antivirus_profile: Field antivirus-profile
            webfilter_profile: Field webfilter-profile
            scan_botnet_connections: Field scan-botnet-connections
            address_group: Field address-group
            address_group_policy: Field address-group-policy
            sticky_client_remove: Field sticky-client-remove
            sticky_client_threshold_5g: Field sticky-client-threshold-5g
            sticky_client_threshold_2g: Field sticky-client-threshold-2g
            sticky_client_threshold_6g: Field sticky-client-threshold-6g
            bstm_rssi_disassoc_timer: Field bstm-rssi-disassoc-timer
            bstm_load_balancing_disassoc_timer: Field bstm-load-balancing-disassoc-timer
            bstm_disassociation_imminent: Field bstm-disassociation-imminent
            beacon_advertising: Field beacon-advertising
            osen: Field osen
            application_detection_engine: Field application-detection-engine
            application_dscp_marking: Field application-dscp-marking
            application_report_intv: Field application-report-intv
            l3_roaming: Field l3-roaming
            l3_roaming_mode: Field l3-roaming-mode
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            response_mode: Override client-level response_mode
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.wireless_controller_vap.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
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
        # Build payload using helper function with auto-normalization
        payload_data = build_api_payload(
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
            mlo=mlo,
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
        
        mkey_value = payload_data.get("name")
        if not mkey_value:
            raise ValueError("name is required for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_data, vdom=vdom, raw_json=raw_json, response_mode=response_mode, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_data, vdom=vdom, raw_json=raw_json, response_mode=response_mode, **kwargs)

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
        Move wireless_controller/vap object to a new position.
        
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
            >>> fgt.api.cmdb.wireless_controller_vap.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/vap",
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
        Clone wireless_controller/vap object.
        
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
            >>> fgt.api.cmdb.wireless_controller_vap.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/vap",
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
        Check if wireless_controller/vap object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_vap.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_vap.post(payload_dict=data)
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

