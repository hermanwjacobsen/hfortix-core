"""
Validation helpers for firewall/policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

from typing import Any, TypedDict, NotRequired, Literal

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "srcintf",  # Incoming (ingress) interface.
    "dstintf",  # Outgoing (egress) interface.
    "schedule",  # Schedule name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "policyid": 0,
    "status": "enable",
    "name": "",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "action": "deny",
    "nat64": "disable",
    "nat46": "disable",
    "ztna-status": "disable",
    "ztna-device-ownership": "disable",
    "ztna-tags-match-logic": "or",
    "internet-service": "disable",
    "internet-service-src": "disable",
    "reputation-minimum": 0,
    "reputation-direction": "destination",
    "internet-service6": "disable",
    "internet-service6-src": "disable",
    "reputation-minimum6": 0,
    "reputation-direction6": "destination",
    "rtp-nat": "disable",
    "send-deny-packet": "disable",
    "firewall-session-dirty": "check-all",
    "schedule": "",
    "schedule-timeout": "disable",
    "policy-expiry": "disable",
    "policy-expiry-date": "0000-00-00 00:00:00",
    "policy-expiry-date-utc": "",
    "tos-mask": "",
    "tos": "",
    "tos-negate": "disable",
    "anti-replay": "enable",
    "tcp-session-without-syn": "disable",
    "geoip-anycast": "disable",
    "geoip-match": "physical-location",
    "dynamic-shaping": "disable",
    "passive-wan-health-measurement": "disable",
    "app-monitor": "disable",
    "utm-status": "disable",
    "inspection-mode": "flow",
    "http-policy-redirect": "disable",
    "ssh-policy-redirect": "disable",
    "ztna-policy-redirect": "disable",
    "webproxy-profile": "",
    "profile-type": "single",
    "profile-group": "",
    "profile-protocol-options": "default",
    "ssl-ssh-profile": "no-inspection",
    "av-profile": "",
    "webfilter-profile": "",
    "dnsfilter-profile": "",
    "emailfilter-profile": "",
    "dlp-profile": "",
    "file-filter-profile": "",
    "ips-sensor": "",
    "application-list": "",
    "voip-profile": "",
    "ips-voip-filter": "",
    "sctp-filter-profile": "",
    "diameter-filter-profile": "",
    "virtual-patch-profile": "",
    "icap-profile": "",
    "videofilter-profile": "",
    "waf-profile": "",
    "ssh-filter-profile": "",
    "casb-profile": "",
    "logtraffic": "utm",
    "logtraffic-start": "disable",
    "log-http-transaction": "disable",
    "capture-packet": "disable",
    "auto-asic-offload": "enable",
    "wanopt": "disable",
    "wanopt-detection": "active",
    "wanopt-passive-opt": "default",
    "wanopt-profile": "",
    "wanopt-peer": "",
    "webcache": "disable",
    "webcache-https": "disable",
    "webproxy-forward-server": "",
    "traffic-shaper": "",
    "traffic-shaper-reverse": "",
    "per-ip-shaper": "",
    "nat": "disable",
    "pcp-outbound": "disable",
    "pcp-inbound": "disable",
    "permit-any-host": "disable",
    "permit-stun-host": "disable",
    "fixedport": "disable",
    "port-preserve": "enable",
    "port-random": "disable",
    "ippool": "disable",
    "session-ttl": "",
    "vlan-cos-fwd": 255,
    "vlan-cos-rev": 255,
    "inbound": "disable",
    "outbound": "enable",
    "natinbound": "disable",
    "natoutbound": "disable",
    "fec": "disable",
    "wccp": "disable",
    "ntlm": "disable",
    "ntlm-guest": "disable",
    "fsso-agent-for-ntlm": "",
    "auth-path": "disable",
    "disclaimer": "disable",
    "email-collect": "disable",
    "vpntunnel": "",
    "natip": "0.0.0.0 0.0.0.0",
    "match-vip": "enable",
    "match-vip-only": "disable",
    "diffserv-copy": "disable",
    "diffserv-forward": "disable",
    "diffserv-reverse": "disable",
    "diffservcode-forward": "",
    "diffservcode-rev": "",
    "tcp-mss-sender": 0,
    "tcp-mss-receiver": 0,
    "auth-cert": "",
    "auth-redirect-addr": "",
    "identity-based-route": "",
    "block-notification": "disable",
    "replacemsg-override-group": "",
    "srcaddr-negate": "disable",
    "srcaddr6-negate": "disable",
    "dstaddr-negate": "disable",
    "dstaddr6-negate": "disable",
    "ztna-ems-tag-negate": "disable",
    "service-negate": "disable",
    "internet-service-negate": "disable",
    "internet-service-src-negate": "disable",
    "internet-service6-negate": "disable",
    "internet-service6-src-negate": "disable",
    "timeout-send-rst": "disable",
    "captive-portal-exempt": "disable",
    "decrypted-traffic-mirror": "",
    "dsri": "disable",
    "radius-mac-auth-bypass": "disable",
    "radius-ip-auth-bypass": "disable",
    "delay-tcp-npu-session": "disable",
    "vlan-filter": "",
    "sgt-check": "disable",
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "policyid": "integer",  # Policy ID (0 - 4294967294).
    "status": "option",  # Enable or disable this policy.
    "name": "string",  # Policy name.
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "srcintf": "string",  # Incoming (ingress) interface.
    "dstintf": "string",  # Outgoing (egress) interface.
    "action": "option",  # Policy action (accept/deny/ipsec).
    "nat64": "option",  # Enable/disable NAT64.
    "nat46": "option",  # Enable/disable NAT46.
    "ztna-status": "option",  # Enable/disable zero trust access.
    "ztna-device-ownership": "option",  # Enable/disable zero trust device ownership.
    "srcaddr": "string",  # Source IPv4 address and address group names.
    "dstaddr": "string",  # Destination IPv4 address and address group names.
    "srcaddr6": "string",  # Source IPv6 address name and address group names.
    "dstaddr6": "string",  # Destination IPv6 address name and address group names.
    "ztna-ems-tag": "string",  # Source ztna-ems-tag names.
    "ztna-ems-tag-secondary": "string",  # Source ztna-ems-tag-secondary names.
    "ztna-tags-match-logic": "option",  # ZTNA tag matching logic.
    "ztna-geo-tag": "string",  # Source ztna-geo-tag names.
    "internet-service": "option",  # Enable/disable use of Internet Services for this policy. If 
    "internet-service-name": "string",  # Internet Service name.
    "internet-service-group": "string",  # Internet Service group name.
    "internet-service-custom": "string",  # Custom Internet Service name.
    "network-service-dynamic": "string",  # Dynamic Network Service name.
    "internet-service-custom-group": "string",  # Custom Internet Service group name.
    "internet-service-src": "option",  # Enable/disable use of Internet Services in source for this p
    "internet-service-src-name": "string",  # Internet Service source name.
    "internet-service-src-group": "string",  # Internet Service source group name.
    "internet-service-src-custom": "string",  # Custom Internet Service source name.
    "network-service-src-dynamic": "string",  # Dynamic Network Service source name.
    "internet-service-src-custom-group": "string",  # Custom Internet Service source group name.
    "reputation-minimum": "integer",  # Minimum Reputation to take action.
    "reputation-direction": "option",  # Direction of the initial traffic for reputation to take effe
    "src-vendor-mac": "string",  # Vendor MAC source ID.
    "internet-service6": "option",  # Enable/disable use of IPv6 Internet Services for this policy
    "internet-service6-name": "string",  # IPv6 Internet Service name.
    "internet-service6-group": "string",  # Internet Service group name.
    "internet-service6-custom": "string",  # Custom IPv6 Internet Service name.
    "internet-service6-custom-group": "string",  # Custom Internet Service6 group name.
    "internet-service6-src": "option",  # Enable/disable use of IPv6 Internet Services in source for t
    "internet-service6-src-name": "string",  # IPv6 Internet Service source name.
    "internet-service6-src-group": "string",  # Internet Service6 source group name.
    "internet-service6-src-custom": "string",  # Custom IPv6 Internet Service source name.
    "internet-service6-src-custom-group": "string",  # Custom Internet Service6 source group name.
    "reputation-minimum6": "integer",  # IPv6 Minimum Reputation to take action.
    "reputation-direction6": "option",  # Direction of the initial traffic for IPv6 reputation to take
    "rtp-nat": "option",  # Enable Real Time Protocol (RTP) NAT.
    "rtp-addr": "string",  # Address names if this is an RTP NAT policy.
    "send-deny-packet": "option",  # Enable to send a reply when a session is denied or blocked b
    "firewall-session-dirty": "option",  # How to handle sessions if the configuration of this firewall
    "schedule": "string",  # Schedule name.
    "schedule-timeout": "option",  # Enable to force current sessions to end when the schedule ob
    "policy-expiry": "option",  # Enable/disable policy expiry.
    "policy-expiry-date": "datetime",  # Policy expiry date (YYYY-MM-DD HH:MM:SS).
    "policy-expiry-date-utc": "user",  # Policy expiry date and time, in epoch format.
    "service": "string",  # Service and service group names.
    "tos-mask": "user",  # Non-zero bit positions are used for comparison while zero bi
    "tos": "user",  # ToS (Type of Service) value used for comparison.
    "tos-negate": "option",  # Enable negated TOS match.
    "anti-replay": "option",  # Enable/disable anti-replay check.
    "tcp-session-without-syn": "option",  # Enable/disable creation of TCP session without SYN flag.
    "geoip-anycast": "option",  # Enable/disable recognition of anycast IP addresses using the
    "geoip-match": "option",  # Match geography address based either on its physical locatio
    "dynamic-shaping": "option",  # Enable/disable dynamic RADIUS defined traffic shaping.
    "passive-wan-health-measurement": "option",  # Enable/disable passive WAN health measurement. When enabled,
    "app-monitor": "option",  # Enable/disable application TCP metrics in session logs.When 
    "utm-status": "option",  # Enable to add one or more security profiles (AV, IPS, etc.) 
    "inspection-mode": "option",  # Policy inspection mode (Flow/proxy). Default is Flow mode.
    "http-policy-redirect": "option",  # Redirect HTTP(S) traffic to matching transparent web proxy p
    "ssh-policy-redirect": "option",  # Redirect SSH traffic to matching transparent proxy policy.
    "ztna-policy-redirect": "option",  # Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
    "webproxy-profile": "string",  # Webproxy profile name.
    "profile-type": "option",  # Determine whether the firewall policy allows security profil
    "profile-group": "string",  # Name of profile group.
    "profile-protocol-options": "string",  # Name of an existing Protocol options profile.
    "ssl-ssh-profile": "string",  # Name of an existing SSL SSH profile.
    "av-profile": "string",  # Name of an existing Antivirus profile.
    "webfilter-profile": "string",  # Name of an existing Web filter profile.
    "dnsfilter-profile": "string",  # Name of an existing DNS filter profile.
    "emailfilter-profile": "string",  # Name of an existing email filter profile.
    "dlp-profile": "string",  # Name of an existing DLP profile.
    "file-filter-profile": "string",  # Name of an existing file-filter profile.
    "ips-sensor": "string",  # Name of an existing IPS sensor.
    "application-list": "string",  # Name of an existing Application list.
    "voip-profile": "string",  # Name of an existing VoIP (voipd) profile.
    "ips-voip-filter": "string",  # Name of an existing VoIP (ips) profile.
    "sctp-filter-profile": "string",  # Name of an existing SCTP filter profile.
    "diameter-filter-profile": "string",  # Name of an existing Diameter filter profile.
    "virtual-patch-profile": "string",  # Name of an existing virtual-patch profile.
    "icap-profile": "string",  # Name of an existing ICAP profile.
    "videofilter-profile": "string",  # Name of an existing VideoFilter profile.
    "waf-profile": "string",  # Name of an existing Web application firewall profile.
    "ssh-filter-profile": "string",  # Name of an existing SSH filter profile.
    "casb-profile": "string",  # Name of an existing CASB profile.
    "logtraffic": "option",  # Enable or disable logging. Log all sessions or security prof
    "logtraffic-start": "option",  # Record logs when a session starts.
    "log-http-transaction": "option",  # Enable/disable HTTP transaction log.
    "capture-packet": "option",  # Enable/disable capture packets.
    "auto-asic-offload": "option",  # Enable/disable policy traffic ASIC offloading.
    "wanopt": "option",  # Enable/disable WAN optimization.
    "wanopt-detection": "option",  # WAN optimization auto-detection mode.
    "wanopt-passive-opt": "option",  # WAN optimization passive mode options. This option decides w
    "wanopt-profile": "string",  # WAN optimization profile.
    "wanopt-peer": "string",  # WAN optimization peer.
    "webcache": "option",  # Enable/disable web cache.
    "webcache-https": "option",  # Enable/disable web cache for HTTPS.
    "webproxy-forward-server": "string",  # Webproxy forward server name.
    "traffic-shaper": "string",  # Traffic shaper.
    "traffic-shaper-reverse": "string",  # Reverse traffic shaper.
    "per-ip-shaper": "string",  # Per-IP traffic shaper.
    "nat": "option",  # Enable/disable source NAT.
    "pcp-outbound": "option",  # Enable/disable PCP outbound SNAT.
    "pcp-inbound": "option",  # Enable/disable PCP inbound DNAT.
    "pcp-poolname": "string",  # PCP pool names.
    "permit-any-host": "option",  # Enable/disable fullcone NAT. Accept UDP packets from any hos
    "permit-stun-host": "option",  # Accept UDP packets from any Session Traversal Utilities for 
    "fixedport": "option",  # Enable to prevent source NAT from changing a session's sourc
    "port-preserve": "option",  # Enable/disable preservation of the original source port from
    "port-random": "option",  # Enable/disable random source port selection for source NAT.
    "ippool": "option",  # Enable to use IP Pools for source NAT.
    "poolname": "string",  # IP Pool names.
    "poolname6": "string",  # IPv6 pool names.
    "session-ttl": "user",  # TTL in seconds for sessions accepted by this policy (0 means
    "vlan-cos-fwd": "integer",  # VLAN forward direction user priority: 255 passthrough, 0 low
    "vlan-cos-rev": "integer",  # VLAN reverse direction user priority: 255 passthrough, 0 low
    "inbound": "option",  # Policy-based IPsec VPN: only traffic from the remote network
    "outbound": "option",  # Policy-based IPsec VPN: only traffic from the internal netwo
    "natinbound": "option",  # Policy-based IPsec VPN: apply destination NAT to inbound tra
    "natoutbound": "option",  # Policy-based IPsec VPN: apply source NAT to outbound traffic
    "fec": "option",  # Enable/disable Forward Error Correction on traffic matching 
    "wccp": "option",  # Enable/disable forwarding traffic matching this policy to a 
    "ntlm": "option",  # Enable/disable NTLM authentication.
    "ntlm-guest": "option",  # Enable/disable NTLM guest user access.
    "ntlm-enabled-browsers": "string",  # HTTP-User-Agent value of supported browsers.
    "fsso-agent-for-ntlm": "string",  # FSSO agent to use for NTLM authentication.
    "groups": "string",  # Names of user groups that can authenticate with this policy.
    "users": "string",  # Names of individual users that can authenticate with this po
    "fsso-groups": "string",  # Names of FSSO groups.
    "auth-path": "option",  # Enable/disable authentication-based routing.
    "disclaimer": "option",  # Enable/disable user authentication disclaimer.
    "email-collect": "option",  # Enable/disable email collection.
    "vpntunnel": "string",  # Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
    "natip": "ipv4-classnet",  # Policy-based IPsec VPN: source NAT IP address for outgoing t
    "match-vip": "option",  # Enable to match packets that have had their destination addr
    "match-vip-only": "option",  # Enable/disable matching of only those packets that have had 
    "diffserv-copy": "option",  # Enable to copy packet's DiffServ values from session's origi
    "diffserv-forward": "option",  # Enable to change packet's DiffServ values to the specified d
    "diffserv-reverse": "option",  # Enable to change packet's reverse (reply) DiffServ values to
    "diffservcode-forward": "user",  # Change packet's DiffServ to this value.
    "diffservcode-rev": "user",  # Change packet's reverse (reply) DiffServ to this value.
    "tcp-mss-sender": "integer",  # Sender TCP maximum segment size (MSS).
    "tcp-mss-receiver": "integer",  # Receiver TCP maximum segment size (MSS).
    "comments": "var-string",  # Comment.
    "auth-cert": "string",  # HTTPS server certificate for policy authentication.
    "auth-redirect-addr": "string",  # HTTP-to-HTTPS redirect address for firewall authentication.
    "redirect-url": "var-string",  # URL users are directed to after seeing and accepting the dis
    "identity-based-route": "string",  # Name of identity-based routing rule.
    "block-notification": "option",  # Enable/disable block notification.
    "custom-log-fields": "string",  # Custom fields to append to log messages for this policy.
    "replacemsg-override-group": "string",  # Override the default replacement message group for this poli
    "srcaddr-negate": "option",  # When enabled srcaddr specifies what the source address must 
    "srcaddr6-negate": "option",  # When enabled srcaddr6 specifies what the source address must
    "dstaddr-negate": "option",  # When enabled dstaddr specifies what the destination address 
    "dstaddr6-negate": "option",  # When enabled dstaddr6 specifies what the destination address
    "ztna-ems-tag-negate": "option",  # When enabled ztna-ems-tag specifies what the tags must NOT b
    "service-negate": "option",  # When enabled service specifies what the service must NOT be.
    "internet-service-negate": "option",  # When enabled internet-service specifies what the service mus
    "internet-service-src-negate": "option",  # When enabled internet-service-src specifies what the service
    "internet-service6-negate": "option",  # When enabled internet-service6 specifies what the service mu
    "internet-service6-src-negate": "option",  # When enabled internet-service6-src specifies what the servic
    "timeout-send-rst": "option",  # Enable/disable sending RST packets when TCP sessions expire.
    "captive-portal-exempt": "option",  # Enable to exempt some users from the captive portal.
    "decrypted-traffic-mirror": "string",  # Decrypted traffic mirror.
    "dsri": "option",  # Enable DSRI to ignore HTTP server responses.
    "radius-mac-auth-bypass": "option",  # Enable MAC authentication bypass. The bypassed MAC address m
    "radius-ip-auth-bypass": "option",  # Enable IP authentication bypass. The bypassed IP address mus
    "delay-tcp-npu-session": "option",  # Enable TCP NPU session delay to guarantee packet order of 3-
    "vlan-filter": "user",  # VLAN ranges to allow
    "sgt-check": "option",  # Enable/disable security group tags (SGT) check.
    "sgt": "string",  # Security group tags.
    "internet-service-fortiguard": "string",  # FortiGuard Internet Service name.
    "internet-service-src-fortiguard": "string",  # FortiGuard Internet Service source name.
    "internet-service6-fortiguard": "string",  # FortiGuard IPv6 Internet Service name.
    "internet-service6-src-fortiguard": "string",  # FortiGuard IPv6 Internet Service source name.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "policyid": "Policy ID (0 - 4294967294).",
    "status": "Enable or disable this policy.",
    "name": "Policy name.",
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "srcintf": "Incoming (ingress) interface.",
    "dstintf": "Outgoing (egress) interface.",
    "action": "Policy action (accept/deny/ipsec).",
    "nat64": "Enable/disable NAT64.",
    "nat46": "Enable/disable NAT46.",
    "ztna-status": "Enable/disable zero trust access.",
    "ztna-device-ownership": "Enable/disable zero trust device ownership.",
    "srcaddr": "Source IPv4 address and address group names.",
    "dstaddr": "Destination IPv4 address and address group names.",
    "srcaddr6": "Source IPv6 address name and address group names.",
    "dstaddr6": "Destination IPv6 address name and address group names.",
    "ztna-ems-tag": "Source ztna-ems-tag names.",
    "ztna-ems-tag-secondary": "Source ztna-ems-tag-secondary names.",
    "ztna-tags-match-logic": "ZTNA tag matching logic.",
    "ztna-geo-tag": "Source ztna-geo-tag names.",
    "internet-service": "Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.",
    "internet-service-name": "Internet Service name.",
    "internet-service-group": "Internet Service group name.",
    "internet-service-custom": "Custom Internet Service name.",
    "network-service-dynamic": "Dynamic Network Service name.",
    "internet-service-custom-group": "Custom Internet Service group name.",
    "internet-service-src": "Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.",
    "internet-service-src-name": "Internet Service source name.",
    "internet-service-src-group": "Internet Service source group name.",
    "internet-service-src-custom": "Custom Internet Service source name.",
    "network-service-src-dynamic": "Dynamic Network Service source name.",
    "internet-service-src-custom-group": "Custom Internet Service source group name.",
    "reputation-minimum": "Minimum Reputation to take action.",
    "reputation-direction": "Direction of the initial traffic for reputation to take effect.",
    "src-vendor-mac": "Vendor MAC source ID.",
    "internet-service6": "Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used.",
    "internet-service6-name": "IPv6 Internet Service name.",
    "internet-service6-group": "Internet Service group name.",
    "internet-service6-custom": "Custom IPv6 Internet Service name.",
    "internet-service6-custom-group": "Custom Internet Service6 group name.",
    "internet-service6-src": "Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.",
    "internet-service6-src-name": "IPv6 Internet Service source name.",
    "internet-service6-src-group": "Internet Service6 source group name.",
    "internet-service6-src-custom": "Custom IPv6 Internet Service source name.",
    "internet-service6-src-custom-group": "Custom Internet Service6 source group name.",
    "reputation-minimum6": "IPv6 Minimum Reputation to take action.",
    "reputation-direction6": "Direction of the initial traffic for IPv6 reputation to take effect.",
    "rtp-nat": "Enable Real Time Protocol (RTP) NAT.",
    "rtp-addr": "Address names if this is an RTP NAT policy.",
    "send-deny-packet": "Enable to send a reply when a session is denied or blocked by a firewall policy.",
    "firewall-session-dirty": "How to handle sessions if the configuration of this firewall policy changes.",
    "schedule": "Schedule name.",
    "schedule-timeout": "Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.",
    "policy-expiry": "Enable/disable policy expiry.",
    "policy-expiry-date": "Policy expiry date (YYYY-MM-DD HH:MM:SS).",
    "policy-expiry-date-utc": "Policy expiry date and time, in epoch format.",
    "service": "Service and service group names.",
    "tos-mask": "Non-zero bit positions are used for comparison while zero bit positions are ignored.",
    "tos": "ToS (Type of Service) value used for comparison.",
    "tos-negate": "Enable negated TOS match.",
    "anti-replay": "Enable/disable anti-replay check.",
    "tcp-session-without-syn": "Enable/disable creation of TCP session without SYN flag.",
    "geoip-anycast": "Enable/disable recognition of anycast IP addresses using the geography IP database.",
    "geoip-match": "Match geography address based either on its physical location or registered location.",
    "dynamic-shaping": "Enable/disable dynamic RADIUS defined traffic shaping.",
    "passive-wan-health-measurement": "Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled.",
    "app-monitor": "Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled.",
    "utm-status": "Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.",
    "inspection-mode": "Policy inspection mode (Flow/proxy). Default is Flow mode.",
    "http-policy-redirect": "Redirect HTTP(S) traffic to matching transparent web proxy policy.",
    "ssh-policy-redirect": "Redirect SSH traffic to matching transparent proxy policy.",
    "ztna-policy-redirect": "Redirect ZTNA traffic to matching Access-Proxy proxy-policy.",
    "webproxy-profile": "Webproxy profile name.",
    "profile-type": "Determine whether the firewall policy allows security profile groups or single profiles only.",
    "profile-group": "Name of profile group.",
    "profile-protocol-options": "Name of an existing Protocol options profile.",
    "ssl-ssh-profile": "Name of an existing SSL SSH profile.",
    "av-profile": "Name of an existing Antivirus profile.",
    "webfilter-profile": "Name of an existing Web filter profile.",
    "dnsfilter-profile": "Name of an existing DNS filter profile.",
    "emailfilter-profile": "Name of an existing email filter profile.",
    "dlp-profile": "Name of an existing DLP profile.",
    "file-filter-profile": "Name of an existing file-filter profile.",
    "ips-sensor": "Name of an existing IPS sensor.",
    "application-list": "Name of an existing Application list.",
    "voip-profile": "Name of an existing VoIP (voipd) profile.",
    "ips-voip-filter": "Name of an existing VoIP (ips) profile.",
    "sctp-filter-profile": "Name of an existing SCTP filter profile.",
    "diameter-filter-profile": "Name of an existing Diameter filter profile.",
    "virtual-patch-profile": "Name of an existing virtual-patch profile.",
    "icap-profile": "Name of an existing ICAP profile.",
    "videofilter-profile": "Name of an existing VideoFilter profile.",
    "waf-profile": "Name of an existing Web application firewall profile.",
    "ssh-filter-profile": "Name of an existing SSH filter profile.",
    "casb-profile": "Name of an existing CASB profile.",
    "logtraffic": "Enable or disable logging. Log all sessions or security profile sessions.",
    "logtraffic-start": "Record logs when a session starts.",
    "log-http-transaction": "Enable/disable HTTP transaction log.",
    "capture-packet": "Enable/disable capture packets.",
    "auto-asic-offload": "Enable/disable policy traffic ASIC offloading.",
    "wanopt": "Enable/disable WAN optimization.",
    "wanopt-detection": "WAN optimization auto-detection mode.",
    "wanopt-passive-opt": "WAN optimization passive mode options. This option decides what IP address will be used to connect server.",
    "wanopt-profile": "WAN optimization profile.",
    "wanopt-peer": "WAN optimization peer.",
    "webcache": "Enable/disable web cache.",
    "webcache-https": "Enable/disable web cache for HTTPS.",
    "webproxy-forward-server": "Webproxy forward server name.",
    "traffic-shaper": "Traffic shaper.",
    "traffic-shaper-reverse": "Reverse traffic shaper.",
    "per-ip-shaper": "Per-IP traffic shaper.",
    "nat": "Enable/disable source NAT.",
    "pcp-outbound": "Enable/disable PCP outbound SNAT.",
    "pcp-inbound": "Enable/disable PCP inbound DNAT.",
    "pcp-poolname": "PCP pool names.",
    "permit-any-host": "Enable/disable fullcone NAT. Accept UDP packets from any host.",
    "permit-stun-host": "Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.",
    "fixedport": "Enable to prevent source NAT from changing a session's source port.",
    "port-preserve": "Enable/disable preservation of the original source port from source NAT if it has not been used.",
    "port-random": "Enable/disable random source port selection for source NAT.",
    "ippool": "Enable to use IP Pools for source NAT.",
    "poolname": "IP Pool names.",
    "poolname6": "IPv6 pool names.",
    "session-ttl": "TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).",
    "vlan-cos-fwd": "VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.",
    "vlan-cos-rev": "VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.",
    "inbound": "Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.",
    "outbound": "Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.",
    "natinbound": "Policy-based IPsec VPN: apply destination NAT to inbound traffic.",
    "natoutbound": "Policy-based IPsec VPN: apply source NAT to outbound traffic.",
    "fec": "Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.",
    "wccp": "Enable/disable forwarding traffic matching this policy to a configured WCCP server.",
    "ntlm": "Enable/disable NTLM authentication.",
    "ntlm-guest": "Enable/disable NTLM guest user access.",
    "ntlm-enabled-browsers": "HTTP-User-Agent value of supported browsers.",
    "fsso-agent-for-ntlm": "FSSO agent to use for NTLM authentication.",
    "groups": "Names of user groups that can authenticate with this policy.",
    "users": "Names of individual users that can authenticate with this policy.",
    "fsso-groups": "Names of FSSO groups.",
    "auth-path": "Enable/disable authentication-based routing.",
    "disclaimer": "Enable/disable user authentication disclaimer.",
    "email-collect": "Enable/disable email collection.",
    "vpntunnel": "Policy-based IPsec VPN: name of the IPsec VPN Phase 1.",
    "natip": "Policy-based IPsec VPN: source NAT IP address for outgoing traffic.",
    "match-vip": "Enable to match packets that have had their destination addresses changed by a VIP.",
    "match-vip-only": "Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.",
    "diffserv-copy": "Enable to copy packet's DiffServ values from session's original direction to its reply direction.",
    "diffserv-forward": "Enable to change packet's DiffServ values to the specified diffservcode-forward value.",
    "diffserv-reverse": "Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.",
    "diffservcode-forward": "Change packet's DiffServ to this value.",
    "diffservcode-rev": "Change packet's reverse (reply) DiffServ to this value.",
    "tcp-mss-sender": "Sender TCP maximum segment size (MSS).",
    "tcp-mss-receiver": "Receiver TCP maximum segment size (MSS).",
    "comments": "Comment.",
    "auth-cert": "HTTPS server certificate for policy authentication.",
    "auth-redirect-addr": "HTTP-to-HTTPS redirect address for firewall authentication.",
    "redirect-url": "URL users are directed to after seeing and accepting the disclaimer or authenticating.",
    "identity-based-route": "Name of identity-based routing rule.",
    "block-notification": "Enable/disable block notification.",
    "custom-log-fields": "Custom fields to append to log messages for this policy.",
    "replacemsg-override-group": "Override the default replacement message group for this policy.",
    "srcaddr-negate": "When enabled srcaddr specifies what the source address must NOT be.",
    "srcaddr6-negate": "When enabled srcaddr6 specifies what the source address must NOT be.",
    "dstaddr-negate": "When enabled dstaddr specifies what the destination address must NOT be.",
    "dstaddr6-negate": "When enabled dstaddr6 specifies what the destination address must NOT be.",
    "ztna-ems-tag-negate": "When enabled ztna-ems-tag specifies what the tags must NOT be.",
    "service-negate": "When enabled service specifies what the service must NOT be.",
    "internet-service-negate": "When enabled internet-service specifies what the service must NOT be.",
    "internet-service-src-negate": "When enabled internet-service-src specifies what the service must NOT be.",
    "internet-service6-negate": "When enabled internet-service6 specifies what the service must NOT be.",
    "internet-service6-src-negate": "When enabled internet-service6-src specifies what the service must NOT be.",
    "timeout-send-rst": "Enable/disable sending RST packets when TCP sessions expire.",
    "captive-portal-exempt": "Enable to exempt some users from the captive portal.",
    "decrypted-traffic-mirror": "Decrypted traffic mirror.",
    "dsri": "Enable DSRI to ignore HTTP server responses.",
    "radius-mac-auth-bypass": "Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.",
    "radius-ip-auth-bypass": "Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server.",
    "delay-tcp-npu-session": "Enable TCP NPU session delay to guarantee packet order of 3-way handshake.",
    "vlan-filter": "VLAN ranges to allow",
    "sgt-check": "Enable/disable security group tags (SGT) check.",
    "sgt": "Security group tags.",
    "internet-service-fortiguard": "FortiGuard Internet Service name.",
    "internet-service-src-fortiguard": "FortiGuard Internet Service source name.",
    "internet-service6-fortiguard": "FortiGuard IPv6 Internet Service name.",
    "internet-service6-src-fortiguard": "FortiGuard IPv6 Internet Service source name.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967294},
    "name": {"type": "string", "max_length": 35},
    "reputation-minimum": {"type": "integer", "min": 0, "max": 4294967295},
    "reputation-minimum6": {"type": "integer", "min": 0, "max": 4294967295},
    "schedule": {"type": "string", "max_length": 35},
    "webproxy-profile": {"type": "string", "max_length": 63},
    "profile-group": {"type": "string", "max_length": 47},
    "profile-protocol-options": {"type": "string", "max_length": 47},
    "ssl-ssh-profile": {"type": "string", "max_length": 47},
    "av-profile": {"type": "string", "max_length": 47},
    "webfilter-profile": {"type": "string", "max_length": 47},
    "dnsfilter-profile": {"type": "string", "max_length": 47},
    "emailfilter-profile": {"type": "string", "max_length": 47},
    "dlp-profile": {"type": "string", "max_length": 47},
    "file-filter-profile": {"type": "string", "max_length": 47},
    "ips-sensor": {"type": "string", "max_length": 47},
    "application-list": {"type": "string", "max_length": 47},
    "voip-profile": {"type": "string", "max_length": 47},
    "ips-voip-filter": {"type": "string", "max_length": 47},
    "sctp-filter-profile": {"type": "string", "max_length": 47},
    "diameter-filter-profile": {"type": "string", "max_length": 47},
    "virtual-patch-profile": {"type": "string", "max_length": 47},
    "icap-profile": {"type": "string", "max_length": 47},
    "videofilter-profile": {"type": "string", "max_length": 47},
    "waf-profile": {"type": "string", "max_length": 47},
    "ssh-filter-profile": {"type": "string", "max_length": 47},
    "casb-profile": {"type": "string", "max_length": 47},
    "wanopt-profile": {"type": "string", "max_length": 35},
    "wanopt-peer": {"type": "string", "max_length": 35},
    "webproxy-forward-server": {"type": "string", "max_length": 63},
    "traffic-shaper": {"type": "string", "max_length": 35},
    "traffic-shaper-reverse": {"type": "string", "max_length": 35},
    "per-ip-shaper": {"type": "string", "max_length": 35},
    "vlan-cos-fwd": {"type": "integer", "min": 0, "max": 7},
    "vlan-cos-rev": {"type": "integer", "min": 0, "max": 7},
    "fsso-agent-for-ntlm": {"type": "string", "max_length": 35},
    "vpntunnel": {"type": "string", "max_length": 35},
    "tcp-mss-sender": {"type": "integer", "min": 0, "max": 65535},
    "tcp-mss-receiver": {"type": "integer", "min": 0, "max": 65535},
    "auth-cert": {"type": "string", "max_length": 35},
    "auth-redirect-addr": {"type": "string", "max_length": 63},
    "identity-based-route": {"type": "string", "max_length": 35},
    "replacemsg-override-group": {"type": "string", "max_length": 35},
    "decrypted-traffic-mirror": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "srcintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "dstintf": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "srcaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dstaddr6": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "ztna-ems-tag": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "ztna-ems-tag-secondary": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "ztna-geo-tag": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "network-service-dynamic": {
        "name": {
            "type": "string",
            "help": "Dynamic Network Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "network-service-src-dynamic": {
        "name": {
            "type": "string",
            "help": "Dynamic Network Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "src-vendor-mac": {
        "id": {
            "type": "integer",
            "help": "Vendor MAC ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "internet-service6-name": {
        "name": {
            "type": "string",
            "help": "IPv6 Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service6 group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-group": {
        "name": {
            "type": "string",
            "help": "Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service6 group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "rtp-addr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service": {
        "name": {
            "type": "string",
            "help": "Service and service group names.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "pcp-poolname": {
        "name": {
            "type": "string",
            "help": "PCP pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "poolname": {
        "name": {
            "type": "string",
            "help": "IP pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "poolname6": {
        "name": {
            "type": "string",
            "help": "IPv6 pool name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "ntlm-enabled-browsers": {
        "user-agent-string": {
            "type": "string",
            "help": "User agent string.",
            "default": "",
            "max_length": 79,
        },
    },
    "groups": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "default": "",
            "max_length": 79,
        },
    },
    "users": {
        "name": {
            "type": "string",
            "help": "Names of individual users that can authenticate with this policy.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "fsso-groups": {
        "name": {
            "type": "string",
            "help": "Names of FSSO groups.",
            "required": True,
            "default": "",
            "max_length": 511,
        },
    },
    "custom-log-fields": {
        "field-id": {
            "type": "string",
            "help": "Custom log field.",
            "default": "",
            "max_length": 35,
        },
    },
    "sgt": {
        "id": {
            "type": "integer",
            "help": "Security group tag (1 - 65535).",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
    },
    "internet-service-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-src-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-src-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ACTION = [
    "accept",  # Allows session that match the firewall policy.
    "deny",  # Blocks sessions that match the firewall policy.
    "ipsec",  # Firewall policy becomes a policy-based IPsec VPN policy.
]
VALID_BODY_NAT64 = [
    "enable",  # Enable NAT64.
    "disable",  # Disable NAT64.
]
VALID_BODY_NAT46 = [
    "enable",  # Enable NAT46.
    "disable",  # Disable NAT46.
]
VALID_BODY_ZTNA_STATUS = [
    "enable",  # Enable zero trust network access.
    "disable",  # Disable zero trust network access.
]
VALID_BODY_ZTNA_DEVICE_OWNERSHIP = [
    "enable",  # Enable ZTNA device ownership check.
    "disable",  # Disable ZTNA device ownership check.
]
VALID_BODY_ZTNA_TAGS_MATCH_LOGIC = [
    "or",  # Match ZTNA tags using a logical OR operator.
    "and",  # Match ZTNA tags using a logical AND operator.
]
VALID_BODY_INTERNET_SERVICE = [
    "enable",  # Enable use of Internet Services in policy.
    "disable",  # Disable use of Internet Services in policy.
]
VALID_BODY_INTERNET_SERVICE_SRC = [
    "enable",  # Enable use of Internet Services source in policy.
    "disable",  # Disable use of Internet Services source in policy.
]
VALID_BODY_REPUTATION_DIRECTION = [
    "source",  # Check reputation for source address.
    "destination",  # Check reputation for destination address.
]
VALID_BODY_INTERNET_SERVICE6 = [
    "enable",  # Enable use of IPv6 Internet Services in policy.
    "disable",  # Disable use of IPv6 Internet Services in policy.
]
VALID_BODY_INTERNET_SERVICE6_SRC = [
    "enable",  # Enable use of IPv6 Internet Services source in policy.
    "disable",  # Disable use of IPv6 Internet Services source in policy.
]
VALID_BODY_REPUTATION_DIRECTION6 = [
    "source",  # Check reputation for IPv6 source address.
    "destination",  # Check reputation for IPv6 destination address.
]
VALID_BODY_RTP_NAT = [
    "disable",  # Disable setting.
    "enable",  # Enable setting.
]
VALID_BODY_SEND_DENY_PACKET = [
    "disable",  # Disable deny-packet sending.
    "enable",  # Enable deny-packet sending.
]
VALID_BODY_FIREWALL_SESSION_DIRTY = [
    "check-all",  # Flush all current sessions accepted by this policy. These sessions must be started and re-matched with policies.
    "check-new",  # Continue to allow sessions already accepted by this policy.
]
VALID_BODY_SCHEDULE_TIMEOUT = [
    "enable",  # Enable schedule timeout.
    "disable",  # Disable schedule timeout.
]
VALID_BODY_POLICY_EXPIRY = [
    "enable",  # Enable policy expiry.
    "disable",  # Disable polcy expiry.
]
VALID_BODY_TOS_NEGATE = [
    "enable",  # Enable TOS match negate.
    "disable",  # Disable TOS match negate.
]
VALID_BODY_ANTI_REPLAY = [
    "enable",  # Enable anti-replay check.
    "disable",  # Disable anti-replay check.
]
VALID_BODY_TCP_SESSION_WITHOUT_SYN = [
    "all",  # Enable TCP session without SYN.
    "data-only",  # Enable TCP session data only.
    "disable",  # Disable TCP session without SYN.
]
VALID_BODY_GEOIP_ANYCAST = [
    "enable",  # Enable recognition of anycast IP addresses using the geography IP database.
    "disable",  # Disable recognition of anycast IP addresses using the geography IP database.
]
VALID_BODY_GEOIP_MATCH = [
    "physical-location",  # Match geography address to its physical location using the geography IP database.
    "registered-location",  # Match geography address to its registered location using the geography IP database.
]
VALID_BODY_DYNAMIC_SHAPING = [
    "enable",  # Enable dynamic RADIUS defined traffic shaping.
    "disable",  # Disable dynamic RADIUS defined traffic shaping.
]
VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT = [
    "enable",  # Enable Passive WAN health measurement.
    "disable",  # Disable Passive WAN health measurement.
]
VALID_BODY_APP_MONITOR = [
    "enable",  # Enable TCP metrics in session logs.
    "disable",  # Disable TCP metrics in session logs.
]
VALID_BODY_UTM_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_INSPECTION_MODE = [
    "proxy",  # Proxy based inspection.
    "flow",  # Flow based inspection.
]
VALID_BODY_HTTP_POLICY_REDIRECT = [
    "enable",  # Enable HTTP(S) policy redirect.
    "disable",  # Disable HTTP(S) policy redirect.
    "legacy",  # Enable HTTP(S) policy redirect (for preserving old behavior, not recommended for new setups).
]
VALID_BODY_SSH_POLICY_REDIRECT = [
    "enable",  # Enable SSH policy redirect.
    "disable",  # Disable SSH policy redirect.
]
VALID_BODY_ZTNA_POLICY_REDIRECT = [
    "enable",  # Enable ZTNA proxy-policy redirect.
    "disable",  # Disable ZTNA proxy-policy redirect.
]
VALID_BODY_PROFILE_TYPE = [
    "single",  # Do not allow security profile groups.
    "group",  # Allow security profile groups.
]
VALID_BODY_LOGTRAFFIC = [
    "all",  # Log all sessions accepted or denied by this policy.
    "utm",  # Log traffic that has a security profile applied to it.
    "disable",  # Disable all logging for this policy.
]
VALID_BODY_LOGTRAFFIC_START = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOG_HTTP_TRANSACTION = [
    "enable",  # Enable HTTP transaction log.
    "disable",  # Disable HTTP transaction log.
]
VALID_BODY_CAPTURE_PACKET = [
    "enable",  # Enable capture packets.
    "disable",  # Disable capture packets.
]
VALID_BODY_AUTO_ASIC_OFFLOAD = [
    "enable",  # Enable auto ASIC offloading.
    "disable",  # Disable ASIC offloading.
]
VALID_BODY_WANOPT = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WANOPT_DETECTION = [
    "active",  # Active WAN optimization peer auto-detection.
    "passive",  # Passive WAN optimization peer auto-detection.
    "off",  # Turn off WAN optimization peer auto-detection.
]
VALID_BODY_WANOPT_PASSIVE_OPT = [
    "default",  # Allow client side WAN opt peer to decide.
    "transparent",  # Use address of client to connect to server.
    "non-transparent",  # Use local FortiGate address to connect to server.
]
VALID_BODY_WEBCACHE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEBCACHE_HTTPS = [
    "disable",  # Disable web cache for HTTPS.
    "enable",  # Enable web cache for HTTPS.
]
VALID_BODY_NAT = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PCP_OUTBOUND = [
    "enable",  # Enable PCP outbound SNAT.
    "disable",  # Disable PCP outbound SNAT.
]
VALID_BODY_PCP_INBOUND = [
    "enable",  # Enable PCP inbound DNAT.
    "disable",  # Disable PCP inbound DNAT.
]
VALID_BODY_PERMIT_ANY_HOST = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PERMIT_STUN_HOST = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_FIXEDPORT = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PORT_PRESERVE = [
    "enable",  # Use the original source port if it has not been used.
    "disable",  # Source NAT always changes the source port.
]
VALID_BODY_PORT_RANDOM = [
    "enable",  # Enable random source port selection for source NAT.
    "disable",  # Disable random source port selection for source NAT.
]
VALID_BODY_IPPOOL = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_INBOUND = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_OUTBOUND = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_NATINBOUND = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_NATOUTBOUND = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_FEC = [
    "enable",  # Enable Forward Error Correction.
    "disable",  # Disable Forward Error Correction.
]
VALID_BODY_WCCP = [
    "enable",  # Enable WCCP setting.
    "disable",  # Disable WCCP setting.
]
VALID_BODY_NTLM = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_NTLM_GUEST = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_AUTH_PATH = [
    "enable",  # Enable authentication-based routing.
    "disable",  # Disable authentication-based routing.
]
VALID_BODY_DISCLAIMER = [
    "enable",  # Enable user authentication disclaimer.
    "disable",  # Disable user authentication disclaimer.
]
VALID_BODY_EMAIL_COLLECT = [
    "enable",  # Enable email collection.
    "disable",  # Disable email collection.
]
VALID_BODY_MATCH_VIP = [
    "enable",  # Match DNATed packet.
    "disable",  # Do not match DNATed packet.
]
VALID_BODY_MATCH_VIP_ONLY = [
    "enable",  # Enable matching of only those packets that have had their destination addresses changed by a VIP.
    "disable",  # Disable matching of only those packets that have had their destination addresses changed by a VIP.
]
VALID_BODY_DIFFSERV_COPY = [
    "enable",  # Enable DSCP copy.
    "disable",  # Disable DSCP copy.
]
VALID_BODY_DIFFSERV_FORWARD = [
    "enable",  # Enable setting forward (original) traffic Diffserv.
    "disable",  # Disable setting forward (original) traffic Diffserv.
]
VALID_BODY_DIFFSERV_REVERSE = [
    "enable",  # Enable setting reverse (reply) traffic DiffServ.
    "disable",  # Disable setting reverse (reply) traffic DiffServ.
]
VALID_BODY_BLOCK_NOTIFICATION = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_SRCADDR_NEGATE = [
    "enable",  # Enable source address negate.
    "disable",  # Disable source address negate.
]
VALID_BODY_SRCADDR6_NEGATE = [
    "enable",  # Enable IPv6 source address negate.
    "disable",  # Disable IPv6 source address negate.
]
VALID_BODY_DSTADDR_NEGATE = [
    "enable",  # Enable destination address negate.
    "disable",  # Disable destination address negate.
]
VALID_BODY_DSTADDR6_NEGATE = [
    "enable",  # Enable IPv6 destination address negate.
    "disable",  # Disable IPv6 destination address negate.
]
VALID_BODY_ZTNA_EMS_TAG_NEGATE = [
    "enable",  # Enable ZTNA EMS tags negate.
    "disable",  # Disable ZTNA EMS tags negate.
]
VALID_BODY_SERVICE_NEGATE = [
    "enable",  # Enable negated service match.
    "disable",  # Disable negated service match.
]
VALID_BODY_INTERNET_SERVICE_NEGATE = [
    "enable",  # Enable negated Internet Service match.
    "disable",  # Disable negated Internet Service match.
]
VALID_BODY_INTERNET_SERVICE_SRC_NEGATE = [
    "enable",  # Enable negated Internet Service source match.
    "disable",  # Disable negated Internet Service source match.
]
VALID_BODY_INTERNET_SERVICE6_NEGATE = [
    "enable",  # Enable negated IPv6 Internet Service match.
    "disable",  # Disable negated IPv6 Internet Service match.
]
VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE = [
    "enable",  # Enable negated IPv6 Internet Service source match.
    "disable",  # Disable negated IPv6 Internet Service source match.
]
VALID_BODY_TIMEOUT_SEND_RST = [
    "enable",  # Enable sending of RST packet upon TCP session expiration.
    "disable",  # Disable sending of RST packet upon TCP session expiration.
]
VALID_BODY_CAPTIVE_PORTAL_EXEMPT = [
    "enable",  # Enable exemption of captive portal.
    "disable",  # Disable exemption of captive portal.
]
VALID_BODY_DSRI = [
    "enable",  # Enable DSRI.
    "disable",  # Disable DSRI.
]
VALID_BODY_RADIUS_MAC_AUTH_BYPASS = [
    "enable",  # Enable MAC authentication bypass.
    "disable",  # Disable MAC authentication bypass.
]
VALID_BODY_RADIUS_IP_AUTH_BYPASS = [
    "enable",  # Enable IP authentication bypass.
    "disable",  # Disable IP authentication bypass.
]
VALID_BODY_DELAY_TCP_NPU_SESSION = [
    "enable",  # Enable TCP NPU session delay in order to guarantee packet order of 3-way handshake.
    "disable",  # Disable TCP NPU session delay in order to guarantee packet order of 3-way handshake.
]
VALID_BODY_SGT_CHECK = [
    "enable",  # Enable SGT check.
    "disable",  # Disable SGT check.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for firewall/policy.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_firewall_policy_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by policyid
        >>> is_valid, error = validate_firewall_policy_get(policyid="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_firewall_policy_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """
    Validate required fields for firewall/policy.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_firewall_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new firewall/policy object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ...     "srcintf": True,  # Incoming (ingress) interface.
        ...     "dstintf": True,  # Outgoing (egress) interface.
        ... }
        >>> is_valid, error = validate_firewall_policy_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "srcintf": True,
        ...     "status": "{'name': 'enable', 'help': 'Enable setting.', 'label': 'Enable', 'description': 'Enable setting'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_firewall_policy_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["status"] = "invalid-value"
        >>> is_valid, error = validate_firewall_policy_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_firewall_policy_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            desc = FIELD_DESCRIPTIONS.get("status", "")
            error_msg = f"Invalid value for 'status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STATUS)}"
            error_msg += f"\n  → Example: status='{{ VALID_BODY_STATUS[0] }}'"
            return (False, error_msg)
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            desc = FIELD_DESCRIPTIONS.get("action", "")
            error_msg = f"Invalid value for 'action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACTION)}"
            error_msg += f"\n  → Example: action='{{ VALID_BODY_ACTION[0] }}'"
            return (False, error_msg)
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            desc = FIELD_DESCRIPTIONS.get("nat64", "")
            error_msg = f"Invalid value for 'nat64': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT64)}"
            error_msg += f"\n  → Example: nat64='{{ VALID_BODY_NAT64[0] }}'"
            return (False, error_msg)
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            desc = FIELD_DESCRIPTIONS.get("nat46", "")
            error_msg = f"Invalid value for 'nat46': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT46)}"
            error_msg += f"\n  → Example: nat46='{{ VALID_BODY_NAT46[0] }}'"
            return (False, error_msg)
    if "ztna-status" in payload:
        value = payload["ztna-status"]
        if value not in VALID_BODY_ZTNA_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ztna-status", "")
            error_msg = f"Invalid value for 'ztna-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_STATUS)}"
            error_msg += f"\n  → Example: ztna-status='{{ VALID_BODY_ZTNA_STATUS[0] }}'"
            return (False, error_msg)
    if "ztna-device-ownership" in payload:
        value = payload["ztna-device-ownership"]
        if value not in VALID_BODY_ZTNA_DEVICE_OWNERSHIP:
            desc = FIELD_DESCRIPTIONS.get("ztna-device-ownership", "")
            error_msg = f"Invalid value for 'ztna-device-ownership': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_DEVICE_OWNERSHIP)}"
            error_msg += f"\n  → Example: ztna-device-ownership='{{ VALID_BODY_ZTNA_DEVICE_OWNERSHIP[0] }}'"
            return (False, error_msg)
    if "ztna-tags-match-logic" in payload:
        value = payload["ztna-tags-match-logic"]
        if value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            desc = FIELD_DESCRIPTIONS.get("ztna-tags-match-logic", "")
            error_msg = f"Invalid value for 'ztna-tags-match-logic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}"
            error_msg += f"\n  → Example: ztna-tags-match-logic='{{ VALID_BODY_ZTNA_TAGS_MATCH_LOGIC[0] }}'"
            return (False, error_msg)
    if "internet-service" in payload:
        value = payload["internet-service"]
        if value not in VALID_BODY_INTERNET_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("internet-service", "")
            error_msg = f"Invalid value for 'internet-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE)}"
            error_msg += f"\n  → Example: internet-service='{{ VALID_BODY_INTERNET_SERVICE[0] }}'"
            return (False, error_msg)
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            desc = FIELD_DESCRIPTIONS.get("internet-service-src", "")
            error_msg = f"Invalid value for 'internet-service-src': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_SRC)}"
            error_msg += f"\n  → Example: internet-service-src='{{ VALID_BODY_INTERNET_SERVICE_SRC[0] }}'"
            return (False, error_msg)
    if "reputation-direction" in payload:
        value = payload["reputation-direction"]
        if value not in VALID_BODY_REPUTATION_DIRECTION:
            desc = FIELD_DESCRIPTIONS.get("reputation-direction", "")
            error_msg = f"Invalid value for 'reputation-direction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REPUTATION_DIRECTION)}"
            error_msg += f"\n  → Example: reputation-direction='{{ VALID_BODY_REPUTATION_DIRECTION[0] }}'"
            return (False, error_msg)
    if "internet-service6" in payload:
        value = payload["internet-service6"]
        if value not in VALID_BODY_INTERNET_SERVICE6:
            desc = FIELD_DESCRIPTIONS.get("internet-service6", "")
            error_msg = f"Invalid value for 'internet-service6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE6)}"
            error_msg += f"\n  → Example: internet-service6='{{ VALID_BODY_INTERNET_SERVICE6[0] }}'"
            return (False, error_msg)
    if "internet-service6-src" in payload:
        value = payload["internet-service6-src"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            desc = FIELD_DESCRIPTIONS.get("internet-service6-src", "")
            error_msg = f"Invalid value for 'internet-service6-src': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE6_SRC)}"
            error_msg += f"\n  → Example: internet-service6-src='{{ VALID_BODY_INTERNET_SERVICE6_SRC[0] }}'"
            return (False, error_msg)
    if "reputation-direction6" in payload:
        value = payload["reputation-direction6"]
        if value not in VALID_BODY_REPUTATION_DIRECTION6:
            desc = FIELD_DESCRIPTIONS.get("reputation-direction6", "")
            error_msg = f"Invalid value for 'reputation-direction6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REPUTATION_DIRECTION6)}"
            error_msg += f"\n  → Example: reputation-direction6='{{ VALID_BODY_REPUTATION_DIRECTION6[0] }}'"
            return (False, error_msg)
    if "rtp-nat" in payload:
        value = payload["rtp-nat"]
        if value not in VALID_BODY_RTP_NAT:
            desc = FIELD_DESCRIPTIONS.get("rtp-nat", "")
            error_msg = f"Invalid value for 'rtp-nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RTP_NAT)}"
            error_msg += f"\n  → Example: rtp-nat='{{ VALID_BODY_RTP_NAT[0] }}'"
            return (False, error_msg)
    if "send-deny-packet" in payload:
        value = payload["send-deny-packet"]
        if value not in VALID_BODY_SEND_DENY_PACKET:
            desc = FIELD_DESCRIPTIONS.get("send-deny-packet", "")
            error_msg = f"Invalid value for 'send-deny-packet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEND_DENY_PACKET)}"
            error_msg += f"\n  → Example: send-deny-packet='{{ VALID_BODY_SEND_DENY_PACKET[0] }}'"
            return (False, error_msg)
    if "firewall-session-dirty" in payload:
        value = payload["firewall-session-dirty"]
        if value not in VALID_BODY_FIREWALL_SESSION_DIRTY:
            desc = FIELD_DESCRIPTIONS.get("firewall-session-dirty", "")
            error_msg = f"Invalid value for 'firewall-session-dirty': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIREWALL_SESSION_DIRTY)}"
            error_msg += f"\n  → Example: firewall-session-dirty='{{ VALID_BODY_FIREWALL_SESSION_DIRTY[0] }}'"
            return (False, error_msg)
    if "schedule-timeout" in payload:
        value = payload["schedule-timeout"]
        if value not in VALID_BODY_SCHEDULE_TIMEOUT:
            desc = FIELD_DESCRIPTIONS.get("schedule-timeout", "")
            error_msg = f"Invalid value for 'schedule-timeout': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCHEDULE_TIMEOUT)}"
            error_msg += f"\n  → Example: schedule-timeout='{{ VALID_BODY_SCHEDULE_TIMEOUT[0] }}'"
            return (False, error_msg)
    if "policy-expiry" in payload:
        value = payload["policy-expiry"]
        if value not in VALID_BODY_POLICY_EXPIRY:
            desc = FIELD_DESCRIPTIONS.get("policy-expiry", "")
            error_msg = f"Invalid value for 'policy-expiry': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POLICY_EXPIRY)}"
            error_msg += f"\n  → Example: policy-expiry='{{ VALID_BODY_POLICY_EXPIRY[0] }}'"
            return (False, error_msg)
    if "tos-negate" in payload:
        value = payload["tos-negate"]
        if value not in VALID_BODY_TOS_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("tos-negate", "")
            error_msg = f"Invalid value for 'tos-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TOS_NEGATE)}"
            error_msg += f"\n  → Example: tos-negate='{{ VALID_BODY_TOS_NEGATE[0] }}'"
            return (False, error_msg)
    if "anti-replay" in payload:
        value = payload["anti-replay"]
        if value not in VALID_BODY_ANTI_REPLAY:
            desc = FIELD_DESCRIPTIONS.get("anti-replay", "")
            error_msg = f"Invalid value for 'anti-replay': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANTI_REPLAY)}"
            error_msg += f"\n  → Example: anti-replay='{{ VALID_BODY_ANTI_REPLAY[0] }}'"
            return (False, error_msg)
    if "tcp-session-without-syn" in payload:
        value = payload["tcp-session-without-syn"]
        if value not in VALID_BODY_TCP_SESSION_WITHOUT_SYN:
            desc = FIELD_DESCRIPTIONS.get("tcp-session-without-syn", "")
            error_msg = f"Invalid value for 'tcp-session-without-syn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TCP_SESSION_WITHOUT_SYN)}"
            error_msg += f"\n  → Example: tcp-session-without-syn='{{ VALID_BODY_TCP_SESSION_WITHOUT_SYN[0] }}'"
            return (False, error_msg)
    if "geoip-anycast" in payload:
        value = payload["geoip-anycast"]
        if value not in VALID_BODY_GEOIP_ANYCAST:
            desc = FIELD_DESCRIPTIONS.get("geoip-anycast", "")
            error_msg = f"Invalid value for 'geoip-anycast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GEOIP_ANYCAST)}"
            error_msg += f"\n  → Example: geoip-anycast='{{ VALID_BODY_GEOIP_ANYCAST[0] }}'"
            return (False, error_msg)
    if "geoip-match" in payload:
        value = payload["geoip-match"]
        if value not in VALID_BODY_GEOIP_MATCH:
            desc = FIELD_DESCRIPTIONS.get("geoip-match", "")
            error_msg = f"Invalid value for 'geoip-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GEOIP_MATCH)}"
            error_msg += f"\n  → Example: geoip-match='{{ VALID_BODY_GEOIP_MATCH[0] }}'"
            return (False, error_msg)
    if "dynamic-shaping" in payload:
        value = payload["dynamic-shaping"]
        if value not in VALID_BODY_DYNAMIC_SHAPING:
            desc = FIELD_DESCRIPTIONS.get("dynamic-shaping", "")
            error_msg = f"Invalid value for 'dynamic-shaping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYNAMIC_SHAPING)}"
            error_msg += f"\n  → Example: dynamic-shaping='{{ VALID_BODY_DYNAMIC_SHAPING[0] }}'"
            return (False, error_msg)
    if "passive-wan-health-measurement" in payload:
        value = payload["passive-wan-health-measurement"]
        if value not in VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT:
            desc = FIELD_DESCRIPTIONS.get("passive-wan-health-measurement", "")
            error_msg = f"Invalid value for 'passive-wan-health-measurement': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT)}"
            error_msg += f"\n  → Example: passive-wan-health-measurement='{{ VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT[0] }}'"
            return (False, error_msg)
    if "app-monitor" in payload:
        value = payload["app-monitor"]
        if value not in VALID_BODY_APP_MONITOR:
            desc = FIELD_DESCRIPTIONS.get("app-monitor", "")
            error_msg = f"Invalid value for 'app-monitor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APP_MONITOR)}"
            error_msg += f"\n  → Example: app-monitor='{{ VALID_BODY_APP_MONITOR[0] }}'"
            return (False, error_msg)
    if "utm-status" in payload:
        value = payload["utm-status"]
        if value not in VALID_BODY_UTM_STATUS:
            desc = FIELD_DESCRIPTIONS.get("utm-status", "")
            error_msg = f"Invalid value for 'utm-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTM_STATUS)}"
            error_msg += f"\n  → Example: utm-status='{{ VALID_BODY_UTM_STATUS[0] }}'"
            return (False, error_msg)
    if "inspection-mode" in payload:
        value = payload["inspection-mode"]
        if value not in VALID_BODY_INSPECTION_MODE:
            desc = FIELD_DESCRIPTIONS.get("inspection-mode", "")
            error_msg = f"Invalid value for 'inspection-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INSPECTION_MODE)}"
            error_msg += f"\n  → Example: inspection-mode='{{ VALID_BODY_INSPECTION_MODE[0] }}'"
            return (False, error_msg)
    if "http-policy-redirect" in payload:
        value = payload["http-policy-redirect"]
        if value not in VALID_BODY_HTTP_POLICY_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("http-policy-redirect", "")
            error_msg = f"Invalid value for 'http-policy-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_POLICY_REDIRECT)}"
            error_msg += f"\n  → Example: http-policy-redirect='{{ VALID_BODY_HTTP_POLICY_REDIRECT[0] }}'"
            return (False, error_msg)
    if "ssh-policy-redirect" in payload:
        value = payload["ssh-policy-redirect"]
        if value not in VALID_BODY_SSH_POLICY_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("ssh-policy-redirect", "")
            error_msg = f"Invalid value for 'ssh-policy-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSH_POLICY_REDIRECT)}"
            error_msg += f"\n  → Example: ssh-policy-redirect='{{ VALID_BODY_SSH_POLICY_REDIRECT[0] }}'"
            return (False, error_msg)
    if "ztna-policy-redirect" in payload:
        value = payload["ztna-policy-redirect"]
        if value not in VALID_BODY_ZTNA_POLICY_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("ztna-policy-redirect", "")
            error_msg = f"Invalid value for 'ztna-policy-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_POLICY_REDIRECT)}"
            error_msg += f"\n  → Example: ztna-policy-redirect='{{ VALID_BODY_ZTNA_POLICY_REDIRECT[0] }}'"
            return (False, error_msg)
    if "profile-type" in payload:
        value = payload["profile-type"]
        if value not in VALID_BODY_PROFILE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("profile-type", "")
            error_msg = f"Invalid value for 'profile-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROFILE_TYPE)}"
            error_msg += f"\n  → Example: profile-type='{{ VALID_BODY_PROFILE_TYPE[0] }}'"
            return (False, error_msg)
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("logtraffic", "")
            error_msg = f"Invalid value for 'logtraffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGTRAFFIC)}"
            error_msg += f"\n  → Example: logtraffic='{{ VALID_BODY_LOGTRAFFIC[0] }}'"
            return (False, error_msg)
    if "logtraffic-start" in payload:
        value = payload["logtraffic-start"]
        if value not in VALID_BODY_LOGTRAFFIC_START:
            desc = FIELD_DESCRIPTIONS.get("logtraffic-start", "")
            error_msg = f"Invalid value for 'logtraffic-start': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGTRAFFIC_START)}"
            error_msg += f"\n  → Example: logtraffic-start='{{ VALID_BODY_LOGTRAFFIC_START[0] }}'"
            return (False, error_msg)
    if "log-http-transaction" in payload:
        value = payload["log-http-transaction"]
        if value not in VALID_BODY_LOG_HTTP_TRANSACTION:
            desc = FIELD_DESCRIPTIONS.get("log-http-transaction", "")
            error_msg = f"Invalid value for 'log-http-transaction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_HTTP_TRANSACTION)}"
            error_msg += f"\n  → Example: log-http-transaction='{{ VALID_BODY_LOG_HTTP_TRANSACTION[0] }}'"
            return (False, error_msg)
    if "capture-packet" in payload:
        value = payload["capture-packet"]
        if value not in VALID_BODY_CAPTURE_PACKET:
            desc = FIELD_DESCRIPTIONS.get("capture-packet", "")
            error_msg = f"Invalid value for 'capture-packet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTURE_PACKET)}"
            error_msg += f"\n  → Example: capture-packet='{{ VALID_BODY_CAPTURE_PACKET[0] }}'"
            return (False, error_msg)
    if "auto-asic-offload" in payload:
        value = payload["auto-asic-offload"]
        if value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("auto-asic-offload", "")
            error_msg = f"Invalid value for 'auto-asic-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_ASIC_OFFLOAD)}"
            error_msg += f"\n  → Example: auto-asic-offload='{{ VALID_BODY_AUTO_ASIC_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "wanopt" in payload:
        value = payload["wanopt"]
        if value not in VALID_BODY_WANOPT:
            desc = FIELD_DESCRIPTIONS.get("wanopt", "")
            error_msg = f"Invalid value for 'wanopt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WANOPT)}"
            error_msg += f"\n  → Example: wanopt='{{ VALID_BODY_WANOPT[0] }}'"
            return (False, error_msg)
    if "wanopt-detection" in payload:
        value = payload["wanopt-detection"]
        if value not in VALID_BODY_WANOPT_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("wanopt-detection", "")
            error_msg = f"Invalid value for 'wanopt-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WANOPT_DETECTION)}"
            error_msg += f"\n  → Example: wanopt-detection='{{ VALID_BODY_WANOPT_DETECTION[0] }}'"
            return (False, error_msg)
    if "wanopt-passive-opt" in payload:
        value = payload["wanopt-passive-opt"]
        if value not in VALID_BODY_WANOPT_PASSIVE_OPT:
            desc = FIELD_DESCRIPTIONS.get("wanopt-passive-opt", "")
            error_msg = f"Invalid value for 'wanopt-passive-opt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WANOPT_PASSIVE_OPT)}"
            error_msg += f"\n  → Example: wanopt-passive-opt='{{ VALID_BODY_WANOPT_PASSIVE_OPT[0] }}'"
            return (False, error_msg)
    if "webcache" in payload:
        value = payload["webcache"]
        if value not in VALID_BODY_WEBCACHE:
            desc = FIELD_DESCRIPTIONS.get("webcache", "")
            error_msg = f"Invalid value for 'webcache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBCACHE)}"
            error_msg += f"\n  → Example: webcache='{{ VALID_BODY_WEBCACHE[0] }}'"
            return (False, error_msg)
    if "webcache-https" in payload:
        value = payload["webcache-https"]
        if value not in VALID_BODY_WEBCACHE_HTTPS:
            desc = FIELD_DESCRIPTIONS.get("webcache-https", "")
            error_msg = f"Invalid value for 'webcache-https': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEBCACHE_HTTPS)}"
            error_msg += f"\n  → Example: webcache-https='{{ VALID_BODY_WEBCACHE_HTTPS[0] }}'"
            return (False, error_msg)
    if "nat" in payload:
        value = payload["nat"]
        if value not in VALID_BODY_NAT:
            desc = FIELD_DESCRIPTIONS.get("nat", "")
            error_msg = f"Invalid value for 'nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT)}"
            error_msg += f"\n  → Example: nat='{{ VALID_BODY_NAT[0] }}'"
            return (False, error_msg)
    if "pcp-outbound" in payload:
        value = payload["pcp-outbound"]
        if value not in VALID_BODY_PCP_OUTBOUND:
            desc = FIELD_DESCRIPTIONS.get("pcp-outbound", "")
            error_msg = f"Invalid value for 'pcp-outbound': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PCP_OUTBOUND)}"
            error_msg += f"\n  → Example: pcp-outbound='{{ VALID_BODY_PCP_OUTBOUND[0] }}'"
            return (False, error_msg)
    if "pcp-inbound" in payload:
        value = payload["pcp-inbound"]
        if value not in VALID_BODY_PCP_INBOUND:
            desc = FIELD_DESCRIPTIONS.get("pcp-inbound", "")
            error_msg = f"Invalid value for 'pcp-inbound': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PCP_INBOUND)}"
            error_msg += f"\n  → Example: pcp-inbound='{{ VALID_BODY_PCP_INBOUND[0] }}'"
            return (False, error_msg)
    if "permit-any-host" in payload:
        value = payload["permit-any-host"]
        if value not in VALID_BODY_PERMIT_ANY_HOST:
            desc = FIELD_DESCRIPTIONS.get("permit-any-host", "")
            error_msg = f"Invalid value for 'permit-any-host': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_ANY_HOST)}"
            error_msg += f"\n  → Example: permit-any-host='{{ VALID_BODY_PERMIT_ANY_HOST[0] }}'"
            return (False, error_msg)
    if "permit-stun-host" in payload:
        value = payload["permit-stun-host"]
        if value not in VALID_BODY_PERMIT_STUN_HOST:
            desc = FIELD_DESCRIPTIONS.get("permit-stun-host", "")
            error_msg = f"Invalid value for 'permit-stun-host': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PERMIT_STUN_HOST)}"
            error_msg += f"\n  → Example: permit-stun-host='{{ VALID_BODY_PERMIT_STUN_HOST[0] }}'"
            return (False, error_msg)
    if "fixedport" in payload:
        value = payload["fixedport"]
        if value not in VALID_BODY_FIXEDPORT:
            desc = FIELD_DESCRIPTIONS.get("fixedport", "")
            error_msg = f"Invalid value for 'fixedport': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FIXEDPORT)}"
            error_msg += f"\n  → Example: fixedport='{{ VALID_BODY_FIXEDPORT[0] }}'"
            return (False, error_msg)
    if "port-preserve" in payload:
        value = payload["port-preserve"]
        if value not in VALID_BODY_PORT_PRESERVE:
            desc = FIELD_DESCRIPTIONS.get("port-preserve", "")
            error_msg = f"Invalid value for 'port-preserve': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_PRESERVE)}"
            error_msg += f"\n  → Example: port-preserve='{{ VALID_BODY_PORT_PRESERVE[0] }}'"
            return (False, error_msg)
    if "port-random" in payload:
        value = payload["port-random"]
        if value not in VALID_BODY_PORT_RANDOM:
            desc = FIELD_DESCRIPTIONS.get("port-random", "")
            error_msg = f"Invalid value for 'port-random': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_RANDOM)}"
            error_msg += f"\n  → Example: port-random='{{ VALID_BODY_PORT_RANDOM[0] }}'"
            return (False, error_msg)
    if "ippool" in payload:
        value = payload["ippool"]
        if value not in VALID_BODY_IPPOOL:
            desc = FIELD_DESCRIPTIONS.get("ippool", "")
            error_msg = f"Invalid value for 'ippool': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPPOOL)}"
            error_msg += f"\n  → Example: ippool='{{ VALID_BODY_IPPOOL[0] }}'"
            return (False, error_msg)
    if "inbound" in payload:
        value = payload["inbound"]
        if value not in VALID_BODY_INBOUND:
            desc = FIELD_DESCRIPTIONS.get("inbound", "")
            error_msg = f"Invalid value for 'inbound': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INBOUND)}"
            error_msg += f"\n  → Example: inbound='{{ VALID_BODY_INBOUND[0] }}'"
            return (False, error_msg)
    if "outbound" in payload:
        value = payload["outbound"]
        if value not in VALID_BODY_OUTBOUND:
            desc = FIELD_DESCRIPTIONS.get("outbound", "")
            error_msg = f"Invalid value for 'outbound': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OUTBOUND)}"
            error_msg += f"\n  → Example: outbound='{{ VALID_BODY_OUTBOUND[0] }}'"
            return (False, error_msg)
    if "natinbound" in payload:
        value = payload["natinbound"]
        if value not in VALID_BODY_NATINBOUND:
            desc = FIELD_DESCRIPTIONS.get("natinbound", "")
            error_msg = f"Invalid value for 'natinbound': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NATINBOUND)}"
            error_msg += f"\n  → Example: natinbound='{{ VALID_BODY_NATINBOUND[0] }}'"
            return (False, error_msg)
    if "natoutbound" in payload:
        value = payload["natoutbound"]
        if value not in VALID_BODY_NATOUTBOUND:
            desc = FIELD_DESCRIPTIONS.get("natoutbound", "")
            error_msg = f"Invalid value for 'natoutbound': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NATOUTBOUND)}"
            error_msg += f"\n  → Example: natoutbound='{{ VALID_BODY_NATOUTBOUND[0] }}'"
            return (False, error_msg)
    if "fec" in payload:
        value = payload["fec"]
        if value not in VALID_BODY_FEC:
            desc = FIELD_DESCRIPTIONS.get("fec", "")
            error_msg = f"Invalid value for 'fec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEC)}"
            error_msg += f"\n  → Example: fec='{{ VALID_BODY_FEC[0] }}'"
            return (False, error_msg)
    if "wccp" in payload:
        value = payload["wccp"]
        if value not in VALID_BODY_WCCP:
            desc = FIELD_DESCRIPTIONS.get("wccp", "")
            error_msg = f"Invalid value for 'wccp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WCCP)}"
            error_msg += f"\n  → Example: wccp='{{ VALID_BODY_WCCP[0] }}'"
            return (False, error_msg)
    if "ntlm" in payload:
        value = payload["ntlm"]
        if value not in VALID_BODY_NTLM:
            desc = FIELD_DESCRIPTIONS.get("ntlm", "")
            error_msg = f"Invalid value for 'ntlm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NTLM)}"
            error_msg += f"\n  → Example: ntlm='{{ VALID_BODY_NTLM[0] }}'"
            return (False, error_msg)
    if "ntlm-guest" in payload:
        value = payload["ntlm-guest"]
        if value not in VALID_BODY_NTLM_GUEST:
            desc = FIELD_DESCRIPTIONS.get("ntlm-guest", "")
            error_msg = f"Invalid value for 'ntlm-guest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NTLM_GUEST)}"
            error_msg += f"\n  → Example: ntlm-guest='{{ VALID_BODY_NTLM_GUEST[0] }}'"
            return (False, error_msg)
    if "auth-path" in payload:
        value = payload["auth-path"]
        if value not in VALID_BODY_AUTH_PATH:
            desc = FIELD_DESCRIPTIONS.get("auth-path", "")
            error_msg = f"Invalid value for 'auth-path': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_PATH)}"
            error_msg += f"\n  → Example: auth-path='{{ VALID_BODY_AUTH_PATH[0] }}'"
            return (False, error_msg)
    if "disclaimer" in payload:
        value = payload["disclaimer"]
        if value not in VALID_BODY_DISCLAIMER:
            desc = FIELD_DESCRIPTIONS.get("disclaimer", "")
            error_msg = f"Invalid value for 'disclaimer': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISCLAIMER)}"
            error_msg += f"\n  → Example: disclaimer='{{ VALID_BODY_DISCLAIMER[0] }}'"
            return (False, error_msg)
    if "email-collect" in payload:
        value = payload["email-collect"]
        if value not in VALID_BODY_EMAIL_COLLECT:
            desc = FIELD_DESCRIPTIONS.get("email-collect", "")
            error_msg = f"Invalid value for 'email-collect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMAIL_COLLECT)}"
            error_msg += f"\n  → Example: email-collect='{{ VALID_BODY_EMAIL_COLLECT[0] }}'"
            return (False, error_msg)
    if "match-vip" in payload:
        value = payload["match-vip"]
        if value not in VALID_BODY_MATCH_VIP:
            desc = FIELD_DESCRIPTIONS.get("match-vip", "")
            error_msg = f"Invalid value for 'match-vip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_VIP)}"
            error_msg += f"\n  → Example: match-vip='{{ VALID_BODY_MATCH_VIP[0] }}'"
            return (False, error_msg)
    if "match-vip-only" in payload:
        value = payload["match-vip-only"]
        if value not in VALID_BODY_MATCH_VIP_ONLY:
            desc = FIELD_DESCRIPTIONS.get("match-vip-only", "")
            error_msg = f"Invalid value for 'match-vip-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MATCH_VIP_ONLY)}"
            error_msg += f"\n  → Example: match-vip-only='{{ VALID_BODY_MATCH_VIP_ONLY[0] }}'"
            return (False, error_msg)
    if "diffserv-copy" in payload:
        value = payload["diffserv-copy"]
        if value not in VALID_BODY_DIFFSERV_COPY:
            desc = FIELD_DESCRIPTIONS.get("diffserv-copy", "")
            error_msg = f"Invalid value for 'diffserv-copy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_COPY)}"
            error_msg += f"\n  → Example: diffserv-copy='{{ VALID_BODY_DIFFSERV_COPY[0] }}'"
            return (False, error_msg)
    if "diffserv-forward" in payload:
        value = payload["diffserv-forward"]
        if value not in VALID_BODY_DIFFSERV_FORWARD:
            desc = FIELD_DESCRIPTIONS.get("diffserv-forward", "")
            error_msg = f"Invalid value for 'diffserv-forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_FORWARD)}"
            error_msg += f"\n  → Example: diffserv-forward='{{ VALID_BODY_DIFFSERV_FORWARD[0] }}'"
            return (False, error_msg)
    if "diffserv-reverse" in payload:
        value = payload["diffserv-reverse"]
        if value not in VALID_BODY_DIFFSERV_REVERSE:
            desc = FIELD_DESCRIPTIONS.get("diffserv-reverse", "")
            error_msg = f"Invalid value for 'diffserv-reverse': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIFFSERV_REVERSE)}"
            error_msg += f"\n  → Example: diffserv-reverse='{{ VALID_BODY_DIFFSERV_REVERSE[0] }}'"
            return (False, error_msg)
    if "block-notification" in payload:
        value = payload["block-notification"]
        if value not in VALID_BODY_BLOCK_NOTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("block-notification", "")
            error_msg = f"Invalid value for 'block-notification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCK_NOTIFICATION)}"
            error_msg += f"\n  → Example: block-notification='{{ VALID_BODY_BLOCK_NOTIFICATION[0] }}'"
            return (False, error_msg)
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("srcaddr-negate", "")
            error_msg = f"Invalid value for 'srcaddr-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRCADDR_NEGATE)}"
            error_msg += f"\n  → Example: srcaddr-negate='{{ VALID_BODY_SRCADDR_NEGATE[0] }}'"
            return (False, error_msg)
    if "srcaddr6-negate" in payload:
        value = payload["srcaddr6-negate"]
        if value not in VALID_BODY_SRCADDR6_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("srcaddr6-negate", "")
            error_msg = f"Invalid value for 'srcaddr6-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRCADDR6_NEGATE)}"
            error_msg += f"\n  → Example: srcaddr6-negate='{{ VALID_BODY_SRCADDR6_NEGATE[0] }}'"
            return (False, error_msg)
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("dstaddr-negate", "")
            error_msg = f"Invalid value for 'dstaddr-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSTADDR_NEGATE)}"
            error_msg += f"\n  → Example: dstaddr-negate='{{ VALID_BODY_DSTADDR_NEGATE[0] }}'"
            return (False, error_msg)
    if "dstaddr6-negate" in payload:
        value = payload["dstaddr6-negate"]
        if value not in VALID_BODY_DSTADDR6_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("dstaddr6-negate", "")
            error_msg = f"Invalid value for 'dstaddr6-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSTADDR6_NEGATE)}"
            error_msg += f"\n  → Example: dstaddr6-negate='{{ VALID_BODY_DSTADDR6_NEGATE[0] }}'"
            return (False, error_msg)
    if "ztna-ems-tag-negate" in payload:
        value = payload["ztna-ems-tag-negate"]
        if value not in VALID_BODY_ZTNA_EMS_TAG_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("ztna-ems-tag-negate", "")
            error_msg = f"Invalid value for 'ztna-ems-tag-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ZTNA_EMS_TAG_NEGATE)}"
            error_msg += f"\n  → Example: ztna-ems-tag-negate='{{ VALID_BODY_ZTNA_EMS_TAG_NEGATE[0] }}'"
            return (False, error_msg)
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("service-negate", "")
            error_msg = f"Invalid value for 'service-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SERVICE_NEGATE)}"
            error_msg += f"\n  → Example: service-negate='{{ VALID_BODY_SERVICE_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service-negate" in payload:
        value = payload["internet-service-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("internet-service-negate", "")
            error_msg = f"Invalid value for 'internet-service-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_NEGATE)}"
            error_msg += f"\n  → Example: internet-service-negate='{{ VALID_BODY_INTERNET_SERVICE_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service-src-negate" in payload:
        value = payload["internet-service-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("internet-service-src-negate", "")
            error_msg = f"Invalid value for 'internet-service-src-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}"
            error_msg += f"\n  → Example: internet-service-src-negate='{{ VALID_BODY_INTERNET_SERVICE_SRC_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service6-negate" in payload:
        value = payload["internet-service6-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("internet-service6-negate", "")
            error_msg = f"Invalid value for 'internet-service6-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE6_NEGATE)}"
            error_msg += f"\n  → Example: internet-service6-negate='{{ VALID_BODY_INTERNET_SERVICE6_NEGATE[0] }}'"
            return (False, error_msg)
    if "internet-service6-src-negate" in payload:
        value = payload["internet-service6-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            desc = FIELD_DESCRIPTIONS.get("internet-service6-src-negate", "")
            error_msg = f"Invalid value for 'internet-service6-src-negate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}"
            error_msg += f"\n  → Example: internet-service6-src-negate='{{ VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE[0] }}'"
            return (False, error_msg)
    if "timeout-send-rst" in payload:
        value = payload["timeout-send-rst"]
        if value not in VALID_BODY_TIMEOUT_SEND_RST:
            desc = FIELD_DESCRIPTIONS.get("timeout-send-rst", "")
            error_msg = f"Invalid value for 'timeout-send-rst': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TIMEOUT_SEND_RST)}"
            error_msg += f"\n  → Example: timeout-send-rst='{{ VALID_BODY_TIMEOUT_SEND_RST[0] }}'"
            return (False, error_msg)
    if "captive-portal-exempt" in payload:
        value = payload["captive-portal-exempt"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_EXEMPT:
            desc = FIELD_DESCRIPTIONS.get("captive-portal-exempt", "")
            error_msg = f"Invalid value for 'captive-portal-exempt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTIVE_PORTAL_EXEMPT)}"
            error_msg += f"\n  → Example: captive-portal-exempt='{{ VALID_BODY_CAPTIVE_PORTAL_EXEMPT[0] }}'"
            return (False, error_msg)
    if "dsri" in payload:
        value = payload["dsri"]
        if value not in VALID_BODY_DSRI:
            desc = FIELD_DESCRIPTIONS.get("dsri", "")
            error_msg = f"Invalid value for 'dsri': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DSRI)}"
            error_msg += f"\n  → Example: dsri='{{ VALID_BODY_DSRI[0] }}'"
            return (False, error_msg)
    if "radius-mac-auth-bypass" in payload:
        value = payload["radius-mac-auth-bypass"]
        if value not in VALID_BODY_RADIUS_MAC_AUTH_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("radius-mac-auth-bypass", "")
            error_msg = f"Invalid value for 'radius-mac-auth-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_MAC_AUTH_BYPASS)}"
            error_msg += f"\n  → Example: radius-mac-auth-bypass='{{ VALID_BODY_RADIUS_MAC_AUTH_BYPASS[0] }}'"
            return (False, error_msg)
    if "radius-ip-auth-bypass" in payload:
        value = payload["radius-ip-auth-bypass"]
        if value not in VALID_BODY_RADIUS_IP_AUTH_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("radius-ip-auth-bypass", "")
            error_msg = f"Invalid value for 'radius-ip-auth-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_IP_AUTH_BYPASS)}"
            error_msg += f"\n  → Example: radius-ip-auth-bypass='{{ VALID_BODY_RADIUS_IP_AUTH_BYPASS[0] }}'"
            return (False, error_msg)
    if "delay-tcp-npu-session" in payload:
        value = payload["delay-tcp-npu-session"]
        if value not in VALID_BODY_DELAY_TCP_NPU_SESSION:
            desc = FIELD_DESCRIPTIONS.get("delay-tcp-npu-session", "")
            error_msg = f"Invalid value for 'delay-tcp-npu-session': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DELAY_TCP_NPU_SESSION)}"
            error_msg += f"\n  → Example: delay-tcp-npu-session='{{ VALID_BODY_DELAY_TCP_NPU_SESSION[0] }}'"
            return (False, error_msg)
    if "sgt-check" in payload:
        value = payload["sgt-check"]
        if value not in VALID_BODY_SGT_CHECK:
            desc = FIELD_DESCRIPTIONS.get("sgt-check", "")
            error_msg = f"Invalid value for 'sgt-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SGT_CHECK)}"
            error_msg += f"\n  → Example: sgt-check='{{ VALID_BODY_SGT_CHECK[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update firewall/policy.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_firewall_policy_put(payload)
    """
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid value for 'nat64'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid value for 'nat46'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )
    if "ztna-status" in payload:
        value = payload["ztna-status"]
        if value not in VALID_BODY_ZTNA_STATUS:
            return (
                False,
                f"Invalid value for 'ztna-status'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_STATUS)}",
            )
    if "ztna-device-ownership" in payload:
        value = payload["ztna-device-ownership"]
        if value not in VALID_BODY_ZTNA_DEVICE_OWNERSHIP:
            return (
                False,
                f"Invalid value for 'ztna-device-ownership'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_DEVICE_OWNERSHIP)}",
            )
    if "ztna-tags-match-logic" in payload:
        value = payload["ztna-tags-match-logic"]
        if value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            return (
                False,
                f"Invalid value for 'ztna-tags-match-logic'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}",
            )
    if "internet-service" in payload:
        value = payload["internet-service"]
        if value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid value for 'internet-service'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid value for 'internet-service-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )
    if "reputation-direction" in payload:
        value = payload["reputation-direction"]
        if value not in VALID_BODY_REPUTATION_DIRECTION:
            return (
                False,
                f"Invalid value for 'reputation-direction'='{value}'. Must be one of: {', '.join(VALID_BODY_REPUTATION_DIRECTION)}",
            )
    if "internet-service6" in payload:
        value = payload["internet-service6"]
        if value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid value for 'internet-service6'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )
    if "internet-service6-src" in payload:
        value = payload["internet-service6-src"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid value for 'internet-service6-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )
    if "reputation-direction6" in payload:
        value = payload["reputation-direction6"]
        if value not in VALID_BODY_REPUTATION_DIRECTION6:
            return (
                False,
                f"Invalid value for 'reputation-direction6'='{value}'. Must be one of: {', '.join(VALID_BODY_REPUTATION_DIRECTION6)}",
            )
    if "rtp-nat" in payload:
        value = payload["rtp-nat"]
        if value not in VALID_BODY_RTP_NAT:
            return (
                False,
                f"Invalid value for 'rtp-nat'='{value}'. Must be one of: {', '.join(VALID_BODY_RTP_NAT)}",
            )
    if "send-deny-packet" in payload:
        value = payload["send-deny-packet"]
        if value not in VALID_BODY_SEND_DENY_PACKET:
            return (
                False,
                f"Invalid value for 'send-deny-packet'='{value}'. Must be one of: {', '.join(VALID_BODY_SEND_DENY_PACKET)}",
            )
    if "firewall-session-dirty" in payload:
        value = payload["firewall-session-dirty"]
        if value not in VALID_BODY_FIREWALL_SESSION_DIRTY:
            return (
                False,
                f"Invalid value for 'firewall-session-dirty'='{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_SESSION_DIRTY)}",
            )
    if "schedule-timeout" in payload:
        value = payload["schedule-timeout"]
        if value not in VALID_BODY_SCHEDULE_TIMEOUT:
            return (
                False,
                f"Invalid value for 'schedule-timeout'='{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_TIMEOUT)}",
            )
    if "policy-expiry" in payload:
        value = payload["policy-expiry"]
        if value not in VALID_BODY_POLICY_EXPIRY:
            return (
                False,
                f"Invalid value for 'policy-expiry'='{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_EXPIRY)}",
            )
    if "tos-negate" in payload:
        value = payload["tos-negate"]
        if value not in VALID_BODY_TOS_NEGATE:
            return (
                False,
                f"Invalid value for 'tos-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_TOS_NEGATE)}",
            )
    if "anti-replay" in payload:
        value = payload["anti-replay"]
        if value not in VALID_BODY_ANTI_REPLAY:
            return (
                False,
                f"Invalid value for 'anti-replay'='{value}'. Must be one of: {', '.join(VALID_BODY_ANTI_REPLAY)}",
            )
    if "tcp-session-without-syn" in payload:
        value = payload["tcp-session-without-syn"]
        if value not in VALID_BODY_TCP_SESSION_WITHOUT_SYN:
            return (
                False,
                f"Invalid value for 'tcp-session-without-syn'='{value}'. Must be one of: {', '.join(VALID_BODY_TCP_SESSION_WITHOUT_SYN)}",
            )
    if "geoip-anycast" in payload:
        value = payload["geoip-anycast"]
        if value not in VALID_BODY_GEOIP_ANYCAST:
            return (
                False,
                f"Invalid value for 'geoip-anycast'='{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_ANYCAST)}",
            )
    if "geoip-match" in payload:
        value = payload["geoip-match"]
        if value not in VALID_BODY_GEOIP_MATCH:
            return (
                False,
                f"Invalid value for 'geoip-match'='{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_MATCH)}",
            )
    if "dynamic-shaping" in payload:
        value = payload["dynamic-shaping"]
        if value not in VALID_BODY_DYNAMIC_SHAPING:
            return (
                False,
                f"Invalid value for 'dynamic-shaping'='{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_SHAPING)}",
            )
    if "passive-wan-health-measurement" in payload:
        value = payload["passive-wan-health-measurement"]
        if value not in VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT:
            return (
                False,
                f"Invalid value for 'passive-wan-health-measurement'='{value}'. Must be one of: {', '.join(VALID_BODY_PASSIVE_WAN_HEALTH_MEASUREMENT)}",
            )
    if "app-monitor" in payload:
        value = payload["app-monitor"]
        if value not in VALID_BODY_APP_MONITOR:
            return (
                False,
                f"Invalid value for 'app-monitor'='{value}'. Must be one of: {', '.join(VALID_BODY_APP_MONITOR)}",
            )
    if "utm-status" in payload:
        value = payload["utm-status"]
        if value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid value for 'utm-status'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )
    if "inspection-mode" in payload:
        value = payload["inspection-mode"]
        if value not in VALID_BODY_INSPECTION_MODE:
            return (
                False,
                f"Invalid value for 'inspection-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_INSPECTION_MODE)}",
            )
    if "http-policy-redirect" in payload:
        value = payload["http-policy-redirect"]
        if value not in VALID_BODY_HTTP_POLICY_REDIRECT:
            return (
                False,
                f"Invalid value for 'http-policy-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_POLICY_REDIRECT)}",
            )
    if "ssh-policy-redirect" in payload:
        value = payload["ssh-policy-redirect"]
        if value not in VALID_BODY_SSH_POLICY_REDIRECT:
            return (
                False,
                f"Invalid value for 'ssh-policy-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_POLICY_REDIRECT)}",
            )
    if "ztna-policy-redirect" in payload:
        value = payload["ztna-policy-redirect"]
        if value not in VALID_BODY_ZTNA_POLICY_REDIRECT:
            return (
                False,
                f"Invalid value for 'ztna-policy-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_POLICY_REDIRECT)}",
            )
    if "profile-type" in payload:
        value = payload["profile-type"]
        if value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid value for 'profile-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )
    if "logtraffic-start" in payload:
        value = payload["logtraffic-start"]
        if value not in VALID_BODY_LOGTRAFFIC_START:
            return (
                False,
                f"Invalid value for 'logtraffic-start'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC_START)}",
            )
    if "log-http-transaction" in payload:
        value = payload["log-http-transaction"]
        if value not in VALID_BODY_LOG_HTTP_TRANSACTION:
            return (
                False,
                f"Invalid value for 'log-http-transaction'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_HTTP_TRANSACTION)}",
            )
    if "capture-packet" in payload:
        value = payload["capture-packet"]
        if value not in VALID_BODY_CAPTURE_PACKET:
            return (
                False,
                f"Invalid value for 'capture-packet'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTURE_PACKET)}",
            )
    if "auto-asic-offload" in payload:
        value = payload["auto-asic-offload"]
        if value not in VALID_BODY_AUTO_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid value for 'auto-asic-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ASIC_OFFLOAD)}",
            )
    if "wanopt" in payload:
        value = payload["wanopt"]
        if value not in VALID_BODY_WANOPT:
            return (
                False,
                f"Invalid value for 'wanopt'='{value}'. Must be one of: {', '.join(VALID_BODY_WANOPT)}",
            )
    if "wanopt-detection" in payload:
        value = payload["wanopt-detection"]
        if value not in VALID_BODY_WANOPT_DETECTION:
            return (
                False,
                f"Invalid value for 'wanopt-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_WANOPT_DETECTION)}",
            )
    if "wanopt-passive-opt" in payload:
        value = payload["wanopt-passive-opt"]
        if value not in VALID_BODY_WANOPT_PASSIVE_OPT:
            return (
                False,
                f"Invalid value for 'wanopt-passive-opt'='{value}'. Must be one of: {', '.join(VALID_BODY_WANOPT_PASSIVE_OPT)}",
            )
    if "webcache" in payload:
        value = payload["webcache"]
        if value not in VALID_BODY_WEBCACHE:
            return (
                False,
                f"Invalid value for 'webcache'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBCACHE)}",
            )
    if "webcache-https" in payload:
        value = payload["webcache-https"]
        if value not in VALID_BODY_WEBCACHE_HTTPS:
            return (
                False,
                f"Invalid value for 'webcache-https'='{value}'. Must be one of: {', '.join(VALID_BODY_WEBCACHE_HTTPS)}",
            )
    if "nat" in payload:
        value = payload["nat"]
        if value not in VALID_BODY_NAT:
            return (
                False,
                f"Invalid value for 'nat'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT)}",
            )
    if "pcp-outbound" in payload:
        value = payload["pcp-outbound"]
        if value not in VALID_BODY_PCP_OUTBOUND:
            return (
                False,
                f"Invalid value for 'pcp-outbound'='{value}'. Must be one of: {', '.join(VALID_BODY_PCP_OUTBOUND)}",
            )
    if "pcp-inbound" in payload:
        value = payload["pcp-inbound"]
        if value not in VALID_BODY_PCP_INBOUND:
            return (
                False,
                f"Invalid value for 'pcp-inbound'='{value}'. Must be one of: {', '.join(VALID_BODY_PCP_INBOUND)}",
            )
    if "permit-any-host" in payload:
        value = payload["permit-any-host"]
        if value not in VALID_BODY_PERMIT_ANY_HOST:
            return (
                False,
                f"Invalid value for 'permit-any-host'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_ANY_HOST)}",
            )
    if "permit-stun-host" in payload:
        value = payload["permit-stun-host"]
        if value not in VALID_BODY_PERMIT_STUN_HOST:
            return (
                False,
                f"Invalid value for 'permit-stun-host'='{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_STUN_HOST)}",
            )
    if "fixedport" in payload:
        value = payload["fixedport"]
        if value not in VALID_BODY_FIXEDPORT:
            return (
                False,
                f"Invalid value for 'fixedport'='{value}'. Must be one of: {', '.join(VALID_BODY_FIXEDPORT)}",
            )
    if "port-preserve" in payload:
        value = payload["port-preserve"]
        if value not in VALID_BODY_PORT_PRESERVE:
            return (
                False,
                f"Invalid value for 'port-preserve'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_PRESERVE)}",
            )
    if "port-random" in payload:
        value = payload["port-random"]
        if value not in VALID_BODY_PORT_RANDOM:
            return (
                False,
                f"Invalid value for 'port-random'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_RANDOM)}",
            )
    if "ippool" in payload:
        value = payload["ippool"]
        if value not in VALID_BODY_IPPOOL:
            return (
                False,
                f"Invalid value for 'ippool'='{value}'. Must be one of: {', '.join(VALID_BODY_IPPOOL)}",
            )
    if "inbound" in payload:
        value = payload["inbound"]
        if value not in VALID_BODY_INBOUND:
            return (
                False,
                f"Invalid value for 'inbound'='{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND)}",
            )
    if "outbound" in payload:
        value = payload["outbound"]
        if value not in VALID_BODY_OUTBOUND:
            return (
                False,
                f"Invalid value for 'outbound'='{value}'. Must be one of: {', '.join(VALID_BODY_OUTBOUND)}",
            )
    if "natinbound" in payload:
        value = payload["natinbound"]
        if value not in VALID_BODY_NATINBOUND:
            return (
                False,
                f"Invalid value for 'natinbound'='{value}'. Must be one of: {', '.join(VALID_BODY_NATINBOUND)}",
            )
    if "natoutbound" in payload:
        value = payload["natoutbound"]
        if value not in VALID_BODY_NATOUTBOUND:
            return (
                False,
                f"Invalid value for 'natoutbound'='{value}'. Must be one of: {', '.join(VALID_BODY_NATOUTBOUND)}",
            )
    if "fec" in payload:
        value = payload["fec"]
        if value not in VALID_BODY_FEC:
            return (
                False,
                f"Invalid value for 'fec'='{value}'. Must be one of: {', '.join(VALID_BODY_FEC)}",
            )
    if "wccp" in payload:
        value = payload["wccp"]
        if value not in VALID_BODY_WCCP:
            return (
                False,
                f"Invalid value for 'wccp'='{value}'. Must be one of: {', '.join(VALID_BODY_WCCP)}",
            )
    if "ntlm" in payload:
        value = payload["ntlm"]
        if value not in VALID_BODY_NTLM:
            return (
                False,
                f"Invalid value for 'ntlm'='{value}'. Must be one of: {', '.join(VALID_BODY_NTLM)}",
            )
    if "ntlm-guest" in payload:
        value = payload["ntlm-guest"]
        if value not in VALID_BODY_NTLM_GUEST:
            return (
                False,
                f"Invalid value for 'ntlm-guest'='{value}'. Must be one of: {', '.join(VALID_BODY_NTLM_GUEST)}",
            )
    if "auth-path" in payload:
        value = payload["auth-path"]
        if value not in VALID_BODY_AUTH_PATH:
            return (
                False,
                f"Invalid value for 'auth-path'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PATH)}",
            )
    if "disclaimer" in payload:
        value = payload["disclaimer"]
        if value not in VALID_BODY_DISCLAIMER:
            return (
                False,
                f"Invalid value for 'disclaimer'='{value}'. Must be one of: {', '.join(VALID_BODY_DISCLAIMER)}",
            )
    if "email-collect" in payload:
        value = payload["email-collect"]
        if value not in VALID_BODY_EMAIL_COLLECT:
            return (
                False,
                f"Invalid value for 'email-collect'='{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_COLLECT)}",
            )
    if "match-vip" in payload:
        value = payload["match-vip"]
        if value not in VALID_BODY_MATCH_VIP:
            return (
                False,
                f"Invalid value for 'match-vip'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_VIP)}",
            )
    if "match-vip-only" in payload:
        value = payload["match-vip-only"]
        if value not in VALID_BODY_MATCH_VIP_ONLY:
            return (
                False,
                f"Invalid value for 'match-vip-only'='{value}'. Must be one of: {', '.join(VALID_BODY_MATCH_VIP_ONLY)}",
            )
    if "diffserv-copy" in payload:
        value = payload["diffserv-copy"]
        if value not in VALID_BODY_DIFFSERV_COPY:
            return (
                False,
                f"Invalid value for 'diffserv-copy'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_COPY)}",
            )
    if "diffserv-forward" in payload:
        value = payload["diffserv-forward"]
        if value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid value for 'diffserv-forward'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )
    if "diffserv-reverse" in payload:
        value = payload["diffserv-reverse"]
        if value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid value for 'diffserv-reverse'='{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )
    if "block-notification" in payload:
        value = payload["block-notification"]
        if value not in VALID_BODY_BLOCK_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'block-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_NOTIFICATION)}",
            )
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'srcaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )
    if "srcaddr6-negate" in payload:
        value = payload["srcaddr6-negate"]
        if value not in VALID_BODY_SRCADDR6_NEGATE:
            return (
                False,
                f"Invalid value for 'srcaddr6-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR6_NEGATE)}",
            )
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'dstaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )
    if "dstaddr6-negate" in payload:
        value = payload["dstaddr6-negate"]
        if value not in VALID_BODY_DSTADDR6_NEGATE:
            return (
                False,
                f"Invalid value for 'dstaddr6-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR6_NEGATE)}",
            )
    if "ztna-ems-tag-negate" in payload:
        value = payload["ztna-ems-tag-negate"]
        if value not in VALID_BODY_ZTNA_EMS_TAG_NEGATE:
            return (
                False,
                f"Invalid value for 'ztna-ems-tag-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_EMS_TAG_NEGATE)}",
            )
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'service-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )
    if "internet-service-negate" in payload:
        value = payload["internet-service-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )
    if "internet-service-src-negate" in payload:
        value = payload["internet-service-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service-src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )
    if "internet-service6-negate" in payload:
        value = payload["internet-service6-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service6-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )
    if "internet-service6-src-negate" in payload:
        value = payload["internet-service6-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service6-src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )
    if "timeout-send-rst" in payload:
        value = payload["timeout-send-rst"]
        if value not in VALID_BODY_TIMEOUT_SEND_RST:
            return (
                False,
                f"Invalid value for 'timeout-send-rst'='{value}'. Must be one of: {', '.join(VALID_BODY_TIMEOUT_SEND_RST)}",
            )
    if "captive-portal-exempt" in payload:
        value = payload["captive-portal-exempt"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_EXEMPT:
            return (
                False,
                f"Invalid value for 'captive-portal-exempt'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_EXEMPT)}",
            )
    if "dsri" in payload:
        value = payload["dsri"]
        if value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid value for 'dsri'='{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )
    if "radius-mac-auth-bypass" in payload:
        value = payload["radius-mac-auth-bypass"]
        if value not in VALID_BODY_RADIUS_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid value for 'radius-mac-auth-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_AUTH_BYPASS)}",
            )
    if "radius-ip-auth-bypass" in payload:
        value = payload["radius-ip-auth-bypass"]
        if value not in VALID_BODY_RADIUS_IP_AUTH_BYPASS:
            return (
                False,
                f"Invalid value for 'radius-ip-auth-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_IP_AUTH_BYPASS)}",
            )
    if "delay-tcp-npu-session" in payload:
        value = payload["delay-tcp-npu-session"]
        if value not in VALID_BODY_DELAY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid value for 'delay-tcp-npu-session'='{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_TCP_NPU_SESSION)}",
            )
    if "sgt-check" in payload:
        value = payload["sgt-check"]
        if value not in VALID_BODY_SGT_CHECK:
            return (
                False,
                f"Invalid value for 'sgt-check'='{value}'. Must be one of: {', '.join(VALID_BODY_SGT_CHECK)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "firewall/policy",
    "category": "cmdb",
    "api_path": "firewall/policy",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure IPv4/IPv6 policies.",
    "total_fields": 184,
    "required_fields_count": 3,
    "fields_with_defaults_count": 139,
}


def get_schema_info() -> dict[str, Any]:
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()
