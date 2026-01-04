"""
Validation helpers for system/settings endpoint.

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
    "manageip",  # Transparent mode IPv4 management IP address and netmask.
    "device",  # Interface to use for management access for NAT mode.
    "dhcp-proxy-interface",  # Specify outgoing interface to reach server.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "vdom-type": "traffic",
    "lan-extension-controller-addr": "",
    "opmode": "nat",
    "ngfw-mode": "profile-based",
    "http-external-dest": "fortiweb",
    "firewall-session-dirty": "check-all",
    "manageip": "",
    "gateway": "0.0.0.0",
    "ip": "0.0.0.0 0.0.0.0",
    "manageip6": "::/0",
    "gateway6": "::",
    "ip6": "::/0",
    "device": "",
    "bfd": "disable",
    "bfd-desired-min-tx": 250,
    "bfd-required-min-rx": 250,
    "bfd-detect-mult": 3,
    "bfd-dont-enforce-src-port": "disable",
    "utf8-spam-tagging": "enable",
    "wccp-cache-engine": "disable",
    "vpn-stats-log": "ipsec pptp l2tp ssl",
    "vpn-stats-period": 600,
    "v4-ecmp-mode": "source-ip-based",
    "mac-ttl": 300,
    "fw-session-hairpin": "disable",
    "prp-trailer-action": "disable",
    "snat-hairpin-traffic": "enable",
    "dhcp-proxy": "disable",
    "dhcp-proxy-interface-select-method": "auto",
    "dhcp-proxy-interface": "",
    "dhcp-proxy-vrf-select": 0,
    "dhcp-server-ip": "",
    "dhcp6-server-ip": "",
    "central-nat": "disable",
    "lldp-reception": "global",
    "lldp-transmission": "global",
    "link-down-access": "enable",
    "nat46-generate-ipv6-fragment-header": "disable",
    "nat46-force-ipv4-packet-forwarding": "disable",
    "nat64-force-ipv6-packet-forwarding": "enable",
    "detect-unknown-esp": "enable",
    "intree-ses-best-route": "disable",
    "auxiliary-session": "disable",
    "asymroute": "disable",
    "asymroute-icmp": "disable",
    "tcp-session-without-syn": "disable",
    "ses-denied-traffic": "disable",
    "ses-denied-multicast-traffic": "disable",
    "strict-src-check": "disable",
    "allow-linkdown-path": "disable",
    "asymroute6": "disable",
    "asymroute6-icmp": "disable",
    "sctp-session-without-init": "disable",
    "sip-expectation": "disable",
    "sip-nat-trace": "enable",
    "h323-direct-model": "disable",
    "status": "enable",
    "sip-tcp-port": 5060,
    "sip-udp-port": 5060,
    "sip-ssl-port": 5061,
    "sccp-port": 2000,
    "multicast-forward": "enable",
    "multicast-ttl-notchange": "disable",
    "multicast-skip-policy": "disable",
    "allow-subnet-overlap": "disable",
    "deny-tcp-with-icmp": "disable",
    "ecmp-max-paths": 255,
    "discovered-device-timeout": 28,
    "email-portal-check-dns": "enable",
    "default-voip-alg-mode": "proxy-based",
    "gui-icap": "disable",
    "gui-implicit-policy": "enable",
    "gui-dns-database": "disable",
    "gui-load-balance": "disable",
    "gui-multicast-policy": "disable",
    "gui-dos-policy": "enable",
    "gui-object-colors": "enable",
    "gui-route-tag-address-creation": "disable",
    "gui-voip-profile": "disable",
    "gui-ap-profile": "enable",
    "gui-security-profile-group": "disable",
    "gui-local-in-policy": "disable",
    "gui-wanopt-cache": "disable",
    "gui-explicit-proxy": "disable",
    "gui-dynamic-routing": "enable",
    "gui-sslvpn-personal-bookmarks": "disable",
    "gui-sslvpn-realms": "disable",
    "gui-policy-based-ipsec": "disable",
    "gui-threat-weight": "enable",
    "gui-spamfilter": "disable",
    "gui-file-filter": "enable",
    "gui-application-control": "enable",
    "gui-ips": "enable",
    "gui-dhcp-advanced": "enable",
    "gui-vpn": "enable",
    "gui-sslvpn": "disable",
    "gui-wireless-controller": "enable",
    "gui-advanced-wireless-features": "disable",
    "gui-switch-controller": "enable",
    "gui-fortiap-split-tunneling": "disable",
    "gui-webfilter-advanced": "disable",
    "gui-traffic-shaping": "enable",
    "gui-wan-load-balancing": "enable",
    "gui-antivirus": "enable",
    "gui-webfilter": "enable",
    "gui-videofilter": "enable",
    "gui-dnsfilter": "enable",
    "gui-waf-profile": "disable",
    "gui-dlp-profile": "disable",
    "gui-dlp-advanced": "disable",
    "gui-virtual-patch-profile": "disable",
    "gui-casb": "disable",
    "gui-fortiextender-controller": "disable",
    "gui-advanced-policy": "disable",
    "gui-allow-unnamed-policy": "disable",
    "gui-email-collection": "disable",
    "gui-multiple-interface-policy": "disable",
    "gui-policy-disclaimer": "disable",
    "gui-ztna": "disable",
    "gui-ot": "disable",
    "gui-dynamic-device-os-id": "disable",
    "gui-gtp": "enable",
    "location-id": "0.0.0.0",
    "ike-session-resume": "disable",
    "ike-quick-crash-detect": "disable",
    "ike-dn-format": "with-space",
    "ike-port": 500,
    "ike-tcp-port": 443,
    "ike-policy-route": "disable",
    "ike-detailed-event-logs": "disable",
    "block-land-attack": "disable",
    "default-app-port-as-service": "enable",
    "fqdn-session-check": "disable",
    "ext-resource-session-check": "disable",
    "dyn-addr-session-check": "disable",
    "default-policy-expiry-days": 30,
    "gui-enforce-change-summary": "require",
    "internet-service-database-cache": "disable",
    "internet-service-app-ctrl-size": 32768,
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
    "comments": "var-string",  # VDOM comments.
    "vdom-type": "option",  # Vdom type (traffic, lan-extension or admin).
    "lan-extension-controller-addr": "string",  # Controller IP address or FQDN to connect.
    "opmode": "option",  # Firewall operation mode (NAT or Transparent).
    "ngfw-mode": "option",  # Next Generation Firewall (NGFW) mode.
    "http-external-dest": "option",  # Offload HTTP traffic to FortiWeb or FortiCache.
    "firewall-session-dirty": "option",  # Select how to manage sessions affected by firewall policy co
    "manageip": "user",  # Transparent mode IPv4 management IP address and netmask.
    "gateway": "ipv4-address",  # Transparent mode IPv4 default gateway IP address.
    "ip": "ipv4-classnet-host",  # IP address and netmask.
    "manageip6": "ipv6-prefix",  # Transparent mode IPv6 management IP address and netmask.
    "gateway6": "ipv6-address",  # Transparent mode IPv6 default gateway IP address.
    "ip6": "ipv6-prefix",  # IPv6 address prefix for NAT mode.
    "device": "string",  # Interface to use for management access for NAT mode.
    "bfd": "option",  # Enable/disable Bi-directional Forwarding Detection (BFD) on 
    "bfd-desired-min-tx": "integer",  # BFD desired minimal transmit interval (1 - 100000 ms, defaul
    "bfd-required-min-rx": "integer",  # BFD required minimal receive interval (1 - 100000 ms, defaul
    "bfd-detect-mult": "integer",  # BFD detection multiplier (1 - 50, default = 3).
    "bfd-dont-enforce-src-port": "option",  # Enable to not enforce verifying the source port of BFD Packe
    "utf8-spam-tagging": "option",  # Enable/disable converting antispam tags to UTF-8 for better 
    "wccp-cache-engine": "option",  # Enable/disable WCCP cache engine.
    "vpn-stats-log": "option",  # Enable/disable periodic VPN log statistics for one or more t
    "vpn-stats-period": "integer",  # Period to send VPN log statistics (0 or 60 - 86400 sec).
    "v4-ecmp-mode": "option",  # IPv4 Equal-cost multi-path (ECMP) routing and load balancing
    "mac-ttl": "integer",  # Duration of MAC addresses in Transparent mode (300 - 8640000
    "fw-session-hairpin": "option",  # Enable/disable checking for a matching policy each time hair
    "prp-trailer-action": "option",  # Enable/disable action to take on PRP trailer.
    "snat-hairpin-traffic": "option",  # Enable/disable source NAT (SNAT) for VIP hairpin traffic.
    "dhcp-proxy": "option",  # Enable/disable the DHCP Proxy.
    "dhcp-proxy-interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "dhcp-proxy-interface": "string",  # Specify outgoing interface to reach server.
    "dhcp-proxy-vrf-select": "integer",  # VRF ID used for connection to server.
    "dhcp-server-ip": "user",  # DHCP Server IPv4 address.
    "dhcp6-server-ip": "user",  # DHCPv6 server IPv6 address.
    "central-nat": "option",  # Enable/disable central NAT.
    "gui-default-policy-columns": "string",  # Default columns to display for policy lists on GUI.
    "lldp-reception": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) receptio
    "lldp-transmission": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) transmis
    "link-down-access": "option",  # Enable/disable link down access traffic.
    "nat46-generate-ipv6-fragment-header": "option",  # Enable/disable NAT46 IPv6 fragment header generation.
    "nat46-force-ipv4-packet-forwarding": "option",  # Enable/disable mandatory IPv4 packet forwarding in NAT46.
    "nat64-force-ipv6-packet-forwarding": "option",  # Enable/disable mandatory IPv6 packet forwarding in NAT64.
    "detect-unknown-esp": "option",  # Enable/disable detection of unknown ESP packets (default = e
    "intree-ses-best-route": "option",  # Force the intree session to always use the best route.
    "auxiliary-session": "option",  # Enable/disable auxiliary session.
    "asymroute": "option",  # Enable/disable IPv4 asymmetric routing.
    "asymroute-icmp": "option",  # Enable/disable ICMP asymmetric routing.
    "tcp-session-without-syn": "option",  # Enable/disable allowing TCP session without SYN flags.
    "ses-denied-traffic": "option",  # Enable/disable including denied session in the session table
    "ses-denied-multicast-traffic": "option",  # Enable/disable including denied multicast session in the ses
    "strict-src-check": "option",  # Enable/disable strict source verification.
    "allow-linkdown-path": "option",  # Enable/disable link down path.
    "asymroute6": "option",  # Enable/disable asymmetric IPv6 routing.
    "asymroute6-icmp": "option",  # Enable/disable asymmetric ICMPv6 routing.
    "sctp-session-without-init": "option",  # Enable/disable SCTP session creation without SCTP INIT.
    "sip-expectation": "option",  # Enable/disable the SIP kernel session helper to create an ex
    "sip-nat-trace": "option",  # Enable/disable recording the original SIP source IP address 
    "h323-direct-model": "option",  # Enable/disable H323 direct model.
    "status": "option",  # Enable/disable this VDOM.
    "sip-tcp-port": "integer",  # TCP port the SIP proxy monitors for SIP traffic (0 - 65535, 
    "sip-udp-port": "integer",  # UDP port the SIP proxy monitors for SIP traffic (0 - 65535, 
    "sip-ssl-port": "integer",  # TCP port the SIP proxy monitors for SIP SSL/TLS traffic (0 -
    "sccp-port": "integer",  # TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535
    "multicast-forward": "option",  # Enable/disable multicast forwarding.
    "multicast-ttl-notchange": "option",  # Enable/disable preventing the FortiGate from changing the TT
    "multicast-skip-policy": "option",  # Enable/disable allowing multicast traffic through the FortiG
    "allow-subnet-overlap": "option",  # Enable/disable allowing interface subnets to use overlapping
    "deny-tcp-with-icmp": "option",  # Enable/disable denying TCP by sending an ICMP communication 
    "ecmp-max-paths": "integer",  # Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Se
    "discovered-device-timeout": "integer",  # Timeout for discovered devices (1 - 365 days, default = 28).
    "email-portal-check-dns": "option",  # Enable/disable using DNS to validate email addresses collect
    "default-voip-alg-mode": "option",  # Configure how the FortiGate handles VoIP traffic when a poli
    "gui-icap": "option",  # Enable/disable ICAP on the GUI.
    "gui-implicit-policy": "option",  # Enable/disable implicit firewall policies on the GUI.
    "gui-dns-database": "option",  # Enable/disable DNS database settings on the GUI.
    "gui-load-balance": "option",  # Enable/disable server load balancing on the GUI.
    "gui-multicast-policy": "option",  # Enable/disable multicast firewall policies on the GUI.
    "gui-dos-policy": "option",  # Enable/disable DoS policies on the GUI.
    "gui-object-colors": "option",  # Enable/disable object colors on the GUI.
    "gui-route-tag-address-creation": "option",  # Enable/disable route-tag addresses on the GUI.
    "gui-voip-profile": "option",  # Enable/disable VoIP profiles on the GUI.
    "gui-ap-profile": "option",  # Enable/disable FortiAP profiles on the GUI.
    "gui-security-profile-group": "option",  # Enable/disable Security Profile Groups on the GUI.
    "gui-local-in-policy": "option",  # Enable/disable Local-In policies on the GUI.
    "gui-wanopt-cache": "option",  # Enable/disable WAN Optimization and Web Caching on the GUI.
    "gui-explicit-proxy": "option",  # Enable/disable the explicit proxy on the GUI.
    "gui-dynamic-routing": "option",  # Enable/disable dynamic routing on the GUI.
    "gui-sslvpn-personal-bookmarks": "option",  # Enable/disable SSL-VPN personal bookmark management on the G
    "gui-sslvpn-realms": "option",  # Enable/disable SSL-VPN realms on the GUI.
    "gui-policy-based-ipsec": "option",  # Enable/disable policy-based IPsec VPN on the GUI.
    "gui-threat-weight": "option",  # Enable/disable threat weight on the GUI.
    "gui-spamfilter": "option",  # Enable/disable Antispam on the GUI.
    "gui-file-filter": "option",  # Enable/disable File-filter on the GUI.
    "gui-application-control": "option",  # Enable/disable application control on the GUI.
    "gui-ips": "option",  # Enable/disable IPS on the GUI.
    "gui-dhcp-advanced": "option",  # Enable/disable advanced DHCP options on the GUI.
    "gui-vpn": "option",  # Enable/disable IPsec VPN settings pages on the GUI.
    "gui-sslvpn": "option",  # Enable/disable SSL-VPN settings pages on the GUI.
    "gui-wireless-controller": "option",  # Enable/disable the wireless controller on the GUI.
    "gui-advanced-wireless-features": "option",  # Enable/disable advanced wireless features in GUI.
    "gui-switch-controller": "option",  # Enable/disable the switch controller on the GUI.
    "gui-fortiap-split-tunneling": "option",  # Enable/disable FortiAP split tunneling on the GUI.
    "gui-webfilter-advanced": "option",  # Enable/disable advanced web filtering on the GUI.
    "gui-traffic-shaping": "option",  # Enable/disable traffic shaping on the GUI.
    "gui-wan-load-balancing": "option",  # Enable/disable SD-WAN on the GUI.
    "gui-antivirus": "option",  # Enable/disable AntiVirus on the GUI.
    "gui-webfilter": "option",  # Enable/disable Web filtering on the GUI.
    "gui-videofilter": "option",  # Enable/disable Video filtering on the GUI.
    "gui-dnsfilter": "option",  # Enable/disable DNS Filtering on the GUI.
    "gui-waf-profile": "option",  # Enable/disable Web Application Firewall on the GUI.
    "gui-dlp-profile": "option",  # Enable/disable Data Loss Prevention on the GUI.
    "gui-dlp-advanced": "option",  # Enable/disable Show advanced DLP expressions on the GUI.
    "gui-virtual-patch-profile": "option",  # Enable/disable Virtual Patching on the GUI.
    "gui-casb": "option",  # Enable/disable Inline-CASB on the GUI.
    "gui-fortiextender-controller": "option",  # Enable/disable FortiExtender on the GUI.
    "gui-advanced-policy": "option",  # Enable/disable advanced policy configuration on the GUI.
    "gui-allow-unnamed-policy": "option",  # Enable/disable the requirement for policy naming on the GUI.
    "gui-email-collection": "option",  # Enable/disable email collection on the GUI.
    "gui-multiple-interface-policy": "option",  # Enable/disable adding multiple interfaces to a policy on the
    "gui-policy-disclaimer": "option",  # Enable/disable policy disclaimer on the GUI.
    "gui-ztna": "option",  # Enable/disable Zero Trust Network Access features on the GUI
    "gui-ot": "option",  # Enable/disable Operational technology features on the GUI.
    "gui-dynamic-device-os-id": "option",  # Enable/disable Create dynamic addresses to manage known devi
    "gui-gtp": "option",  # Enable/disable Manage general radio packet service (GPRS) pr
    "location-id": "ipv4-address",  # Local location ID in the form of an IPv4 address.
    "ike-session-resume": "option",  # Enable/disable IKEv2 session resumption (RFC 5723).
    "ike-quick-crash-detect": "option",  # Enable/disable IKE quick crash detection (RFC 6290).
    "ike-dn-format": "option",  # Configure IKE ASN.1 Distinguished Name format conventions.
    "ike-port": "integer",  # UDP port for IKE/IPsec traffic (default 500).
    "ike-tcp-port": "integer",  # TCP port for IKE/IPsec traffic (default 443).
    "ike-policy-route": "option",  # Enable/disable IKE Policy Based Routing (PBR).
    "ike-detailed-event-logs": "option",  # Enable/disable detail log for IKE events.
    "block-land-attack": "option",  # Enable/disable blocking of land attacks.
    "default-app-port-as-service": "option",  # Enable/disable policy service enforcement based on applicati
    "fqdn-session-check": "option",  # Enable/disable dirty session check caused by FQDN updates.
    "ext-resource-session-check": "option",  # Enable/disable dirty session check caused by external resour
    "dyn-addr-session-check": "option",  # Enable/disable dirty session check caused by dynamic address
    "default-policy-expiry-days": "integer",  # Default policy expiry in days (0 - 365 days, default = 30).
    "gui-enforce-change-summary": "option",  # Enforce change summaries for select tables in the GUI.
    "internet-service-database-cache": "option",  # Enable/disable Internet Service database caching.
    "internet-service-app-ctrl-size": "integer",  # Maximum number of tuple entries (protocol, port, IP address,
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "comments": "VDOM comments.",
    "vdom-type": "Vdom type (traffic, lan-extension or admin).",
    "lan-extension-controller-addr": "Controller IP address or FQDN to connect.",
    "opmode": "Firewall operation mode (NAT or Transparent).",
    "ngfw-mode": "Next Generation Firewall (NGFW) mode.",
    "http-external-dest": "Offload HTTP traffic to FortiWeb or FortiCache.",
    "firewall-session-dirty": "Select how to manage sessions affected by firewall policy configuration changes.",
    "manageip": "Transparent mode IPv4 management IP address and netmask.",
    "gateway": "Transparent mode IPv4 default gateway IP address.",
    "ip": "IP address and netmask.",
    "manageip6": "Transparent mode IPv6 management IP address and netmask.",
    "gateway6": "Transparent mode IPv6 default gateway IP address.",
    "ip6": "IPv6 address prefix for NAT mode.",
    "device": "Interface to use for management access for NAT mode.",
    "bfd": "Enable/disable Bi-directional Forwarding Detection (BFD) on all interfaces.",
    "bfd-desired-min-tx": "BFD desired minimal transmit interval (1 - 100000 ms, default = 250).",
    "bfd-required-min-rx": "BFD required minimal receive interval (1 - 100000 ms, default = 250).",
    "bfd-detect-mult": "BFD detection multiplier (1 - 50, default = 3).",
    "bfd-dont-enforce-src-port": "Enable to not enforce verifying the source port of BFD Packets.",
    "utf8-spam-tagging": "Enable/disable converting antispam tags to UTF-8 for better non-ASCII character support.",
    "wccp-cache-engine": "Enable/disable WCCP cache engine.",
    "vpn-stats-log": "Enable/disable periodic VPN log statistics for one or more types of VPN. Separate names with a space.",
    "vpn-stats-period": "Period to send VPN log statistics (0 or 60 - 86400 sec).",
    "v4-ecmp-mode": "IPv4 Equal-cost multi-path (ECMP) routing and load balancing mode.",
    "mac-ttl": "Duration of MAC addresses in Transparent mode (300 - 8640000 sec, default = 300).",
    "fw-session-hairpin": "Enable/disable checking for a matching policy each time hairpin traffic goes through the FortiGate.",
    "prp-trailer-action": "Enable/disable action to take on PRP trailer.",
    "snat-hairpin-traffic": "Enable/disable source NAT (SNAT) for VIP hairpin traffic.",
    "dhcp-proxy": "Enable/disable the DHCP Proxy.",
    "dhcp-proxy-interface-select-method": "Specify how to select outgoing interface to reach server.",
    "dhcp-proxy-interface": "Specify outgoing interface to reach server.",
    "dhcp-proxy-vrf-select": "VRF ID used for connection to server.",
    "dhcp-server-ip": "DHCP Server IPv4 address.",
    "dhcp6-server-ip": "DHCPv6 server IPv6 address.",
    "central-nat": "Enable/disable central NAT.",
    "gui-default-policy-columns": "Default columns to display for policy lists on GUI.",
    "lldp-reception": "Enable/disable Link Layer Discovery Protocol (LLDP) reception for this VDOM or apply global settings to this VDOM.",
    "lldp-transmission": "Enable/disable Link Layer Discovery Protocol (LLDP) transmission for this VDOM or apply global settings to this VDOM.",
    "link-down-access": "Enable/disable link down access traffic.",
    "nat46-generate-ipv6-fragment-header": "Enable/disable NAT46 IPv6 fragment header generation.",
    "nat46-force-ipv4-packet-forwarding": "Enable/disable mandatory IPv4 packet forwarding in NAT46.",
    "nat64-force-ipv6-packet-forwarding": "Enable/disable mandatory IPv6 packet forwarding in NAT64.",
    "detect-unknown-esp": "Enable/disable detection of unknown ESP packets (default = enable).",
    "intree-ses-best-route": "Force the intree session to always use the best route.",
    "auxiliary-session": "Enable/disable auxiliary session.",
    "asymroute": "Enable/disable IPv4 asymmetric routing.",
    "asymroute-icmp": "Enable/disable ICMP asymmetric routing.",
    "tcp-session-without-syn": "Enable/disable allowing TCP session without SYN flags.",
    "ses-denied-traffic": "Enable/disable including denied session in the session table.",
    "ses-denied-multicast-traffic": "Enable/disable including denied multicast session in the session table.",
    "strict-src-check": "Enable/disable strict source verification.",
    "allow-linkdown-path": "Enable/disable link down path.",
    "asymroute6": "Enable/disable asymmetric IPv6 routing.",
    "asymroute6-icmp": "Enable/disable asymmetric ICMPv6 routing.",
    "sctp-session-without-init": "Enable/disable SCTP session creation without SCTP INIT.",
    "sip-expectation": "Enable/disable the SIP kernel session helper to create an expectation for port 5060.",
    "sip-nat-trace": "Enable/disable recording the original SIP source IP address when NAT is used.",
    "h323-direct-model": "Enable/disable H323 direct model.",
    "status": "Enable/disable this VDOM.",
    "sip-tcp-port": "TCP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).",
    "sip-udp-port": "UDP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).",
    "sip-ssl-port": "TCP port the SIP proxy monitors for SIP SSL/TLS traffic (0 - 65535, default = 5061).",
    "sccp-port": "TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535, default = 2000).",
    "multicast-forward": "Enable/disable multicast forwarding.",
    "multicast-ttl-notchange": "Enable/disable preventing the FortiGate from changing the TTL for forwarded multicast packets.",
    "multicast-skip-policy": "Enable/disable allowing multicast traffic through the FortiGate without a policy check.",
    "allow-subnet-overlap": "Enable/disable allowing interface subnets to use overlapping IP addresses.",
    "deny-tcp-with-icmp": "Enable/disable denying TCP by sending an ICMP communication prohibited packet.",
    "ecmp-max-paths": "Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to disable ECMP routing (1 - 255, default = 255).",
    "discovered-device-timeout": "Timeout for discovered devices (1 - 365 days, default = 28).",
    "email-portal-check-dns": "Enable/disable using DNS to validate email addresses collected by a captive portal.",
    "default-voip-alg-mode": "Configure how the FortiGate handles VoIP traffic when a policy that accepts the traffic doesn't include a VoIP profile.",
    "gui-icap": "Enable/disable ICAP on the GUI.",
    "gui-implicit-policy": "Enable/disable implicit firewall policies on the GUI.",
    "gui-dns-database": "Enable/disable DNS database settings on the GUI.",
    "gui-load-balance": "Enable/disable server load balancing on the GUI.",
    "gui-multicast-policy": "Enable/disable multicast firewall policies on the GUI.",
    "gui-dos-policy": "Enable/disable DoS policies on the GUI.",
    "gui-object-colors": "Enable/disable object colors on the GUI.",
    "gui-route-tag-address-creation": "Enable/disable route-tag addresses on the GUI.",
    "gui-voip-profile": "Enable/disable VoIP profiles on the GUI.",
    "gui-ap-profile": "Enable/disable FortiAP profiles on the GUI.",
    "gui-security-profile-group": "Enable/disable Security Profile Groups on the GUI.",
    "gui-local-in-policy": "Enable/disable Local-In policies on the GUI.",
    "gui-wanopt-cache": "Enable/disable WAN Optimization and Web Caching on the GUI.",
    "gui-explicit-proxy": "Enable/disable the explicit proxy on the GUI.",
    "gui-dynamic-routing": "Enable/disable dynamic routing on the GUI.",
    "gui-sslvpn-personal-bookmarks": "Enable/disable SSL-VPN personal bookmark management on the GUI.",
    "gui-sslvpn-realms": "Enable/disable SSL-VPN realms on the GUI.",
    "gui-policy-based-ipsec": "Enable/disable policy-based IPsec VPN on the GUI.",
    "gui-threat-weight": "Enable/disable threat weight on the GUI.",
    "gui-spamfilter": "Enable/disable Antispam on the GUI.",
    "gui-file-filter": "Enable/disable File-filter on the GUI.",
    "gui-application-control": "Enable/disable application control on the GUI.",
    "gui-ips": "Enable/disable IPS on the GUI.",
    "gui-dhcp-advanced": "Enable/disable advanced DHCP options on the GUI.",
    "gui-vpn": "Enable/disable IPsec VPN settings pages on the GUI.",
    "gui-sslvpn": "Enable/disable SSL-VPN settings pages on the GUI.",
    "gui-wireless-controller": "Enable/disable the wireless controller on the GUI.",
    "gui-advanced-wireless-features": "Enable/disable advanced wireless features in GUI.",
    "gui-switch-controller": "Enable/disable the switch controller on the GUI.",
    "gui-fortiap-split-tunneling": "Enable/disable FortiAP split tunneling on the GUI.",
    "gui-webfilter-advanced": "Enable/disable advanced web filtering on the GUI.",
    "gui-traffic-shaping": "Enable/disable traffic shaping on the GUI.",
    "gui-wan-load-balancing": "Enable/disable SD-WAN on the GUI.",
    "gui-antivirus": "Enable/disable AntiVirus on the GUI.",
    "gui-webfilter": "Enable/disable Web filtering on the GUI.",
    "gui-videofilter": "Enable/disable Video filtering on the GUI.",
    "gui-dnsfilter": "Enable/disable DNS Filtering on the GUI.",
    "gui-waf-profile": "Enable/disable Web Application Firewall on the GUI.",
    "gui-dlp-profile": "Enable/disable Data Loss Prevention on the GUI.",
    "gui-dlp-advanced": "Enable/disable Show advanced DLP expressions on the GUI.",
    "gui-virtual-patch-profile": "Enable/disable Virtual Patching on the GUI.",
    "gui-casb": "Enable/disable Inline-CASB on the GUI.",
    "gui-fortiextender-controller": "Enable/disable FortiExtender on the GUI.",
    "gui-advanced-policy": "Enable/disable advanced policy configuration on the GUI.",
    "gui-allow-unnamed-policy": "Enable/disable the requirement for policy naming on the GUI.",
    "gui-email-collection": "Enable/disable email collection on the GUI.",
    "gui-multiple-interface-policy": "Enable/disable adding multiple interfaces to a policy on the GUI.",
    "gui-policy-disclaimer": "Enable/disable policy disclaimer on the GUI.",
    "gui-ztna": "Enable/disable Zero Trust Network Access features on the GUI.",
    "gui-ot": "Enable/disable Operational technology features on the GUI.",
    "gui-dynamic-device-os-id": "Enable/disable Create dynamic addresses to manage known devices.",
    "gui-gtp": "Enable/disable Manage general radio packet service (GPRS) protocols on the GUI.",
    "location-id": "Local location ID in the form of an IPv4 address.",
    "ike-session-resume": "Enable/disable IKEv2 session resumption (RFC 5723).",
    "ike-quick-crash-detect": "Enable/disable IKE quick crash detection (RFC 6290).",
    "ike-dn-format": "Configure IKE ASN.1 Distinguished Name format conventions.",
    "ike-port": "UDP port for IKE/IPsec traffic (default 500).",
    "ike-tcp-port": "TCP port for IKE/IPsec traffic (default 443).",
    "ike-policy-route": "Enable/disable IKE Policy Based Routing (PBR).",
    "ike-detailed-event-logs": "Enable/disable detail log for IKE events.",
    "block-land-attack": "Enable/disable blocking of land attacks.",
    "default-app-port-as-service": "Enable/disable policy service enforcement based on application default ports.",
    "fqdn-session-check": "Enable/disable dirty session check caused by FQDN updates.",
    "ext-resource-session-check": "Enable/disable dirty session check caused by external resource updates.",
    "dyn-addr-session-check": "Enable/disable dirty session check caused by dynamic address updates.",
    "default-policy-expiry-days": "Default policy expiry in days (0 - 365 days, default = 30).",
    "gui-enforce-change-summary": "Enforce change summaries for select tables in the GUI.",
    "internet-service-database-cache": "Enable/disable Internet Service database caching.",
    "internet-service-app-ctrl-size": "Maximum number of tuple entries (protocol, port, IP address, application ID) stored by the FortiGate unit (0 - 4294967295, default = 32768). A smaller value limits the FortiGate unit from learning about internet applications.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "lan-extension-controller-addr": {"type": "string", "max_length": 255},
    "device": {"type": "string", "max_length": 35},
    "bfd-desired-min-tx": {"type": "integer", "min": 1, "max": 100000},
    "bfd-required-min-rx": {"type": "integer", "min": 1, "max": 100000},
    "bfd-detect-mult": {"type": "integer", "min": 1, "max": 50},
    "vpn-stats-period": {"type": "integer", "min": 0, "max": 4294967295},
    "mac-ttl": {"type": "integer", "min": 300, "max": 8640000},
    "dhcp-proxy-interface": {"type": "string", "max_length": 15},
    "dhcp-proxy-vrf-select": {"type": "integer", "min": 0, "max": 511},
    "sip-tcp-port": {"type": "integer", "min": 1, "max": 65535},
    "sip-udp-port": {"type": "integer", "min": 1, "max": 65535},
    "sip-ssl-port": {"type": "integer", "min": 0, "max": 65535},
    "sccp-port": {"type": "integer", "min": 0, "max": 65535},
    "ecmp-max-paths": {"type": "integer", "min": 1, "max": 255},
    "discovered-device-timeout": {"type": "integer", "min": 1, "max": 365},
    "ike-port": {"type": "integer", "min": 1024, "max": 65535},
    "ike-tcp-port": {"type": "integer", "min": 1, "max": 65535},
    "default-policy-expiry-days": {"type": "integer", "min": 0, "max": 365},
    "internet-service-app-ctrl-size": {"type": "integer", "min": 0, "max": 4294967295},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "gui-default-policy-columns": {
        "name": {
            "type": "string",
            "help": "Select column name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_VDOM_TYPE = [
    "traffic",
    "lan-extension",
    "admin",
]
VALID_BODY_OPMODE = [
    "nat",
    "transparent",
]
VALID_BODY_NGFW_MODE = [
    "profile-based",
    "policy-based",
]
VALID_BODY_HTTP_EXTERNAL_DEST = [
    "fortiweb",
    "forticache",
]
VALID_BODY_FIREWALL_SESSION_DIRTY = [
    "check-all",
    "check-new",
    "check-policy-option",
]
VALID_BODY_BFD = [
    "enable",
    "disable",
]
VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT = [
    "enable",
    "disable",
]
VALID_BODY_UTF8_SPAM_TAGGING = [
    "enable",
    "disable",
]
VALID_BODY_WCCP_CACHE_ENGINE = [
    "enable",
    "disable",
]
VALID_BODY_VPN_STATS_LOG = [
    "ipsec",
    "pptp",
    "l2tp",
    "ssl",
]
VALID_BODY_V4_ECMP_MODE = [
    "source-ip-based",
    "weight-based",
    "usage-based",
    "source-dest-ip-based",
]
VALID_BODY_FW_SESSION_HAIRPIN = [
    "enable",
    "disable",
]
VALID_BODY_PRP_TRAILER_ACTION = [
    "enable",
    "disable",
]
VALID_BODY_SNAT_HAIRPIN_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_DHCP_PROXY = [
    "enable",
    "disable",
]
VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD = [
    "auto",
    "sdwan",
    "specify",
]
VALID_BODY_CENTRAL_NAT = [
    "enable",
    "disable",
]
VALID_BODY_LLDP_RECEPTION = [
    "enable",
    "disable",
    "global",
]
VALID_BODY_LLDP_TRANSMISSION = [
    "enable",
    "disable",
    "global",
]
VALID_BODY_LINK_DOWN_ACCESS = [
    "enable",
    "disable",
]
VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER = [
    "enable",
    "disable",
]
VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING = [
    "enable",
    "disable",
]
VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING = [
    "enable",
    "disable",
]
VALID_BODY_DETECT_UNKNOWN_ESP = [
    "enable",
    "disable",
]
VALID_BODY_INTREE_SES_BEST_ROUTE = [
    "force",
    "disable",
]
VALID_BODY_AUXILIARY_SESSION = [
    "enable",
    "disable",
]
VALID_BODY_ASYMROUTE = [
    "enable",
    "disable",
]
VALID_BODY_ASYMROUTE_ICMP = [
    "enable",
    "disable",
]
VALID_BODY_TCP_SESSION_WITHOUT_SYN = [
    "enable",
    "disable",
]
VALID_BODY_SES_DENIED_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC = [
    "enable",
    "disable",
]
VALID_BODY_STRICT_SRC_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_ALLOW_LINKDOWN_PATH = [
    "enable",
    "disable",
]
VALID_BODY_ASYMROUTE6 = [
    "enable",
    "disable",
]
VALID_BODY_ASYMROUTE6_ICMP = [
    "enable",
    "disable",
]
VALID_BODY_SCTP_SESSION_WITHOUT_INIT = [
    "enable",
    "disable",
]
VALID_BODY_SIP_EXPECTATION = [
    "enable",
    "disable",
]
VALID_BODY_SIP_NAT_TRACE = [
    "enable",
    "disable",
]
VALID_BODY_H323_DIRECT_MODEL = [
    "disable",
    "enable",
]
VALID_BODY_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_MULTICAST_FORWARD = [
    "enable",
    "disable",
]
VALID_BODY_MULTICAST_TTL_NOTCHANGE = [
    "enable",
    "disable",
]
VALID_BODY_MULTICAST_SKIP_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_ALLOW_SUBNET_OVERLAP = [
    "enable",
    "disable",
]
VALID_BODY_DENY_TCP_WITH_ICMP = [
    "enable",
    "disable",
]
VALID_BODY_EMAIL_PORTAL_CHECK_DNS = [
    "disable",
    "enable",
]
VALID_BODY_DEFAULT_VOIP_ALG_MODE = [
    "proxy-based",
    "kernel-helper-based",
]
VALID_BODY_GUI_ICAP = [
    "enable",
    "disable",
]
VALID_BODY_GUI_IMPLICIT_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DNS_DATABASE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_LOAD_BALANCE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_MULTICAST_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DOS_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_OBJECT_COLORS = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION = [
    "enable",
    "disable",
]
VALID_BODY_GUI_VOIP_PROFILE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_AP_PROFILE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_SECURITY_PROFILE_GROUP = [
    "enable",
    "disable",
]
VALID_BODY_GUI_LOCAL_IN_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WANOPT_CACHE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_EXPLICIT_PROXY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DYNAMIC_ROUTING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_SSLVPN_PERSONAL_BOOKMARKS = [
    "enable",
    "disable",
]
VALID_BODY_GUI_SSLVPN_REALMS = [
    "enable",
    "disable",
]
VALID_BODY_GUI_POLICY_BASED_IPSEC = [
    "enable",
    "disable",
]
VALID_BODY_GUI_THREAT_WEIGHT = [
    "enable",
    "disable",
]
VALID_BODY_GUI_SPAMFILTER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_FILE_FILTER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_APPLICATION_CONTROL = [
    "enable",
    "disable",
]
VALID_BODY_GUI_IPS = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DHCP_ADVANCED = [
    "enable",
    "disable",
]
VALID_BODY_GUI_VPN = [
    "enable",
    "disable",
]
VALID_BODY_GUI_SSLVPN = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WIRELESS_CONTROLLER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES = [
    "enable",
    "disable",
]
VALID_BODY_GUI_SWITCH_CONTROLLER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WEBFILTER_ADVANCED = [
    "enable",
    "disable",
]
VALID_BODY_GUI_TRAFFIC_SHAPING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WAN_LOAD_BALANCING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ANTIVIRUS = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WEBFILTER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_VIDEOFILTER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DNSFILTER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WAF_PROFILE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DLP_PROFILE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DLP_ADVANCED = [
    "enable",
    "disable",
]
VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_CASB = [
    "enable",
    "disable",
]
VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ADVANCED_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ALLOW_UNNAMED_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_EMAIL_COLLECTION = [
    "enable",
    "disable",
]
VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_POLICY_DISCLAIMER = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ZTNA = [
    "enable",
    "disable",
]
VALID_BODY_GUI_OT = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID = [
    "enable",
    "disable",
]
VALID_BODY_GUI_GTP = [
    "enable",
    "disable",
]
VALID_BODY_IKE_SESSION_RESUME = [
    "enable",
    "disable",
]
VALID_BODY_IKE_QUICK_CRASH_DETECT = [
    "enable",
    "disable",
]
VALID_BODY_IKE_DN_FORMAT = [
    "with-space",
    "no-space",
]
VALID_BODY_IKE_POLICY_ROUTE = [
    "enable",
    "disable",
]
VALID_BODY_IKE_DETAILED_EVENT_LOGS = [
    "disable",
    "enable",
]
VALID_BODY_BLOCK_LAND_ATTACK = [
    "disable",
    "enable",
]
VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE = [
    "enable",
    "disable",
]
VALID_BODY_FQDN_SESSION_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_EXT_RESOURCE_SESSION_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_DYN_ADDR_SESSION_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY = [
    "disable",
    "require",
    "optional",
]
VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE = [
    "disable",
    "enable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_settings_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/settings.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_settings_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_settings_get(
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
    Validate required fields for system/settings.

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


def validate_system_settings_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/settings object.

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
        ...     "manageip": True,  # Transparent mode IPv4 management IP address and ne
        ...     "device": True,  # Interface to use for management access for NAT mod
        ... }
        >>> is_valid, error = validate_system_settings_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "manageip": True,
        ...     "vdom-type": "traffic",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_settings_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["vdom-type"] = "invalid-value"
        >>> is_valid, error = validate_system_settings_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_settings_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "vdom-type" in payload:
        value = payload["vdom-type"]
        if value not in VALID_BODY_VDOM_TYPE:
            desc = FIELD_DESCRIPTIONS.get("vdom-type", "")
            error_msg = f"Invalid value for 'vdom-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VDOM_TYPE)}"
            error_msg += f"\n  → Example: vdom-type='{{ VALID_BODY_VDOM_TYPE[0] }}'"
            return (False, error_msg)
    if "opmode" in payload:
        value = payload["opmode"]
        if value not in VALID_BODY_OPMODE:
            desc = FIELD_DESCRIPTIONS.get("opmode", "")
            error_msg = f"Invalid value for 'opmode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OPMODE)}"
            error_msg += f"\n  → Example: opmode='{{ VALID_BODY_OPMODE[0] }}'"
            return (False, error_msg)
    if "ngfw-mode" in payload:
        value = payload["ngfw-mode"]
        if value not in VALID_BODY_NGFW_MODE:
            desc = FIELD_DESCRIPTIONS.get("ngfw-mode", "")
            error_msg = f"Invalid value for 'ngfw-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NGFW_MODE)}"
            error_msg += f"\n  → Example: ngfw-mode='{{ VALID_BODY_NGFW_MODE[0] }}'"
            return (False, error_msg)
    if "http-external-dest" in payload:
        value = payload["http-external-dest"]
        if value not in VALID_BODY_HTTP_EXTERNAL_DEST:
            desc = FIELD_DESCRIPTIONS.get("http-external-dest", "")
            error_msg = f"Invalid value for 'http-external-dest': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_EXTERNAL_DEST)}"
            error_msg += f"\n  → Example: http-external-dest='{{ VALID_BODY_HTTP_EXTERNAL_DEST[0] }}'"
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
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            desc = FIELD_DESCRIPTIONS.get("bfd", "")
            error_msg = f"Invalid value for 'bfd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BFD)}"
            error_msg += f"\n  → Example: bfd='{{ VALID_BODY_BFD[0] }}'"
            return (False, error_msg)
    if "bfd-dont-enforce-src-port" in payload:
        value = payload["bfd-dont-enforce-src-port"]
        if value not in VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT:
            desc = FIELD_DESCRIPTIONS.get("bfd-dont-enforce-src-port", "")
            error_msg = f"Invalid value for 'bfd-dont-enforce-src-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT)}"
            error_msg += f"\n  → Example: bfd-dont-enforce-src-port='{{ VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT[0] }}'"
            return (False, error_msg)
    if "utf8-spam-tagging" in payload:
        value = payload["utf8-spam-tagging"]
        if value not in VALID_BODY_UTF8_SPAM_TAGGING:
            desc = FIELD_DESCRIPTIONS.get("utf8-spam-tagging", "")
            error_msg = f"Invalid value for 'utf8-spam-tagging': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTF8_SPAM_TAGGING)}"
            error_msg += f"\n  → Example: utf8-spam-tagging='{{ VALID_BODY_UTF8_SPAM_TAGGING[0] }}'"
            return (False, error_msg)
    if "wccp-cache-engine" in payload:
        value = payload["wccp-cache-engine"]
        if value not in VALID_BODY_WCCP_CACHE_ENGINE:
            desc = FIELD_DESCRIPTIONS.get("wccp-cache-engine", "")
            error_msg = f"Invalid value for 'wccp-cache-engine': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WCCP_CACHE_ENGINE)}"
            error_msg += f"\n  → Example: wccp-cache-engine='{{ VALID_BODY_WCCP_CACHE_ENGINE[0] }}'"
            return (False, error_msg)
    if "vpn-stats-log" in payload:
        value = payload["vpn-stats-log"]
        if value not in VALID_BODY_VPN_STATS_LOG:
            desc = FIELD_DESCRIPTIONS.get("vpn-stats-log", "")
            error_msg = f"Invalid value for 'vpn-stats-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VPN_STATS_LOG)}"
            error_msg += f"\n  → Example: vpn-stats-log='{{ VALID_BODY_VPN_STATS_LOG[0] }}'"
            return (False, error_msg)
    if "v4-ecmp-mode" in payload:
        value = payload["v4-ecmp-mode"]
        if value not in VALID_BODY_V4_ECMP_MODE:
            desc = FIELD_DESCRIPTIONS.get("v4-ecmp-mode", "")
            error_msg = f"Invalid value for 'v4-ecmp-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_V4_ECMP_MODE)}"
            error_msg += f"\n  → Example: v4-ecmp-mode='{{ VALID_BODY_V4_ECMP_MODE[0] }}'"
            return (False, error_msg)
    if "fw-session-hairpin" in payload:
        value = payload["fw-session-hairpin"]
        if value not in VALID_BODY_FW_SESSION_HAIRPIN:
            desc = FIELD_DESCRIPTIONS.get("fw-session-hairpin", "")
            error_msg = f"Invalid value for 'fw-session-hairpin': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FW_SESSION_HAIRPIN)}"
            error_msg += f"\n  → Example: fw-session-hairpin='{{ VALID_BODY_FW_SESSION_HAIRPIN[0] }}'"
            return (False, error_msg)
    if "prp-trailer-action" in payload:
        value = payload["prp-trailer-action"]
        if value not in VALID_BODY_PRP_TRAILER_ACTION:
            desc = FIELD_DESCRIPTIONS.get("prp-trailer-action", "")
            error_msg = f"Invalid value for 'prp-trailer-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRP_TRAILER_ACTION)}"
            error_msg += f"\n  → Example: prp-trailer-action='{{ VALID_BODY_PRP_TRAILER_ACTION[0] }}'"
            return (False, error_msg)
    if "snat-hairpin-traffic" in payload:
        value = payload["snat-hairpin-traffic"]
        if value not in VALID_BODY_SNAT_HAIRPIN_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("snat-hairpin-traffic", "")
            error_msg = f"Invalid value for 'snat-hairpin-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SNAT_HAIRPIN_TRAFFIC)}"
            error_msg += f"\n  → Example: snat-hairpin-traffic='{{ VALID_BODY_SNAT_HAIRPIN_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "dhcp-proxy" in payload:
        value = payload["dhcp-proxy"]
        if value not in VALID_BODY_DHCP_PROXY:
            desc = FIELD_DESCRIPTIONS.get("dhcp-proxy", "")
            error_msg = f"Invalid value for 'dhcp-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_PROXY)}"
            error_msg += f"\n  → Example: dhcp-proxy='{{ VALID_BODY_DHCP_PROXY[0] }}'"
            return (False, error_msg)
    if "dhcp-proxy-interface-select-method" in payload:
        value = payload["dhcp-proxy-interface-select-method"]
        if value not in VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("dhcp-proxy-interface-select-method", "")
            error_msg = f"Invalid value for 'dhcp-proxy-interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: dhcp-proxy-interface-select-method='{{ VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "central-nat" in payload:
        value = payload["central-nat"]
        if value not in VALID_BODY_CENTRAL_NAT:
            desc = FIELD_DESCRIPTIONS.get("central-nat", "")
            error_msg = f"Invalid value for 'central-nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CENTRAL_NAT)}"
            error_msg += f"\n  → Example: central-nat='{{ VALID_BODY_CENTRAL_NAT[0] }}'"
            return (False, error_msg)
    if "lldp-reception" in payload:
        value = payload["lldp-reception"]
        if value not in VALID_BODY_LLDP_RECEPTION:
            desc = FIELD_DESCRIPTIONS.get("lldp-reception", "")
            error_msg = f"Invalid value for 'lldp-reception': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LLDP_RECEPTION)}"
            error_msg += f"\n  → Example: lldp-reception='{{ VALID_BODY_LLDP_RECEPTION[0] }}'"
            return (False, error_msg)
    if "lldp-transmission" in payload:
        value = payload["lldp-transmission"]
        if value not in VALID_BODY_LLDP_TRANSMISSION:
            desc = FIELD_DESCRIPTIONS.get("lldp-transmission", "")
            error_msg = f"Invalid value for 'lldp-transmission': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LLDP_TRANSMISSION)}"
            error_msg += f"\n  → Example: lldp-transmission='{{ VALID_BODY_LLDP_TRANSMISSION[0] }}'"
            return (False, error_msg)
    if "link-down-access" in payload:
        value = payload["link-down-access"]
        if value not in VALID_BODY_LINK_DOWN_ACCESS:
            desc = FIELD_DESCRIPTIONS.get("link-down-access", "")
            error_msg = f"Invalid value for 'link-down-access': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LINK_DOWN_ACCESS)}"
            error_msg += f"\n  → Example: link-down-access='{{ VALID_BODY_LINK_DOWN_ACCESS[0] }}'"
            return (False, error_msg)
    if "nat46-generate-ipv6-fragment-header" in payload:
        value = payload["nat46-generate-ipv6-fragment-header"]
        if value not in VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER:
            desc = FIELD_DESCRIPTIONS.get("nat46-generate-ipv6-fragment-header", "")
            error_msg = f"Invalid value for 'nat46-generate-ipv6-fragment-header': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER)}"
            error_msg += f"\n  → Example: nat46-generate-ipv6-fragment-header='{{ VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER[0] }}'"
            return (False, error_msg)
    if "nat46-force-ipv4-packet-forwarding" in payload:
        value = payload["nat46-force-ipv4-packet-forwarding"]
        if value not in VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING:
            desc = FIELD_DESCRIPTIONS.get("nat46-force-ipv4-packet-forwarding", "")
            error_msg = f"Invalid value for 'nat46-force-ipv4-packet-forwarding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING)}"
            error_msg += f"\n  → Example: nat46-force-ipv4-packet-forwarding='{{ VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING[0] }}'"
            return (False, error_msg)
    if "nat64-force-ipv6-packet-forwarding" in payload:
        value = payload["nat64-force-ipv6-packet-forwarding"]
        if value not in VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING:
            desc = FIELD_DESCRIPTIONS.get("nat64-force-ipv6-packet-forwarding", "")
            error_msg = f"Invalid value for 'nat64-force-ipv6-packet-forwarding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING)}"
            error_msg += f"\n  → Example: nat64-force-ipv6-packet-forwarding='{{ VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING[0] }}'"
            return (False, error_msg)
    if "detect-unknown-esp" in payload:
        value = payload["detect-unknown-esp"]
        if value not in VALID_BODY_DETECT_UNKNOWN_ESP:
            desc = FIELD_DESCRIPTIONS.get("detect-unknown-esp", "")
            error_msg = f"Invalid value for 'detect-unknown-esp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DETECT_UNKNOWN_ESP)}"
            error_msg += f"\n  → Example: detect-unknown-esp='{{ VALID_BODY_DETECT_UNKNOWN_ESP[0] }}'"
            return (False, error_msg)
    if "intree-ses-best-route" in payload:
        value = payload["intree-ses-best-route"]
        if value not in VALID_BODY_INTREE_SES_BEST_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("intree-ses-best-route", "")
            error_msg = f"Invalid value for 'intree-ses-best-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTREE_SES_BEST_ROUTE)}"
            error_msg += f"\n  → Example: intree-ses-best-route='{{ VALID_BODY_INTREE_SES_BEST_ROUTE[0] }}'"
            return (False, error_msg)
    if "auxiliary-session" in payload:
        value = payload["auxiliary-session"]
        if value not in VALID_BODY_AUXILIARY_SESSION:
            desc = FIELD_DESCRIPTIONS.get("auxiliary-session", "")
            error_msg = f"Invalid value for 'auxiliary-session': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUXILIARY_SESSION)}"
            error_msg += f"\n  → Example: auxiliary-session='{{ VALID_BODY_AUXILIARY_SESSION[0] }}'"
            return (False, error_msg)
    if "asymroute" in payload:
        value = payload["asymroute"]
        if value not in VALID_BODY_ASYMROUTE:
            desc = FIELD_DESCRIPTIONS.get("asymroute", "")
            error_msg = f"Invalid value for 'asymroute': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASYMROUTE)}"
            error_msg += f"\n  → Example: asymroute='{{ VALID_BODY_ASYMROUTE[0] }}'"
            return (False, error_msg)
    if "asymroute-icmp" in payload:
        value = payload["asymroute-icmp"]
        if value not in VALID_BODY_ASYMROUTE_ICMP:
            desc = FIELD_DESCRIPTIONS.get("asymroute-icmp", "")
            error_msg = f"Invalid value for 'asymroute-icmp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASYMROUTE_ICMP)}"
            error_msg += f"\n  → Example: asymroute-icmp='{{ VALID_BODY_ASYMROUTE_ICMP[0] }}'"
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
    if "ses-denied-traffic" in payload:
        value = payload["ses-denied-traffic"]
        if value not in VALID_BODY_SES_DENIED_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("ses-denied-traffic", "")
            error_msg = f"Invalid value for 'ses-denied-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SES_DENIED_TRAFFIC)}"
            error_msg += f"\n  → Example: ses-denied-traffic='{{ VALID_BODY_SES_DENIED_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "ses-denied-multicast-traffic" in payload:
        value = payload["ses-denied-multicast-traffic"]
        if value not in VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC:
            desc = FIELD_DESCRIPTIONS.get("ses-denied-multicast-traffic", "")
            error_msg = f"Invalid value for 'ses-denied-multicast-traffic': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC)}"
            error_msg += f"\n  → Example: ses-denied-multicast-traffic='{{ VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC[0] }}'"
            return (False, error_msg)
    if "strict-src-check" in payload:
        value = payload["strict-src-check"]
        if value not in VALID_BODY_STRICT_SRC_CHECK:
            desc = FIELD_DESCRIPTIONS.get("strict-src-check", "")
            error_msg = f"Invalid value for 'strict-src-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRICT_SRC_CHECK)}"
            error_msg += f"\n  → Example: strict-src-check='{{ VALID_BODY_STRICT_SRC_CHECK[0] }}'"
            return (False, error_msg)
    if "allow-linkdown-path" in payload:
        value = payload["allow-linkdown-path"]
        if value not in VALID_BODY_ALLOW_LINKDOWN_PATH:
            desc = FIELD_DESCRIPTIONS.get("allow-linkdown-path", "")
            error_msg = f"Invalid value for 'allow-linkdown-path': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_LINKDOWN_PATH)}"
            error_msg += f"\n  → Example: allow-linkdown-path='{{ VALID_BODY_ALLOW_LINKDOWN_PATH[0] }}'"
            return (False, error_msg)
    if "asymroute6" in payload:
        value = payload["asymroute6"]
        if value not in VALID_BODY_ASYMROUTE6:
            desc = FIELD_DESCRIPTIONS.get("asymroute6", "")
            error_msg = f"Invalid value for 'asymroute6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASYMROUTE6)}"
            error_msg += f"\n  → Example: asymroute6='{{ VALID_BODY_ASYMROUTE6[0] }}'"
            return (False, error_msg)
    if "asymroute6-icmp" in payload:
        value = payload["asymroute6-icmp"]
        if value not in VALID_BODY_ASYMROUTE6_ICMP:
            desc = FIELD_DESCRIPTIONS.get("asymroute6-icmp", "")
            error_msg = f"Invalid value for 'asymroute6-icmp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASYMROUTE6_ICMP)}"
            error_msg += f"\n  → Example: asymroute6-icmp='{{ VALID_BODY_ASYMROUTE6_ICMP[0] }}'"
            return (False, error_msg)
    if "sctp-session-without-init" in payload:
        value = payload["sctp-session-without-init"]
        if value not in VALID_BODY_SCTP_SESSION_WITHOUT_INIT:
            desc = FIELD_DESCRIPTIONS.get("sctp-session-without-init", "")
            error_msg = f"Invalid value for 'sctp-session-without-init': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCTP_SESSION_WITHOUT_INIT)}"
            error_msg += f"\n  → Example: sctp-session-without-init='{{ VALID_BODY_SCTP_SESSION_WITHOUT_INIT[0] }}'"
            return (False, error_msg)
    if "sip-expectation" in payload:
        value = payload["sip-expectation"]
        if value not in VALID_BODY_SIP_EXPECTATION:
            desc = FIELD_DESCRIPTIONS.get("sip-expectation", "")
            error_msg = f"Invalid value for 'sip-expectation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SIP_EXPECTATION)}"
            error_msg += f"\n  → Example: sip-expectation='{{ VALID_BODY_SIP_EXPECTATION[0] }}'"
            return (False, error_msg)
    if "sip-nat-trace" in payload:
        value = payload["sip-nat-trace"]
        if value not in VALID_BODY_SIP_NAT_TRACE:
            desc = FIELD_DESCRIPTIONS.get("sip-nat-trace", "")
            error_msg = f"Invalid value for 'sip-nat-trace': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SIP_NAT_TRACE)}"
            error_msg += f"\n  → Example: sip-nat-trace='{{ VALID_BODY_SIP_NAT_TRACE[0] }}'"
            return (False, error_msg)
    if "h323-direct-model" in payload:
        value = payload["h323-direct-model"]
        if value not in VALID_BODY_H323_DIRECT_MODEL:
            desc = FIELD_DESCRIPTIONS.get("h323-direct-model", "")
            error_msg = f"Invalid value for 'h323-direct-model': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_H323_DIRECT_MODEL)}"
            error_msg += f"\n  → Example: h323-direct-model='{{ VALID_BODY_H323_DIRECT_MODEL[0] }}'"
            return (False, error_msg)
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
    if "multicast-forward" in payload:
        value = payload["multicast-forward"]
        if value not in VALID_BODY_MULTICAST_FORWARD:
            desc = FIELD_DESCRIPTIONS.get("multicast-forward", "")
            error_msg = f"Invalid value for 'multicast-forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_FORWARD)}"
            error_msg += f"\n  → Example: multicast-forward='{{ VALID_BODY_MULTICAST_FORWARD[0] }}'"
            return (False, error_msg)
    if "multicast-ttl-notchange" in payload:
        value = payload["multicast-ttl-notchange"]
        if value not in VALID_BODY_MULTICAST_TTL_NOTCHANGE:
            desc = FIELD_DESCRIPTIONS.get("multicast-ttl-notchange", "")
            error_msg = f"Invalid value for 'multicast-ttl-notchange': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_TTL_NOTCHANGE)}"
            error_msg += f"\n  → Example: multicast-ttl-notchange='{{ VALID_BODY_MULTICAST_TTL_NOTCHANGE[0] }}'"
            return (False, error_msg)
    if "multicast-skip-policy" in payload:
        value = payload["multicast-skip-policy"]
        if value not in VALID_BODY_MULTICAST_SKIP_POLICY:
            desc = FIELD_DESCRIPTIONS.get("multicast-skip-policy", "")
            error_msg = f"Invalid value for 'multicast-skip-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_SKIP_POLICY)}"
            error_msg += f"\n  → Example: multicast-skip-policy='{{ VALID_BODY_MULTICAST_SKIP_POLICY[0] }}'"
            return (False, error_msg)
    if "allow-subnet-overlap" in payload:
        value = payload["allow-subnet-overlap"]
        if value not in VALID_BODY_ALLOW_SUBNET_OVERLAP:
            desc = FIELD_DESCRIPTIONS.get("allow-subnet-overlap", "")
            error_msg = f"Invalid value for 'allow-subnet-overlap': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_SUBNET_OVERLAP)}"
            error_msg += f"\n  → Example: allow-subnet-overlap='{{ VALID_BODY_ALLOW_SUBNET_OVERLAP[0] }}'"
            return (False, error_msg)
    if "deny-tcp-with-icmp" in payload:
        value = payload["deny-tcp-with-icmp"]
        if value not in VALID_BODY_DENY_TCP_WITH_ICMP:
            desc = FIELD_DESCRIPTIONS.get("deny-tcp-with-icmp", "")
            error_msg = f"Invalid value for 'deny-tcp-with-icmp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DENY_TCP_WITH_ICMP)}"
            error_msg += f"\n  → Example: deny-tcp-with-icmp='{{ VALID_BODY_DENY_TCP_WITH_ICMP[0] }}'"
            return (False, error_msg)
    if "email-portal-check-dns" in payload:
        value = payload["email-portal-check-dns"]
        if value not in VALID_BODY_EMAIL_PORTAL_CHECK_DNS:
            desc = FIELD_DESCRIPTIONS.get("email-portal-check-dns", "")
            error_msg = f"Invalid value for 'email-portal-check-dns': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMAIL_PORTAL_CHECK_DNS)}"
            error_msg += f"\n  → Example: email-portal-check-dns='{{ VALID_BODY_EMAIL_PORTAL_CHECK_DNS[0] }}'"
            return (False, error_msg)
    if "default-voip-alg-mode" in payload:
        value = payload["default-voip-alg-mode"]
        if value not in VALID_BODY_DEFAULT_VOIP_ALG_MODE:
            desc = FIELD_DESCRIPTIONS.get("default-voip-alg-mode", "")
            error_msg = f"Invalid value for 'default-voip-alg-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_VOIP_ALG_MODE)}"
            error_msg += f"\n  → Example: default-voip-alg-mode='{{ VALID_BODY_DEFAULT_VOIP_ALG_MODE[0] }}'"
            return (False, error_msg)
    if "gui-icap" in payload:
        value = payload["gui-icap"]
        if value not in VALID_BODY_GUI_ICAP:
            desc = FIELD_DESCRIPTIONS.get("gui-icap", "")
            error_msg = f"Invalid value for 'gui-icap': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ICAP)}"
            error_msg += f"\n  → Example: gui-icap='{{ VALID_BODY_GUI_ICAP[0] }}'"
            return (False, error_msg)
    if "gui-implicit-policy" in payload:
        value = payload["gui-implicit-policy"]
        if value not in VALID_BODY_GUI_IMPLICIT_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-implicit-policy", "")
            error_msg = f"Invalid value for 'gui-implicit-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_IMPLICIT_POLICY)}"
            error_msg += f"\n  → Example: gui-implicit-policy='{{ VALID_BODY_GUI_IMPLICIT_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-dns-database" in payload:
        value = payload["gui-dns-database"]
        if value not in VALID_BODY_GUI_DNS_DATABASE:
            desc = FIELD_DESCRIPTIONS.get("gui-dns-database", "")
            error_msg = f"Invalid value for 'gui-dns-database': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DNS_DATABASE)}"
            error_msg += f"\n  → Example: gui-dns-database='{{ VALID_BODY_GUI_DNS_DATABASE[0] }}'"
            return (False, error_msg)
    if "gui-load-balance" in payload:
        value = payload["gui-load-balance"]
        if value not in VALID_BODY_GUI_LOAD_BALANCE:
            desc = FIELD_DESCRIPTIONS.get("gui-load-balance", "")
            error_msg = f"Invalid value for 'gui-load-balance': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_LOAD_BALANCE)}"
            error_msg += f"\n  → Example: gui-load-balance='{{ VALID_BODY_GUI_LOAD_BALANCE[0] }}'"
            return (False, error_msg)
    if "gui-multicast-policy" in payload:
        value = payload["gui-multicast-policy"]
        if value not in VALID_BODY_GUI_MULTICAST_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-multicast-policy", "")
            error_msg = f"Invalid value for 'gui-multicast-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_MULTICAST_POLICY)}"
            error_msg += f"\n  → Example: gui-multicast-policy='{{ VALID_BODY_GUI_MULTICAST_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-dos-policy" in payload:
        value = payload["gui-dos-policy"]
        if value not in VALID_BODY_GUI_DOS_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-dos-policy", "")
            error_msg = f"Invalid value for 'gui-dos-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DOS_POLICY)}"
            error_msg += f"\n  → Example: gui-dos-policy='{{ VALID_BODY_GUI_DOS_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-object-colors" in payload:
        value = payload["gui-object-colors"]
        if value not in VALID_BODY_GUI_OBJECT_COLORS:
            desc = FIELD_DESCRIPTIONS.get("gui-object-colors", "")
            error_msg = f"Invalid value for 'gui-object-colors': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_OBJECT_COLORS)}"
            error_msg += f"\n  → Example: gui-object-colors='{{ VALID_BODY_GUI_OBJECT_COLORS[0] }}'"
            return (False, error_msg)
    if "gui-route-tag-address-creation" in payload:
        value = payload["gui-route-tag-address-creation"]
        if value not in VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION:
            desc = FIELD_DESCRIPTIONS.get("gui-route-tag-address-creation", "")
            error_msg = f"Invalid value for 'gui-route-tag-address-creation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION)}"
            error_msg += f"\n  → Example: gui-route-tag-address-creation='{{ VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION[0] }}'"
            return (False, error_msg)
    if "gui-voip-profile" in payload:
        value = payload["gui-voip-profile"]
        if value not in VALID_BODY_GUI_VOIP_PROFILE:
            desc = FIELD_DESCRIPTIONS.get("gui-voip-profile", "")
            error_msg = f"Invalid value for 'gui-voip-profile': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_VOIP_PROFILE)}"
            error_msg += f"\n  → Example: gui-voip-profile='{{ VALID_BODY_GUI_VOIP_PROFILE[0] }}'"
            return (False, error_msg)
    if "gui-ap-profile" in payload:
        value = payload["gui-ap-profile"]
        if value not in VALID_BODY_GUI_AP_PROFILE:
            desc = FIELD_DESCRIPTIONS.get("gui-ap-profile", "")
            error_msg = f"Invalid value for 'gui-ap-profile': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_AP_PROFILE)}"
            error_msg += f"\n  → Example: gui-ap-profile='{{ VALID_BODY_GUI_AP_PROFILE[0] }}'"
            return (False, error_msg)
    if "gui-security-profile-group" in payload:
        value = payload["gui-security-profile-group"]
        if value not in VALID_BODY_GUI_SECURITY_PROFILE_GROUP:
            desc = FIELD_DESCRIPTIONS.get("gui-security-profile-group", "")
            error_msg = f"Invalid value for 'gui-security-profile-group': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_SECURITY_PROFILE_GROUP)}"
            error_msg += f"\n  → Example: gui-security-profile-group='{{ VALID_BODY_GUI_SECURITY_PROFILE_GROUP[0] }}'"
            return (False, error_msg)
    if "gui-local-in-policy" in payload:
        value = payload["gui-local-in-policy"]
        if value not in VALID_BODY_GUI_LOCAL_IN_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-local-in-policy", "")
            error_msg = f"Invalid value for 'gui-local-in-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_LOCAL_IN_POLICY)}"
            error_msg += f"\n  → Example: gui-local-in-policy='{{ VALID_BODY_GUI_LOCAL_IN_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-wanopt-cache" in payload:
        value = payload["gui-wanopt-cache"]
        if value not in VALID_BODY_GUI_WANOPT_CACHE:
            desc = FIELD_DESCRIPTIONS.get("gui-wanopt-cache", "")
            error_msg = f"Invalid value for 'gui-wanopt-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WANOPT_CACHE)}"
            error_msg += f"\n  → Example: gui-wanopt-cache='{{ VALID_BODY_GUI_WANOPT_CACHE[0] }}'"
            return (False, error_msg)
    if "gui-explicit-proxy" in payload:
        value = payload["gui-explicit-proxy"]
        if value not in VALID_BODY_GUI_EXPLICIT_PROXY:
            desc = FIELD_DESCRIPTIONS.get("gui-explicit-proxy", "")
            error_msg = f"Invalid value for 'gui-explicit-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_EXPLICIT_PROXY)}"
            error_msg += f"\n  → Example: gui-explicit-proxy='{{ VALID_BODY_GUI_EXPLICIT_PROXY[0] }}'"
            return (False, error_msg)
    if "gui-dynamic-routing" in payload:
        value = payload["gui-dynamic-routing"]
        if value not in VALID_BODY_GUI_DYNAMIC_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("gui-dynamic-routing", "")
            error_msg = f"Invalid value for 'gui-dynamic-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DYNAMIC_ROUTING)}"
            error_msg += f"\n  → Example: gui-dynamic-routing='{{ VALID_BODY_GUI_DYNAMIC_ROUTING[0] }}'"
            return (False, error_msg)
    if "gui-sslvpn-personal-bookmarks" in payload:
        value = payload["gui-sslvpn-personal-bookmarks"]
        if value not in VALID_BODY_GUI_SSLVPN_PERSONAL_BOOKMARKS:
            desc = FIELD_DESCRIPTIONS.get("gui-sslvpn-personal-bookmarks", "")
            error_msg = f"Invalid value for 'gui-sslvpn-personal-bookmarks': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_SSLVPN_PERSONAL_BOOKMARKS)}"
            error_msg += f"\n  → Example: gui-sslvpn-personal-bookmarks='{{ VALID_BODY_GUI_SSLVPN_PERSONAL_BOOKMARKS[0] }}'"
            return (False, error_msg)
    if "gui-sslvpn-realms" in payload:
        value = payload["gui-sslvpn-realms"]
        if value not in VALID_BODY_GUI_SSLVPN_REALMS:
            desc = FIELD_DESCRIPTIONS.get("gui-sslvpn-realms", "")
            error_msg = f"Invalid value for 'gui-sslvpn-realms': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_SSLVPN_REALMS)}"
            error_msg += f"\n  → Example: gui-sslvpn-realms='{{ VALID_BODY_GUI_SSLVPN_REALMS[0] }}'"
            return (False, error_msg)
    if "gui-policy-based-ipsec" in payload:
        value = payload["gui-policy-based-ipsec"]
        if value not in VALID_BODY_GUI_POLICY_BASED_IPSEC:
            desc = FIELD_DESCRIPTIONS.get("gui-policy-based-ipsec", "")
            error_msg = f"Invalid value for 'gui-policy-based-ipsec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_POLICY_BASED_IPSEC)}"
            error_msg += f"\n  → Example: gui-policy-based-ipsec='{{ VALID_BODY_GUI_POLICY_BASED_IPSEC[0] }}'"
            return (False, error_msg)
    if "gui-threat-weight" in payload:
        value = payload["gui-threat-weight"]
        if value not in VALID_BODY_GUI_THREAT_WEIGHT:
            desc = FIELD_DESCRIPTIONS.get("gui-threat-weight", "")
            error_msg = f"Invalid value for 'gui-threat-weight': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_THREAT_WEIGHT)}"
            error_msg += f"\n  → Example: gui-threat-weight='{{ VALID_BODY_GUI_THREAT_WEIGHT[0] }}'"
            return (False, error_msg)
    if "gui-spamfilter" in payload:
        value = payload["gui-spamfilter"]
        if value not in VALID_BODY_GUI_SPAMFILTER:
            desc = FIELD_DESCRIPTIONS.get("gui-spamfilter", "")
            error_msg = f"Invalid value for 'gui-spamfilter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_SPAMFILTER)}"
            error_msg += f"\n  → Example: gui-spamfilter='{{ VALID_BODY_GUI_SPAMFILTER[0] }}'"
            return (False, error_msg)
    if "gui-file-filter" in payload:
        value = payload["gui-file-filter"]
        if value not in VALID_BODY_GUI_FILE_FILTER:
            desc = FIELD_DESCRIPTIONS.get("gui-file-filter", "")
            error_msg = f"Invalid value for 'gui-file-filter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_FILE_FILTER)}"
            error_msg += f"\n  → Example: gui-file-filter='{{ VALID_BODY_GUI_FILE_FILTER[0] }}'"
            return (False, error_msg)
    if "gui-application-control" in payload:
        value = payload["gui-application-control"]
        if value not in VALID_BODY_GUI_APPLICATION_CONTROL:
            desc = FIELD_DESCRIPTIONS.get("gui-application-control", "")
            error_msg = f"Invalid value for 'gui-application-control': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_APPLICATION_CONTROL)}"
            error_msg += f"\n  → Example: gui-application-control='{{ VALID_BODY_GUI_APPLICATION_CONTROL[0] }}'"
            return (False, error_msg)
    if "gui-ips" in payload:
        value = payload["gui-ips"]
        if value not in VALID_BODY_GUI_IPS:
            desc = FIELD_DESCRIPTIONS.get("gui-ips", "")
            error_msg = f"Invalid value for 'gui-ips': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_IPS)}"
            error_msg += f"\n  → Example: gui-ips='{{ VALID_BODY_GUI_IPS[0] }}'"
            return (False, error_msg)
    if "gui-dhcp-advanced" in payload:
        value = payload["gui-dhcp-advanced"]
        if value not in VALID_BODY_GUI_DHCP_ADVANCED:
            desc = FIELD_DESCRIPTIONS.get("gui-dhcp-advanced", "")
            error_msg = f"Invalid value for 'gui-dhcp-advanced': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DHCP_ADVANCED)}"
            error_msg += f"\n  → Example: gui-dhcp-advanced='{{ VALID_BODY_GUI_DHCP_ADVANCED[0] }}'"
            return (False, error_msg)
    if "gui-vpn" in payload:
        value = payload["gui-vpn"]
        if value not in VALID_BODY_GUI_VPN:
            desc = FIELD_DESCRIPTIONS.get("gui-vpn", "")
            error_msg = f"Invalid value for 'gui-vpn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_VPN)}"
            error_msg += f"\n  → Example: gui-vpn='{{ VALID_BODY_GUI_VPN[0] }}'"
            return (False, error_msg)
    if "gui-sslvpn" in payload:
        value = payload["gui-sslvpn"]
        if value not in VALID_BODY_GUI_SSLVPN:
            desc = FIELD_DESCRIPTIONS.get("gui-sslvpn", "")
            error_msg = f"Invalid value for 'gui-sslvpn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_SSLVPN)}"
            error_msg += f"\n  → Example: gui-sslvpn='{{ VALID_BODY_GUI_SSLVPN[0] }}'"
            return (False, error_msg)
    if "gui-wireless-controller" in payload:
        value = payload["gui-wireless-controller"]
        if value not in VALID_BODY_GUI_WIRELESS_CONTROLLER:
            desc = FIELD_DESCRIPTIONS.get("gui-wireless-controller", "")
            error_msg = f"Invalid value for 'gui-wireless-controller': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WIRELESS_CONTROLLER)}"
            error_msg += f"\n  → Example: gui-wireless-controller='{{ VALID_BODY_GUI_WIRELESS_CONTROLLER[0] }}'"
            return (False, error_msg)
    if "gui-advanced-wireless-features" in payload:
        value = payload["gui-advanced-wireless-features"]
        if value not in VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES:
            desc = FIELD_DESCRIPTIONS.get("gui-advanced-wireless-features", "")
            error_msg = f"Invalid value for 'gui-advanced-wireless-features': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES)}"
            error_msg += f"\n  → Example: gui-advanced-wireless-features='{{ VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES[0] }}'"
            return (False, error_msg)
    if "gui-switch-controller" in payload:
        value = payload["gui-switch-controller"]
        if value not in VALID_BODY_GUI_SWITCH_CONTROLLER:
            desc = FIELD_DESCRIPTIONS.get("gui-switch-controller", "")
            error_msg = f"Invalid value for 'gui-switch-controller': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_SWITCH_CONTROLLER)}"
            error_msg += f"\n  → Example: gui-switch-controller='{{ VALID_BODY_GUI_SWITCH_CONTROLLER[0] }}'"
            return (False, error_msg)
    if "gui-fortiap-split-tunneling" in payload:
        value = payload["gui-fortiap-split-tunneling"]
        if value not in VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING:
            desc = FIELD_DESCRIPTIONS.get("gui-fortiap-split-tunneling", "")
            error_msg = f"Invalid value for 'gui-fortiap-split-tunneling': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING)}"
            error_msg += f"\n  → Example: gui-fortiap-split-tunneling='{{ VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING[0] }}'"
            return (False, error_msg)
    if "gui-webfilter-advanced" in payload:
        value = payload["gui-webfilter-advanced"]
        if value not in VALID_BODY_GUI_WEBFILTER_ADVANCED:
            desc = FIELD_DESCRIPTIONS.get("gui-webfilter-advanced", "")
            error_msg = f"Invalid value for 'gui-webfilter-advanced': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WEBFILTER_ADVANCED)}"
            error_msg += f"\n  → Example: gui-webfilter-advanced='{{ VALID_BODY_GUI_WEBFILTER_ADVANCED[0] }}'"
            return (False, error_msg)
    if "gui-traffic-shaping" in payload:
        value = payload["gui-traffic-shaping"]
        if value not in VALID_BODY_GUI_TRAFFIC_SHAPING:
            desc = FIELD_DESCRIPTIONS.get("gui-traffic-shaping", "")
            error_msg = f"Invalid value for 'gui-traffic-shaping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_TRAFFIC_SHAPING)}"
            error_msg += f"\n  → Example: gui-traffic-shaping='{{ VALID_BODY_GUI_TRAFFIC_SHAPING[0] }}'"
            return (False, error_msg)
    if "gui-wan-load-balancing" in payload:
        value = payload["gui-wan-load-balancing"]
        if value not in VALID_BODY_GUI_WAN_LOAD_BALANCING:
            desc = FIELD_DESCRIPTIONS.get("gui-wan-load-balancing", "")
            error_msg = f"Invalid value for 'gui-wan-load-balancing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WAN_LOAD_BALANCING)}"
            error_msg += f"\n  → Example: gui-wan-load-balancing='{{ VALID_BODY_GUI_WAN_LOAD_BALANCING[0] }}'"
            return (False, error_msg)
    if "gui-antivirus" in payload:
        value = payload["gui-antivirus"]
        if value not in VALID_BODY_GUI_ANTIVIRUS:
            desc = FIELD_DESCRIPTIONS.get("gui-antivirus", "")
            error_msg = f"Invalid value for 'gui-antivirus': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ANTIVIRUS)}"
            error_msg += f"\n  → Example: gui-antivirus='{{ VALID_BODY_GUI_ANTIVIRUS[0] }}'"
            return (False, error_msg)
    if "gui-webfilter" in payload:
        value = payload["gui-webfilter"]
        if value not in VALID_BODY_GUI_WEBFILTER:
            desc = FIELD_DESCRIPTIONS.get("gui-webfilter", "")
            error_msg = f"Invalid value for 'gui-webfilter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WEBFILTER)}"
            error_msg += f"\n  → Example: gui-webfilter='{{ VALID_BODY_GUI_WEBFILTER[0] }}'"
            return (False, error_msg)
    if "gui-videofilter" in payload:
        value = payload["gui-videofilter"]
        if value not in VALID_BODY_GUI_VIDEOFILTER:
            desc = FIELD_DESCRIPTIONS.get("gui-videofilter", "")
            error_msg = f"Invalid value for 'gui-videofilter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_VIDEOFILTER)}"
            error_msg += f"\n  → Example: gui-videofilter='{{ VALID_BODY_GUI_VIDEOFILTER[0] }}'"
            return (False, error_msg)
    if "gui-dnsfilter" in payload:
        value = payload["gui-dnsfilter"]
        if value not in VALID_BODY_GUI_DNSFILTER:
            desc = FIELD_DESCRIPTIONS.get("gui-dnsfilter", "")
            error_msg = f"Invalid value for 'gui-dnsfilter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DNSFILTER)}"
            error_msg += f"\n  → Example: gui-dnsfilter='{{ VALID_BODY_GUI_DNSFILTER[0] }}'"
            return (False, error_msg)
    if "gui-waf-profile" in payload:
        value = payload["gui-waf-profile"]
        if value not in VALID_BODY_GUI_WAF_PROFILE:
            desc = FIELD_DESCRIPTIONS.get("gui-waf-profile", "")
            error_msg = f"Invalid value for 'gui-waf-profile': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WAF_PROFILE)}"
            error_msg += f"\n  → Example: gui-waf-profile='{{ VALID_BODY_GUI_WAF_PROFILE[0] }}'"
            return (False, error_msg)
    if "gui-dlp-profile" in payload:
        value = payload["gui-dlp-profile"]
        if value not in VALID_BODY_GUI_DLP_PROFILE:
            desc = FIELD_DESCRIPTIONS.get("gui-dlp-profile", "")
            error_msg = f"Invalid value for 'gui-dlp-profile': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DLP_PROFILE)}"
            error_msg += f"\n  → Example: gui-dlp-profile='{{ VALID_BODY_GUI_DLP_PROFILE[0] }}'"
            return (False, error_msg)
    if "gui-dlp-advanced" in payload:
        value = payload["gui-dlp-advanced"]
        if value not in VALID_BODY_GUI_DLP_ADVANCED:
            desc = FIELD_DESCRIPTIONS.get("gui-dlp-advanced", "")
            error_msg = f"Invalid value for 'gui-dlp-advanced': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DLP_ADVANCED)}"
            error_msg += f"\n  → Example: gui-dlp-advanced='{{ VALID_BODY_GUI_DLP_ADVANCED[0] }}'"
            return (False, error_msg)
    if "gui-virtual-patch-profile" in payload:
        value = payload["gui-virtual-patch-profile"]
        if value not in VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE:
            desc = FIELD_DESCRIPTIONS.get("gui-virtual-patch-profile", "")
            error_msg = f"Invalid value for 'gui-virtual-patch-profile': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE)}"
            error_msg += f"\n  → Example: gui-virtual-patch-profile='{{ VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE[0] }}'"
            return (False, error_msg)
    if "gui-casb" in payload:
        value = payload["gui-casb"]
        if value not in VALID_BODY_GUI_CASB:
            desc = FIELD_DESCRIPTIONS.get("gui-casb", "")
            error_msg = f"Invalid value for 'gui-casb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_CASB)}"
            error_msg += f"\n  → Example: gui-casb='{{ VALID_BODY_GUI_CASB[0] }}'"
            return (False, error_msg)
    if "gui-fortiextender-controller" in payload:
        value = payload["gui-fortiextender-controller"]
        if value not in VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER:
            desc = FIELD_DESCRIPTIONS.get("gui-fortiextender-controller", "")
            error_msg = f"Invalid value for 'gui-fortiextender-controller': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER)}"
            error_msg += f"\n  → Example: gui-fortiextender-controller='{{ VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER[0] }}'"
            return (False, error_msg)
    if "gui-advanced-policy" in payload:
        value = payload["gui-advanced-policy"]
        if value not in VALID_BODY_GUI_ADVANCED_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-advanced-policy", "")
            error_msg = f"Invalid value for 'gui-advanced-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ADVANCED_POLICY)}"
            error_msg += f"\n  → Example: gui-advanced-policy='{{ VALID_BODY_GUI_ADVANCED_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-allow-unnamed-policy" in payload:
        value = payload["gui-allow-unnamed-policy"]
        if value not in VALID_BODY_GUI_ALLOW_UNNAMED_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-allow-unnamed-policy", "")
            error_msg = f"Invalid value for 'gui-allow-unnamed-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ALLOW_UNNAMED_POLICY)}"
            error_msg += f"\n  → Example: gui-allow-unnamed-policy='{{ VALID_BODY_GUI_ALLOW_UNNAMED_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-email-collection" in payload:
        value = payload["gui-email-collection"]
        if value not in VALID_BODY_GUI_EMAIL_COLLECTION:
            desc = FIELD_DESCRIPTIONS.get("gui-email-collection", "")
            error_msg = f"Invalid value for 'gui-email-collection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_EMAIL_COLLECTION)}"
            error_msg += f"\n  → Example: gui-email-collection='{{ VALID_BODY_GUI_EMAIL_COLLECTION[0] }}'"
            return (False, error_msg)
    if "gui-multiple-interface-policy" in payload:
        value = payload["gui-multiple-interface-policy"]
        if value not in VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY:
            desc = FIELD_DESCRIPTIONS.get("gui-multiple-interface-policy", "")
            error_msg = f"Invalid value for 'gui-multiple-interface-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY)}"
            error_msg += f"\n  → Example: gui-multiple-interface-policy='{{ VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY[0] }}'"
            return (False, error_msg)
    if "gui-policy-disclaimer" in payload:
        value = payload["gui-policy-disclaimer"]
        if value not in VALID_BODY_GUI_POLICY_DISCLAIMER:
            desc = FIELD_DESCRIPTIONS.get("gui-policy-disclaimer", "")
            error_msg = f"Invalid value for 'gui-policy-disclaimer': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_POLICY_DISCLAIMER)}"
            error_msg += f"\n  → Example: gui-policy-disclaimer='{{ VALID_BODY_GUI_POLICY_DISCLAIMER[0] }}'"
            return (False, error_msg)
    if "gui-ztna" in payload:
        value = payload["gui-ztna"]
        if value not in VALID_BODY_GUI_ZTNA:
            desc = FIELD_DESCRIPTIONS.get("gui-ztna", "")
            error_msg = f"Invalid value for 'gui-ztna': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ZTNA)}"
            error_msg += f"\n  → Example: gui-ztna='{{ VALID_BODY_GUI_ZTNA[0] }}'"
            return (False, error_msg)
    if "gui-ot" in payload:
        value = payload["gui-ot"]
        if value not in VALID_BODY_GUI_OT:
            desc = FIELD_DESCRIPTIONS.get("gui-ot", "")
            error_msg = f"Invalid value for 'gui-ot': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_OT)}"
            error_msg += f"\n  → Example: gui-ot='{{ VALID_BODY_GUI_OT[0] }}'"
            return (False, error_msg)
    if "gui-dynamic-device-os-id" in payload:
        value = payload["gui-dynamic-device-os-id"]
        if value not in VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID:
            desc = FIELD_DESCRIPTIONS.get("gui-dynamic-device-os-id", "")
            error_msg = f"Invalid value for 'gui-dynamic-device-os-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID)}"
            error_msg += f"\n  → Example: gui-dynamic-device-os-id='{{ VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID[0] }}'"
            return (False, error_msg)
    if "gui-gtp" in payload:
        value = payload["gui-gtp"]
        if value not in VALID_BODY_GUI_GTP:
            desc = FIELD_DESCRIPTIONS.get("gui-gtp", "")
            error_msg = f"Invalid value for 'gui-gtp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_GTP)}"
            error_msg += f"\n  → Example: gui-gtp='{{ VALID_BODY_GUI_GTP[0] }}'"
            return (False, error_msg)
    if "ike-session-resume" in payload:
        value = payload["ike-session-resume"]
        if value not in VALID_BODY_IKE_SESSION_RESUME:
            desc = FIELD_DESCRIPTIONS.get("ike-session-resume", "")
            error_msg = f"Invalid value for 'ike-session-resume': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_SESSION_RESUME)}"
            error_msg += f"\n  → Example: ike-session-resume='{{ VALID_BODY_IKE_SESSION_RESUME[0] }}'"
            return (False, error_msg)
    if "ike-quick-crash-detect" in payload:
        value = payload["ike-quick-crash-detect"]
        if value not in VALID_BODY_IKE_QUICK_CRASH_DETECT:
            desc = FIELD_DESCRIPTIONS.get("ike-quick-crash-detect", "")
            error_msg = f"Invalid value for 'ike-quick-crash-detect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_QUICK_CRASH_DETECT)}"
            error_msg += f"\n  → Example: ike-quick-crash-detect='{{ VALID_BODY_IKE_QUICK_CRASH_DETECT[0] }}'"
            return (False, error_msg)
    if "ike-dn-format" in payload:
        value = payload["ike-dn-format"]
        if value not in VALID_BODY_IKE_DN_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("ike-dn-format", "")
            error_msg = f"Invalid value for 'ike-dn-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_DN_FORMAT)}"
            error_msg += f"\n  → Example: ike-dn-format='{{ VALID_BODY_IKE_DN_FORMAT[0] }}'"
            return (False, error_msg)
    if "ike-policy-route" in payload:
        value = payload["ike-policy-route"]
        if value not in VALID_BODY_IKE_POLICY_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("ike-policy-route", "")
            error_msg = f"Invalid value for 'ike-policy-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_POLICY_ROUTE)}"
            error_msg += f"\n  → Example: ike-policy-route='{{ VALID_BODY_IKE_POLICY_ROUTE[0] }}'"
            return (False, error_msg)
    if "ike-detailed-event-logs" in payload:
        value = payload["ike-detailed-event-logs"]
        if value not in VALID_BODY_IKE_DETAILED_EVENT_LOGS:
            desc = FIELD_DESCRIPTIONS.get("ike-detailed-event-logs", "")
            error_msg = f"Invalid value for 'ike-detailed-event-logs': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_DETAILED_EVENT_LOGS)}"
            error_msg += f"\n  → Example: ike-detailed-event-logs='{{ VALID_BODY_IKE_DETAILED_EVENT_LOGS[0] }}'"
            return (False, error_msg)
    if "block-land-attack" in payload:
        value = payload["block-land-attack"]
        if value not in VALID_BODY_BLOCK_LAND_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("block-land-attack", "")
            error_msg = f"Invalid value for 'block-land-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCK_LAND_ATTACK)}"
            error_msg += f"\n  → Example: block-land-attack='{{ VALID_BODY_BLOCK_LAND_ATTACK[0] }}'"
            return (False, error_msg)
    if "default-app-port-as-service" in payload:
        value = payload["default-app-port-as-service"]
        if value not in VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("default-app-port-as-service", "")
            error_msg = f"Invalid value for 'default-app-port-as-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE)}"
            error_msg += f"\n  → Example: default-app-port-as-service='{{ VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE[0] }}'"
            return (False, error_msg)
    if "fqdn-session-check" in payload:
        value = payload["fqdn-session-check"]
        if value not in VALID_BODY_FQDN_SESSION_CHECK:
            desc = FIELD_DESCRIPTIONS.get("fqdn-session-check", "")
            error_msg = f"Invalid value for 'fqdn-session-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FQDN_SESSION_CHECK)}"
            error_msg += f"\n  → Example: fqdn-session-check='{{ VALID_BODY_FQDN_SESSION_CHECK[0] }}'"
            return (False, error_msg)
    if "ext-resource-session-check" in payload:
        value = payload["ext-resource-session-check"]
        if value not in VALID_BODY_EXT_RESOURCE_SESSION_CHECK:
            desc = FIELD_DESCRIPTIONS.get("ext-resource-session-check", "")
            error_msg = f"Invalid value for 'ext-resource-session-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXT_RESOURCE_SESSION_CHECK)}"
            error_msg += f"\n  → Example: ext-resource-session-check='{{ VALID_BODY_EXT_RESOURCE_SESSION_CHECK[0] }}'"
            return (False, error_msg)
    if "dyn-addr-session-check" in payload:
        value = payload["dyn-addr-session-check"]
        if value not in VALID_BODY_DYN_ADDR_SESSION_CHECK:
            desc = FIELD_DESCRIPTIONS.get("dyn-addr-session-check", "")
            error_msg = f"Invalid value for 'dyn-addr-session-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYN_ADDR_SESSION_CHECK)}"
            error_msg += f"\n  → Example: dyn-addr-session-check='{{ VALID_BODY_DYN_ADDR_SESSION_CHECK[0] }}'"
            return (False, error_msg)
    if "gui-enforce-change-summary" in payload:
        value = payload["gui-enforce-change-summary"]
        if value not in VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY:
            desc = FIELD_DESCRIPTIONS.get("gui-enforce-change-summary", "")
            error_msg = f"Invalid value for 'gui-enforce-change-summary': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY)}"
            error_msg += f"\n  → Example: gui-enforce-change-summary='{{ VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY[0] }}'"
            return (False, error_msg)
    if "internet-service-database-cache" in payload:
        value = payload["internet-service-database-cache"]
        if value not in VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE:
            desc = FIELD_DESCRIPTIONS.get("internet-service-database-cache", "")
            error_msg = f"Invalid value for 'internet-service-database-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE)}"
            error_msg += f"\n  → Example: internet-service-database-cache='{{ VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_settings_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/settings.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_settings_put(payload)
    """
    # Step 1: Validate enum values
    if "vdom-type" in payload:
        value = payload["vdom-type"]
        if value not in VALID_BODY_VDOM_TYPE:
            return (
                False,
                f"Invalid value for 'vdom-type'='{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_TYPE)}",
            )
    if "opmode" in payload:
        value = payload["opmode"]
        if value not in VALID_BODY_OPMODE:
            return (
                False,
                f"Invalid value for 'opmode'='{value}'. Must be one of: {', '.join(VALID_BODY_OPMODE)}",
            )
    if "ngfw-mode" in payload:
        value = payload["ngfw-mode"]
        if value not in VALID_BODY_NGFW_MODE:
            return (
                False,
                f"Invalid value for 'ngfw-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_NGFW_MODE)}",
            )
    if "http-external-dest" in payload:
        value = payload["http-external-dest"]
        if value not in VALID_BODY_HTTP_EXTERNAL_DEST:
            return (
                False,
                f"Invalid value for 'http-external-dest'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_EXTERNAL_DEST)}",
            )
    if "firewall-session-dirty" in payload:
        value = payload["firewall-session-dirty"]
        if value not in VALID_BODY_FIREWALL_SESSION_DIRTY:
            return (
                False,
                f"Invalid value for 'firewall-session-dirty'='{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_SESSION_DIRTY)}",
            )
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid value for 'bfd'='{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )
    if "bfd-dont-enforce-src-port" in payload:
        value = payload["bfd-dont-enforce-src-port"]
        if value not in VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT:
            return (
                False,
                f"Invalid value for 'bfd-dont-enforce-src-port'='{value}'. Must be one of: {', '.join(VALID_BODY_BFD_DONT_ENFORCE_SRC_PORT)}",
            )
    if "utf8-spam-tagging" in payload:
        value = payload["utf8-spam-tagging"]
        if value not in VALID_BODY_UTF8_SPAM_TAGGING:
            return (
                False,
                f"Invalid value for 'utf8-spam-tagging'='{value}'. Must be one of: {', '.join(VALID_BODY_UTF8_SPAM_TAGGING)}",
            )
    if "wccp-cache-engine" in payload:
        value = payload["wccp-cache-engine"]
        if value not in VALID_BODY_WCCP_CACHE_ENGINE:
            return (
                False,
                f"Invalid value for 'wccp-cache-engine'='{value}'. Must be one of: {', '.join(VALID_BODY_WCCP_CACHE_ENGINE)}",
            )
    if "vpn-stats-log" in payload:
        value = payload["vpn-stats-log"]
        if value not in VALID_BODY_VPN_STATS_LOG:
            return (
                False,
                f"Invalid value for 'vpn-stats-log'='{value}'. Must be one of: {', '.join(VALID_BODY_VPN_STATS_LOG)}",
            )
    if "v4-ecmp-mode" in payload:
        value = payload["v4-ecmp-mode"]
        if value not in VALID_BODY_V4_ECMP_MODE:
            return (
                False,
                f"Invalid value for 'v4-ecmp-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_V4_ECMP_MODE)}",
            )
    if "fw-session-hairpin" in payload:
        value = payload["fw-session-hairpin"]
        if value not in VALID_BODY_FW_SESSION_HAIRPIN:
            return (
                False,
                f"Invalid value for 'fw-session-hairpin'='{value}'. Must be one of: {', '.join(VALID_BODY_FW_SESSION_HAIRPIN)}",
            )
    if "prp-trailer-action" in payload:
        value = payload["prp-trailer-action"]
        if value not in VALID_BODY_PRP_TRAILER_ACTION:
            return (
                False,
                f"Invalid value for 'prp-trailer-action'='{value}'. Must be one of: {', '.join(VALID_BODY_PRP_TRAILER_ACTION)}",
            )
    if "snat-hairpin-traffic" in payload:
        value = payload["snat-hairpin-traffic"]
        if value not in VALID_BODY_SNAT_HAIRPIN_TRAFFIC:
            return (
                False,
                f"Invalid value for 'snat-hairpin-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_SNAT_HAIRPIN_TRAFFIC)}",
            )
    if "dhcp-proxy" in payload:
        value = payload["dhcp-proxy"]
        if value not in VALID_BODY_DHCP_PROXY:
            return (
                False,
                f"Invalid value for 'dhcp-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_PROXY)}",
            )
    if "dhcp-proxy-interface-select-method" in payload:
        value = payload["dhcp-proxy-interface-select-method"]
        if value not in VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'dhcp-proxy-interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_PROXY_INTERFACE_SELECT_METHOD)}",
            )
    if "central-nat" in payload:
        value = payload["central-nat"]
        if value not in VALID_BODY_CENTRAL_NAT:
            return (
                False,
                f"Invalid value for 'central-nat'='{value}'. Must be one of: {', '.join(VALID_BODY_CENTRAL_NAT)}",
            )
    if "lldp-reception" in payload:
        value = payload["lldp-reception"]
        if value not in VALID_BODY_LLDP_RECEPTION:
            return (
                False,
                f"Invalid value for 'lldp-reception'='{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_RECEPTION)}",
            )
    if "lldp-transmission" in payload:
        value = payload["lldp-transmission"]
        if value not in VALID_BODY_LLDP_TRANSMISSION:
            return (
                False,
                f"Invalid value for 'lldp-transmission'='{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_TRANSMISSION)}",
            )
    if "link-down-access" in payload:
        value = payload["link-down-access"]
        if value not in VALID_BODY_LINK_DOWN_ACCESS:
            return (
                False,
                f"Invalid value for 'link-down-access'='{value}'. Must be one of: {', '.join(VALID_BODY_LINK_DOWN_ACCESS)}",
            )
    if "nat46-generate-ipv6-fragment-header" in payload:
        value = payload["nat46-generate-ipv6-fragment-header"]
        if value not in VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER:
            return (
                False,
                f"Invalid value for 'nat46-generate-ipv6-fragment-header'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46_GENERATE_IPV6_FRAGMENT_HEADER)}",
            )
    if "nat46-force-ipv4-packet-forwarding" in payload:
        value = payload["nat46-force-ipv4-packet-forwarding"]
        if value not in VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING:
            return (
                False,
                f"Invalid value for 'nat46-force-ipv4-packet-forwarding'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46_FORCE_IPV4_PACKET_FORWARDING)}",
            )
    if "nat64-force-ipv6-packet-forwarding" in payload:
        value = payload["nat64-force-ipv6-packet-forwarding"]
        if value not in VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING:
            return (
                False,
                f"Invalid value for 'nat64-force-ipv6-packet-forwarding'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT64_FORCE_IPV6_PACKET_FORWARDING)}",
            )
    if "detect-unknown-esp" in payload:
        value = payload["detect-unknown-esp"]
        if value not in VALID_BODY_DETECT_UNKNOWN_ESP:
            return (
                False,
                f"Invalid value for 'detect-unknown-esp'='{value}'. Must be one of: {', '.join(VALID_BODY_DETECT_UNKNOWN_ESP)}",
            )
    if "intree-ses-best-route" in payload:
        value = payload["intree-ses-best-route"]
        if value not in VALID_BODY_INTREE_SES_BEST_ROUTE:
            return (
                False,
                f"Invalid value for 'intree-ses-best-route'='{value}'. Must be one of: {', '.join(VALID_BODY_INTREE_SES_BEST_ROUTE)}",
            )
    if "auxiliary-session" in payload:
        value = payload["auxiliary-session"]
        if value not in VALID_BODY_AUXILIARY_SESSION:
            return (
                False,
                f"Invalid value for 'auxiliary-session'='{value}'. Must be one of: {', '.join(VALID_BODY_AUXILIARY_SESSION)}",
            )
    if "asymroute" in payload:
        value = payload["asymroute"]
        if value not in VALID_BODY_ASYMROUTE:
            return (
                False,
                f"Invalid value for 'asymroute'='{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE)}",
            )
    if "asymroute-icmp" in payload:
        value = payload["asymroute-icmp"]
        if value not in VALID_BODY_ASYMROUTE_ICMP:
            return (
                False,
                f"Invalid value for 'asymroute-icmp'='{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE_ICMP)}",
            )
    if "tcp-session-without-syn" in payload:
        value = payload["tcp-session-without-syn"]
        if value not in VALID_BODY_TCP_SESSION_WITHOUT_SYN:
            return (
                False,
                f"Invalid value for 'tcp-session-without-syn'='{value}'. Must be one of: {', '.join(VALID_BODY_TCP_SESSION_WITHOUT_SYN)}",
            )
    if "ses-denied-traffic" in payload:
        value = payload["ses-denied-traffic"]
        if value not in VALID_BODY_SES_DENIED_TRAFFIC:
            return (
                False,
                f"Invalid value for 'ses-denied-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_SES_DENIED_TRAFFIC)}",
            )
    if "ses-denied-multicast-traffic" in payload:
        value = payload["ses-denied-multicast-traffic"]
        if value not in VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC:
            return (
                False,
                f"Invalid value for 'ses-denied-multicast-traffic'='{value}'. Must be one of: {', '.join(VALID_BODY_SES_DENIED_MULTICAST_TRAFFIC)}",
            )
    if "strict-src-check" in payload:
        value = payload["strict-src-check"]
        if value not in VALID_BODY_STRICT_SRC_CHECK:
            return (
                False,
                f"Invalid value for 'strict-src-check'='{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_SRC_CHECK)}",
            )
    if "allow-linkdown-path" in payload:
        value = payload["allow-linkdown-path"]
        if value not in VALID_BODY_ALLOW_LINKDOWN_PATH:
            return (
                False,
                f"Invalid value for 'allow-linkdown-path'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_LINKDOWN_PATH)}",
            )
    if "asymroute6" in payload:
        value = payload["asymroute6"]
        if value not in VALID_BODY_ASYMROUTE6:
            return (
                False,
                f"Invalid value for 'asymroute6'='{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE6)}",
            )
    if "asymroute6-icmp" in payload:
        value = payload["asymroute6-icmp"]
        if value not in VALID_BODY_ASYMROUTE6_ICMP:
            return (
                False,
                f"Invalid value for 'asymroute6-icmp'='{value}'. Must be one of: {', '.join(VALID_BODY_ASYMROUTE6_ICMP)}",
            )
    if "sctp-session-without-init" in payload:
        value = payload["sctp-session-without-init"]
        if value not in VALID_BODY_SCTP_SESSION_WITHOUT_INIT:
            return (
                False,
                f"Invalid value for 'sctp-session-without-init'='{value}'. Must be one of: {', '.join(VALID_BODY_SCTP_SESSION_WITHOUT_INIT)}",
            )
    if "sip-expectation" in payload:
        value = payload["sip-expectation"]
        if value not in VALID_BODY_SIP_EXPECTATION:
            return (
                False,
                f"Invalid value for 'sip-expectation'='{value}'. Must be one of: {', '.join(VALID_BODY_SIP_EXPECTATION)}",
            )
    if "sip-nat-trace" in payload:
        value = payload["sip-nat-trace"]
        if value not in VALID_BODY_SIP_NAT_TRACE:
            return (
                False,
                f"Invalid value for 'sip-nat-trace'='{value}'. Must be one of: {', '.join(VALID_BODY_SIP_NAT_TRACE)}",
            )
    if "h323-direct-model" in payload:
        value = payload["h323-direct-model"]
        if value not in VALID_BODY_H323_DIRECT_MODEL:
            return (
                False,
                f"Invalid value for 'h323-direct-model'='{value}'. Must be one of: {', '.join(VALID_BODY_H323_DIRECT_MODEL)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "multicast-forward" in payload:
        value = payload["multicast-forward"]
        if value not in VALID_BODY_MULTICAST_FORWARD:
            return (
                False,
                f"Invalid value for 'multicast-forward'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_FORWARD)}",
            )
    if "multicast-ttl-notchange" in payload:
        value = payload["multicast-ttl-notchange"]
        if value not in VALID_BODY_MULTICAST_TTL_NOTCHANGE:
            return (
                False,
                f"Invalid value for 'multicast-ttl-notchange'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_TTL_NOTCHANGE)}",
            )
    if "multicast-skip-policy" in payload:
        value = payload["multicast-skip-policy"]
        if value not in VALID_BODY_MULTICAST_SKIP_POLICY:
            return (
                False,
                f"Invalid value for 'multicast-skip-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_SKIP_POLICY)}",
            )
    if "allow-subnet-overlap" in payload:
        value = payload["allow-subnet-overlap"]
        if value not in VALID_BODY_ALLOW_SUBNET_OVERLAP:
            return (
                False,
                f"Invalid value for 'allow-subnet-overlap'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_SUBNET_OVERLAP)}",
            )
    if "deny-tcp-with-icmp" in payload:
        value = payload["deny-tcp-with-icmp"]
        if value not in VALID_BODY_DENY_TCP_WITH_ICMP:
            return (
                False,
                f"Invalid value for 'deny-tcp-with-icmp'='{value}'. Must be one of: {', '.join(VALID_BODY_DENY_TCP_WITH_ICMP)}",
            )
    if "email-portal-check-dns" in payload:
        value = payload["email-portal-check-dns"]
        if value not in VALID_BODY_EMAIL_PORTAL_CHECK_DNS:
            return (
                False,
                f"Invalid value for 'email-portal-check-dns'='{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_PORTAL_CHECK_DNS)}",
            )
    if "default-voip-alg-mode" in payload:
        value = payload["default-voip-alg-mode"]
        if value not in VALID_BODY_DEFAULT_VOIP_ALG_MODE:
            return (
                False,
                f"Invalid value for 'default-voip-alg-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_VOIP_ALG_MODE)}",
            )
    if "gui-icap" in payload:
        value = payload["gui-icap"]
        if value not in VALID_BODY_GUI_ICAP:
            return (
                False,
                f"Invalid value for 'gui-icap'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ICAP)}",
            )
    if "gui-implicit-policy" in payload:
        value = payload["gui-implicit-policy"]
        if value not in VALID_BODY_GUI_IMPLICIT_POLICY:
            return (
                False,
                f"Invalid value for 'gui-implicit-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_IMPLICIT_POLICY)}",
            )
    if "gui-dns-database" in payload:
        value = payload["gui-dns-database"]
        if value not in VALID_BODY_GUI_DNS_DATABASE:
            return (
                False,
                f"Invalid value for 'gui-dns-database'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DNS_DATABASE)}",
            )
    if "gui-load-balance" in payload:
        value = payload["gui-load-balance"]
        if value not in VALID_BODY_GUI_LOAD_BALANCE:
            return (
                False,
                f"Invalid value for 'gui-load-balance'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_LOAD_BALANCE)}",
            )
    if "gui-multicast-policy" in payload:
        value = payload["gui-multicast-policy"]
        if value not in VALID_BODY_GUI_MULTICAST_POLICY:
            return (
                False,
                f"Invalid value for 'gui-multicast-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_MULTICAST_POLICY)}",
            )
    if "gui-dos-policy" in payload:
        value = payload["gui-dos-policy"]
        if value not in VALID_BODY_GUI_DOS_POLICY:
            return (
                False,
                f"Invalid value for 'gui-dos-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DOS_POLICY)}",
            )
    if "gui-object-colors" in payload:
        value = payload["gui-object-colors"]
        if value not in VALID_BODY_GUI_OBJECT_COLORS:
            return (
                False,
                f"Invalid value for 'gui-object-colors'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_OBJECT_COLORS)}",
            )
    if "gui-route-tag-address-creation" in payload:
        value = payload["gui-route-tag-address-creation"]
        if value not in VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION:
            return (
                False,
                f"Invalid value for 'gui-route-tag-address-creation'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ROUTE_TAG_ADDRESS_CREATION)}",
            )
    if "gui-voip-profile" in payload:
        value = payload["gui-voip-profile"]
        if value not in VALID_BODY_GUI_VOIP_PROFILE:
            return (
                False,
                f"Invalid value for 'gui-voip-profile'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VOIP_PROFILE)}",
            )
    if "gui-ap-profile" in payload:
        value = payload["gui-ap-profile"]
        if value not in VALID_BODY_GUI_AP_PROFILE:
            return (
                False,
                f"Invalid value for 'gui-ap-profile'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_AP_PROFILE)}",
            )
    if "gui-security-profile-group" in payload:
        value = payload["gui-security-profile-group"]
        if value not in VALID_BODY_GUI_SECURITY_PROFILE_GROUP:
            return (
                False,
                f"Invalid value for 'gui-security-profile-group'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SECURITY_PROFILE_GROUP)}",
            )
    if "gui-local-in-policy" in payload:
        value = payload["gui-local-in-policy"]
        if value not in VALID_BODY_GUI_LOCAL_IN_POLICY:
            return (
                False,
                f"Invalid value for 'gui-local-in-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_LOCAL_IN_POLICY)}",
            )
    if "gui-wanopt-cache" in payload:
        value = payload["gui-wanopt-cache"]
        if value not in VALID_BODY_GUI_WANOPT_CACHE:
            return (
                False,
                f"Invalid value for 'gui-wanopt-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WANOPT_CACHE)}",
            )
    if "gui-explicit-proxy" in payload:
        value = payload["gui-explicit-proxy"]
        if value not in VALID_BODY_GUI_EXPLICIT_PROXY:
            return (
                False,
                f"Invalid value for 'gui-explicit-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_EXPLICIT_PROXY)}",
            )
    if "gui-dynamic-routing" in payload:
        value = payload["gui-dynamic-routing"]
        if value not in VALID_BODY_GUI_DYNAMIC_ROUTING:
            return (
                False,
                f"Invalid value for 'gui-dynamic-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DYNAMIC_ROUTING)}",
            )
    if "gui-sslvpn-personal-bookmarks" in payload:
        value = payload["gui-sslvpn-personal-bookmarks"]
        if value not in VALID_BODY_GUI_SSLVPN_PERSONAL_BOOKMARKS:
            return (
                False,
                f"Invalid value for 'gui-sslvpn-personal-bookmarks'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SSLVPN_PERSONAL_BOOKMARKS)}",
            )
    if "gui-sslvpn-realms" in payload:
        value = payload["gui-sslvpn-realms"]
        if value not in VALID_BODY_GUI_SSLVPN_REALMS:
            return (
                False,
                f"Invalid value for 'gui-sslvpn-realms'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SSLVPN_REALMS)}",
            )
    if "gui-policy-based-ipsec" in payload:
        value = payload["gui-policy-based-ipsec"]
        if value not in VALID_BODY_GUI_POLICY_BASED_IPSEC:
            return (
                False,
                f"Invalid value for 'gui-policy-based-ipsec'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_POLICY_BASED_IPSEC)}",
            )
    if "gui-threat-weight" in payload:
        value = payload["gui-threat-weight"]
        if value not in VALID_BODY_GUI_THREAT_WEIGHT:
            return (
                False,
                f"Invalid value for 'gui-threat-weight'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_THREAT_WEIGHT)}",
            )
    if "gui-spamfilter" in payload:
        value = payload["gui-spamfilter"]
        if value not in VALID_BODY_GUI_SPAMFILTER:
            return (
                False,
                f"Invalid value for 'gui-spamfilter'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SPAMFILTER)}",
            )
    if "gui-file-filter" in payload:
        value = payload["gui-file-filter"]
        if value not in VALID_BODY_GUI_FILE_FILTER:
            return (
                False,
                f"Invalid value for 'gui-file-filter'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FILE_FILTER)}",
            )
    if "gui-application-control" in payload:
        value = payload["gui-application-control"]
        if value not in VALID_BODY_GUI_APPLICATION_CONTROL:
            return (
                False,
                f"Invalid value for 'gui-application-control'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_APPLICATION_CONTROL)}",
            )
    if "gui-ips" in payload:
        value = payload["gui-ips"]
        if value not in VALID_BODY_GUI_IPS:
            return (
                False,
                f"Invalid value for 'gui-ips'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_IPS)}",
            )
    if "gui-dhcp-advanced" in payload:
        value = payload["gui-dhcp-advanced"]
        if value not in VALID_BODY_GUI_DHCP_ADVANCED:
            return (
                False,
                f"Invalid value for 'gui-dhcp-advanced'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DHCP_ADVANCED)}",
            )
    if "gui-vpn" in payload:
        value = payload["gui-vpn"]
        if value not in VALID_BODY_GUI_VPN:
            return (
                False,
                f"Invalid value for 'gui-vpn'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VPN)}",
            )
    if "gui-sslvpn" in payload:
        value = payload["gui-sslvpn"]
        if value not in VALID_BODY_GUI_SSLVPN:
            return (
                False,
                f"Invalid value for 'gui-sslvpn'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SSLVPN)}",
            )
    if "gui-wireless-controller" in payload:
        value = payload["gui-wireless-controller"]
        if value not in VALID_BODY_GUI_WIRELESS_CONTROLLER:
            return (
                False,
                f"Invalid value for 'gui-wireless-controller'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WIRELESS_CONTROLLER)}",
            )
    if "gui-advanced-wireless-features" in payload:
        value = payload["gui-advanced-wireless-features"]
        if value not in VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES:
            return (
                False,
                f"Invalid value for 'gui-advanced-wireless-features'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ADVANCED_WIRELESS_FEATURES)}",
            )
    if "gui-switch-controller" in payload:
        value = payload["gui-switch-controller"]
        if value not in VALID_BODY_GUI_SWITCH_CONTROLLER:
            return (
                False,
                f"Invalid value for 'gui-switch-controller'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_SWITCH_CONTROLLER)}",
            )
    if "gui-fortiap-split-tunneling" in payload:
        value = payload["gui-fortiap-split-tunneling"]
        if value not in VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING:
            return (
                False,
                f"Invalid value for 'gui-fortiap-split-tunneling'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTIAP_SPLIT_TUNNELING)}",
            )
    if "gui-webfilter-advanced" in payload:
        value = payload["gui-webfilter-advanced"]
        if value not in VALID_BODY_GUI_WEBFILTER_ADVANCED:
            return (
                False,
                f"Invalid value for 'gui-webfilter-advanced'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WEBFILTER_ADVANCED)}",
            )
    if "gui-traffic-shaping" in payload:
        value = payload["gui-traffic-shaping"]
        if value not in VALID_BODY_GUI_TRAFFIC_SHAPING:
            return (
                False,
                f"Invalid value for 'gui-traffic-shaping'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_TRAFFIC_SHAPING)}",
            )
    if "gui-wan-load-balancing" in payload:
        value = payload["gui-wan-load-balancing"]
        if value not in VALID_BODY_GUI_WAN_LOAD_BALANCING:
            return (
                False,
                f"Invalid value for 'gui-wan-load-balancing'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WAN_LOAD_BALANCING)}",
            )
    if "gui-antivirus" in payload:
        value = payload["gui-antivirus"]
        if value not in VALID_BODY_GUI_ANTIVIRUS:
            return (
                False,
                f"Invalid value for 'gui-antivirus'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ANTIVIRUS)}",
            )
    if "gui-webfilter" in payload:
        value = payload["gui-webfilter"]
        if value not in VALID_BODY_GUI_WEBFILTER:
            return (
                False,
                f"Invalid value for 'gui-webfilter'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WEBFILTER)}",
            )
    if "gui-videofilter" in payload:
        value = payload["gui-videofilter"]
        if value not in VALID_BODY_GUI_VIDEOFILTER:
            return (
                False,
                f"Invalid value for 'gui-videofilter'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VIDEOFILTER)}",
            )
    if "gui-dnsfilter" in payload:
        value = payload["gui-dnsfilter"]
        if value not in VALID_BODY_GUI_DNSFILTER:
            return (
                False,
                f"Invalid value for 'gui-dnsfilter'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DNSFILTER)}",
            )
    if "gui-waf-profile" in payload:
        value = payload["gui-waf-profile"]
        if value not in VALID_BODY_GUI_WAF_PROFILE:
            return (
                False,
                f"Invalid value for 'gui-waf-profile'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WAF_PROFILE)}",
            )
    if "gui-dlp-profile" in payload:
        value = payload["gui-dlp-profile"]
        if value not in VALID_BODY_GUI_DLP_PROFILE:
            return (
                False,
                f"Invalid value for 'gui-dlp-profile'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DLP_PROFILE)}",
            )
    if "gui-dlp-advanced" in payload:
        value = payload["gui-dlp-advanced"]
        if value not in VALID_BODY_GUI_DLP_ADVANCED:
            return (
                False,
                f"Invalid value for 'gui-dlp-advanced'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DLP_ADVANCED)}",
            )
    if "gui-virtual-patch-profile" in payload:
        value = payload["gui-virtual-patch-profile"]
        if value not in VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE:
            return (
                False,
                f"Invalid value for 'gui-virtual-patch-profile'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_VIRTUAL_PATCH_PROFILE)}",
            )
    if "gui-casb" in payload:
        value = payload["gui-casb"]
        if value not in VALID_BODY_GUI_CASB:
            return (
                False,
                f"Invalid value for 'gui-casb'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CASB)}",
            )
    if "gui-fortiextender-controller" in payload:
        value = payload["gui-fortiextender-controller"]
        if value not in VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER:
            return (
                False,
                f"Invalid value for 'gui-fortiextender-controller'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTIEXTENDER_CONTROLLER)}",
            )
    if "gui-advanced-policy" in payload:
        value = payload["gui-advanced-policy"]
        if value not in VALID_BODY_GUI_ADVANCED_POLICY:
            return (
                False,
                f"Invalid value for 'gui-advanced-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ADVANCED_POLICY)}",
            )
    if "gui-allow-unnamed-policy" in payload:
        value = payload["gui-allow-unnamed-policy"]
        if value not in VALID_BODY_GUI_ALLOW_UNNAMED_POLICY:
            return (
                False,
                f"Invalid value for 'gui-allow-unnamed-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ALLOW_UNNAMED_POLICY)}",
            )
    if "gui-email-collection" in payload:
        value = payload["gui-email-collection"]
        if value not in VALID_BODY_GUI_EMAIL_COLLECTION:
            return (
                False,
                f"Invalid value for 'gui-email-collection'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_EMAIL_COLLECTION)}",
            )
    if "gui-multiple-interface-policy" in payload:
        value = payload["gui-multiple-interface-policy"]
        if value not in VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY:
            return (
                False,
                f"Invalid value for 'gui-multiple-interface-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_MULTIPLE_INTERFACE_POLICY)}",
            )
    if "gui-policy-disclaimer" in payload:
        value = payload["gui-policy-disclaimer"]
        if value not in VALID_BODY_GUI_POLICY_DISCLAIMER:
            return (
                False,
                f"Invalid value for 'gui-policy-disclaimer'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_POLICY_DISCLAIMER)}",
            )
    if "gui-ztna" in payload:
        value = payload["gui-ztna"]
        if value not in VALID_BODY_GUI_ZTNA:
            return (
                False,
                f"Invalid value for 'gui-ztna'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ZTNA)}",
            )
    if "gui-ot" in payload:
        value = payload["gui-ot"]
        if value not in VALID_BODY_GUI_OT:
            return (
                False,
                f"Invalid value for 'gui-ot'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_OT)}",
            )
    if "gui-dynamic-device-os-id" in payload:
        value = payload["gui-dynamic-device-os-id"]
        if value not in VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID:
            return (
                False,
                f"Invalid value for 'gui-dynamic-device-os-id'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DYNAMIC_DEVICE_OS_ID)}",
            )
    if "gui-gtp" in payload:
        value = payload["gui-gtp"]
        if value not in VALID_BODY_GUI_GTP:
            return (
                False,
                f"Invalid value for 'gui-gtp'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_GTP)}",
            )
    if "ike-session-resume" in payload:
        value = payload["ike-session-resume"]
        if value not in VALID_BODY_IKE_SESSION_RESUME:
            return (
                False,
                f"Invalid value for 'ike-session-resume'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_SESSION_RESUME)}",
            )
    if "ike-quick-crash-detect" in payload:
        value = payload["ike-quick-crash-detect"]
        if value not in VALID_BODY_IKE_QUICK_CRASH_DETECT:
            return (
                False,
                f"Invalid value for 'ike-quick-crash-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_QUICK_CRASH_DETECT)}",
            )
    if "ike-dn-format" in payload:
        value = payload["ike-dn-format"]
        if value not in VALID_BODY_IKE_DN_FORMAT:
            return (
                False,
                f"Invalid value for 'ike-dn-format'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_DN_FORMAT)}",
            )
    if "ike-policy-route" in payload:
        value = payload["ike-policy-route"]
        if value not in VALID_BODY_IKE_POLICY_ROUTE:
            return (
                False,
                f"Invalid value for 'ike-policy-route'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_POLICY_ROUTE)}",
            )
    if "ike-detailed-event-logs" in payload:
        value = payload["ike-detailed-event-logs"]
        if value not in VALID_BODY_IKE_DETAILED_EVENT_LOGS:
            return (
                False,
                f"Invalid value for 'ike-detailed-event-logs'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_DETAILED_EVENT_LOGS)}",
            )
    if "block-land-attack" in payload:
        value = payload["block-land-attack"]
        if value not in VALID_BODY_BLOCK_LAND_ATTACK:
            return (
                False,
                f"Invalid value for 'block-land-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_LAND_ATTACK)}",
            )
    if "default-app-port-as-service" in payload:
        value = payload["default-app-port-as-service"]
        if value not in VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE:
            return (
                False,
                f"Invalid value for 'default-app-port-as-service'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_APP_PORT_AS_SERVICE)}",
            )
    if "fqdn-session-check" in payload:
        value = payload["fqdn-session-check"]
        if value not in VALID_BODY_FQDN_SESSION_CHECK:
            return (
                False,
                f"Invalid value for 'fqdn-session-check'='{value}'. Must be one of: {', '.join(VALID_BODY_FQDN_SESSION_CHECK)}",
            )
    if "ext-resource-session-check" in payload:
        value = payload["ext-resource-session-check"]
        if value not in VALID_BODY_EXT_RESOURCE_SESSION_CHECK:
            return (
                False,
                f"Invalid value for 'ext-resource-session-check'='{value}'. Must be one of: {', '.join(VALID_BODY_EXT_RESOURCE_SESSION_CHECK)}",
            )
    if "dyn-addr-session-check" in payload:
        value = payload["dyn-addr-session-check"]
        if value not in VALID_BODY_DYN_ADDR_SESSION_CHECK:
            return (
                False,
                f"Invalid value for 'dyn-addr-session-check'='{value}'. Must be one of: {', '.join(VALID_BODY_DYN_ADDR_SESSION_CHECK)}",
            )
    if "gui-enforce-change-summary" in payload:
        value = payload["gui-enforce-change-summary"]
        if value not in VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY:
            return (
                False,
                f"Invalid value for 'gui-enforce-change-summary'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ENFORCE_CHANGE_SUMMARY)}",
            )
    if "internet-service-database-cache" in payload:
        value = payload["internet-service-database-cache"]
        if value not in VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE:
            return (
                False,
                f"Invalid value for 'internet-service-database-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_DATABASE_CACHE)}",
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
    constant_name = f"VALID_BODY_{field_name.replace('-', '_').upper()}"
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
    "endpoint": "system/settings",
    "category": "cmdb",
    "api_path": "system/settings",
    "help": "Configure VDOM settings.",
    "total_fields": 141,
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
