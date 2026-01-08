"""
FortiOS CMDB - System global_

Configuration endpoint for managing cmdb system/global_ objects.

API Endpoints:
    GET    /cmdb/system/global_
    POST   /cmdb/system/global_
    PUT    /cmdb/system/global_/{identifier}
    DELETE /cmdb/system/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_global_.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_global_.post(
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

class Global(CRUDEndpoint, MetadataMixin):
    """Global Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "global_"
    
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
        """Initialize Global endpoint."""
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
        Retrieve system/global_ configuration.

        Configure global attributes.

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
            >>> # Get all system/global_ objects
            >>> result = fgt.api.cmdb.system_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_global_.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_global_.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_global_.get_schema()

        See Also:
            - post(): Create new system/global_ object
            - put(): Update existing system/global_ object
            - delete(): Remove system/global_ object
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
            endpoint = f"/system/global/{name}"
        else:
            endpoint = "/system/global"
        
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
            >>> schema = fgt.api.cmdb.system_global_.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_global_.get_schema(format="json-schema")
        
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
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = None,
        gui_ipv6: Literal["enable", "disable"] | None = None,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = None,
        gui_local_out: Literal["enable", "disable"] | None = None,
        gui_certificates: Literal["enable", "disable"] | None = None,
        gui_custom_language: Literal["enable", "disable"] | None = None,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = None,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = None,
        gui_display_hostname: Literal["enable", "disable"] | None = None,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = None,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = None,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = None,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = None,
        gui_workflow_management: Literal["enable", "disable"] | None = None,
        gui_cdn_usage: Literal["enable", "disable"] | None = None,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | list[dict[str, Any]] | None = None,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | list[dict[str, Any]] | None = None,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | list[dict[str, Any]] | None = None,
        admintimeout: int | None = None,
        admin_console_timeout: int | None = None,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = None,
        ssd_trim_hour: int | None = None,
        ssd_trim_min: int | None = None,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = None,
        ssd_trim_date: int | None = None,
        admin_concurrent: Literal["enable", "disable"] | None = None,
        admin_lockout_threshold: int | None = None,
        admin_lockout_duration: int | None = None,
        refresh: int | None = None,
        interval: int | None = None,
        failtime: int | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        daily_restart: Literal["enable", "disable"] | None = None,
        restart_time: str | None = None,
        wad_restart_mode: Literal["none", "time", "memory"] | None = None,
        wad_restart_start_time: str | None = None,
        wad_restart_end_time: str | None = None,
        wad_p2s_max_body_size: int | None = None,
        radius_port: int | None = None,
        speedtestd_server_port: int | None = None,
        speedtestd_ctrl_port: int | None = None,
        admin_login_max: int | None = None,
        remoteauthtimeout: int | None = None,
        ldapconntimeout: int | None = None,
        batch_cmdb: Literal["enable", "disable"] | None = None,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = None,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        autorun_log_fsck: Literal["enable", "disable"] | None = None,
        timezone: str | None = None,
        traffic_priority: Literal["tos", "dscp"] | None = None,
        traffic_priority_level: Literal["low", "medium", "high"] | None = None,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = None,
        quic_max_datagram_size: int | None = None,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = None,
        quic_ack_thresold: int | None = None,
        quic_pmtud: Literal["enable", "disable"] | None = None,
        quic_tls_handshake_timeout: int | None = None,
        anti_replay: Literal["disable", "loose", "strict"] | None = None,
        send_pmtu_icmp: Literal["enable", "disable"] | None = None,
        honor_df: Literal["enable", "disable"] | None = None,
        pmtu_discovery: Literal["enable", "disable"] | None = None,
        revision_image_auto_backup: Literal["enable", "disable"] | None = None,
        revision_backup_on_logout: Literal["enable", "disable"] | None = None,
        management_vdom: str | None = None,
        hostname: str | None = None,
        alias: str | None = None,
        strong_crypto: Literal["enable", "disable"] | None = None,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = None,
        snat_route_change: Literal["enable", "disable"] | None = None,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = None,
        speedtest_server: Literal["enable", "disable"] | None = None,
        cli_audit_log: Literal["enable", "disable"] | None = None,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = None,
        fds_statistics: Literal["enable", "disable"] | None = None,
        fds_statistics_period: int | None = None,
        tcp_option: Literal["enable", "disable"] | None = None,
        lldp_transmission: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable"] | None = None,
        proxy_auth_timeout: int | None = None,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = None,
        proxy_re_authentication_time: int | None = None,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = None,
        proxy_auth_lifetime_timeout: int | None = None,
        proxy_resource_mode: Literal["enable", "disable"] | None = None,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = None,
        sys_perf_log_interval: int | None = None,
        check_protocol_header: Literal["loose", "strict"] | None = None,
        vip_arp_range: Literal["unlimited", "restricted"] | None = None,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = None,
        allow_traffic_redirect: Literal["enable", "disable"] | None = None,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = None,
        strict_dirty_session_check: Literal["enable", "disable"] | None = None,
        tcp_halfclose_timer: int | None = None,
        tcp_halfopen_timer: int | None = None,
        tcp_timewait_timer: int | None = None,
        tcp_rst_timer: int | None = None,
        udp_idle_timer: int | None = None,
        block_session_timer: int | None = None,
        ip_src_port_range: str | None = None,
        pre_login_banner: Literal["enable", "disable"] | None = None,
        post_login_banner: Literal["disable", "enable"] | None = None,
        tftp: Literal["enable", "disable"] | None = None,
        av_failopen: Literal["pass", "off", "one-shot"] | None = None,
        av_failopen_session: Literal["enable", "disable"] | None = None,
        memory_use_threshold_extreme: int | None = None,
        memory_use_threshold_red: int | None = None,
        memory_use_threshold_green: int | None = None,
        ip_fragment_mem_thresholds: int | None = None,
        ip_fragment_timeout: int | None = None,
        ipv6_fragment_timeout: int | None = None,
        cpu_use_threshold: int | None = None,
        log_single_cpu_high: Literal["enable", "disable"] | None = None,
        check_reset_range: Literal["strict", "disable"] | None = None,
        upgrade_report: Literal["enable", "disable"] | None = None,
        admin_port: int | None = None,
        admin_sport: int | None = None,
        admin_host: str | None = None,
        admin_https_redirect: Literal["enable", "disable"] | None = None,
        admin_hsts_max_age: int | None = None,
        admin_ssh_password: Literal["enable", "disable"] | None = None,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = None,
        admin_ssh_port: int | None = None,
        admin_ssh_grace_time: int | None = None,
        admin_ssh_v1: Literal["enable", "disable"] | None = None,
        admin_telnet: Literal["enable", "disable"] | None = None,
        admin_telnet_port: int | None = None,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = None,
        admin_forticloud_sso_default_profile: str | None = None,
        default_service_source_port: str | None = None,
        admin_server_cert: str | None = None,
        admin_https_pki_required: Literal["enable", "disable"] | None = None,
        wifi_certificate: str | None = None,
        dhcp_lease_backup_interval: int | None = None,
        wifi_ca_certificate: str | None = None,
        auth_http_port: int | None = None,
        auth_https_port: int | None = None,
        auth_ike_saml_port: int | None = None,
        auth_keepalive: Literal["enable", "disable"] | None = None,
        policy_auth_concurrent: int | None = None,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = None,
        auth_cert: str | None = None,
        clt_cert_req: Literal["enable", "disable"] | None = None,
        fortiservice_port: int | None = None,
        cfg_save: Literal["automatic", "manual", "revert"] | None = None,
        cfg_revert_timeout: int | None = None,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = None,
        admin_scp: Literal["enable", "disable"] | None = None,
        wireless_controller: Literal["enable", "disable"] | None = None,
        wireless_controller_port: int | None = None,
        fortiextender_data_port: int | None = None,
        fortiextender: Literal["disable", "enable"] | None = None,
        extender_controller_reserved_network: Any | None = None,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = None,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = None,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = None,
        switch_controller: Literal["disable", "enable"] | None = None,
        switch_controller_reserved_network: Any | None = None,
        dnsproxy_worker_count: int | None = None,
        url_filter_count: int | None = None,
        httpd_max_worker_count: int | None = None,
        proxy_worker_count: int | None = None,
        scanunit_count: int | None = None,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | list[dict[str, Any]] | None = None,
        ipv6_accept_dad: int | None = None,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = None,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = None,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = None,
        csr_ca_attribute: Literal["enable", "disable"] | None = None,
        wimax_4g_usb: Literal["enable", "disable"] | None = None,
        cert_chain_max: int | None = None,
        sslvpn_max_worker_count: int | None = None,
        sslvpn_affinity: str | None = None,
        sslvpn_web_mode: Literal["enable", "disable"] | None = None,
        two_factor_ftk_expiry: int | None = None,
        two_factor_email_expiry: int | None = None,
        two_factor_sms_expiry: int | None = None,
        two_factor_fac_expiry: int | None = None,
        two_factor_ftm_expiry: int | None = None,
        per_user_bal: Literal["enable", "disable"] | None = None,
        wad_worker_count: int | None = None,
        wad_worker_dev_cache: int | None = None,
        wad_csvc_cs_count: int | None = None,
        wad_csvc_db_count: int | None = None,
        wad_source_affinity: Literal["disable", "enable"] | None = None,
        wad_memory_change_granularity: int | None = None,
        login_timestamp: Literal["enable", "disable"] | None = None,
        ip_conflict_detection: Literal["enable", "disable"] | None = None,
        miglogd_children: int | None = None,
        log_daemon_cpu_threshold: int | None = None,
        special_file_23_support: Literal["disable", "enable"] | None = None,
        log_uuid_address: Literal["enable", "disable"] | None = None,
        log_ssl_connection: Literal["enable", "disable"] | None = None,
        gui_rest_api_cache: Literal["enable", "disable"] | None = None,
        rest_api_key_url_query: Literal["enable", "disable"] | None = None,
        arp_max_entry: int | None = None,
        ha_affinity: str | None = None,
        bfd_affinity: str | None = None,
        cmdbsvr_affinity: str | None = None,
        av_affinity: str | None = None,
        wad_affinity: str | None = None,
        ips_affinity: str | None = None,
        miglog_affinity: str | None = None,
        syslog_affinity: str | None = None,
        url_filter_affinity: str | None = None,
        router_affinity: str | None = None,
        ndp_max_entry: int | None = None,
        br_fdb_max_entry: int | None = None,
        max_route_cache_size: int | None = None,
        ipsec_qat_offload: Literal["enable", "disable"] | None = None,
        device_idle_timeout: int | None = None,
        user_device_store_max_devices: int | None = None,
        user_device_store_max_device_mem: int | None = None,
        user_device_store_max_users: int | None = None,
        user_device_store_max_unified_mem: int | None = None,
        gui_device_latitude: str | None = None,
        gui_device_longitude: str | None = None,
        private_data_encryption: Literal["disable", "enable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = None,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = None,
        gui_date_time_source: Literal["system", "browser"] | None = None,
        igmp_state_limit: int | None = None,
        cloud_communication: Literal["enable", "disable"] | None = None,
        ipsec_ha_seqjump_rate: int | None = None,
        fortitoken_cloud: Literal["enable", "disable"] | None = None,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = None,
        fortitoken_cloud_region: str | None = None,
        fortitoken_cloud_sync_interval: int | None = None,
        faz_disk_buffer_size: int | None = None,
        irq_time_accounting: Literal["auto", "force"] | None = None,
        management_ip: str | None = None,
        management_port: int | None = None,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = None,
        forticonverter_integration: Literal["enable", "disable"] | None = None,
        forticonverter_config_upload: Literal["once", "disable"] | None = None,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = None,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = None,
        geoip_full_db: Literal["enable", "disable"] | None = None,
        early_tcp_npu_session: Literal["enable", "disable"] | None = None,
        npu_neighbor_update: Literal["enable", "disable"] | None = None,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = None,
        interface_subnet_usage: Literal["disable", "enable"] | None = None,
        sflowd_max_children_num: int | None = None,
        fortigslb_integration: Literal["disable", "enable"] | None = None,
        user_history_password_threshold: int | None = None,
        auth_session_auto_backup: Literal["enable", "disable"] | None = None,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = None,
        scim_https_port: int | None = None,
        scim_http_port: int | None = None,
        scim_server_cert: str | None = None,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = None,
        tls_session_cache: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        response_mode: Literal["dict", "object"] | None = None,
        **kwargs: Any,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/global_ object.

        Configure global attributes.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            language: GUI display language.
            gui_ipv6: Enable/disable IPv6 settings on the GUI.
            gui_replacement_message_groups: Enable/disable replacement message groups on the GUI.
            gui_local_out: Enable/disable Local-out traffic on the GUI.
            gui_certificates: Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI.
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
            >>> result = fgt.api.cmdb.system_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            language=language,
            gui_ipv6=gui_ipv6,
            gui_replacement_message_groups=gui_replacement_message_groups,
            gui_local_out=gui_local_out,
            gui_certificates=gui_certificates,
            gui_custom_language=gui_custom_language,
            gui_wireless_opensecurity=gui_wireless_opensecurity,
            gui_app_detection_sdwan=gui_app_detection_sdwan,
            gui_display_hostname=gui_display_hostname,
            gui_fortigate_cloud_sandbox=gui_fortigate_cloud_sandbox,
            gui_firmware_upgrade_warning=gui_firmware_upgrade_warning,
            gui_forticare_registration_setup_warning=gui_forticare_registration_setup_warning,
            gui_auto_upgrade_setup_warning=gui_auto_upgrade_setup_warning,
            gui_workflow_management=gui_workflow_management,
            gui_cdn_usage=gui_cdn_usage,
            admin_https_ssl_versions=admin_https_ssl_versions,
            admin_https_ssl_ciphersuites=admin_https_ssl_ciphersuites,
            admin_https_ssl_banned_ciphers=admin_https_ssl_banned_ciphers,
            admintimeout=admintimeout,
            admin_console_timeout=admin_console_timeout,
            ssd_trim_freq=ssd_trim_freq,
            ssd_trim_hour=ssd_trim_hour,
            ssd_trim_min=ssd_trim_min,
            ssd_trim_weekday=ssd_trim_weekday,
            ssd_trim_date=ssd_trim_date,
            admin_concurrent=admin_concurrent,
            admin_lockout_threshold=admin_lockout_threshold,
            admin_lockout_duration=admin_lockout_duration,
            refresh=refresh,
            interval=interval,
            failtime=failtime,
            purdue_level=purdue_level,
            daily_restart=daily_restart,
            restart_time=restart_time,
            wad_restart_mode=wad_restart_mode,
            wad_restart_start_time=wad_restart_start_time,
            wad_restart_end_time=wad_restart_end_time,
            wad_p2s_max_body_size=wad_p2s_max_body_size,
            radius_port=radius_port,
            speedtestd_server_port=speedtestd_server_port,
            speedtestd_ctrl_port=speedtestd_ctrl_port,
            admin_login_max=admin_login_max,
            remoteauthtimeout=remoteauthtimeout,
            ldapconntimeout=ldapconntimeout,
            batch_cmdb=batch_cmdb,
            multi_factor_authentication=multi_factor_authentication,
            ssl_min_proto_version=ssl_min_proto_version,
            autorun_log_fsck=autorun_log_fsck,
            timezone=timezone,
            traffic_priority=traffic_priority,
            traffic_priority_level=traffic_priority_level,
            quic_congestion_control_algo=quic_congestion_control_algo,
            quic_max_datagram_size=quic_max_datagram_size,
            quic_udp_payload_size_shaping_per_cid=quic_udp_payload_size_shaping_per_cid,
            quic_ack_thresold=quic_ack_thresold,
            quic_pmtud=quic_pmtud,
            quic_tls_handshake_timeout=quic_tls_handshake_timeout,
            anti_replay=anti_replay,
            send_pmtu_icmp=send_pmtu_icmp,
            honor_df=honor_df,
            pmtu_discovery=pmtu_discovery,
            revision_image_auto_backup=revision_image_auto_backup,
            revision_backup_on_logout=revision_backup_on_logout,
            management_vdom=management_vdom,
            hostname=hostname,
            alias=alias,
            strong_crypto=strong_crypto,
            ssl_static_key_ciphers=ssl_static_key_ciphers,
            snat_route_change=snat_route_change,
            ipv6_snat_route_change=ipv6_snat_route_change,
            speedtest_server=speedtest_server,
            cli_audit_log=cli_audit_log,
            dh_params=dh_params,
            fds_statistics=fds_statistics,
            fds_statistics_period=fds_statistics_period,
            tcp_option=tcp_option,
            lldp_transmission=lldp_transmission,
            lldp_reception=lldp_reception,
            proxy_auth_timeout=proxy_auth_timeout,
            proxy_keep_alive_mode=proxy_keep_alive_mode,
            proxy_re_authentication_time=proxy_re_authentication_time,
            proxy_auth_lifetime=proxy_auth_lifetime,
            proxy_auth_lifetime_timeout=proxy_auth_lifetime_timeout,
            proxy_resource_mode=proxy_resource_mode,
            proxy_cert_use_mgmt_vdom=proxy_cert_use_mgmt_vdom,
            sys_perf_log_interval=sys_perf_log_interval,
            check_protocol_header=check_protocol_header,
            vip_arp_range=vip_arp_range,
            reset_sessionless_tcp=reset_sessionless_tcp,
            allow_traffic_redirect=allow_traffic_redirect,
            ipv6_allow_traffic_redirect=ipv6_allow_traffic_redirect,
            strict_dirty_session_check=strict_dirty_session_check,
            tcp_halfclose_timer=tcp_halfclose_timer,
            tcp_halfopen_timer=tcp_halfopen_timer,
            tcp_timewait_timer=tcp_timewait_timer,
            tcp_rst_timer=tcp_rst_timer,
            udp_idle_timer=udp_idle_timer,
            block_session_timer=block_session_timer,
            ip_src_port_range=ip_src_port_range,
            pre_login_banner=pre_login_banner,
            post_login_banner=post_login_banner,
            tftp=tftp,
            av_failopen=av_failopen,
            av_failopen_session=av_failopen_session,
            memory_use_threshold_extreme=memory_use_threshold_extreme,
            memory_use_threshold_red=memory_use_threshold_red,
            memory_use_threshold_green=memory_use_threshold_green,
            ip_fragment_mem_thresholds=ip_fragment_mem_thresholds,
            ip_fragment_timeout=ip_fragment_timeout,
            ipv6_fragment_timeout=ipv6_fragment_timeout,
            cpu_use_threshold=cpu_use_threshold,
            log_single_cpu_high=log_single_cpu_high,
            check_reset_range=check_reset_range,
            upgrade_report=upgrade_report,
            admin_port=admin_port,
            admin_sport=admin_sport,
            admin_host=admin_host,
            admin_https_redirect=admin_https_redirect,
            admin_hsts_max_age=admin_hsts_max_age,
            admin_ssh_password=admin_ssh_password,
            admin_restrict_local=admin_restrict_local,
            admin_ssh_port=admin_ssh_port,
            admin_ssh_grace_time=admin_ssh_grace_time,
            admin_ssh_v1=admin_ssh_v1,
            admin_telnet=admin_telnet,
            admin_telnet_port=admin_telnet_port,
            admin_forticloud_sso_login=admin_forticloud_sso_login,
            admin_forticloud_sso_default_profile=admin_forticloud_sso_default_profile,
            default_service_source_port=default_service_source_port,
            admin_server_cert=admin_server_cert,
            admin_https_pki_required=admin_https_pki_required,
            wifi_certificate=wifi_certificate,
            dhcp_lease_backup_interval=dhcp_lease_backup_interval,
            wifi_ca_certificate=wifi_ca_certificate,
            auth_http_port=auth_http_port,
            auth_https_port=auth_https_port,
            auth_ike_saml_port=auth_ike_saml_port,
            auth_keepalive=auth_keepalive,
            policy_auth_concurrent=policy_auth_concurrent,
            auth_session_limit=auth_session_limit,
            auth_cert=auth_cert,
            clt_cert_req=clt_cert_req,
            fortiservice_port=fortiservice_port,
            cfg_save=cfg_save,
            cfg_revert_timeout=cfg_revert_timeout,
            reboot_upon_config_restore=reboot_upon_config_restore,
            admin_scp=admin_scp,
            wireless_controller=wireless_controller,
            wireless_controller_port=wireless_controller_port,
            fortiextender_data_port=fortiextender_data_port,
            fortiextender=fortiextender,
            extender_controller_reserved_network=extender_controller_reserved_network,
            fortiextender_discovery_lockdown=fortiextender_discovery_lockdown,
            fortiextender_vlan_mode=fortiextender_vlan_mode,
            fortiextender_provision_on_authorization=fortiextender_provision_on_authorization,
            switch_controller=switch_controller,
            switch_controller_reserved_network=switch_controller_reserved_network,
            dnsproxy_worker_count=dnsproxy_worker_count,
            url_filter_count=url_filter_count,
            httpd_max_worker_count=httpd_max_worker_count,
            proxy_worker_count=proxy_worker_count,
            scanunit_count=scanunit_count,
            fgd_alert_subscription=fgd_alert_subscription,
            ipv6_accept_dad=ipv6_accept_dad,
            ipv6_allow_anycast_probe=ipv6_allow_anycast_probe,
            ipv6_allow_multicast_probe=ipv6_allow_multicast_probe,
            ipv6_allow_local_in_silent_drop=ipv6_allow_local_in_silent_drop,
            csr_ca_attribute=csr_ca_attribute,
            wimax_4g_usb=wimax_4g_usb,
            cert_chain_max=cert_chain_max,
            sslvpn_max_worker_count=sslvpn_max_worker_count,
            sslvpn_affinity=sslvpn_affinity,
            sslvpn_web_mode=sslvpn_web_mode,
            two_factor_ftk_expiry=two_factor_ftk_expiry,
            two_factor_email_expiry=two_factor_email_expiry,
            two_factor_sms_expiry=two_factor_sms_expiry,
            two_factor_fac_expiry=two_factor_fac_expiry,
            two_factor_ftm_expiry=two_factor_ftm_expiry,
            per_user_bal=per_user_bal,
            wad_worker_count=wad_worker_count,
            wad_worker_dev_cache=wad_worker_dev_cache,
            wad_csvc_cs_count=wad_csvc_cs_count,
            wad_csvc_db_count=wad_csvc_db_count,
            wad_source_affinity=wad_source_affinity,
            wad_memory_change_granularity=wad_memory_change_granularity,
            login_timestamp=login_timestamp,
            ip_conflict_detection=ip_conflict_detection,
            miglogd_children=miglogd_children,
            log_daemon_cpu_threshold=log_daemon_cpu_threshold,
            special_file_23_support=special_file_23_support,
            log_uuid_address=log_uuid_address,
            log_ssl_connection=log_ssl_connection,
            gui_rest_api_cache=gui_rest_api_cache,
            rest_api_key_url_query=rest_api_key_url_query,
            arp_max_entry=arp_max_entry,
            ha_affinity=ha_affinity,
            bfd_affinity=bfd_affinity,
            cmdbsvr_affinity=cmdbsvr_affinity,
            av_affinity=av_affinity,
            wad_affinity=wad_affinity,
            ips_affinity=ips_affinity,
            miglog_affinity=miglog_affinity,
            syslog_affinity=syslog_affinity,
            url_filter_affinity=url_filter_affinity,
            router_affinity=router_affinity,
            ndp_max_entry=ndp_max_entry,
            br_fdb_max_entry=br_fdb_max_entry,
            max_route_cache_size=max_route_cache_size,
            ipsec_qat_offload=ipsec_qat_offload,
            device_idle_timeout=device_idle_timeout,
            user_device_store_max_devices=user_device_store_max_devices,
            user_device_store_max_device_mem=user_device_store_max_device_mem,
            user_device_store_max_users=user_device_store_max_users,
            user_device_store_max_unified_mem=user_device_store_max_unified_mem,
            gui_device_latitude=gui_device_latitude,
            gui_device_longitude=gui_device_longitude,
            private_data_encryption=private_data_encryption,
            auto_auth_extension_device=auto_auth_extension_device,
            gui_theme=gui_theme,
            gui_date_format=gui_date_format,
            gui_date_time_source=gui_date_time_source,
            igmp_state_limit=igmp_state_limit,
            cloud_communication=cloud_communication,
            ipsec_ha_seqjump_rate=ipsec_ha_seqjump_rate,
            fortitoken_cloud=fortitoken_cloud,
            fortitoken_cloud_push_status=fortitoken_cloud_push_status,
            fortitoken_cloud_region=fortitoken_cloud_region,
            fortitoken_cloud_sync_interval=fortitoken_cloud_sync_interval,
            faz_disk_buffer_size=faz_disk_buffer_size,
            irq_time_accounting=irq_time_accounting,
            management_ip=management_ip,
            management_port=management_port,
            management_port_use_admin_sport=management_port_use_admin_sport,
            forticonverter_integration=forticonverter_integration,
            forticonverter_config_upload=forticonverter_config_upload,
            internet_service_database=internet_service_database,
            internet_service_download_list=internet_service_download_list,
            geoip_full_db=geoip_full_db,
            early_tcp_npu_session=early_tcp_npu_session,
            npu_neighbor_update=npu_neighbor_update,
            delay_tcp_npu_session=delay_tcp_npu_session,
            interface_subnet_usage=interface_subnet_usage,
            sflowd_max_children_num=sflowd_max_children_num,
            fortigslb_integration=fortigslb_integration,
            user_history_password_threshold=user_history_password_threshold,
            auth_session_auto_backup=auth_session_auto_backup,
            auth_session_auto_backup_interval=auth_session_auto_backup_interval,
            scim_https_port=scim_https_port,
            scim_http_port=scim_http_port,
            scim_server_cert=scim_server_cert,
            application_bandwidth_tracking=application_bandwidth_tracking,
            tls_session_cache=tls_session_cache,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/global_",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/system/global"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json, response_mode=response_mode
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
        Move system/global_ object to a new position.
        
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
            >>> fgt.api.cmdb.system_global_.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/global",
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
        Clone system/global_ object.
        
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
            >>> fgt.api.cmdb.system_global_.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/global",
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
        Check if system/global_ object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_global_.exists(name="myobj"):
            ...     fgt.api.cmdb.system_global_.post(payload_dict=data)
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

