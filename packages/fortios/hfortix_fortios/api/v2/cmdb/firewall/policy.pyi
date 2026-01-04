from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class PolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/policy payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: PolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    policyid: NotRequired[int]  # Policy ID (0 - 4294967294).
    status: NotRequired[Literal["enable", "disable"]]  # Enable or disable this policy.
    name: NotRequired[str]  # Policy name.
    uuid: NotRequired[str]  # Universally Unique Identifier (UUID; automatically assigned 
    srcintf: list[dict[str, Any]]  # Incoming (ingress) interface.
    dstintf: list[dict[str, Any]]  # Outgoing (egress) interface.
    action: NotRequired[Literal["accept", "deny", "ipsec"]]  # Policy action (accept/deny/ipsec).
    nat64: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT64.
    nat46: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46.
    ztna_status: NotRequired[Literal["enable", "disable"]]  # Enable/disable zero trust access.
    ztna_device_ownership: NotRequired[Literal["enable", "disable"]]  # Enable/disable zero trust device ownership.
    srcaddr: NotRequired[list[dict[str, Any]]]  # Source IPv4 address and address group names.
    dstaddr: NotRequired[list[dict[str, Any]]]  # Destination IPv4 address and address group names.
    srcaddr6: NotRequired[list[dict[str, Any]]]  # Source IPv6 address name and address group names.
    dstaddr6: NotRequired[list[dict[str, Any]]]  # Destination IPv6 address name and address group names.
    ztna_ems_tag: NotRequired[list[dict[str, Any]]]  # Source ztna-ems-tag names.
    ztna_ems_tag_secondary: NotRequired[list[dict[str, Any]]]  # Source ztna-ems-tag-secondary names.
    ztna_tags_match_logic: NotRequired[Literal["or", "and"]]  # ZTNA tag matching logic.
    ztna_geo_tag: NotRequired[list[dict[str, Any]]]  # Source ztna-geo-tag names.
    internet_service: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services for this policy. If 
    internet_service_name: NotRequired[list[dict[str, Any]]]  # Internet Service name.
    internet_service_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service name.
    network_service_dynamic: NotRequired[list[dict[str, Any]]]  # Dynamic Network Service name.
    internet_service_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service group name.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this p
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    network_service_src_dynamic: NotRequired[list[dict[str, Any]]]  # Dynamic Network Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    reputation_minimum: NotRequired[int]  # Minimum Reputation to take action.
    reputation_direction: NotRequired[Literal["source", "destination"]]  # Direction of the initial traffic for reputation to take effe
    src_vendor_mac: NotRequired[list[dict[str, Any]]]  # Vendor MAC source ID.
    internet_service6: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services for this policy
    internet_service6_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service name.
    internet_service6_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service6_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service name.
    internet_service6_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service6 group name.
    internet_service6_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services in source for t
    internet_service6_src_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service source name.
    internet_service6_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service6 source group name.
    internet_service6_src_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service6 source group name.
    reputation_minimum6: NotRequired[int]  # IPv6 Minimum Reputation to take action.
    reputation_direction6: NotRequired[Literal["source", "destination"]]  # Direction of the initial traffic for IPv6 reputation to take
    rtp_nat: NotRequired[Literal["disable", "enable"]]  # Enable Real Time Protocol (RTP) NAT.
    rtp_addr: list[dict[str, Any]]  # Address names if this is an RTP NAT policy.
    send_deny_packet: NotRequired[Literal["disable", "enable"]]  # Enable to send a reply when a session is denied or blocked b
    firewall_session_dirty: NotRequired[Literal["check-all", "check-new"]]  # How to handle sessions if the configuration of this firewall
    schedule: str  # Schedule name.
    schedule_timeout: NotRequired[Literal["enable", "disable"]]  # Enable to force current sessions to end when the schedule ob
    policy_expiry: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy expiry.
    policy_expiry_date: NotRequired[str]  # Policy expiry date (YYYY-MM-DD HH:MM:SS).
    policy_expiry_date_utc: NotRequired[str]  # Policy expiry date and time, in epoch format.
    service: NotRequired[list[dict[str, Any]]]  # Service and service group names.
    tos_mask: NotRequired[str]  # Non-zero bit positions are used for comparison while zero bi
    tos: NotRequired[str]  # ToS (Type of Service) value used for comparison.
    tos_negate: NotRequired[Literal["enable", "disable"]]  # Enable negated TOS match.
    anti_replay: NotRequired[Literal["enable", "disable"]]  # Enable/disable anti-replay check.
    tcp_session_without_syn: NotRequired[Literal["all", "data-only", "disable"]]  # Enable/disable creation of TCP session without SYN flag.
    geoip_anycast: NotRequired[Literal["enable", "disable"]]  # Enable/disable recognition of anycast IP addresses using the
    geoip_match: NotRequired[Literal["physical-location", "registered-location"]]  # Match geography address based either on its physical locatio
    dynamic_shaping: NotRequired[Literal["enable", "disable"]]  # Enable/disable dynamic RADIUS defined traffic shaping.
    passive_wan_health_measurement: NotRequired[Literal["enable", "disable"]]  # Enable/disable passive WAN health measurement. When enabled,
    app_monitor: NotRequired[Literal["enable", "disable"]]  # Enable/disable application TCP metrics in session logs.When 
    utm_status: NotRequired[Literal["enable", "disable"]]  # Enable to add one or more security profiles (AV, IPS, etc.) 
    inspection_mode: NotRequired[Literal["proxy", "flow"]]  # Policy inspection mode (Flow/proxy). Default is Flow mode.
    http_policy_redirect: NotRequired[Literal["enable", "disable", "legacy"]]  # Redirect HTTP(S) traffic to matching transparent web proxy p
    ssh_policy_redirect: NotRequired[Literal["enable", "disable"]]  # Redirect SSH traffic to matching transparent proxy policy.
    ztna_policy_redirect: NotRequired[Literal["enable", "disable"]]  # Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
    webproxy_profile: NotRequired[str]  # Webproxy profile name.
    profile_type: NotRequired[Literal["single", "group"]]  # Determine whether the firewall policy allows security profil
    profile_group: NotRequired[str]  # Name of profile group.
    profile_protocol_options: NotRequired[str]  # Name of an existing Protocol options profile.
    ssl_ssh_profile: NotRequired[str]  # Name of an existing SSL SSH profile.
    av_profile: NotRequired[str]  # Name of an existing Antivirus profile.
    webfilter_profile: NotRequired[str]  # Name of an existing Web filter profile.
    dnsfilter_profile: NotRequired[str]  # Name of an existing DNS filter profile.
    emailfilter_profile: NotRequired[str]  # Name of an existing email filter profile.
    dlp_profile: NotRequired[str]  # Name of an existing DLP profile.
    file_filter_profile: NotRequired[str]  # Name of an existing file-filter profile.
    ips_sensor: NotRequired[str]  # Name of an existing IPS sensor.
    application_list: NotRequired[str]  # Name of an existing Application list.
    voip_profile: NotRequired[str]  # Name of an existing VoIP (voipd) profile.
    ips_voip_filter: NotRequired[str]  # Name of an existing VoIP (ips) profile.
    sctp_filter_profile: NotRequired[str]  # Name of an existing SCTP filter profile.
    diameter_filter_profile: NotRequired[str]  # Name of an existing Diameter filter profile.
    virtual_patch_profile: NotRequired[str]  # Name of an existing virtual-patch profile.
    icap_profile: NotRequired[str]  # Name of an existing ICAP profile.
    videofilter_profile: NotRequired[str]  # Name of an existing VideoFilter profile.
    waf_profile: NotRequired[str]  # Name of an existing Web application firewall profile.
    ssh_filter_profile: NotRequired[str]  # Name of an existing SSH filter profile.
    casb_profile: NotRequired[str]  # Name of an existing CASB profile.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Enable or disable logging. Log all sessions or security prof
    logtraffic_start: NotRequired[Literal["enable", "disable"]]  # Record logs when a session starts.
    log_http_transaction: NotRequired[Literal["enable", "disable"]]  # Enable/disable HTTP transaction log.
    capture_packet: NotRequired[Literal["enable", "disable"]]  # Enable/disable capture packets.
    auto_asic_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable policy traffic ASIC offloading.
    wanopt: NotRequired[Literal["enable", "disable"]]  # Enable/disable WAN optimization.
    wanopt_detection: NotRequired[Literal["active", "passive", "off"]]  # WAN optimization auto-detection mode.
    wanopt_passive_opt: NotRequired[Literal["default", "transparent", "non-transparent"]]  # WAN optimization passive mode options. This option decides w
    wanopt_profile: str  # WAN optimization profile.
    wanopt_peer: str  # WAN optimization peer.
    webcache: NotRequired[Literal["enable", "disable"]]  # Enable/disable web cache.
    webcache_https: NotRequired[Literal["disable", "enable"]]  # Enable/disable web cache for HTTPS.
    webproxy_forward_server: NotRequired[str]  # Webproxy forward server name.
    traffic_shaper: NotRequired[str]  # Traffic shaper.
    traffic_shaper_reverse: NotRequired[str]  # Reverse traffic shaper.
    per_ip_shaper: NotRequired[str]  # Per-IP traffic shaper.
    nat: NotRequired[Literal["enable", "disable"]]  # Enable/disable source NAT.
    pcp_outbound: NotRequired[Literal["enable", "disable"]]  # Enable/disable PCP outbound SNAT.
    pcp_inbound: NotRequired[Literal["enable", "disable"]]  # Enable/disable PCP inbound DNAT.
    pcp_poolname: NotRequired[list[dict[str, Any]]]  # PCP pool names.
    permit_any_host: NotRequired[Literal["enable", "disable"]]  # Accept UDP packets from any host.
    permit_stun_host: NotRequired[Literal["enable", "disable"]]  # Accept UDP packets from any Session Traversal Utilities for 
    fixedport: NotRequired[Literal["enable", "disable"]]  # Enable to prevent source NAT from changing a session's sourc
    port_preserve: NotRequired[Literal["enable", "disable"]]  # Enable/disable preservation of the original source port from
    port_random: NotRequired[Literal["enable", "disable"]]  # Enable/disable random source port selection for source NAT.
    ippool: NotRequired[Literal["enable", "disable"]]  # Enable to use IP Pools for source NAT.
    poolname: NotRequired[list[dict[str, Any]]]  # IP Pool names.
    poolname6: NotRequired[list[dict[str, Any]]]  # IPv6 pool names.
    session_ttl: NotRequired[str]  # TTL in seconds for sessions accepted by this policy (0 means
    vlan_cos_fwd: NotRequired[int]  # VLAN forward direction user priority: 255 passthrough, 0 low
    vlan_cos_rev: NotRequired[int]  # VLAN reverse direction user priority: 255 passthrough, 0 low
    inbound: NotRequired[Literal["enable", "disable"]]  # Policy-based IPsec VPN: only traffic from the remote network
    outbound: NotRequired[Literal["enable", "disable"]]  # Policy-based IPsec VPN: only traffic from the internal netwo
    natinbound: NotRequired[Literal["enable", "disable"]]  # Policy-based IPsec VPN: apply destination NAT to inbound tra
    natoutbound: NotRequired[Literal["enable", "disable"]]  # Policy-based IPsec VPN: apply source NAT to outbound traffic
    fec: NotRequired[Literal["enable", "disable"]]  # Enable/disable Forward Error Correction on traffic matching 
    wccp: NotRequired[Literal["enable", "disable"]]  # Enable/disable forwarding traffic matching this policy to a 
    ntlm: NotRequired[Literal["enable", "disable"]]  # Enable/disable NTLM authentication.
    ntlm_guest: NotRequired[Literal["enable", "disable"]]  # Enable/disable NTLM guest user access.
    ntlm_enabled_browsers: NotRequired[list[dict[str, Any]]]  # HTTP-User-Agent value of supported browsers.
    fsso_agent_for_ntlm: NotRequired[str]  # FSSO agent to use for NTLM authentication.
    groups: NotRequired[list[dict[str, Any]]]  # Names of user groups that can authenticate with this policy.
    users: NotRequired[list[dict[str, Any]]]  # Names of individual users that can authenticate with this po
    fsso_groups: NotRequired[list[dict[str, Any]]]  # Names of FSSO groups.
    scim: NotRequired[Literal["enable", "disable"]]  # Enable/disable SCIM (default = disable).
    saml_server: NotRequired[str]  # SAML server name.
    scim_users: NotRequired[list[dict[str, Any]]]  # Names of SCIM users.
    scim_groups: NotRequired[list[dict[str, Any]]]  # Names of SCIM groups.
    auth_path: NotRequired[Literal["enable", "disable"]]  # Enable/disable authentication-based routing.
    disclaimer: NotRequired[Literal["enable", "disable"]]  # Enable/disable user authentication disclaimer.
    email_collect: NotRequired[Literal["enable", "disable"]]  # Enable/disable email collection.
    vpntunnel: str  # Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
    natip: NotRequired[str]  # Policy-based IPsec VPN: source NAT IP address for outgoing t
    match_vip: NotRequired[Literal["enable", "disable"]]  # Enable to match packets that have had their destination addr
    match_vip_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable matching of only those packets that have had 
    diffserv_copy: NotRequired[Literal["enable", "disable"]]  # Enable to copy packet's DiffServ values from session's origi
    diffserv_forward: NotRequired[Literal["enable", "disable"]]  # Enable to change packet's DiffServ values to the specified d
    diffserv_reverse: NotRequired[Literal["enable", "disable"]]  # Enable to change packet's reverse (reply) DiffServ values to
    diffservcode_forward: NotRequired[str]  # Change packet's DiffServ to this value.
    diffservcode_rev: NotRequired[str]  # Change packet's reverse (reply) DiffServ to this value.
    tcp_mss_sender: NotRequired[int]  # Sender TCP maximum segment size (MSS).
    tcp_mss_receiver: NotRequired[int]  # Receiver TCP maximum segment size (MSS).
    comments: NotRequired[str]  # Comment.
    auth_cert: NotRequired[str]  # HTTPS server certificate for policy authentication.
    auth_redirect_addr: NotRequired[str]  # HTTP-to-HTTPS redirect address for firewall authentication.
    redirect_url: NotRequired[str]  # URL users are directed to after seeing and accepting the dis
    identity_based_route: NotRequired[str]  # Name of identity-based routing rule.
    block_notification: NotRequired[Literal["enable", "disable"]]  # Enable/disable block notification.
    custom_log_fields: NotRequired[list[dict[str, Any]]]  # Custom fields to append to log messages for this policy.
    replacemsg_override_group: NotRequired[str]  # Override the default replacement message group for this poli
    srcaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr specifies what the source address must 
    srcaddr6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr6 specifies what the source address must
    dstaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr specifies what the destination address 
    dstaddr6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr6 specifies what the destination address
    ztna_ems_tag_negate: NotRequired[Literal["enable", "disable"]]  # When enabled ztna-ems-tag specifies what the tags must NOT b
    service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled service specifies what the service must NOT be.
    internet_service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service specifies what the service mus
    internet_service_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service-src specifies what the service
    internet_service6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6 specifies what the service mu
    internet_service6_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6-src specifies what the servic
    timeout_send_rst: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending RST packets when TCP sessions expire.
    captive_portal_exempt: NotRequired[Literal["enable", "disable"]]  # Enable to exempt some users from the captive portal.
    decrypted_traffic_mirror: NotRequired[str]  # Decrypted traffic mirror.
    dsri: NotRequired[Literal["enable", "disable"]]  # Enable DSRI to ignore HTTP server responses.
    radius_mac_auth_bypass: NotRequired[Literal["enable", "disable"]]  # Enable MAC authentication bypass. The bypassed MAC address m
    radius_ip_auth_bypass: NotRequired[Literal["enable", "disable"]]  # Enable IP authentication bypass. The bypassed IP address mus
    delay_tcp_npu_session: NotRequired[Literal["enable", "disable"]]  # Enable TCP NPU session delay to guarantee packet order of 3-
    vlan_filter: NotRequired[str]  # VLAN ranges to allow
    sgt_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable security group tags (SGT) check.
    sgt: NotRequired[list[dict[str, Any]]]  # Security group tags.
    internet_service_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service name.
    internet_service_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service source name.
    internet_service6_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard IPv6 Internet Service name.
    internet_service6_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard IPv6 Internet Service source name.


class Policy:
    """
    Configure IPv4/IPv6 policies.
    
    Path: firewall/policy
    Category: cmdb
    Primary Key: policyid
    """
    
    def get(
        self,
        policyid: int | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        ztna_ems_tag: list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: list[dict[str, Any]] | None = ...,
        dstintf: list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: list[dict[str, Any]] | None = ...,
        dstaddr: list[dict[str, Any]] | None = ...,
        srcaddr6: list[dict[str, Any]] | None = ...,
        dstaddr6: list[dict[str, Any]] | None = ...,
        ztna_ems_tag: list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: PolicyPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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