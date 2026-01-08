from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete
class PolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/policy payload fields.
    
    Configure IPv4/IPv6 policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.diameter-filter.profile.ProfileEndpoint` (via: diameter-filter-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.identity-based-route.IdentityBasedRouteEndpoint` (via: identity-based-route)
        - ... and 28 more dependencies

    **Usage:**
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
    permit_any_host: NotRequired[Literal["enable", "disable"]]  # Enable/disable fullcone NAT. Accept UDP packets from any hos
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


class PolicyObject(FortiObject[PolicyPayload]):
    """Typed FortiObject for firewall/policy with IDE autocomplete support."""
    
    # Policy ID (0 - 4294967294).
    policyid: int
    # Enable or disable this policy.
    status: Literal["enable", "disable"]
    # Policy name.
    name: str
    # Universally Unique Identifier (UUID; automatically assigned but can be manually 
    uuid: str
    # Incoming (ingress) interface.
    srcintf: list[str]  # Auto-flattened from member_table
    # Outgoing (egress) interface.
    dstintf: list[str]  # Auto-flattened from member_table
    # Policy action (accept/deny/ipsec).
    action: Literal["accept", "deny", "ipsec"]
    # Enable/disable NAT64.
    nat64: Literal["enable", "disable"]
    # Enable/disable NAT46.
    nat46: Literal["enable", "disable"]
    # Enable/disable zero trust access.
    ztna_status: Literal["enable", "disable"]
    # Enable/disable zero trust device ownership.
    ztna_device_ownership: Literal["enable", "disable"]
    # Source IPv4 address and address group names.
    srcaddr: list[str]  # Auto-flattened from member_table
    # Destination IPv4 address and address group names.
    dstaddr: list[str]  # Auto-flattened from member_table
    # Source IPv6 address name and address group names.
    srcaddr6: list[str]  # Auto-flattened from member_table
    # Destination IPv6 address name and address group names.
    dstaddr6: list[str]  # Auto-flattened from member_table
    # Source ztna-ems-tag names.
    ztna_ems_tag: list[str]  # Auto-flattened from member_table
    # Source ztna-ems-tag-secondary names.
    ztna_ems_tag_secondary: list[str]  # Auto-flattened from member_table
    # ZTNA tag matching logic.
    ztna_tags_match_logic: Literal["or", "and"]
    # Source ztna-geo-tag names.
    ztna_geo_tag: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services for this policy. If enabled, destination
    internet_service: Literal["enable", "disable"]
    # Internet Service name.
    internet_service_name: list[str]  # Auto-flattened from member_table
    # Internet Service group name.
    internet_service_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service name.
    internet_service_custom: list[str]  # Auto-flattened from member_table
    # Dynamic Network Service name.
    network_service_dynamic: list[str]  # Auto-flattened from member_table
    # Custom Internet Service group name.
    internet_service_custom_group: list[str]  # Auto-flattened from member_table
    # Enable/disable use of Internet Services in source for this policy. If enabled, s
    internet_service_src: Literal["enable", "disable"]
    # Internet Service source name.
    internet_service_src_name: list[str]  # Auto-flattened from member_table
    # Internet Service source group name.
    internet_service_src_group: list[str]  # Auto-flattened from member_table
    # Custom Internet Service source name.
    internet_service_src_custom: list[str]  # Auto-flattened from member_table
    # Dynamic Network Service source name.
    network_service_src_dynamic: list[str]  # Auto-flattened from member_table
    # Custom Internet Service source group name.
    internet_service_src_custom_group: list[str]  # Auto-flattened from member_table
    # Minimum Reputation to take action.
    reputation_minimum: int
    # Direction of the initial traffic for reputation to take effect.
    reputation_direction: Literal["source", "destination"]
    # Vendor MAC source ID.
    src_vendor_mac: list[str]  # Auto-flattened from member_table
    # Enable/disable use of IPv6 Internet Services for this policy. If enabled, destin
    internet_service6: Literal["enable", "disable"]
    # IPv6 Internet Service name.
    internet_service6_name: list[str]  # Auto-flattened from member_table
    # Internet Service group name.
    internet_service6_group: list[str]  # Auto-flattened from member_table
    # Custom IPv6 Internet Service name.
    internet_service6_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service6 group name.
    internet_service6_custom_group: list[str]  # Auto-flattened from member_table
    # Enable/disable use of IPv6 Internet Services in source for this policy. If enabl
    internet_service6_src: Literal["enable", "disable"]
    # IPv6 Internet Service source name.
    internet_service6_src_name: list[str]  # Auto-flattened from member_table
    # Internet Service6 source group name.
    internet_service6_src_group: list[str]  # Auto-flattened from member_table
    # Custom IPv6 Internet Service source name.
    internet_service6_src_custom: list[str]  # Auto-flattened from member_table
    # Custom Internet Service6 source group name.
    internet_service6_src_custom_group: list[str]  # Auto-flattened from member_table
    # IPv6 Minimum Reputation to take action.
    reputation_minimum6: int
    # Direction of the initial traffic for IPv6 reputation to take effect.
    reputation_direction6: Literal["source", "destination"]
    # Enable Real Time Protocol (RTP) NAT.
    rtp_nat: Literal["disable", "enable"]
    # Address names if this is an RTP NAT policy.
    rtp_addr: list[str]  # Auto-flattened from member_table
    # Enable to send a reply when a session is denied or blocked by a firewall policy.
    send_deny_packet: Literal["disable", "enable"]
    # How to handle sessions if the configuration of this firewall policy changes.
    firewall_session_dirty: Literal["check-all", "check-new"]
    # Schedule name.
    schedule: str
    # Enable to force current sessions to end when the schedule object times out. Disa
    schedule_timeout: Literal["enable", "disable"]
    # Enable/disable policy expiry.
    policy_expiry: Literal["enable", "disable"]
    # Policy expiry date (YYYY-MM-DD HH:MM:SS).
    policy_expiry_date: str
    # Policy expiry date and time, in epoch format.
    policy_expiry_date_utc: str
    # Service and service group names.
    service: list[str]  # Auto-flattened from member_table
    # Non-zero bit positions are used for comparison while zero bit positions are igno
    tos_mask: str
    # ToS (Type of Service) value used for comparison.
    tos: str
    # Enable negated TOS match.
    tos_negate: Literal["enable", "disable"]
    # Enable/disable anti-replay check.
    anti_replay: Literal["enable", "disable"]
    # Enable/disable creation of TCP session without SYN flag.
    tcp_session_without_syn: Literal["all", "data-only", "disable"]
    # Enable/disable recognition of anycast IP addresses using the geography IP databa
    geoip_anycast: Literal["enable", "disable"]
    # Match geography address based either on its physical location or registered loca
    geoip_match: Literal["physical-location", "registered-location"]
    # Enable/disable dynamic RADIUS defined traffic shaping.
    dynamic_shaping: Literal["enable", "disable"]
    # Enable/disable passive WAN health measurement. When enabled, auto-asic-offload i
    passive_wan_health_measurement: Literal["enable", "disable"]
    # Enable/disable application TCP metrics in session logs.When enabled, auto-asic-o
    app_monitor: Literal["enable", "disable"]
    # Enable to add one or more security profiles (AV, IPS, etc.) to the firewall poli
    utm_status: Literal["enable", "disable"]
    # Policy inspection mode (Flow/proxy). Default is Flow mode.
    inspection_mode: Literal["proxy", "flow"]
    # Redirect HTTP(S) traffic to matching transparent web proxy policy.
    http_policy_redirect: Literal["enable", "disable", "legacy"]
    # Redirect SSH traffic to matching transparent proxy policy.
    ssh_policy_redirect: Literal["enable", "disable"]
    # Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
    ztna_policy_redirect: Literal["enable", "disable"]
    # Webproxy profile name.
    webproxy_profile: str
    # Determine whether the firewall policy allows security profile groups or single p
    profile_type: Literal["single", "group"]
    # Name of profile group.
    profile_group: str
    # Name of an existing Protocol options profile.
    profile_protocol_options: str
    # Name of an existing SSL SSH profile.
    ssl_ssh_profile: str
    # Name of an existing Antivirus profile.
    av_profile: str
    # Name of an existing Web filter profile.
    webfilter_profile: str
    # Name of an existing DNS filter profile.
    dnsfilter_profile: str
    # Name of an existing email filter profile.
    emailfilter_profile: str
    # Name of an existing DLP profile.
    dlp_profile: str
    # Name of an existing file-filter profile.
    file_filter_profile: str
    # Name of an existing IPS sensor.
    ips_sensor: str
    # Name of an existing Application list.
    application_list: str
    # Name of an existing VoIP (voipd) profile.
    voip_profile: str
    # Name of an existing VoIP (ips) profile.
    ips_voip_filter: str
    # Name of an existing SCTP filter profile.
    sctp_filter_profile: str
    # Name of an existing Diameter filter profile.
    diameter_filter_profile: str
    # Name of an existing virtual-patch profile.
    virtual_patch_profile: str
    # Name of an existing ICAP profile.
    icap_profile: str
    # Name of an existing VideoFilter profile.
    videofilter_profile: str
    # Name of an existing Web application firewall profile.
    waf_profile: str
    # Name of an existing SSH filter profile.
    ssh_filter_profile: str
    # Name of an existing CASB profile.
    casb_profile: str
    # Enable or disable logging. Log all sessions or security profile sessions.
    logtraffic: Literal["all", "utm", "disable"]
    # Record logs when a session starts.
    logtraffic_start: Literal["enable", "disable"]
    # Enable/disable HTTP transaction log.
    log_http_transaction: Literal["enable", "disable"]
    # Enable/disable capture packets.
    capture_packet: Literal["enable", "disable"]
    # Enable/disable policy traffic ASIC offloading.
    auto_asic_offload: Literal["enable", "disable"]
    # Enable/disable WAN optimization.
    wanopt: Literal["enable", "disable"]
    # WAN optimization auto-detection mode.
    wanopt_detection: Literal["active", "passive", "off"]
    # WAN optimization passive mode options. This option decides what IP address will 
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"]
    # WAN optimization profile.
    wanopt_profile: str
    # WAN optimization peer.
    wanopt_peer: str
    # Enable/disable web cache.
    webcache: Literal["enable", "disable"]
    # Enable/disable web cache for HTTPS.
    webcache_https: Literal["disable", "enable"]
    # Webproxy forward server name.
    webproxy_forward_server: str
    # Traffic shaper.
    traffic_shaper: str
    # Reverse traffic shaper.
    traffic_shaper_reverse: str
    # Per-IP traffic shaper.
    per_ip_shaper: str
    # Enable/disable source NAT.
    nat: Literal["enable", "disable"]
    # Enable/disable PCP outbound SNAT.
    pcp_outbound: Literal["enable", "disable"]
    # Enable/disable PCP inbound DNAT.
    pcp_inbound: Literal["enable", "disable"]
    # PCP pool names.
    pcp_poolname: list[str]  # Auto-flattened from member_table
    # Enable/disable fullcone NAT. Accept UDP packets from any host.
    permit_any_host: Literal["enable", "disable"]
    # Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.
    permit_stun_host: Literal["enable", "disable"]
    # Enable to prevent source NAT from changing a session's source port.
    fixedport: Literal["enable", "disable"]
    # Enable/disable preservation of the original source port from source NAT if it ha
    port_preserve: Literal["enable", "disable"]
    # Enable/disable random source port selection for source NAT.
    port_random: Literal["enable", "disable"]
    # Enable to use IP Pools for source NAT.
    ippool: Literal["enable", "disable"]
    # IP Pool names.
    poolname: list[str]  # Auto-flattened from member_table
    # IPv6 pool names.
    poolname6: list[str]  # Auto-flattened from member_table
    # TTL in seconds for sessions accepted by this policy (0 means use the system defa
    session_ttl: str
    # VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.
    vlan_cos_fwd: int
    # VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.
    vlan_cos_rev: int
    # Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.
    inbound: Literal["enable", "disable"]
    # Policy-based IPsec VPN: only traffic from the internal network can initiate a VP
    outbound: Literal["enable", "disable"]
    # Policy-based IPsec VPN: apply destination NAT to inbound traffic.
    natinbound: Literal["enable", "disable"]
    # Policy-based IPsec VPN: apply source NAT to outbound traffic.
    natoutbound: Literal["enable", "disable"]
    # Enable/disable Forward Error Correction on traffic matching this policy on a FEC
    fec: Literal["enable", "disable"]
    # Enable/disable forwarding traffic matching this policy to a configured WCCP serv
    wccp: Literal["enable", "disable"]
    # Enable/disable NTLM authentication.
    ntlm: Literal["enable", "disable"]
    # Enable/disable NTLM guest user access.
    ntlm_guest: Literal["enable", "disable"]
    # HTTP-User-Agent value of supported browsers.
    ntlm_enabled_browsers: list[str]  # Auto-flattened from member_table
    # FSSO agent to use for NTLM authentication.
    fsso_agent_for_ntlm: str
    # Names of user groups that can authenticate with this policy.
    groups: list[str]  # Auto-flattened from member_table
    # Names of individual users that can authenticate with this policy.
    users: list[str]  # Auto-flattened from member_table
    # Names of FSSO groups.
    fsso_groups: list[str]  # Auto-flattened from member_table
    # Enable/disable authentication-based routing.
    auth_path: Literal["enable", "disable"]
    # Enable/disable user authentication disclaimer.
    disclaimer: Literal["enable", "disable"]
    # Enable/disable email collection.
    email_collect: Literal["enable", "disable"]
    # Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
    vpntunnel: str
    # Policy-based IPsec VPN: source NAT IP address for outgoing traffic.
    natip: str
    # Enable to match packets that have had their destination addresses changed by a V
    match_vip: Literal["enable", "disable"]
    # Enable/disable matching of only those packets that have had their destination ad
    match_vip_only: Literal["enable", "disable"]
    # Enable to copy packet's DiffServ values from session's original direction to its
    diffserv_copy: Literal["enable", "disable"]
    # Enable to change packet's DiffServ values to the specified diffservcode-forward 
    diffserv_forward: Literal["enable", "disable"]
    # Enable to change packet's reverse (reply) DiffServ values to the specified diffs
    diffserv_reverse: Literal["enable", "disable"]
    # Change packet's DiffServ to this value.
    diffservcode_forward: str
    # Change packet's reverse (reply) DiffServ to this value.
    diffservcode_rev: str
    # Sender TCP maximum segment size (MSS).
    tcp_mss_sender: int
    # Receiver TCP maximum segment size (MSS).
    tcp_mss_receiver: int
    # Comment.
    comments: str
    # HTTPS server certificate for policy authentication.
    auth_cert: str
    # HTTP-to-HTTPS redirect address for firewall authentication.
    auth_redirect_addr: str
    # URL users are directed to after seeing and accepting the disclaimer or authentic
    redirect_url: str
    # Name of identity-based routing rule.
    identity_based_route: str
    # Enable/disable block notification.
    block_notification: Literal["enable", "disable"]
    # Custom fields to append to log messages for this policy.
    custom_log_fields: list[str]  # Auto-flattened from member_table
    # Override the default replacement message group for this policy.
    replacemsg_override_group: str
    # When enabled srcaddr specifies what the source address must NOT be.
    srcaddr_negate: Literal["enable", "disable"]
    # When enabled srcaddr6 specifies what the source address must NOT be.
    srcaddr6_negate: Literal["enable", "disable"]
    # When enabled dstaddr specifies what the destination address must NOT be.
    dstaddr_negate: Literal["enable", "disable"]
    # When enabled dstaddr6 specifies what the destination address must NOT be.
    dstaddr6_negate: Literal["enable", "disable"]
    # When enabled ztna-ems-tag specifies what the tags must NOT be.
    ztna_ems_tag_negate: Literal["enable", "disable"]
    # When enabled service specifies what the service must NOT be.
    service_negate: Literal["enable", "disable"]
    # When enabled internet-service specifies what the service must NOT be.
    internet_service_negate: Literal["enable", "disable"]
    # When enabled internet-service-src specifies what the service must NOT be.
    internet_service_src_negate: Literal["enable", "disable"]
    # When enabled internet-service6 specifies what the service must NOT be.
    internet_service6_negate: Literal["enable", "disable"]
    # When enabled internet-service6-src specifies what the service must NOT be.
    internet_service6_src_negate: Literal["enable", "disable"]
    # Enable/disable sending RST packets when TCP sessions expire.
    timeout_send_rst: Literal["enable", "disable"]
    # Enable to exempt some users from the captive portal.
    captive_portal_exempt: Literal["enable", "disable"]
    # Decrypted traffic mirror.
    decrypted_traffic_mirror: str
    # Enable DSRI to ignore HTTP server responses.
    dsri: Literal["enable", "disable"]
    # Enable MAC authentication bypass. The bypassed MAC address must be received from
    radius_mac_auth_bypass: Literal["enable", "disable"]
    # Enable IP authentication bypass. The bypassed IP address must be received from R
    radius_ip_auth_bypass: Literal["enable", "disable"]
    # Enable TCP NPU session delay to guarantee packet order of 3-way handshake.
    delay_tcp_npu_session: Literal["enable", "disable"]
    # VLAN ranges to allow
    vlan_filter: str
    # Enable/disable security group tags (SGT) check.
    sgt_check: Literal["enable", "disable"]
    # Security group tags.
    sgt: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[str]  # Auto-flattened from member_table
    # FortiGuard Internet Service source name.
    internet_service_src_fortiguard: list[str]  # Auto-flattened from member_table
    # FortiGuard IPv6 Internet Service name.
    internet_service6_fortiguard: list[str]  # Auto-flattened from member_table
    # FortiGuard IPv6 Internet Service source name.
    internet_service6_src_fortiguard: list[str]  # Auto-flattened from member_table
    
    # Methods inherited from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Policy:
    """
    Configure IPv4/IPv6 policies.
    
    Path: firewall/policy
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey provided)
    @overload
    def get(
        self,
        policyid: int,
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
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    # List of objects (no mkey provided - most specific for list returns)
    # For singleton endpoints (no mkey), returns single object; for table endpoints, returns list
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
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> list[PolicyObject]: ...
    
    @overload
    def get(
        self,
        policyid: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True],
        *,
        response_mode: Literal["object"],
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided (single dict)
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> dict[str, Any]: ...
    
    # Dict mode without mkey (returns dict with results array)
    @overload
    def get(
        self,
        policyid: None = None,
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
    ) -> dict[str, Any]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        policyid: int | None = ...,
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
    ) -> PolicyObject | list[PolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> PolicyObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PolicyPayload | None = ...,
        policyid: int | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        action: Literal["accept", "deny", "ipsec"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        ztna_status: Literal["enable", "disable"] | None = ...,
        ztna_device_ownership: Literal["enable", "disable"] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = ...,
        ztna_tags_match_logic: Literal["or", "and"] | None = ...,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum: int | None = ...,
        reputation_direction: Literal["source", "destination"] | None = ...,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        reputation_minimum6: int | None = ...,
        reputation_direction6: Literal["source", "destination"] | None = ...,
        rtp_nat: Literal["disable", "enable"] | None = ...,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = ...,
        schedule: str | None = ...,
        schedule_timeout: Literal["enable", "disable"] | None = ...,
        policy_expiry: Literal["enable", "disable"] | None = ...,
        policy_expiry_date: str | None = ...,
        policy_expiry_date_utc: str | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        tos_mask: str | None = ...,
        tos: str | None = ...,
        tos_negate: Literal["enable", "disable"] | None = ...,
        anti_replay: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = ...,
        geoip_anycast: Literal["enable", "disable"] | None = ...,
        geoip_match: Literal["physical-location", "registered-location"] | None = ...,
        dynamic_shaping: Literal["enable", "disable"] | None = ...,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = ...,
        app_monitor: Literal["enable", "disable"] | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        inspection_mode: Literal["proxy", "flow"] | None = ...,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = ...,
        ssh_policy_redirect: Literal["enable", "disable"] | None = ...,
        ztna_policy_redirect: Literal["enable", "disable"] | None = ...,
        webproxy_profile: str | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        waf_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        logtraffic_start: Literal["enable", "disable"] | None = ...,
        log_http_transaction: Literal["enable", "disable"] | None = ...,
        capture_packet: Literal["enable", "disable"] | None = ...,
        auto_asic_offload: Literal["enable", "disable"] | None = ...,
        wanopt: Literal["enable", "disable"] | None = ...,
        wanopt_detection: Literal["active", "passive", "off"] | None = ...,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = ...,
        wanopt_profile: str | None = ...,
        wanopt_peer: str | None = ...,
        webcache: Literal["enable", "disable"] | None = ...,
        webcache_https: Literal["disable", "enable"] | None = ...,
        webproxy_forward_server: str | None = ...,
        traffic_shaper: str | None = ...,
        traffic_shaper_reverse: str | None = ...,
        per_ip_shaper: str | None = ...,
        nat: Literal["enable", "disable"] | None = ...,
        pcp_outbound: Literal["enable", "disable"] | None = ...,
        pcp_inbound: Literal["enable", "disable"] | None = ...,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        permit_any_host: Literal["enable", "disable"] | None = ...,
        permit_stun_host: Literal["enable", "disable"] | None = ...,
        fixedport: Literal["enable", "disable"] | None = ...,
        port_preserve: Literal["enable", "disable"] | None = ...,
        port_random: Literal["enable", "disable"] | None = ...,
        ippool: Literal["enable", "disable"] | None = ...,
        poolname: str | list[str] | list[dict[str, Any]] | None = ...,
        poolname6: str | list[str] | list[dict[str, Any]] | None = ...,
        session_ttl: str | None = ...,
        vlan_cos_fwd: int | None = ...,
        vlan_cos_rev: int | None = ...,
        inbound: Literal["enable", "disable"] | None = ...,
        outbound: Literal["enable", "disable"] | None = ...,
        natinbound: Literal["enable", "disable"] | None = ...,
        natoutbound: Literal["enable", "disable"] | None = ...,
        fec: Literal["enable", "disable"] | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        ntlm: Literal["enable", "disable"] | None = ...,
        ntlm_guest: Literal["enable", "disable"] | None = ...,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_agent_for_ntlm: str | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_path: Literal["enable", "disable"] | None = ...,
        disclaimer: Literal["enable", "disable"] | None = ...,
        email_collect: Literal["enable", "disable"] | None = ...,
        vpntunnel: str | None = ...,
        natip: str | None = ...,
        match_vip: Literal["enable", "disable"] | None = ...,
        match_vip_only: Literal["enable", "disable"] | None = ...,
        diffserv_copy: Literal["enable", "disable"] | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        tcp_mss_sender: int | None = ...,
        tcp_mss_receiver: int | None = ...,
        comments: str | None = ...,
        auth_cert: str | None = ...,
        auth_redirect_addr: str | None = ...,
        redirect_url: str | None = ...,
        identity_based_route: str | None = ...,
        block_notification: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        replacemsg_override_group: str | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        timeout_send_rst: Literal["enable", "disable"] | None = ...,
        captive_portal_exempt: Literal["enable", "disable"] | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        dsri: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        vlan_filter: str | None = ...,
        sgt_check: Literal["enable", "disable"] | None = ...,
        sgt: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Policy",
    "PolicyPayload",
    "PolicyObject",
]