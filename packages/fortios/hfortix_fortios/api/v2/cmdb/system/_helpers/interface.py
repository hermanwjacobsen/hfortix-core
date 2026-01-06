"""Validation helpers for system/interface - Auto-generated"""

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

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "vdom",  # Interface is in this virtual domain (VDOM).
    "dhcp-relay-interface",  # Specify outgoing interface to reach server.
    "interface",  # Interface name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "vdom": "",
    "vrf": 0,
    "cli-conn-status": 0,
    "fortilink": "disable",
    "switch-controller-source-ip": "outbound",
    "mode": "static",
    "distance": 5,
    "priority": 1,
    "dhcp-relay-interface-select-method": "auto",
    "dhcp-relay-interface": "",
    "dhcp-relay-vrf-select": -1,
    "dhcp-broadcast-flag": "enable",
    "dhcp-relay-service": "disable",
    "dhcp-relay-ip": "",
    "dhcp-relay-source-ip": "0.0.0.0",
    "dhcp-relay-circuit-id": "",
    "dhcp-relay-link-selection": "0.0.0.0",
    "dhcp-relay-request-all-server": "disable",
    "dhcp-relay-allow-no-end-option": "disable",
    "dhcp-relay-type": "regular",
    "dhcp-smart-relay": "disable",
    "dhcp-relay-agent-option": "enable",
    "dhcp-classless-route-addition": "enable",
    "management-ip": "0.0.0.0 0.0.0.0",
    "ip": "0.0.0.0 0.0.0.0",
    "allowaccess": "",
    "gwdetect": "disable",
    "ping-serv-status": 0,
    "detectserver": "",
    "detectprotocol": "ping",
    "ha-priority": 1,
    "fail-detect": "disable",
    "fail-detect-option": "link-down",
    "fail-alert-method": "link-down",
    "fail-action-on-extender": "soft-restart",
    "dhcp-client-identifier": "",
    "dhcp-renew-time": 0,
    "ipunnumbered": "0.0.0.0",
    "username": "",
    "pppoe-egress-cos": "cos0",
    "pppoe-unnumbered-negotiate": "enable",
    "idle-timeout": 0,
    "multilink": "disable",
    "mrru": 1500,
    "detected-peer-mtu": 0,
    "disc-retry-timeout": 1,
    "padt-retry-timeout": 1,
    "service-name": "",
    "ac-name": "",
    "lcp-echo-interval": 5,
    "lcp-max-echo-fails": 3,
    "defaultgw": "enable",
    "dns-server-override": "enable",
    "dns-server-protocol": "cleartext",
    "auth-type": "auto",
    "pptp-client": "disable",
    "pptp-user": "",
    "pptp-server-ip": "0.0.0.0",
    "pptp-auth-type": "auto",
    "pptp-timeout": 0,
    "arpforward": "enable",
    "ndiscforward": "enable",
    "broadcast-forward": "disable",
    "bfd": "global",
    "bfd-desired-min-tx": 250,
    "bfd-detect-mult": 3,
    "bfd-required-min-rx": 250,
    "l2forward": "disable",
    "icmp-send-redirect": "enable",
    "icmp-accept-redirect": "enable",
    "reachable-time": 30000,
    "vlanforward": "disable",
    "stpforward": "disable",
    "stpforward-mode": "rpl-all-ext-id",
    "ips-sniffer-mode": "disable",
    "ident-accept": "disable",
    "ipmac": "disable",
    "subst": "disable",
    "macaddr": "00:00:00:00:00:00",
    "virtual-mac": "00:00:00:00:00:00",
    "substitute-dst-mac": "00:00:00:00:00:00",
    "speed": "auto",
    "status": "up",
    "netbios-forward": "disable",
    "wins-ip": "0.0.0.0",
    "type": "vlan",
    "dedicated-to": "none",
    "trust-ip-1": "0.0.0.0 0.0.0.0",
    "trust-ip-2": "0.0.0.0 0.0.0.0",
    "trust-ip-3": "0.0.0.0 0.0.0.0",
    "trust-ip6-1": "::/0",
    "trust-ip6-2": "::/0",
    "trust-ip6-3": "::/0",
    "ring-rx": 0,
    "ring-tx": 0,
    "wccp": "disable",
    "netflow-sampler": "disable",
    "netflow-sample-rate": 1,
    "netflow-sampler-id": 0,
    "sflow-sampler": "disable",
    "drop-fragment": "disable",
    "src-check": "enable",
    "sample-rate": 2000,
    "polling-interval": 20,
    "sample-direction": "both",
    "explicit-web-proxy": "disable",
    "explicit-ftp-proxy": "disable",
    "proxy-captive-portal": "disable",
    "tcp-mss": 0,
    "inbandwidth": 0,
    "outbandwidth": 0,
    "egress-shaping-profile": "",
    "ingress-shaping-profile": "",
    "spillover-threshold": 0,
    "ingress-spillover-threshold": 0,
    "weight": 0,
    "interface": "",
    "external": "disable",
    "mtu-override": "disable",
    "mtu": 1500,
    "vlan-protocol": "8021q",
    "vlanid": 0,
    "forward-domain": 0,
    "remote-ip": "0.0.0.0 0.0.0.0",
    "lacp-mode": "active",
    "lacp-ha-secondary": "enable",
    "system-id-type": "auto",
    "system-id": "00:00:00:00:00:00",
    "lacp-speed": "slow",
    "min-links": 1,
    "min-links-down": "operational",
    "algorithm": "L4",
    "link-up-delay": 50,
    "aggregate-type": "physical",
    "priority-override": "enable",
    "aggregate": "",
    "redundant-interface": "",
    "devindex": 0,
    "vindex": 0,
    "switch": "",
    "alias": "",
    "security-mode": "none",
    "security-mac-auth-bypass": "disable",
    "security-ip-auth-bypass": "disable",
    "security-external-logout": "",
    "replacemsg-override-group": "",
    "auth-cert": "",
    "auth-portal-addr": "",
    "security-exempt-list": "",
    "ike-saml-server": "",
    "device-identification": "disable",
    "exclude-signatures": "",
    "device-user-identification": "enable",
    "lldp-reception": "vdom",
    "lldp-transmission": "vdom",
    "lldp-network-policy": "",
    "estimated-upstream-bandwidth": 0,
    "estimated-downstream-bandwidth": 0,
    "measured-upstream-bandwidth": 0,
    "measured-downstream-bandwidth": 0,
    "bandwidth-measure-time": 0,
    "monitor-bandwidth": "disable",
    "vrrp-virtual-mac": "disable",
    "role": "undefined",
    "snmp-index": 0,
    "secondary-IP": "disable",
    "preserve-session-route": "disable",
    "auto-auth-extension-device": "disable",
    "ap-discover": "enable",
    "fortilink-neighbor-detect": "lldp",
    "ip-managed-by-fortiipam": "inherit-global",
    "managed-subnetwork-size": "256",
    "fortilink-split-interface": "enable",
    "internal": 0,
    "fortilink-backup-link": 0,
    "switch-controller-access-vlan": "disable",
    "switch-controller-traffic-policy": "",
    "switch-controller-rspan-mode": "disable",
    "switch-controller-netflow-collect": "disable",
    "switch-controller-mgmt-vlan": 4094,
    "switch-controller-igmp-snooping": "disable",
    "switch-controller-igmp-snooping-proxy": "disable",
    "switch-controller-igmp-snooping-fast-leave": "disable",
    "switch-controller-dhcp-snooping": "disable",
    "switch-controller-dhcp-snooping-verify-mac": "disable",
    "switch-controller-dhcp-snooping-option82": "disable",
    "switch-controller-arp-inspection": "disable",
    "switch-controller-learning-limit": 0,
    "switch-controller-nac": "",
    "switch-controller-dynamic": "",
    "switch-controller-feature": "none",
    "switch-controller-iot-scanning": "disable",
    "switch-controller-offload": "disable",
    "switch-controller-offload-ip": "0.0.0.0",
    "switch-controller-offload-gw": "disable",
    "swc-vlan": 0,
    "swc-first-create": 0,
    "color": 0,
    "eap-supplicant": "disable",
    "eap-method": "",
    "eap-identity": "",
    "eap-ca-cert": "",
    "eap-user-cert": "",
    "default-purdue-level": "3",
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
    "name": "string",  # Name.
    "vdom": "string",  # Interface is in this virtual domain (VDOM).
    "vrf": "integer",  # Virtual Routing Forwarding ID.
    "cli-conn-status": "integer",  # CLI connection status.
    "fortilink": "option",  # Enable FortiLink to dedicate this interface to manage other 
    "switch-controller-source-ip": "option",  # Source IP address used in FortiLink over L3 connections.
    "mode": "option",  # Addressing mode (static, DHCP, PPPoE).
    "client-options": "string",  # DHCP client options.
    "distance": "integer",  # Distance for routes learned through PPPoE or DHCP, lower dis
    "priority": "integer",  # Priority of learned routes.
    "dhcp-relay-interface-select-method": "option",  # Specify how to select outgoing interface to reach server.
    "dhcp-relay-interface": "string",  # Specify outgoing interface to reach server.
    "dhcp-relay-vrf-select": "integer",  # VRF ID used for connection to server.
    "dhcp-broadcast-flag": "option",  # Enable/disable setting of the broadcast flag in messages sen
    "dhcp-relay-service": "option",  # Enable/disable allowing this interface to act as a DHCP rela
    "dhcp-relay-ip": "user",  # DHCP relay IP address.
    "dhcp-relay-source-ip": "ipv4-address",  # IP address used by the DHCP relay as its source IP.
    "dhcp-relay-circuit-id": "string",  # DHCP relay circuit ID.
    "dhcp-relay-link-selection": "ipv4-address",  # DHCP relay link selection.
    "dhcp-relay-request-all-server": "option",  # Enable/disable sending of DHCP requests to all servers.
    "dhcp-relay-allow-no-end-option": "option",  # Enable/disable relaying DHCP messages with no end option.
    "dhcp-relay-type": "option",  # DHCP relay type (regular or IPsec).
    "dhcp-smart-relay": "option",  # Enable/disable DHCP smart relay.
    "dhcp-relay-agent-option": "option",  # Enable/disable DHCP relay agent option.
    "dhcp-classless-route-addition": "option",  # Enable/disable addition of classless static routes retrieved
    "management-ip": "ipv4-classnet-host",  # High Availability in-band management IP address of this inte
    "ip": "ipv4-classnet-host",  # Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
    "allowaccess": "option",  # Permitted types of management access to this interface.
    "gwdetect": "option",  # Enable/disable detect gateway alive for first.
    "ping-serv-status": "integer",  # PING server status.
    "detectserver": "user",  # Gateway's ping server for this IP.
    "detectprotocol": "option",  # Protocols used to detect the server.
    "ha-priority": "integer",  # HA election priority for the PING server.
    "fail-detect": "option",  # Enable/disable fail detection features for this interface.
    "fail-detect-option": "option",  # Options for detecting that this interface has failed.
    "fail-alert-method": "option",  # Select link-failed-signal or link-down method to alert about
    "fail-action-on-extender": "option",  # Action on FortiExtender when interface fail.
    "fail-alert-interfaces": "string",  # Names of the FortiGate interfaces to which the link failure 
    "dhcp-client-identifier": "string",  # DHCP client identifier.
    "dhcp-renew-time": "integer",  # DHCP renew time in seconds (300-604800), 0 means use the ren
    "ipunnumbered": "ipv4-address",  # Unnumbered IP used for PPPoE interfaces for which no unique 
    "username": "string",  # Username of the PPPoE account, provided by your ISP.
    "pppoe-egress-cos": "option",  # CoS in VLAN tag for outgoing PPPoE/PPP packets.
    "pppoe-unnumbered-negotiate": "option",  # Enable/disable PPPoE unnumbered negotiation.
    "password": "password",  # PPPoE account's password.
    "idle-timeout": "integer",  # PPPoE auto disconnect after idle timeout seconds, 0 means no
    "multilink": "option",  # Enable/disable PPP multilink support.
    "mrru": "integer",  # PPP MRRU (296 - 65535, default = 1500).
    "detected-peer-mtu": "integer",  # MTU of detected peer (0 - 4294967295).
    "disc-retry-timeout": "integer",  # Time in seconds to wait before retrying to start a PPPoE dis
    "padt-retry-timeout": "integer",  # PPPoE Active Discovery Terminate (PADT) used to terminate se
    "service-name": "string",  # PPPoE service name.
    "ac-name": "string",  # PPPoE server name.
    "lcp-echo-interval": "integer",  # Time in seconds between PPPoE Link Control Protocol (LCP) ec
    "lcp-max-echo-fails": "integer",  # Maximum missed LCP echo messages before disconnect.
    "defaultgw": "option",  # Enable to get the gateway IP from the DHCP or PPPoE server.
    "dns-server-override": "option",  # Enable/disable use DNS acquired by DHCP or PPPoE.
    "dns-server-protocol": "option",  # DNS transport protocols.
    "auth-type": "option",  # PPP authentication type to use.
    "pptp-client": "option",  # Enable/disable PPTP client.
    "pptp-user": "string",  # PPTP user name.
    "pptp-password": "password",  # PPTP password.
    "pptp-server-ip": "ipv4-address",  # PPTP server IP address.
    "pptp-auth-type": "option",  # PPTP authentication type.
    "pptp-timeout": "integer",  # Idle timer in minutes (0 for disabled).
    "arpforward": "option",  # Enable/disable ARP forwarding.
    "ndiscforward": "option",  # Enable/disable NDISC forwarding.
    "broadcast-forward": "option",  # Enable/disable broadcast forwarding.
    "bfd": "option",  # Bidirectional Forwarding Detection (BFD) settings.
    "bfd-desired-min-tx": "integer",  # BFD desired minimal transmit interval.
    "bfd-detect-mult": "integer",  # BFD detection multiplier.
    "bfd-required-min-rx": "integer",  # BFD required minimal receive interval.
    "l2forward": "option",  # Enable/disable l2 forwarding.
    "icmp-send-redirect": "option",  # Enable/disable sending of ICMP redirects.
    "icmp-accept-redirect": "option",  # Enable/disable ICMP accept redirect.
    "reachable-time": "integer",  # IPv4 reachable time in milliseconds (30000 - 3600000, defaul
    "vlanforward": "option",  # Enable/disable traffic forwarding between VLANs on this inte
    "stpforward": "option",  # Enable/disable STP forwarding.
    "stpforward-mode": "option",  # Configure STP forwarding mode.
    "ips-sniffer-mode": "option",  # Enable/disable the use of this interface as a one-armed snif
    "ident-accept": "option",  # Enable/disable authentication for this interface.
    "ipmac": "option",  # Enable/disable IP/MAC binding.
    "subst": "option",  # Enable to always send packets from this interface to a desti
    "macaddr": "mac-address",  # Change the interface's MAC address.
    "virtual-mac": "mac-address",  # Change the interface's virtual MAC address.
    "substitute-dst-mac": "mac-address",  # Destination MAC address that all packets are sent to from th
    "speed": "option",  # Interface speed. The default setting and the options availab
    "status": "option",  # Bring the interface up or shut the interface down.
    "netbios-forward": "option",  # Enable/disable NETBIOS forwarding.
    "wins-ip": "ipv4-address",  # WINS server IP.
    "type": "option",  # Interface type.
    "dedicated-to": "option",  # Configure interface for single purpose.
    "trust-ip-1": "ipv4-classnet-any",  # Trusted host for dedicated management traffic (0.0.0.0/24 fo
    "trust-ip-2": "ipv4-classnet-any",  # Trusted host for dedicated management traffic (0.0.0.0/24 fo
    "trust-ip-3": "ipv4-classnet-any",  # Trusted host for dedicated management traffic (0.0.0.0/24 fo
    "trust-ip6-1": "ipv6-prefix",  # Trusted IPv6 host for dedicated management traffic (::/0 for
    "trust-ip6-2": "ipv6-prefix",  # Trusted IPv6 host for dedicated management traffic (::/0 for
    "trust-ip6-3": "ipv6-prefix",  # Trusted IPv6 host for dedicated management traffic (::/0 for
    "ring-rx": "integer",  # RX ring size.
    "ring-tx": "integer",  # TX ring size.
    "wccp": "option",  # Enable/disable WCCP on this interface. Used for encapsulated
    "netflow-sampler": "option",  # Enable/disable NetFlow on this interface and set the data th
    "netflow-sample-rate": "integer",  # NetFlow sample rate.  Sample one packet every configured num
    "netflow-sampler-id": "integer",  # Netflow sampler ID.
    "sflow-sampler": "option",  # Enable/disable sFlow on this interface.
    "drop-fragment": "option",  # Enable/disable drop fragment packets.
    "src-check": "option",  # Enable/disable source IP check.
    "sample-rate": "integer",  # sFlow sample rate (10 - 99999).
    "polling-interval": "integer",  # sFlow polling interval in seconds (1 - 255).
    "sample-direction": "option",  # Data that NetFlow collects (rx, tx, or both).
    "explicit-web-proxy": "option",  # Enable/disable the explicit web proxy on this interface.
    "explicit-ftp-proxy": "option",  # Enable/disable the explicit FTP proxy on this interface.
    "proxy-captive-portal": "option",  # Enable/disable proxy captive portal on this interface.
    "tcp-mss": "integer",  # TCP maximum segment size. 0 means do not change segment size
    "inbandwidth": "integer",  # Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 
    "outbandwidth": "integer",  # Bandwidth limit for outgoing traffic (0 - 80000000 kbps).
    "egress-shaping-profile": "string",  # Outgoing traffic shaping profile.
    "ingress-shaping-profile": "string",  # Incoming traffic shaping profile.
    "spillover-threshold": "integer",  # Egress Spillover threshold (0 - 16776000 kbps), 0 means unli
    "ingress-spillover-threshold": "integer",  # Ingress Spillover threshold (0 - 16776000 kbps), 0 means unl
    "weight": "integer",  # Default weight for static routes (if route has no weight con
    "interface": "string",  # Interface name.
    "external": "option",  # Enable/disable identifying the interface as an external inte
    "mtu-override": "option",  # Enable to set a custom MTU for this interface.
    "mtu": "integer",  # MTU value for this interface.
    "vlan-protocol": "option",  # Ethernet protocol of VLAN.
    "vlanid": "integer",  # VLAN ID (1 - 4094).
    "forward-domain": "integer",  # Transparent mode forward domain.
    "remote-ip": "ipv4-classnet-host",  # Remote IP address of tunnel.
    "member": "string",  # Physical interfaces that belong to the aggregate or redundan
    "lacp-mode": "option",  # LACP mode.
    "lacp-ha-secondary": "option",  # LACP HA secondary member.
    "system-id-type": "option",  # Method in which system ID is generated.
    "system-id": "mac-address",  # Define a system ID for the aggregate interface.
    "lacp-speed": "option",  # How often the interface sends LACP messages.
    "min-links": "integer",  # Minimum number of aggregated ports that must be up.
    "min-links-down": "option",  # Action to take when less than the configured minimum number 
    "algorithm": "option",  # Frame distribution algorithm.
    "link-up-delay": "integer",  # Number of milliseconds to wait before considering a link is 
    "aggregate-type": "option",  # Type of aggregation.
    "priority-override": "option",  # Enable/disable fail back to higher priority port once recove
    "aggregate": "string",  # Aggregate interface.
    "redundant-interface": "string",  # Redundant interface.
    "devindex": "integer",  # Device Index.
    "vindex": "integer",  # Switch control interface VLAN ID.
    "switch": "string",  # Contained in switch.
    "description": "var-string",  # Description.
    "alias": "string",  # Alias will be displayed with the interface name to make it e
    "security-mode": "option",  # Turn on captive portal authentication for this interface.
    "security-mac-auth-bypass": "option",  # Enable/disable MAC authentication bypass.
    "security-ip-auth-bypass": "option",  # Enable/disable IP authentication bypass.
    "security-external-web": "var-string",  # URL of external authentication web server.
    "security-external-logout": "string",  # URL of external authentication logout server.
    "replacemsg-override-group": "string",  # Replacement message override group.
    "security-redirect-url": "var-string",  # URL redirection after disclaimer/authentication.
    "auth-cert": "string",  # HTTPS server certificate.
    "auth-portal-addr": "string",  # Address of captive portal.
    "security-exempt-list": "string",  # Name of security-exempt-list.
    "security-groups": "string",  # User groups that can authenticate with the captive portal.
    "ike-saml-server": "string",  # Configure IKE authentication SAML server.
    "device-identification": "option",  # Enable/disable passively gathering of device identity inform
    "exclude-signatures": "option",  # Exclude IOT or OT application signatures.
    "device-user-identification": "option",  # Enable/disable passive gathering of user identity informatio
    "lldp-reception": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) receptio
    "lldp-transmission": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) transmis
    "lldp-network-policy": "string",  # LLDP-MED network policy profile.
    "estimated-upstream-bandwidth": "integer",  # Estimated maximum upstream bandwidth (kbps). Used to estimat
    "estimated-downstream-bandwidth": "integer",  # Estimated maximum downstream bandwidth (kbps). Used to estim
    "measured-upstream-bandwidth": "integer",  # Measured upstream bandwidth (kbps).
    "measured-downstream-bandwidth": "integer",  # Measured downstream bandwidth (kbps).
    "bandwidth-measure-time": "integer",  # Bandwidth measure time.
    "monitor-bandwidth": "option",  # Enable monitoring bandwidth on this interface.
    "vrrp-virtual-mac": "option",  # Enable/disable use of virtual MAC for VRRP.
    "vrrp": "string",  # VRRP configuration.
    "phy-setting": "string",  # PHY settings
    "role": "option",  # Interface role.
    "snmp-index": "integer",  # Permanent SNMP Index of the interface.
    "secondary-IP": "option",  # Enable/disable adding a secondary IP to this interface.
    "secondaryip": "string",  # Second IP address of interface.
    "preserve-session-route": "option",  # Enable/disable preservation of session route when dirty.
    "auto-auth-extension-device": "option",  # Enable/disable automatic authorization of dedicated Fortinet
    "ap-discover": "option",  # Enable/disable automatic registration of unknown FortiAP dev
    "fortilink-neighbor-detect": "option",  # Protocol for FortiGate neighbor discovery.
    "ip-managed-by-fortiipam": "option",  # Enable/disable automatic IP address assignment of this inter
    "managed-subnetwork-size": "option",  # Number of IP addresses to be allocated by FortiIPAM and used
    "fortilink-split-interface": "option",  # Enable/disable FortiLink split interface to connect member l
    "internal": "integer",  # Implicitly created.
    "fortilink-backup-link": "integer",  # FortiLink split interface backup link.
    "switch-controller-access-vlan": "option",  # Block FortiSwitch port-to-port traffic.
    "switch-controller-traffic-policy": "string",  # Switch controller traffic policy for the VLAN.
    "switch-controller-rspan-mode": "option",  # Stop Layer2 MAC learning and interception of BPDUs and other
    "switch-controller-netflow-collect": "option",  # NetFlow collection and processing.
    "switch-controller-mgmt-vlan": "integer",  # VLAN to use for FortiLink management purposes.
    "switch-controller-igmp-snooping": "option",  # Switch controller IGMP snooping.
    "switch-controller-igmp-snooping-proxy": "option",  # Switch controller IGMP snooping proxy.
    "switch-controller-igmp-snooping-fast-leave": "option",  # Switch controller IGMP snooping fast-leave.
    "switch-controller-dhcp-snooping": "option",  # Switch controller DHCP snooping.
    "switch-controller-dhcp-snooping-verify-mac": "option",  # Switch controller DHCP snooping verify MAC.
    "switch-controller-dhcp-snooping-option82": "option",  # Switch controller DHCP snooping option82.
    "dhcp-snooping-server-list": "string",  # Configure DHCP server access list.
    "switch-controller-arp-inspection": "option",  # Enable/disable/Monitor FortiSwitch ARP inspection.
    "switch-controller-learning-limit": "integer",  # Limit the number of dynamic MAC addresses on this VLAN (1 - 
    "switch-controller-nac": "string",  # Integrated FortiLink settings for managed FortiSwitch.
    "switch-controller-dynamic": "string",  # Integrated FortiLink settings for managed FortiSwitch.
    "switch-controller-feature": "option",  # Interface's purpose when assigning traffic (read only).
    "switch-controller-iot-scanning": "option",  # Enable/disable managed FortiSwitch IoT scanning.
    "switch-controller-offload": "option",  # Enable/disable managed FortiSwitch routing offload.
    "switch-controller-offload-ip": "ipv4-address",  # IP for routing offload on FortiSwitch.
    "switch-controller-offload-gw": "option",  # Enable/disable managed FortiSwitch routing offload gateway.
    "swc-vlan": "integer",  # Creation status for switch-controller VLANs.
    "swc-first-create": "integer",  # Initial create for switch-controller VLANs.
    "color": "integer",  # Color of icon on the GUI.
    "tagging": "string",  # Config object tagging.
    "eap-supplicant": "option",  # Enable/disable EAP-Supplicant.
    "eap-method": "option",  # EAP method.
    "eap-identity": "string",  # EAP identity.
    "eap-password": "password",  # EAP password.
    "eap-ca-cert": "string",  # EAP CA certificate name.
    "eap-user-cert": "string",  # EAP user certificate name.
    "default-purdue-level": "option",  # default purdue level of device detected on this interface.
    "ipv6": "string",  # IPv6 of interface.
    "physical": "key",  # Print physical interface information.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "vdom": "Interface is in this virtual domain (VDOM).",
    "vrf": "Virtual Routing Forwarding ID.",
    "cli-conn-status": "CLI connection status.",
    "fortilink": "Enable FortiLink to dedicate this interface to manage other Fortinet devices.",
    "switch-controller-source-ip": "Source IP address used in FortiLink over L3 connections.",
    "mode": "Addressing mode (static, DHCP, PPPoE).",
    "client-options": "DHCP client options.",
    "distance": "Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.",
    "priority": "Priority of learned routes.",
    "dhcp-relay-interface-select-method": "Specify how to select outgoing interface to reach server.",
    "dhcp-relay-interface": "Specify outgoing interface to reach server.",
    "dhcp-relay-vrf-select": "VRF ID used for connection to server.",
    "dhcp-broadcast-flag": "Enable/disable setting of the broadcast flag in messages sent by the DHCP client (default = enable).",
    "dhcp-relay-service": "Enable/disable allowing this interface to act as a DHCP relay.",
    "dhcp-relay-ip": "DHCP relay IP address.",
    "dhcp-relay-source-ip": "IP address used by the DHCP relay as its source IP.",
    "dhcp-relay-circuit-id": "DHCP relay circuit ID.",
    "dhcp-relay-link-selection": "DHCP relay link selection.",
    "dhcp-relay-request-all-server": "Enable/disable sending of DHCP requests to all servers.",
    "dhcp-relay-allow-no-end-option": "Enable/disable relaying DHCP messages with no end option.",
    "dhcp-relay-type": "DHCP relay type (regular or IPsec).",
    "dhcp-smart-relay": "Enable/disable DHCP smart relay.",
    "dhcp-relay-agent-option": "Enable/disable DHCP relay agent option.",
    "dhcp-classless-route-addition": "Enable/disable addition of classless static routes retrieved from DHCP server.",
    "management-ip": "High Availability in-band management IP address of this interface.",
    "ip": "Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.",
    "allowaccess": "Permitted types of management access to this interface.",
    "gwdetect": "Enable/disable detect gateway alive for first.",
    "ping-serv-status": "PING server status.",
    "detectserver": "Gateway's ping server for this IP.",
    "detectprotocol": "Protocols used to detect the server.",
    "ha-priority": "HA election priority for the PING server.",
    "fail-detect": "Enable/disable fail detection features for this interface.",
    "fail-detect-option": "Options for detecting that this interface has failed.",
    "fail-alert-method": "Select link-failed-signal or link-down method to alert about a failed link.",
    "fail-action-on-extender": "Action on FortiExtender when interface fail.",
    "fail-alert-interfaces": "Names of the FortiGate interfaces to which the link failure alert is sent.",
    "dhcp-client-identifier": "DHCP client identifier.",
    "dhcp-renew-time": "DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server.",
    "ipunnumbered": "Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.",
    "username": "Username of the PPPoE account, provided by your ISP.",
    "pppoe-egress-cos": "CoS in VLAN tag for outgoing PPPoE/PPP packets.",
    "pppoe-unnumbered-negotiate": "Enable/disable PPPoE unnumbered negotiation.",
    "password": "PPPoE account's password.",
    "idle-timeout": "PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.",
    "multilink": "Enable/disable PPP multilink support.",
    "mrru": "PPP MRRU (296 - 65535, default = 1500).",
    "detected-peer-mtu": "MTU of detected peer (0 - 4294967295).",
    "disc-retry-timeout": "Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.",
    "padt-retry-timeout": "PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.",
    "service-name": "PPPoE service name.",
    "ac-name": "PPPoE server name.",
    "lcp-echo-interval": "Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.",
    "lcp-max-echo-fails": "Maximum missed LCP echo messages before disconnect.",
    "defaultgw": "Enable to get the gateway IP from the DHCP or PPPoE server.",
    "dns-server-override": "Enable/disable use DNS acquired by DHCP or PPPoE.",
    "dns-server-protocol": "DNS transport protocols.",
    "auth-type": "PPP authentication type to use.",
    "pptp-client": "Enable/disable PPTP client.",
    "pptp-user": "PPTP user name.",
    "pptp-password": "PPTP password.",
    "pptp-server-ip": "PPTP server IP address.",
    "pptp-auth-type": "PPTP authentication type.",
    "pptp-timeout": "Idle timer in minutes (0 for disabled).",
    "arpforward": "Enable/disable ARP forwarding.",
    "ndiscforward": "Enable/disable NDISC forwarding.",
    "broadcast-forward": "Enable/disable broadcast forwarding.",
    "bfd": "Bidirectional Forwarding Detection (BFD) settings.",
    "bfd-desired-min-tx": "BFD desired minimal transmit interval.",
    "bfd-detect-mult": "BFD detection multiplier.",
    "bfd-required-min-rx": "BFD required minimal receive interval.",
    "l2forward": "Enable/disable l2 forwarding.",
    "icmp-send-redirect": "Enable/disable sending of ICMP redirects.",
    "icmp-accept-redirect": "Enable/disable ICMP accept redirect.",
    "reachable-time": "IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000).",
    "vlanforward": "Enable/disable traffic forwarding between VLANs on this interface.",
    "stpforward": "Enable/disable STP forwarding.",
    "stpforward-mode": "Configure STP forwarding mode.",
    "ips-sniffer-mode": "Enable/disable the use of this interface as a one-armed sniffer.",
    "ident-accept": "Enable/disable authentication for this interface.",
    "ipmac": "Enable/disable IP/MAC binding.",
    "subst": "Enable to always send packets from this interface to a destination MAC address.",
    "macaddr": "Change the interface's MAC address.",
    "virtual-mac": "Change the interface's virtual MAC address.",
    "substitute-dst-mac": "Destination MAC address that all packets are sent to from this interface.",
    "speed": "Interface speed. The default setting and the options available depend on the interface hardware.",
    "status": "Bring the interface up or shut the interface down.",
    "netbios-forward": "Enable/disable NETBIOS forwarding.",
    "wins-ip": "WINS server IP.",
    "type": "Interface type.",
    "dedicated-to": "Configure interface for single purpose.",
    "trust-ip-1": "Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).",
    "trust-ip-2": "Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).",
    "trust-ip-3": "Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).",
    "trust-ip6-1": "Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).",
    "trust-ip6-2": "Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).",
    "trust-ip6-3": "Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).",
    "ring-rx": "RX ring size.",
    "ring-tx": "TX ring size.",
    "wccp": "Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.",
    "netflow-sampler": "Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).",
    "netflow-sample-rate": "NetFlow sample rate.  Sample one packet every configured number of packets (1 - 65535, default = 1, which means standard NetFlow where all packets are sampled).",
    "netflow-sampler-id": "Netflow sampler ID.",
    "sflow-sampler": "Enable/disable sFlow on this interface.",
    "drop-fragment": "Enable/disable drop fragment packets.",
    "src-check": "Enable/disable source IP check.",
    "sample-rate": "sFlow sample rate (10 - 99999).",
    "polling-interval": "sFlow polling interval in seconds (1 - 255).",
    "sample-direction": "Data that NetFlow collects (rx, tx, or both).",
    "explicit-web-proxy": "Enable/disable the explicit web proxy on this interface.",
    "explicit-ftp-proxy": "Enable/disable the explicit FTP proxy on this interface.",
    "proxy-captive-portal": "Enable/disable proxy captive portal on this interface.",
    "tcp-mss": "TCP maximum segment size. 0 means do not change segment size.",
    "inbandwidth": "Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 means unlimited.",
    "outbandwidth": "Bandwidth limit for outgoing traffic (0 - 80000000 kbps).",
    "egress-shaping-profile": "Outgoing traffic shaping profile.",
    "ingress-shaping-profile": "Incoming traffic shaping profile.",
    "spillover-threshold": "Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.",
    "ingress-spillover-threshold": "Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.",
    "weight": "Default weight for static routes (if route has no weight configured).",
    "interface": "Interface name.",
    "external": "Enable/disable identifying the interface as an external interface (which usually means it's connected to the Internet).",
    "mtu-override": "Enable to set a custom MTU for this interface.",
    "mtu": "MTU value for this interface.",
    "vlan-protocol": "Ethernet protocol of VLAN.",
    "vlanid": "VLAN ID (1 - 4094).",
    "forward-domain": "Transparent mode forward domain.",
    "remote-ip": "Remote IP address of tunnel.",
    "member": "Physical interfaces that belong to the aggregate or redundant interface.",
    "lacp-mode": "LACP mode.",
    "lacp-ha-secondary": "LACP HA secondary member.",
    "system-id-type": "Method in which system ID is generated.",
    "system-id": "Define a system ID for the aggregate interface.",
    "lacp-speed": "How often the interface sends LACP messages.",
    "min-links": "Minimum number of aggregated ports that must be up.",
    "min-links-down": "Action to take when less than the configured minimum number of links are active.",
    "algorithm": "Frame distribution algorithm.",
    "link-up-delay": "Number of milliseconds to wait before considering a link is up.",
    "aggregate-type": "Type of aggregation.",
    "priority-override": "Enable/disable fail back to higher priority port once recovered.",
    "aggregate": "Aggregate interface.",
    "redundant-interface": "Redundant interface.",
    "devindex": "Device Index.",
    "vindex": "Switch control interface VLAN ID.",
    "switch": "Contained in switch.",
    "description": "Description.",
    "alias": "Alias will be displayed with the interface name to make it easier to distinguish.",
    "security-mode": "Turn on captive portal authentication for this interface.",
    "security-mac-auth-bypass": "Enable/disable MAC authentication bypass.",
    "security-ip-auth-bypass": "Enable/disable IP authentication bypass.",
    "security-external-web": "URL of external authentication web server.",
    "security-external-logout": "URL of external authentication logout server.",
    "replacemsg-override-group": "Replacement message override group.",
    "security-redirect-url": "URL redirection after disclaimer/authentication.",
    "auth-cert": "HTTPS server certificate.",
    "auth-portal-addr": "Address of captive portal.",
    "security-exempt-list": "Name of security-exempt-list.",
    "security-groups": "User groups that can authenticate with the captive portal.",
    "ike-saml-server": "Configure IKE authentication SAML server.",
    "device-identification": "Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.",
    "exclude-signatures": "Exclude IOT or OT application signatures.",
    "device-user-identification": "Enable/disable passive gathering of user identity information about users on this interface.",
    "lldp-reception": "Enable/disable Link Layer Discovery Protocol (LLDP) reception.",
    "lldp-transmission": "Enable/disable Link Layer Discovery Protocol (LLDP) transmission.",
    "lldp-network-policy": "LLDP-MED network policy profile.",
    "estimated-upstream-bandwidth": "Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.",
    "estimated-downstream-bandwidth": "Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.",
    "measured-upstream-bandwidth": "Measured upstream bandwidth (kbps).",
    "measured-downstream-bandwidth": "Measured downstream bandwidth (kbps).",
    "bandwidth-measure-time": "Bandwidth measure time.",
    "monitor-bandwidth": "Enable monitoring bandwidth on this interface.",
    "vrrp-virtual-mac": "Enable/disable use of virtual MAC for VRRP.",
    "vrrp": "VRRP configuration.",
    "phy-setting": "PHY settings",
    "role": "Interface role.",
    "snmp-index": "Permanent SNMP Index of the interface.",
    "secondary-IP": "Enable/disable adding a secondary IP to this interface.",
    "secondaryip": "Second IP address of interface.",
    "preserve-session-route": "Enable/disable preservation of session route when dirty.",
    "auto-auth-extension-device": "Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.",
    "ap-discover": "Enable/disable automatic registration of unknown FortiAP devices.",
    "fortilink-neighbor-detect": "Protocol for FortiGate neighbor discovery.",
    "ip-managed-by-fortiipam": "Enable/disable automatic IP address assignment of this interface by FortiIPAM.",
    "managed-subnetwork-size": "Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit's DHCP server settings.",
    "fortilink-split-interface": "Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.",
    "internal": "Implicitly created.",
    "fortilink-backup-link": "FortiLink split interface backup link.",
    "switch-controller-access-vlan": "Block FortiSwitch port-to-port traffic.",
    "switch-controller-traffic-policy": "Switch controller traffic policy for the VLAN.",
    "switch-controller-rspan-mode": "Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.",
    "switch-controller-netflow-collect": "NetFlow collection and processing.",
    "switch-controller-mgmt-vlan": "VLAN to use for FortiLink management purposes.",
    "switch-controller-igmp-snooping": "Switch controller IGMP snooping.",
    "switch-controller-igmp-snooping-proxy": "Switch controller IGMP snooping proxy.",
    "switch-controller-igmp-snooping-fast-leave": "Switch controller IGMP snooping fast-leave.",
    "switch-controller-dhcp-snooping": "Switch controller DHCP snooping.",
    "switch-controller-dhcp-snooping-verify-mac": "Switch controller DHCP snooping verify MAC.",
    "switch-controller-dhcp-snooping-option82": "Switch controller DHCP snooping option82.",
    "dhcp-snooping-server-list": "Configure DHCP server access list.",
    "switch-controller-arp-inspection": "Enable/disable/Monitor FortiSwitch ARP inspection.",
    "switch-controller-learning-limit": "Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default).",
    "switch-controller-nac": "Integrated FortiLink settings for managed FortiSwitch.",
    "switch-controller-dynamic": "Integrated FortiLink settings for managed FortiSwitch.",
    "switch-controller-feature": "Interface's purpose when assigning traffic (read only).",
    "switch-controller-iot-scanning": "Enable/disable managed FortiSwitch IoT scanning.",
    "switch-controller-offload": "Enable/disable managed FortiSwitch routing offload.",
    "switch-controller-offload-ip": "IP for routing offload on FortiSwitch.",
    "switch-controller-offload-gw": "Enable/disable managed FortiSwitch routing offload gateway.",
    "swc-vlan": "Creation status for switch-controller VLANs.",
    "swc-first-create": "Initial create for switch-controller VLANs.",
    "color": "Color of icon on the GUI.",
    "tagging": "Config object tagging.",
    "eap-supplicant": "Enable/disable EAP-Supplicant.",
    "eap-method": "EAP method.",
    "eap-identity": "EAP identity.",
    "eap-password": "EAP password.",
    "eap-ca-cert": "EAP CA certificate name.",
    "eap-user-cert": "EAP user certificate name.",
    "default-purdue-level": "default purdue level of device detected on this interface.",
    "ipv6": "IPv6 of interface.",
    "physical": "Print physical interface information.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "vdom": {"type": "string", "max_length": 31},
    "vrf": {"type": "integer", "min": 0, "max": 511},
    "cli-conn-status": {"type": "integer", "min": 0, "max": 4294967295},
    "distance": {"type": "integer", "min": 1, "max": 255},
    "priority": {"type": "integer", "min": 1, "max": 65535},
    "dhcp-relay-interface": {"type": "string", "max_length": 15},
    "dhcp-relay-vrf-select": {"type": "integer", "min": 0, "max": 511},
    "dhcp-relay-circuit-id": {"type": "string", "max_length": 64},
    "ping-serv-status": {"type": "integer", "min": 0, "max": 255},
    "ha-priority": {"type": "integer", "min": 1, "max": 50},
    "dhcp-client-identifier": {"type": "string", "max_length": 48},
    "dhcp-renew-time": {"type": "integer", "min": 300, "max": 604800},
    "username": {"type": "string", "max_length": 64},
    "idle-timeout": {"type": "integer", "min": 0, "max": 32767},
    "mrru": {"type": "integer", "min": 296, "max": 65535},
    "detected-peer-mtu": {"type": "integer", "min": 0, "max": 4294967295},
    "disc-retry-timeout": {"type": "integer", "min": 0, "max": 4294967295},
    "padt-retry-timeout": {"type": "integer", "min": 0, "max": 4294967295},
    "service-name": {"type": "string", "max_length": 63},
    "ac-name": {"type": "string", "max_length": 63},
    "lcp-echo-interval": {"type": "integer", "min": 0, "max": 32767},
    "lcp-max-echo-fails": {"type": "integer", "min": 0, "max": 32767},
    "pptp-user": {"type": "string", "max_length": 64},
    "pptp-timeout": {"type": "integer", "min": 0, "max": 65535},
    "bfd-desired-min-tx": {"type": "integer", "min": 1, "max": 100000},
    "bfd-detect-mult": {"type": "integer", "min": 1, "max": 50},
    "bfd-required-min-rx": {"type": "integer", "min": 1, "max": 100000},
    "reachable-time": {"type": "integer", "min": 30000, "max": 3600000},
    "ring-rx": {"type": "integer", "min": 0, "max": 4294967295},
    "ring-tx": {"type": "integer", "min": 0, "max": 4294967295},
    "netflow-sample-rate": {"type": "integer", "min": 1, "max": 65535},
    "netflow-sampler-id": {"type": "integer", "min": 1, "max": 254},
    "sample-rate": {"type": "integer", "min": 10, "max": 99999},
    "polling-interval": {"type": "integer", "min": 1, "max": 255},
    "tcp-mss": {"type": "integer", "min": 48, "max": 65535},
    "inbandwidth": {"type": "integer", "min": 0, "max": 80000000},
    "outbandwidth": {"type": "integer", "min": 0, "max": 80000000},
    "egress-shaping-profile": {"type": "string", "max_length": 35},
    "ingress-shaping-profile": {"type": "string", "max_length": 35},
    "spillover-threshold": {"type": "integer", "min": 0, "max": 16776000},
    "ingress-spillover-threshold": {"type": "integer", "min": 0, "max": 16776000},
    "weight": {"type": "integer", "min": 0, "max": 255},
    "interface": {"type": "string", "max_length": 15},
    "mtu": {"type": "integer", "min": 0, "max": 4294967295},
    "vlanid": {"type": "integer", "min": 1, "max": 4094},
    "forward-domain": {"type": "integer", "min": 0, "max": 2147483647},
    "min-links": {"type": "integer", "min": 1, "max": 32},
    "link-up-delay": {"type": "integer", "min": 50, "max": 3600000},
    "aggregate": {"type": "string", "max_length": 15},
    "redundant-interface": {"type": "string", "max_length": 15},
    "devindex": {"type": "integer", "min": 0, "max": 4294967295},
    "vindex": {"type": "integer", "min": 0, "max": 65535},
    "switch": {"type": "string", "max_length": 15},
    "alias": {"type": "string", "max_length": 25},
    "security-external-logout": {"type": "string", "max_length": 127},
    "replacemsg-override-group": {"type": "string", "max_length": 35},
    "auth-cert": {"type": "string", "max_length": 35},
    "auth-portal-addr": {"type": "string", "max_length": 63},
    "security-exempt-list": {"type": "string", "max_length": 35},
    "ike-saml-server": {"type": "string", "max_length": 35},
    "lldp-network-policy": {"type": "string", "max_length": 35},
    "estimated-upstream-bandwidth": {"type": "integer", "min": 0, "max": 4294967295},
    "estimated-downstream-bandwidth": {"type": "integer", "min": 0, "max": 4294967295},
    "measured-upstream-bandwidth": {"type": "integer", "min": 0, "max": 4294967295},
    "measured-downstream-bandwidth": {"type": "integer", "min": 0, "max": 4294967295},
    "bandwidth-measure-time": {"type": "integer", "min": 0, "max": 4294967295},
    "snmp-index": {"type": "integer", "min": 0, "max": 2147483647},
    "internal": {"type": "integer", "min": 0, "max": 255},
    "fortilink-backup-link": {"type": "integer", "min": 0, "max": 255},
    "switch-controller-traffic-policy": {"type": "string", "max_length": 63},
    "switch-controller-mgmt-vlan": {"type": "integer", "min": 1, "max": 4094},
    "switch-controller-learning-limit": {"type": "integer", "min": 0, "max": 128},
    "switch-controller-nac": {"type": "string", "max_length": 35},
    "switch-controller-dynamic": {"type": "string", "max_length": 35},
    "swc-vlan": {"type": "integer", "min": 0, "max": 4294967295},
    "swc-first-create": {"type": "integer", "min": 0, "max": 4294967295},
    "color": {"type": "integer", "min": 0, "max": 32},
    "eap-identity": {"type": "string", "max_length": 35},
    "eap-ca-cert": {"type": "string", "max_length": 79},
    "eap-user-cert": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "client-options": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "code": {
            "type": "integer",
            "help": "DHCP client option code.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "type": {
            "type": "option",
            "help": "DHCP client option type.",
            "default": "hex",
            "options": [{"help": "DHCP option in hex.", "label": "Hex", "name": "hex"}, {"help": "DHCP option in string.", "label": "String", "name": "string"}, {"help": "DHCP option in IP.", "label": "Ip", "name": "ip"}, {"help": "DHCP option in domain search option format.", "label": "Fqdn", "name": "fqdn"}],
        },
        "value": {
            "type": "string",
            "help": "DHCP client option value.",
            "default": "",
            "max_length": 312,
        },
        "ip": {
            "type": "user",
            "help": "DHCP option IPs.",
            "default": "",
        },
    },
    "fail-alert-interfaces": {
        "name": {
            "type": "string",
            "help": "Names of the non-virtual interface.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
    },
    "member": {
        "interface-name": {
            "type": "string",
            "help": "Physical interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "security-groups": {
        "name": {
            "type": "string",
            "help": "Names of user groups that can authenticate with the captive portal.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "vrrp": {
        "vrid": {
            "type": "integer",
            "help": "Virtual router identifier (1 - 255).",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 255,
        },
        "version": {
            "type": "option",
            "help": "VRRP version.",
            "default": "2",
            "options": [{"help": "VRRP version 2.", "label": "2", "name": "2"}, {"help": "VRRP version 3.", "label": "3", "name": "3"}],
        },
        "vrgrp": {
            "type": "integer",
            "help": "VRRP group ID (1 - 65535).",
            "default": 0,
            "min_value": 1,
            "max_value": 65535,
        },
        "vrip": {
            "type": "ipv4-address-any",
            "help": "IP address of the virtual router.",
            "required": True,
            "default": "0.0.0.0",
        },
        "priority": {
            "type": "integer",
            "help": "Priority of the virtual router (1 - 255).",
            "default": 100,
            "min_value": 1,
            "max_value": 255,
        },
        "adv-interval": {
            "type": "integer",
            "help": "Advertisement interval (250 - 255000 milliseconds).",
            "default": 1000,
            "min_value": 250,
            "max_value": 255000,
        },
        "start-time": {
            "type": "integer",
            "help": "Startup time (1 - 255 seconds).",
            "default": 3,
            "min_value": 1,
            "max_value": 255,
        },
        "preempt": {
            "type": "option",
            "help": "Enable/disable preempt mode.",
            "default": "enable",
            "options": [{"help": "Enable preempt mode.", "label": "Enable", "name": "enable"}, {"help": "Disable preempt mode.", "label": "Disable", "name": "disable"}],
        },
        "accept-mode": {
            "type": "option",
            "help": "Enable/disable accept mode.",
            "default": "enable",
            "options": [{"help": "Enable accept mode.", "label": "Enable", "name": "enable"}, {"help": "Disable accept mode.", "label": "Disable", "name": "disable"}],
        },
        "vrdst": {
            "type": "ipv4-address-any",
            "help": "Monitor the route to this destination.",
            "default": "",
        },
        "vrdst-priority": {
            "type": "integer",
            "help": "Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254).",
            "default": 0,
            "min_value": 0,
            "max_value": 254,
        },
        "ignore-default-route": {
            "type": "option",
            "help": "Enable/disable ignoring of default route when checking destination.",
            "default": "disable",
            "options": [{"help": "Ignore default route when checking destination.", "label": "Enable", "name": "enable"}, {"help": "Do not ignore default route when checking destination.", "label": "Disable", "name": "disable"}],
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this VRRP configuration.",
            "default": "enable",
            "options": [{"help": "Enable this VRRP configuration.", "label": "Enable", "name": "enable"}, {"help": "Disable this VRRP configuration.", "label": "Disable", "name": "disable"}],
        },
        "proxy-arp": {
            "type": "string",
            "help": "VRRP Proxy ARP configuration.",
        },
    },
    "phy-setting": {
        "signal-ok-threshold": {
            "type": "integer",
            "help": "Configure the signal strength value at which the FortiGate unit detects that the receiving signal is idle or that data is not being received. Zero means idle detection is disabled. Higher values mean the signal strength must be higher in order for the FortiGate unit to consider the interface is not idle (0 - 12, default = 0).",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 12,
        },
    },
    "secondaryip": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip": {
            "type": "ipv4-classnet-host",
            "help": "Secondary IP address of the interface.",
            "default": "0.0.0.0 0.0.0.0",
        },
        "secip-relay-ip": {
            "type": "user",
            "help": "DHCP relay IP address.",
            "default": "",
        },
        "allowaccess": {
            "type": "option",
            "help": "Management access settings for the secondary IP address.",
            "default": "",
            "options": [{"help": "PING access.", "label": "Ping", "name": "ping"}, {"help": "HTTPS access.", "label": "Https", "name": "https"}, {"help": "SSH access.", "label": "Ssh", "name": "ssh"}, {"help": "SNMP access.", "label": "Snmp", "name": "snmp"}, {"help": "HTTP access.", "label": "Http", "name": "http"}, {"help": "TELNET access.", "label": "Telnet", "name": "telnet"}, {"help": "FortiManager access.", "label": "Fgfm", "name": "fgfm"}, {"help": "RADIUS accounting access.", "label": "Radius Acct", "name": "radius-acct"}, {"help": "Probe access.", "label": "Probe Response", "name": "probe-response"}, {"help": "Security Fabric access.", "label": "Fabric", "name": "fabric"}, {"help": "FTM access.", "label": "Ftm", "name": "ftm"}, {"help": "Speed test access.", "label": "Speed Test", "name": "speed-test"}, {"help": "System for Cross-domain Identity Management (SCIM) access.", "label": "Scim", "name": "scim"}],
        },
        "gwdetect": {
            "type": "option",
            "help": "Enable/disable detect gateway alive for first.",
            "default": "disable",
            "options": [{"help": "Enable detect gateway alive for first.", "label": "Enable", "name": "enable"}, {"help": "Disable detect gateway alive for first.", "label": "Disable", "name": "disable"}],
        },
        "ping-serv-status": {
            "type": "integer",
            "help": "PING server status.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "detectserver": {
            "type": "user",
            "help": "Gateway's ping server for this IP.",
            "default": "",
        },
        "detectprotocol": {
            "type": "option",
            "help": "Protocols used to detect the server.",
            "default": "ping",
            "options": [{"help": "PING.", "label": "Ping", "name": "ping"}, {"help": "TCP echo.", "label": "Tcp Echo", "name": "tcp-echo"}, {"help": "UDP echo.", "label": "Udp Echo", "name": "udp-echo"}],
        },
        "ha-priority": {
            "type": "integer",
            "help": "HA election priority for the PING server.",
            "default": 1,
            "min_value": 1,
            "max_value": 50,
        },
    },
    "dhcp-snooping-server-list": {
        "name": {
            "type": "string",
            "help": "DHCP server name.",
            "default": "default",
            "max_length": 35,
        },
        "server-ip": {
            "type": "ipv4-address",
            "help": "IP address for DHCP server.",
            "default": "0.0.0.0",
        },
    },
    "tagging": {
        "name": {
            "type": "string",
            "help": "Tagging entry name.",
            "default": "",
            "max_length": 63,
        },
        "category": {
            "type": "string",
            "help": "Tag category.",
            "default": "",
            "max_length": 63,
        },
        "tags": {
            "type": "string",
            "help": "Tags.",
        },
    },
    "ipv6": {
        "ip6-mode": {
            "type": "option",
            "help": "Addressing mode (static, DHCP, delegated).",
            "default": "static",
            "options": [{"help": "Static setting.", "label": "Static", "name": "static"}, {"help": "DHCPv6 client mode.", "label": "Dhcp", "name": "dhcp"}, {"help": "IPv6 over PPPoE mode.", "label": "Pppoe", "name": "pppoe"}, {"help": "IPv6 address with delegated prefix.", "label": "Delegated", "name": "delegated"}],
        },
        "client-options": {
            "type": "string",
            "help": "DHCP6 client options.",
        },
        "nd-mode": {
            "type": "option",
            "help": "Neighbor discovery mode.",
            "default": "basic",
            "options": [{"help": "Do not support SEND.", "label": "Basic", "name": "basic"}, {"help": "Support SEND.", "label": "Send Compatible", "name": "SEND-compatible"}],
        },
        "nd-cert": {
            "type": "string",
            "help": "Neighbor discovery certificate.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "nd-security-level": {
            "type": "integer",
            "help": "Neighbor discovery security level (0 - 7; 0 = least secure, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 7,
        },
        "nd-timestamp-delta": {
            "type": "integer",
            "help": "Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300).",
            "default": 300,
            "min_value": 1,
            "max_value": 3600,
        },
        "nd-timestamp-fuzz": {
            "type": "integer",
            "help": "Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1).",
            "default": 1,
            "min_value": 1,
            "max_value": 60,
        },
        "nd-cga-modifier": {
            "type": "user",
            "help": "Neighbor discovery CGA modifier.",
            "default": "",
        },
        "ip6-dns-server-override": {
            "type": "option",
            "help": "Enable/disable using the DNS server acquired by DHCP.",
            "default": "enable",
            "options": [{"help": "Enable using the DNS server acquired by DHCP.", "label": "Enable", "name": "enable"}, {"help": "Disable using the DNS server acquired by DHCP.", "label": "Disable", "name": "disable"}],
        },
        "ip6-address": {
            "type": "ipv6-prefix",
            "help": "Primary IPv6 address prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.",
            "default": "::/0",
        },
        "ip6-extra-addr": {
            "type": "string",
            "help": "Extra IPv6 address prefixes of interface.",
        },
        "ip6-allowaccess": {
            "type": "option",
            "help": "Allow management access to the interface.",
            "default": "",
            "options": [{"help": "PING access.", "label": "Ping", "name": "ping"}, {"help": "HTTPS access.", "label": "Https", "name": "https"}, {"help": "SSH access.", "label": "Ssh", "name": "ssh"}, {"help": "SNMP access.", "label": "Snmp", "name": "snmp"}, {"help": "HTTP access.", "label": "Http", "name": "http"}, {"help": "TELNET access.", "label": "Telnet", "name": "telnet"}, {"help": "FortiManager access.", "label": "Fgfm", "name": "fgfm"}, {"help": "Security Fabric access.", "label": "Fabric", "name": "fabric"}, {"help": "System for Cross-domain Identity Management (SCIM) access.", "label": "Scim", "name": "scim"}, {"help": "Probe access.", "label": "Probe Response", "name": "probe-response"}],
        },
        "ip6-send-adv": {
            "type": "option",
            "help": "Enable/disable sending advertisements about the interface.",
            "default": "disable",
            "options": [{"help": "Enable sending advertisements about this interface.", "label": "Enable", "name": "enable"}, {"help": "Disable sending advertisements about this interface.", "label": "Disable", "name": "disable"}],
        },
        "icmp6-send-redirect": {
            "type": "option",
            "help": "Enable/disable sending of ICMPv6 redirects.",
            "default": "enable",
            "options": [{"help": "Enable sending of ICMPv6 redirects.", "label": "Enable", "name": "enable"}, {"help": "Disable sending of ICMPv6 redirects.", "label": "Disable", "name": "disable"}],
        },
        "ip6-manage-flag": {
            "type": "option",
            "help": "Enable/disable the managed flag.",
            "default": "disable",
            "options": [{"help": "Enable the managed IPv6 flag.", "label": "Enable", "name": "enable"}, {"help": "Disable the managed IPv6 flag.", "label": "Disable", "name": "disable"}],
        },
        "ip6-other-flag": {
            "type": "option",
            "help": "Enable/disable the other IPv6 flag.",
            "default": "disable",
            "options": [{"help": "Enable the other IPv6 flag.", "label": "Enable", "name": "enable"}, {"help": "Disable the other IPv6 flag.", "label": "Disable", "name": "disable"}],
        },
        "ip6-max-interval": {
            "type": "integer",
            "help": "IPv6 maximum interval (4 to 1800 sec).",
            "default": 600,
            "min_value": 4,
            "max_value": 1800,
        },
        "ip6-min-interval": {
            "type": "integer",
            "help": "IPv6 minimum interval (3 to 1350 sec).",
            "default": 198,
            "min_value": 3,
            "max_value": 1350,
        },
        "ip6-link-mtu": {
            "type": "integer",
            "help": "IPv6 link MTU.",
            "default": 0,
            "min_value": 1280,
            "max_value": 16000,
        },
        "ra-send-mtu": {
            "type": "option",
            "help": "Enable/disable sending link MTU in RA packet.",
            "default": "enable",
            "options": [{"help": "Enable sending link MTU in RA packet.", "label": "Enable", "name": "enable"}, {"help": "Disable sending link MTU in RA packet.", "label": "Disable", "name": "disable"}],
        },
        "ip6-reachable-time": {
            "type": "integer",
            "help": "IPv6 reachable time (milliseconds; 0 means unspecified).",
            "default": 0,
            "min_value": 0,
            "max_value": 3600000,
        },
        "ip6-retrans-time": {
            "type": "integer",
            "help": "IPv6 retransmit time (milliseconds; 0 means unspecified).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip6-default-life": {
            "type": "integer",
            "help": "Default life (sec).",
            "default": 1800,
            "min_value": 0,
            "max_value": 9000,
        },
        "ip6-hop-limit": {
            "type": "integer",
            "help": "Hop limit (0 means unspecified).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "ip6-adv-rio": {
            "type": "option",
            "help": "Enable/disable sending advertisements with route information option.",
            "default": "disable",
            "options": [{"help": "Enable sending advertisements with route information option.", "label": "Enable", "name": "enable"}, {"help": "Disable sending advertisements with route information option.", "label": "Disable", "name": "disable"}],
        },
        "ip6-route-pref": {
            "type": "option",
            "help": "Set route preference to the interface (default = medium).",
            "default": "medium",
            "options": [{"help": "Medium route preferences in RA packet.", "label": "Medium", "name": "medium"}, {"help": "High route preferences in RA packet.", "label": "High", "name": "high"}, {"help": "Low route preferences in RA packet.", "label": "Low", "name": "low"}],
        },
        "ip6-route-list": {
            "type": "string",
            "help": "Advertised route list.",
        },
        "autoconf": {
            "type": "option",
            "help": "Enable/disable address auto config.",
            "default": "disable",
            "options": [{"help": "Enable auto-configuration.", "label": "Enable", "name": "enable"}, {"help": "Disable auto-configuration.", "label": "Disable", "name": "disable"}],
        },
        "unique-autoconf-addr": {
            "type": "option",
            "help": "Enable/disable unique auto config address.",
            "default": "disable",
            "options": [{"help": "Enable unique auto-configuration address.", "label": "Enable", "name": "enable"}, {"help": "Disable unique auto-configuration address.", "label": "Disable", "name": "disable"}],
        },
        "interface-identifier": {
            "type": "ipv6-address",
            "help": "IPv6 interface identifier.",
            "default": "::",
        },
        "ip6-prefix-mode": {
            "type": "option",
            "help": "Assigning a prefix from DHCP or RA.",
            "default": "dhcp6",
            "options": [{"help": "Use delegated prefix from a DHCPv6 client to form a delegated IPv6 address.", "label": "Dhcp6", "name": "dhcp6"}, {"help": "Use prefix from RA to form a delegated IPv6 address.", "label": "Ra", "name": "ra"}],
        },
        "ip6-delegated-prefix-iaid": {
            "type": "integer",
            "help": "IAID of obtained delegated-prefix from the upstream interface.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "ip6-upstream-interface": {
            "type": "string",
            "help": "Interface name providing delegated information.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "ip6-subnet": {
            "type": "ipv6-prefix",
            "help": "Subnet to routing prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.",
            "default": "::/0",
        },
        "ip6-prefix-list": {
            "type": "string",
            "help": "Advertised prefix list.",
        },
        "ip6-rdnss-list": {
            "type": "string",
            "help": "Advertised IPv6 RDNSS list.",
        },
        "ip6-dnssl-list": {
            "type": "string",
            "help": "Advertised IPv6 DNSS list.",
        },
        "ip6-delegated-prefix-list": {
            "type": "string",
            "help": "Advertised IPv6 delegated prefix list.",
        },
        "dhcp6-relay-service": {
            "type": "option",
            "help": "Enable/disable DHCPv6 relay.",
            "default": "disable",
            "options": [{"help": "Disable DHCPv6 relay", "label": "Disable", "name": "disable"}, {"help": "Enable DHCPv6 relay.", "label": "Enable", "name": "enable"}],
        },
        "dhcp6-relay-type": {
            "type": "option",
            "help": "DHCPv6 relay type.",
            "default": "regular",
            "options": [{"help": "Regular DHCP relay.", "label": "Regular", "name": "regular"}],
        },
        "dhcp6-relay-source-interface": {
            "type": "option",
            "help": "Enable/disable use of address on this interface as the source address of the relay message.",
            "default": "disable",
            "options": [{"help": "Use address of the egress interface as source address of the relay message.", "label": "Disable", "name": "disable"}, {"help": "Use address of this interface as source address of the relay message.", "label": "Enable", "name": "enable"}],
        },
        "dhcp6-relay-ip": {
            "type": "user",
            "help": "DHCPv6 relay IP address.",
            "default": "",
        },
        "dhcp6-relay-source-ip": {
            "type": "ipv6-address",
            "help": "IPv6 address used by the DHCP6 relay as its source IP.",
            "default": "::",
        },
        "dhcp6-relay-interface-id": {
            "type": "string",
            "help": "DHCP6 relay interface ID.",
            "default": "",
            "max_length": 64,
        },
        "dhcp6-client-options": {
            "type": "option",
            "help": "DHCPv6 client options.",
            "default": "",
            "options": [{"help": "Send rapid commit option.", "label": "Rapid", "name": "rapid"}, {"help": "Send including IA-PD option.", "label": "Iapd", "name": "iapd"}, {"help": "Send including IA-NA option.", "label": "Iana", "name": "iana"}],
        },
        "dhcp6-prefix-delegation": {
            "type": "option",
            "help": "Enable/disable DHCPv6 prefix delegation.",
            "default": "disable",
            "options": [{"help": "Enable DHCPv6 prefix delegation.", "label": "Enable", "name": "enable"}, {"help": "Disable DHCPv6 prefix delegation.", "label": "Disable", "name": "disable"}],
        },
        "dhcp6-information-request": {
            "type": "option",
            "help": "Enable/disable DHCPv6 information request.",
            "default": "disable",
            "options": [{"help": "Enable DHCPv6 information request.", "label": "Enable", "name": "enable"}, {"help": "Disable DHCPv6 information request.", "label": "Disable", "name": "disable"}],
        },
        "dhcp6-iapd-list": {
            "type": "string",
            "help": "DHCPv6 IA-PD list.",
        },
        "cli-conn6-status": {
            "type": "integer",
            "help": "CLI IPv6 connection status.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "vrrp-virtual-mac6": {
            "type": "option",
            "help": "Enable/disable virtual MAC for VRRP.",
            "default": "disable",
            "options": [{"help": "Enable virtual MAC for VRRP.", "label": "Enable", "name": "enable"}, {"help": "Disable virtual MAC for VRRP.", "label": "Disable", "name": "disable"}],
        },
        "vrip6_link_local": {
            "type": "ipv6-address",
            "help": "Link-local IPv6 address of virtual router.",
            "default": "::",
        },
        "vrrp6": {
            "type": "string",
            "help": "IPv6 VRRP configuration.",
        },
    },
    "physical": {
        "<interface>": {
            "type": "value",
            "help": "Interface name.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FORTILINK = [
    "enable",  # Enable FortiLink to dedicated interface for managing FortiSwitch devices.
    "disable",  # Disable FortiLink to dedicated interface for managing FortiSwitch devices.
]
VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP = [
    "outbound",  # Source IP address is that of the outbound interface.
    "fixed",  # Source IP address is that of the FortiLink interface.
]
VALID_BODY_MODE = [
    "static",  # Static setting.
    "dhcp",  # External DHCP client mode.
    "pppoe",  # External PPPoE mode.
]
VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD = [
    "auto",  # Set outgoing interface automatically.
    "sdwan",  # Set outgoing interface by SD-WAN or policy routing rules.
    "specify",  # Set outgoing interface manually.
]
VALID_BODY_DHCP_BROADCAST_FLAG = [
    "disable",  # Disable broadcast flag.
    "enable",  # Enable broadcast flag.
]
VALID_BODY_DHCP_RELAY_SERVICE = [
    "disable",  # None.
    "enable",  # DHCP relay agent.
]
VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER = [
    "disable",  # Send DHCP requests only to a matching server.
    "enable",  # Send DHCP requests to all servers.
]
VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION = [
    "disable",  # Disable relaying DHCP messages with no end option.
    "enable",  # Enable relaying DHCP messages with no end option.
]
VALID_BODY_DHCP_RELAY_TYPE = [
    "regular",  # Regular DHCP relay.
    "ipsec",  # DHCP relay for IPsec.
]
VALID_BODY_DHCP_SMART_RELAY = [
    "disable",  # Disable DHCP smart relay.
    "enable",  # Enable DHCP smart relay.
]
VALID_BODY_DHCP_RELAY_AGENT_OPTION = [
    "enable",  # Enable DHCP relay agent option.
    "disable",  # Disable DHCP relay agent option.
]
VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION = [
    "enable",  # Enable addition of classless static routes retrieved from DHCP server.
    "disable",  # Disable addition of classless static routes retrieved from DHCP server.
]
VALID_BODY_ALLOWACCESS = [
    "ping",  # PING access.
    "https",  # HTTPS access.
    "ssh",  # SSH access.
    "snmp",  # SNMP access.
    "http",  # HTTP access.
    "telnet",  # TELNET access.
    "fgfm",  # FortiManager access.
    "radius-acct",  # RADIUS accounting access.
    "probe-response",  # Probe access.
    "fabric",  # Security Fabric access.
    "ftm",  # FTM access.
    "speed-test",  # Speed test access.
    "scim",  # System for Cross-domain Identity Management (SCIM) access.
]
VALID_BODY_GWDETECT = [
    "enable",  # Enable detect gateway alive for first.
    "disable",  # Disable detect gateway alive for first.
]
VALID_BODY_DETECTPROTOCOL = [
    "ping",  # PING.
    "tcp-echo",  # TCP echo.
    "udp-echo",  # UDP echo.
]
VALID_BODY_FAIL_DETECT = [
    "enable",  # Enable interface failed option status.
    "disable",  # Disable interface failed option status.
]
VALID_BODY_FAIL_DETECT_OPTION = [
    "detectserver",  # Use a ping server to determine if the interface has failed.
    "link-down",  # Use port detection to determine if the interface has failed.
]
VALID_BODY_FAIL_ALERT_METHOD = [
    "link-failed-signal",  # Link-failed-signal.
    "link-down",  # Link-down.
]
VALID_BODY_FAIL_ACTION_ON_EXTENDER = [
    "soft-restart",  # Soft-restart-on-extender.
    "hard-restart",  # Hard-restart-on-extender.
    "reboot",  # Reboot-on-extender.
]
VALID_BODY_PPPOE_EGRESS_COS = [
    "cos0",  # CoS 0.
    "cos1",  # CoS 1.
    "cos2",  # CoS 2.
    "cos3",  # CoS 3.
    "cos4",  # CoS 4.
    "cos5",  # CoS 5.
    "cos6",  # CoS 6.
    "cos7",  # CoS 7.
]
VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE = [
    "enable",  # Enable IP address negotiating for unnumbered.
    "disable",  # Disable IP address negotiating for unnumbered.
]
VALID_BODY_MULTILINK = [
    "enable",  # Enable PPP multilink support.
    "disable",  # Disable PPP multilink support.
]
VALID_BODY_DEFAULTGW = [
    "enable",  # Enable default gateway.
    "disable",  # Disable default gateway.
]
VALID_BODY_DNS_SERVER_OVERRIDE = [
    "enable",  # Use DNS acquired by DHCP or PPPoE.
    "disable",  # No not use DNS acquired by DHCP or PPPoE.
]
VALID_BODY_DNS_SERVER_PROTOCOL = [
    "cleartext",  # DNS over UDP/53, DNS over TCP/53.
    "dot",  # DNS over TLS/853.
    "doh",  # DNS over HTTPS/443.
]
VALID_BODY_AUTH_TYPE = [
    "auto",  # Automatically choose authentication.
    "pap",  # PAP authentication.
    "chap",  # CHAP authentication.
    "mschapv1",  # MS-CHAPv1 authentication.
    "mschapv2",  # MS-CHAPv2 authentication.
]
VALID_BODY_PPTP_CLIENT = [
    "enable",  # Enable PPTP client.
    "disable",  # Disable PPTP client.
]
VALID_BODY_PPTP_AUTH_TYPE = [
    "auto",  # Automatically choose authentication.
    "pap",  # PAP authentication.
    "chap",  # CHAP authentication.
    "mschapv1",  # MS-CHAPv1 authentication.
    "mschapv2",  # MS-CHAPv2 authentication.
]
VALID_BODY_ARPFORWARD = [
    "enable",  # Enable ARP forwarding.
    "disable",  # Disable ARP forwarding.
]
VALID_BODY_NDISCFORWARD = [
    "enable",  # Enable NDISC forwarding.
    "disable",  # Disable NDISC forwarding.
]
VALID_BODY_BROADCAST_FORWARD = [
    "enable",  # Enable broadcast forwarding.
    "disable",  # Disable broadcast forwarding.
]
VALID_BODY_BFD = [
    "global",  # BFD behavior of this interface will be based on global configuration.
    "enable",  # Enable BFD on this interface and ignore global configuration.
    "disable",  # Disable BFD on this interface and ignore global configuration.
]
VALID_BODY_L2FORWARD = [
    "enable",  # Enable L2 forwarding.
    "disable",  # Disable L2 forwarding.
]
VALID_BODY_ICMP_SEND_REDIRECT = [
    "enable",  # Enable sending of ICMP redirects.
    "disable",  # Disable sending of ICMP redirects.
]
VALID_BODY_ICMP_ACCEPT_REDIRECT = [
    "enable",  # Enable ICMP accept redirect.
    "disable",  # Disable ICMP accept redirect.
]
VALID_BODY_VLANFORWARD = [
    "enable",  # Enable traffic forwarding.
    "disable",  # Disable traffic forwarding.
]
VALID_BODY_STPFORWARD = [
    "enable",  # Enable STP forwarding.
    "disable",  # Disable STP forwarding.
]
VALID_BODY_STPFORWARD_MODE = [
    "rpl-all-ext-id",  # Replace all extension IDs (root, bridge).
    "rpl-bridge-ext-id",  # Replace the bridge extension ID only.
    "rpl-nothing",  # Replace nothing.
]
VALID_BODY_IPS_SNIFFER_MODE = [
    "enable",  # Enable IPS sniffer mode.
    "disable",  # Disable IPS sniffer mode.
]
VALID_BODY_IDENT_ACCEPT = [
    "enable",  # Enable determining a user's identity from packet identification.
    "disable",  # Disable determining a user's identity from packet identification.
]
VALID_BODY_IPMAC = [
    "enable",  # Enable IP/MAC binding.
    "disable",  # Disable IP/MAC binding.
]
VALID_BODY_SUBST = [
    "enable",  # Send packets from this interface.
    "disable",  # Do not send packets from this interface.
]
VALID_BODY_SPEED = [
    "auto",  # Automatically adjust speed.
    "10full",  # 10M full-duplex.
    "10half",  # 10M half-duplex.
    "100full",  # 100M full-duplex.
    "100half",  # 100M half-duplex.
    "100auto",  # 100M auto-negotiation.
    "1000full",  # 1000M full-duplex.
    "1000auto",  # 1000M auto adjust.
]
VALID_BODY_STATUS = [
    "up",  # Bring the interface up.
    "down",  # Shut the interface down.
]
VALID_BODY_NETBIOS_FORWARD = [
    "disable",  # Disable NETBIOS forwarding.
    "enable",  # Enable NETBIOS forwarding.
]
VALID_BODY_TYPE = [
    "physical",  # Physical interface.
    "vlan",  # VLAN interface.
    "aggregate",  # Aggregate interface.
    "redundant",  # Redundant interface.
    "tunnel",  # Tunnel interface.
    "vdom-link",  # VDOM link interface.
    "loopback",  # Loopback interface.
    "switch",  # Software switch interface.
    "vap-switch",  # VAP interface.
    "wl-mesh",  # WLAN mesh interface.
    "fext-wan",  # FortiExtender interface.
    "vxlan",  # VXLAN interface.
    "geneve",  # GENEVE interface.
    "switch-vlan",  # Switch VLAN interface.
    "emac-vlan",  # EMAC VLAN interface.
    "lan-extension",  # LAN extension interface.
]
VALID_BODY_DEDICATED_TO = [
    "none",  # Interface not dedicated for any purpose.
    "management",  # Dedicate this interface for management purposes only.
]
VALID_BODY_WCCP = [
    "enable",  # Enable WCCP protocol on this interface.
    "disable",  # Disable WCCP protocol on this interface.
]
VALID_BODY_NETFLOW_SAMPLER = [
    "disable",  # Disable NetFlow protocol on this interface.
    "tx",  # Monitor transmitted traffic on this interface.
    "rx",  # Monitor received traffic on this interface.
    "both",  # Monitor transmitted/received traffic on this interface.
]
VALID_BODY_SFLOW_SAMPLER = [
    "enable",  # Enable sFlow protocol on this interface.
    "disable",  # Disable sFlow protocol on this interface.
]
VALID_BODY_DROP_FRAGMENT = [
    "enable",  # Enable/disable drop fragment packets.
    "disable",  # Do not drop fragment packets.
]
VALID_BODY_SRC_CHECK = [
    "enable",  # Enable source IP check.
    "disable",  # Disable source IP check.
]
VALID_BODY_SAMPLE_DIRECTION = [
    "tx",  # Monitor transmitted traffic on this interface.
    "rx",  # Monitor received traffic on this interface.
    "both",  # Monitor transmitted/received traffic on this interface.
]
VALID_BODY_EXPLICIT_WEB_PROXY = [
    "enable",  # Enable explicit Web proxy on this interface.
    "disable",  # Disable explicit Web proxy on this interface.
]
VALID_BODY_EXPLICIT_FTP_PROXY = [
    "enable",  # Enable explicit FTP proxy on this interface.
    "disable",  # Disable explicit FTP proxy on this interface.
]
VALID_BODY_PROXY_CAPTIVE_PORTAL = [
    "enable",  # Enable proxy captive portal on this interface.
    "disable",  # Disable proxy captive portal on this interface.
]
VALID_BODY_EXTERNAL = [
    "enable",  # Enable identifying the interface as an external interface.
    "disable",  # Disable identifying the interface as an external interface.
]
VALID_BODY_MTU_OVERRIDE = [
    "enable",  # Override default MTU.
    "disable",  # Use default MTU.
]
VALID_BODY_VLAN_PROTOCOL = [
    "8021q",  # IEEE 802.1Q.
    "8021ad",  # IEEE 802.1AD.
]
VALID_BODY_LACP_MODE = [
    "static",  # Use static aggregation, do not send and ignore any LACP messages.
    "passive",  # Passively use LACP to negotiate 802.3ad aggregation.
    "active",  # Actively use LACP to negotiate 802.3ad aggregation.
]
VALID_BODY_LACP_HA_SECONDARY = [
    "enable",  # Allow HA secondary member to send/receive LACP messages.
    "disable",  # Block HA secondary member from sending/receiving LACP messages.
]
VALID_BODY_SYSTEM_ID_TYPE = [
    "auto",  # Use the MAC address of the first member.
    "user",  # User-defined system ID.
]
VALID_BODY_LACP_SPEED = [
    "slow",  # Send LACP message every 30 seconds.
    "fast",  # Send LACP message every second.
]
VALID_BODY_MIN_LINKS_DOWN = [
    "operational",  # Set the aggregate operationally down.
    "administrative",  # Set the aggregate administratively down.
]
VALID_BODY_ALGORITHM = [
    "L2",  # Use layer 2 address for distribution.
    "L3",  # Use layer 3 address for distribution.
    "L4",  # Use layer 4 information for distribution.
    "NPU-GRE",  # Use L4 and GRE inner header information for distribution.
    "Source-MAC",  # Use source MAC address for distribution.
]
VALID_BODY_AGGREGATE_TYPE = [
    "physical",  # Physical interface aggregation.
    "vxlan",  # VXLAN interface aggregation.
]
VALID_BODY_PRIORITY_OVERRIDE = [
    "enable",  # Enable fail back to higher priority port once recovered.
    "disable",  # Disable fail back to higher priority port once recovered.
]
VALID_BODY_SECURITY_MODE = [
    "none",  # No security option.
    "captive-portal",  # Captive portal authentication.
    "802.1X",  # 802.1X port-based authentication.
]
VALID_BODY_SECURITY_MAC_AUTH_BYPASS = [
    "mac-auth-only",  # Enable MAC authentication bypass without EAP.
    "enable",  # Enable MAC authentication bypass.
    "disable",  # Disable MAC authentication bypass.
]
VALID_BODY_SECURITY_IP_AUTH_BYPASS = [
    "enable",  # Enable IP authentication bypass.
    "disable",  # Disable IP authentication bypass.
]
VALID_BODY_DEVICE_IDENTIFICATION = [
    "enable",  # Enable passive gathering of identity information about hosts.
    "disable",  # Disable passive gathering of identity information about hosts.
]
VALID_BODY_EXCLUDE_SIGNATURES = [
    "iot",  # Exclude IOT appctrl signatures.
    "ot",  # Exclude OT appctrl signatures.
]
VALID_BODY_DEVICE_USER_IDENTIFICATION = [
    "enable",  # Enable passive gathering of user identity information about users.
    "disable",  # Disable passive gathering of user identity information about users.
]
VALID_BODY_LLDP_RECEPTION = [
    "enable",  # Enable reception of Link Layer Discovery Protocol (LLDP).
    "disable",  # Disable reception of Link Layer Discovery Protocol (LLDP).
    "vdom",  # Use VDOM Link Layer Discovery Protocol (LLDP) reception configuration setting.
]
VALID_BODY_LLDP_TRANSMISSION = [
    "enable",  # Enable transmission of Link Layer Discovery Protocol (LLDP).
    "disable",  # Disable transmission of Link Layer Discovery Protocol (LLDP).
    "vdom",  # Use VDOM Link Layer Discovery Protocol (LLDP) transmission configuration setting.
]
VALID_BODY_MONITOR_BANDWIDTH = [
    "enable",  # Enable monitoring bandwidth on this interface.
    "disable",  # Disable monitoring bandwidth on this interface.
]
VALID_BODY_VRRP_VIRTUAL_MAC = [
    "enable",  # Enable use of virtual MAC for VRRP.
    "disable",  # Disable use of virtual MAC for VRRP.
]
VALID_BODY_ROLE = [
    "lan",  # Connected to local network of endpoints.
    "wan",  # Connected to Internet.
    "dmz",  # Connected to server zone.
    "undefined",  # Interface has no specific role.
]
VALID_BODY_SECONDARY_IP = [
    "enable",  # Enable secondary IP.
    "disable",  # Disable secondary IP.
]
VALID_BODY_PRESERVE_SESSION_ROUTE = [
    "enable",  # Enable preservation of session route when dirty.
    "disable",  # Disable preservation of session route when dirty.
]
VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE = [
    "enable",  # Enable automatic authorization of dedicated Fortinet extension device on this interface.
    "disable",  # Disable automatic authorization of dedicated Fortinet extension device on this interface.
]
VALID_BODY_AP_DISCOVER = [
    "enable",  # Enable automatic registration of unknown FortiAP devices.
    "disable",  # Disable automatic registration of unknown FortiAP devices.
]
VALID_BODY_FORTILINK_NEIGHBOR_DETECT = [
    "lldp",  # Detect FortiLink neighbors using LLDP protocol.
    "fortilink",  # Detect FortiLink neighbors using FortiLink protocol.
]
VALID_BODY_IP_MANAGED_BY_FORTIIPAM = [
    "inherit-global",  # Control automatic IP address assignment status using the central FortiIPAM config.
    "enable",  # Enable automatic IP address assignment of this interface by FortiIPAM.
    "disable",  # Disable automatic IP address assignment of this interface by FortiIPAM.
]
VALID_BODY_MANAGED_SUBNETWORK_SIZE = [
    "4",  # Allocate a subnet with 4 IP addresses.
    "8",  # Allocate a subnet with 8 IP addresses.
    "16",  # Allocate a subnet with 16 IP addresses.
    "32",  # Allocate a subnet with 32 IP addresses.
    "64",  # Allocate a subnet with 64 IP addresses.
    "128",  # Allocate a subnet with 128 IP addresses.
    "256",  # Allocate a subnet with 256 IP addresses.
    "512",  # Allocate a subnet with 512 IP addresses.
    "1024",  # Allocate a subnet with 1024 IP addresses.
    "2048",  # Allocate a subnet with 2048 IP addresses.
    "4096",  # Allocate a subnet with 4096 IP addresses.
    "8192",  # Allocate a subnet with 8192 IP addresses.
    "16384",  # Allocate a subnet with 16384 IP addresses.
    "32768",  # Allocate a subnet with 32768 IP addresses.
    "65536",  # Allocate a subnet with 65536 IP addresses.
    "131072",  # Allocate a subnet with 131072 IP addresses.
    "262144",  # Allocate a subnet with 262144 IP addresses.
    "524288",  # Allocate a subnet with 524288 IP addresses.
    "1048576",  # Allocate a subnet with 1048576 IP addresses.
    "2097152",  # Allocate a subnet with 2097152 IP addresses.
    "4194304",  # Allocate a subnet with 4194304 IP addresses.
    "8388608",  # Allocate a subnet with 8388608 IP addresses.
    "16777216",  # Allocate a subnet with 16777216 IP addresses.
]
VALID_BODY_FORTILINK_SPLIT_INTERFACE = [
    "enable",  # Enable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.
    "disable",  # Disable FortiLink split interface.
]
VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN = [
    "enable",  # Block FortiSwitch port-to-port traffic on the VLAN, only permitting traffic to and from the FortiGate.
    "disable",  # Allow normal VLAN traffic.
]
VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE = [
    "disable",  # Disable RSPAN passthrough mode on this VLAN interface.
    "enable",  # Enable RSPAN passthrough mode on this VLAN interface.
]
VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT = [
    "disable",  # Disable NetFlow collection.
    "enable",  # Enable NetFlow collection.
]
VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING = [
    "enable",  # Enable IGMP snooping.
    "disable",  # Disable IGMP snooping.
]
VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY = [
    "enable",  # Enable IGMP snooping proxy.
    "disable",  # Disable IGMP snooping proxy.
]
VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE = [
    "enable",  # Enable IGMP snooping fast-leave.
    "disable",  # Disable IGMP snooping fast-leave.
]
VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING = [
    "enable",  # Enable DHCP snooping for FortiSwitch devices.
    "disable",  # Disable DHCP snooping for FortiSwitch devices.
]
VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC = [
    "enable",  # Enable DHCP snooping verify source MAC for FortiSwitch devices.
    "disable",  # Disable DHCP snooping verify source MAC for FortiSwitch devices.
]
VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82 = [
    "enable",  # Enable DHCP snooping insert option82 for FortiSwitch devices.
    "disable",  # Disable DHCP snooping insert option82 for FortiSwitch devices.
]
VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION = [
    "enable",  # Enable ARP inspection for FortiSwitch devices.
    "disable",  # Disable ARP inspection for FortiSwitch devices.
    "monitor",  # Monitor ARP traffic and update DHCP client database with MAC-VLAN-IP.
]
VALID_BODY_SWITCH_CONTROLLER_FEATURE = [
    "none",  # VLAN for generic purpose.
    "default-vlan",  # Default VLAN (native) assigned to all switch ports upon discovery.
    "quarantine",  # VLAN for quarantined traffic.
    "rspan",  # VLAN for RSPAN/ERSPAN mirrored traffic.
    "voice",  # VLAN dedicated for voice devices.
    "video",  # VLAN dedicated for camera devices.
    "nac",  # VLAN dedicated for NAC onboarding devices.
    "nac-segment",  # VLAN dedicated for NAC segment devices.
]
VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING = [
    "enable",  # Enable IoT scanning for managed FortiSwitch devices.
    "disable",  # Disable IoT scanning for managed FortiSwitch devices.
]
VALID_BODY_SWITCH_CONTROLLER_OFFLOAD = [
    "enable",  # Enable routing offload to managed FortiSwitch devices.
    "disable",  # Disable routing offload to managed FortiSwitch devices.
]
VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW = [
    "enable",  # Enable routing offload gateway to managed FortiSwitch devices.
    "disable",  # Disable routing offload gateway to managed FortiSwitch devices.
]
VALID_BODY_EAP_SUPPLICANT = [
    "enable",  # Enable EAP Supplicant.
    "disable",  # Disable EAP Supplicant.
]
VALID_BODY_EAP_METHOD = [
    "tls",  # TLS.
    "peap",  # PEAP.
]
VALID_BODY_DEFAULT_PURDUE_LEVEL = [
    "1",  # Level 1 - Basic Control
    "1.5",  # Level 1.5
    "2",  # Level 2 - Area Supervisory Control
    "2.5",  # Level 2.5
    "3",  # Level 3 - Operations & Control
    "3.5",  # Level 3.5
    "4",  # Level 4 - Business Planning & Logistics
    "5",  # Level 5 - Enterprise Network
    "5.5",  # Level 5.5
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_interface_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/interface."""
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
    """Validate required fields for system/interface."""
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


def validate_system_interface_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/interface object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "fortilink" in payload:
        value = payload["fortilink"]
        if value not in VALID_BODY_FORTILINK:
            desc = FIELD_DESCRIPTIONS.get("fortilink", "")
            error_msg = f"Invalid value for 'fortilink': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTILINK)}"
            error_msg += f"\n  → Example: fortilink='{{ VALID_BODY_FORTILINK[0] }}'"
            return (False, error_msg)
    if "switch-controller-source-ip" in payload:
        value = payload["switch-controller-source-ip"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-source-ip", "")
            error_msg = f"Invalid value for 'switch-controller-source-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP)}"
            error_msg += f"\n  → Example: switch-controller-source-ip='{{ VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP[0] }}'"
            return (False, error_msg)
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            desc = FIELD_DESCRIPTIONS.get("mode", "")
            error_msg = f"Invalid value for 'mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE)}"
            error_msg += f"\n  → Example: mode='{{ VALID_BODY_MODE[0] }}'"
            return (False, error_msg)
    if "dhcp-relay-interface-select-method" in payload:
        value = payload["dhcp-relay-interface-select-method"]
        if value not in VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("dhcp-relay-interface-select-method", "")
            error_msg = f"Invalid value for 'dhcp-relay-interface-select-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD)}"
            error_msg += f"\n  → Example: dhcp-relay-interface-select-method='{{ VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD[0] }}'"
            return (False, error_msg)
    if "dhcp-broadcast-flag" in payload:
        value = payload["dhcp-broadcast-flag"]
        if value not in VALID_BODY_DHCP_BROADCAST_FLAG:
            desc = FIELD_DESCRIPTIONS.get("dhcp-broadcast-flag", "")
            error_msg = f"Invalid value for 'dhcp-broadcast-flag': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_BROADCAST_FLAG)}"
            error_msg += f"\n  → Example: dhcp-broadcast-flag='{{ VALID_BODY_DHCP_BROADCAST_FLAG[0] }}'"
            return (False, error_msg)
    if "dhcp-relay-service" in payload:
        value = payload["dhcp-relay-service"]
        if value not in VALID_BODY_DHCP_RELAY_SERVICE:
            desc = FIELD_DESCRIPTIONS.get("dhcp-relay-service", "")
            error_msg = f"Invalid value for 'dhcp-relay-service': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_RELAY_SERVICE)}"
            error_msg += f"\n  → Example: dhcp-relay-service='{{ VALID_BODY_DHCP_RELAY_SERVICE[0] }}'"
            return (False, error_msg)
    if "dhcp-relay-request-all-server" in payload:
        value = payload["dhcp-relay-request-all-server"]
        if value not in VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER:
            desc = FIELD_DESCRIPTIONS.get("dhcp-relay-request-all-server", "")
            error_msg = f"Invalid value for 'dhcp-relay-request-all-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER)}"
            error_msg += f"\n  → Example: dhcp-relay-request-all-server='{{ VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER[0] }}'"
            return (False, error_msg)
    if "dhcp-relay-allow-no-end-option" in payload:
        value = payload["dhcp-relay-allow-no-end-option"]
        if value not in VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-relay-allow-no-end-option", "")
            error_msg = f"Invalid value for 'dhcp-relay-allow-no-end-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION)}"
            error_msg += f"\n  → Example: dhcp-relay-allow-no-end-option='{{ VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION[0] }}'"
            return (False, error_msg)
    if "dhcp-relay-type" in payload:
        value = payload["dhcp-relay-type"]
        if value not in VALID_BODY_DHCP_RELAY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("dhcp-relay-type", "")
            error_msg = f"Invalid value for 'dhcp-relay-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_RELAY_TYPE)}"
            error_msg += f"\n  → Example: dhcp-relay-type='{{ VALID_BODY_DHCP_RELAY_TYPE[0] }}'"
            return (False, error_msg)
    if "dhcp-smart-relay" in payload:
        value = payload["dhcp-smart-relay"]
        if value not in VALID_BODY_DHCP_SMART_RELAY:
            desc = FIELD_DESCRIPTIONS.get("dhcp-smart-relay", "")
            error_msg = f"Invalid value for 'dhcp-smart-relay': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_SMART_RELAY)}"
            error_msg += f"\n  → Example: dhcp-smart-relay='{{ VALID_BODY_DHCP_SMART_RELAY[0] }}'"
            return (False, error_msg)
    if "dhcp-relay-agent-option" in payload:
        value = payload["dhcp-relay-agent-option"]
        if value not in VALID_BODY_DHCP_RELAY_AGENT_OPTION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-relay-agent-option", "")
            error_msg = f"Invalid value for 'dhcp-relay-agent-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_RELAY_AGENT_OPTION)}"
            error_msg += f"\n  → Example: dhcp-relay-agent-option='{{ VALID_BODY_DHCP_RELAY_AGENT_OPTION[0] }}'"
            return (False, error_msg)
    if "dhcp-classless-route-addition" in payload:
        value = payload["dhcp-classless-route-addition"]
        if value not in VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-classless-route-addition", "")
            error_msg = f"Invalid value for 'dhcp-classless-route-addition': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION)}"
            error_msg += f"\n  → Example: dhcp-classless-route-addition='{{ VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION[0] }}'"
            return (False, error_msg)
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            desc = FIELD_DESCRIPTIONS.get("allowaccess", "")
            error_msg = f"Invalid value for 'allowaccess': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOWACCESS)}"
            error_msg += f"\n  → Example: allowaccess='{{ VALID_BODY_ALLOWACCESS[0] }}'"
            return (False, error_msg)
    if "gwdetect" in payload:
        value = payload["gwdetect"]
        if value not in VALID_BODY_GWDETECT:
            desc = FIELD_DESCRIPTIONS.get("gwdetect", "")
            error_msg = f"Invalid value for 'gwdetect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GWDETECT)}"
            error_msg += f"\n  → Example: gwdetect='{{ VALID_BODY_GWDETECT[0] }}'"
            return (False, error_msg)
    if "detectprotocol" in payload:
        value = payload["detectprotocol"]
        if value not in VALID_BODY_DETECTPROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("detectprotocol", "")
            error_msg = f"Invalid value for 'detectprotocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DETECTPROTOCOL)}"
            error_msg += f"\n  → Example: detectprotocol='{{ VALID_BODY_DETECTPROTOCOL[0] }}'"
            return (False, error_msg)
    if "fail-detect" in payload:
        value = payload["fail-detect"]
        if value not in VALID_BODY_FAIL_DETECT:
            desc = FIELD_DESCRIPTIONS.get("fail-detect", "")
            error_msg = f"Invalid value for 'fail-detect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAIL_DETECT)}"
            error_msg += f"\n  → Example: fail-detect='{{ VALID_BODY_FAIL_DETECT[0] }}'"
            return (False, error_msg)
    if "fail-detect-option" in payload:
        value = payload["fail-detect-option"]
        if value not in VALID_BODY_FAIL_DETECT_OPTION:
            desc = FIELD_DESCRIPTIONS.get("fail-detect-option", "")
            error_msg = f"Invalid value for 'fail-detect-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAIL_DETECT_OPTION)}"
            error_msg += f"\n  → Example: fail-detect-option='{{ VALID_BODY_FAIL_DETECT_OPTION[0] }}'"
            return (False, error_msg)
    if "fail-alert-method" in payload:
        value = payload["fail-alert-method"]
        if value not in VALID_BODY_FAIL_ALERT_METHOD:
            desc = FIELD_DESCRIPTIONS.get("fail-alert-method", "")
            error_msg = f"Invalid value for 'fail-alert-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAIL_ALERT_METHOD)}"
            error_msg += f"\n  → Example: fail-alert-method='{{ VALID_BODY_FAIL_ALERT_METHOD[0] }}'"
            return (False, error_msg)
    if "fail-action-on-extender" in payload:
        value = payload["fail-action-on-extender"]
        if value not in VALID_BODY_FAIL_ACTION_ON_EXTENDER:
            desc = FIELD_DESCRIPTIONS.get("fail-action-on-extender", "")
            error_msg = f"Invalid value for 'fail-action-on-extender': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAIL_ACTION_ON_EXTENDER)}"
            error_msg += f"\n  → Example: fail-action-on-extender='{{ VALID_BODY_FAIL_ACTION_ON_EXTENDER[0] }}'"
            return (False, error_msg)
    if "pppoe-egress-cos" in payload:
        value = payload["pppoe-egress-cos"]
        if value not in VALID_BODY_PPPOE_EGRESS_COS:
            desc = FIELD_DESCRIPTIONS.get("pppoe-egress-cos", "")
            error_msg = f"Invalid value for 'pppoe-egress-cos': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPPOE_EGRESS_COS)}"
            error_msg += f"\n  → Example: pppoe-egress-cos='{{ VALID_BODY_PPPOE_EGRESS_COS[0] }}'"
            return (False, error_msg)
    if "pppoe-unnumbered-negotiate" in payload:
        value = payload["pppoe-unnumbered-negotiate"]
        if value not in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE:
            desc = FIELD_DESCRIPTIONS.get("pppoe-unnumbered-negotiate", "")
            error_msg = f"Invalid value for 'pppoe-unnumbered-negotiate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE)}"
            error_msg += f"\n  → Example: pppoe-unnumbered-negotiate='{{ VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE[0] }}'"
            return (False, error_msg)
    if "multilink" in payload:
        value = payload["multilink"]
        if value not in VALID_BODY_MULTILINK:
            desc = FIELD_DESCRIPTIONS.get("multilink", "")
            error_msg = f"Invalid value for 'multilink': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTILINK)}"
            error_msg += f"\n  → Example: multilink='{{ VALID_BODY_MULTILINK[0] }}'"
            return (False, error_msg)
    if "defaultgw" in payload:
        value = payload["defaultgw"]
        if value not in VALID_BODY_DEFAULTGW:
            desc = FIELD_DESCRIPTIONS.get("defaultgw", "")
            error_msg = f"Invalid value for 'defaultgw': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULTGW)}"
            error_msg += f"\n  → Example: defaultgw='{{ VALID_BODY_DEFAULTGW[0] }}'"
            return (False, error_msg)
    if "dns-server-override" in payload:
        value = payload["dns-server-override"]
        if value not in VALID_BODY_DNS_SERVER_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("dns-server-override", "")
            error_msg = f"Invalid value for 'dns-server-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_SERVER_OVERRIDE)}"
            error_msg += f"\n  → Example: dns-server-override='{{ VALID_BODY_DNS_SERVER_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "dns-server-protocol" in payload:
        value = payload["dns-server-protocol"]
        if value not in VALID_BODY_DNS_SERVER_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("dns-server-protocol", "")
            error_msg = f"Invalid value for 'dns-server-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_SERVER_PROTOCOL)}"
            error_msg += f"\n  → Example: dns-server-protocol='{{ VALID_BODY_DNS_SERVER_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("auth-type", "")
            error_msg = f"Invalid value for 'auth-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_TYPE)}"
            error_msg += f"\n  → Example: auth-type='{{ VALID_BODY_AUTH_TYPE[0] }}'"
            return (False, error_msg)
    if "pptp-client" in payload:
        value = payload["pptp-client"]
        if value not in VALID_BODY_PPTP_CLIENT:
            desc = FIELD_DESCRIPTIONS.get("pptp-client", "")
            error_msg = f"Invalid value for 'pptp-client': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPTP_CLIENT)}"
            error_msg += f"\n  → Example: pptp-client='{{ VALID_BODY_PPTP_CLIENT[0] }}'"
            return (False, error_msg)
    if "pptp-auth-type" in payload:
        value = payload["pptp-auth-type"]
        if value not in VALID_BODY_PPTP_AUTH_TYPE:
            desc = FIELD_DESCRIPTIONS.get("pptp-auth-type", "")
            error_msg = f"Invalid value for 'pptp-auth-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPTP_AUTH_TYPE)}"
            error_msg += f"\n  → Example: pptp-auth-type='{{ VALID_BODY_PPTP_AUTH_TYPE[0] }}'"
            return (False, error_msg)
    if "arpforward" in payload:
        value = payload["arpforward"]
        if value not in VALID_BODY_ARPFORWARD:
            desc = FIELD_DESCRIPTIONS.get("arpforward", "")
            error_msg = f"Invalid value for 'arpforward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ARPFORWARD)}"
            error_msg += f"\n  → Example: arpforward='{{ VALID_BODY_ARPFORWARD[0] }}'"
            return (False, error_msg)
    if "ndiscforward" in payload:
        value = payload["ndiscforward"]
        if value not in VALID_BODY_NDISCFORWARD:
            desc = FIELD_DESCRIPTIONS.get("ndiscforward", "")
            error_msg = f"Invalid value for 'ndiscforward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NDISCFORWARD)}"
            error_msg += f"\n  → Example: ndiscforward='{{ VALID_BODY_NDISCFORWARD[0] }}'"
            return (False, error_msg)
    if "broadcast-forward" in payload:
        value = payload["broadcast-forward"]
        if value not in VALID_BODY_BROADCAST_FORWARD:
            desc = FIELD_DESCRIPTIONS.get("broadcast-forward", "")
            error_msg = f"Invalid value for 'broadcast-forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BROADCAST_FORWARD)}"
            error_msg += f"\n  → Example: broadcast-forward='{{ VALID_BODY_BROADCAST_FORWARD[0] }}'"
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
    if "l2forward" in payload:
        value = payload["l2forward"]
        if value not in VALID_BODY_L2FORWARD:
            desc = FIELD_DESCRIPTIONS.get("l2forward", "")
            error_msg = f"Invalid value for 'l2forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_L2FORWARD)}"
            error_msg += f"\n  → Example: l2forward='{{ VALID_BODY_L2FORWARD[0] }}'"
            return (False, error_msg)
    if "icmp-send-redirect" in payload:
        value = payload["icmp-send-redirect"]
        if value not in VALID_BODY_ICMP_SEND_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("icmp-send-redirect", "")
            error_msg = f"Invalid value for 'icmp-send-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ICMP_SEND_REDIRECT)}"
            error_msg += f"\n  → Example: icmp-send-redirect='{{ VALID_BODY_ICMP_SEND_REDIRECT[0] }}'"
            return (False, error_msg)
    if "icmp-accept-redirect" in payload:
        value = payload["icmp-accept-redirect"]
        if value not in VALID_BODY_ICMP_ACCEPT_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("icmp-accept-redirect", "")
            error_msg = f"Invalid value for 'icmp-accept-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ICMP_ACCEPT_REDIRECT)}"
            error_msg += f"\n  → Example: icmp-accept-redirect='{{ VALID_BODY_ICMP_ACCEPT_REDIRECT[0] }}'"
            return (False, error_msg)
    if "vlanforward" in payload:
        value = payload["vlanforward"]
        if value not in VALID_BODY_VLANFORWARD:
            desc = FIELD_DESCRIPTIONS.get("vlanforward", "")
            error_msg = f"Invalid value for 'vlanforward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLANFORWARD)}"
            error_msg += f"\n  → Example: vlanforward='{{ VALID_BODY_VLANFORWARD[0] }}'"
            return (False, error_msg)
    if "stpforward" in payload:
        value = payload["stpforward"]
        if value not in VALID_BODY_STPFORWARD:
            desc = FIELD_DESCRIPTIONS.get("stpforward", "")
            error_msg = f"Invalid value for 'stpforward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STPFORWARD)}"
            error_msg += f"\n  → Example: stpforward='{{ VALID_BODY_STPFORWARD[0] }}'"
            return (False, error_msg)
    if "stpforward-mode" in payload:
        value = payload["stpforward-mode"]
        if value not in VALID_BODY_STPFORWARD_MODE:
            desc = FIELD_DESCRIPTIONS.get("stpforward-mode", "")
            error_msg = f"Invalid value for 'stpforward-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STPFORWARD_MODE)}"
            error_msg += f"\n  → Example: stpforward-mode='{{ VALID_BODY_STPFORWARD_MODE[0] }}'"
            return (False, error_msg)
    if "ips-sniffer-mode" in payload:
        value = payload["ips-sniffer-mode"]
        if value not in VALID_BODY_IPS_SNIFFER_MODE:
            desc = FIELD_DESCRIPTIONS.get("ips-sniffer-mode", "")
            error_msg = f"Invalid value for 'ips-sniffer-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPS_SNIFFER_MODE)}"
            error_msg += f"\n  → Example: ips-sniffer-mode='{{ VALID_BODY_IPS_SNIFFER_MODE[0] }}'"
            return (False, error_msg)
    if "ident-accept" in payload:
        value = payload["ident-accept"]
        if value not in VALID_BODY_IDENT_ACCEPT:
            desc = FIELD_DESCRIPTIONS.get("ident-accept", "")
            error_msg = f"Invalid value for 'ident-accept': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IDENT_ACCEPT)}"
            error_msg += f"\n  → Example: ident-accept='{{ VALID_BODY_IDENT_ACCEPT[0] }}'"
            return (False, error_msg)
    if "ipmac" in payload:
        value = payload["ipmac"]
        if value not in VALID_BODY_IPMAC:
            desc = FIELD_DESCRIPTIONS.get("ipmac", "")
            error_msg = f"Invalid value for 'ipmac': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPMAC)}"
            error_msg += f"\n  → Example: ipmac='{{ VALID_BODY_IPMAC[0] }}'"
            return (False, error_msg)
    if "subst" in payload:
        value = payload["subst"]
        if value not in VALID_BODY_SUBST:
            desc = FIELD_DESCRIPTIONS.get("subst", "")
            error_msg = f"Invalid value for 'subst': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUBST)}"
            error_msg += f"\n  → Example: subst='{{ VALID_BODY_SUBST[0] }}'"
            return (False, error_msg)
    if "speed" in payload:
        value = payload["speed"]
        if value not in VALID_BODY_SPEED:
            desc = FIELD_DESCRIPTIONS.get("speed", "")
            error_msg = f"Invalid value for 'speed': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPEED)}"
            error_msg += f"\n  → Example: speed='{{ VALID_BODY_SPEED[0] }}'"
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
    if "netbios-forward" in payload:
        value = payload["netbios-forward"]
        if value not in VALID_BODY_NETBIOS_FORWARD:
            desc = FIELD_DESCRIPTIONS.get("netbios-forward", "")
            error_msg = f"Invalid value for 'netbios-forward': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NETBIOS_FORWARD)}"
            error_msg += f"\n  → Example: netbios-forward='{{ VALID_BODY_NETBIOS_FORWARD[0] }}'"
            return (False, error_msg)
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            desc = FIELD_DESCRIPTIONS.get("type", "")
            error_msg = f"Invalid value for 'type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TYPE)}"
            error_msg += f"\n  → Example: type='{{ VALID_BODY_TYPE[0] }}'"
            return (False, error_msg)
    if "dedicated-to" in payload:
        value = payload["dedicated-to"]
        if value not in VALID_BODY_DEDICATED_TO:
            desc = FIELD_DESCRIPTIONS.get("dedicated-to", "")
            error_msg = f"Invalid value for 'dedicated-to': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEDICATED_TO)}"
            error_msg += f"\n  → Example: dedicated-to='{{ VALID_BODY_DEDICATED_TO[0] }}'"
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
    if "netflow-sampler" in payload:
        value = payload["netflow-sampler"]
        if value not in VALID_BODY_NETFLOW_SAMPLER:
            desc = FIELD_DESCRIPTIONS.get("netflow-sampler", "")
            error_msg = f"Invalid value for 'netflow-sampler': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NETFLOW_SAMPLER)}"
            error_msg += f"\n  → Example: netflow-sampler='{{ VALID_BODY_NETFLOW_SAMPLER[0] }}'"
            return (False, error_msg)
    if "sflow-sampler" in payload:
        value = payload["sflow-sampler"]
        if value not in VALID_BODY_SFLOW_SAMPLER:
            desc = FIELD_DESCRIPTIONS.get("sflow-sampler", "")
            error_msg = f"Invalid value for 'sflow-sampler': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SFLOW_SAMPLER)}"
            error_msg += f"\n  → Example: sflow-sampler='{{ VALID_BODY_SFLOW_SAMPLER[0] }}'"
            return (False, error_msg)
    if "drop-fragment" in payload:
        value = payload["drop-fragment"]
        if value not in VALID_BODY_DROP_FRAGMENT:
            desc = FIELD_DESCRIPTIONS.get("drop-fragment", "")
            error_msg = f"Invalid value for 'drop-fragment': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DROP_FRAGMENT)}"
            error_msg += f"\n  → Example: drop-fragment='{{ VALID_BODY_DROP_FRAGMENT[0] }}'"
            return (False, error_msg)
    if "src-check" in payload:
        value = payload["src-check"]
        if value not in VALID_BODY_SRC_CHECK:
            desc = FIELD_DESCRIPTIONS.get("src-check", "")
            error_msg = f"Invalid value for 'src-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SRC_CHECK)}"
            error_msg += f"\n  → Example: src-check='{{ VALID_BODY_SRC_CHECK[0] }}'"
            return (False, error_msg)
    if "sample-direction" in payload:
        value = payload["sample-direction"]
        if value not in VALID_BODY_SAMPLE_DIRECTION:
            desc = FIELD_DESCRIPTIONS.get("sample-direction", "")
            error_msg = f"Invalid value for 'sample-direction': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAMPLE_DIRECTION)}"
            error_msg += f"\n  → Example: sample-direction='{{ VALID_BODY_SAMPLE_DIRECTION[0] }}'"
            return (False, error_msg)
    if "explicit-web-proxy" in payload:
        value = payload["explicit-web-proxy"]
        if value not in VALID_BODY_EXPLICIT_WEB_PROXY:
            desc = FIELD_DESCRIPTIONS.get("explicit-web-proxy", "")
            error_msg = f"Invalid value for 'explicit-web-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXPLICIT_WEB_PROXY)}"
            error_msg += f"\n  → Example: explicit-web-proxy='{{ VALID_BODY_EXPLICIT_WEB_PROXY[0] }}'"
            return (False, error_msg)
    if "explicit-ftp-proxy" in payload:
        value = payload["explicit-ftp-proxy"]
        if value not in VALID_BODY_EXPLICIT_FTP_PROXY:
            desc = FIELD_DESCRIPTIONS.get("explicit-ftp-proxy", "")
            error_msg = f"Invalid value for 'explicit-ftp-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXPLICIT_FTP_PROXY)}"
            error_msg += f"\n  → Example: explicit-ftp-proxy='{{ VALID_BODY_EXPLICIT_FTP_PROXY[0] }}'"
            return (False, error_msg)
    if "proxy-captive-portal" in payload:
        value = payload["proxy-captive-portal"]
        if value not in VALID_BODY_PROXY_CAPTIVE_PORTAL:
            desc = FIELD_DESCRIPTIONS.get("proxy-captive-portal", "")
            error_msg = f"Invalid value for 'proxy-captive-portal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_CAPTIVE_PORTAL)}"
            error_msg += f"\n  → Example: proxy-captive-portal='{{ VALID_BODY_PROXY_CAPTIVE_PORTAL[0] }}'"
            return (False, error_msg)
    if "external" in payload:
        value = payload["external"]
        if value not in VALID_BODY_EXTERNAL:
            desc = FIELD_DESCRIPTIONS.get("external", "")
            error_msg = f"Invalid value for 'external': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTERNAL)}"
            error_msg += f"\n  → Example: external='{{ VALID_BODY_EXTERNAL[0] }}'"
            return (False, error_msg)
    if "mtu-override" in payload:
        value = payload["mtu-override"]
        if value not in VALID_BODY_MTU_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("mtu-override", "")
            error_msg = f"Invalid value for 'mtu-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MTU_OVERRIDE)}"
            error_msg += f"\n  → Example: mtu-override='{{ VALID_BODY_MTU_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "vlan-protocol" in payload:
        value = payload["vlan-protocol"]
        if value not in VALID_BODY_VLAN_PROTOCOL:
            desc = FIELD_DESCRIPTIONS.get("vlan-protocol", "")
            error_msg = f"Invalid value for 'vlan-protocol': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLAN_PROTOCOL)}"
            error_msg += f"\n  → Example: vlan-protocol='{{ VALID_BODY_VLAN_PROTOCOL[0] }}'"
            return (False, error_msg)
    if "lacp-mode" in payload:
        value = payload["lacp-mode"]
        if value not in VALID_BODY_LACP_MODE:
            desc = FIELD_DESCRIPTIONS.get("lacp-mode", "")
            error_msg = f"Invalid value for 'lacp-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LACP_MODE)}"
            error_msg += f"\n  → Example: lacp-mode='{{ VALID_BODY_LACP_MODE[0] }}'"
            return (False, error_msg)
    if "lacp-ha-secondary" in payload:
        value = payload["lacp-ha-secondary"]
        if value not in VALID_BODY_LACP_HA_SECONDARY:
            desc = FIELD_DESCRIPTIONS.get("lacp-ha-secondary", "")
            error_msg = f"Invalid value for 'lacp-ha-secondary': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LACP_HA_SECONDARY)}"
            error_msg += f"\n  → Example: lacp-ha-secondary='{{ VALID_BODY_LACP_HA_SECONDARY[0] }}'"
            return (False, error_msg)
    if "system-id-type" in payload:
        value = payload["system-id-type"]
        if value not in VALID_BODY_SYSTEM_ID_TYPE:
            desc = FIELD_DESCRIPTIONS.get("system-id-type", "")
            error_msg = f"Invalid value for 'system-id-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYSTEM_ID_TYPE)}"
            error_msg += f"\n  → Example: system-id-type='{{ VALID_BODY_SYSTEM_ID_TYPE[0] }}'"
            return (False, error_msg)
    if "lacp-speed" in payload:
        value = payload["lacp-speed"]
        if value not in VALID_BODY_LACP_SPEED:
            desc = FIELD_DESCRIPTIONS.get("lacp-speed", "")
            error_msg = f"Invalid value for 'lacp-speed': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LACP_SPEED)}"
            error_msg += f"\n  → Example: lacp-speed='{{ VALID_BODY_LACP_SPEED[0] }}'"
            return (False, error_msg)
    if "min-links-down" in payload:
        value = payload["min-links-down"]
        if value not in VALID_BODY_MIN_LINKS_DOWN:
            desc = FIELD_DESCRIPTIONS.get("min-links-down", "")
            error_msg = f"Invalid value for 'min-links-down': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MIN_LINKS_DOWN)}"
            error_msg += f"\n  → Example: min-links-down='{{ VALID_BODY_MIN_LINKS_DOWN[0] }}'"
            return (False, error_msg)
    if "algorithm" in payload:
        value = payload["algorithm"]
        if value not in VALID_BODY_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("algorithm", "")
            error_msg = f"Invalid value for 'algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALGORITHM)}"
            error_msg += f"\n  → Example: algorithm='{{ VALID_BODY_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "aggregate-type" in payload:
        value = payload["aggregate-type"]
        if value not in VALID_BODY_AGGREGATE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("aggregate-type", "")
            error_msg = f"Invalid value for 'aggregate-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AGGREGATE_TYPE)}"
            error_msg += f"\n  → Example: aggregate-type='{{ VALID_BODY_AGGREGATE_TYPE[0] }}'"
            return (False, error_msg)
    if "priority-override" in payload:
        value = payload["priority-override"]
        if value not in VALID_BODY_PRIORITY_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("priority-override", "")
            error_msg = f"Invalid value for 'priority-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIORITY_OVERRIDE)}"
            error_msg += f"\n  → Example: priority-override='{{ VALID_BODY_PRIORITY_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            desc = FIELD_DESCRIPTIONS.get("security-mode", "")
            error_msg = f"Invalid value for 'security-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_MODE)}"
            error_msg += f"\n  → Example: security-mode='{{ VALID_BODY_SECURITY_MODE[0] }}'"
            return (False, error_msg)
    if "security-mac-auth-bypass" in payload:
        value = payload["security-mac-auth-bypass"]
        if value not in VALID_BODY_SECURITY_MAC_AUTH_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("security-mac-auth-bypass", "")
            error_msg = f"Invalid value for 'security-mac-auth-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_MAC_AUTH_BYPASS)}"
            error_msg += f"\n  → Example: security-mac-auth-bypass='{{ VALID_BODY_SECURITY_MAC_AUTH_BYPASS[0] }}'"
            return (False, error_msg)
    if "security-ip-auth-bypass" in payload:
        value = payload["security-ip-auth-bypass"]
        if value not in VALID_BODY_SECURITY_IP_AUTH_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("security-ip-auth-bypass", "")
            error_msg = f"Invalid value for 'security-ip-auth-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY_IP_AUTH_BYPASS)}"
            error_msg += f"\n  → Example: security-ip-auth-bypass='{{ VALID_BODY_SECURITY_IP_AUTH_BYPASS[0] }}'"
            return (False, error_msg)
    if "device-identification" in payload:
        value = payload["device-identification"]
        if value not in VALID_BODY_DEVICE_IDENTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("device-identification", "")
            error_msg = f"Invalid value for 'device-identification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEVICE_IDENTIFICATION)}"
            error_msg += f"\n  → Example: device-identification='{{ VALID_BODY_DEVICE_IDENTIFICATION[0] }}'"
            return (False, error_msg)
    if "exclude-signatures" in payload:
        value = payload["exclude-signatures"]
        if value not in VALID_BODY_EXCLUDE_SIGNATURES:
            desc = FIELD_DESCRIPTIONS.get("exclude-signatures", "")
            error_msg = f"Invalid value for 'exclude-signatures': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXCLUDE_SIGNATURES)}"
            error_msg += f"\n  → Example: exclude-signatures='{{ VALID_BODY_EXCLUDE_SIGNATURES[0] }}'"
            return (False, error_msg)
    if "device-user-identification" in payload:
        value = payload["device-user-identification"]
        if value not in VALID_BODY_DEVICE_USER_IDENTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("device-user-identification", "")
            error_msg = f"Invalid value for 'device-user-identification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEVICE_USER_IDENTIFICATION)}"
            error_msg += f"\n  → Example: device-user-identification='{{ VALID_BODY_DEVICE_USER_IDENTIFICATION[0] }}'"
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
    if "monitor-bandwidth" in payload:
        value = payload["monitor-bandwidth"]
        if value not in VALID_BODY_MONITOR_BANDWIDTH:
            desc = FIELD_DESCRIPTIONS.get("monitor-bandwidth", "")
            error_msg = f"Invalid value for 'monitor-bandwidth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MONITOR_BANDWIDTH)}"
            error_msg += f"\n  → Example: monitor-bandwidth='{{ VALID_BODY_MONITOR_BANDWIDTH[0] }}'"
            return (False, error_msg)
    if "vrrp-virtual-mac" in payload:
        value = payload["vrrp-virtual-mac"]
        if value not in VALID_BODY_VRRP_VIRTUAL_MAC:
            desc = FIELD_DESCRIPTIONS.get("vrrp-virtual-mac", "")
            error_msg = f"Invalid value for 'vrrp-virtual-mac': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VRRP_VIRTUAL_MAC)}"
            error_msg += f"\n  → Example: vrrp-virtual-mac='{{ VALID_BODY_VRRP_VIRTUAL_MAC[0] }}'"
            return (False, error_msg)
    if "role" in payload:
        value = payload["role"]
        if value not in VALID_BODY_ROLE:
            desc = FIELD_DESCRIPTIONS.get("role", "")
            error_msg = f"Invalid value for 'role': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROLE)}"
            error_msg += f"\n  → Example: role='{{ VALID_BODY_ROLE[0] }}'"
            return (False, error_msg)
    if "secondary-IP" in payload:
        value = payload["secondary-IP"]
        if value not in VALID_BODY_SECONDARY_IP:
            desc = FIELD_DESCRIPTIONS.get("secondary-IP", "")
            error_msg = f"Invalid value for 'secondary-IP': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECONDARY_IP)}"
            error_msg += f"\n  → Example: secondary-IP='{{ VALID_BODY_SECONDARY_IP[0] }}'"
            return (False, error_msg)
    if "preserve-session-route" in payload:
        value = payload["preserve-session-route"]
        if value not in VALID_BODY_PRESERVE_SESSION_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("preserve-session-route", "")
            error_msg = f"Invalid value for 'preserve-session-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRESERVE_SESSION_ROUTE)}"
            error_msg += f"\n  → Example: preserve-session-route='{{ VALID_BODY_PRESERVE_SESSION_ROUTE[0] }}'"
            return (False, error_msg)
    if "auto-auth-extension-device" in payload:
        value = payload["auto-auth-extension-device"]
        if value not in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE:
            desc = FIELD_DESCRIPTIONS.get("auto-auth-extension-device", "")
            error_msg = f"Invalid value for 'auto-auth-extension-device': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE)}"
            error_msg += f"\n  → Example: auto-auth-extension-device='{{ VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE[0] }}'"
            return (False, error_msg)
    if "ap-discover" in payload:
        value = payload["ap-discover"]
        if value not in VALID_BODY_AP_DISCOVER:
            desc = FIELD_DESCRIPTIONS.get("ap-discover", "")
            error_msg = f"Invalid value for 'ap-discover': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_DISCOVER)}"
            error_msg += f"\n  → Example: ap-discover='{{ VALID_BODY_AP_DISCOVER[0] }}'"
            return (False, error_msg)
    if "fortilink-neighbor-detect" in payload:
        value = payload["fortilink-neighbor-detect"]
        if value not in VALID_BODY_FORTILINK_NEIGHBOR_DETECT:
            desc = FIELD_DESCRIPTIONS.get("fortilink-neighbor-detect", "")
            error_msg = f"Invalid value for 'fortilink-neighbor-detect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTILINK_NEIGHBOR_DETECT)}"
            error_msg += f"\n  → Example: fortilink-neighbor-detect='{{ VALID_BODY_FORTILINK_NEIGHBOR_DETECT[0] }}'"
            return (False, error_msg)
    if "ip-managed-by-fortiipam" in payload:
        value = payload["ip-managed-by-fortiipam"]
        if value not in VALID_BODY_IP_MANAGED_BY_FORTIIPAM:
            desc = FIELD_DESCRIPTIONS.get("ip-managed-by-fortiipam", "")
            error_msg = f"Invalid value for 'ip-managed-by-fortiipam': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_MANAGED_BY_FORTIIPAM)}"
            error_msg += f"\n  → Example: ip-managed-by-fortiipam='{{ VALID_BODY_IP_MANAGED_BY_FORTIIPAM[0] }}'"
            return (False, error_msg)
    if "managed-subnetwork-size" in payload:
        value = payload["managed-subnetwork-size"]
        if value not in VALID_BODY_MANAGED_SUBNETWORK_SIZE:
            desc = FIELD_DESCRIPTIONS.get("managed-subnetwork-size", "")
            error_msg = f"Invalid value for 'managed-subnetwork-size': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MANAGED_SUBNETWORK_SIZE)}"
            error_msg += f"\n  → Example: managed-subnetwork-size='{{ VALID_BODY_MANAGED_SUBNETWORK_SIZE[0] }}'"
            return (False, error_msg)
    if "fortilink-split-interface" in payload:
        value = payload["fortilink-split-interface"]
        if value not in VALID_BODY_FORTILINK_SPLIT_INTERFACE:
            desc = FIELD_DESCRIPTIONS.get("fortilink-split-interface", "")
            error_msg = f"Invalid value for 'fortilink-split-interface': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTILINK_SPLIT_INTERFACE)}"
            error_msg += f"\n  → Example: fortilink-split-interface='{{ VALID_BODY_FORTILINK_SPLIT_INTERFACE[0] }}'"
            return (False, error_msg)
    if "switch-controller-access-vlan" in payload:
        value = payload["switch-controller-access-vlan"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-access-vlan", "")
            error_msg = f"Invalid value for 'switch-controller-access-vlan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN)}"
            error_msg += f"\n  → Example: switch-controller-access-vlan='{{ VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN[0] }}'"
            return (False, error_msg)
    if "switch-controller-rspan-mode" in payload:
        value = payload["switch-controller-rspan-mode"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-rspan-mode", "")
            error_msg = f"Invalid value for 'switch-controller-rspan-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE)}"
            error_msg += f"\n  → Example: switch-controller-rspan-mode='{{ VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE[0] }}'"
            return (False, error_msg)
    if "switch-controller-netflow-collect" in payload:
        value = payload["switch-controller-netflow-collect"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-netflow-collect", "")
            error_msg = f"Invalid value for 'switch-controller-netflow-collect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT)}"
            error_msg += f"\n  → Example: switch-controller-netflow-collect='{{ VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT[0] }}'"
            return (False, error_msg)
    if "switch-controller-igmp-snooping" in payload:
        value = payload["switch-controller-igmp-snooping"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-igmp-snooping", "")
            error_msg = f"Invalid value for 'switch-controller-igmp-snooping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING)}"
            error_msg += f"\n  → Example: switch-controller-igmp-snooping='{{ VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING[0] }}'"
            return (False, error_msg)
    if "switch-controller-igmp-snooping-proxy" in payload:
        value = payload["switch-controller-igmp-snooping-proxy"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-igmp-snooping-proxy", "")
            error_msg = f"Invalid value for 'switch-controller-igmp-snooping-proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY)}"
            error_msg += f"\n  → Example: switch-controller-igmp-snooping-proxy='{{ VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY[0] }}'"
            return (False, error_msg)
    if "switch-controller-igmp-snooping-fast-leave" in payload:
        value = payload["switch-controller-igmp-snooping-fast-leave"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-igmp-snooping-fast-leave", "")
            error_msg = f"Invalid value for 'switch-controller-igmp-snooping-fast-leave': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE)}"
            error_msg += f"\n  → Example: switch-controller-igmp-snooping-fast-leave='{{ VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE[0] }}'"
            return (False, error_msg)
    if "switch-controller-dhcp-snooping" in payload:
        value = payload["switch-controller-dhcp-snooping"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-dhcp-snooping", "")
            error_msg = f"Invalid value for 'switch-controller-dhcp-snooping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING)}"
            error_msg += f"\n  → Example: switch-controller-dhcp-snooping='{{ VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING[0] }}'"
            return (False, error_msg)
    if "switch-controller-dhcp-snooping-verify-mac" in payload:
        value = payload["switch-controller-dhcp-snooping-verify-mac"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-dhcp-snooping-verify-mac", "")
            error_msg = f"Invalid value for 'switch-controller-dhcp-snooping-verify-mac': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC)}"
            error_msg += f"\n  → Example: switch-controller-dhcp-snooping-verify-mac='{{ VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC[0] }}'"
            return (False, error_msg)
    if "switch-controller-dhcp-snooping-option82" in payload:
        value = payload["switch-controller-dhcp-snooping-option82"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-dhcp-snooping-option82", "")
            error_msg = f"Invalid value for 'switch-controller-dhcp-snooping-option82': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82)}"
            error_msg += f"\n  → Example: switch-controller-dhcp-snooping-option82='{{ VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82[0] }}'"
            return (False, error_msg)
    if "switch-controller-arp-inspection" in payload:
        value = payload["switch-controller-arp-inspection"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-arp-inspection", "")
            error_msg = f"Invalid value for 'switch-controller-arp-inspection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION)}"
            error_msg += f"\n  → Example: switch-controller-arp-inspection='{{ VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION[0] }}'"
            return (False, error_msg)
    if "switch-controller-feature" in payload:
        value = payload["switch-controller-feature"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_FEATURE:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-feature", "")
            error_msg = f"Invalid value for 'switch-controller-feature': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_FEATURE)}"
            error_msg += f"\n  → Example: switch-controller-feature='{{ VALID_BODY_SWITCH_CONTROLLER_FEATURE[0] }}'"
            return (False, error_msg)
    if "switch-controller-iot-scanning" in payload:
        value = payload["switch-controller-iot-scanning"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-iot-scanning", "")
            error_msg = f"Invalid value for 'switch-controller-iot-scanning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING)}"
            error_msg += f"\n  → Example: switch-controller-iot-scanning='{{ VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING[0] }}'"
            return (False, error_msg)
    if "switch-controller-offload" in payload:
        value = payload["switch-controller-offload"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-offload", "")
            error_msg = f"Invalid value for 'switch-controller-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD)}"
            error_msg += f"\n  → Example: switch-controller-offload='{{ VALID_BODY_SWITCH_CONTROLLER_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "switch-controller-offload-gw" in payload:
        value = payload["switch-controller-offload-gw"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW:
            desc = FIELD_DESCRIPTIONS.get("switch-controller-offload-gw", "")
            error_msg = f"Invalid value for 'switch-controller-offload-gw': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW)}"
            error_msg += f"\n  → Example: switch-controller-offload-gw='{{ VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW[0] }}'"
            return (False, error_msg)
    if "eap-supplicant" in payload:
        value = payload["eap-supplicant"]
        if value not in VALID_BODY_EAP_SUPPLICANT:
            desc = FIELD_DESCRIPTIONS.get("eap-supplicant", "")
            error_msg = f"Invalid value for 'eap-supplicant': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_SUPPLICANT)}"
            error_msg += f"\n  → Example: eap-supplicant='{{ VALID_BODY_EAP_SUPPLICANT[0] }}'"
            return (False, error_msg)
    if "eap-method" in payload:
        value = payload["eap-method"]
        if value not in VALID_BODY_EAP_METHOD:
            desc = FIELD_DESCRIPTIONS.get("eap-method", "")
            error_msg = f"Invalid value for 'eap-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_METHOD)}"
            error_msg += f"\n  → Example: eap-method='{{ VALID_BODY_EAP_METHOD[0] }}'"
            return (False, error_msg)
    if "default-purdue-level" in payload:
        value = payload["default-purdue-level"]
        if value not in VALID_BODY_DEFAULT_PURDUE_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("default-purdue-level", "")
            error_msg = f"Invalid value for 'default-purdue-level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEFAULT_PURDUE_LEVEL)}"
            error_msg += f"\n  → Example: default-purdue-level='{{ VALID_BODY_DEFAULT_PURDUE_LEVEL[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_interface_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/interface."""
    # Step 1: Validate enum values
    if "fortilink" in payload:
        value = payload["fortilink"]
        if value not in VALID_BODY_FORTILINK:
            return (
                False,
                f"Invalid value for 'fortilink'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK)}",
            )
    if "switch-controller-source-ip" in payload:
        value = payload["switch-controller-source-ip"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP:
            return (
                False,
                f"Invalid value for 'switch-controller-source-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP)}",
            )
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "dhcp-relay-interface-select-method" in payload:
        value = payload["dhcp-relay-interface-select-method"]
        if value not in VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid value for 'dhcp-relay-interface-select-method'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD)}",
            )
    if "dhcp-broadcast-flag" in payload:
        value = payload["dhcp-broadcast-flag"]
        if value not in VALID_BODY_DHCP_BROADCAST_FLAG:
            return (
                False,
                f"Invalid value for 'dhcp-broadcast-flag'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_BROADCAST_FLAG)}",
            )
    if "dhcp-relay-service" in payload:
        value = payload["dhcp-relay-service"]
        if value not in VALID_BODY_DHCP_RELAY_SERVICE:
            return (
                False,
                f"Invalid value for 'dhcp-relay-service'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_SERVICE)}",
            )
    if "dhcp-relay-request-all-server" in payload:
        value = payload["dhcp-relay-request-all-server"]
        if value not in VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER:
            return (
                False,
                f"Invalid value for 'dhcp-relay-request-all-server'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER)}",
            )
    if "dhcp-relay-allow-no-end-option" in payload:
        value = payload["dhcp-relay-allow-no-end-option"]
        if value not in VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION:
            return (
                False,
                f"Invalid value for 'dhcp-relay-allow-no-end-option'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION)}",
            )
    if "dhcp-relay-type" in payload:
        value = payload["dhcp-relay-type"]
        if value not in VALID_BODY_DHCP_RELAY_TYPE:
            return (
                False,
                f"Invalid value for 'dhcp-relay-type'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_TYPE)}",
            )
    if "dhcp-smart-relay" in payload:
        value = payload["dhcp-smart-relay"]
        if value not in VALID_BODY_DHCP_SMART_RELAY:
            return (
                False,
                f"Invalid value for 'dhcp-smart-relay'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SMART_RELAY)}",
            )
    if "dhcp-relay-agent-option" in payload:
        value = payload["dhcp-relay-agent-option"]
        if value not in VALID_BODY_DHCP_RELAY_AGENT_OPTION:
            return (
                False,
                f"Invalid value for 'dhcp-relay-agent-option'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_AGENT_OPTION)}",
            )
    if "dhcp-classless-route-addition" in payload:
        value = payload["dhcp-classless-route-addition"]
        if value not in VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION:
            return (
                False,
                f"Invalid value for 'dhcp-classless-route-addition'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION)}",
            )
    if "allowaccess" in payload:
        value = payload["allowaccess"]
        if value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid value for 'allowaccess'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )
    if "gwdetect" in payload:
        value = payload["gwdetect"]
        if value not in VALID_BODY_GWDETECT:
            return (
                False,
                f"Invalid value for 'gwdetect'='{value}'. Must be one of: {', '.join(VALID_BODY_GWDETECT)}",
            )
    if "detectprotocol" in payload:
        value = payload["detectprotocol"]
        if value not in VALID_BODY_DETECTPROTOCOL:
            return (
                False,
                f"Invalid value for 'detectprotocol'='{value}'. Must be one of: {', '.join(VALID_BODY_DETECTPROTOCOL)}",
            )
    if "fail-detect" in payload:
        value = payload["fail-detect"]
        if value not in VALID_BODY_FAIL_DETECT:
            return (
                False,
                f"Invalid value for 'fail-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT)}",
            )
    if "fail-detect-option" in payload:
        value = payload["fail-detect-option"]
        if value not in VALID_BODY_FAIL_DETECT_OPTION:
            return (
                False,
                f"Invalid value for 'fail-detect-option'='{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT_OPTION)}",
            )
    if "fail-alert-method" in payload:
        value = payload["fail-alert-method"]
        if value not in VALID_BODY_FAIL_ALERT_METHOD:
            return (
                False,
                f"Invalid value for 'fail-alert-method'='{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_ALERT_METHOD)}",
            )
    if "fail-action-on-extender" in payload:
        value = payload["fail-action-on-extender"]
        if value not in VALID_BODY_FAIL_ACTION_ON_EXTENDER:
            return (
                False,
                f"Invalid value for 'fail-action-on-extender'='{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_ACTION_ON_EXTENDER)}",
            )
    if "pppoe-egress-cos" in payload:
        value = payload["pppoe-egress-cos"]
        if value not in VALID_BODY_PPPOE_EGRESS_COS:
            return (
                False,
                f"Invalid value for 'pppoe-egress-cos'='{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_EGRESS_COS)}",
            )
    if "pppoe-unnumbered-negotiate" in payload:
        value = payload["pppoe-unnumbered-negotiate"]
        if value not in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE:
            return (
                False,
                f"Invalid value for 'pppoe-unnumbered-negotiate'='{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE)}",
            )
    if "multilink" in payload:
        value = payload["multilink"]
        if value not in VALID_BODY_MULTILINK:
            return (
                False,
                f"Invalid value for 'multilink'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTILINK)}",
            )
    if "defaultgw" in payload:
        value = payload["defaultgw"]
        if value not in VALID_BODY_DEFAULTGW:
            return (
                False,
                f"Invalid value for 'defaultgw'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULTGW)}",
            )
    if "dns-server-override" in payload:
        value = payload["dns-server-override"]
        if value not in VALID_BODY_DNS_SERVER_OVERRIDE:
            return (
                False,
                f"Invalid value for 'dns-server-override'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVER_OVERRIDE)}",
            )
    if "dns-server-protocol" in payload:
        value = payload["dns-server-protocol"]
        if value not in VALID_BODY_DNS_SERVER_PROTOCOL:
            return (
                False,
                f"Invalid value for 'dns-server-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVER_PROTOCOL)}",
            )
    if "auth-type" in payload:
        value = payload["auth-type"]
        if value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )
    if "pptp-client" in payload:
        value = payload["pptp-client"]
        if value not in VALID_BODY_PPTP_CLIENT:
            return (
                False,
                f"Invalid value for 'pptp-client'='{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_CLIENT)}",
            )
    if "pptp-auth-type" in payload:
        value = payload["pptp-auth-type"]
        if value not in VALID_BODY_PPTP_AUTH_TYPE:
            return (
                False,
                f"Invalid value for 'pptp-auth-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_AUTH_TYPE)}",
            )
    if "arpforward" in payload:
        value = payload["arpforward"]
        if value not in VALID_BODY_ARPFORWARD:
            return (
                False,
                f"Invalid value for 'arpforward'='{value}'. Must be one of: {', '.join(VALID_BODY_ARPFORWARD)}",
            )
    if "ndiscforward" in payload:
        value = payload["ndiscforward"]
        if value not in VALID_BODY_NDISCFORWARD:
            return (
                False,
                f"Invalid value for 'ndiscforward'='{value}'. Must be one of: {', '.join(VALID_BODY_NDISCFORWARD)}",
            )
    if "broadcast-forward" in payload:
        value = payload["broadcast-forward"]
        if value not in VALID_BODY_BROADCAST_FORWARD:
            return (
                False,
                f"Invalid value for 'broadcast-forward'='{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_FORWARD)}",
            )
    if "bfd" in payload:
        value = payload["bfd"]
        if value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid value for 'bfd'='{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )
    if "l2forward" in payload:
        value = payload["l2forward"]
        if value not in VALID_BODY_L2FORWARD:
            return (
                False,
                f"Invalid value for 'l2forward'='{value}'. Must be one of: {', '.join(VALID_BODY_L2FORWARD)}",
            )
    if "icmp-send-redirect" in payload:
        value = payload["icmp-send-redirect"]
        if value not in VALID_BODY_ICMP_SEND_REDIRECT:
            return (
                False,
                f"Invalid value for 'icmp-send-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_SEND_REDIRECT)}",
            )
    if "icmp-accept-redirect" in payload:
        value = payload["icmp-accept-redirect"]
        if value not in VALID_BODY_ICMP_ACCEPT_REDIRECT:
            return (
                False,
                f"Invalid value for 'icmp-accept-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_ACCEPT_REDIRECT)}",
            )
    if "vlanforward" in payload:
        value = payload["vlanforward"]
        if value not in VALID_BODY_VLANFORWARD:
            return (
                False,
                f"Invalid value for 'vlanforward'='{value}'. Must be one of: {', '.join(VALID_BODY_VLANFORWARD)}",
            )
    if "stpforward" in payload:
        value = payload["stpforward"]
        if value not in VALID_BODY_STPFORWARD:
            return (
                False,
                f"Invalid value for 'stpforward'='{value}'. Must be one of: {', '.join(VALID_BODY_STPFORWARD)}",
            )
    if "stpforward-mode" in payload:
        value = payload["stpforward-mode"]
        if value not in VALID_BODY_STPFORWARD_MODE:
            return (
                False,
                f"Invalid value for 'stpforward-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_STPFORWARD_MODE)}",
            )
    if "ips-sniffer-mode" in payload:
        value = payload["ips-sniffer-mode"]
        if value not in VALID_BODY_IPS_SNIFFER_MODE:
            return (
                False,
                f"Invalid value for 'ips-sniffer-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SNIFFER_MODE)}",
            )
    if "ident-accept" in payload:
        value = payload["ident-accept"]
        if value not in VALID_BODY_IDENT_ACCEPT:
            return (
                False,
                f"Invalid value for 'ident-accept'='{value}'. Must be one of: {', '.join(VALID_BODY_IDENT_ACCEPT)}",
            )
    if "ipmac" in payload:
        value = payload["ipmac"]
        if value not in VALID_BODY_IPMAC:
            return (
                False,
                f"Invalid value for 'ipmac'='{value}'. Must be one of: {', '.join(VALID_BODY_IPMAC)}",
            )
    if "subst" in payload:
        value = payload["subst"]
        if value not in VALID_BODY_SUBST:
            return (
                False,
                f"Invalid value for 'subst'='{value}'. Must be one of: {', '.join(VALID_BODY_SUBST)}",
            )
    if "speed" in payload:
        value = payload["speed"]
        if value not in VALID_BODY_SPEED:
            return (
                False,
                f"Invalid value for 'speed'='{value}'. Must be one of: {', '.join(VALID_BODY_SPEED)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "netbios-forward" in payload:
        value = payload["netbios-forward"]
        if value not in VALID_BODY_NETBIOS_FORWARD:
            return (
                False,
                f"Invalid value for 'netbios-forward'='{value}'. Must be one of: {', '.join(VALID_BODY_NETBIOS_FORWARD)}",
            )
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "dedicated-to" in payload:
        value = payload["dedicated-to"]
        if value not in VALID_BODY_DEDICATED_TO:
            return (
                False,
                f"Invalid value for 'dedicated-to'='{value}'. Must be one of: {', '.join(VALID_BODY_DEDICATED_TO)}",
            )
    if "wccp" in payload:
        value = payload["wccp"]
        if value not in VALID_BODY_WCCP:
            return (
                False,
                f"Invalid value for 'wccp'='{value}'. Must be one of: {', '.join(VALID_BODY_WCCP)}",
            )
    if "netflow-sampler" in payload:
        value = payload["netflow-sampler"]
        if value not in VALID_BODY_NETFLOW_SAMPLER:
            return (
                False,
                f"Invalid value for 'netflow-sampler'='{value}'. Must be one of: {', '.join(VALID_BODY_NETFLOW_SAMPLER)}",
            )
    if "sflow-sampler" in payload:
        value = payload["sflow-sampler"]
        if value not in VALID_BODY_SFLOW_SAMPLER:
            return (
                False,
                f"Invalid value for 'sflow-sampler'='{value}'. Must be one of: {', '.join(VALID_BODY_SFLOW_SAMPLER)}",
            )
    if "drop-fragment" in payload:
        value = payload["drop-fragment"]
        if value not in VALID_BODY_DROP_FRAGMENT:
            return (
                False,
                f"Invalid value for 'drop-fragment'='{value}'. Must be one of: {', '.join(VALID_BODY_DROP_FRAGMENT)}",
            )
    if "src-check" in payload:
        value = payload["src-check"]
        if value not in VALID_BODY_SRC_CHECK:
            return (
                False,
                f"Invalid value for 'src-check'='{value}'. Must be one of: {', '.join(VALID_BODY_SRC_CHECK)}",
            )
    if "sample-direction" in payload:
        value = payload["sample-direction"]
        if value not in VALID_BODY_SAMPLE_DIRECTION:
            return (
                False,
                f"Invalid value for 'sample-direction'='{value}'. Must be one of: {', '.join(VALID_BODY_SAMPLE_DIRECTION)}",
            )
    if "explicit-web-proxy" in payload:
        value = payload["explicit-web-proxy"]
        if value not in VALID_BODY_EXPLICIT_WEB_PROXY:
            return (
                False,
                f"Invalid value for 'explicit-web-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_EXPLICIT_WEB_PROXY)}",
            )
    if "explicit-ftp-proxy" in payload:
        value = payload["explicit-ftp-proxy"]
        if value not in VALID_BODY_EXPLICIT_FTP_PROXY:
            return (
                False,
                f"Invalid value for 'explicit-ftp-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_EXPLICIT_FTP_PROXY)}",
            )
    if "proxy-captive-portal" in payload:
        value = payload["proxy-captive-portal"]
        if value not in VALID_BODY_PROXY_CAPTIVE_PORTAL:
            return (
                False,
                f"Invalid value for 'proxy-captive-portal'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_CAPTIVE_PORTAL)}",
            )
    if "external" in payload:
        value = payload["external"]
        if value not in VALID_BODY_EXTERNAL:
            return (
                False,
                f"Invalid value for 'external'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL)}",
            )
    if "mtu-override" in payload:
        value = payload["mtu-override"]
        if value not in VALID_BODY_MTU_OVERRIDE:
            return (
                False,
                f"Invalid value for 'mtu-override'='{value}'. Must be one of: {', '.join(VALID_BODY_MTU_OVERRIDE)}",
            )
    if "vlan-protocol" in payload:
        value = payload["vlan-protocol"]
        if value not in VALID_BODY_VLAN_PROTOCOL:
            return (
                False,
                f"Invalid value for 'vlan-protocol'='{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_PROTOCOL)}",
            )
    if "lacp-mode" in payload:
        value = payload["lacp-mode"]
        if value not in VALID_BODY_LACP_MODE:
            return (
                False,
                f"Invalid value for 'lacp-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_LACP_MODE)}",
            )
    if "lacp-ha-secondary" in payload:
        value = payload["lacp-ha-secondary"]
        if value not in VALID_BODY_LACP_HA_SECONDARY:
            return (
                False,
                f"Invalid value for 'lacp-ha-secondary'='{value}'. Must be one of: {', '.join(VALID_BODY_LACP_HA_SECONDARY)}",
            )
    if "system-id-type" in payload:
        value = payload["system-id-type"]
        if value not in VALID_BODY_SYSTEM_ID_TYPE:
            return (
                False,
                f"Invalid value for 'system-id-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_ID_TYPE)}",
            )
    if "lacp-speed" in payload:
        value = payload["lacp-speed"]
        if value not in VALID_BODY_LACP_SPEED:
            return (
                False,
                f"Invalid value for 'lacp-speed'='{value}'. Must be one of: {', '.join(VALID_BODY_LACP_SPEED)}",
            )
    if "min-links-down" in payload:
        value = payload["min-links-down"]
        if value not in VALID_BODY_MIN_LINKS_DOWN:
            return (
                False,
                f"Invalid value for 'min-links-down'='{value}'. Must be one of: {', '.join(VALID_BODY_MIN_LINKS_DOWN)}",
            )
    if "algorithm" in payload:
        value = payload["algorithm"]
        if value not in VALID_BODY_ALGORITHM:
            return (
                False,
                f"Invalid value for 'algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_ALGORITHM)}",
            )
    if "aggregate-type" in payload:
        value = payload["aggregate-type"]
        if value not in VALID_BODY_AGGREGATE_TYPE:
            return (
                False,
                f"Invalid value for 'aggregate-type'='{value}'. Must be one of: {', '.join(VALID_BODY_AGGREGATE_TYPE)}",
            )
    if "priority-override" in payload:
        value = payload["priority-override"]
        if value not in VALID_BODY_PRIORITY_OVERRIDE:
            return (
                False,
                f"Invalid value for 'priority-override'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_OVERRIDE)}",
            )
    if "security-mode" in payload:
        value = payload["security-mode"]
        if value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid value for 'security-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )
    if "security-mac-auth-bypass" in payload:
        value = payload["security-mac-auth-bypass"]
        if value not in VALID_BODY_SECURITY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid value for 'security-mac-auth-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MAC_AUTH_BYPASS)}",
            )
    if "security-ip-auth-bypass" in payload:
        value = payload["security-ip-auth-bypass"]
        if value not in VALID_BODY_SECURITY_IP_AUTH_BYPASS:
            return (
                False,
                f"Invalid value for 'security-ip-auth-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_IP_AUTH_BYPASS)}",
            )
    if "device-identification" in payload:
        value = payload["device-identification"]
        if value not in VALID_BODY_DEVICE_IDENTIFICATION:
            return (
                False,
                f"Invalid value for 'device-identification'='{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_IDENTIFICATION)}",
            )
    if "exclude-signatures" in payload:
        value = payload["exclude-signatures"]
        if value not in VALID_BODY_EXCLUDE_SIGNATURES:
            return (
                False,
                f"Invalid value for 'exclude-signatures'='{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE_SIGNATURES)}",
            )
    if "device-user-identification" in payload:
        value = payload["device-user-identification"]
        if value not in VALID_BODY_DEVICE_USER_IDENTIFICATION:
            return (
                False,
                f"Invalid value for 'device-user-identification'='{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_USER_IDENTIFICATION)}",
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
    if "monitor-bandwidth" in payload:
        value = payload["monitor-bandwidth"]
        if value not in VALID_BODY_MONITOR_BANDWIDTH:
            return (
                False,
                f"Invalid value for 'monitor-bandwidth'='{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_BANDWIDTH)}",
            )
    if "vrrp-virtual-mac" in payload:
        value = payload["vrrp-virtual-mac"]
        if value not in VALID_BODY_VRRP_VIRTUAL_MAC:
            return (
                False,
                f"Invalid value for 'vrrp-virtual-mac'='{value}'. Must be one of: {', '.join(VALID_BODY_VRRP_VIRTUAL_MAC)}",
            )
    if "role" in payload:
        value = payload["role"]
        if value not in VALID_BODY_ROLE:
            return (
                False,
                f"Invalid value for 'role'='{value}'. Must be one of: {', '.join(VALID_BODY_ROLE)}",
            )
    if "secondary-IP" in payload:
        value = payload["secondary-IP"]
        if value not in VALID_BODY_SECONDARY_IP:
            return (
                False,
                f"Invalid value for 'secondary-IP'='{value}'. Must be one of: {', '.join(VALID_BODY_SECONDARY_IP)}",
            )
    if "preserve-session-route" in payload:
        value = payload["preserve-session-route"]
        if value not in VALID_BODY_PRESERVE_SESSION_ROUTE:
            return (
                False,
                f"Invalid value for 'preserve-session-route'='{value}'. Must be one of: {', '.join(VALID_BODY_PRESERVE_SESSION_ROUTE)}",
            )
    if "auto-auth-extension-device" in payload:
        value = payload["auto-auth-extension-device"]
        if value not in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE:
            return (
                False,
                f"Invalid value for 'auto-auth-extension-device'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE)}",
            )
    if "ap-discover" in payload:
        value = payload["ap-discover"]
        if value not in VALID_BODY_AP_DISCOVER:
            return (
                False,
                f"Invalid value for 'ap-discover'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_DISCOVER)}",
            )
    if "fortilink-neighbor-detect" in payload:
        value = payload["fortilink-neighbor-detect"]
        if value not in VALID_BODY_FORTILINK_NEIGHBOR_DETECT:
            return (
                False,
                f"Invalid value for 'fortilink-neighbor-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK_NEIGHBOR_DETECT)}",
            )
    if "ip-managed-by-fortiipam" in payload:
        value = payload["ip-managed-by-fortiipam"]
        if value not in VALID_BODY_IP_MANAGED_BY_FORTIIPAM:
            return (
                False,
                f"Invalid value for 'ip-managed-by-fortiipam'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_MANAGED_BY_FORTIIPAM)}",
            )
    if "managed-subnetwork-size" in payload:
        value = payload["managed-subnetwork-size"]
        if value not in VALID_BODY_MANAGED_SUBNETWORK_SIZE:
            return (
                False,
                f"Invalid value for 'managed-subnetwork-size'='{value}'. Must be one of: {', '.join(VALID_BODY_MANAGED_SUBNETWORK_SIZE)}",
            )
    if "fortilink-split-interface" in payload:
        value = payload["fortilink-split-interface"]
        if value not in VALID_BODY_FORTILINK_SPLIT_INTERFACE:
            return (
                False,
                f"Invalid value for 'fortilink-split-interface'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK_SPLIT_INTERFACE)}",
            )
    if "switch-controller-access-vlan" in payload:
        value = payload["switch-controller-access-vlan"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN:
            return (
                False,
                f"Invalid value for 'switch-controller-access-vlan'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN)}",
            )
    if "switch-controller-rspan-mode" in payload:
        value = payload["switch-controller-rspan-mode"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE:
            return (
                False,
                f"Invalid value for 'switch-controller-rspan-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE)}",
            )
    if "switch-controller-netflow-collect" in payload:
        value = payload["switch-controller-netflow-collect"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT:
            return (
                False,
                f"Invalid value for 'switch-controller-netflow-collect'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT)}",
            )
    if "switch-controller-igmp-snooping" in payload:
        value = payload["switch-controller-igmp-snooping"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING:
            return (
                False,
                f"Invalid value for 'switch-controller-igmp-snooping'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING)}",
            )
    if "switch-controller-igmp-snooping-proxy" in payload:
        value = payload["switch-controller-igmp-snooping-proxy"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY:
            return (
                False,
                f"Invalid value for 'switch-controller-igmp-snooping-proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY)}",
            )
    if "switch-controller-igmp-snooping-fast-leave" in payload:
        value = payload["switch-controller-igmp-snooping-fast-leave"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE:
            return (
                False,
                f"Invalid value for 'switch-controller-igmp-snooping-fast-leave'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE)}",
            )
    if "switch-controller-dhcp-snooping" in payload:
        value = payload["switch-controller-dhcp-snooping"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING:
            return (
                False,
                f"Invalid value for 'switch-controller-dhcp-snooping'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING)}",
            )
    if "switch-controller-dhcp-snooping-verify-mac" in payload:
        value = payload["switch-controller-dhcp-snooping-verify-mac"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC:
            return (
                False,
                f"Invalid value for 'switch-controller-dhcp-snooping-verify-mac'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC)}",
            )
    if "switch-controller-dhcp-snooping-option82" in payload:
        value = payload["switch-controller-dhcp-snooping-option82"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82:
            return (
                False,
                f"Invalid value for 'switch-controller-dhcp-snooping-option82'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82)}",
            )
    if "switch-controller-arp-inspection" in payload:
        value = payload["switch-controller-arp-inspection"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION:
            return (
                False,
                f"Invalid value for 'switch-controller-arp-inspection'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION)}",
            )
    if "switch-controller-feature" in payload:
        value = payload["switch-controller-feature"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_FEATURE:
            return (
                False,
                f"Invalid value for 'switch-controller-feature'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_FEATURE)}",
            )
    if "switch-controller-iot-scanning" in payload:
        value = payload["switch-controller-iot-scanning"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING:
            return (
                False,
                f"Invalid value for 'switch-controller-iot-scanning'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING)}",
            )
    if "switch-controller-offload" in payload:
        value = payload["switch-controller-offload"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD:
            return (
                False,
                f"Invalid value for 'switch-controller-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_OFFLOAD)}",
            )
    if "switch-controller-offload-gw" in payload:
        value = payload["switch-controller-offload-gw"]
        if value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW:
            return (
                False,
                f"Invalid value for 'switch-controller-offload-gw'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW)}",
            )
    if "eap-supplicant" in payload:
        value = payload["eap-supplicant"]
        if value not in VALID_BODY_EAP_SUPPLICANT:
            return (
                False,
                f"Invalid value for 'eap-supplicant'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_SUPPLICANT)}",
            )
    if "eap-method" in payload:
        value = payload["eap-method"]
        if value not in VALID_BODY_EAP_METHOD:
            return (
                False,
                f"Invalid value for 'eap-method'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_METHOD)}",
            )
    if "default-purdue-level" in payload:
        value = payload["default-purdue-level"]
        if value not in VALID_BODY_DEFAULT_PURDUE_LEVEL:
            return (
                False,
                f"Invalid value for 'default-purdue-level'='{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_PURDUE_LEVEL)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "system/interface",
    "category": "cmdb",
    "api_path": "system/interface",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure interfaces.",
    "total_fields": 222,
    "required_fields_count": 3,
    "fields_with_defaults_count": 205,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
