"""
Validation helpers for vpn/ipsec/phase1 endpoint.

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
    "interface",  # Local physical, aggregate, or VLAN outgoing interface.
    "remotegw-ddns",  # Domain name of remote gateway. For example, name.ddns.com.
    "certificate",  # Names of up to 4 signed personal certificates.
    "peerid",  # Accept this peer identity.
    "usrgrp",  # User group name for dialup peers.
    "peer",  # Accept this peer certificate.
    "peergrp",  # Accept this peer certificate group.
    "proposal",  # Phase1 proposal.
    "psksecret",  # Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).
    "psksecret-remote",  # Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).
    "ppk-secret",  # IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).
    "authusr",  # XAuth user name.
    "authpasswd",  # XAuth password (max 35 characters).
    "group-authentication-secret",  # Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x.
    "dev-id",  # Device ID carried by the device ID notification.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "type": "static",
    "interface": "",
    "ike-version": "1",
    "remote-gw": "0.0.0.0",
    "local-gw": "0.0.0.0",
    "remotegw-ddns": "",
    "keylife": 86400,
    "authmethod": "psk",
    "authmethod-remote": "",
    "mode": "main",
    "peertype": "peer",
    "peerid": "",
    "usrgrp": "",
    "peer": "",
    "peergrp": "",
    "mode-cfg": "disable",
    "mode-cfg-allow-client-selector": "disable",
    "assign-ip": "enable",
    "assign-ip-from": "range",
    "ipv4-start-ip": "0.0.0.0",
    "ipv4-end-ip": "0.0.0.0",
    "ipv4-netmask": "255.255.255.255",
    "dhcp-ra-giaddr": "0.0.0.0",
    "dhcp6-ra-linkaddr": "::",
    "dns-mode": "manual",
    "ipv4-dns-server1": "0.0.0.0",
    "ipv4-dns-server2": "0.0.0.0",
    "ipv4-dns-server3": "0.0.0.0",
    "ipv4-wins-server1": "0.0.0.0",
    "ipv4-wins-server2": "0.0.0.0",
    "ipv4-split-include": "",
    "split-include-service": "",
    "ipv4-name": "",
    "ipv6-start-ip": "::",
    "ipv6-end-ip": "::",
    "ipv6-prefix": 128,
    "ipv6-dns-server1": "::",
    "ipv6-dns-server2": "::",
    "ipv6-dns-server3": "::",
    "ipv6-split-include": "",
    "ipv6-name": "",
    "ip-delay-interval": 0,
    "unity-support": "enable",
    "domain": "",
    "include-local-lan": "disable",
    "ipv4-split-exclude": "",
    "ipv6-split-exclude": "",
    "save-password": "disable",
    "client-auto-negotiate": "disable",
    "client-keep-alive": "disable",
    "proposal": "",
    "add-route": "disable",
    "add-gw-route": "disable",
    "keepalive": 10,
    "distance": 15,
    "priority": 1,
    "localid": "",
    "localid-type": "auto",
    "auto-negotiate": "enable",
    "negotiate-timeout": 30,
    "fragmentation": "enable",
    "dpd": "on-demand",
    "dpd-retrycount": 3,
    "dpd-retryinterval": "",
    "npu-offload": "enable",
    "send-cert-chain": "enable",
    "dhgrp": "20",
    "addke1": "",
    "addke2": "",
    "addke3": "",
    "addke4": "",
    "addke5": "",
    "addke6": "",
    "addke7": "",
    "suite-b": "disable",
    "eap": "disable",
    "eap-identity": "use-id-payload",
    "eap-exclude-peergrp": "",
    "eap-cert-auth": "disable",
    "acct-verify": "disable",
    "ppk": "disable",
    "ppk-identity": "",
    "wizard-type": "custom",
    "xauthtype": "disable",
    "reauth": "disable",
    "authusr": "",
    "group-authentication": "disable",
    "authusrgrp": "",
    "mesh-selector-type": "disable",
    "idle-timeout": "disable",
    "shared-idle-timeout": "disable",
    "idle-timeoutinterval": 15,
    "ha-sync-esp-seqno": "enable",
    "fgsp-sync": "disable",
    "inbound-dscp-copy": "disable",
    "nattraversal": "enable",
    "esn": "disable",
    "fragmentation-mtu": 1200,
    "childless-ike": "disable",
    "azure-ad-autoconnect": "disable",
    "client-resume": "disable",
    "client-resume-interval": 7200,
    "rekey": "enable",
    "digital-signature-auth": "disable",
    "signature-hash-alg": "sha2-512",
    "rsa-signature-format": "pkcs1",
    "rsa-signature-hash-override": "disable",
    "enforce-unique-id": "disable",
    "cert-id-validation": "enable",
    "fec-egress": "disable",
    "fec-send-timeout": 5,
    "fec-base": 10,
    "fec-codec": "rs",
    "fec-redundant": 1,
    "fec-ingress": "disable",
    "fec-receive-timeout": 50,
    "fec-health-check": "",
    "fec-mapping-profile": "",
    "network-overlay": "disable",
    "network-id": 0,
    "dev-id-notification": "disable",
    "dev-id": "",
    "loopback-asymroute": "enable",
    "link-cost": 0,
    "kms": "",
    "exchange-fgt-device-id": "disable",
    "ipv6-auto-linklocal": "disable",
    "ems-sn-check": "disable",
    "cert-trust-store": "local",
    "qkd": "disable",
    "qkd-hybrid": "disable",
    "qkd-profile": "",
    "transport": "auto",
    "fortinet-esp": "disable",
    "auto-transport-threshold": 15,
    "remote-gw-match": "any",
    "remote-gw-subnet": "0.0.0.0 0.0.0.0",
    "remote-gw-start-ip": "0.0.0.0",
    "remote-gw-end-ip": "0.0.0.0",
    "remote-gw-country": "",
    "remote-gw6-match": "any",
    "remote-gw6-subnet": "::/0",
    "remote-gw6-start-ip": "::",
    "remote-gw6-end-ip": "::",
    "remote-gw6-country": "",
    "cert-peer-username-validation": "none",
    "cert-peer-username-strip": "disable",
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
    "name": "string",  # IPsec remote gateway name.
    "type": "option",  # Remote gateway type.
    "interface": "string",  # Local physical, aggregate, or VLAN outgoing interface.
    "ike-version": "option",  # IKE protocol version.
    "remote-gw": "ipv4-address",  # Remote VPN gateway.
    "local-gw": "ipv4-address",  # Local VPN gateway.
    "remotegw-ddns": "string",  # Domain name of remote gateway. For example, name.ddns.com.
    "keylife": "integer",  # Time to wait in seconds before phase 1 encryption key expire
    "certificate": "string",  # Names of up to 4 signed personal certificates.
    "authmethod": "option",  # Authentication method.
    "authmethod-remote": "option",  # Authentication method (remote side).
    "mode": "option",  # ID protection mode used to establish a secure channel.
    "peertype": "option",  # Accept this peer type.
    "peerid": "string",  # Accept this peer identity.
    "usrgrp": "string",  # User group name for dialup peers.
    "peer": "string",  # Accept this peer certificate.
    "peergrp": "string",  # Accept this peer certificate group.
    "mode-cfg": "option",  # Enable/disable configuration method.
    "mode-cfg-allow-client-selector": "option",  # Enable/disable mode-cfg client to use custom phase2 selector
    "assign-ip": "option",  # Enable/disable assignment of IP to IPsec interface via confi
    "assign-ip-from": "option",  # Method by which the IP address will be assigned.
    "ipv4-start-ip": "ipv4-address",  # Start of IPv4 range.
    "ipv4-end-ip": "ipv4-address",  # End of IPv4 range.
    "ipv4-netmask": "ipv4-netmask",  # IPv4 Netmask.
    "dhcp-ra-giaddr": "ipv4-address",  # Relay agent gateway IP address to use in the giaddr field of
    "dhcp6-ra-linkaddr": "ipv6-address",  # Relay agent IPv6 link address to use in DHCP6 requests.
    "dns-mode": "option",  # DNS server mode.
    "ipv4-dns-server1": "ipv4-address",  # IPv4 DNS server 1.
    "ipv4-dns-server2": "ipv4-address",  # IPv4 DNS server 2.
    "ipv4-dns-server3": "ipv4-address",  # IPv4 DNS server 3.
    "internal-domain-list": "string",  # One or more internal domain names in quotes separated by spa
    "dns-suffix-search": "string",  # One or more DNS domain name suffixes in quotes separated by 
    "ipv4-wins-server1": "ipv4-address",  # WINS server 1.
    "ipv4-wins-server2": "ipv4-address",  # WINS server 2.
    "ipv4-exclude-range": "string",  # Configuration Method IPv4 exclude ranges.
    "ipv4-split-include": "string",  # IPv4 split-include subnets.
    "split-include-service": "string",  # Split-include services.
    "ipv4-name": "string",  # IPv4 address name.
    "ipv6-start-ip": "ipv6-address",  # Start of IPv6 range.
    "ipv6-end-ip": "ipv6-address",  # End of IPv6 range.
    "ipv6-prefix": "integer",  # IPv6 prefix.
    "ipv6-dns-server1": "ipv6-address",  # IPv6 DNS server 1.
    "ipv6-dns-server2": "ipv6-address",  # IPv6 DNS server 2.
    "ipv6-dns-server3": "ipv6-address",  # IPv6 DNS server 3.
    "ipv6-exclude-range": "string",  # Configuration method IPv6 exclude ranges.
    "ipv6-split-include": "string",  # IPv6 split-include subnets.
    "ipv6-name": "string",  # IPv6 address name.
    "ip-delay-interval": "integer",  # IP address reuse delay interval in seconds (0 - 28800).
    "unity-support": "option",  # Enable/disable support for Cisco UNITY Configuration Method 
    "domain": "string",  # Instruct unity clients about the single default DNS domain.
    "banner": "var-string",  # Message that unity client should display after connecting.
    "include-local-lan": "option",  # Enable/disable allow local LAN access on unity clients.
    "ipv4-split-exclude": "string",  # IPv4 subnets that should not be sent over the IPsec tunnel.
    "ipv6-split-exclude": "string",  # IPv6 subnets that should not be sent over the IPsec tunnel.
    "save-password": "option",  # Enable/disable saving XAuth username and password on VPN cli
    "client-auto-negotiate": "option",  # Enable/disable allowing the VPN client to bring up the tunne
    "client-keep-alive": "option",  # Enable/disable allowing the VPN client to keep the tunnel up
    "backup-gateway": "string",  # Instruct unity clients about the backup gateway address(es).
    "proposal": "option",  # Phase1 proposal.
    "add-route": "option",  # Enable/disable control addition of a route to peer destinati
    "add-gw-route": "option",  # Enable/disable automatically add a route to the remote gatew
    "psksecret": "password-3",  # Pre-shared secret for PSK authentication (ASCII string or he
    "psksecret-remote": "password-3",  # Pre-shared secret for remote side PSK authentication (ASCII 
    "keepalive": "integer",  # NAT-T keep alive interval.
    "distance": "integer",  # Distance for routes added by IKE (1 - 255).
    "priority": "integer",  # Priority for routes added by IKE (1 - 65535).
    "localid": "string",  # Local ID.
    "localid-type": "option",  # Local ID type.
    "auto-negotiate": "option",  # Enable/disable automatic initiation of IKE SA negotiation.
    "negotiate-timeout": "integer",  # IKE SA negotiation timeout in seconds (1 - 300).
    "fragmentation": "option",  # Enable/disable fragment IKE message on re-transmission.
    "dpd": "option",  # Dead Peer Detection mode.
    "dpd-retrycount": "integer",  # Number of DPD retry attempts.
    "dpd-retryinterval": "user",  # DPD retry interval.
    "comments": "var-string",  # Comment.
    "npu-offload": "option",  # Enable/disable offloading NPU.
    "send-cert-chain": "option",  # Enable/disable sending certificate chain.
    "dhgrp": "option",  # DH group.
    "addke1": "option",  # ADDKE1 group.
    "addke2": "option",  # ADDKE2 group.
    "addke3": "option",  # ADDKE3 group.
    "addke4": "option",  # ADDKE4 group.
    "addke5": "option",  # ADDKE5 group.
    "addke6": "option",  # ADDKE6 group.
    "addke7": "option",  # ADDKE7 group.
    "suite-b": "option",  # Use Suite-B.
    "eap": "option",  # Enable/disable IKEv2 EAP authentication.
    "eap-identity": "option",  # IKEv2 EAP peer identity type.
    "eap-exclude-peergrp": "string",  # Peer group excluded from EAP authentication.
    "eap-cert-auth": "option",  # Enable/disable peer certificate authentication in addition t
    "acct-verify": "option",  # Enable/disable verification of RADIUS accounting record.
    "ppk": "option",  # Enable/disable IKEv2 Postquantum Preshared Key (PPK).
    "ppk-secret": "password-3",  # IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal
    "ppk-identity": "string",  # IKEv2 Postquantum Preshared Key Identity.
    "wizard-type": "option",  # GUI VPN Wizard Type.
    "xauthtype": "option",  # XAuth type.
    "reauth": "option",  # Enable/disable re-authentication upon IKE SA lifetime expira
    "authusr": "string",  # XAuth user name.
    "authpasswd": "password",  # XAuth password (max 35 characters).
    "group-authentication": "option",  # Enable/disable IKEv2 IDi group authentication.
    "group-authentication-secret": "password-3",  # Password for IKEv2 ID group authentication. ASCII string or 
    "authusrgrp": "string",  # Authentication user group.
    "mesh-selector-type": "option",  # Add selectors containing subsets of the configuration depend
    "idle-timeout": "option",  # Enable/disable IPsec tunnel idle timeout.
    "shared-idle-timeout": "option",  # Enable/disable IPsec tunnel shared idle timeout.
    "idle-timeoutinterval": "integer",  # IPsec tunnel idle timeout in minutes (5 - 43200).
    "ha-sync-esp-seqno": "option",  # Enable/disable sequence number jump ahead for IPsec HA.
    "fgsp-sync": "option",  # Enable/disable IPsec syncing of tunnels for FGSP IPsec.
    "inbound-dscp-copy": "option",  # Enable/disable copy the dscp in the ESP header to the inner 
    "nattraversal": "option",  # Enable/disable NAT traversal.
    "esn": "option",  # Extended sequence number (ESN) negotiation.
    "fragmentation-mtu": "integer",  # IKE fragmentation MTU (500 - 16000).
    "childless-ike": "option",  # Enable/disable childless IKEv2 initiation (RFC 6023).
    "azure-ad-autoconnect": "option",  # Enable/disable Azure AD Auto-Connect for FortiClient.
    "client-resume": "option",  # Enable/disable resumption of offline FortiClient sessions.  
    "client-resume-interval": "integer",  # Maximum time in seconds during which a VPN client may resume
    "rekey": "option",  # Enable/disable phase1 rekey.
    "digital-signature-auth": "option",  # Enable/disable IKEv2 Digital Signature Authentication (RFC 7
    "signature-hash-alg": "option",  # Digital Signature Authentication hash algorithms.
    "rsa-signature-format": "option",  # Digital Signature Authentication RSA signature format.
    "rsa-signature-hash-override": "option",  # Enable/disable IKEv2 RSA signature hash algorithm override.
    "enforce-unique-id": "option",  # Enable/disable peer ID uniqueness check.
    "cert-id-validation": "option",  # Enable/disable cross validation of peer ID and the identity 
    "fec-egress": "option",  # Enable/disable Forward Error Correction for egress IPsec tra
    "fec-send-timeout": "integer",  # Timeout in milliseconds before sending Forward Error Correct
    "fec-base": "integer",  # Number of base Forward Error Correction packets (1 - 20).
    "fec-codec": "option",  # Forward Error Correction encoding/decoding algorithm.
    "fec-redundant": "integer",  # Number of redundant Forward Error Correction packets (1 - 5 
    "fec-ingress": "option",  # Enable/disable Forward Error Correction for ingress IPsec tr
    "fec-receive-timeout": "integer",  # Timeout in milliseconds before dropping Forward Error Correc
    "fec-health-check": "string",  # SD-WAN health check.
    "fec-mapping-profile": "string",  # Forward Error Correction (FEC) mapping profile.
    "network-overlay": "option",  # Enable/disable network overlays.
    "network-id": "integer",  # VPN gateway network ID.
    "dev-id-notification": "option",  # Enable/disable device ID notification.
    "dev-id": "string",  # Device ID carried by the device ID notification.
    "loopback-asymroute": "option",  # Enable/disable asymmetric routing for IKE traffic on loopbac
    "link-cost": "integer",  # VPN tunnel underlay link cost.
    "kms": "string",  # Key Management Services server.
    "exchange-fgt-device-id": "option",  # Enable/disable device identifier exchange with peer FortiGat
    "ipv6-auto-linklocal": "option",  # Enable/disable auto generation of IPv6 link-local address us
    "ems-sn-check": "option",  # Enable/disable verification of EMS serial number.
    "cert-trust-store": "option",  # CA certificate trust store.
    "qkd": "option",  # Enable/disable use of Quantum Key Distribution (QKD) server.
    "qkd-hybrid": "option",  # Enable/disable use of Quantum Key Distribution (QKD) hybrid 
    "qkd-profile": "string",  # Quantum Key Distribution (QKD) server profile.
    "transport": "option",  # Set IKE transport protocol.
    "fortinet-esp": "option",  # Enable/disable Fortinet ESP encapsulation.
    "auto-transport-threshold": "integer",  # Timeout in seconds before falling back to next transport pro
    "remote-gw-match": "option",  # Set type of IPv4 remote gateway address matching.
    "remote-gw-subnet": "ipv4-classnet-any",  # IPv4 address and subnet mask.
    "remote-gw-start-ip": "ipv4-address-any",  # First IPv4 address in the range.
    "remote-gw-end-ip": "ipv4-address-any",  # Last IPv4 address in the range.
    "remote-gw-country": "string",  # IPv4 addresses associated to a specific country.
    "remote-gw-ztna-tags": "string",  # IPv4 ZTNA posture tags.
    "remote-gw6-match": "option",  # Set type of IPv6 remote gateway address matching.
    "remote-gw6-subnet": "ipv6-network",  # IPv6 address and prefix.
    "remote-gw6-start-ip": "ipv6-address",  # First IPv6 address in the range.
    "remote-gw6-end-ip": "ipv6-address",  # Last IPv6 address in the range.
    "remote-gw6-country": "string",  # IPv6 addresses associated to a specific country.
    "cert-peer-username-validation": "option",  # Enable/disable cross validation of peer username and the ide
    "cert-peer-username-strip": "option",  # Enable/disable domain stripping on certificate identity.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "IPsec remote gateway name.",
    "type": "Remote gateway type.",
    "interface": "Local physical, aggregate, or VLAN outgoing interface.",
    "ike-version": "IKE protocol version.",
    "remote-gw": "Remote VPN gateway.",
    "local-gw": "Local VPN gateway.",
    "remotegw-ddns": "Domain name of remote gateway. For example, name.ddns.com.",
    "keylife": "Time to wait in seconds before phase 1 encryption key expires.",
    "certificate": "Names of up to 4 signed personal certificates.",
    "authmethod": "Authentication method.",
    "authmethod-remote": "Authentication method (remote side).",
    "mode": "ID protection mode used to establish a secure channel.",
    "peertype": "Accept this peer type.",
    "peerid": "Accept this peer identity.",
    "usrgrp": "User group name for dialup peers.",
    "peer": "Accept this peer certificate.",
    "peergrp": "Accept this peer certificate group.",
    "mode-cfg": "Enable/disable configuration method.",
    "mode-cfg-allow-client-selector": "Enable/disable mode-cfg client to use custom phase2 selectors.",
    "assign-ip": "Enable/disable assignment of IP to IPsec interface via configuration method.",
    "assign-ip-from": "Method by which the IP address will be assigned.",
    "ipv4-start-ip": "Start of IPv4 range.",
    "ipv4-end-ip": "End of IPv4 range.",
    "ipv4-netmask": "IPv4 Netmask.",
    "dhcp-ra-giaddr": "Relay agent gateway IP address to use in the giaddr field of DHCP requests.",
    "dhcp6-ra-linkaddr": "Relay agent IPv6 link address to use in DHCP6 requests.",
    "dns-mode": "DNS server mode.",
    "ipv4-dns-server1": "IPv4 DNS server 1.",
    "ipv4-dns-server2": "IPv4 DNS server 2.",
    "ipv4-dns-server3": "IPv4 DNS server 3.",
    "internal-domain-list": "One or more internal domain names in quotes separated by spaces.",
    "dns-suffix-search": "One or more DNS domain name suffixes in quotes separated by spaces.",
    "ipv4-wins-server1": "WINS server 1.",
    "ipv4-wins-server2": "WINS server 2.",
    "ipv4-exclude-range": "Configuration Method IPv4 exclude ranges.",
    "ipv4-split-include": "IPv4 split-include subnets.",
    "split-include-service": "Split-include services.",
    "ipv4-name": "IPv4 address name.",
    "ipv6-start-ip": "Start of IPv6 range.",
    "ipv6-end-ip": "End of IPv6 range.",
    "ipv6-prefix": "IPv6 prefix.",
    "ipv6-dns-server1": "IPv6 DNS server 1.",
    "ipv6-dns-server2": "IPv6 DNS server 2.",
    "ipv6-dns-server3": "IPv6 DNS server 3.",
    "ipv6-exclude-range": "Configuration method IPv6 exclude ranges.",
    "ipv6-split-include": "IPv6 split-include subnets.",
    "ipv6-name": "IPv6 address name.",
    "ip-delay-interval": "IP address reuse delay interval in seconds (0 - 28800).",
    "unity-support": "Enable/disable support for Cisco UNITY Configuration Method extensions.",
    "domain": "Instruct unity clients about the single default DNS domain.",
    "banner": "Message that unity client should display after connecting.",
    "include-local-lan": "Enable/disable allow local LAN access on unity clients.",
    "ipv4-split-exclude": "IPv4 subnets that should not be sent over the IPsec tunnel.",
    "ipv6-split-exclude": "IPv6 subnets that should not be sent over the IPsec tunnel.",
    "save-password": "Enable/disable saving XAuth username and password on VPN clients.",
    "client-auto-negotiate": "Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic.",
    "client-keep-alive": "Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic.",
    "backup-gateway": "Instruct unity clients about the backup gateway address(es).",
    "proposal": "Phase1 proposal.",
    "add-route": "Enable/disable control addition of a route to peer destination selector.",
    "add-gw-route": "Enable/disable automatically add a route to the remote gateway.",
    "psksecret": "Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).",
    "psksecret-remote": "Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).",
    "keepalive": "NAT-T keep alive interval.",
    "distance": "Distance for routes added by IKE (1 - 255).",
    "priority": "Priority for routes added by IKE (1 - 65535).",
    "localid": "Local ID.",
    "localid-type": "Local ID type.",
    "auto-negotiate": "Enable/disable automatic initiation of IKE SA negotiation.",
    "negotiate-timeout": "IKE SA negotiation timeout in seconds (1 - 300).",
    "fragmentation": "Enable/disable fragment IKE message on re-transmission.",
    "dpd": "Dead Peer Detection mode.",
    "dpd-retrycount": "Number of DPD retry attempts.",
    "dpd-retryinterval": "DPD retry interval.",
    "comments": "Comment.",
    "npu-offload": "Enable/disable offloading NPU.",
    "send-cert-chain": "Enable/disable sending certificate chain.",
    "dhgrp": "DH group.",
    "addke1": "ADDKE1 group.",
    "addke2": "ADDKE2 group.",
    "addke3": "ADDKE3 group.",
    "addke4": "ADDKE4 group.",
    "addke5": "ADDKE5 group.",
    "addke6": "ADDKE6 group.",
    "addke7": "ADDKE7 group.",
    "suite-b": "Use Suite-B.",
    "eap": "Enable/disable IKEv2 EAP authentication.",
    "eap-identity": "IKEv2 EAP peer identity type.",
    "eap-exclude-peergrp": "Peer group excluded from EAP authentication.",
    "eap-cert-auth": "Enable/disable peer certificate authentication in addition to EAP if peer is a FortiClient endpoint.",
    "acct-verify": "Enable/disable verification of RADIUS accounting record.",
    "ppk": "Enable/disable IKEv2 Postquantum Preshared Key (PPK).",
    "ppk-secret": "IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).",
    "ppk-identity": "IKEv2 Postquantum Preshared Key Identity.",
    "wizard-type": "GUI VPN Wizard Type.",
    "xauthtype": "XAuth type.",
    "reauth": "Enable/disable re-authentication upon IKE SA lifetime expiration.",
    "authusr": "XAuth user name.",
    "authpasswd": "XAuth password (max 35 characters).",
    "group-authentication": "Enable/disable IKEv2 IDi group authentication.",
    "group-authentication-secret": "Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x.",
    "authusrgrp": "Authentication user group.",
    "mesh-selector-type": "Add selectors containing subsets of the configuration depending on traffic.",
    "idle-timeout": "Enable/disable IPsec tunnel idle timeout.",
    "shared-idle-timeout": "Enable/disable IPsec tunnel shared idle timeout.",
    "idle-timeoutinterval": "IPsec tunnel idle timeout in minutes (5 - 43200).",
    "ha-sync-esp-seqno": "Enable/disable sequence number jump ahead for IPsec HA.",
    "fgsp-sync": "Enable/disable IPsec syncing of tunnels for FGSP IPsec.",
    "inbound-dscp-copy": "Enable/disable copy the dscp in the ESP header to the inner IP Header.",
    "nattraversal": "Enable/disable NAT traversal.",
    "esn": "Extended sequence number (ESN) negotiation.",
    "fragmentation-mtu": "IKE fragmentation MTU (500 - 16000).",
    "childless-ike": "Enable/disable childless IKEv2 initiation (RFC 6023).",
    "azure-ad-autoconnect": "Enable/disable Azure AD Auto-Connect for FortiClient.",
    "client-resume": "Enable/disable resumption of offline FortiClient sessions.  When a FortiClient enabled laptop is closed or enters sleep/hibernate mode, enabling this feature allows FortiClient to keep the tunnel during this period, and allows users to immediately resume using the IPsec tunnel when the device wakes up.",
    "client-resume-interval": "Maximum time in seconds during which a VPN client may resume using a tunnel after a client PC has entered sleep mode or temporarily lost its network connection (120 - 172800, default = 7200).",
    "rekey": "Enable/disable phase1 rekey.",
    "digital-signature-auth": "Enable/disable IKEv2 Digital Signature Authentication (RFC 7427).",
    "signature-hash-alg": "Digital Signature Authentication hash algorithms.",
    "rsa-signature-format": "Digital Signature Authentication RSA signature format.",
    "rsa-signature-hash-override": "Enable/disable IKEv2 RSA signature hash algorithm override.",
    "enforce-unique-id": "Enable/disable peer ID uniqueness check.",
    "cert-id-validation": "Enable/disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.",
    "fec-egress": "Enable/disable Forward Error Correction for egress IPsec traffic.",
    "fec-send-timeout": "Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000).",
    "fec-base": "Number of base Forward Error Correction packets (1 - 20).",
    "fec-codec": "Forward Error Correction encoding/decoding algorithm.",
    "fec-redundant": "Number of redundant Forward Error Correction packets (1 - 5 for reed-solomon, 1 for xor).",
    "fec-ingress": "Enable/disable Forward Error Correction for ingress IPsec traffic.",
    "fec-receive-timeout": "Timeout in milliseconds before dropping Forward Error Correction packets (1 - 1000).",
    "fec-health-check": "SD-WAN health check.",
    "fec-mapping-profile": "Forward Error Correction (FEC) mapping profile.",
    "network-overlay": "Enable/disable network overlays.",
    "network-id": "VPN gateway network ID.",
    "dev-id-notification": "Enable/disable device ID notification.",
    "dev-id": "Device ID carried by the device ID notification.",
    "loopback-asymroute": "Enable/disable asymmetric routing for IKE traffic on loopback interface.",
    "link-cost": "VPN tunnel underlay link cost.",
    "kms": "Key Management Services server.",
    "exchange-fgt-device-id": "Enable/disable device identifier exchange with peer FortiGate units for use of VPN monitor data by FortiManager.",
    "ipv6-auto-linklocal": "Enable/disable auto generation of IPv6 link-local address using last 8 bytes of mode-cfg assigned IPv6 address.",
    "ems-sn-check": "Enable/disable verification of EMS serial number.",
    "cert-trust-store": "CA certificate trust store.",
    "qkd": "Enable/disable use of Quantum Key Distribution (QKD) server.",
    "qkd-hybrid": "Enable/disable use of Quantum Key Distribution (QKD) hybrid keys.",
    "qkd-profile": "Quantum Key Distribution (QKD) server profile.",
    "transport": "Set IKE transport protocol.",
    "fortinet-esp": "Enable/disable Fortinet ESP encapsulation.",
    "auto-transport-threshold": "Timeout in seconds before falling back to next transport protocol.",
    "remote-gw-match": "Set type of IPv4 remote gateway address matching.",
    "remote-gw-subnet": "IPv4 address and subnet mask.",
    "remote-gw-start-ip": "First IPv4 address in the range.",
    "remote-gw-end-ip": "Last IPv4 address in the range.",
    "remote-gw-country": "IPv4 addresses associated to a specific country.",
    "remote-gw-ztna-tags": "IPv4 ZTNA posture tags.",
    "remote-gw6-match": "Set type of IPv6 remote gateway address matching.",
    "remote-gw6-subnet": "IPv6 address and prefix.",
    "remote-gw6-start-ip": "First IPv6 address in the range.",
    "remote-gw6-end-ip": "Last IPv6 address in the range.",
    "remote-gw6-country": "IPv6 addresses associated to a specific country.",
    "cert-peer-username-validation": "Enable/disable cross validation of peer username and the identity in the peer's certificate.",
    "cert-peer-username-strip": "Enable/disable domain stripping on certificate identity.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "interface": {"type": "string", "max_length": 35},
    "remotegw-ddns": {"type": "string", "max_length": 63},
    "keylife": {"type": "integer", "min": 120, "max": 172800},
    "peerid": {"type": "string", "max_length": 255},
    "usrgrp": {"type": "string", "max_length": 35},
    "peer": {"type": "string", "max_length": 35},
    "peergrp": {"type": "string", "max_length": 35},
    "ipv4-split-include": {"type": "string", "max_length": 79},
    "split-include-service": {"type": "string", "max_length": 79},
    "ipv4-name": {"type": "string", "max_length": 79},
    "ipv6-prefix": {"type": "integer", "min": 1, "max": 128},
    "ipv6-split-include": {"type": "string", "max_length": 79},
    "ipv6-name": {"type": "string", "max_length": 79},
    "ip-delay-interval": {"type": "integer", "min": 0, "max": 28800},
    "domain": {"type": "string", "max_length": 63},
    "ipv4-split-exclude": {"type": "string", "max_length": 79},
    "ipv6-split-exclude": {"type": "string", "max_length": 79},
    "keepalive": {"type": "integer", "min": 5, "max": 900},
    "distance": {"type": "integer", "min": 1, "max": 255},
    "priority": {"type": "integer", "min": 1, "max": 65535},
    "localid": {"type": "string", "max_length": 63},
    "negotiate-timeout": {"type": "integer", "min": 1, "max": 300},
    "dpd-retrycount": {"type": "integer", "min": 1, "max": 10},
    "eap-exclude-peergrp": {"type": "string", "max_length": 35},
    "ppk-identity": {"type": "string", "max_length": 35},
    "authusr": {"type": "string", "max_length": 64},
    "authusrgrp": {"type": "string", "max_length": 35},
    "idle-timeoutinterval": {"type": "integer", "min": 5, "max": 43200},
    "fragmentation-mtu": {"type": "integer", "min": 500, "max": 16000},
    "client-resume-interval": {"type": "integer", "min": 120, "max": 172800},
    "fec-send-timeout": {"type": "integer", "min": 1, "max": 1000},
    "fec-base": {"type": "integer", "min": 1, "max": 20},
    "fec-redundant": {"type": "integer", "min": 1, "max": 5},
    "fec-receive-timeout": {"type": "integer", "min": 1, "max": 1000},
    "fec-health-check": {"type": "string", "max_length": 35},
    "fec-mapping-profile": {"type": "string", "max_length": 35},
    "network-id": {"type": "integer", "min": 0, "max": 255},
    "dev-id": {"type": "string", "max_length": 63},
    "link-cost": {"type": "integer", "min": 0, "max": 255},
    "kms": {"type": "string", "max_length": 35},
    "qkd-profile": {"type": "string", "max_length": 35},
    "auto-transport-threshold": {"type": "integer", "min": 1, "max": 300},
    "remote-gw-country": {"type": "string", "max_length": 2},
    "remote-gw6-country": {"type": "string", "max_length": 2},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "certificate": {
        "name": {
            "type": "string",
            "help": "Certificate name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internal-domain-list": {
        "domain-name": {
            "type": "string",
            "help": "Domain name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "dns-suffix-search": {
        "dns-suffix": {
            "type": "string",
            "help": "DNS suffix.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "ipv4-exclude-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-ip": {
            "type": "ipv4-address",
            "help": "Start of IPv4 exclusive range.",
            "required": True,
            "default": "0.0.0.0",
        },
        "end-ip": {
            "type": "ipv4-address",
            "help": "End of IPv4 exclusive range.",
            "required": True,
            "default": "0.0.0.0",
        },
    },
    "ipv6-exclude-range": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "start-ip": {
            "type": "ipv6-address",
            "help": "Start of IPv6 exclusive range.",
            "required": True,
            "default": "::",
        },
        "end-ip": {
            "type": "ipv6-address",
            "help": "End of IPv6 exclusive range.",
            "required": True,
            "default": "::",
        },
    },
    "backup-gateway": {
        "address": {
            "type": "string",
            "help": "Address of backup gateway.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "remote-gw-ztna-tags": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "static",  # Remote VPN gateway has fixed IP address.
    "dynamic",  # Remote VPN gateway has dynamic IP address.
    "ddns",  # Remote VPN gateway has dynamic IP address and is a dynamic DNS client.
]
VALID_BODY_IKE_VERSION = [
    "1",  # Use IKEv1 protocol.
    "2",  # Use IKEv2 protocol.
]
VALID_BODY_AUTHMETHOD = [
    "psk",  # PSK authentication method.
    "signature",  # Signature authentication method.
]
VALID_BODY_AUTHMETHOD_REMOTE = [
    "psk",  # PSK authentication method.
    "signature",  # Signature authentication method.
]
VALID_BODY_MODE = [
    "aggressive",  # Aggressive mode.
    "main",  # Main mode.
]
VALID_BODY_PEERTYPE = [
    "any",  # Accept any peer ID.
    "one",  # Accept this peer ID.
    "dialup",  # Accept peer ID in dialup group.
    "peer",  # Accept this peer certificate.
    "peergrp",  # Accept this peer certificate group.
]
VALID_BODY_MODE_CFG = [
    "disable",  # Disable Configuration Method.
    "enable",  # Enable Configuration Method.
]
VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR = [
    "disable",  # Mode-cfg client to use wildcard selectors.
    "enable",  # Mode-cfg client to use custom selectors.
]
VALID_BODY_ASSIGN_IP = [
    "disable",  # Do not assign an IP address to the IPsec interface.
    "enable",  # Assign an IP address to the IPsec interface.
]
VALID_BODY_ASSIGN_IP_FROM = [
    "range",  # Assign IP address from locally defined range.
    "usrgrp",  # Assign IP address via user group.
    "dhcp",  # Assign IP address via DHCP.
    "name",  # Assign IP address from firewall address or group.
]
VALID_BODY_DNS_MODE = [
    "manual",  # Manually configure DNS servers.
    "auto",  # Use default DNS servers.
]
VALID_BODY_UNITY_SUPPORT = [
    "disable",  # Disable Cisco Unity Configuration Method Extensions.
    "enable",  # Enable Cisco Unity Configuration Method Extensions.
]
VALID_BODY_INCLUDE_LOCAL_LAN = [
    "disable",  # Disable local LAN access on Unity clients.
    "enable",  # Enable local LAN access on Unity clients.
]
VALID_BODY_SAVE_PASSWORD = [
    "disable",  # Disable saving XAuth username and password on VPN clients.
    "enable",  # Enable saving XAuth username and password on VPN clients.
]
VALID_BODY_CLIENT_AUTO_NEGOTIATE = [
    "disable",  # Disable allowing the VPN client to bring up the tunnel when there is no traffic.
    "enable",  # Enable allowing the VPN client to bring up the tunnel when there is no traffic.
]
VALID_BODY_CLIENT_KEEP_ALIVE = [
    "disable",  # Disable allowing the VPN client to keep the tunnel up when there is no traffic.
    "enable",  # Enable allowing the VPN client to keep the tunnel up when there is no traffic.
]
VALID_BODY_PROPOSAL = [
    "des-md5",  # des-md5
    "des-sha1",  # des-sha1
    "des-sha256",  # des-sha256
    "des-sha384",  # des-sha384
    "des-sha512",  # des-sha512
    "3des-md5",  # 3des-md5
    "3des-sha1",  # 3des-sha1
    "3des-sha256",  # 3des-sha256
    "3des-sha384",  # 3des-sha384
    "3des-sha512",  # 3des-sha512
    "aes128-md5",  # aes128-md5
    "aes128-sha1",  # aes128-sha1
    "aes128-sha256",  # aes128-sha256
    "aes128-sha384",  # aes128-sha384
    "aes128-sha512",  # aes128-sha512
    "aes128gcm-prfsha1",  # aes128gcm-prfsha1
    "aes128gcm-prfsha256",  # aes128gcm-prfsha256
    "aes128gcm-prfsha384",  # aes128gcm-prfsha384
    "aes128gcm-prfsha512",  # aes128gcm-prfsha512
    "aes192-md5",  # aes192-md5
    "aes192-sha1",  # aes192-sha1
    "aes192-sha256",  # aes192-sha256
    "aes192-sha384",  # aes192-sha384
    "aes192-sha512",  # aes192-sha512
    "aes256-md5",  # aes256-md5
    "aes256-sha1",  # aes256-sha1
    "aes256-sha256",  # aes256-sha256
    "aes256-sha384",  # aes256-sha384
    "aes256-sha512",  # aes256-sha512
    "aes256gcm-prfsha1",  # aes256gcm-prfsha1
    "aes256gcm-prfsha256",  # aes256gcm-prfsha256
    "aes256gcm-prfsha384",  # aes256gcm-prfsha384
    "aes256gcm-prfsha512",  # aes256gcm-prfsha512
    "chacha20poly1305-prfsha1",  # chacha20poly1305-prfsha1
    "chacha20poly1305-prfsha256",  # chacha20poly1305-prfsha256
    "chacha20poly1305-prfsha384",  # chacha20poly1305-prfsha384
    "chacha20poly1305-prfsha512",  # chacha20poly1305-prfsha512
    "aria128-md5",  # aria128-md5
    "aria128-sha1",  # aria128-sha1
    "aria128-sha256",  # aria128-sha256
    "aria128-sha384",  # aria128-sha384
    "aria128-sha512",  # aria128-sha512
    "aria192-md5",  # aria192-md5
    "aria192-sha1",  # aria192-sha1
    "aria192-sha256",  # aria192-sha256
    "aria192-sha384",  # aria192-sha384
    "aria192-sha512",  # aria192-sha512
    "aria256-md5",  # aria256-md5
    "aria256-sha1",  # aria256-sha1
    "aria256-sha256",  # aria256-sha256
    "aria256-sha384",  # aria256-sha384
    "aria256-sha512",  # aria256-sha512
    "seed-md5",  # seed-md5
    "seed-sha1",  # seed-sha1
    "seed-sha256",  # seed-sha256
    "seed-sha384",  # seed-sha384
    "seed-sha512",  # seed-sha512
]
VALID_BODY_ADD_ROUTE = [
    "disable",  # Do not add a route to destination of peer selector.
    "enable",  # Add route to destination of peer selector.
]
VALID_BODY_ADD_GW_ROUTE = [
    "enable",  # Automatically add a route to the remote gateway.
    "disable",  # Do not automatically add a route to the remote gateway.
]
VALID_BODY_LOCALID_TYPE = [
    "auto",  # Select ID type automatically.
    "fqdn",  # Use fully qualified domain name.
    "user-fqdn",  # Use user fully qualified domain name.
    "keyid",  # Use key-id string.
    "address",  # Use local IP address.
    "asn1dn",  # Use ASN.1 distinguished name.
]
VALID_BODY_AUTO_NEGOTIATE = [
    "enable",  # Enable automatic initiation of IKE SA negotiation.
    "disable",  # Disable automatic initiation of IKE SA negotiation.
]
VALID_BODY_FRAGMENTATION = [
    "enable",  # Enable intra-IKE fragmentation support on re-transmission.
    "disable",  # Disable intra-IKE fragmentation support.
]
VALID_BODY_DPD = [
    "disable",  # Disable Dead Peer Detection.
    "on-idle",  # Trigger Dead Peer Detection when IPsec is idle.
    "on-demand",  # Trigger Dead Peer Detection when IPsec traffic is sent but no reply is received from the peer.
]
VALID_BODY_NPU_OFFLOAD = [
    "enable",  # Enable NPU offloading.
    "disable",  # Disable NPU offloading.
]
VALID_BODY_SEND_CERT_CHAIN = [
    "enable",  # Enable sending certificate chain.
    "disable",  # Disable sending certificate chain.
]
VALID_BODY_DHGRP = [
    "1",  # DH Group 1.
    "2",  # DH Group 2.
    "5",  # DH Group 5.
    "14",  # DH Group 14.
    "15",  # DH Group 15.
    "16",  # DH Group 16.
    "17",  # DH Group 17.
    "18",  # DH Group 18.
    "19",  # DH Group 19.
    "20",  # DH Group 20.
    "21",  # DH Group 21.
    "27",  # DH Group 27.
    "28",  # DH Group 28.
    "29",  # DH Group 29.
    "30",  # DH Group 30.
    "31",  # DH Group 31.
    "32",  # DH Group 32.
]
VALID_BODY_ADDKE1 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE2 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE3 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE4 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE5 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE6 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_ADDKE7 = [
    "0",  # NONE.
    "35",  # ML-KEM-512.
    "36",  # ML-KEM-768.
    "37",  # ML-KEM-1024.
    "1080",  # KYBER512.
    "1081",  # KYBER768.
    "1082",  # KYBER1024.
    "1083",  # FRODO L1.
    "1084",  # FRODO L3.
    "1085",  # FRODO L5.
    "1089",  # BIKE L1.
    "1090",  # BIKE L3.
    "1091",  # BIKE L5.
    "1092",  # HQC128.
    "1093",  # HQC192.
    "1094",  # HQC256.
]
VALID_BODY_SUITE_B = [
    "disable",  # Do not use UI suite.
    "suite-b-gcm-128",  # Use Suite-B-GCM-128.
    "suite-b-gcm-256",  # Use Suite-B-GCM-256.
]
VALID_BODY_EAP = [
    "enable",  # Enable IKEv2 EAP authentication.
    "disable",  # Disable IKEv2 EAP authentication.
]
VALID_BODY_EAP_IDENTITY = [
    "use-id-payload",  # Use IKEv2 IDi payload to resolve peer identity.
    "send-request",  # Use EAP identity request to resolve peer identity.
]
VALID_BODY_EAP_CERT_AUTH = [
    "enable",  # Enable peer certificate authentication in addition to EAP if peer is a FortiClient endpoint.
    "disable",  # Disable peer certificate authentication in addition to EAP if peer is a FortiClient endpoint.
]
VALID_BODY_ACCT_VERIFY = [
    "enable",  # Enable verification of RADIUS accounting record.
    "disable",  # Disable verification of RADIUS accounting record.
]
VALID_BODY_PPK = [
    "disable",  # Disable use of IKEv2 Postquantum Preshared Key (PPK).
    "allow",  # Allow, but do not require, use of IKEv2 Postquantum Preshared Key (PPK).
    "require",  # Require use of IKEv2 Postquantum Preshared Key (PPK).
]
VALID_BODY_WIZARD_TYPE = [
    "custom",  # Custom VPN configuration.
    "dialup-forticlient",  # Dial Up - FortiClient Windows, Mac and Android.
    "dialup-ios",  # Dial Up - iPhone / iPad Native IPsec Client.
    "dialup-android",  # Dial Up - Android Native IPsec Client.
    "dialup-windows",  # Dial Up - Windows Native IPsec Client.
    "dialup-cisco",  # Dial Up - Cisco IPsec Client.
    "static-fortigate",  # Site to Site - FortiGate.
    "dialup-fortigate",  # Dial Up - FortiGate.
    "static-cisco",  # Site to Site - Cisco.
    "dialup-cisco-fw",  # Dialup Up - Cisco Firewall.
    "simplified-static-fortigate",  # Site to Site - FortiGate (SD-WAN).
    "hub-fortigate-auto-discovery",  # Hub role in a Hub-and-Spoke auto-discovery VPN.
    "spoke-fortigate-auto-discovery",  # Spoke role in a Hub-and-Spoke auto-discovery VPN.
    "fabric-overlay-orchestrator",  # Fabric Overlay Orchestrator.
]
VALID_BODY_XAUTHTYPE = [
    "disable",  # Disable.
    "client",  # Enable as client.
    "pap",  # Enable as server PAP.
    "chap",  # Enable as server CHAP.
    "auto",  # Enable as server auto.
]
VALID_BODY_REAUTH = [
    "disable",  # Disable IKE SA re-authentication.
    "enable",  # Enable IKE SA re-authentication.
]
VALID_BODY_GROUP_AUTHENTICATION = [
    "enable",  # Enable IKEv2 IDi group authentication.
    "disable",  # Disable IKEv2 IDi group authentication.
]
VALID_BODY_MESH_SELECTOR_TYPE = [
    "disable",  # Disable.
    "subnet",  # Enable addition of matching subnet selector.
    "host",  # Enable addition of host to host selector.
]
VALID_BODY_IDLE_TIMEOUT = [
    "enable",  # Enable IPsec tunnel idle timeout.
    "disable",  # Disable IPsec tunnel idle timeout.
]
VALID_BODY_SHARED_IDLE_TIMEOUT = [
    "enable",  # Enable IPsec tunnel shared idle timeout. The location-id attribute must be configured on both spokes. Shared idle timeout is supported only on IKEv2 since remote-location is availabe only for IKEv2.
    "disable",  # Disable IPsec tunnel shared idle timeout.
]
VALID_BODY_HA_SYNC_ESP_SEQNO = [
    "enable",  # Enable HA syncing of ESP sequence numbers.
    "disable",  # Disable HA syncing of ESP sequence numbers.
]
VALID_BODY_FGSP_SYNC = [
    "enable",  # Enable IPsec syncing of tunnels to other cluster members.
    "disable",  # Disable IPsec syncing of tunnels to other cluster members.
]
VALID_BODY_INBOUND_DSCP_COPY = [
    "enable",  # Enable copy the dscp in the ESP header to the inner IP Header.
    "disable",  # Disable copy the dscp in the ESP header to the inner IP Header.
]
VALID_BODY_NATTRAVERSAL = [
    "enable",  # Enable IPsec NAT traversal.
    "disable",  # Disable IPsec NAT traversal.
    "forced",  # Force IPsec NAT traversal on.
]
VALID_BODY_ESN = [
    "require",  # Require extended sequence number.
    "allow",  # Allow extended sequence number.
    "disable",  # Disable extended sequence number.
]
VALID_BODY_CHILDLESS_IKE = [
    "enable",  # Enable childless IKEv2 initiation (RFC 6023).
    "disable",  # Disable childless IKEv2 initiation (RFC 6023).
]
VALID_BODY_AZURE_AD_AUTOCONNECT = [
    "enable",  # Enable Azure AD Auto-Connect for FortiClient.
    "disable",  # Disable Azure AD Auto-Connect for FortiClient.
]
VALID_BODY_CLIENT_RESUME = [
    "enable",  # Enable client session resumption.
    "disable",  # Disable client session resumption.
]
VALID_BODY_REKEY = [
    "enable",  # Enable phase1 rekey.
    "disable",  # Disable phase1 rekey.
]
VALID_BODY_DIGITAL_SIGNATURE_AUTH = [
    "enable",  # Enable IKEv2 Digital Signature Authentication (RFC 7427).
    "disable",  # Disable IKEv2 Digital Signature Authentication (RFC 7427).
]
VALID_BODY_SIGNATURE_HASH_ALG = [
    "sha1",  # SHA1.
    "sha2-256",  # SHA2-256.
    "sha2-384",  # SHA2-384.
    "sha2-512",  # SHA2-512.
]
VALID_BODY_RSA_SIGNATURE_FORMAT = [
    "pkcs1",  # RSASSA PKCS#1 v1.5.
    "pss",  # RSASSA Probabilistic Signature Scheme (PSS).
]
VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE = [
    "enable",  # Enable IKEv2 RSA signature hash algorithm override.
    "disable",  # Disable IKEv2 RSA signature hash algorithm override.
]
VALID_BODY_ENFORCE_UNIQUE_ID = [
    "disable",  # Disable peer ID uniqueness enforcement.
    "keep-new",  # Enforce peer ID uniqueness, keep new connection if collision found.
    "keep-old",  # Enforce peer ID uniqueness, keep old connection if collision found.
]
VALID_BODY_CERT_ID_VALIDATION = [
    "enable",  # Enable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.
    "disable",  # Disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.
]
VALID_BODY_FEC_EGRESS = [
    "enable",  # Enable Forward Error Correction for egress IPsec traffic.
    "disable",  # Disable Forward Error Correction for egress IPsec traffic.
]
VALID_BODY_FEC_CODEC = [
    "rs",  # Reed-Solomon FEC algorithm.
    "xor",  # XOR FEC algorithm.
]
VALID_BODY_FEC_INGRESS = [
    "enable",  # Enable Forward Error Correction for ingress IPsec traffic.
    "disable",  # Disable Forward Error Correction for ingress IPsec traffic.
]
VALID_BODY_NETWORK_OVERLAY = [
    "disable",  # Disable network overlays.
    "enable",  # Enable network overlays.
]
VALID_BODY_DEV_ID_NOTIFICATION = [
    "disable",  # Disable device ID notification.
    "enable",  # Enable device ID notification.
]
VALID_BODY_LOOPBACK_ASYMROUTE = [
    "enable",  # Allow ingress/egress IKE traffic to be routed over different interfaces.
    "disable",  # Ingress/egress IKE traffic must be routed over the same interface.
]
VALID_BODY_EXCHANGE_FGT_DEVICE_ID = [
    "enable",  # Enable exchange of FortiGate device identifier.
    "disable",  # Disable exchange of FortiGate device identifier.
]
VALID_BODY_IPV6_AUTO_LINKLOCAL = [
    "enable",  # Enable mode-cfg auto configuration of IPv6 link-local address.
    "disable",  # Disable mode-cfg auto configuration of IPv6 link-local address.
]
VALID_BODY_EMS_SN_CHECK = [
    "enable",  # Enable EMS serial number verification.
    "disable",  # Disable EMS serial number verification.
]
VALID_BODY_CERT_TRUST_STORE = [
    "local",  # Use local CA certificate.
    "ems",  # Use EMS CA certificate.
]
VALID_BODY_QKD = [
    "disable",  # Disable use of a Quantum Key Distribution (QKD) server.
    "allow",  # Allow, but do not require, use of a Quantum Key Distribution (QKD) server.
    "require",  # Require use of a Quantum Key Distribution (QKD) server.
]
VALID_BODY_QKD_HYBRID = [
    "disable",  # Disable use of Quantum Key Distribution (QKD) hybrid keys.
    "allow",  # Allow, but do not require, use of Quantum Key Distribution (QKD) hybrid keys.
    "require",  # Require use of Quantum Key Distribution (QKD) hybrid keys.
]
VALID_BODY_TRANSPORT = [
    "udp",  # Use UDP transport for IKE.
    "auto",  # Use AUTO transport for IKE.
    "tcp",  # Use TCP transport for IKE.
]
VALID_BODY_FORTINET_ESP = [
    "enable",  # Enable Fortinet ESP encapsulation.
    "disable",  # Disable Fortinet ESP encapsulation.
]
VALID_BODY_REMOTE_GW_MATCH = [
    "any",  # Match any IPv4 gateway address.
    "ipmask",  # Match IPv4 gateway address and mask.
    "iprange",  # Match IPv4 gateway address range.
    "geography",  # Match IPv4 gateway address from a specified country.
    "ztna",  # Match IPv4 gateway address against ZTNA posture tags.
]
VALID_BODY_REMOTE_GW6_MATCH = [
    "any",  # Match any IPv6 gateway address.
    "ipprefix",  # Match IPv6 gateway address and prefix.
    "iprange",  # Match IPv6 gateway address range.
    "geography",  # Match IPv6 gateway address from a specified country.
]
VALID_BODY_CERT_PEER_USERNAME_VALIDATION = [
    "none",  # Disable cross validation of peer username and the identity in the peer's certificate.
    "othername",  # Validate principal name in SAN othername.
    "rfc822name",  # Validate RFC822 email address in SAN.
    "cn",  # Validate CN in subject.
]
VALID_BODY_CERT_PEER_USERNAME_STRIP = [
    "disable",  # Disable domain stripping on certificate identity.
    "enable",  # Enable domain stripping on certificate identity.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vpn_ipsec_phase1_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for vpn/ipsec/phase1.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_vpn_ipsec_phase1_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_vpn_ipsec_phase1_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_vpn_ipsec_phase1_get(
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
    Validate required fields for vpn/ipsec/phase1.

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


def validate_vpn_ipsec_phase1_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new vpn/ipsec/phase1 object.

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
        ...     "interface": True,  # Local physical, aggregate, or VLAN outgoing interf
        ...     "remotegw-ddns": True,  # Domain name of remote gateway. For example, name.d
        ... }
        >>> is_valid, error = validate_vpn_ipsec_phase1_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "interface": True,
        ...     "type": "{'name': 'static', 'help': 'Remote VPN gateway has fixed IP address.', 'label': 'Static', 'description': 'Remote VPN gateway has fixed IP address'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_vpn_ipsec_phase1_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["type"] = "invalid-value"
        >>> is_valid, error = validate_vpn_ipsec_phase1_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_vpn_ipsec_phase1_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "ike-version" in payload:
        value = payload["ike-version"]
        if value not in VALID_BODY_IKE_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ike-version", "")
            error_msg = f"Invalid value for 'ike-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IKE_VERSION)}"
            error_msg += f"\n  → Example: ike-version='{{ VALID_BODY_IKE_VERSION[0] }}'"
            return (False, error_msg)
    if "authmethod" in payload:
        value = payload["authmethod"]
        if value not in VALID_BODY_AUTHMETHOD:
            desc = FIELD_DESCRIPTIONS.get("authmethod", "")
            error_msg = f"Invalid value for 'authmethod': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHMETHOD)}"
            error_msg += f"\n  → Example: authmethod='{{ VALID_BODY_AUTHMETHOD[0] }}'"
            return (False, error_msg)
    if "authmethod-remote" in payload:
        value = payload["authmethod-remote"]
        if value not in VALID_BODY_AUTHMETHOD_REMOTE:
            desc = FIELD_DESCRIPTIONS.get("authmethod-remote", "")
            error_msg = f"Invalid value for 'authmethod-remote': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHMETHOD_REMOTE)}"
            error_msg += f"\n  → Example: authmethod-remote='{{ VALID_BODY_AUTHMETHOD_REMOTE[0] }}'"
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
    if "peertype" in payload:
        value = payload["peertype"]
        if value not in VALID_BODY_PEERTYPE:
            desc = FIELD_DESCRIPTIONS.get("peertype", "")
            error_msg = f"Invalid value for 'peertype': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PEERTYPE)}"
            error_msg += f"\n  → Example: peertype='{{ VALID_BODY_PEERTYPE[0] }}'"
            return (False, error_msg)
    if "mode-cfg" in payload:
        value = payload["mode-cfg"]
        if value not in VALID_BODY_MODE_CFG:
            desc = FIELD_DESCRIPTIONS.get("mode-cfg", "")
            error_msg = f"Invalid value for 'mode-cfg': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE_CFG)}"
            error_msg += f"\n  → Example: mode-cfg='{{ VALID_BODY_MODE_CFG[0] }}'"
            return (False, error_msg)
    if "mode-cfg-allow-client-selector" in payload:
        value = payload["mode-cfg-allow-client-selector"]
        if value not in VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR:
            desc = FIELD_DESCRIPTIONS.get("mode-cfg-allow-client-selector", "")
            error_msg = f"Invalid value for 'mode-cfg-allow-client-selector': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR)}"
            error_msg += f"\n  → Example: mode-cfg-allow-client-selector='{{ VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR[0] }}'"
            return (False, error_msg)
    if "assign-ip" in payload:
        value = payload["assign-ip"]
        if value not in VALID_BODY_ASSIGN_IP:
            desc = FIELD_DESCRIPTIONS.get("assign-ip", "")
            error_msg = f"Invalid value for 'assign-ip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSIGN_IP)}"
            error_msg += f"\n  → Example: assign-ip='{{ VALID_BODY_ASSIGN_IP[0] }}'"
            return (False, error_msg)
    if "assign-ip-from" in payload:
        value = payload["assign-ip-from"]
        if value not in VALID_BODY_ASSIGN_IP_FROM:
            desc = FIELD_DESCRIPTIONS.get("assign-ip-from", "")
            error_msg = f"Invalid value for 'assign-ip-from': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSIGN_IP_FROM)}"
            error_msg += f"\n  → Example: assign-ip-from='{{ VALID_BODY_ASSIGN_IP_FROM[0] }}'"
            return (False, error_msg)
    if "dns-mode" in payload:
        value = payload["dns-mode"]
        if value not in VALID_BODY_DNS_MODE:
            desc = FIELD_DESCRIPTIONS.get("dns-mode", "")
            error_msg = f"Invalid value for 'dns-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DNS_MODE)}"
            error_msg += f"\n  → Example: dns-mode='{{ VALID_BODY_DNS_MODE[0] }}'"
            return (False, error_msg)
    if "unity-support" in payload:
        value = payload["unity-support"]
        if value not in VALID_BODY_UNITY_SUPPORT:
            desc = FIELD_DESCRIPTIONS.get("unity-support", "")
            error_msg = f"Invalid value for 'unity-support': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNITY_SUPPORT)}"
            error_msg += f"\n  → Example: unity-support='{{ VALID_BODY_UNITY_SUPPORT[0] }}'"
            return (False, error_msg)
    if "include-local-lan" in payload:
        value = payload["include-local-lan"]
        if value not in VALID_BODY_INCLUDE_LOCAL_LAN:
            desc = FIELD_DESCRIPTIONS.get("include-local-lan", "")
            error_msg = f"Invalid value for 'include-local-lan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INCLUDE_LOCAL_LAN)}"
            error_msg += f"\n  → Example: include-local-lan='{{ VALID_BODY_INCLUDE_LOCAL_LAN[0] }}'"
            return (False, error_msg)
    if "save-password" in payload:
        value = payload["save-password"]
        if value not in VALID_BODY_SAVE_PASSWORD:
            desc = FIELD_DESCRIPTIONS.get("save-password", "")
            error_msg = f"Invalid value for 'save-password': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAVE_PASSWORD)}"
            error_msg += f"\n  → Example: save-password='{{ VALID_BODY_SAVE_PASSWORD[0] }}'"
            return (False, error_msg)
    if "client-auto-negotiate" in payload:
        value = payload["client-auto-negotiate"]
        if value not in VALID_BODY_CLIENT_AUTO_NEGOTIATE:
            desc = FIELD_DESCRIPTIONS.get("client-auto-negotiate", "")
            error_msg = f"Invalid value for 'client-auto-negotiate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_AUTO_NEGOTIATE)}"
            error_msg += f"\n  → Example: client-auto-negotiate='{{ VALID_BODY_CLIENT_AUTO_NEGOTIATE[0] }}'"
            return (False, error_msg)
    if "client-keep-alive" in payload:
        value = payload["client-keep-alive"]
        if value not in VALID_BODY_CLIENT_KEEP_ALIVE:
            desc = FIELD_DESCRIPTIONS.get("client-keep-alive", "")
            error_msg = f"Invalid value for 'client-keep-alive': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_KEEP_ALIVE)}"
            error_msg += f"\n  → Example: client-keep-alive='{{ VALID_BODY_CLIENT_KEEP_ALIVE[0] }}'"
            return (False, error_msg)
    if "proposal" in payload:
        value = payload["proposal"]
        if value not in VALID_BODY_PROPOSAL:
            desc = FIELD_DESCRIPTIONS.get("proposal", "")
            error_msg = f"Invalid value for 'proposal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROPOSAL)}"
            error_msg += f"\n  → Example: proposal='{{ VALID_BODY_PROPOSAL[0] }}'"
            return (False, error_msg)
    if "add-route" in payload:
        value = payload["add-route"]
        if value not in VALID_BODY_ADD_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("add-route", "")
            error_msg = f"Invalid value for 'add-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_ROUTE)}"
            error_msg += f"\n  → Example: add-route='{{ VALID_BODY_ADD_ROUTE[0] }}'"
            return (False, error_msg)
    if "add-gw-route" in payload:
        value = payload["add-gw-route"]
        if value not in VALID_BODY_ADD_GW_ROUTE:
            desc = FIELD_DESCRIPTIONS.get("add-gw-route", "")
            error_msg = f"Invalid value for 'add-gw-route': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADD_GW_ROUTE)}"
            error_msg += f"\n  → Example: add-gw-route='{{ VALID_BODY_ADD_GW_ROUTE[0] }}'"
            return (False, error_msg)
    if "localid-type" in payload:
        value = payload["localid-type"]
        if value not in VALID_BODY_LOCALID_TYPE:
            desc = FIELD_DESCRIPTIONS.get("localid-type", "")
            error_msg = f"Invalid value for 'localid-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCALID_TYPE)}"
            error_msg += f"\n  → Example: localid-type='{{ VALID_BODY_LOCALID_TYPE[0] }}'"
            return (False, error_msg)
    if "auto-negotiate" in payload:
        value = payload["auto-negotiate"]
        if value not in VALID_BODY_AUTO_NEGOTIATE:
            desc = FIELD_DESCRIPTIONS.get("auto-negotiate", "")
            error_msg = f"Invalid value for 'auto-negotiate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTO_NEGOTIATE)}"
            error_msg += f"\n  → Example: auto-negotiate='{{ VALID_BODY_AUTO_NEGOTIATE[0] }}'"
            return (False, error_msg)
    if "fragmentation" in payload:
        value = payload["fragmentation"]
        if value not in VALID_BODY_FRAGMENTATION:
            desc = FIELD_DESCRIPTIONS.get("fragmentation", "")
            error_msg = f"Invalid value for 'fragmentation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FRAGMENTATION)}"
            error_msg += f"\n  → Example: fragmentation='{{ VALID_BODY_FRAGMENTATION[0] }}'"
            return (False, error_msg)
    if "dpd" in payload:
        value = payload["dpd"]
        if value not in VALID_BODY_DPD:
            desc = FIELD_DESCRIPTIONS.get("dpd", "")
            error_msg = f"Invalid value for 'dpd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DPD)}"
            error_msg += f"\n  → Example: dpd='{{ VALID_BODY_DPD[0] }}'"
            return (False, error_msg)
    if "npu-offload" in payload:
        value = payload["npu-offload"]
        if value not in VALID_BODY_NPU_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("npu-offload", "")
            error_msg = f"Invalid value for 'npu-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NPU_OFFLOAD)}"
            error_msg += f"\n  → Example: npu-offload='{{ VALID_BODY_NPU_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "send-cert-chain" in payload:
        value = payload["send-cert-chain"]
        if value not in VALID_BODY_SEND_CERT_CHAIN:
            desc = FIELD_DESCRIPTIONS.get("send-cert-chain", "")
            error_msg = f"Invalid value for 'send-cert-chain': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEND_CERT_CHAIN)}"
            error_msg += f"\n  → Example: send-cert-chain='{{ VALID_BODY_SEND_CERT_CHAIN[0] }}'"
            return (False, error_msg)
    if "dhgrp" in payload:
        value = payload["dhgrp"]
        if value not in VALID_BODY_DHGRP:
            desc = FIELD_DESCRIPTIONS.get("dhgrp", "")
            error_msg = f"Invalid value for 'dhgrp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHGRP)}"
            error_msg += f"\n  → Example: dhgrp='{{ VALID_BODY_DHGRP[0] }}'"
            return (False, error_msg)
    if "addke1" in payload:
        value = payload["addke1"]
        if value not in VALID_BODY_ADDKE1:
            desc = FIELD_DESCRIPTIONS.get("addke1", "")
            error_msg = f"Invalid value for 'addke1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE1)}"
            error_msg += f"\n  → Example: addke1='{{ VALID_BODY_ADDKE1[0] }}'"
            return (False, error_msg)
    if "addke2" in payload:
        value = payload["addke2"]
        if value not in VALID_BODY_ADDKE2:
            desc = FIELD_DESCRIPTIONS.get("addke2", "")
            error_msg = f"Invalid value for 'addke2': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE2)}"
            error_msg += f"\n  → Example: addke2='{{ VALID_BODY_ADDKE2[0] }}'"
            return (False, error_msg)
    if "addke3" in payload:
        value = payload["addke3"]
        if value not in VALID_BODY_ADDKE3:
            desc = FIELD_DESCRIPTIONS.get("addke3", "")
            error_msg = f"Invalid value for 'addke3': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE3)}"
            error_msg += f"\n  → Example: addke3='{{ VALID_BODY_ADDKE3[0] }}'"
            return (False, error_msg)
    if "addke4" in payload:
        value = payload["addke4"]
        if value not in VALID_BODY_ADDKE4:
            desc = FIELD_DESCRIPTIONS.get("addke4", "")
            error_msg = f"Invalid value for 'addke4': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE4)}"
            error_msg += f"\n  → Example: addke4='{{ VALID_BODY_ADDKE4[0] }}'"
            return (False, error_msg)
    if "addke5" in payload:
        value = payload["addke5"]
        if value not in VALID_BODY_ADDKE5:
            desc = FIELD_DESCRIPTIONS.get("addke5", "")
            error_msg = f"Invalid value for 'addke5': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE5)}"
            error_msg += f"\n  → Example: addke5='{{ VALID_BODY_ADDKE5[0] }}'"
            return (False, error_msg)
    if "addke6" in payload:
        value = payload["addke6"]
        if value not in VALID_BODY_ADDKE6:
            desc = FIELD_DESCRIPTIONS.get("addke6", "")
            error_msg = f"Invalid value for 'addke6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE6)}"
            error_msg += f"\n  → Example: addke6='{{ VALID_BODY_ADDKE6[0] }}'"
            return (False, error_msg)
    if "addke7" in payload:
        value = payload["addke7"]
        if value not in VALID_BODY_ADDKE7:
            desc = FIELD_DESCRIPTIONS.get("addke7", "")
            error_msg = f"Invalid value for 'addke7': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDKE7)}"
            error_msg += f"\n  → Example: addke7='{{ VALID_BODY_ADDKE7[0] }}'"
            return (False, error_msg)
    if "suite-b" in payload:
        value = payload["suite-b"]
        if value not in VALID_BODY_SUITE_B:
            desc = FIELD_DESCRIPTIONS.get("suite-b", "")
            error_msg = f"Invalid value for 'suite-b': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SUITE_B)}"
            error_msg += f"\n  → Example: suite-b='{{ VALID_BODY_SUITE_B[0] }}'"
            return (False, error_msg)
    if "eap" in payload:
        value = payload["eap"]
        if value not in VALID_BODY_EAP:
            desc = FIELD_DESCRIPTIONS.get("eap", "")
            error_msg = f"Invalid value for 'eap': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP)}"
            error_msg += f"\n  → Example: eap='{{ VALID_BODY_EAP[0] }}'"
            return (False, error_msg)
    if "eap-identity" in payload:
        value = payload["eap-identity"]
        if value not in VALID_BODY_EAP_IDENTITY:
            desc = FIELD_DESCRIPTIONS.get("eap-identity", "")
            error_msg = f"Invalid value for 'eap-identity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_IDENTITY)}"
            error_msg += f"\n  → Example: eap-identity='{{ VALID_BODY_EAP_IDENTITY[0] }}'"
            return (False, error_msg)
    if "eap-cert-auth" in payload:
        value = payload["eap-cert-auth"]
        if value not in VALID_BODY_EAP_CERT_AUTH:
            desc = FIELD_DESCRIPTIONS.get("eap-cert-auth", "")
            error_msg = f"Invalid value for 'eap-cert-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_CERT_AUTH)}"
            error_msg += f"\n  → Example: eap-cert-auth='{{ VALID_BODY_EAP_CERT_AUTH[0] }}'"
            return (False, error_msg)
    if "acct-verify" in payload:
        value = payload["acct-verify"]
        if value not in VALID_BODY_ACCT_VERIFY:
            desc = FIELD_DESCRIPTIONS.get("acct-verify", "")
            error_msg = f"Invalid value for 'acct-verify': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ACCT_VERIFY)}"
            error_msg += f"\n  → Example: acct-verify='{{ VALID_BODY_ACCT_VERIFY[0] }}'"
            return (False, error_msg)
    if "ppk" in payload:
        value = payload["ppk"]
        if value not in VALID_BODY_PPK:
            desc = FIELD_DESCRIPTIONS.get("ppk", "")
            error_msg = f"Invalid value for 'ppk': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PPK)}"
            error_msg += f"\n  → Example: ppk='{{ VALID_BODY_PPK[0] }}'"
            return (False, error_msg)
    if "wizard-type" in payload:
        value = payload["wizard-type"]
        if value not in VALID_BODY_WIZARD_TYPE:
            desc = FIELD_DESCRIPTIONS.get("wizard-type", "")
            error_msg = f"Invalid value for 'wizard-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIZARD_TYPE)}"
            error_msg += f"\n  → Example: wizard-type='{{ VALID_BODY_WIZARD_TYPE[0] }}'"
            return (False, error_msg)
    if "xauthtype" in payload:
        value = payload["xauthtype"]
        if value not in VALID_BODY_XAUTHTYPE:
            desc = FIELD_DESCRIPTIONS.get("xauthtype", "")
            error_msg = f"Invalid value for 'xauthtype': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_XAUTHTYPE)}"
            error_msg += f"\n  → Example: xauthtype='{{ VALID_BODY_XAUTHTYPE[0] }}'"
            return (False, error_msg)
    if "reauth" in payload:
        value = payload["reauth"]
        if value not in VALID_BODY_REAUTH:
            desc = FIELD_DESCRIPTIONS.get("reauth", "")
            error_msg = f"Invalid value for 'reauth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REAUTH)}"
            error_msg += f"\n  → Example: reauth='{{ VALID_BODY_REAUTH[0] }}'"
            return (False, error_msg)
    if "group-authentication" in payload:
        value = payload["group-authentication"]
        if value not in VALID_BODY_GROUP_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("group-authentication", "")
            error_msg = f"Invalid value for 'group-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_AUTHENTICATION)}"
            error_msg += f"\n  → Example: group-authentication='{{ VALID_BODY_GROUP_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "mesh-selector-type" in payload:
        value = payload["mesh-selector-type"]
        if value not in VALID_BODY_MESH_SELECTOR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("mesh-selector-type", "")
            error_msg = f"Invalid value for 'mesh-selector-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MESH_SELECTOR_TYPE)}"
            error_msg += f"\n  → Example: mesh-selector-type='{{ VALID_BODY_MESH_SELECTOR_TYPE[0] }}'"
            return (False, error_msg)
    if "idle-timeout" in payload:
        value = payload["idle-timeout"]
        if value not in VALID_BODY_IDLE_TIMEOUT:
            desc = FIELD_DESCRIPTIONS.get("idle-timeout", "")
            error_msg = f"Invalid value for 'idle-timeout': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IDLE_TIMEOUT)}"
            error_msg += f"\n  → Example: idle-timeout='{{ VALID_BODY_IDLE_TIMEOUT[0] }}'"
            return (False, error_msg)
    if "shared-idle-timeout" in payload:
        value = payload["shared-idle-timeout"]
        if value not in VALID_BODY_SHARED_IDLE_TIMEOUT:
            desc = FIELD_DESCRIPTIONS.get("shared-idle-timeout", "")
            error_msg = f"Invalid value for 'shared-idle-timeout': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SHARED_IDLE_TIMEOUT)}"
            error_msg += f"\n  → Example: shared-idle-timeout='{{ VALID_BODY_SHARED_IDLE_TIMEOUT[0] }}'"
            return (False, error_msg)
    if "ha-sync-esp-seqno" in payload:
        value = payload["ha-sync-esp-seqno"]
        if value not in VALID_BODY_HA_SYNC_ESP_SEQNO:
            desc = FIELD_DESCRIPTIONS.get("ha-sync-esp-seqno", "")
            error_msg = f"Invalid value for 'ha-sync-esp-seqno': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_SYNC_ESP_SEQNO)}"
            error_msg += f"\n  → Example: ha-sync-esp-seqno='{{ VALID_BODY_HA_SYNC_ESP_SEQNO[0] }}'"
            return (False, error_msg)
    if "fgsp-sync" in payload:
        value = payload["fgsp-sync"]
        if value not in VALID_BODY_FGSP_SYNC:
            desc = FIELD_DESCRIPTIONS.get("fgsp-sync", "")
            error_msg = f"Invalid value for 'fgsp-sync': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FGSP_SYNC)}"
            error_msg += f"\n  → Example: fgsp-sync='{{ VALID_BODY_FGSP_SYNC[0] }}'"
            return (False, error_msg)
    if "inbound-dscp-copy" in payload:
        value = payload["inbound-dscp-copy"]
        if value not in VALID_BODY_INBOUND_DSCP_COPY:
            desc = FIELD_DESCRIPTIONS.get("inbound-dscp-copy", "")
            error_msg = f"Invalid value for 'inbound-dscp-copy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INBOUND_DSCP_COPY)}"
            error_msg += f"\n  → Example: inbound-dscp-copy='{{ VALID_BODY_INBOUND_DSCP_COPY[0] }}'"
            return (False, error_msg)
    if "nattraversal" in payload:
        value = payload["nattraversal"]
        if value not in VALID_BODY_NATTRAVERSAL:
            desc = FIELD_DESCRIPTIONS.get("nattraversal", "")
            error_msg = f"Invalid value for 'nattraversal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NATTRAVERSAL)}"
            error_msg += f"\n  → Example: nattraversal='{{ VALID_BODY_NATTRAVERSAL[0] }}'"
            return (False, error_msg)
    if "esn" in payload:
        value = payload["esn"]
        if value not in VALID_BODY_ESN:
            desc = FIELD_DESCRIPTIONS.get("esn", "")
            error_msg = f"Invalid value for 'esn': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ESN)}"
            error_msg += f"\n  → Example: esn='{{ VALID_BODY_ESN[0] }}'"
            return (False, error_msg)
    if "childless-ike" in payload:
        value = payload["childless-ike"]
        if value not in VALID_BODY_CHILDLESS_IKE:
            desc = FIELD_DESCRIPTIONS.get("childless-ike", "")
            error_msg = f"Invalid value for 'childless-ike': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHILDLESS_IKE)}"
            error_msg += f"\n  → Example: childless-ike='{{ VALID_BODY_CHILDLESS_IKE[0] }}'"
            return (False, error_msg)
    if "azure-ad-autoconnect" in payload:
        value = payload["azure-ad-autoconnect"]
        if value not in VALID_BODY_AZURE_AD_AUTOCONNECT:
            desc = FIELD_DESCRIPTIONS.get("azure-ad-autoconnect", "")
            error_msg = f"Invalid value for 'azure-ad-autoconnect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AZURE_AD_AUTOCONNECT)}"
            error_msg += f"\n  → Example: azure-ad-autoconnect='{{ VALID_BODY_AZURE_AD_AUTOCONNECT[0] }}'"
            return (False, error_msg)
    if "client-resume" in payload:
        value = payload["client-resume"]
        if value not in VALID_BODY_CLIENT_RESUME:
            desc = FIELD_DESCRIPTIONS.get("client-resume", "")
            error_msg = f"Invalid value for 'client-resume': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_RESUME)}"
            error_msg += f"\n  → Example: client-resume='{{ VALID_BODY_CLIENT_RESUME[0] }}'"
            return (False, error_msg)
    if "rekey" in payload:
        value = payload["rekey"]
        if value not in VALID_BODY_REKEY:
            desc = FIELD_DESCRIPTIONS.get("rekey", "")
            error_msg = f"Invalid value for 'rekey': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REKEY)}"
            error_msg += f"\n  → Example: rekey='{{ VALID_BODY_REKEY[0] }}'"
            return (False, error_msg)
    if "digital-signature-auth" in payload:
        value = payload["digital-signature-auth"]
        if value not in VALID_BODY_DIGITAL_SIGNATURE_AUTH:
            desc = FIELD_DESCRIPTIONS.get("digital-signature-auth", "")
            error_msg = f"Invalid value for 'digital-signature-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIGITAL_SIGNATURE_AUTH)}"
            error_msg += f"\n  → Example: digital-signature-auth='{{ VALID_BODY_DIGITAL_SIGNATURE_AUTH[0] }}'"
            return (False, error_msg)
    if "signature-hash-alg" in payload:
        value = payload["signature-hash-alg"]
        if value not in VALID_BODY_SIGNATURE_HASH_ALG:
            desc = FIELD_DESCRIPTIONS.get("signature-hash-alg", "")
            error_msg = f"Invalid value for 'signature-hash-alg': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SIGNATURE_HASH_ALG)}"
            error_msg += f"\n  → Example: signature-hash-alg='{{ VALID_BODY_SIGNATURE_HASH_ALG[0] }}'"
            return (False, error_msg)
    if "rsa-signature-format" in payload:
        value = payload["rsa-signature-format"]
        if value not in VALID_BODY_RSA_SIGNATURE_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("rsa-signature-format", "")
            error_msg = f"Invalid value for 'rsa-signature-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSA_SIGNATURE_FORMAT)}"
            error_msg += f"\n  → Example: rsa-signature-format='{{ VALID_BODY_RSA_SIGNATURE_FORMAT[0] }}'"
            return (False, error_msg)
    if "rsa-signature-hash-override" in payload:
        value = payload["rsa-signature-hash-override"]
        if value not in VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("rsa-signature-hash-override", "")
            error_msg = f"Invalid value for 'rsa-signature-hash-override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE)}"
            error_msg += f"\n  → Example: rsa-signature-hash-override='{{ VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "enforce-unique-id" in payload:
        value = payload["enforce-unique-id"]
        if value not in VALID_BODY_ENFORCE_UNIQUE_ID:
            desc = FIELD_DESCRIPTIONS.get("enforce-unique-id", "")
            error_msg = f"Invalid value for 'enforce-unique-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_UNIQUE_ID)}"
            error_msg += f"\n  → Example: enforce-unique-id='{{ VALID_BODY_ENFORCE_UNIQUE_ID[0] }}'"
            return (False, error_msg)
    if "cert-id-validation" in payload:
        value = payload["cert-id-validation"]
        if value not in VALID_BODY_CERT_ID_VALIDATION:
            desc = FIELD_DESCRIPTIONS.get("cert-id-validation", "")
            error_msg = f"Invalid value for 'cert-id-validation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_ID_VALIDATION)}"
            error_msg += f"\n  → Example: cert-id-validation='{{ VALID_BODY_CERT_ID_VALIDATION[0] }}'"
            return (False, error_msg)
    if "fec-egress" in payload:
        value = payload["fec-egress"]
        if value not in VALID_BODY_FEC_EGRESS:
            desc = FIELD_DESCRIPTIONS.get("fec-egress", "")
            error_msg = f"Invalid value for 'fec-egress': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEC_EGRESS)}"
            error_msg += f"\n  → Example: fec-egress='{{ VALID_BODY_FEC_EGRESS[0] }}'"
            return (False, error_msg)
    if "fec-codec" in payload:
        value = payload["fec-codec"]
        if value not in VALID_BODY_FEC_CODEC:
            desc = FIELD_DESCRIPTIONS.get("fec-codec", "")
            error_msg = f"Invalid value for 'fec-codec': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEC_CODEC)}"
            error_msg += f"\n  → Example: fec-codec='{{ VALID_BODY_FEC_CODEC[0] }}'"
            return (False, error_msg)
    if "fec-ingress" in payload:
        value = payload["fec-ingress"]
        if value not in VALID_BODY_FEC_INGRESS:
            desc = FIELD_DESCRIPTIONS.get("fec-ingress", "")
            error_msg = f"Invalid value for 'fec-ingress': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEC_INGRESS)}"
            error_msg += f"\n  → Example: fec-ingress='{{ VALID_BODY_FEC_INGRESS[0] }}'"
            return (False, error_msg)
    if "network-overlay" in payload:
        value = payload["network-overlay"]
        if value not in VALID_BODY_NETWORK_OVERLAY:
            desc = FIELD_DESCRIPTIONS.get("network-overlay", "")
            error_msg = f"Invalid value for 'network-overlay': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NETWORK_OVERLAY)}"
            error_msg += f"\n  → Example: network-overlay='{{ VALID_BODY_NETWORK_OVERLAY[0] }}'"
            return (False, error_msg)
    if "dev-id-notification" in payload:
        value = payload["dev-id-notification"]
        if value not in VALID_BODY_DEV_ID_NOTIFICATION:
            desc = FIELD_DESCRIPTIONS.get("dev-id-notification", "")
            error_msg = f"Invalid value for 'dev-id-notification': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEV_ID_NOTIFICATION)}"
            error_msg += f"\n  → Example: dev-id-notification='{{ VALID_BODY_DEV_ID_NOTIFICATION[0] }}'"
            return (False, error_msg)
    if "loopback-asymroute" in payload:
        value = payload["loopback-asymroute"]
        if value not in VALID_BODY_LOOPBACK_ASYMROUTE:
            desc = FIELD_DESCRIPTIONS.get("loopback-asymroute", "")
            error_msg = f"Invalid value for 'loopback-asymroute': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOOPBACK_ASYMROUTE)}"
            error_msg += f"\n  → Example: loopback-asymroute='{{ VALID_BODY_LOOPBACK_ASYMROUTE[0] }}'"
            return (False, error_msg)
    if "exchange-fgt-device-id" in payload:
        value = payload["exchange-fgt-device-id"]
        if value not in VALID_BODY_EXCHANGE_FGT_DEVICE_ID:
            desc = FIELD_DESCRIPTIONS.get("exchange-fgt-device-id", "")
            error_msg = f"Invalid value for 'exchange-fgt-device-id': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXCHANGE_FGT_DEVICE_ID)}"
            error_msg += f"\n  → Example: exchange-fgt-device-id='{{ VALID_BODY_EXCHANGE_FGT_DEVICE_ID[0] }}'"
            return (False, error_msg)
    if "ipv6-auto-linklocal" in payload:
        value = payload["ipv6-auto-linklocal"]
        if value not in VALID_BODY_IPV6_AUTO_LINKLOCAL:
            desc = FIELD_DESCRIPTIONS.get("ipv6-auto-linklocal", "")
            error_msg = f"Invalid value for 'ipv6-auto-linklocal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_AUTO_LINKLOCAL)}"
            error_msg += f"\n  → Example: ipv6-auto-linklocal='{{ VALID_BODY_IPV6_AUTO_LINKLOCAL[0] }}'"
            return (False, error_msg)
    if "ems-sn-check" in payload:
        value = payload["ems-sn-check"]
        if value not in VALID_BODY_EMS_SN_CHECK:
            desc = FIELD_DESCRIPTIONS.get("ems-sn-check", "")
            error_msg = f"Invalid value for 'ems-sn-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMS_SN_CHECK)}"
            error_msg += f"\n  → Example: ems-sn-check='{{ VALID_BODY_EMS_SN_CHECK[0] }}'"
            return (False, error_msg)
    if "cert-trust-store" in payload:
        value = payload["cert-trust-store"]
        if value not in VALID_BODY_CERT_TRUST_STORE:
            desc = FIELD_DESCRIPTIONS.get("cert-trust-store", "")
            error_msg = f"Invalid value for 'cert-trust-store': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_TRUST_STORE)}"
            error_msg += f"\n  → Example: cert-trust-store='{{ VALID_BODY_CERT_TRUST_STORE[0] }}'"
            return (False, error_msg)
    if "qkd" in payload:
        value = payload["qkd"]
        if value not in VALID_BODY_QKD:
            desc = FIELD_DESCRIPTIONS.get("qkd", "")
            error_msg = f"Invalid value for 'qkd': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QKD)}"
            error_msg += f"\n  → Example: qkd='{{ VALID_BODY_QKD[0] }}'"
            return (False, error_msg)
    if "qkd-hybrid" in payload:
        value = payload["qkd-hybrid"]
        if value not in VALID_BODY_QKD_HYBRID:
            desc = FIELD_DESCRIPTIONS.get("qkd-hybrid", "")
            error_msg = f"Invalid value for 'qkd-hybrid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QKD_HYBRID)}"
            error_msg += f"\n  → Example: qkd-hybrid='{{ VALID_BODY_QKD_HYBRID[0] }}'"
            return (False, error_msg)
    if "transport" in payload:
        value = payload["transport"]
        if value not in VALID_BODY_TRANSPORT:
            desc = FIELD_DESCRIPTIONS.get("transport", "")
            error_msg = f"Invalid value for 'transport': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRANSPORT)}"
            error_msg += f"\n  → Example: transport='{{ VALID_BODY_TRANSPORT[0] }}'"
            return (False, error_msg)
    if "fortinet-esp" in payload:
        value = payload["fortinet-esp"]
        if value not in VALID_BODY_FORTINET_ESP:
            desc = FIELD_DESCRIPTIONS.get("fortinet-esp", "")
            error_msg = f"Invalid value for 'fortinet-esp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTINET_ESP)}"
            error_msg += f"\n  → Example: fortinet-esp='{{ VALID_BODY_FORTINET_ESP[0] }}'"
            return (False, error_msg)
    if "remote-gw-match" in payload:
        value = payload["remote-gw-match"]
        if value not in VALID_BODY_REMOTE_GW_MATCH:
            desc = FIELD_DESCRIPTIONS.get("remote-gw-match", "")
            error_msg = f"Invalid value for 'remote-gw-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REMOTE_GW_MATCH)}"
            error_msg += f"\n  → Example: remote-gw-match='{{ VALID_BODY_REMOTE_GW_MATCH[0] }}'"
            return (False, error_msg)
    if "remote-gw6-match" in payload:
        value = payload["remote-gw6-match"]
        if value not in VALID_BODY_REMOTE_GW6_MATCH:
            desc = FIELD_DESCRIPTIONS.get("remote-gw6-match", "")
            error_msg = f"Invalid value for 'remote-gw6-match': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REMOTE_GW6_MATCH)}"
            error_msg += f"\n  → Example: remote-gw6-match='{{ VALID_BODY_REMOTE_GW6_MATCH[0] }}'"
            return (False, error_msg)
    if "cert-peer-username-validation" in payload:
        value = payload["cert-peer-username-validation"]
        if value not in VALID_BODY_CERT_PEER_USERNAME_VALIDATION:
            desc = FIELD_DESCRIPTIONS.get("cert-peer-username-validation", "")
            error_msg = f"Invalid value for 'cert-peer-username-validation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_PEER_USERNAME_VALIDATION)}"
            error_msg += f"\n  → Example: cert-peer-username-validation='{{ VALID_BODY_CERT_PEER_USERNAME_VALIDATION[0] }}'"
            return (False, error_msg)
    if "cert-peer-username-strip" in payload:
        value = payload["cert-peer-username-strip"]
        if value not in VALID_BODY_CERT_PEER_USERNAME_STRIP:
            desc = FIELD_DESCRIPTIONS.get("cert-peer-username-strip", "")
            error_msg = f"Invalid value for 'cert-peer-username-strip': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CERT_PEER_USERNAME_STRIP)}"
            error_msg += f"\n  → Example: cert-peer-username-strip='{{ VALID_BODY_CERT_PEER_USERNAME_STRIP[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vpn_ipsec_phase1_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update vpn/ipsec/phase1.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_vpn_ipsec_phase1_put(payload)
    """
    # Step 1: Validate enum values
    if "type" in payload:
        value = payload["type"]
        if value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid value for 'type'='{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )
    if "ike-version" in payload:
        value = payload["ike-version"]
        if value not in VALID_BODY_IKE_VERSION:
            return (
                False,
                f"Invalid value for 'ike-version'='{value}'. Must be one of: {', '.join(VALID_BODY_IKE_VERSION)}",
            )
    if "authmethod" in payload:
        value = payload["authmethod"]
        if value not in VALID_BODY_AUTHMETHOD:
            return (
                False,
                f"Invalid value for 'authmethod'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHMETHOD)}",
            )
    if "authmethod-remote" in payload:
        value = payload["authmethod-remote"]
        if value not in VALID_BODY_AUTHMETHOD_REMOTE:
            return (
                False,
                f"Invalid value for 'authmethod-remote'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHMETHOD_REMOTE)}",
            )
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "peertype" in payload:
        value = payload["peertype"]
        if value not in VALID_BODY_PEERTYPE:
            return (
                False,
                f"Invalid value for 'peertype'='{value}'. Must be one of: {', '.join(VALID_BODY_PEERTYPE)}",
            )
    if "mode-cfg" in payload:
        value = payload["mode-cfg"]
        if value not in VALID_BODY_MODE_CFG:
            return (
                False,
                f"Invalid value for 'mode-cfg'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE_CFG)}",
            )
    if "mode-cfg-allow-client-selector" in payload:
        value = payload["mode-cfg-allow-client-selector"]
        if value not in VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR:
            return (
                False,
                f"Invalid value for 'mode-cfg-allow-client-selector'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR)}",
            )
    if "assign-ip" in payload:
        value = payload["assign-ip"]
        if value not in VALID_BODY_ASSIGN_IP:
            return (
                False,
                f"Invalid value for 'assign-ip'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGN_IP)}",
            )
    if "assign-ip-from" in payload:
        value = payload["assign-ip-from"]
        if value not in VALID_BODY_ASSIGN_IP_FROM:
            return (
                False,
                f"Invalid value for 'assign-ip-from'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGN_IP_FROM)}",
            )
    if "dns-mode" in payload:
        value = payload["dns-mode"]
        if value not in VALID_BODY_DNS_MODE:
            return (
                False,
                f"Invalid value for 'dns-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_DNS_MODE)}",
            )
    if "unity-support" in payload:
        value = payload["unity-support"]
        if value not in VALID_BODY_UNITY_SUPPORT:
            return (
                False,
                f"Invalid value for 'unity-support'='{value}'. Must be one of: {', '.join(VALID_BODY_UNITY_SUPPORT)}",
            )
    if "include-local-lan" in payload:
        value = payload["include-local-lan"]
        if value not in VALID_BODY_INCLUDE_LOCAL_LAN:
            return (
                False,
                f"Invalid value for 'include-local-lan'='{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_LOCAL_LAN)}",
            )
    if "save-password" in payload:
        value = payload["save-password"]
        if value not in VALID_BODY_SAVE_PASSWORD:
            return (
                False,
                f"Invalid value for 'save-password'='{value}'. Must be one of: {', '.join(VALID_BODY_SAVE_PASSWORD)}",
            )
    if "client-auto-negotiate" in payload:
        value = payload["client-auto-negotiate"]
        if value not in VALID_BODY_CLIENT_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid value for 'client-auto-negotiate'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_AUTO_NEGOTIATE)}",
            )
    if "client-keep-alive" in payload:
        value = payload["client-keep-alive"]
        if value not in VALID_BODY_CLIENT_KEEP_ALIVE:
            return (
                False,
                f"Invalid value for 'client-keep-alive'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_KEEP_ALIVE)}",
            )
    if "proposal" in payload:
        value = payload["proposal"]
        if value not in VALID_BODY_PROPOSAL:
            return (
                False,
                f"Invalid value for 'proposal'='{value}'. Must be one of: {', '.join(VALID_BODY_PROPOSAL)}",
            )
    if "add-route" in payload:
        value = payload["add-route"]
        if value not in VALID_BODY_ADD_ROUTE:
            return (
                False,
                f"Invalid value for 'add-route'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_ROUTE)}",
            )
    if "add-gw-route" in payload:
        value = payload["add-gw-route"]
        if value not in VALID_BODY_ADD_GW_ROUTE:
            return (
                False,
                f"Invalid value for 'add-gw-route'='{value}'. Must be one of: {', '.join(VALID_BODY_ADD_GW_ROUTE)}",
            )
    if "localid-type" in payload:
        value = payload["localid-type"]
        if value not in VALID_BODY_LOCALID_TYPE:
            return (
                False,
                f"Invalid value for 'localid-type'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCALID_TYPE)}",
            )
    if "auto-negotiate" in payload:
        value = payload["auto-negotiate"]
        if value not in VALID_BODY_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid value for 'auto-negotiate'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_NEGOTIATE)}",
            )
    if "fragmentation" in payload:
        value = payload["fragmentation"]
        if value not in VALID_BODY_FRAGMENTATION:
            return (
                False,
                f"Invalid value for 'fragmentation'='{value}'. Must be one of: {', '.join(VALID_BODY_FRAGMENTATION)}",
            )
    if "dpd" in payload:
        value = payload["dpd"]
        if value not in VALID_BODY_DPD:
            return (
                False,
                f"Invalid value for 'dpd'='{value}'. Must be one of: {', '.join(VALID_BODY_DPD)}",
            )
    if "npu-offload" in payload:
        value = payload["npu-offload"]
        if value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid value for 'npu-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )
    if "send-cert-chain" in payload:
        value = payload["send-cert-chain"]
        if value not in VALID_BODY_SEND_CERT_CHAIN:
            return (
                False,
                f"Invalid value for 'send-cert-chain'='{value}'. Must be one of: {', '.join(VALID_BODY_SEND_CERT_CHAIN)}",
            )
    if "dhgrp" in payload:
        value = payload["dhgrp"]
        if value not in VALID_BODY_DHGRP:
            return (
                False,
                f"Invalid value for 'dhgrp'='{value}'. Must be one of: {', '.join(VALID_BODY_DHGRP)}",
            )
    if "addke1" in payload:
        value = payload["addke1"]
        if value not in VALID_BODY_ADDKE1:
            return (
                False,
                f"Invalid value for 'addke1'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE1)}",
            )
    if "addke2" in payload:
        value = payload["addke2"]
        if value not in VALID_BODY_ADDKE2:
            return (
                False,
                f"Invalid value for 'addke2'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE2)}",
            )
    if "addke3" in payload:
        value = payload["addke3"]
        if value not in VALID_BODY_ADDKE3:
            return (
                False,
                f"Invalid value for 'addke3'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE3)}",
            )
    if "addke4" in payload:
        value = payload["addke4"]
        if value not in VALID_BODY_ADDKE4:
            return (
                False,
                f"Invalid value for 'addke4'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE4)}",
            )
    if "addke5" in payload:
        value = payload["addke5"]
        if value not in VALID_BODY_ADDKE5:
            return (
                False,
                f"Invalid value for 'addke5'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE5)}",
            )
    if "addke6" in payload:
        value = payload["addke6"]
        if value not in VALID_BODY_ADDKE6:
            return (
                False,
                f"Invalid value for 'addke6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE6)}",
            )
    if "addke7" in payload:
        value = payload["addke7"]
        if value not in VALID_BODY_ADDKE7:
            return (
                False,
                f"Invalid value for 'addke7'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE7)}",
            )
    if "suite-b" in payload:
        value = payload["suite-b"]
        if value not in VALID_BODY_SUITE_B:
            return (
                False,
                f"Invalid value for 'suite-b'='{value}'. Must be one of: {', '.join(VALID_BODY_SUITE_B)}",
            )
    if "eap" in payload:
        value = payload["eap"]
        if value not in VALID_BODY_EAP:
            return (
                False,
                f"Invalid value for 'eap'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP)}",
            )
    if "eap-identity" in payload:
        value = payload["eap-identity"]
        if value not in VALID_BODY_EAP_IDENTITY:
            return (
                False,
                f"Invalid value for 'eap-identity'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_IDENTITY)}",
            )
    if "eap-cert-auth" in payload:
        value = payload["eap-cert-auth"]
        if value not in VALID_BODY_EAP_CERT_AUTH:
            return (
                False,
                f"Invalid value for 'eap-cert-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_CERT_AUTH)}",
            )
    if "acct-verify" in payload:
        value = payload["acct-verify"]
        if value not in VALID_BODY_ACCT_VERIFY:
            return (
                False,
                f"Invalid value for 'acct-verify'='{value}'. Must be one of: {', '.join(VALID_BODY_ACCT_VERIFY)}",
            )
    if "ppk" in payload:
        value = payload["ppk"]
        if value not in VALID_BODY_PPK:
            return (
                False,
                f"Invalid value for 'ppk'='{value}'. Must be one of: {', '.join(VALID_BODY_PPK)}",
            )
    if "wizard-type" in payload:
        value = payload["wizard-type"]
        if value not in VALID_BODY_WIZARD_TYPE:
            return (
                False,
                f"Invalid value for 'wizard-type'='{value}'. Must be one of: {', '.join(VALID_BODY_WIZARD_TYPE)}",
            )
    if "xauthtype" in payload:
        value = payload["xauthtype"]
        if value not in VALID_BODY_XAUTHTYPE:
            return (
                False,
                f"Invalid value for 'xauthtype'='{value}'. Must be one of: {', '.join(VALID_BODY_XAUTHTYPE)}",
            )
    if "reauth" in payload:
        value = payload["reauth"]
        if value not in VALID_BODY_REAUTH:
            return (
                False,
                f"Invalid value for 'reauth'='{value}'. Must be one of: {', '.join(VALID_BODY_REAUTH)}",
            )
    if "group-authentication" in payload:
        value = payload["group-authentication"]
        if value not in VALID_BODY_GROUP_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'group-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_AUTHENTICATION)}",
            )
    if "mesh-selector-type" in payload:
        value = payload["mesh-selector-type"]
        if value not in VALID_BODY_MESH_SELECTOR_TYPE:
            return (
                False,
                f"Invalid value for 'mesh-selector-type'='{value}'. Must be one of: {', '.join(VALID_BODY_MESH_SELECTOR_TYPE)}",
            )
    if "idle-timeout" in payload:
        value = payload["idle-timeout"]
        if value not in VALID_BODY_IDLE_TIMEOUT:
            return (
                False,
                f"Invalid value for 'idle-timeout'='{value}'. Must be one of: {', '.join(VALID_BODY_IDLE_TIMEOUT)}",
            )
    if "shared-idle-timeout" in payload:
        value = payload["shared-idle-timeout"]
        if value not in VALID_BODY_SHARED_IDLE_TIMEOUT:
            return (
                False,
                f"Invalid value for 'shared-idle-timeout'='{value}'. Must be one of: {', '.join(VALID_BODY_SHARED_IDLE_TIMEOUT)}",
            )
    if "ha-sync-esp-seqno" in payload:
        value = payload["ha-sync-esp-seqno"]
        if value not in VALID_BODY_HA_SYNC_ESP_SEQNO:
            return (
                False,
                f"Invalid value for 'ha-sync-esp-seqno'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_SYNC_ESP_SEQNO)}",
            )
    if "fgsp-sync" in payload:
        value = payload["fgsp-sync"]
        if value not in VALID_BODY_FGSP_SYNC:
            return (
                False,
                f"Invalid value for 'fgsp-sync'='{value}'. Must be one of: {', '.join(VALID_BODY_FGSP_SYNC)}",
            )
    if "inbound-dscp-copy" in payload:
        value = payload["inbound-dscp-copy"]
        if value not in VALID_BODY_INBOUND_DSCP_COPY:
            return (
                False,
                f"Invalid value for 'inbound-dscp-copy'='{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND_DSCP_COPY)}",
            )
    if "nattraversal" in payload:
        value = payload["nattraversal"]
        if value not in VALID_BODY_NATTRAVERSAL:
            return (
                False,
                f"Invalid value for 'nattraversal'='{value}'. Must be one of: {', '.join(VALID_BODY_NATTRAVERSAL)}",
            )
    if "esn" in payload:
        value = payload["esn"]
        if value not in VALID_BODY_ESN:
            return (
                False,
                f"Invalid value for 'esn'='{value}'. Must be one of: {', '.join(VALID_BODY_ESN)}",
            )
    if "childless-ike" in payload:
        value = payload["childless-ike"]
        if value not in VALID_BODY_CHILDLESS_IKE:
            return (
                False,
                f"Invalid value for 'childless-ike'='{value}'. Must be one of: {', '.join(VALID_BODY_CHILDLESS_IKE)}",
            )
    if "azure-ad-autoconnect" in payload:
        value = payload["azure-ad-autoconnect"]
        if value not in VALID_BODY_AZURE_AD_AUTOCONNECT:
            return (
                False,
                f"Invalid value for 'azure-ad-autoconnect'='{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_AD_AUTOCONNECT)}",
            )
    if "client-resume" in payload:
        value = payload["client-resume"]
        if value not in VALID_BODY_CLIENT_RESUME:
            return (
                False,
                f"Invalid value for 'client-resume'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_RESUME)}",
            )
    if "rekey" in payload:
        value = payload["rekey"]
        if value not in VALID_BODY_REKEY:
            return (
                False,
                f"Invalid value for 'rekey'='{value}'. Must be one of: {', '.join(VALID_BODY_REKEY)}",
            )
    if "digital-signature-auth" in payload:
        value = payload["digital-signature-auth"]
        if value not in VALID_BODY_DIGITAL_SIGNATURE_AUTH:
            return (
                False,
                f"Invalid value for 'digital-signature-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_DIGITAL_SIGNATURE_AUTH)}",
            )
    if "signature-hash-alg" in payload:
        value = payload["signature-hash-alg"]
        if value not in VALID_BODY_SIGNATURE_HASH_ALG:
            return (
                False,
                f"Invalid value for 'signature-hash-alg'='{value}'. Must be one of: {', '.join(VALID_BODY_SIGNATURE_HASH_ALG)}",
            )
    if "rsa-signature-format" in payload:
        value = payload["rsa-signature-format"]
        if value not in VALID_BODY_RSA_SIGNATURE_FORMAT:
            return (
                False,
                f"Invalid value for 'rsa-signature-format'='{value}'. Must be one of: {', '.join(VALID_BODY_RSA_SIGNATURE_FORMAT)}",
            )
    if "rsa-signature-hash-override" in payload:
        value = payload["rsa-signature-hash-override"]
        if value not in VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE:
            return (
                False,
                f"Invalid value for 'rsa-signature-hash-override'='{value}'. Must be one of: {', '.join(VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE)}",
            )
    if "enforce-unique-id" in payload:
        value = payload["enforce-unique-id"]
        if value not in VALID_BODY_ENFORCE_UNIQUE_ID:
            return (
                False,
                f"Invalid value for 'enforce-unique-id'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_UNIQUE_ID)}",
            )
    if "cert-id-validation" in payload:
        value = payload["cert-id-validation"]
        if value not in VALID_BODY_CERT_ID_VALIDATION:
            return (
                False,
                f"Invalid value for 'cert-id-validation'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_ID_VALIDATION)}",
            )
    if "fec-egress" in payload:
        value = payload["fec-egress"]
        if value not in VALID_BODY_FEC_EGRESS:
            return (
                False,
                f"Invalid value for 'fec-egress'='{value}'. Must be one of: {', '.join(VALID_BODY_FEC_EGRESS)}",
            )
    if "fec-codec" in payload:
        value = payload["fec-codec"]
        if value not in VALID_BODY_FEC_CODEC:
            return (
                False,
                f"Invalid value for 'fec-codec'='{value}'. Must be one of: {', '.join(VALID_BODY_FEC_CODEC)}",
            )
    if "fec-ingress" in payload:
        value = payload["fec-ingress"]
        if value not in VALID_BODY_FEC_INGRESS:
            return (
                False,
                f"Invalid value for 'fec-ingress'='{value}'. Must be one of: {', '.join(VALID_BODY_FEC_INGRESS)}",
            )
    if "network-overlay" in payload:
        value = payload["network-overlay"]
        if value not in VALID_BODY_NETWORK_OVERLAY:
            return (
                False,
                f"Invalid value for 'network-overlay'='{value}'. Must be one of: {', '.join(VALID_BODY_NETWORK_OVERLAY)}",
            )
    if "dev-id-notification" in payload:
        value = payload["dev-id-notification"]
        if value not in VALID_BODY_DEV_ID_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'dev-id-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_DEV_ID_NOTIFICATION)}",
            )
    if "loopback-asymroute" in payload:
        value = payload["loopback-asymroute"]
        if value not in VALID_BODY_LOOPBACK_ASYMROUTE:
            return (
                False,
                f"Invalid value for 'loopback-asymroute'='{value}'. Must be one of: {', '.join(VALID_BODY_LOOPBACK_ASYMROUTE)}",
            )
    if "exchange-fgt-device-id" in payload:
        value = payload["exchange-fgt-device-id"]
        if value not in VALID_BODY_EXCHANGE_FGT_DEVICE_ID:
            return (
                False,
                f"Invalid value for 'exchange-fgt-device-id'='{value}'. Must be one of: {', '.join(VALID_BODY_EXCHANGE_FGT_DEVICE_ID)}",
            )
    if "ipv6-auto-linklocal" in payload:
        value = payload["ipv6-auto-linklocal"]
        if value not in VALID_BODY_IPV6_AUTO_LINKLOCAL:
            return (
                False,
                f"Invalid value for 'ipv6-auto-linklocal'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_AUTO_LINKLOCAL)}",
            )
    if "ems-sn-check" in payload:
        value = payload["ems-sn-check"]
        if value not in VALID_BODY_EMS_SN_CHECK:
            return (
                False,
                f"Invalid value for 'ems-sn-check'='{value}'. Must be one of: {', '.join(VALID_BODY_EMS_SN_CHECK)}",
            )
    if "cert-trust-store" in payload:
        value = payload["cert-trust-store"]
        if value not in VALID_BODY_CERT_TRUST_STORE:
            return (
                False,
                f"Invalid value for 'cert-trust-store'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_TRUST_STORE)}",
            )
    if "qkd" in payload:
        value = payload["qkd"]
        if value not in VALID_BODY_QKD:
            return (
                False,
                f"Invalid value for 'qkd'='{value}'. Must be one of: {', '.join(VALID_BODY_QKD)}",
            )
    if "qkd-hybrid" in payload:
        value = payload["qkd-hybrid"]
        if value not in VALID_BODY_QKD_HYBRID:
            return (
                False,
                f"Invalid value for 'qkd-hybrid'='{value}'. Must be one of: {', '.join(VALID_BODY_QKD_HYBRID)}",
            )
    if "transport" in payload:
        value = payload["transport"]
        if value not in VALID_BODY_TRANSPORT:
            return (
                False,
                f"Invalid value for 'transport'='{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT)}",
            )
    if "fortinet-esp" in payload:
        value = payload["fortinet-esp"]
        if value not in VALID_BODY_FORTINET_ESP:
            return (
                False,
                f"Invalid value for 'fortinet-esp'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTINET_ESP)}",
            )
    if "remote-gw-match" in payload:
        value = payload["remote-gw-match"]
        if value not in VALID_BODY_REMOTE_GW_MATCH:
            return (
                False,
                f"Invalid value for 'remote-gw-match'='{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_GW_MATCH)}",
            )
    if "remote-gw6-match" in payload:
        value = payload["remote-gw6-match"]
        if value not in VALID_BODY_REMOTE_GW6_MATCH:
            return (
                False,
                f"Invalid value for 'remote-gw6-match'='{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_GW6_MATCH)}",
            )
    if "cert-peer-username-validation" in payload:
        value = payload["cert-peer-username-validation"]
        if value not in VALID_BODY_CERT_PEER_USERNAME_VALIDATION:
            return (
                False,
                f"Invalid value for 'cert-peer-username-validation'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_PEER_USERNAME_VALIDATION)}",
            )
    if "cert-peer-username-strip" in payload:
        value = payload["cert-peer-username-strip"]
        if value not in VALID_BODY_CERT_PEER_USERNAME_STRIP:
            return (
                False,
                f"Invalid value for 'cert-peer-username-strip'='{value}'. Must be one of: {', '.join(VALID_BODY_CERT_PEER_USERNAME_STRIP)}",
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
    "endpoint": "vpn/ipsec/phase1",
    "category": "cmdb",
    "api_path": "vpn.ipsec/phase1",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure VPN remote gateway.",
    "total_fields": 162,
    "required_fields_count": 15,
    "fields_with_defaults_count": 148,
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
