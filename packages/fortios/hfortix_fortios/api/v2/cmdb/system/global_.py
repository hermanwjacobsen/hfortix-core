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


class Global:
    """Global Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Global endpoint."""
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
        Retrieve system/global_ configuration.

        Configure global attributes.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
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
            >>> # Get all system/global_ objects
            >>> result = fgt.api.cmdb.system_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_global_.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_global_.get(action="schema")

        See Also:
            - post(): Create new system/global_ object
            - put(): Update existing system/global_ object
            - delete(): Remove system/global_ object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/global/{name}"
        else:
            endpoint = "/system/global"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        language: str | None = None,
        gui_ipv6: str | None = None,
        gui_replacement_message_groups: str | None = None,
        gui_local_out: str | None = None,
        gui_certificates: str | None = None,
        gui_custom_language: str | None = None,
        gui_wireless_opensecurity: str | None = None,
        gui_app_detection_sdwan: str | None = None,
        gui_display_hostname: str | None = None,
        gui_fortigate_cloud_sandbox: str | None = None,
        gui_firmware_upgrade_warning: str | None = None,
        gui_forticare_registration_setup_warning: str | None = None,
        gui_auto_upgrade_setup_warning: str | None = None,
        gui_workflow_management: str | None = None,
        gui_cdn_usage: str | None = None,
        admin_https_ssl_versions: str | list | None = None,
        admin_https_ssl_ciphersuites: str | list | None = None,
        admin_https_ssl_banned_ciphers: str | list | None = None,
        admintimeout: int | None = None,
        admin_console_timeout: int | None = None,
        ssd_trim_freq: str | None = None,
        ssd_trim_hour: int | None = None,
        ssd_trim_min: int | None = None,
        ssd_trim_weekday: str | None = None,
        ssd_trim_date: int | None = None,
        admin_concurrent: str | None = None,
        admin_lockout_threshold: int | None = None,
        admin_lockout_duration: int | None = None,
        refresh: int | None = None,
        interval: int | None = None,
        failtime: int | None = None,
        purdue_level: str | None = None,
        daily_restart: str | None = None,
        restart_time: str | None = None,
        wad_restart_mode: str | None = None,
        wad_restart_start_time: str | None = None,
        wad_restart_end_time: str | None = None,
        wad_p2s_max_body_size: int | None = None,
        radius_port: int | None = None,
        speedtestd_server_port: int | None = None,
        speedtestd_ctrl_port: int | None = None,
        admin_login_max: int | None = None,
        remoteauthtimeout: int | None = None,
        ldapconntimeout: int | None = None,
        batch_cmdb: str | None = None,
        multi_factor_authentication: str | None = None,
        ssl_min_proto_version: str | None = None,
        autorun_log_fsck: str | None = None,
        timezone: str | None = None,
        traffic_priority: str | None = None,
        traffic_priority_level: str | None = None,
        quic_congestion_control_algo: str | None = None,
        quic_max_datagram_size: int | None = None,
        quic_udp_payload_size_shaping_per_cid: str | None = None,
        quic_ack_thresold: int | None = None,
        quic_pmtud: str | None = None,
        quic_tls_handshake_timeout: int | None = None,
        anti_replay: str | None = None,
        send_pmtu_icmp: str | None = None,
        honor_df: str | None = None,
        pmtu_discovery: str | None = None,
        revision_image_auto_backup: str | None = None,
        revision_backup_on_logout: str | None = None,
        management_vdom: str | None = None,
        hostname: str | None = None,
        alias: str | None = None,
        strong_crypto: str | None = None,
        ssl_static_key_ciphers: str | None = None,
        snat_route_change: str | None = None,
        ipv6_snat_route_change: str | None = None,
        speedtest_server: str | None = None,
        cli_audit_log: str | None = None,
        dh_params: str | None = None,
        fds_statistics: str | None = None,
        fds_statistics_period: int | None = None,
        tcp_option: str | None = None,
        lldp_transmission: str | None = None,
        lldp_reception: str | None = None,
        proxy_auth_timeout: int | None = None,
        proxy_keep_alive_mode: str | None = None,
        proxy_re_authentication_time: int | None = None,
        proxy_auth_lifetime: str | None = None,
        proxy_auth_lifetime_timeout: int | None = None,
        proxy_resource_mode: str | None = None,
        proxy_cert_use_mgmt_vdom: str | None = None,
        sys_perf_log_interval: int | None = None,
        check_protocol_header: str | None = None,
        vip_arp_range: str | None = None,
        reset_sessionless_tcp: str | None = None,
        allow_traffic_redirect: str | None = None,
        ipv6_allow_traffic_redirect: str | None = None,
        strict_dirty_session_check: str | None = None,
        tcp_halfclose_timer: int | None = None,
        tcp_halfopen_timer: int | None = None,
        tcp_timewait_timer: int | None = None,
        tcp_rst_timer: int | None = None,
        udp_idle_timer: int | None = None,
        block_session_timer: int | None = None,
        ip_src_port_range: str | None = None,
        pre_login_banner: str | None = None,
        post_login_banner: str | None = None,
        tftp: str | None = None,
        av_failopen: str | None = None,
        av_failopen_session: str | None = None,
        memory_use_threshold_extreme: int | None = None,
        memory_use_threshold_red: int | None = None,
        memory_use_threshold_green: int | None = None,
        ip_fragment_mem_thresholds: int | None = None,
        ip_fragment_timeout: int | None = None,
        ipv6_fragment_timeout: int | None = None,
        cpu_use_threshold: int | None = None,
        log_single_cpu_high: str | None = None,
        check_reset_range: str | None = None,
        upgrade_report: str | None = None,
        admin_port: int | None = None,
        admin_sport: int | None = None,
        admin_host: str | None = None,
        admin_https_redirect: str | None = None,
        admin_hsts_max_age: int | None = None,
        admin_ssh_password: str | None = None,
        admin_restrict_local: str | None = None,
        admin_ssh_port: int | None = None,
        admin_ssh_grace_time: int | None = None,
        admin_ssh_v1: str | None = None,
        admin_telnet: str | None = None,
        admin_telnet_port: int | None = None,
        admin_forticloud_sso_login: str | None = None,
        admin_forticloud_sso_default_profile: str | None = None,
        default_service_source_port: str | None = None,
        admin_server_cert: str | None = None,
        admin_https_pki_required: str | None = None,
        wifi_certificate: str | None = None,
        dhcp_lease_backup_interval: int | None = None,
        wifi_ca_certificate: str | None = None,
        auth_http_port: int | None = None,
        auth_https_port: int | None = None,
        auth_ike_saml_port: int | None = None,
        auth_keepalive: str | None = None,
        policy_auth_concurrent: int | None = None,
        auth_session_limit: str | None = None,
        auth_cert: str | None = None,
        clt_cert_req: str | None = None,
        fortiservice_port: int | None = None,
        cfg_save: str | None = None,
        cfg_revert_timeout: int | None = None,
        reboot_upon_config_restore: str | None = None,
        admin_scp: str | None = None,
        wireless_controller: str | None = None,
        wireless_controller_port: int | None = None,
        fortiextender_data_port: int | None = None,
        fortiextender: str | None = None,
        extender_controller_reserved_network: Any | None = None,
        fortiextender_discovery_lockdown: str | None = None,
        fortiextender_vlan_mode: str | None = None,
        fortiextender_provision_on_authorization: str | None = None,
        switch_controller: str | None = None,
        switch_controller_reserved_network: Any | None = None,
        dnsproxy_worker_count: int | None = None,
        url_filter_count: int | None = None,
        httpd_max_worker_count: int | None = None,
        proxy_worker_count: int | None = None,
        scanunit_count: int | None = None,
        fgd_alert_subscription: str | list | None = None,
        ipv6_accept_dad: int | None = None,
        ipv6_allow_anycast_probe: str | None = None,
        ipv6_allow_multicast_probe: str | None = None,
        ipv6_allow_local_in_silent_drop: str | None = None,
        csr_ca_attribute: str | None = None,
        wimax_4g_usb: str | None = None,
        cert_chain_max: int | None = None,
        sslvpn_max_worker_count: int | None = None,
        sslvpn_affinity: str | None = None,
        sslvpn_web_mode: str | None = None,
        two_factor_ftk_expiry: int | None = None,
        two_factor_email_expiry: int | None = None,
        two_factor_sms_expiry: int | None = None,
        two_factor_fac_expiry: int | None = None,
        two_factor_ftm_expiry: int | None = None,
        per_user_bal: str | None = None,
        wad_worker_count: int | None = None,
        wad_worker_dev_cache: int | None = None,
        wad_csvc_cs_count: int | None = None,
        wad_csvc_db_count: int | None = None,
        wad_source_affinity: str | None = None,
        wad_memory_change_granularity: int | None = None,
        login_timestamp: str | None = None,
        ip_conflict_detection: str | None = None,
        miglogd_children: int | None = None,
        log_daemon_cpu_threshold: int | None = None,
        special_file_23_support: str | None = None,
        log_uuid_address: str | None = None,
        log_ssl_connection: str | None = None,
        gui_rest_api_cache: str | None = None,
        rest_api_key_url_query: str | None = None,
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
        ipsec_qat_offload: str | None = None,
        device_idle_timeout: int | None = None,
        user_device_store_max_devices: int | None = None,
        user_device_store_max_device_mem: int | None = None,
        user_device_store_max_users: int | None = None,
        user_device_store_max_unified_mem: int | None = None,
        gui_device_latitude: str | None = None,
        gui_device_longitude: str | None = None,
        private_data_encryption: str | None = None,
        auto_auth_extension_device: str | None = None,
        gui_theme: str | None = None,
        gui_date_format: str | None = None,
        gui_date_time_source: str | None = None,
        igmp_state_limit: int | None = None,
        cloud_communication: str | None = None,
        ipsec_ha_seqjump_rate: int | None = None,
        fortitoken_cloud: str | None = None,
        fortitoken_cloud_push_status: str | None = None,
        fortitoken_cloud_region: str | None = None,
        fortitoken_cloud_sync_interval: int | None = None,
        faz_disk_buffer_size: int | None = None,
        irq_time_accounting: str | None = None,
        management_ip: str | None = None,
        management_port: int | None = None,
        management_port_use_admin_sport: str | None = None,
        forticonverter_integration: str | None = None,
        forticonverter_config_upload: str | None = None,
        internet_service_database: str | None = None,
        internet_service_download_list: str | list | None = None,
        geoip_full_db: str | None = None,
        early_tcp_npu_session: str | None = None,
        npu_neighbor_update: str | None = None,
        delay_tcp_npu_session: str | None = None,
        interface_subnet_usage: str | None = None,
        sflowd_max_children_num: int | None = None,
        fortigslb_integration: str | None = None,
        user_history_password_threshold: int | None = None,
        auth_session_auto_backup: str | None = None,
        auth_session_auto_backup_interval: str | None = None,
        scim_https_port: int | None = None,
        scim_http_port: int | None = None,
        scim_server_cert: str | None = None,
        application_bandwidth_tracking: str | None = None,
        tls_session_cache: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
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
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
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
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/global/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





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
            >>> print(Global.help())
            
            >>> # Get field information
            >>> print(Global.help("language"))
        """
        from ._helpers.global_ import (
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
            >>> fields = Global.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Global.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.global_ import get_all_fields, get_field_metadata

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
            >>> info = Global.field_info("language")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.global_ import get_field_metadata

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
            >>> is_valid, error = Global.validate_field("language", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.global_ import validate_field_value

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
            >>> required = Global.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.global_ import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Global.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.global_ import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Global.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.global_ import get_schema_info

        return get_schema_info()
