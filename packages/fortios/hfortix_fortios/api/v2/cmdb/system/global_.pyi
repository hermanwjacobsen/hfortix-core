from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for system/global_ payload fields.
    
    Configure global attributes.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: wifi-ca-certificate)
        - :class:`~.certificate.local.LocalEndpoint` (via: admin-server-cert, auth-cert, scim-server-cert, +1 more)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: admin-forticloud-sso-default-profile)
        - :class:`~.system.timezone.TimezoneEndpoint` (via: timezone)
        - :class:`~.system.vdom.VdomEndpoint` (via: management-vdom)

    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    language: NotRequired[Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"]]  # GUI display language.
    gui_ipv6: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv6 settings on the GUI.
    gui_replacement_message_groups: NotRequired[Literal["enable", "disable"]]  # Enable/disable replacement message groups on the GUI.
    gui_local_out: NotRequired[Literal["enable", "disable"]]  # Enable/disable Local-out traffic on the GUI.
    gui_certificates: NotRequired[Literal["enable", "disable"]]  # Enable/disable the System > Certificate GUI page, allowing y
    gui_custom_language: NotRequired[Literal["enable", "disable"]]  # Enable/disable custom languages in GUI.
    gui_wireless_opensecurity: NotRequired[Literal["enable", "disable"]]  # Enable/disable wireless open security option on the GUI.
    gui_app_detection_sdwan: NotRequired[Literal["enable", "disable"]]  # Enable/disable Allow app-detection based SD-WAN.
    gui_display_hostname: NotRequired[Literal["enable", "disable"]]  # Enable/disable displaying the FortiGate's hostname on the GU
    gui_fortigate_cloud_sandbox: NotRequired[Literal["enable", "disable"]]  # Enable/disable displaying FortiGate Cloud Sandbox on the GUI
    gui_firmware_upgrade_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable the firmware upgrade warning on the GUI.
    gui_forticare_registration_setup_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable the FortiCare registration setup warning on t
    gui_auto_upgrade_setup_warning: NotRequired[Literal["enable", "disable"]]  # Enable/disable the automatic patch upgrade setup prompt on t
    gui_workflow_management: NotRequired[Literal["enable", "disable"]]  # Enable/disable Workflow management features on the GUI.
    gui_cdn_usage: NotRequired[Literal["enable", "disable"]]  # Enable/disable Load GUI static files from a CDN.
    admin_https_ssl_versions: NotRequired[Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"]]  # Allowed TLS versions for web administration.
    admin_https_ssl_ciphersuites: NotRequired[Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"]]  # Select one or more TLS 1.3 ciphersuites to enable. Does not
    admin_https_ssl_banned_ciphers: NotRequired[Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"]]  # Select one or more cipher technologies that cannot be used i
    admintimeout: NotRequired[int]  # Number of minutes before an idle administrator session times
    admin_console_timeout: NotRequired[int]  # Console login timeout that overrides the admin timeout value
    ssd_trim_freq: NotRequired[Literal["never", "hourly", "daily", "weekly", "monthly"]]  # How often to run SSD Trim (default = weekly). SSD Trim preve
    ssd_trim_hour: NotRequired[int]  # Hour of the day on which to run SSD Trim
    ssd_trim_min: NotRequired[int]  # Minute of the hour on which to run SSD Trim
    ssd_trim_weekday: NotRequired[Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]]  # Day of week to run SSD Trim.
    ssd_trim_date: NotRequired[int]  # Date within a month to run ssd trim.
    admin_concurrent: NotRequired[Literal["enable", "disable"]]  # Enable/disable concurrent administrator logins. Use policy-a
    admin_lockout_threshold: NotRequired[int]  # Number of failed login attempts before an administrator acco
    admin_lockout_duration: NotRequired[int]  # Amount of time in seconds that an administrator account is l
    refresh: NotRequired[int]  # Statistics refresh interval second(s) in GUI.
    interval: NotRequired[int]  # Dead gateway detection interval.
    failtime: NotRequired[int]  # Fail-time for server lost.
    purdue_level: NotRequired[Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]]  # Purdue Level of this FortiGate.
    daily_restart: NotRequired[Literal["enable", "disable"]]  # Enable/disable daily restart of FortiGate unit. Use the rest
    restart_time: str  # Daily restart time (hh:mm).
    wad_restart_mode: NotRequired[Literal["none", "time", "memory"]]  # WAD worker restart mode (default = none).
    wad_restart_start_time: str  # WAD workers daily restart time (hh:mm).
    wad_restart_end_time: str  # WAD workers daily restart end time (hh:mm).
    wad_p2s_max_body_size: NotRequired[int]  # Maximum size of the body of the local out HTTP request
    radius_port: NotRequired[int]  # RADIUS service port number.
    speedtestd_server_port: NotRequired[int]  # Speedtest server port number.
    speedtestd_ctrl_port: NotRequired[int]  # Speedtest server controller port number.
    admin_login_max: NotRequired[int]  # Maximum number of administrators who can be logged in at the
    remoteauthtimeout: NotRequired[int]  # Number of seconds that the FortiGate waits for responses fro
    ldapconntimeout: NotRequired[int]  # Global timeout for connections with remote LDAP servers in m
    batch_cmdb: NotRequired[Literal["enable", "disable"]]  # Enable/disable batch mode, allowing you to enter a series of
    multi_factor_authentication: NotRequired[Literal["optional", "mandatory"]]  # Enforce all login methods to require an additional authentic
    ssl_min_proto_version: NotRequired[Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for SSL/TLS connections
    autorun_log_fsck: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic log partition check after ungracefu
    timezone: str  # Timezone database name. Enter ? to view the list of timezone
    traffic_priority: Literal["tos", "dscp"]  # Choose Type of Service (ToS) or Differentiated Services Code
    traffic_priority_level: Literal["low", "medium", "high"]  # Default system-wide level of priority for traffic prioritiza
    quic_congestion_control_algo: NotRequired[Literal["cubic", "bbr", "bbr2", "reno"]]  # QUIC congestion control algorithm (default = cubic).
    quic_max_datagram_size: NotRequired[int]  # Maximum transmit datagram size (1200 - 1500, default = 1500)
    quic_udp_payload_size_shaping_per_cid: NotRequired[Literal["enable", "disable"]]  # Enable/disable UDP payload size shaping per connection ID
    quic_ack_thresold: NotRequired[int]  # Maximum number of unacknowledged packets before sending ACK
    quic_pmtud: NotRequired[Literal["enable", "disable"]]  # Enable/disable path MTU discovery (default = enable).
    quic_tls_handshake_timeout: NotRequired[int]  # Time-to-live (TTL) for TLS handshake in seconds
    anti_replay: NotRequired[Literal["disable", "loose", "strict"]]  # Level of checking for packet replay and TCP sequence checkin
    send_pmtu_icmp: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending of path maximum transmission unit
    honor_df: NotRequired[Literal["enable", "disable"]]  # Enable/disable honoring of Don't-Fragment (DF) flag.
    pmtu_discovery: NotRequired[Literal["enable", "disable"]]  # Enable/disable path MTU discovery.
    revision_image_auto_backup: NotRequired[Literal["enable", "disable"]]  # Enable/disable back-up of the latest image revision after th
    revision_backup_on_logout: NotRequired[Literal["enable", "disable"]]  # Enable/disable back-up of the latest configuration revision
    management_vdom: NotRequired[str]  # Management virtual domain name.
    hostname: NotRequired[str]  # FortiGate unit's hostname. Most models will truncate names l
    alias: NotRequired[str]  # Alias for your FortiGate unit.
    strong_crypto: NotRequired[Literal["enable", "disable"]]  # Enable to use strong encryption and only allow strong cipher
    ssl_static_key_ciphers: NotRequired[Literal["enable", "disable"]]  # Enable/disable static key ciphers in SSL/TLS connections
    snat_route_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable the ability to change the source NAT route.
    ipv6_snat_route_change: NotRequired[Literal["enable", "disable"]]  # Enable/disable the ability to change the IPv6 source NAT rou
    speedtest_server: NotRequired[Literal["enable", "disable"]]  # Enable/disable speed test server.
    cli_audit_log: NotRequired[Literal["enable", "disable"]]  # Enable/disable CLI audit log.
    dh_params: NotRequired[Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]]  # Number of bits to use in the Diffie-Hellman exchange for HTT
    fds_statistics: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending IPS, Application Control, and AntiVir
    fds_statistics_period: NotRequired[int]  # FortiGuard statistics collection period in minutes.
    tcp_option: NotRequired[Literal["enable", "disable"]]  # Enable SACK, timestamp and MSS TCP options.
    lldp_transmission: NotRequired[Literal["enable", "disable"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) transmis
    lldp_reception: NotRequired[Literal["enable", "disable"]]  # Enable/disable Link Layer Discovery Protocol (LLDP) receptio
    proxy_auth_timeout: NotRequired[int]  # Authentication timeout in minutes for authenticated users
    proxy_keep_alive_mode: NotRequired[Literal["session", "traffic", "re-authentication"]]  # Control if users must re-authenticate after a session is clo
    proxy_re_authentication_time: NotRequired[int]  # The time limit that users must re-authenticate if proxy-keep
    proxy_auth_lifetime: NotRequired[Literal["enable", "disable"]]  # Enable/disable authenticated users lifetime control. This is
    proxy_auth_lifetime_timeout: NotRequired[int]  # Lifetime timeout in minutes for authenticated users
    proxy_resource_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of the maximum memory usage on the FortiG
    proxy_cert_use_mgmt_vdom: NotRequired[Literal["enable", "disable"]]  # Enable/disable using management VDOM to send requests.
    sys_perf_log_interval: NotRequired[int]  # Time in minutes between updates of performance statistics lo
    check_protocol_header: NotRequired[Literal["loose", "strict"]]  # Level of checking performed on protocol headers. Strict chec
    vip_arp_range: NotRequired[Literal["unlimited", "restricted"]]  # Controls the number of ARPs that the FortiGate sends for a V
    reset_sessionless_tcp: NotRequired[Literal["enable", "disable"]]  # Action to perform if the FortiGate receives a TCP packet but
    allow_traffic_redirect: NotRequired[Literal["enable", "disable"]]  # Disable to prevent traffic with same local ingress and egres
    ipv6_allow_traffic_redirect: NotRequired[Literal["enable", "disable"]]  # Disable to prevent IPv6 traffic with same local ingress and
    strict_dirty_session_check: NotRequired[Literal["enable", "disable"]]  # Enable to check the session against the original policy when
    tcp_halfclose_timer: NotRequired[int]  # Number of seconds the FortiGate unit should wait to close a
    tcp_halfopen_timer: NotRequired[int]  # Number of seconds the FortiGate unit should wait to close a
    tcp_timewait_timer: NotRequired[int]  # Length of the TCP TIME-WAIT state in seconds
    tcp_rst_timer: NotRequired[int]  # Length of the TCP CLOSE state in seconds
    udp_idle_timer: NotRequired[int]  # UDP connection session timeout. This command can be useful i
    block_session_timer: NotRequired[int]  # Duration in seconds for blocked sessions (1 - 300 sec
    ip_src_port_range: str  # IP source port range used for traffic originating from the F
    pre_login_banner: NotRequired[Literal["enable", "disable"]]  # Enable/disable displaying the administrator access disclaime
    post_login_banner: NotRequired[Literal["disable", "enable"]]  # Enable/disable displaying the administrator access disclaime
    tftp: NotRequired[Literal["enable", "disable"]]  # Enable/disable TFTP.
    av_failopen: NotRequired[Literal["pass", "off", "one-shot"]]  # Set the action to take if the FortiGate is running low on me
    av_failopen_session: NotRequired[Literal["enable", "disable"]]  # When enabled and a proxy for a protocol runs out of room in
    memory_use_threshold_extreme: NotRequired[int]  # Threshold at which memory usage is considered extreme
    memory_use_threshold_red: NotRequired[int]  # Threshold at which memory usage forces the FortiGate to ente
    memory_use_threshold_green: NotRequired[int]  # Threshold at which memory usage forces the FortiGate to exit
    ip_fragment_mem_thresholds: NotRequired[int]  # Maximum memory (MB) used to reassemble IPv4/IPv6 fragments.
    ip_fragment_timeout: NotRequired[int]  # Timeout value in seconds for any fragment not being reassemb
    ipv6_fragment_timeout: NotRequired[int]  # Timeout value in seconds for any IPv6 fragment not being rea
    cpu_use_threshold: NotRequired[int]  # Threshold at which CPU usage is reported
    log_single_cpu_high: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging the event of a single CPU core reachi
    check_reset_range: NotRequired[Literal["strict", "disable"]]  # Configure ICMP error message verification. You can either ap
    upgrade_report: NotRequired[Literal["enable", "disable"]]  # Enable/disable the generation of an upgrade report when upgr
    admin_port: NotRequired[int]  # Administrative access port for HTTP.
    admin_sport: NotRequired[int]  # Administrative access port for HTTPS.
    admin_host: NotRequired[str]  # Administrative host for HTTP and HTTPS. When set, will be us
    admin_https_redirect: NotRequired[Literal["enable", "disable"]]  # Enable/disable redirection of HTTP administration access to
    admin_hsts_max_age: NotRequired[int]  # HTTPS Strict-Transport-Security header max-age in seconds. A
    admin_ssh_password: NotRequired[Literal["enable", "disable"]]  # Enable/disable password authentication for SSH admin access.
    admin_restrict_local: NotRequired[Literal["all", "non-console-only", "disable"]]  # Enable/disable local admin authentication restriction when r
    admin_ssh_port: NotRequired[int]  # Administrative access port for SSH.
    admin_ssh_grace_time: NotRequired[int]  # Maximum time in seconds permitted between making an SSH conn
    admin_ssh_v1: NotRequired[Literal["enable", "disable"]]  # Enable/disable SSH v1 compatibility.
    admin_telnet: NotRequired[Literal["enable", "disable"]]  # Enable/disable TELNET service.
    admin_telnet_port: NotRequired[int]  # Administrative access port for TELNET.
    admin_forticloud_sso_login: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiCloud admin login via SSO.
    admin_forticloud_sso_default_profile: NotRequired[str]  # Override access profile.
    default_service_source_port: NotRequired[str]  # Default service source port range (default = 1 - 65535).
    admin_server_cert: NotRequired[str]  # Server certificate that the FortiGate uses for HTTPS adminis
    admin_https_pki_required: NotRequired[Literal["enable", "disable"]]  # Enable/disable admin login method. Enable to force administr
    wifi_certificate: NotRequired[str]  # Certificate to use for WiFi authentication.
    dhcp_lease_backup_interval: NotRequired[int]  # DHCP leases backup interval in seconds
    wifi_ca_certificate: NotRequired[str]  # CA certificate that verifies the WiFi certificate.
    auth_http_port: NotRequired[int]  # User authentication HTTP port. (1 - 65535, default = 1000).
    auth_https_port: NotRequired[int]  # User authentication HTTPS port. (1 - 65535, default = 1003).
    auth_ike_saml_port: NotRequired[int]  # User IKE SAML authentication port
    auth_keepalive: NotRequired[Literal["enable", "disable"]]  # Enable to prevent user authentication sessions from timing o
    policy_auth_concurrent: NotRequired[int]  # Number of concurrent firewall use logins from the same user
    auth_session_limit: NotRequired[Literal["block-new", "logout-inactive"]]  # Action to take when the number of allowed user authenticated
    auth_cert: NotRequired[str]  # Server certificate that the FortiGate uses for HTTPS firewal
    clt_cert_req: NotRequired[Literal["enable", "disable"]]  # Enable/disable requiring administrators to have a client cer
    fortiservice_port: NotRequired[int]  # FortiService port (1 - 65535, default = 8013). Used by Forti
    cfg_save: NotRequired[Literal["automatic", "manual", "revert"]]  # Configuration file save mode for CLI changes.
    cfg_revert_timeout: NotRequired[int]  # Time-out for reverting to the last saved configuration.
    reboot_upon_config_restore: NotRequired[Literal["enable", "disable"]]  # Enable/disable reboot of system upon restoring configuration
    admin_scp: NotRequired[Literal["enable", "disable"]]  # Enable/disable SCP support for system configuration backup,
    wireless_controller: NotRequired[Literal["enable", "disable"]]  # Enable/disable the wireless controller feature to use the Fo
    wireless_controller_port: NotRequired[int]  # Port used for the control channel in wireless controller mod
    fortiextender_data_port: NotRequired[int]  # FortiExtender data port (1024 - 49150, default = 25246).
    fortiextender: NotRequired[Literal["disable", "enable"]]  # Enable/disable FortiExtender.
    extender_controller_reserved_network: NotRequired[str]  # Configure reserved network subnet for managed LAN extension
    fortiextender_discovery_lockdown: NotRequired[Literal["disable", "enable"]]  # Enable/disable FortiExtender CAPWAP lockdown.
    fortiextender_vlan_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiExtender VLAN mode.
    fortiextender_provision_on_authorization: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic provisioning of latest FortiExtende
    switch_controller: NotRequired[Literal["disable", "enable"]]  # Enable/disable switch controller feature. Switch controller
    switch_controller_reserved_network: NotRequired[str]  # Configure reserved network subnet for managed switches. This
    dnsproxy_worker_count: NotRequired[int]  # DNS proxy worker count. For a FortiGate with multiple logica
    url_filter_count: NotRequired[int]  # URL filter daemon count.
    httpd_max_worker_count: NotRequired[int]  # Maximum number of simultaneous HTTP requests that will be se
    proxy_worker_count: NotRequired[int]  # Proxy worker count.
    scanunit_count: NotRequired[int]  # Number of scanunits. The range and the default depend on the
    fgd_alert_subscription: NotRequired[Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"]]  # Type of alert to retrieve from FortiGuard.
    ipv6_accept_dad: NotRequired[int]  # Enable/disable acceptance of IPv6 Duplicate Address Detectio
    ipv6_allow_anycast_probe: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv6 address probe through Anycast.
    ipv6_allow_multicast_probe: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPv6 address probe through Multicast.
    ipv6_allow_local_in_silent_drop: NotRequired[Literal["enable", "disable"]]  # Enable/disable silent drop of IPv6 local-in traffic.
    csr_ca_attribute: NotRequired[Literal["enable", "disable"]]  # Enable/disable the CA attribute in certificates. Some CA ser
    wimax_4g_usb: NotRequired[Literal["enable", "disable"]]  # Enable/disable comparability with WiMAX 4G USB devices.
    cert_chain_max: NotRequired[int]  # Maximum number of certificates that can be traversed in a ce
    sslvpn_max_worker_count: NotRequired[int]  # Maximum number of Agentless VPN processes. Upper limit for t
    sslvpn_affinity: NotRequired[str]  # Agentless VPN CPU affinity.
    sslvpn_web_mode: NotRequired[Literal["enable", "disable"]]  # Enable/disable Agentless VPN web mode.
    two_factor_ftk_expiry: NotRequired[int]  # FortiToken authentication session timeout (60 - 600 sec
    two_factor_email_expiry: NotRequired[int]  # Email-based two-factor authentication session timeout
    two_factor_sms_expiry: NotRequired[int]  # SMS-based two-factor authentication session timeout
    two_factor_fac_expiry: NotRequired[int]  # FortiAuthenticator token authentication session timeout
    two_factor_ftm_expiry: NotRequired[int]  # FortiToken Mobile session timeout (1 - 168 hours
    per_user_bal: NotRequired[Literal["enable", "disable"]]  # Enable/disable per-user block/allow list filter.
    wad_worker_count: NotRequired[int]  # Number of explicit proxy WAN optimization daemon (WAD) proce
    wad_worker_dev_cache: NotRequired[int]  # Number of cached devices for each ZTNA proxy worker. The def
    wad_csvc_cs_count: NotRequired[int]  # Number of concurrent WAD-cache-service object-cache processe
    wad_csvc_db_count: NotRequired[int]  # Number of concurrent WAD-cache-service byte-cache processes.
    wad_source_affinity: NotRequired[Literal["disable", "enable"]]  # Enable/disable dispatching traffic to WAD workers based on s
    wad_memory_change_granularity: NotRequired[int]  # Minimum percentage change in system memory usage detected by
    login_timestamp: NotRequired[Literal["enable", "disable"]]  # Enable/disable login time recording.
    ip_conflict_detection: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of IPv4 address conflict detection.
    miglogd_children: NotRequired[int]  # Number of logging (miglogd) processes to be allowed to run.
    log_daemon_cpu_threshold: NotRequired[int]  # Configure syslog daemon process spawning threshold. Use a pe
    special_file_23_support: NotRequired[Literal["disable", "enable"]]  # Enable/disable detection of those special format files when
    log_uuid_address: NotRequired[Literal["enable", "disable"]]  # Enable/disable insertion of address UUIDs to traffic logs.
    log_ssl_connection: NotRequired[Literal["enable", "disable"]]  # Enable/disable logging of SSL connection events.
    gui_rest_api_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable REST API result caching on FortiGate.
    rest_api_key_url_query: NotRequired[Literal["enable", "disable"]]  # Enable/disable support for passing REST API keys through URL
    arp_max_entry: NotRequired[int]  # Maximum number of dynamically learned MAC addresses that can
    ha_affinity: NotRequired[str]  # Affinity setting for HA daemons
    bfd_affinity: NotRequired[str]  # Affinity setting for BFD daemon
    cmdbsvr_affinity: NotRequired[str]  # Affinity setting for cmdbsvr
    av_affinity: NotRequired[str]  # Affinity setting for AV scanning
    wad_affinity: NotRequired[str]  # Affinity setting for wad
    ips_affinity: NotRequired[str]  # Affinity setting for IPS
    miglog_affinity: NotRequired[str]  # Affinity setting for logging
    syslog_affinity: NotRequired[str]  # Affinity setting for syslog
    url_filter_affinity: NotRequired[str]  # URL filter CPU affinity.
    router_affinity: NotRequired[str]  # Affinity setting for BFD/VRRP/BGP/OSPF daemons
    ndp_max_entry: NotRequired[int]  # Maximum number of NDP table entries
    br_fdb_max_entry: NotRequired[int]  # Maximum number of bridge forwarding database (FDB) entries.
    max_route_cache_size: NotRequired[int]  # Maximum number of IP route cache entries (0 - 2147483647).
    ipsec_qat_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable QAT offloading (Intel QuickAssist) for IPsec
    device_idle_timeout: NotRequired[int]  # Time in seconds that a device must be idle to automatically
    user_device_store_max_devices: NotRequired[int]  # Maximum number of devices allowed in user device store.
    user_device_store_max_device_mem: NotRequired[int]  # Maximum percentage of total system memory allowed to be used
    user_device_store_max_users: NotRequired[int]  # Maximum number of users allowed in user device store.
    user_device_store_max_unified_mem: NotRequired[int]  # Maximum unified memory allowed in user device store.
    gui_device_latitude: NotRequired[str]  # Add the latitude of the location of this FortiGate to positi
    gui_device_longitude: NotRequired[str]  # Add the longitude of the location of this FortiGate to posit
    private_data_encryption: NotRequired[Literal["disable", "enable"]]  # Enable/disable private data encryption using an AES 128-bit
    auto_auth_extension_device: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic authorization of dedicated Fortinet
    gui_theme: NotRequired[Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"]]  # Color scheme for the administration GUI.
    gui_date_format: NotRequired[Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"]]  # Default date format used throughout GUI.
    gui_date_time_source: NotRequired[Literal["system", "browser"]]  # Source from which the FortiGate GUI uses to display date and
    igmp_state_limit: NotRequired[int]  # Maximum number of IGMP memberships
    cloud_communication: NotRequired[Literal["enable", "disable"]]  # Enable/disable all cloud communication.
    ipsec_ha_seqjump_rate: NotRequired[int]  # ESP jump ahead rate (1G - 10G pps equivalent).
    fortitoken_cloud: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiToken Cloud service.
    fortitoken_cloud_push_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable FTM push service of FortiToken Cloud.
    fortitoken_cloud_region: NotRequired[str]  # Region domain of FortiToken Cloud(unset to non-region).
    fortitoken_cloud_sync_interval: NotRequired[int]  # Interval in which to clean up remote users in FortiToken Clo
    faz_disk_buffer_size: NotRequired[int]  # Maximum disk buffer size to temporarily store logs destined
    irq_time_accounting: NotRequired[Literal["auto", "force"]]  # Configure CPU IRQ time accounting mode.
    management_ip: NotRequired[str]  # Management IP address of this FortiGate. Used to log into th
    management_port: NotRequired[int]  # Overriding port for management connection
    management_port_use_admin_sport: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of the admin-sport setting for the manage
    forticonverter_integration: NotRequired[Literal["enable", "disable"]]  # Enable/disable FortiConverter integration service.
    forticonverter_config_upload: NotRequired[Literal["once", "disable"]]  # Enable/disable config upload to FortiConverter.
    internet_service_database: NotRequired[Literal["mini", "standard", "full", "on-demand"]]  # Configure which Internet Service database size to download f
    internet_service_download_list: NotRequired[list[dict[str, Any]]]  # Configure which on-demand Internet Service IDs are to be dow
    geoip_full_db: NotRequired[Literal["enable", "disable"]]  # When enabled, the full geographic database will be loaded in
    early_tcp_npu_session: NotRequired[Literal["enable", "disable"]]  # Enable/disable early TCP NPU session.
    npu_neighbor_update: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending of ARP/ICMP6 probing packets to updat
    delay_tcp_npu_session: NotRequired[Literal["enable", "disable"]]  # Enable TCP NPU session delay to guarantee packet order of 3-
    interface_subnet_usage: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowing use of interface-subnet setting in f
    sflowd_max_children_num: NotRequired[int]  # Maximum number of sflowd child processes allowed to run.
    fortigslb_integration: NotRequired[Literal["disable", "enable"]]  # Enable/disable integration with the FortiGSLB cloud service.
    user_history_password_threshold: NotRequired[int]  # Maximum number of previous passwords saved per admin/user
    auth_session_auto_backup: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic and periodic backup of authenticati
    auth_session_auto_backup_interval: NotRequired[Literal["1min", "5min", "15min", "30min", "1hr"]]  # Configure automatic authentication session backup interval
    scim_https_port: NotRequired[int]  # SCIM port (0 - 65535, default = 44559).
    scim_http_port: NotRequired[int]  # SCIM http port (0 - 65535, default = 44558).
    scim_server_cert: NotRequired[str]  # Server certificate that the FortiGate uses for SCIM connecti
    application_bandwidth_tracking: NotRequired[Literal["disable", "enable"]]  # Enable/disable application bandwidth tracking.
    tls_session_cache: NotRequired[Literal["enable", "disable"]]  # Enable/disable TLS session cache.

# Nested classes for table field children

@final
class GlobalInternetservicedownloadlistObject:
    """Typed object for internet-service-download-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service ID.
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class GlobalResponse(TypedDict):
    """
    Type hints for system/global_ API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"]
    gui_ipv6: Literal["enable", "disable"]
    gui_replacement_message_groups: Literal["enable", "disable"]
    gui_local_out: Literal["enable", "disable"]
    gui_certificates: Literal["enable", "disable"]
    gui_custom_language: Literal["enable", "disable"]
    gui_wireless_opensecurity: Literal["enable", "disable"]
    gui_app_detection_sdwan: Literal["enable", "disable"]
    gui_display_hostname: Literal["enable", "disable"]
    gui_fortigate_cloud_sandbox: Literal["enable", "disable"]
    gui_firmware_upgrade_warning: Literal["enable", "disable"]
    gui_forticare_registration_setup_warning: Literal["enable", "disable"]
    gui_auto_upgrade_setup_warning: Literal["enable", "disable"]
    gui_workflow_management: Literal["enable", "disable"]
    gui_cdn_usage: Literal["enable", "disable"]
    admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"]
    admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"]
    admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"]
    admintimeout: int
    admin_console_timeout: int
    ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"]
    ssd_trim_hour: int
    ssd_trim_min: int
    ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    ssd_trim_date: int
    admin_concurrent: Literal["enable", "disable"]
    admin_lockout_threshold: int
    admin_lockout_duration: int
    refresh: int
    interval: int
    failtime: int
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    daily_restart: Literal["enable", "disable"]
    restart_time: str
    wad_restart_mode: Literal["none", "time", "memory"]
    wad_restart_start_time: str
    wad_restart_end_time: str
    wad_p2s_max_body_size: int
    radius_port: int
    speedtestd_server_port: int
    speedtestd_ctrl_port: int
    admin_login_max: int
    remoteauthtimeout: int
    ldapconntimeout: int
    batch_cmdb: Literal["enable", "disable"]
    multi_factor_authentication: Literal["optional", "mandatory"]
    ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    autorun_log_fsck: Literal["enable", "disable"]
    timezone: str
    traffic_priority: Literal["tos", "dscp"]
    traffic_priority_level: Literal["low", "medium", "high"]
    quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"]
    quic_max_datagram_size: int
    quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"]
    quic_ack_thresold: int
    quic_pmtud: Literal["enable", "disable"]
    quic_tls_handshake_timeout: int
    anti_replay: Literal["disable", "loose", "strict"]
    send_pmtu_icmp: Literal["enable", "disable"]
    honor_df: Literal["enable", "disable"]
    pmtu_discovery: Literal["enable", "disable"]
    revision_image_auto_backup: Literal["enable", "disable"]
    revision_backup_on_logout: Literal["enable", "disable"]
    management_vdom: str
    hostname: str
    alias: str
    strong_crypto: Literal["enable", "disable"]
    ssl_static_key_ciphers: Literal["enable", "disable"]
    snat_route_change: Literal["enable", "disable"]
    ipv6_snat_route_change: Literal["enable", "disable"]
    speedtest_server: Literal["enable", "disable"]
    cli_audit_log: Literal["enable", "disable"]
    dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]
    fds_statistics: Literal["enable", "disable"]
    fds_statistics_period: int
    tcp_option: Literal["enable", "disable"]
    lldp_transmission: Literal["enable", "disable"]
    lldp_reception: Literal["enable", "disable"]
    proxy_auth_timeout: int
    proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"]
    proxy_re_authentication_time: int
    proxy_auth_lifetime: Literal["enable", "disable"]
    proxy_auth_lifetime_timeout: int
    proxy_resource_mode: Literal["enable", "disable"]
    proxy_cert_use_mgmt_vdom: Literal["enable", "disable"]
    sys_perf_log_interval: int
    check_protocol_header: Literal["loose", "strict"]
    vip_arp_range: Literal["unlimited", "restricted"]
    reset_sessionless_tcp: Literal["enable", "disable"]
    allow_traffic_redirect: Literal["enable", "disable"]
    ipv6_allow_traffic_redirect: Literal["enable", "disable"]
    strict_dirty_session_check: Literal["enable", "disable"]
    tcp_halfclose_timer: int
    tcp_halfopen_timer: int
    tcp_timewait_timer: int
    tcp_rst_timer: int
    udp_idle_timer: int
    block_session_timer: int
    ip_src_port_range: str
    pre_login_banner: Literal["enable", "disable"]
    post_login_banner: Literal["disable", "enable"]
    tftp: Literal["enable", "disable"]
    av_failopen: Literal["pass", "off", "one-shot"]
    av_failopen_session: Literal["enable", "disable"]
    memory_use_threshold_extreme: int
    memory_use_threshold_red: int
    memory_use_threshold_green: int
    ip_fragment_mem_thresholds: int
    ip_fragment_timeout: int
    ipv6_fragment_timeout: int
    cpu_use_threshold: int
    log_single_cpu_high: Literal["enable", "disable"]
    check_reset_range: Literal["strict", "disable"]
    upgrade_report: Literal["enable", "disable"]
    admin_port: int
    admin_sport: int
    admin_host: str
    admin_https_redirect: Literal["enable", "disable"]
    admin_hsts_max_age: int
    admin_ssh_password: Literal["enable", "disable"]
    admin_restrict_local: Literal["all", "non-console-only", "disable"]
    admin_ssh_port: int
    admin_ssh_grace_time: int
    admin_ssh_v1: Literal["enable", "disable"]
    admin_telnet: Literal["enable", "disable"]
    admin_telnet_port: int
    admin_forticloud_sso_login: Literal["enable", "disable"]
    admin_forticloud_sso_default_profile: str
    default_service_source_port: str
    admin_server_cert: str
    admin_https_pki_required: Literal["enable", "disable"]
    wifi_certificate: str
    dhcp_lease_backup_interval: int
    wifi_ca_certificate: str
    auth_http_port: int
    auth_https_port: int
    auth_ike_saml_port: int
    auth_keepalive: Literal["enable", "disable"]
    policy_auth_concurrent: int
    auth_session_limit: Literal["block-new", "logout-inactive"]
    auth_cert: str
    clt_cert_req: Literal["enable", "disable"]
    fortiservice_port: int
    cfg_save: Literal["automatic", "manual", "revert"]
    cfg_revert_timeout: int
    reboot_upon_config_restore: Literal["enable", "disable"]
    admin_scp: Literal["enable", "disable"]
    wireless_controller: Literal["enable", "disable"]
    wireless_controller_port: int
    fortiextender_data_port: int
    fortiextender: Literal["disable", "enable"]
    extender_controller_reserved_network: str
    fortiextender_discovery_lockdown: Literal["disable", "enable"]
    fortiextender_vlan_mode: Literal["enable", "disable"]
    fortiextender_provision_on_authorization: Literal["enable", "disable"]
    switch_controller: Literal["disable", "enable"]
    switch_controller_reserved_network: str
    dnsproxy_worker_count: int
    url_filter_count: int
    httpd_max_worker_count: int
    proxy_worker_count: int
    scanunit_count: int
    fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"]
    ipv6_accept_dad: int
    ipv6_allow_anycast_probe: Literal["enable", "disable"]
    ipv6_allow_multicast_probe: Literal["enable", "disable"]
    ipv6_allow_local_in_silent_drop: Literal["enable", "disable"]
    csr_ca_attribute: Literal["enable", "disable"]
    wimax_4g_usb: Literal["enable", "disable"]
    cert_chain_max: int
    sslvpn_max_worker_count: int
    sslvpn_affinity: str
    sslvpn_web_mode: Literal["enable", "disable"]
    two_factor_ftk_expiry: int
    two_factor_email_expiry: int
    two_factor_sms_expiry: int
    two_factor_fac_expiry: int
    two_factor_ftm_expiry: int
    per_user_bal: Literal["enable", "disable"]
    wad_worker_count: int
    wad_worker_dev_cache: int
    wad_csvc_cs_count: int
    wad_csvc_db_count: int
    wad_source_affinity: Literal["disable", "enable"]
    wad_memory_change_granularity: int
    login_timestamp: Literal["enable", "disable"]
    ip_conflict_detection: Literal["enable", "disable"]
    miglogd_children: int
    log_daemon_cpu_threshold: int
    special_file_23_support: Literal["disable", "enable"]
    log_uuid_address: Literal["enable", "disable"]
    log_ssl_connection: Literal["enable", "disable"]
    gui_rest_api_cache: Literal["enable", "disable"]
    rest_api_key_url_query: Literal["enable", "disable"]
    arp_max_entry: int
    ha_affinity: str
    bfd_affinity: str
    cmdbsvr_affinity: str
    av_affinity: str
    wad_affinity: str
    ips_affinity: str
    miglog_affinity: str
    syslog_affinity: str
    url_filter_affinity: str
    router_affinity: str
    ndp_max_entry: int
    br_fdb_max_entry: int
    max_route_cache_size: int
    ipsec_qat_offload: Literal["enable", "disable"]
    device_idle_timeout: int
    user_device_store_max_devices: int
    user_device_store_max_device_mem: int
    user_device_store_max_users: int
    user_device_store_max_unified_mem: int
    gui_device_latitude: str
    gui_device_longitude: str
    private_data_encryption: Literal["disable", "enable"]
    auto_auth_extension_device: Literal["enable", "disable"]
    gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"]
    gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"]
    gui_date_time_source: Literal["system", "browser"]
    igmp_state_limit: int
    cloud_communication: Literal["enable", "disable"]
    ipsec_ha_seqjump_rate: int
    fortitoken_cloud: Literal["enable", "disable"]
    fortitoken_cloud_push_status: Literal["enable", "disable"]
    fortitoken_cloud_region: str
    fortitoken_cloud_sync_interval: int
    faz_disk_buffer_size: int
    irq_time_accounting: Literal["auto", "force"]
    management_ip: str
    management_port: int
    management_port_use_admin_sport: Literal["enable", "disable"]
    forticonverter_integration: Literal["enable", "disable"]
    forticonverter_config_upload: Literal["once", "disable"]
    internet_service_database: Literal["mini", "standard", "full", "on-demand"]
    internet_service_download_list: list[dict[str, Any]]
    geoip_full_db: Literal["enable", "disable"]
    early_tcp_npu_session: Literal["enable", "disable"]
    npu_neighbor_update: Literal["enable", "disable"]
    delay_tcp_npu_session: Literal["enable", "disable"]
    interface_subnet_usage: Literal["disable", "enable"]
    sflowd_max_children_num: int
    fortigslb_integration: Literal["disable", "enable"]
    user_history_password_threshold: int
    auth_session_auto_backup: Literal["enable", "disable"]
    auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"]
    scim_https_port: int
    scim_http_port: int
    scim_server_cert: str
    application_bandwidth_tracking: Literal["disable", "enable"]
    tls_session_cache: Literal["enable", "disable"]


@final
class GlobalObject:
    """Typed FortiObject for system/global_ with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # GUI display language.
    language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"]
    # Enable/disable IPv6 settings on the GUI.
    gui_ipv6: Literal["enable", "disable"]
    # Enable/disable replacement message groups on the GUI.
    gui_replacement_message_groups: Literal["enable", "disable"]
    # Enable/disable Local-out traffic on the GUI.
    gui_local_out: Literal["enable", "disable"]
    # Enable/disable the System > Certificate GUI page, allowing you to add and config
    gui_certificates: Literal["enable", "disable"]
    # Enable/disable custom languages in GUI.
    gui_custom_language: Literal["enable", "disable"]
    # Enable/disable wireless open security option on the GUI.
    gui_wireless_opensecurity: Literal["enable", "disable"]
    # Enable/disable Allow app-detection based SD-WAN.
    gui_app_detection_sdwan: Literal["enable", "disable"]
    # Enable/disable displaying the FortiGate's hostname on the GUI login page.
    gui_display_hostname: Literal["enable", "disable"]
    # Enable/disable displaying FortiGate Cloud Sandbox on the GUI.
    gui_fortigate_cloud_sandbox: Literal["enable", "disable"]
    # Enable/disable the firmware upgrade warning on the GUI.
    gui_firmware_upgrade_warning: Literal["enable", "disable"]
    # Enable/disable the FortiCare registration setup warning on the GUI.
    gui_forticare_registration_setup_warning: Literal["enable", "disable"]
    # Enable/disable the automatic patch upgrade setup prompt on the GUI.
    gui_auto_upgrade_setup_warning: Literal["enable", "disable"]
    # Enable/disable Workflow management features on the GUI.
    gui_workflow_management: Literal["enable", "disable"]
    # Enable/disable Load GUI static files from a CDN.
    gui_cdn_usage: Literal["enable", "disable"]
    # Allowed TLS versions for web administration.
    admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"]
    # Select one or more TLS 1.3 ciphersuites to enable. Does not affect ciphers in TL
    admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"]
    # Select one or more cipher technologies that cannot be used in GUI HTTPS negotiat
    admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"]
    # Number of minutes before an idle administrator session times out
    admintimeout: int
    # Console login timeout that overrides the admin timeout value
    admin_console_timeout: int
    # How often to run SSD Trim (default = weekly). SSD Trim prevents SSD drive data l
    ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"]
    # Hour of the day on which to run SSD Trim (0 - 23, default = 1).
    ssd_trim_hour: int
    # Minute of the hour on which to run SSD Trim (0 - 59, 60 for random).
    ssd_trim_min: int
    # Day of week to run SSD Trim.
    ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Date within a month to run ssd trim.
    ssd_trim_date: int
    # Enable/disable concurrent administrator logins. Use policy-auth-concurrent for f
    admin_concurrent: Literal["enable", "disable"]
    # Number of failed login attempts before an administrator account is locked out fo
    admin_lockout_threshold: int
    # Amount of time in seconds that an administrator account is locked out after reac
    admin_lockout_duration: int
    # Statistics refresh interval second(s) in GUI.
    refresh: int
    # Dead gateway detection interval.
    interval: int
    # Fail-time for server lost.
    failtime: int
    # Purdue Level of this FortiGate.
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # Enable/disable daily restart of FortiGate unit. Use the restart-time option to s
    daily_restart: Literal["enable", "disable"]
    # Daily restart time (hh:mm).
    restart_time: str
    # WAD worker restart mode (default = none).
    wad_restart_mode: Literal["none", "time", "memory"]
    # WAD workers daily restart time (hh:mm).
    wad_restart_start_time: str
    # WAD workers daily restart end time (hh:mm).
    wad_restart_end_time: str
    # Maximum size of the body of the local out HTTP request
    wad_p2s_max_body_size: int
    # RADIUS service port number.
    radius_port: int
    # Speedtest server port number.
    speedtestd_server_port: int
    # Speedtest server controller port number.
    speedtestd_ctrl_port: int
    # Maximum number of administrators who can be logged in at the same time
    admin_login_max: int
    # Number of seconds that the FortiGate waits for responses from remote RADIUS, LDA
    remoteauthtimeout: int
    # Global timeout for connections with remote LDAP servers in milliseconds
    ldapconntimeout: int
    # Enable/disable batch mode, allowing you to enter a series of CLI commands that w
    batch_cmdb: Literal["enable", "disable"]
    # Enforce all login methods to require an additional authentication factor
    multi_factor_authentication: Literal["optional", "mandatory"]
    # Minimum supported protocol version for SSL/TLS connections (default = TLSv1.2).
    ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Enable/disable automatic log partition check after ungraceful shutdown.
    autorun_log_fsck: Literal["enable", "disable"]
    # Timezone database name. Enter ? to view the list of timezone.
    timezone: str
    # Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for tr
    traffic_priority: Literal["tos", "dscp"]
    # Default system-wide level of priority for traffic prioritization.
    traffic_priority_level: Literal["low", "medium", "high"]
    # QUIC congestion control algorithm (default = cubic).
    quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"]
    # Maximum transmit datagram size (1200 - 1500, default = 1500).
    quic_max_datagram_size: int
    # Enable/disable UDP payload size shaping per connection ID (default = enable).
    quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"]
    # Maximum number of unacknowledged packets before sending ACK (2 - 5, default = 3)
    quic_ack_thresold: int
    # Enable/disable path MTU discovery (default = enable).
    quic_pmtud: Literal["enable", "disable"]
    # Time-to-live (TTL) for TLS handshake in seconds (1 - 60, default = 5).
    quic_tls_handshake_timeout: int
    # Level of checking for packet replay and TCP sequence checking.
    anti_replay: Literal["disable", "loose", "strict"]
    # Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destinati
    send_pmtu_icmp: Literal["enable", "disable"]
    # Enable/disable honoring of Don't-Fragment (DF) flag.
    honor_df: Literal["enable", "disable"]
    # Enable/disable path MTU discovery.
    pmtu_discovery: Literal["enable", "disable"]
    # Enable/disable back-up of the latest image revision after the firmware is upgrad
    revision_image_auto_backup: Literal["enable", "disable"]
    # Enable/disable back-up of the latest configuration revision when an administrato
    revision_backup_on_logout: Literal["enable", "disable"]
    # Management virtual domain name.
    management_vdom: str
    # FortiGate unit's hostname. Most models will truncate names longer than 24 charac
    hostname: str
    # Alias for your FortiGate unit.
    alias: str
    # Enable to use strong encryption and only allow strong ciphers and digest for HTT
    strong_crypto: Literal["enable", "disable"]
    # Enable/disable static key ciphers in SSL/TLS connections
    ssl_static_key_ciphers: Literal["enable", "disable"]
    # Enable/disable the ability to change the source NAT route.
    snat_route_change: Literal["enable", "disable"]
    # Enable/disable the ability to change the IPv6 source NAT route.
    ipv6_snat_route_change: Literal["enable", "disable"]
    # Enable/disable speed test server.
    speedtest_server: Literal["enable", "disable"]
    # Enable/disable CLI audit log.
    cli_audit_log: Literal["enable", "disable"]
    # Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.
    dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]
    # Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuar
    fds_statistics: Literal["enable", "disable"]
    # FortiGuard statistics collection period in minutes. (1 - 1440 min
    fds_statistics_period: int
    # Enable SACK, timestamp and MSS TCP options.
    tcp_option: Literal["enable", "disable"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
    lldp_transmission: Literal["enable", "disable"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) reception.
    lldp_reception: Literal["enable", "disable"]
    # Authentication timeout in minutes for authenticated users
    proxy_auth_timeout: int
    # Control if users must re-authenticate after a session is closed, traffic has bee
    proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"]
    # The time limit that users must re-authenticate if proxy-keep-alive-mode is set t
    proxy_re_authentication_time: int
    # Enable/disable authenticated users lifetime control. This is a cap on the total
    proxy_auth_lifetime: Literal["enable", "disable"]
    # Lifetime timeout in minutes for authenticated users
    proxy_auth_lifetime_timeout: int
    # Enable/disable use of the maximum memory usage on the FortiGate unit's proxy pro
    proxy_resource_mode: Literal["enable", "disable"]
    # Enable/disable using management VDOM to send requests.
    proxy_cert_use_mgmt_vdom: Literal["enable", "disable"]
    # Time in minutes between updates of performance statistics logging.
    sys_perf_log_interval: int
    # Level of checking performed on protocol headers. Strict checking is more thoroug
    check_protocol_header: Literal["loose", "strict"]
    # Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) addr
    vip_arp_range: Literal["unlimited", "restricted"]
    # Action to perform if the FortiGate receives a TCP packet but cannot find a corre
    reset_sessionless_tcp: Literal["enable", "disable"]
    # Disable to prevent traffic with same local ingress and egress interface from bei
    allow_traffic_redirect: Literal["enable", "disable"]
    # Disable to prevent IPv6 traffic with same local ingress and egress interface fro
    ipv6_allow_traffic_redirect: Literal["enable", "disable"]
    # Enable to check the session against the original policy when revalidating. This
    strict_dirty_session_check: Literal["enable", "disable"]
    # Number of seconds the FortiGate unit should wait to close a session after one pe
    tcp_halfclose_timer: int
    # Number of seconds the FortiGate unit should wait to close a session after one pe
    tcp_halfopen_timer: int
    # Length of the TCP TIME-WAIT state in seconds (1 - 300 sec, default = 1).
    tcp_timewait_timer: int
    # Length of the TCP CLOSE state in seconds (5 - 300 sec, default = 5).
    tcp_rst_timer: int
    # UDP connection session timeout. This command can be useful in managing CPU and m
    udp_idle_timer: int
    # Duration in seconds for blocked sessions (1 - 300 sec
    block_session_timer: int
    # IP source port range used for traffic originating from the FortiGate unit.
    ip_src_port_range: str
    # Enable/disable displaying the administrator access disclaimer message on the log
    pre_login_banner: Literal["enable", "disable"]
    # Enable/disable displaying the administrator access disclaimer message after an a
    post_login_banner: Literal["disable", "enable"]
    # Enable/disable TFTP.
    tftp: Literal["enable", "disable"]
    # Set the action to take if the FortiGate is running low on memory or the proxy co
    av_failopen: Literal["pass", "off", "one-shot"]
    # When enabled and a proxy for a protocol runs out of room in its session table, t
    av_failopen_session: Literal["enable", "disable"]
    # Threshold at which memory usage is considered extreme (new sessions are dropped)
    memory_use_threshold_extreme: int
    # Threshold at which memory usage forces the FortiGate to enter conserve mode
    memory_use_threshold_red: int
    # Threshold at which memory usage forces the FortiGate to exit conserve mode
    memory_use_threshold_green: int
    # Maximum memory (MB) used to reassemble IPv4/IPv6 fragments.
    ip_fragment_mem_thresholds: int
    # Timeout value in seconds for any fragment not being reassembled
    ip_fragment_timeout: int
    # Timeout value in seconds for any IPv6 fragment not being reassembled
    ipv6_fragment_timeout: int
    # Threshold at which CPU usage is reported (% of total CPU, default = 90).
    cpu_use_threshold: int
    # Enable/disable logging the event of a single CPU core reaching CPU usage thresho
    log_single_cpu_high: Literal["enable", "disable"]
    # Configure ICMP error message verification. You can either apply strict RST range
    check_reset_range: Literal["strict", "disable"]
    # Enable/disable the generation of an upgrade report when upgrading the firmware.
    upgrade_report: Literal["enable", "disable"]
    # Administrative access port for HTTP. (1 - 65535, default = 80).
    admin_port: int
    # Administrative access port for HTTPS. (1 - 65535, default = 443).
    admin_sport: int
    # Administrative host for HTTP and HTTPS. When set, will be used in lieu of the cl
    admin_host: str
    # Enable/disable redirection of HTTP administration access to HTTPS.
    admin_https_redirect: Literal["enable", "disable"]
    # HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will res
    admin_hsts_max_age: int
    # Enable/disable password authentication for SSH admin access.
    admin_ssh_password: Literal["enable", "disable"]
    # Enable/disable local admin authentication restriction when remote authenticator
    admin_restrict_local: Literal["all", "non-console-only", "disable"]
    # Administrative access port for SSH. (1 - 65535, default = 22).
    admin_ssh_port: int
    # Maximum time in seconds permitted between making an SSH connection to the FortiG
    admin_ssh_grace_time: int
    # Enable/disable SSH v1 compatibility.
    admin_ssh_v1: Literal["enable", "disable"]
    # Enable/disable TELNET service.
    admin_telnet: Literal["enable", "disable"]
    # Administrative access port for TELNET. (1 - 65535, default = 23).
    admin_telnet_port: int
    # Enable/disable FortiCloud admin login via SSO.
    admin_forticloud_sso_login: Literal["enable", "disable"]
    # Override access profile.
    admin_forticloud_sso_default_profile: str
    # Default service source port range (default = 1 - 65535).
    default_service_source_port: str
    # Server certificate that the FortiGate uses for HTTPS administrative connections.
    admin_server_cert: str
    # Enable/disable admin login method. Enable to force administrators to provide a v
    admin_https_pki_required: Literal["enable", "disable"]
    # Certificate to use for WiFi authentication.
    wifi_certificate: str
    # DHCP leases backup interval in seconds (10 - 3600, default = 60).
    dhcp_lease_backup_interval: int
    # CA certificate that verifies the WiFi certificate.
    wifi_ca_certificate: str
    # User authentication HTTP port. (1 - 65535, default = 1000).
    auth_http_port: int
    # User authentication HTTPS port. (1 - 65535, default = 1003).
    auth_https_port: int
    # User IKE SAML authentication port (0 - 65535, default = 1001).
    auth_ike_saml_port: int
    # Enable to prevent user authentication sessions from timing out when idle.
    auth_keepalive: Literal["enable", "disable"]
    # Number of concurrent firewall use logins from the same user
    policy_auth_concurrent: int
    # Action to take when the number of allowed user authenticated sessions is reached
    auth_session_limit: Literal["block-new", "logout-inactive"]
    # Server certificate that the FortiGate uses for HTTPS firewall authentication con
    auth_cert: str
    # Enable/disable requiring administrators to have a client certificate to log into
    clt_cert_req: Literal["enable", "disable"]
    # FortiService port (1 - 65535, default = 8013). Used by FortiClient endpoint comp
    fortiservice_port: int
    # Configuration file save mode for CLI changes.
    cfg_save: Literal["automatic", "manual", "revert"]
    # Time-out for reverting to the last saved configuration.
    cfg_revert_timeout: int
    # Enable/disable reboot of system upon restoring configuration.
    reboot_upon_config_restore: Literal["enable", "disable"]
    # Enable/disable SCP support for system configuration backup, restore, and firmwar
    admin_scp: Literal["enable", "disable"]
    # Enable/disable the wireless controller feature to use the FortiGate unit to mana
    wireless_controller: Literal["enable", "disable"]
    # Port used for the control channel in wireless controller mode
    wireless_controller_port: int
    # FortiExtender data port (1024 - 49150, default = 25246).
    fortiextender_data_port: int
    # Enable/disable FortiExtender.
    fortiextender: Literal["disable", "enable"]
    # Configure reserved network subnet for managed LAN extension FortiExtender units.
    extender_controller_reserved_network: str
    # Enable/disable FortiExtender CAPWAP lockdown.
    fortiextender_discovery_lockdown: Literal["disable", "enable"]
    # Enable/disable FortiExtender VLAN mode.
    fortiextender_vlan_mode: Literal["enable", "disable"]
    # Enable/disable automatic provisioning of latest FortiExtender firmware on author
    fortiextender_provision_on_authorization: Literal["enable", "disable"]
    # Enable/disable switch controller feature. Switch controller allows you to manage
    switch_controller: Literal["disable", "enable"]
    # Configure reserved network subnet for managed switches. This is available when t
    switch_controller_reserved_network: str
    # DNS proxy worker count. For a FortiGate with multiple logical CPUs, you can set
    dnsproxy_worker_count: int
    # URL filter daemon count.
    url_filter_count: int
    # Maximum number of simultaneous HTTP requests that will be served. This number ma
    httpd_max_worker_count: int
    # Proxy worker count.
    proxy_worker_count: int
    # Number of scanunits. The range and the default depend on the number of CPUs. Onl
    scanunit_count: int
    # Type of alert to retrieve from FortiGuard.
    fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"]
    # Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD).
    ipv6_accept_dad: int
    # Enable/disable IPv6 address probe through Anycast.
    ipv6_allow_anycast_probe: Literal["enable", "disable"]
    # Enable/disable IPv6 address probe through Multicast.
    ipv6_allow_multicast_probe: Literal["enable", "disable"]
    # Enable/disable silent drop of IPv6 local-in traffic.
    ipv6_allow_local_in_silent_drop: Literal["enable", "disable"]
    # Enable/disable the CA attribute in certificates. Some CA servers reject CSRs tha
    csr_ca_attribute: Literal["enable", "disable"]
    # Enable/disable comparability with WiMAX 4G USB devices.
    wimax_4g_usb: Literal["enable", "disable"]
    # Maximum number of certificates that can be traversed in a certificate chain.
    cert_chain_max: int
    # Maximum number of Agentless VPN processes. Upper limit for this value is the num
    sslvpn_max_worker_count: int
    # Agentless VPN CPU affinity.
    sslvpn_affinity: str
    # Enable/disable Agentless VPN web mode.
    sslvpn_web_mode: Literal["enable", "disable"]
    # FortiToken authentication session timeout (60 - 600 sec
    two_factor_ftk_expiry: int
    # Email-based two-factor authentication session timeout (30 - 300 seconds
    two_factor_email_expiry: int
    # SMS-based two-factor authentication session timeout (30 - 300 sec, default = 60)
    two_factor_sms_expiry: int
    # FortiAuthenticator token authentication session timeout (10 - 3600 seconds
    two_factor_fac_expiry: int
    # FortiToken Mobile session timeout (1 - 168 hours (7 days), default = 72).
    two_factor_ftm_expiry: int
    # Enable/disable per-user block/allow list filter.
    per_user_bal: Literal["enable", "disable"]
    # Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN
    wad_worker_count: int
    # Number of cached devices for each ZTNA proxy worker. The default value is tuned
    wad_worker_dev_cache: int
    # Number of concurrent WAD-cache-service object-cache processes.
    wad_csvc_cs_count: int
    # Number of concurrent WAD-cache-service byte-cache processes.
    wad_csvc_db_count: int
    # Enable/disable dispatching traffic to WAD workers based on source affinity.
    wad_source_affinity: Literal["disable", "enable"]
    # Minimum percentage change in system memory usage detected by the wad daemon prio
    wad_memory_change_granularity: int
    # Enable/disable login time recording.
    login_timestamp: Literal["enable", "disable"]
    # Enable/disable logging of IPv4 address conflict detection.
    ip_conflict_detection: Literal["enable", "disable"]
    # Number of logging (miglogd) processes to be allowed to run. Higher number can re
    miglogd_children: int
    # Configure syslog daemon process spawning threshold. Use a percentage threshold o
    log_daemon_cpu_threshold: int
    # Enable/disable detection of those special format files when using Data Loss Prev
    special_file_23_support: Literal["disable", "enable"]
    # Enable/disable insertion of address UUIDs to traffic logs.
    log_uuid_address: Literal["enable", "disable"]
    # Enable/disable logging of SSL connection events.
    log_ssl_connection: Literal["enable", "disable"]
    # Enable/disable REST API result caching on FortiGate.
    gui_rest_api_cache: Literal["enable", "disable"]
    # Enable/disable support for passing REST API keys through URL query parameters.
    rest_api_key_url_query: Literal["enable", "disable"]
    # Maximum number of dynamically learned MAC addresses that can be added to the ARP
    arp_max_entry: int
    # Affinity setting for HA daemons
    ha_affinity: str
    # Affinity setting for BFD daemon
    bfd_affinity: str
    # Affinity setting for cmdbsvr
    cmdbsvr_affinity: str
    # Affinity setting for AV scanning
    av_affinity: str
    # Affinity setting for wad
    wad_affinity: str
    # Affinity setting for IPS
    ips_affinity: str
    # Affinity setting for logging
    miglog_affinity: str
    # Affinity setting for syslog
    syslog_affinity: str
    # URL filter CPU affinity.
    url_filter_affinity: str
    # Affinity setting for BFD/VRRP/BGP/OSPF daemons
    router_affinity: str
    # Maximum number of NDP table entries
    ndp_max_entry: int
    # Maximum number of bridge forwarding database (FDB) entries.
    br_fdb_max_entry: int
    # Maximum number of IP route cache entries (0 - 2147483647).
    max_route_cache_size: int
    # Enable/disable QAT offloading (Intel QuickAssist) for IPsec VPN traffic. QuickAs
    ipsec_qat_offload: Literal["enable", "disable"]
    # Time in seconds that a device must be idle to automatically log the device user
    device_idle_timeout: int
    # Maximum number of devices allowed in user device store.
    user_device_store_max_devices: int
    # Maximum percentage of total system memory allowed to be used for devices in the
    user_device_store_max_device_mem: int
    # Maximum number of users allowed in user device store.
    user_device_store_max_users: int
    # Maximum unified memory allowed in user device store.
    user_device_store_max_unified_mem: int
    # Add the latitude of the location of this FortiGate to position it on the Threat
    gui_device_latitude: str
    # Add the longitude of the location of this FortiGate to position it on the Threat
    gui_device_longitude: str
    # Enable/disable private data encryption using an AES 128-bit key or passpharse.
    private_data_encryption: Literal["disable", "enable"]
    # Enable/disable automatic authorization of dedicated Fortinet extension devices.
    auto_auth_extension_device: Literal["enable", "disable"]
    # Color scheme for the administration GUI.
    gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"]
    # Default date format used throughout GUI.
    gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"]
    # Source from which the FortiGate GUI uses to display date and time entries.
    gui_date_time_source: Literal["system", "browser"]
    # Maximum number of IGMP memberships (96 - 64000, default = 3200).
    igmp_state_limit: int
    # Enable/disable all cloud communication.
    cloud_communication: Literal["enable", "disable"]
    # ESP jump ahead rate (1G - 10G pps equivalent).
    ipsec_ha_seqjump_rate: int
    # Enable/disable FortiToken Cloud service.
    fortitoken_cloud: Literal["enable", "disable"]
    # Enable/disable FTM push service of FortiToken Cloud.
    fortitoken_cloud_push_status: Literal["enable", "disable"]
    # Region domain of FortiToken Cloud(unset to non-region).
    fortitoken_cloud_region: str
    # Interval in which to clean up remote users in FortiToken Cloud (0 - 336 hours
    fortitoken_cloud_sync_interval: int
    # Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. T
    faz_disk_buffer_size: int
    # Configure CPU IRQ time accounting mode.
    irq_time_accounting: Literal["auto", "force"]
    # Management IP address of this FortiGate. Used to log into this FortiGate from an
    management_ip: str
    # Overriding port for management connection (Overrides admin port).
    management_port: int
    # Enable/disable use of the admin-sport setting for the management port. If disabl
    management_port_use_admin_sport: Literal["enable", "disable"]
    # Enable/disable FortiConverter integration service.
    forticonverter_integration: Literal["enable", "disable"]
    # Enable/disable config upload to FortiConverter.
    forticonverter_config_upload: Literal["once", "disable"]
    # Configure which Internet Service database size to download from FortiGuard and u
    internet_service_database: Literal["mini", "standard", "full", "on-demand"]
    # Configure which on-demand Internet Service IDs are to be downloaded.
    internet_service_download_list: list[GlobalInternetservicedownloadlistObject]  # Table field - list of typed objects
    # When enabled, the full geographic database will be loaded into the kernel which
    geoip_full_db: Literal["enable", "disable"]
    # Enable/disable early TCP NPU session.
    early_tcp_npu_session: Literal["enable", "disable"]
    # Enable/disable sending of ARP/ICMP6 probing packets to update neighbors for offl
    npu_neighbor_update: Literal["enable", "disable"]
    # Enable TCP NPU session delay to guarantee packet order of 3-way handshake.
    delay_tcp_npu_session: Literal["enable", "disable"]
    # Enable/disable allowing use of interface-subnet setting in firewall addresses
    interface_subnet_usage: Literal["disable", "enable"]
    # Maximum number of sflowd child processes allowed to run.
    sflowd_max_children_num: int
    # Enable/disable integration with the FortiGSLB cloud service.
    fortigslb_integration: Literal["disable", "enable"]
    # Maximum number of previous passwords saved per admin/user (3 - 15, default = 3).
    user_history_password_threshold: int
    # Enable/disable automatic and periodic backup of authentication sessions
    auth_session_auto_backup: Literal["enable", "disable"]
    # Configure automatic authentication session backup interval (default = 15min).
    auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"]
    # SCIM port (0 - 65535, default = 44559).
    scim_https_port: int
    # SCIM http port (0 - 65535, default = 44558).
    scim_http_port: int
    # Server certificate that the FortiGate uses for SCIM connections.
    scim_server_cert: str
    # Enable/disable application bandwidth tracking.
    application_bandwidth_tracking: Literal["disable", "enable"]
    # Enable/disable TLS session cache.
    tls_session_cache: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Global:
    """
    Configure global attributes.
    
    Path: system/global_
    Category: cmdb
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> GlobalResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> GlobalResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> GlobalResponse: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "Global",
    "GlobalPayload",
    "GlobalObject",
]