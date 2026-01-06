"""Validation helpers for wireless_controller/vap - Auto-generated"""

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
    "name",  # Virtual AP name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "pre-auth": "enable",
    "external-pre-auth": "disable",
    "mesh-backhaul": "disable",
    "atf-weight": 20,
    "max-clients": 0,
    "max-clients-ap": 0,
    "ssid": "fortinet",
    "broadcast-ssid": "enable",
    "security": "wpa2-only-personal",
    "pmf": "disable",
    "pmf-assoc-comeback-timeout": 1,
    "pmf-sa-query-retry-timeout": 2,
    "beacon-protection": "disable",
    "okc": "enable",
    "mbo": "disable",
    "gas-comeback-delay": 500,
    "gas-fragmentation-limit": 1024,
    "mbo-cell-data-conn-pref": "prefer-not",
    "80211k": "enable",
    "80211v": "enable",
    "neighbor-report-dual-band": "disable",
    "fast-bss-transition": "disable",
    "ft-mobility-domain": 1000,
    "ft-r0-key-lifetime": 480,
    "ft-over-ds": "disable",
    "sae-groups": "",
    "owe-groups": "",
    "owe-transition": "disable",
    "owe-transition-ssid": "",
    "additional-akms": "",
    "eapol-key-retries": "enable",
    "tkip-counter-measure": "enable",
    "external-web-format": "auto-detect",
    "external-logout": "",
    "mac-username-delimiter": "hyphen",
    "mac-password-delimiter": "hyphen",
    "mac-calling-station-delimiter": "hyphen",
    "mac-called-station-delimiter": "hyphen",
    "mac-case": "uppercase",
    "called-station-id-type": "mac",
    "mac-auth-bypass": "disable",
    "radius-mac-auth": "disable",
    "radius-mac-auth-server": "",
    "radius-mac-auth-block-interval": 0,
    "radius-mac-mpsk-auth": "disable",
    "radius-mac-mpsk-timeout": 86400,
    "auth": "",
    "encrypt": "AES",
    "keyindex": 1,
    "sae-h2e-only": "disable",
    "sae-hnp-only": "disable",
    "sae-pk": "disable",
    "sae-private-key": "",
    "akm24-only": "disable",
    "radius-server": "",
    "nas-filter-rule": "disable",
    "domain-name-stripping": "disable",
    "mlo": "disable",
    "local-standalone": "disable",
    "local-standalone-nat": "disable",
    "ip": "0.0.0.0 0.0.0.0",
    "dhcp-lease-time": 2400,
    "local-standalone-dns": "disable",
    "local-standalone-dns-ip": "",
    "local-lan-partition": "disable",
    "local-bridging": "disable",
    "local-lan": "allow",
    "local-authentication": "disable",
    "captive-portal": "disable",
    "captive-network-assistant-bypass": "disable",
    "portal-message-override-group": "",
    "portal-type": "auth",
    "security-exempt-list": "",
    "auth-cert": "",
    "auth-portal-addr": "",
    "intra-vap-privacy": "disable",
    "ldpc": "rxtx",
    "high-efficiency": "enable",
    "target-wake-time": "enable",
    "port-macauth": "disable",
    "port-macauth-timeout": 600,
    "port-macauth-reauth-timeout": 7200,
    "bss-color-partial": "enable",
    "mpsk-profile": "",
    "split-tunneling": "disable",
    "nac": "disable",
    "nac-profile": "",
    "vlanid": 0,
    "vlan-auto": "disable",
    "dynamic-vlan": "disable",
    "captive-portal-fw-accounting": "disable",
    "captive-portal-ac-name": "",
    "captive-portal-auth-timeout": 0,
    "multicast-rate": "0",
    "multicast-enhance": "disable",
    "igmp-snooping": "disable",
    "dhcp-address-enforcement": "disable",
    "broadcast-suppression": "dhcp-up dhcp-ucast arp-known",
    "ipv6-rules": "drop-icmp6ra drop-icmp6rs drop-llmnr6 drop-icmp6mld2 drop-dhcp6s drop-dhcp6c ndp-proxy drop-ns-dad",
    "me-disable-thresh": 32,
    "mu-mimo": "enable",
    "probe-resp-suppression": "disable",
    "probe-resp-threshold": "-80",
    "radio-sensitivity": "disable",
    "quarantine": "disable",
    "radio-5g-threshold": "-76",
    "radio-2g-threshold": "-79",
    "vlan-pooling": "disable",
    "dhcp-option43-insertion": "enable",
    "dhcp-option82-insertion": "disable",
    "dhcp-option82-circuit-id-insertion": "disable",
    "dhcp-option82-remote-id-insertion": "disable",
    "ptk-rekey": "disable",
    "ptk-rekey-intv": 86400,
    "gtk-rekey": "disable",
    "gtk-rekey-intv": 86400,
    "eap-reauth": "disable",
    "eap-reauth-intv": 86400,
    "roaming-acct-interim-update": "disable",
    "qos-profile": "",
    "hotspot20-profile": "",
    "access-control-list": "",
    "primary-wag-profile": "",
    "secondary-wag-profile": "",
    "tunnel-echo-interval": 300,
    "tunnel-fallback-interval": 7200,
    "rates-11a": "",
    "rates-11bg": "",
    "rates-11n-ss12": "",
    "rates-11n-ss34": "",
    "rates-11ac-mcs-map": "",
    "rates-11ax-mcs-map": "",
    "rates-11be-mcs-map": "",
    "rates-11be-mcs-map-160": "",
    "rates-11be-mcs-map-320": "",
    "utm-profile": "",
    "utm-status": "disable",
    "utm-log": "enable",
    "ips-sensor": "",
    "application-list": "",
    "antivirus-profile": "",
    "webfilter-profile": "",
    "scan-botnet-connections": "monitor",
    "address-group": "",
    "address-group-policy": "disable",
    "sticky-client-remove": "disable",
    "sticky-client-threshold-5g": "-76",
    "sticky-client-threshold-2g": "-79",
    "sticky-client-threshold-6g": "-76",
    "bstm-rssi-disassoc-timer": 200,
    "bstm-load-balancing-disassoc-timer": 10,
    "bstm-disassociation-imminent": "enable",
    "beacon-advertising": "",
    "osen": "disable",
    "application-detection-engine": "disable",
    "application-dscp-marking": "disable",
    "application-report-intv": 120,
    "l3-roaming": "disable",
    "l3-roaming-mode": "direct",
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
    "name": "string",  # Virtual AP name.
    "pre-auth": "option",  # Enable/disable pre-authentication, where supported by client
    "external-pre-auth": "option",  # Enable/disable pre-authentication with external APs not mana
    "mesh-backhaul": "option",  # Enable/disable using this VAP as a WiFi mesh backhaul (defau
    "atf-weight": "integer",  # Airtime weight in percentage (default = 20).
    "max-clients": "integer",  # Maximum number of clients that can connect simultaneously to
    "max-clients-ap": "integer",  # Maximum number of clients that can connect simultaneously to
    "ssid": "string",  # IEEE 802.11 service set identifier (SSID) for the wireless i
    "broadcast-ssid": "option",  # Enable/disable broadcasting the SSID (default = enable).
    "security": "option",  # Security mode for the wireless interface (default = wpa2-onl
    "pmf": "option",  # Protected Management Frames (PMF) support (default = disable
    "pmf-assoc-comeback-timeout": "integer",  # Protected Management Frames (PMF) comeback maximum timeout (
    "pmf-sa-query-retry-timeout": "integer",  # Protected Management Frames (PMF) SA query retry timeout int
    "beacon-protection": "option",  # Enable/disable beacon protection support (default = disable)
    "okc": "option",  # Enable/disable Opportunistic Key Caching (OKC) (default = en
    "mbo": "option",  # Enable/disable Multiband Operation (default = disable).
    "gas-comeback-delay": "integer",  # GAS comeback delay (0 or 100 - 10000 milliseconds, default =
    "gas-fragmentation-limit": "integer",  # GAS fragmentation limit (512 - 4096, default = 1024).
    "mbo-cell-data-conn-pref": "option",  # MBO cell data connection preference (0, 1, or 255, default =
    "80211k": "option",  # Enable/disable 802.11k assisted roaming (default = enable).
    "80211v": "option",  # Enable/disable 802.11v assisted roaming (default = enable).
    "neighbor-report-dual-band": "option",  # Enable/disable dual-band neighbor report (default = disable)
    "fast-bss-transition": "option",  # Enable/disable 802.11r Fast BSS Transition (FT) (default = d
    "ft-mobility-domain": "integer",  # Mobility domain identifier in FT (1 - 65535, default = 1000)
    "ft-r0-key-lifetime": "integer",  # Lifetime of the PMK-R0 key in FT, 1-65535 minutes.
    "ft-over-ds": "option",  # Enable/disable FT over the Distribution System (DS).
    "sae-groups": "option",  # SAE-Groups.
    "owe-groups": "option",  # OWE-Groups.
    "owe-transition": "option",  # Enable/disable OWE transition mode support.
    "owe-transition-ssid": "string",  # OWE transition mode peer SSID.
    "additional-akms": "option",  # Additional AKMs.
    "eapol-key-retries": "option",  # Enable/disable retransmission of EAPOL-Key frames (message 3
    "tkip-counter-measure": "option",  # Enable/disable TKIP counter measure.
    "external-web": "var-string",  # URL of external authentication web server.
    "external-web-format": "option",  # URL query parameter detection (default = auto-detect).
    "external-logout": "string",  # URL of external authentication logout server.
    "mac-username-delimiter": "option",  # MAC authentication username delimiter (default = hyphen).
    "mac-password-delimiter": "option",  # MAC authentication password delimiter (default = hyphen).
    "mac-calling-station-delimiter": "option",  # MAC calling station delimiter (default = hyphen).
    "mac-called-station-delimiter": "option",  # MAC called station delimiter (default = hyphen).
    "mac-case": "option",  # MAC case (default = uppercase).
    "called-station-id-type": "option",  # The format type of RADIUS attribute Called-Station-Id (defau
    "mac-auth-bypass": "option",  # Enable/disable MAC authentication bypass.
    "radius-mac-auth": "option",  # Enable/disable RADIUS-based MAC authentication of clients (d
    "radius-mac-auth-server": "string",  # RADIUS-based MAC authentication server.
    "radius-mac-auth-block-interval": "integer",  # Don't send RADIUS MAC auth request again if the client has b
    "radius-mac-mpsk-auth": "option",  # Enable/disable RADIUS-based MAC authentication of clients fo
    "radius-mac-mpsk-timeout": "integer",  # RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000, d
    "radius-mac-auth-usergroups": "string",  # Selective user groups that are permitted for RADIUS mac auth
    "auth": "option",  # Authentication protocol.
    "encrypt": "option",  # Encryption protocol to use (only available when security is 
    "keyindex": "integer",  # WEP key index (1 - 4).
    "key": "password",  # WEP Key.
    "passphrase": "password",  # WPA pre-shared key (PSK) to be used to authenticate WiFi use
    "sae-password": "password",  # WPA3 SAE password to be used to authenticate WiFi users.
    "sae-h2e-only": "option",  # Use hash-to-element-only mechanism for PWE derivation (defau
    "sae-hnp-only": "option",  # Use hunting-and-pecking-only mechanism for PWE derivation (d
    "sae-pk": "option",  # Enable/disable WPA3 SAE-PK (default = disable).
    "sae-private-key": "string",  # Private key used for WPA3 SAE-PK authentication.
    "akm24-only": "option",  # WPA3 SAE using group-dependent hash only (default = disable)
    "radius-server": "string",  # RADIUS server to be used to authenticate WiFi users.
    "nas-filter-rule": "option",  # Enable/disable NAS filter rule support (default = disable).
    "domain-name-stripping": "option",  # Enable/disable stripping domain name from identity (default 
    "mlo": "option",  # Enable/disable WiFi7 Multi-Link-Operation (default = disable
    "local-standalone": "option",  # Enable/disable AP local standalone (default = disable).
    "local-standalone-nat": "option",  # Enable/disable AP local standalone NAT mode.
    "ip": "ipv4-classnet-host",  # IP address and subnet mask for the local standalone NAT subn
    "dhcp-lease-time": "integer",  # DHCP lease time in seconds for NAT IP address.
    "local-standalone-dns": "option",  # Enable/disable AP local standalone DNS.
    "local-standalone-dns-ip": "ipv4-address",  # IPv4 addresses for the local standalone DNS.
    "local-lan-partition": "option",  # Enable/disable segregating client traffic to local LAN side 
    "local-bridging": "option",  # Enable/disable bridging of wireless and Ethernet interfaces 
    "local-lan": "option",  # Allow/deny traffic destined for a Class A, B, or C private I
    "local-authentication": "option",  # Enable/disable AP local authentication.
    "usergroup": "string",  # Firewall user group to be used to authenticate WiFi users.
    "captive-portal": "option",  # Enable/disable captive portal.
    "captive-network-assistant-bypass": "option",  # Enable/disable Captive Network Assistant bypass.
    "portal-message-override-group": "string",  # Replacement message group for this VAP (only available when 
    "portal-message-overrides": "string",  # Individual message overrides.
    "portal-type": "option",  # Captive portal functionality. Configure how the captive port
    "selected-usergroups": "string",  # Selective user groups that are permitted to authenticate.
    "security-exempt-list": "string",  # Optional security exempt list for captive portal authenticat
    "security-redirect-url": "var-string",  # Optional URL for redirecting users after they pass captive p
    "auth-cert": "string",  # HTTPS server certificate.
    "auth-portal-addr": "string",  # Address of captive portal.
    "intra-vap-privacy": "option",  # Enable/disable blocking communication between clients on the
    "schedule": "string",  # Firewall schedules for enabling this VAP on the FortiAP. Thi
    "ldpc": "option",  # VAP low-density parity-check (LDPC) coding configuration.
    "high-efficiency": "option",  # Enable/disable 802.11ax high efficiency (default = enable).
    "target-wake-time": "option",  # Enable/disable 802.11ax target wake time (default = enable).
    "port-macauth": "option",  # Enable/disable LAN port MAC authentication (default = disabl
    "port-macauth-timeout": "integer",  # LAN port MAC authentication idle timeout value (default = 60
    "port-macauth-reauth-timeout": "integer",  # LAN port MAC authentication re-authentication timeout value 
    "bss-color-partial": "option",  # Enable/disable 802.11ax partial BSS color (default = enable)
    "mpsk-profile": "string",  # MPSK profile name.
    "split-tunneling": "option",  # Enable/disable split tunneling (default = disable).
    "nac": "option",  # Enable/disable network access control.
    "nac-profile": "string",  # NAC profile name.
    "vlanid": "integer",  # Optional VLAN ID.
    "vlan-auto": "option",  # Enable/disable automatic management of SSID VLAN interface.
    "dynamic-vlan": "option",  # Enable/disable dynamic VLAN assignment.
    "captive-portal-fw-accounting": "option",  # Enable/disable RADIUS accounting for captive portal firewall
    "captive-portal-ac-name": "string",  # Local-bridging captive portal ac-name.
    "captive-portal-auth-timeout": "integer",  # Hard timeout - AP will always clear the session after timeou
    "multicast-rate": "option",  # Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0).
    "multicast-enhance": "option",  # Enable/disable converting multicast to unicast to improve pe
    "igmp-snooping": "option",  # Enable/disable IGMP snooping.
    "dhcp-address-enforcement": "option",  # Enable/disable DHCP address enforcement (default = disable).
    "broadcast-suppression": "option",  # Optional suppression of broadcast messages. For example, you
    "ipv6-rules": "option",  # Optional rules of IPv6 packets. For example, you can keep RA
    "me-disable-thresh": "integer",  # Disable multicast enhancement when this many clients are rec
    "mu-mimo": "option",  # Enable/disable Multi-user MIMO (default = enable).
    "probe-resp-suppression": "option",  # Enable/disable probe response suppression (to ignore weak si
    "probe-resp-threshold": "string",  # Minimum signal level/threshold in dBm required for the AP re
    "radio-sensitivity": "option",  # Enable/disable software radio sensitivity (to ignore weak si
    "quarantine": "option",  # Enable/disable station quarantine (default = disable).
    "radio-5g-threshold": "string",  # Minimum signal level/threshold in dBm required for the AP re
    "radio-2g-threshold": "string",  # Minimum signal level/threshold in dBm required for the AP re
    "vlan-name": "string",  # Table for mapping VLAN name to VLAN ID.
    "vlan-pooling": "option",  # Enable/disable VLAN pooling, to allow grouping of multiple w
    "vlan-pool": "string",  # VLAN pool.
    "dhcp-option43-insertion": "option",  # Enable/disable insertion of DHCP option 43 (default = enable
    "dhcp-option82-insertion": "option",  # Enable/disable DHCP option 82 insert (default = disable).
    "dhcp-option82-circuit-id-insertion": "option",  # Enable/disable DHCP option 82 circuit-id insert (default = d
    "dhcp-option82-remote-id-insertion": "option",  # Enable/disable DHCP option 82 remote-id insert (default = di
    "ptk-rekey": "option",  # Enable/disable PTK rekey for WPA-Enterprise security.
    "ptk-rekey-intv": "integer",  # PTK rekey interval (600 - 864000 sec, default = 86400).
    "gtk-rekey": "option",  # Enable/disable GTK rekey for WPA security.
    "gtk-rekey-intv": "integer",  # GTK rekey interval (600 - 864000 sec, default = 86400).
    "eap-reauth": "option",  # Enable/disable EAP re-authentication for WPA-Enterprise secu
    "eap-reauth-intv": "integer",  # EAP re-authentication interval (1800 - 864000 sec, default =
    "roaming-acct-interim-update": "option",  # Enable/disable using accounting interim update instead of ac
    "qos-profile": "string",  # Quality of service profile name.
    "hotspot20-profile": "string",  # Hotspot 2.0 profile name.
    "access-control-list": "string",  # Profile name for access-control-list.
    "primary-wag-profile": "string",  # Primary wireless access gateway profile name.
    "secondary-wag-profile": "string",  # Secondary wireless access gateway profile name.
    "tunnel-echo-interval": "integer",  # The time interval to send echo to both primary and secondary
    "tunnel-fallback-interval": "integer",  # The time interval for secondary tunnel to fall back to prima
    "rates-11a": "option",  # Allowed data rates for 802.11a.
    "rates-11bg": "option",  # Allowed data rates for 802.11b/g.
    "rates-11n-ss12": "option",  # Allowed data rates for 802.11n with 1 or 2 spatial streams.
    "rates-11n-ss34": "option",  # Allowed data rates for 802.11n with 3 or 4 spatial streams.
    "rates-11ac-mcs-map": "string",  # Comma separated list of max supported VHT MCS for spatial st
    "rates-11ax-mcs-map": "string",  # Comma separated list of max supported HE MCS for spatial str
    "rates-11be-mcs-map": "string",  # Comma separated list of max nss that supports EHT-MCS 0-9, 1
    "rates-11be-mcs-map-160": "string",  # Comma separated list of max nss that supports EHT-MCS 0-9, 1
    "rates-11be-mcs-map-320": "string",  # Comma separated list of max nss that supports EHT-MCS 0-9, 1
    "utm-profile": "string",  # UTM profile name.
    "utm-status": "option",  # Enable to add one or more security profiles (AV, IPS, etc.) 
    "utm-log": "option",  # Enable/disable UTM logging.
    "ips-sensor": "string",  # IPS sensor name.
    "application-list": "string",  # Application control list name.
    "antivirus-profile": "string",  # AntiVirus profile name.
    "webfilter-profile": "string",  # WebFilter profile name.
    "scan-botnet-connections": "option",  # Block or monitor connections to Botnet servers or disable Bo
    "address-group": "string",  # Firewall Address Group Name.
    "address-group-policy": "option",  # Configure MAC address filtering policy for MAC addresses tha
    "sticky-client-remove": "option",  # Enable/disable sticky client remove to maintain good signal 
    "sticky-client-threshold-5g": "string",  # Minimum signal level/threshold in dBm required for the 5G cl
    "sticky-client-threshold-2g": "string",  # Minimum signal level/threshold in dBm required for the 2G cl
    "sticky-client-threshold-6g": "string",  # Minimum signal level/threshold in dBm required for the 6G cl
    "bstm-rssi-disassoc-timer": "integer",  # Time interval for client to voluntarily leave AP before forc
    "bstm-load-balancing-disassoc-timer": "integer",  # Time interval for client to voluntarily leave AP before forc
    "bstm-disassociation-imminent": "option",  # Enable/disable forcing of disassociation after the BSTM requ
    "beacon-advertising": "option",  # Fortinet beacon advertising IE data   (default = empty).
    "osen": "option",  # Enable/disable OSEN as part of key management (default = dis
    "application-detection-engine": "option",  # Enable/disable application detection engine (default = disab
    "application-dscp-marking": "option",  # Enable/disable application attribute based DSCP marking (def
    "application-report-intv": "integer",  # Application report interval (30 - 864000 sec, default = 120)
    "l3-roaming": "option",  # Enable/disable layer 3 roaming (default = disable).
    "l3-roaming-mode": "option",  # Select the way that layer 3 roaming traffic is passed (defau
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Virtual AP name.",
    "pre-auth": "Enable/disable pre-authentication, where supported by clients (default = enable).",
    "external-pre-auth": "Enable/disable pre-authentication with external APs not managed by the FortiGate (default = disable).",
    "mesh-backhaul": "Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open.",
    "atf-weight": "Airtime weight in percentage (default = 20).",
    "max-clients": "Maximum number of clients that can connect simultaneously to the VAP (default = 0, meaning no limitation).",
    "max-clients-ap": "Maximum number of clients that can connect simultaneously to the VAP per AP radio (default = 0, meaning no limitation).",
    "ssid": "IEEE 802.11 service set identifier (SSID) for the wireless interface. Users who wish to use the wireless network must configure their computers to access this SSID name.",
    "broadcast-ssid": "Enable/disable broadcasting the SSID (default = enable).",
    "security": "Security mode for the wireless interface (default = wpa2-only-personal).",
    "pmf": "Protected Management Frames (PMF) support (default = disable).",
    "pmf-assoc-comeback-timeout": "Protected Management Frames (PMF) comeback maximum timeout (1-20 sec).",
    "pmf-sa-query-retry-timeout": "Protected Management Frames (PMF) SA query retry timeout interval (1 - 5 100s of msec).",
    "beacon-protection": "Enable/disable beacon protection support (default = disable).",
    "okc": "Enable/disable Opportunistic Key Caching (OKC) (default = enable).",
    "mbo": "Enable/disable Multiband Operation (default = disable).",
    "gas-comeback-delay": "GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).",
    "gas-fragmentation-limit": "GAS fragmentation limit (512 - 4096, default = 1024).",
    "mbo-cell-data-conn-pref": "MBO cell data connection preference (0, 1, or 255, default = 1).",
    "80211k": "Enable/disable 802.11k assisted roaming (default = enable).",
    "80211v": "Enable/disable 802.11v assisted roaming (default = enable).",
    "neighbor-report-dual-band": "Enable/disable dual-band neighbor report (default = disable).",
    "fast-bss-transition": "Enable/disable 802.11r Fast BSS Transition (FT) (default = disable).",
    "ft-mobility-domain": "Mobility domain identifier in FT (1 - 65535, default = 1000).",
    "ft-r0-key-lifetime": "Lifetime of the PMK-R0 key in FT, 1-65535 minutes.",
    "ft-over-ds": "Enable/disable FT over the Distribution System (DS).",
    "sae-groups": "SAE-Groups.",
    "owe-groups": "OWE-Groups.",
    "owe-transition": "Enable/disable OWE transition mode support.",
    "owe-transition-ssid": "OWE transition mode peer SSID.",
    "additional-akms": "Additional AKMs.",
    "eapol-key-retries": "Enable/disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2) (default = enable).",
    "tkip-counter-measure": "Enable/disable TKIP counter measure.",
    "external-web": "URL of external authentication web server.",
    "external-web-format": "URL query parameter detection (default = auto-detect).",
    "external-logout": "URL of external authentication logout server.",
    "mac-username-delimiter": "MAC authentication username delimiter (default = hyphen).",
    "mac-password-delimiter": "MAC authentication password delimiter (default = hyphen).",
    "mac-calling-station-delimiter": "MAC calling station delimiter (default = hyphen).",
    "mac-called-station-delimiter": "MAC called station delimiter (default = hyphen).",
    "mac-case": "MAC case (default = uppercase).",
    "called-station-id-type": "The format type of RADIUS attribute Called-Station-Id (default = mac).",
    "mac-auth-bypass": "Enable/disable MAC authentication bypass.",
    "radius-mac-auth": "Enable/disable RADIUS-based MAC authentication of clients (default = disable).",
    "radius-mac-auth-server": "RADIUS-based MAC authentication server.",
    "radius-mac-auth-block-interval": "Don't send RADIUS MAC auth request again if the client has been rejected within specific interval (0 or 30 - 864000 seconds, default = 0, 0 to disable blocking).",
    "radius-mac-mpsk-auth": "Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication (default = disable).",
    "radius-mac-mpsk-timeout": "RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000, default = 86400, 0 to disable caching).",
    "radius-mac-auth-usergroups": "Selective user groups that are permitted for RADIUS mac authentication.",
    "auth": "Authentication protocol.",
    "encrypt": "Encryption protocol to use (only available when security is set to a WPA type).",
    "keyindex": "WEP key index (1 - 4).",
    "key": "WEP Key.",
    "passphrase": "WPA pre-shared key (PSK) to be used to authenticate WiFi users.",
    "sae-password": "WPA3 SAE password to be used to authenticate WiFi users.",
    "sae-h2e-only": "Use hash-to-element-only mechanism for PWE derivation (default = disable).",
    "sae-hnp-only": "Use hunting-and-pecking-only mechanism for PWE derivation (default = disable).",
    "sae-pk": "Enable/disable WPA3 SAE-PK (default = disable).",
    "sae-private-key": "Private key used for WPA3 SAE-PK authentication.",
    "akm24-only": "WPA3 SAE using group-dependent hash only (default = disable).",
    "radius-server": "RADIUS server to be used to authenticate WiFi users.",
    "nas-filter-rule": "Enable/disable NAS filter rule support (default = disable).",
    "domain-name-stripping": "Enable/disable stripping domain name from identity (default = disable).",
    "mlo": "Enable/disable WiFi7 Multi-Link-Operation (default = disable).",
    "local-standalone": "Enable/disable AP local standalone (default = disable).",
    "local-standalone-nat": "Enable/disable AP local standalone NAT mode.",
    "ip": "IP address and subnet mask for the local standalone NAT subnet.",
    "dhcp-lease-time": "DHCP lease time in seconds for NAT IP address.",
    "local-standalone-dns": "Enable/disable AP local standalone DNS.",
    "local-standalone-dns-ip": "IPv4 addresses for the local standalone DNS.",
    "local-lan-partition": "Enable/disable segregating client traffic to local LAN side (default = disable).",
    "local-bridging": "Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP (default = disable).",
    "local-lan": "Allow/deny traffic destined for a Class A, B, or C private IP address (default = allow).",
    "local-authentication": "Enable/disable AP local authentication.",
    "usergroup": "Firewall user group to be used to authenticate WiFi users.",
    "captive-portal": "Enable/disable captive portal.",
    "captive-network-assistant-bypass": "Enable/disable Captive Network Assistant bypass.",
    "portal-message-override-group": "Replacement message group for this VAP (only available when security is set to a captive portal type).",
    "portal-message-overrides": "Individual message overrides.",
    "portal-type": "Captive portal functionality. Configure how the captive portal authenticates users and whether it includes a disclaimer.",
    "selected-usergroups": "Selective user groups that are permitted to authenticate.",
    "security-exempt-list": "Optional security exempt list for captive portal authentication.",
    "security-redirect-url": "Optional URL for redirecting users after they pass captive portal authentication.",
    "auth-cert": "HTTPS server certificate.",
    "auth-portal-addr": "Address of captive portal.",
    "intra-vap-privacy": "Enable/disable blocking communication between clients on the same SSID (called intra-SSID privacy) (default = disable).",
    "schedule": "Firewall schedules for enabling this VAP on the FortiAP. This VAP will be enabled when at least one of the schedules is valid. Separate multiple schedule names with a space.",
    "ldpc": "VAP low-density parity-check (LDPC) coding configuration.",
    "high-efficiency": "Enable/disable 802.11ax high efficiency (default = enable).",
    "target-wake-time": "Enable/disable 802.11ax target wake time (default = enable).",
    "port-macauth": "Enable/disable LAN port MAC authentication (default = disable).",
    "port-macauth-timeout": "LAN port MAC authentication idle timeout value (default = 600 sec).",
    "port-macauth-reauth-timeout": "LAN port MAC authentication re-authentication timeout value (default = 7200 sec).",
    "bss-color-partial": "Enable/disable 802.11ax partial BSS color (default = enable).",
    "mpsk-profile": "MPSK profile name.",
    "split-tunneling": "Enable/disable split tunneling (default = disable).",
    "nac": "Enable/disable network access control.",
    "nac-profile": "NAC profile name.",
    "vlanid": "Optional VLAN ID.",
    "vlan-auto": "Enable/disable automatic management of SSID VLAN interface.",
    "dynamic-vlan": "Enable/disable dynamic VLAN assignment.",
    "captive-portal-fw-accounting": "Enable/disable RADIUS accounting for captive portal firewall authentication session.",
    "captive-portal-ac-name": "Local-bridging captive portal ac-name.",
    "captive-portal-auth-timeout": "Hard timeout - AP will always clear the session after timeout regardless of traffic (0 - 864000 sec, default = 0).",
    "multicast-rate": "Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0).",
    "multicast-enhance": "Enable/disable converting multicast to unicast to improve performance (default = disable).",
    "igmp-snooping": "Enable/disable IGMP snooping.",
    "dhcp-address-enforcement": "Enable/disable DHCP address enforcement (default = disable).",
    "broadcast-suppression": "Optional suppression of broadcast messages. For example, you can keep DHCP messages, ARP broadcasts, and so on off of the wireless network.",
    "ipv6-rules": "Optional rules of IPv6 packets. For example, you can keep RA, RS and so on off of the wireless network.",
    "me-disable-thresh": "Disable multicast enhancement when this many clients are receiving multicast traffic.",
    "mu-mimo": "Enable/disable Multi-user MIMO (default = enable).",
    "probe-resp-suppression": "Enable/disable probe response suppression (to ignore weak signals) (default = disable).",
    "probe-resp-threshold": "Minimum signal level/threshold in dBm required for the AP response to probe requests (-95 to -20, default = -80).",
    "radio-sensitivity": "Enable/disable software radio sensitivity (to ignore weak signals) (default = disable).",
    "quarantine": "Enable/disable station quarantine (default = disable).",
    "radio-5g-threshold": "Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band(-95 to -20, default = -76).",
    "radio-2g-threshold": "Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2.4G band (-95 to -20, default = -79).",
    "vlan-name": "Table for mapping VLAN name to VLAN ID.",
    "vlan-pooling": "Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools (default = disable). When set to wtp-group, VLAN pooling occurs with VLAN assignment by wtp-group.",
    "vlan-pool": "VLAN pool.",
    "dhcp-option43-insertion": "Enable/disable insertion of DHCP option 43 (default = enable).",
    "dhcp-option82-insertion": "Enable/disable DHCP option 82 insert (default = disable).",
    "dhcp-option82-circuit-id-insertion": "Enable/disable DHCP option 82 circuit-id insert (default = disable).",
    "dhcp-option82-remote-id-insertion": "Enable/disable DHCP option 82 remote-id insert (default = disable).",
    "ptk-rekey": "Enable/disable PTK rekey for WPA-Enterprise security.",
    "ptk-rekey-intv": "PTK rekey interval (600 - 864000 sec, default = 86400).",
    "gtk-rekey": "Enable/disable GTK rekey for WPA security.",
    "gtk-rekey-intv": "GTK rekey interval (600 - 864000 sec, default = 86400).",
    "eap-reauth": "Enable/disable EAP re-authentication for WPA-Enterprise security.",
    "eap-reauth-intv": "EAP re-authentication interval (1800 - 864000 sec, default = 86400).",
    "roaming-acct-interim-update": "Enable/disable using accounting interim update instead of accounting start/stop on roaming for WPA-Enterprise security.",
    "qos-profile": "Quality of service profile name.",
    "hotspot20-profile": "Hotspot 2.0 profile name.",
    "access-control-list": "Profile name for access-control-list.",
    "primary-wag-profile": "Primary wireless access gateway profile name.",
    "secondary-wag-profile": "Secondary wireless access gateway profile name.",
    "tunnel-echo-interval": "The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec, default = 300).",
    "tunnel-fallback-interval": "The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec, default = 7200).",
    "rates-11a": "Allowed data rates for 802.11a.",
    "rates-11bg": "Allowed data rates for 802.11b/g.",
    "rates-11n-ss12": "Allowed data rates for 802.11n with 1 or 2 spatial streams.",
    "rates-11n-ss34": "Allowed data rates for 802.11n with 3 or 4 spatial streams.",
    "rates-11ac-mcs-map": "Comma separated list of max supported VHT MCS for spatial streams 1 through 8.",
    "rates-11ax-mcs-map": "Comma separated list of max supported HE MCS for spatial streams 1 through 8.",
    "rates-11be-mcs-map": "Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 20MHz/40MHz/80MHz bandwidth.",
    "rates-11be-mcs-map-160": "Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 160MHz bandwidth.",
    "rates-11be-mcs-map-320": "Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 320MHz bandwidth.",
    "utm-profile": "UTM profile name.",
    "utm-status": "Enable to add one or more security profiles (AV, IPS, etc.) to the VAP.",
    "utm-log": "Enable/disable UTM logging.",
    "ips-sensor": "IPS sensor name.",
    "application-list": "Application control list name.",
    "antivirus-profile": "AntiVirus profile name.",
    "webfilter-profile": "WebFilter profile name.",
    "scan-botnet-connections": "Block or monitor connections to Botnet servers or disable Botnet scanning.",
    "address-group": "Firewall Address Group Name.",
    "address-group-policy": "Configure MAC address filtering policy for MAC addresses that are in the address-group.",
    "sticky-client-remove": "Enable/disable sticky client remove to maintain good signal level clients in SSID (default = disable).",
    "sticky-client-threshold-5g": "Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP (-95 to -20, default = -76).",
    "sticky-client-threshold-2g": "Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP (-95 to -20, default = -79).",
    "sticky-client-threshold-6g": "Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP (-95 to -20, default = -76).",
    "bstm-rssi-disassoc-timer": "Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI (0 to 2000, default = 200).",
    "bstm-load-balancing-disassoc-timer": "Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing (0 to 30, default = 10).",
    "bstm-disassociation-imminent": "Enable/disable forcing of disassociation after the BSTM request timer has been reached (default = enable).",
    "beacon-advertising": "Fortinet beacon advertising IE data   (default = empty).",
    "osen": "Enable/disable OSEN as part of key management (default = disable).",
    "application-detection-engine": "Enable/disable application detection engine (default = disable).",
    "application-dscp-marking": "Enable/disable application attribute based DSCP marking (default = disable).",
    "application-report-intv": "Application report interval (30 - 864000 sec, default = 120).",
    "l3-roaming": "Enable/disable layer 3 roaming (default = disable).",
    "l3-roaming-mode": "Select the way that layer 3 roaming traffic is passed (default = direct).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 15},
    "atf-weight": {"type": "integer", "min": 0, "max": 100},
    "max-clients": {"type": "integer", "min": 0, "max": 4294967295},
    "max-clients-ap": {"type": "integer", "min": 0, "max": 4294967295},
    "ssid": {"type": "string", "max_length": 32},
    "pmf-assoc-comeback-timeout": {"type": "integer", "min": 1, "max": 20},
    "pmf-sa-query-retry-timeout": {"type": "integer", "min": 1, "max": 5},
    "gas-comeback-delay": {"type": "integer", "min": 100, "max": 10000},
    "gas-fragmentation-limit": {"type": "integer", "min": 512, "max": 4096},
    "ft-mobility-domain": {"type": "integer", "min": 1, "max": 65535},
    "ft-r0-key-lifetime": {"type": "integer", "min": 1, "max": 65535},
    "owe-transition-ssid": {"type": "string", "max_length": 32},
    "external-logout": {"type": "string", "max_length": 127},
    "radius-mac-auth-server": {"type": "string", "max_length": 35},
    "radius-mac-auth-block-interval": {"type": "integer", "min": 30, "max": 864000},
    "radius-mac-mpsk-timeout": {"type": "integer", "min": 300, "max": 864000},
    "keyindex": {"type": "integer", "min": 1, "max": 4},
    "sae-private-key": {"type": "string", "max_length": 359},
    "radius-server": {"type": "string", "max_length": 35},
    "dhcp-lease-time": {"type": "integer", "min": 300, "max": 8640000},
    "portal-message-override-group": {"type": "string", "max_length": 35},
    "security-exempt-list": {"type": "string", "max_length": 35},
    "auth-cert": {"type": "string", "max_length": 35},
    "auth-portal-addr": {"type": "string", "max_length": 63},
    "port-macauth-timeout": {"type": "integer", "min": 60, "max": 65535},
    "port-macauth-reauth-timeout": {"type": "integer", "min": 120, "max": 65535},
    "mpsk-profile": {"type": "string", "max_length": 35},
    "nac-profile": {"type": "string", "max_length": 35},
    "vlanid": {"type": "integer", "min": 0, "max": 4094},
    "captive-portal-ac-name": {"type": "string", "max_length": 35},
    "captive-portal-auth-timeout": {"type": "integer", "min": 0, "max": 864000},
    "me-disable-thresh": {"type": "integer", "min": 2, "max": 256},
    "probe-resp-threshold": {"type": "string", "max_length": 7},
    "radio-5g-threshold": {"type": "string", "max_length": 7},
    "radio-2g-threshold": {"type": "string", "max_length": 7},
    "ptk-rekey-intv": {"type": "integer", "min": 600, "max": 864000},
    "gtk-rekey-intv": {"type": "integer", "min": 600, "max": 864000},
    "eap-reauth-intv": {"type": "integer", "min": 1800, "max": 864000},
    "qos-profile": {"type": "string", "max_length": 35},
    "hotspot20-profile": {"type": "string", "max_length": 35},
    "access-control-list": {"type": "string", "max_length": 35},
    "primary-wag-profile": {"type": "string", "max_length": 35},
    "secondary-wag-profile": {"type": "string", "max_length": 35},
    "tunnel-echo-interval": {"type": "integer", "min": 1, "max": 65535},
    "tunnel-fallback-interval": {"type": "integer", "min": 0, "max": 65535},
    "rates-11ac-mcs-map": {"type": "string", "max_length": 63},
    "rates-11ax-mcs-map": {"type": "string", "max_length": 63},
    "rates-11be-mcs-map": {"type": "string", "max_length": 15},
    "rates-11be-mcs-map-160": {"type": "string", "max_length": 15},
    "rates-11be-mcs-map-320": {"type": "string", "max_length": 15},
    "utm-profile": {"type": "string", "max_length": 35},
    "ips-sensor": {"type": "string", "max_length": 47},
    "application-list": {"type": "string", "max_length": 47},
    "antivirus-profile": {"type": "string", "max_length": 47},
    "webfilter-profile": {"type": "string", "max_length": 47},
    "address-group": {"type": "string", "max_length": 79},
    "sticky-client-threshold-5g": {"type": "string", "max_length": 7},
    "sticky-client-threshold-2g": {"type": "string", "max_length": 7},
    "sticky-client-threshold-6g": {"type": "string", "max_length": 7},
    "bstm-rssi-disassoc-timer": {"type": "integer", "min": 1, "max": 2000},
    "bstm-load-balancing-disassoc-timer": {"type": "integer", "min": 1, "max": 30},
    "application-report-intv": {"type": "integer", "min": 30, "max": 864000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "radius-mac-auth-usergroups": {
        "name": {
            "type": "string",
            "help": "User group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "usergroup": {
        "name": {
            "type": "string",
            "help": "User group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "portal-message-overrides": {
        "auth-disclaimer-page": {
            "type": "string",
            "help": "Override auth-disclaimer-page message with message from portal-message-overrides group.",
            "default": "",
            "max_length": 35,
        },
        "auth-reject-page": {
            "type": "string",
            "help": "Override auth-reject-page message with message from portal-message-overrides group.",
            "default": "",
            "max_length": 35,
        },
        "auth-login-page": {
            "type": "string",
            "help": "Override auth-login-page message with message from portal-message-overrides group.",
            "default": "",
            "max_length": 35,
        },
        "auth-login-failed-page": {
            "type": "string",
            "help": "Override auth-login-failed-page message with message from portal-message-overrides group.",
            "default": "",
            "max_length": 35,
        },
    },
    "selected-usergroups": {
        "name": {
            "type": "string",
            "help": "User group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "schedule": {
        "name": {
            "type": "string",
            "help": "Schedule name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
    "vlan-name": {
        "name": {
            "type": "string",
            "help": "VLAN name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "vlan-id": {
            "type": "integer",
            "help": "VLAN IDs (maximum 8 VLAN IDs).",
            "default": "",
            "min_value": 0,
            "max_value": 4094,
        },
    },
    "vlan-pool": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4094,
        },
        "wtp-group": {
            "type": "string",
            "help": "WTP group name.",
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PRE_AUTH = [
    "enable",  # Enable pre-authentication.
    "disable",  # Disable pre-authentication.
]
VALID_BODY_EXTERNAL_PRE_AUTH = [
    "enable",  # Enable pre-authentication with external APs.
    "disable",  # Disable pre-authentication with external APs.
]
VALID_BODY_MESH_BACKHAUL = [
    "enable",  # Enable mesh backhaul.
    "disable",  # Disable mesh backhaul.
]
VALID_BODY_BROADCAST_SSID = [
    "enable",  # Enable broadcasting the SSID.
    "disable",  # Disable broadcasting the SSID.
]
VALID_BODY_SECURITY = [
    "open",  # Open.
    "wep64",  # WEP 64-bit.
    "wep128",  # WEP 128-bit.
    "wpa-personal",  # WPA/WPA2 personal.
    "wpa-enterprise",  # WPA/WPA2 enterprise.
    "wpa-only-personal",  # WPA personal.
    "wpa-only-enterprise",  # WPA enterprise.
    "wpa2-only-personal",  # WPA2 personal.
    "wpa2-only-enterprise",  # WPA2 enterprise.
    "wpa3-enterprise",  # WPA3 enterprise with 192-bit encryption and PMF mandatory.
    "wpa3-only-enterprise",  # WPA3 enterprise with PMF mandatory.
    "wpa3-enterprise-transition",  # WPA3 enterprise with PMF optional.
    "wpa3-sae",  # WPA3 SAE.
    "wpa3-sae-transition",  # WPA3 SAE transition.
    "owe",  # Opportunistic wireless encryption.
    "osen",  # OSEN.
]
VALID_BODY_PMF = [
    "disable",  # Disable PMF completely.
    "enable",  # Enable PMF but deny clients without PMF.
    "optional",  # Enable PMF and allow clients without PMF.
]
VALID_BODY_BEACON_PROTECTION = [
    "disable",  # Disable beacon protection.
    "enable",  # Enable beacon protection.
]
VALID_BODY_OKC = [
    "disable",  # Disable Opportunistic Key Caching (OKC).
    "enable",  # Enable Opportunistic Key Caching (OKC).
]
VALID_BODY_MBO = [
    "disable",  # Disable Multiband Operation (MBO).
    "enable",  # Enable Multiband Operation (MBO).
]
VALID_BODY_MBO_CELL_DATA_CONN_PREF = [
    "excluded",  # Wi-Fi Agile Multiband AP does not want the Wi-Fi Agile Multiband STA to use the cellular data connection.
    "prefer-not",  # Wi-Fi Agile Multiband AP prefers the Wi-Fi Agile Multiband STA should not use cellular data connection.
    "prefer-use",  # Wi-Fi Agile Multiband AP prefers the Wi-Fi Agile Multiband STA should use cellular data connection.
]
VALID_BODY_80211K = [
    "disable",  # Disable 802.11k assisted roaming.
    "enable",  # Enable 802.11k assisted roaming.
]
VALID_BODY_80211V = [
    "disable",  # Disable 802.11v assisted roaming.
    "enable",  # Enable 802.11v assisted roaming.
]
VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND = [
    "disable",  # Disable dual-band neighbor report.
    "enable",  # Enable dual-band neighbor report.
]
VALID_BODY_FAST_BSS_TRANSITION = [
    "disable",  # Disable 802.11r Fast BSS Transition (FT).
    "enable",  # Enable 802.11r Fast BSS Transition (FT).
]
VALID_BODY_FT_OVER_DS = [
    "disable",  # Disable FT over the Distribution System (DS).
    "enable",  # Enable FT over the Distribution System (DS).
]
VALID_BODY_SAE_GROUPS = [
    "19",  # DH Group 19.
    "20",  # DH Group 20.
    "21",  # DH Group 21.
]
VALID_BODY_OWE_GROUPS = [
    "19",  # DH Group 19.
    "20",  # DH Group 20.
    "21",  # DH Group 21.
]
VALID_BODY_OWE_TRANSITION = [
    "disable",  # Disable OWE transition mode support.
    "enable",  # Enable OWE transition mode support.
]
VALID_BODY_ADDITIONAL_AKMS = [
    "akm6",  # Use AKM suite employing PSK_SHA256.
    "akm24",  # Use AKM suite employing SAE_EXT.
]
VALID_BODY_EAPOL_KEY_RETRIES = [
    "disable",  # Disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2).
    "enable",  # Enable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2).
]
VALID_BODY_TKIP_COUNTER_MEASURE = [
    "enable",  # Enable TKIP counter measure.
    "disable",  # Disable TKIP counter measure.
]
VALID_BODY_EXTERNAL_WEB_FORMAT = [
    "auto-detect",  # Automatically detect if "external-web" URL has any query parameter.
    "no-query-string",  # "external-web" URL does not have any query parameter.
    "partial-query-string",  # "external-web" URL has some query parameters.
]
VALID_BODY_MAC_USERNAME_DELIMITER = [
    "hyphen",  # Use hyphen as delimiter for MAC auth username.
    "single-hyphen",  # Use single hyphen as delimiter for MAC auth username.
    "colon",  # Use colon as delimiter for MAC auth username.
    "none",  # No delimiter for MAC auth username.
]
VALID_BODY_MAC_PASSWORD_DELIMITER = [
    "hyphen",  # Use hyphen as delimiter for MAC auth password.
    "single-hyphen",  # Use single hyphen as delimiter for MAC auth password.
    "colon",  # Use colon as delimiter for MAC auth password.
    "none",  # No delimiter for MAC auth password.
]
VALID_BODY_MAC_CALLING_STATION_DELIMITER = [
    "hyphen",  # Use hyphen as delimiter for calling station.
    "single-hyphen",  # Use single hyphen as delimiter for calling station.
    "colon",  # Use colon as delimiter for calling station.
    "none",  # No delimiter for calling station.
]
VALID_BODY_MAC_CALLED_STATION_DELIMITER = [
    "hyphen",  # Use hyphen as delimiter for called station.
    "single-hyphen",  # Use single hyphen as delimiter for called station.
    "colon",  # Use colon as delimiter for called station.
    "none",  # No delimiter for called station.
]
VALID_BODY_MAC_CASE = [
    "uppercase",  # Use uppercase MAC.
    "lowercase",  # Use lowercase MAC.
]
VALID_BODY_CALLED_STATION_ID_TYPE = [
    "mac",  # Use MAC:SSID format.
    "ip",  # Use IP:SSID format.
    "apname",  # Use APName:SSID format.
]
VALID_BODY_MAC_AUTH_BYPASS = [
    "enable",  # Enable MAC authentication bypass.
    "disable",  # Disable MAC authentication bypass.
]
VALID_BODY_RADIUS_MAC_AUTH = [
    "enable",  # Enable RADIUS-based MAC authentication.
    "disable",  # Disable RADIUS-based MAC authentication.
]
VALID_BODY_RADIUS_MAC_MPSK_AUTH = [
    "enable",  # Enable RADIUS-based MAC authentication for MPSK authentication.
    "disable",  # Disable RADIUS-based MAC authentication for MPSK authentication.
]
VALID_BODY_AUTH = [
    "radius",  # Use a RADIUS server to authenticate clients.
    "usergroup",  # Use a firewall usergroup to authenticate clients.
]
VALID_BODY_ENCRYPT = [
    "TKIP",  # Use TKIP encryption.
    "AES",  # Use AES encryption.
    "TKIP-AES",  # Use TKIP and AES encryption.
]
VALID_BODY_SAE_H2E_ONLY = [
    "enable",  # Enable WPA3 SAE-H2E-only.
    "disable",  # Disable WPA3 SAE-H2E-only.
]
VALID_BODY_SAE_HNP_ONLY = [
    "enable",  # Enable WPA3 SAE-HNP-only.
    "disable",  # Disable WPA3 SAE-HNP-only.
]
VALID_BODY_SAE_PK = [
    "enable",  # Enable WPA3 SAE-PK.
    "disable",  # Disable WPA3 SAE-PK.
]
VALID_BODY_AKM24_ONLY = [
    "disable",  # Disable WPA3 SAE using group-dependent hash only.
    "enable",  # Enable WPA3 SAE using group-dependent hash only.
]
VALID_BODY_NAS_FILTER_RULE = [
    "enable",  # Enable NAS filter rule for RADIUS server.
    "disable",  # Disable NAS filter rule for RADIUS server.
]
VALID_BODY_DOMAIN_NAME_STRIPPING = [
    "disable",  # Disable stripping domain name from identity.
    "enable",  # Enable stripping domain name from identity.
]
VALID_BODY_MLO = [
    "disable",  # Disable WiFi7 Multi-Link-Operation.
    "enable",  # Enable WiFi7 Multi-Link-Operation.
]
VALID_BODY_LOCAL_STANDALONE = [
    "enable",  # Enable AP local standalone.
    "disable",  # Disable AP local standalone.
]
VALID_BODY_LOCAL_STANDALONE_NAT = [
    "enable",  # Enable AP local standalone NAT mode.
    "disable",  # Disable AP local standalone NAT mode.
]
VALID_BODY_LOCAL_STANDALONE_DNS = [
    "enable",  # Enable AP local standalone DNS.
    "disable",  # Disable AP local standalone DNS.
]
VALID_BODY_LOCAL_LAN_PARTITION = [
    "enable",  # Enable AP local LAN segregation.
    "disable",  # Disable AP local LAN segregation.
]
VALID_BODY_LOCAL_BRIDGING = [
    "enable",  # Enable AP local VAP to Ethernet bridging.
    "disable",  # Disable AP local VAP to Ethernet bridging.
]
VALID_BODY_LOCAL_LAN = [
    "allow",  # Allow traffic destined for a Class A, B, or C private IP address.
    "deny",  # Deny traffic destined for a Class A, B, or C private IP address.
]
VALID_BODY_LOCAL_AUTHENTICATION = [
    "enable",  # Enable AP local authentication.
    "disable",  # Disable AP local authentication.
]
VALID_BODY_CAPTIVE_PORTAL = [
    "enable",  # Enable captive portal.
    "disable",  # Disable captive portal.
]
VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS = [
    "enable",  # Enable captive bypass.
    "disable",  # Disable captive bypass.
]
VALID_BODY_PORTAL_TYPE = [
    "auth",  # Portal for authentication.
    "auth+disclaimer",  # Portal for authentication and disclaimer.
    "disclaimer",  # Portal for disclaimer.
    "email-collect",  # Portal for email collection.
    "cmcc",  # Portal for CMCC.
    "cmcc-macauth",  # Portal for CMCC and MAC authentication.
    "auth-mac",  # Portal for authentication and MAC authentication.
    "external-auth",  # Portal for external portal authentication.
    "external-macauth",  # Portal for external portal MAC authentication.
]
VALID_BODY_INTRA_VAP_PRIVACY = [
    "enable",  # Enable intra-SSID privacy.
    "disable",  # Disable intra-SSID privacy.
]
VALID_BODY_LDPC = [
    "disable",  # Disable LDPC.
    "rx",  # Enable LDPC when receiving traffic.
    "tx",  # Enable LDPC when transmitting traffic.
    "rxtx",  # Enable LDPC when both receiving and transmitting traffic.
]
VALID_BODY_HIGH_EFFICIENCY = [
    "enable",  # Enable 802.11ax high efficiency.
    "disable",  # Disable 802.11ax high efficiency.
]
VALID_BODY_TARGET_WAKE_TIME = [
    "enable",  # Enable 802.11ax target wake time.
    "disable",  # Disable 802.11ax target wake time.
]
VALID_BODY_PORT_MACAUTH = [
    "disable",  # Disable LAN port MAC authentication.
    "radius",  # Enable LAN port RADIUS-based MAC authentication.
    "address-group",  # Enable LAN port address-group based MAC authentication.
]
VALID_BODY_BSS_COLOR_PARTIAL = [
    "enable",  # Enable 802.11ax partial BSS color.
    "disable",  # Disable 802.11ax partial BSS color.
]
VALID_BODY_SPLIT_TUNNELING = [
    "enable",  # Enable split tunneling.
    "disable",  # Disable split tunneling.
]
VALID_BODY_NAC = [
    "enable",  # Enable network access control.
    "disable",  # Disable network access control.
]
VALID_BODY_VLAN_AUTO = [
    "enable",  # Enable automatic management of SSID VLAN interface.
    "disable",  # Disable automatic management of SSID VLAN interface.
]
VALID_BODY_DYNAMIC_VLAN = [
    "enable",  # Enable dynamic VLAN assignment.
    "disable",  # Disable dynamic VLAN assignment.
]
VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING = [
    "enable",  # Enable RADIUS accounting for captive portal firewall authentication session.
    "disable",  # Disable RADIUS accounting for captive portal firewall authentication session.
]
VALID_BODY_MULTICAST_RATE = [
    "0",  # Use the default multicast rate.
    "6000",  # 6 Mbps.
    "12000",  # 12 Mbps.
    "24000",  # 24 Mbps.
]
VALID_BODY_MULTICAST_ENHANCE = [
    "enable",  # Enable multicast enhancement.
    "disable",  # Disable multicast enhancement.
]
VALID_BODY_IGMP_SNOOPING = [
    "enable",  # Enable IGMP snooping.
    "disable",  # Disable IGMP snooping.
]
VALID_BODY_DHCP_ADDRESS_ENFORCEMENT = [
    "enable",  # Enable DHCP enforcement, data from clients that have not completed the DHCP process will be blocked.
    "disable",  # Disable DHCP enforcement, clients can access the network without DHCP process.
]
VALID_BODY_BROADCAST_SUPPRESSION = [
    "dhcp-up",  # Suppress broadcast uplink DHCP messages.
    "dhcp-down",  # Suppress broadcast downlink DHCP messages.
    "dhcp-starvation",  # Suppress broadcast DHCP starvation req messages.
    "dhcp-ucast",  # Convert downlink broadcast DHCP messages to unicast messages.
    "arp-known",  # Suppress broadcast ARP for known wireless clients.
    "arp-unknown",  # Suppress broadcast ARP for unknown wireless clients.
    "arp-reply",  # Suppress broadcast ARP reply from wireless clients.
    "arp-poison",  # Suppress ARP poison messages from wireless clients.
    "arp-proxy",  # Reply ARP requests for wireless clients as a proxy.
    "netbios-ns",  # Suppress NetBIOS name services packets with UDP port 137.
    "netbios-ds",  # Suppress NetBIOS datagram services packets with UDP port 138.
    "ipv6",  # Suppress IPv6 packets.
    "all-other-mc",  # Suppress all other multicast messages.
    "all-other-bc",  # Suppress all other broadcast messages.
]
VALID_BODY_IPV6_RULES = [
    "drop-icmp6ra",  # Drop ICMP6 Router Advertisement (RA) packets that originate from wireless clients.
    "drop-icmp6rs",  # Drop ICMP6 Router Solicitation (RS) packets to be sent to wireless clients.
    "drop-llmnr6",  # Drop Link-Local Multicast Name Resolution (LLMNR) packets
    "drop-icmp6mld2",  # Drop ICMP6 Multicast Listener Report V2 (MLD2) packets
    "drop-dhcp6s",  # Drop DHCP6 server generated packets that originate from wireless clients.
    "drop-dhcp6c",  # Drop DHCP6 client generated packets to be sent to wireless clients.
    "ndp-proxy",  # Enable IPv6 ndp proxy - send back na on behalf of the client and drop the ns.
    "drop-ns-dad",  # Drop ICMP6 NS-DAD when target address is not found in ndp proxy cache.
    "drop-ns-nondad",  # Drop ICMP6 NS-NonDAD when target address is not found in ndp proxy cache.
]
VALID_BODY_MU_MIMO = [
    "enable",  # Enable Multi-user MIMO.
    "disable",  # Disable Multi-user MIMO.
]
VALID_BODY_PROBE_RESP_SUPPRESSION = [
    "enable",  # Enable probe response suppression.
    "disable",  # Disable probe response suppression.
]
VALID_BODY_RADIO_SENSITIVITY = [
    "enable",  # Enable software radio sensitivity.
    "disable",  # Disable software radio sensitivity.
]
VALID_BODY_QUARANTINE = [
    "enable",  # Enable station quarantine.
    "disable",  # Disable station quarantine.
]
VALID_BODY_VLAN_POOLING = [
    "wtp-group",  # Enable VLAN pooling with VLAN assignment by wtp-group.
    "round-robin",  # Enable VLAN pooling with round-robin VLAN assignment.
    "hash",  # Enable VLAN pooling with hash-based VLAN assignment.
    "disable",  # Disable VLAN pooling.
]
VALID_BODY_DHCP_OPTION43_INSERTION = [
    "enable",  # Enable insertion of DHCP option 43.
    "disable",  # Disable insertion of DHCP option 43.
]
VALID_BODY_DHCP_OPTION82_INSERTION = [
    "enable",  # Enable DHCP option 82 insert.
    "disable",  # Disable DHCP option 82 insert.
]
VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION = [
    "style-1",  # ASCII string composed of AP-MAC;SSID;SSID-TYPE. For example, "xx:xx:xx:xx:xx:xx;wifi;s".
    "style-2",  # ASCII string composed of AP-MAC. For example, "xx:xx:xx:xx:xx:xx".
    "style-3",  # ASCII string composed of NETWORK-TYPE:WTPPROF-NAME:VLAN:SSID:AP-MODEL:AP-HOSTNAME:AP-MAC. For example,"WLAN:FAPS221E-default:100:wifi:PS221E:FortiAP-S221E:xx:xx:xx:xx:xx:xx".
    "disable",  # Disable DHCP option 82 circuit-id insert.
]
VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION = [
    "style-1",  # ASCII string in the format "xx:xx:xx:xx:xx:xx" containing MAC address of client device.
    "disable",  # Disable DHCP option 82 remote-id insert.
]
VALID_BODY_PTK_REKEY = [
    "enable",  # Enable PTK rekey for WPA-Enterprise security.
    "disable",  # Disable PTK rekey for WPA-Enterprise security.
]
VALID_BODY_GTK_REKEY = [
    "enable",  # Enable GTK rekey for WPA security.
    "disable",  # Disable GTK rekey for WPA security.
]
VALID_BODY_EAP_REAUTH = [
    "enable",  # Enable EAP re-authentication for WPA-Enterprise security.
    "disable",  # Disable EAP re-authentication for WPA-Enterprise security.
]
VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE = [
    "enable",  # Enable using accounting interim update on roaming for WPA-Enterprise security.
    "disable",  # Disable using accounting interim update on roaming for WPA-Enterprise security.
]
VALID_BODY_RATES_11A = [
    "6",  # 6 Mbps supported rate.
    "6-basic",  # 6 Mbps BSS basic rate.
    "9",  # 9 Mbps supported rate.
    "9-basic",  # 9 Mbps BSS basic rate.
    "12",  # 12 Mbps supported rate.
    "12-basic",  # 12 Mbps BSS basic rate.
    "18",  # 18 Mbps supported rate.
    "18-basic",  # 18 Mbps BSS basic rate.
    "24",  # 24 Mbps supported rate.
    "24-basic",  # 24 Mbps BSS basic rate.
    "36",  # 36 Mbps supported rate.
    "36-basic",  # 36 Mbps BSS basic rate.
    "48",  # 48 Mbps supported rate.
    "48-basic",  # 48 Mbps BSS basic rate.
    "54",  # 54 Mbps supported rate.
    "54-basic",  # 54 Mbps BSS basic rate.
]
VALID_BODY_RATES_11BG = [
    "1",  # 1 Mbps supported rate.
    "1-basic",  # 1 Mbps BSS basic rate.
    "2",  # 2 Mbps supported rate.
    "2-basic",  # 2 Mbps BSS basic rate.
    "5.5",  # 5.5 Mbps supported rate.
    "5.5-basic",  # 5.5 Mbps BSS basic rate.
    "11",  # 11 Mbps supported rate.
    "11-basic",  # 11 Mbps BSS basic rate.
    "6",  # 6 Mbps supported rate.
    "6-basic",  # 6 Mbps BSS basic rate.
    "9",  # 9 Mbps supported rate.
    "9-basic",  # 9 Mbps BSS basic rate.
    "12",  # 12 Mbps supported rate.
    "12-basic",  # 12 Mbps BSS basic rate.
    "18",  # 18 Mbps supported rate.
    "18-basic",  # 18 Mbps BSS basic rate.
    "24",  # 24 Mbps supported rate.
    "24-basic",  # 24 Mbps BSS basic rate.
    "36",  # 36 Mbps supported rate.
    "36-basic",  # 36 Mbps BSS basic rate.
    "48",  # 48 Mbps supported rate.
    "48-basic",  # 48 Mbps BSS basic rate.
    "54",  # 54 Mbps supported rate.
    "54-basic",  # 54 Mbps BSS basic rate.
]
VALID_BODY_RATES_11N_SS12 = [
    "mcs0/1",  # Data rate for MCS index 0 with 1 spatial stream.
    "mcs1/1",  # Data rate for MCS index 1 with 1 spatial stream.
    "mcs2/1",  # Data rate for MCS index 2 with 1 spatial stream.
    "mcs3/1",  # Data rate for MCS index 3 with 1 spatial stream.
    "mcs4/1",  # Data rate for MCS index 4 with 1 spatial stream.
    "mcs5/1",  # Data rate for MCS index 5 with 1 spatial stream.
    "mcs6/1",  # Data rate for MCS index 6 with 1 spatial stream.
    "mcs7/1",  # Data rate for MCS index 7 with 1 spatial stream.
    "mcs8/2",  # Data rate for MCS index 8 with 2 spatial streams.
    "mcs9/2",  # Data rate for MCS index 9 with 2 spatial streams.
    "mcs10/2",  # Data rate for MCS index 10 with 2 spatial streams.
    "mcs11/2",  # Data rate for MCS index 11 with 2 spatial streams.
    "mcs12/2",  # Data rate for MCS index 12 with 2 spatial streams.
    "mcs13/2",  # Data rate for MCS index 13 with 2 spatial streams.
    "mcs14/2",  # Data rate for MCS index 14 with 2 spatial streams.
    "mcs15/2",  # Data rate for MCS index 15 with 2 spatial streams.
]
VALID_BODY_RATES_11N_SS34 = [
    "mcs16/3",  # Data rate for MCS index 16 with 3 spatial streams.
    "mcs17/3",  # Data rate for MCS index 17 with 3 spatial streams.
    "mcs18/3",  # Data rate for MCS index 18 with 3 spatial streams.
    "mcs19/3",  # Data rate for MCS index 19 with 3 spatial streams.
    "mcs20/3",  # Data rate for MCS index 20 with 3 spatial streams.
    "mcs21/3",  # Data rate for MCS index 21 with 3 spatial streams.
    "mcs22/3",  # Data rate for MCS index 22 with 3 spatial streams.
    "mcs23/3",  # Data rate for MCS index 23 with 3 spatial streams.
    "mcs24/4",  # Data rate for MCS index 24 with 4 spatial streams.
    "mcs25/4",  # Data rate for MCS index 25 with 4 spatial streams.
    "mcs26/4",  # Data rate for MCS index 26 with 4 spatial streams.
    "mcs27/4",  # Data rate for MCS index 27 with 4 spatial streams.
    "mcs28/4",  # Data rate for MCS index 28 with 4 spatial streams.
    "mcs29/4",  # Data rate for MCS index 29 with 4 spatial streams.
    "mcs30/4",  # Data rate for MCS index 30 with 4 spatial streams.
    "mcs31/4",  # Data rate for MCS index 31 with 4 spatial streams.
]
VALID_BODY_UTM_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_UTM_LOG = [
    "enable",  # Enable UTM logging.
    "disable",  # Disable UTM logging.
]
VALID_BODY_SCAN_BOTNET_CONNECTIONS = [
    "disable",  # Do not scan connections to botnet servers.
    "monitor",  # Log connections to botnet servers.
    "block",  # Block connections to botnet servers.
]
VALID_BODY_ADDRESS_GROUP_POLICY = [
    "disable",  # Disable MAC address filtering policy for MAC addresses that are in the address-group
    "allow",  # Allow clients with MAC addresses that are in the address-group.
    "deny",  # Block clients with MAC addresses that are in the address-group.
]
VALID_BODY_STICKY_CLIENT_REMOVE = [
    "enable",  # Enable sticky client remove.
    "disable",  # Disable sticky client remove.
]
VALID_BODY_BSTM_DISASSOCIATION_IMMINENT = [
    "enable",  # Enable BSTM disassociation imminent.
    "disable",  # Disable BSTM disassociation imminent.
]
VALID_BODY_BEACON_ADVERTISING = [
    "name",  # AP name.
    "model",  # AP model abbreviation.
    "serial-number",  # AP serial number.
]
VALID_BODY_OSEN = [
    "enable",  # Enable OSEN auth.
    "disable",  # Disable OSEN auth.
]
VALID_BODY_APPLICATION_DETECTION_ENGINE = [
    "enable",  # Enable application detection engine.
    "disable",  # Disable application detection engine.
]
VALID_BODY_APPLICATION_DSCP_MARKING = [
    "enable",  # Enable application based DSCP marking.
    "disable",  # Disable application based DSCP marking.
]
VALID_BODY_L3_ROAMING = [
    "enable",  # Enable layer 3 roaming.
    "disable",  # Disable layer 3 roaming.
]
VALID_BODY_L3_ROAMING_MODE = [
    "direct",  # Layer 3 roaming traffic is passed between home AP and guest AP directly.
    "indirect",  # Layer 3 roaming traffic is passed between home AP and guest AP through controllers.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_vap_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for wireless_controller/vap."""
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
    """Validate required fields for wireless_controller/vap."""
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


def validate_wireless_controller_vap_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new wireless_controller/vap object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "pre-auth" in payload:
        value = payload["pre-auth"]
        if value not in VALID_BODY_PRE_AUTH:
            desc = FIELD_DESCRIPTIONS.get("pre-auth", "")
            error_msg = f"Invalid value for 'pre-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRE_AUTH)}"
            error_msg += f"\n  → Example: pre-auth='{{ VALID_BODY_PRE_AUTH[0] }}'"
            return (False, error_msg)
    if "external-pre-auth" in payload:
        value = payload["external-pre-auth"]
        if value not in VALID_BODY_EXTERNAL_PRE_AUTH:
            desc = FIELD_DESCRIPTIONS.get("external-pre-auth", "")
            error_msg = f"Invalid value for 'external-pre-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTERNAL_PRE_AUTH)}"
            error_msg += f"\n  → Example: external-pre-auth='{{ VALID_BODY_EXTERNAL_PRE_AUTH[0] }}'"
            return (False, error_msg)
    if "mesh-backhaul" in payload:
        value = payload["mesh-backhaul"]
        if value not in VALID_BODY_MESH_BACKHAUL:
            desc = FIELD_DESCRIPTIONS.get("mesh-backhaul", "")
            error_msg = f"Invalid value for 'mesh-backhaul': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MESH_BACKHAUL)}"
            error_msg += f"\n  → Example: mesh-backhaul='{{ VALID_BODY_MESH_BACKHAUL[0] }}'"
            return (False, error_msg)
    if "broadcast-ssid" in payload:
        value = payload["broadcast-ssid"]
        if value not in VALID_BODY_BROADCAST_SSID:
            desc = FIELD_DESCRIPTIONS.get("broadcast-ssid", "")
            error_msg = f"Invalid value for 'broadcast-ssid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BROADCAST_SSID)}"
            error_msg += f"\n  → Example: broadcast-ssid='{{ VALID_BODY_BROADCAST_SSID[0] }}'"
            return (False, error_msg)
    if "security" in payload:
        value = payload["security"]
        if value not in VALID_BODY_SECURITY:
            desc = FIELD_DESCRIPTIONS.get("security", "")
            error_msg = f"Invalid value for 'security': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SECURITY)}"
            error_msg += f"\n  → Example: security='{{ VALID_BODY_SECURITY[0] }}'"
            return (False, error_msg)
    if "pmf" in payload:
        value = payload["pmf"]
        if value not in VALID_BODY_PMF:
            desc = FIELD_DESCRIPTIONS.get("pmf", "")
            error_msg = f"Invalid value for 'pmf': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PMF)}"
            error_msg += f"\n  → Example: pmf='{{ VALID_BODY_PMF[0] }}'"
            return (False, error_msg)
    if "beacon-protection" in payload:
        value = payload["beacon-protection"]
        if value not in VALID_BODY_BEACON_PROTECTION:
            desc = FIELD_DESCRIPTIONS.get("beacon-protection", "")
            error_msg = f"Invalid value for 'beacon-protection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BEACON_PROTECTION)}"
            error_msg += f"\n  → Example: beacon-protection='{{ VALID_BODY_BEACON_PROTECTION[0] }}'"
            return (False, error_msg)
    if "okc" in payload:
        value = payload["okc"]
        if value not in VALID_BODY_OKC:
            desc = FIELD_DESCRIPTIONS.get("okc", "")
            error_msg = f"Invalid value for 'okc': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OKC)}"
            error_msg += f"\n  → Example: okc='{{ VALID_BODY_OKC[0] }}'"
            return (False, error_msg)
    if "mbo" in payload:
        value = payload["mbo"]
        if value not in VALID_BODY_MBO:
            desc = FIELD_DESCRIPTIONS.get("mbo", "")
            error_msg = f"Invalid value for 'mbo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MBO)}"
            error_msg += f"\n  → Example: mbo='{{ VALID_BODY_MBO[0] }}'"
            return (False, error_msg)
    if "mbo-cell-data-conn-pref" in payload:
        value = payload["mbo-cell-data-conn-pref"]
        if value not in VALID_BODY_MBO_CELL_DATA_CONN_PREF:
            desc = FIELD_DESCRIPTIONS.get("mbo-cell-data-conn-pref", "")
            error_msg = f"Invalid value for 'mbo-cell-data-conn-pref': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MBO_CELL_DATA_CONN_PREF)}"
            error_msg += f"\n  → Example: mbo-cell-data-conn-pref='{{ VALID_BODY_MBO_CELL_DATA_CONN_PREF[0] }}'"
            return (False, error_msg)
    if "80211k" in payload:
        value = payload["80211k"]
        if value not in VALID_BODY_80211K:
            desc = FIELD_DESCRIPTIONS.get("80211k", "")
            error_msg = f"Invalid value for '80211k': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_80211K)}"
            error_msg += f"\n  → Example: 80211k='{{ VALID_BODY_80211K[0] }}'"
            return (False, error_msg)
    if "80211v" in payload:
        value = payload["80211v"]
        if value not in VALID_BODY_80211V:
            desc = FIELD_DESCRIPTIONS.get("80211v", "")
            error_msg = f"Invalid value for '80211v': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_80211V)}"
            error_msg += f"\n  → Example: 80211v='{{ VALID_BODY_80211V[0] }}'"
            return (False, error_msg)
    if "neighbor-report-dual-band" in payload:
        value = payload["neighbor-report-dual-band"]
        if value not in VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND:
            desc = FIELD_DESCRIPTIONS.get("neighbor-report-dual-band", "")
            error_msg = f"Invalid value for 'neighbor-report-dual-band': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND)}"
            error_msg += f"\n  → Example: neighbor-report-dual-band='{{ VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND[0] }}'"
            return (False, error_msg)
    if "fast-bss-transition" in payload:
        value = payload["fast-bss-transition"]
        if value not in VALID_BODY_FAST_BSS_TRANSITION:
            desc = FIELD_DESCRIPTIONS.get("fast-bss-transition", "")
            error_msg = f"Invalid value for 'fast-bss-transition': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAST_BSS_TRANSITION)}"
            error_msg += f"\n  → Example: fast-bss-transition='{{ VALID_BODY_FAST_BSS_TRANSITION[0] }}'"
            return (False, error_msg)
    if "ft-over-ds" in payload:
        value = payload["ft-over-ds"]
        if value not in VALID_BODY_FT_OVER_DS:
            desc = FIELD_DESCRIPTIONS.get("ft-over-ds", "")
            error_msg = f"Invalid value for 'ft-over-ds': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FT_OVER_DS)}"
            error_msg += f"\n  → Example: ft-over-ds='{{ VALID_BODY_FT_OVER_DS[0] }}'"
            return (False, error_msg)
    if "sae-groups" in payload:
        value = payload["sae-groups"]
        if value not in VALID_BODY_SAE_GROUPS:
            desc = FIELD_DESCRIPTIONS.get("sae-groups", "")
            error_msg = f"Invalid value for 'sae-groups': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAE_GROUPS)}"
            error_msg += f"\n  → Example: sae-groups='{{ VALID_BODY_SAE_GROUPS[0] }}'"
            return (False, error_msg)
    if "owe-groups" in payload:
        value = payload["owe-groups"]
        if value not in VALID_BODY_OWE_GROUPS:
            desc = FIELD_DESCRIPTIONS.get("owe-groups", "")
            error_msg = f"Invalid value for 'owe-groups': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OWE_GROUPS)}"
            error_msg += f"\n  → Example: owe-groups='{{ VALID_BODY_OWE_GROUPS[0] }}'"
            return (False, error_msg)
    if "owe-transition" in payload:
        value = payload["owe-transition"]
        if value not in VALID_BODY_OWE_TRANSITION:
            desc = FIELD_DESCRIPTIONS.get("owe-transition", "")
            error_msg = f"Invalid value for 'owe-transition': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OWE_TRANSITION)}"
            error_msg += f"\n  → Example: owe-transition='{{ VALID_BODY_OWE_TRANSITION[0] }}'"
            return (False, error_msg)
    if "additional-akms" in payload:
        value = payload["additional-akms"]
        if value not in VALID_BODY_ADDITIONAL_AKMS:
            desc = FIELD_DESCRIPTIONS.get("additional-akms", "")
            error_msg = f"Invalid value for 'additional-akms': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDITIONAL_AKMS)}"
            error_msg += f"\n  → Example: additional-akms='{{ VALID_BODY_ADDITIONAL_AKMS[0] }}'"
            return (False, error_msg)
    if "eapol-key-retries" in payload:
        value = payload["eapol-key-retries"]
        if value not in VALID_BODY_EAPOL_KEY_RETRIES:
            desc = FIELD_DESCRIPTIONS.get("eapol-key-retries", "")
            error_msg = f"Invalid value for 'eapol-key-retries': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_KEY_RETRIES)}"
            error_msg += f"\n  → Example: eapol-key-retries='{{ VALID_BODY_EAPOL_KEY_RETRIES[0] }}'"
            return (False, error_msg)
    if "tkip-counter-measure" in payload:
        value = payload["tkip-counter-measure"]
        if value not in VALID_BODY_TKIP_COUNTER_MEASURE:
            desc = FIELD_DESCRIPTIONS.get("tkip-counter-measure", "")
            error_msg = f"Invalid value for 'tkip-counter-measure': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TKIP_COUNTER_MEASURE)}"
            error_msg += f"\n  → Example: tkip-counter-measure='{{ VALID_BODY_TKIP_COUNTER_MEASURE[0] }}'"
            return (False, error_msg)
    if "external-web-format" in payload:
        value = payload["external-web-format"]
        if value not in VALID_BODY_EXTERNAL_WEB_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("external-web-format", "")
            error_msg = f"Invalid value for 'external-web-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTERNAL_WEB_FORMAT)}"
            error_msg += f"\n  → Example: external-web-format='{{ VALID_BODY_EXTERNAL_WEB_FORMAT[0] }}'"
            return (False, error_msg)
    if "mac-username-delimiter" in payload:
        value = payload["mac-username-delimiter"]
        if value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("mac-username-delimiter", "")
            error_msg = f"Invalid value for 'mac-username-delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_USERNAME_DELIMITER)}"
            error_msg += f"\n  → Example: mac-username-delimiter='{{ VALID_BODY_MAC_USERNAME_DELIMITER[0] }}'"
            return (False, error_msg)
    if "mac-password-delimiter" in payload:
        value = payload["mac-password-delimiter"]
        if value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("mac-password-delimiter", "")
            error_msg = f"Invalid value for 'mac-password-delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_PASSWORD_DELIMITER)}"
            error_msg += f"\n  → Example: mac-password-delimiter='{{ VALID_BODY_MAC_PASSWORD_DELIMITER[0] }}'"
            return (False, error_msg)
    if "mac-calling-station-delimiter" in payload:
        value = payload["mac-calling-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLING_STATION_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("mac-calling-station-delimiter", "")
            error_msg = f"Invalid value for 'mac-calling-station-delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_CALLING_STATION_DELIMITER)}"
            error_msg += f"\n  → Example: mac-calling-station-delimiter='{{ VALID_BODY_MAC_CALLING_STATION_DELIMITER[0] }}'"
            return (False, error_msg)
    if "mac-called-station-delimiter" in payload:
        value = payload["mac-called-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLED_STATION_DELIMITER:
            desc = FIELD_DESCRIPTIONS.get("mac-called-station-delimiter", "")
            error_msg = f"Invalid value for 'mac-called-station-delimiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_CALLED_STATION_DELIMITER)}"
            error_msg += f"\n  → Example: mac-called-station-delimiter='{{ VALID_BODY_MAC_CALLED_STATION_DELIMITER[0] }}'"
            return (False, error_msg)
    if "mac-case" in payload:
        value = payload["mac-case"]
        if value not in VALID_BODY_MAC_CASE:
            desc = FIELD_DESCRIPTIONS.get("mac-case", "")
            error_msg = f"Invalid value for 'mac-case': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_CASE)}"
            error_msg += f"\n  → Example: mac-case='{{ VALID_BODY_MAC_CASE[0] }}'"
            return (False, error_msg)
    if "called-station-id-type" in payload:
        value = payload["called-station-id-type"]
        if value not in VALID_BODY_CALLED_STATION_ID_TYPE:
            desc = FIELD_DESCRIPTIONS.get("called-station-id-type", "")
            error_msg = f"Invalid value for 'called-station-id-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CALLED_STATION_ID_TYPE)}"
            error_msg += f"\n  → Example: called-station-id-type='{{ VALID_BODY_CALLED_STATION_ID_TYPE[0] }}'"
            return (False, error_msg)
    if "mac-auth-bypass" in payload:
        value = payload["mac-auth-bypass"]
        if value not in VALID_BODY_MAC_AUTH_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("mac-auth-bypass", "")
            error_msg = f"Invalid value for 'mac-auth-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MAC_AUTH_BYPASS)}"
            error_msg += f"\n  → Example: mac-auth-bypass='{{ VALID_BODY_MAC_AUTH_BYPASS[0] }}'"
            return (False, error_msg)
    if "radius-mac-auth" in payload:
        value = payload["radius-mac-auth"]
        if value not in VALID_BODY_RADIUS_MAC_AUTH:
            desc = FIELD_DESCRIPTIONS.get("radius-mac-auth", "")
            error_msg = f"Invalid value for 'radius-mac-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_MAC_AUTH)}"
            error_msg += f"\n  → Example: radius-mac-auth='{{ VALID_BODY_RADIUS_MAC_AUTH[0] }}'"
            return (False, error_msg)
    if "radius-mac-mpsk-auth" in payload:
        value = payload["radius-mac-mpsk-auth"]
        if value not in VALID_BODY_RADIUS_MAC_MPSK_AUTH:
            desc = FIELD_DESCRIPTIONS.get("radius-mac-mpsk-auth", "")
            error_msg = f"Invalid value for 'radius-mac-mpsk-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIUS_MAC_MPSK_AUTH)}"
            error_msg += f"\n  → Example: radius-mac-mpsk-auth='{{ VALID_BODY_RADIUS_MAC_MPSK_AUTH[0] }}'"
            return (False, error_msg)
    if "auth" in payload:
        value = payload["auth"]
        if value not in VALID_BODY_AUTH:
            desc = FIELD_DESCRIPTIONS.get("auth", "")
            error_msg = f"Invalid value for 'auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH)}"
            error_msg += f"\n  → Example: auth='{{ VALID_BODY_AUTH[0] }}'"
            return (False, error_msg)
    if "encrypt" in payload:
        value = payload["encrypt"]
        if value not in VALID_BODY_ENCRYPT:
            desc = FIELD_DESCRIPTIONS.get("encrypt", "")
            error_msg = f"Invalid value for 'encrypt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENCRYPT)}"
            error_msg += f"\n  → Example: encrypt='{{ VALID_BODY_ENCRYPT[0] }}'"
            return (False, error_msg)
    if "sae-h2e-only" in payload:
        value = payload["sae-h2e-only"]
        if value not in VALID_BODY_SAE_H2E_ONLY:
            desc = FIELD_DESCRIPTIONS.get("sae-h2e-only", "")
            error_msg = f"Invalid value for 'sae-h2e-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAE_H2E_ONLY)}"
            error_msg += f"\n  → Example: sae-h2e-only='{{ VALID_BODY_SAE_H2E_ONLY[0] }}'"
            return (False, error_msg)
    if "sae-hnp-only" in payload:
        value = payload["sae-hnp-only"]
        if value not in VALID_BODY_SAE_HNP_ONLY:
            desc = FIELD_DESCRIPTIONS.get("sae-hnp-only", "")
            error_msg = f"Invalid value for 'sae-hnp-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAE_HNP_ONLY)}"
            error_msg += f"\n  → Example: sae-hnp-only='{{ VALID_BODY_SAE_HNP_ONLY[0] }}'"
            return (False, error_msg)
    if "sae-pk" in payload:
        value = payload["sae-pk"]
        if value not in VALID_BODY_SAE_PK:
            desc = FIELD_DESCRIPTIONS.get("sae-pk", "")
            error_msg = f"Invalid value for 'sae-pk': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SAE_PK)}"
            error_msg += f"\n  → Example: sae-pk='{{ VALID_BODY_SAE_PK[0] }}'"
            return (False, error_msg)
    if "akm24-only" in payload:
        value = payload["akm24-only"]
        if value not in VALID_BODY_AKM24_ONLY:
            desc = FIELD_DESCRIPTIONS.get("akm24-only", "")
            error_msg = f"Invalid value for 'akm24-only': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AKM24_ONLY)}"
            error_msg += f"\n  → Example: akm24-only='{{ VALID_BODY_AKM24_ONLY[0] }}'"
            return (False, error_msg)
    if "nas-filter-rule" in payload:
        value = payload["nas-filter-rule"]
        if value not in VALID_BODY_NAS_FILTER_RULE:
            desc = FIELD_DESCRIPTIONS.get("nas-filter-rule", "")
            error_msg = f"Invalid value for 'nas-filter-rule': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAS_FILTER_RULE)}"
            error_msg += f"\n  → Example: nas-filter-rule='{{ VALID_BODY_NAS_FILTER_RULE[0] }}'"
            return (False, error_msg)
    if "domain-name-stripping" in payload:
        value = payload["domain-name-stripping"]
        if value not in VALID_BODY_DOMAIN_NAME_STRIPPING:
            desc = FIELD_DESCRIPTIONS.get("domain-name-stripping", "")
            error_msg = f"Invalid value for 'domain-name-stripping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DOMAIN_NAME_STRIPPING)}"
            error_msg += f"\n  → Example: domain-name-stripping='{{ VALID_BODY_DOMAIN_NAME_STRIPPING[0] }}'"
            return (False, error_msg)
    if "mlo" in payload:
        value = payload["mlo"]
        if value not in VALID_BODY_MLO:
            desc = FIELD_DESCRIPTIONS.get("mlo", "")
            error_msg = f"Invalid value for 'mlo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MLO)}"
            error_msg += f"\n  → Example: mlo='{{ VALID_BODY_MLO[0] }}'"
            return (False, error_msg)
    if "local-standalone" in payload:
        value = payload["local-standalone"]
        if value not in VALID_BODY_LOCAL_STANDALONE:
            desc = FIELD_DESCRIPTIONS.get("local-standalone", "")
            error_msg = f"Invalid value for 'local-standalone': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_STANDALONE)}"
            error_msg += f"\n  → Example: local-standalone='{{ VALID_BODY_LOCAL_STANDALONE[0] }}'"
            return (False, error_msg)
    if "local-standalone-nat" in payload:
        value = payload["local-standalone-nat"]
        if value not in VALID_BODY_LOCAL_STANDALONE_NAT:
            desc = FIELD_DESCRIPTIONS.get("local-standalone-nat", "")
            error_msg = f"Invalid value for 'local-standalone-nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_STANDALONE_NAT)}"
            error_msg += f"\n  → Example: local-standalone-nat='{{ VALID_BODY_LOCAL_STANDALONE_NAT[0] }}'"
            return (False, error_msg)
    if "local-standalone-dns" in payload:
        value = payload["local-standalone-dns"]
        if value not in VALID_BODY_LOCAL_STANDALONE_DNS:
            desc = FIELD_DESCRIPTIONS.get("local-standalone-dns", "")
            error_msg = f"Invalid value for 'local-standalone-dns': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_STANDALONE_DNS)}"
            error_msg += f"\n  → Example: local-standalone-dns='{{ VALID_BODY_LOCAL_STANDALONE_DNS[0] }}'"
            return (False, error_msg)
    if "local-lan-partition" in payload:
        value = payload["local-lan-partition"]
        if value not in VALID_BODY_LOCAL_LAN_PARTITION:
            desc = FIELD_DESCRIPTIONS.get("local-lan-partition", "")
            error_msg = f"Invalid value for 'local-lan-partition': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_LAN_PARTITION)}"
            error_msg += f"\n  → Example: local-lan-partition='{{ VALID_BODY_LOCAL_LAN_PARTITION[0] }}'"
            return (False, error_msg)
    if "local-bridging" in payload:
        value = payload["local-bridging"]
        if value not in VALID_BODY_LOCAL_BRIDGING:
            desc = FIELD_DESCRIPTIONS.get("local-bridging", "")
            error_msg = f"Invalid value for 'local-bridging': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_BRIDGING)}"
            error_msg += f"\n  → Example: local-bridging='{{ VALID_BODY_LOCAL_BRIDGING[0] }}'"
            return (False, error_msg)
    if "local-lan" in payload:
        value = payload["local-lan"]
        if value not in VALID_BODY_LOCAL_LAN:
            desc = FIELD_DESCRIPTIONS.get("local-lan", "")
            error_msg = f"Invalid value for 'local-lan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_LAN)}"
            error_msg += f"\n  → Example: local-lan='{{ VALID_BODY_LOCAL_LAN[0] }}'"
            return (False, error_msg)
    if "local-authentication" in payload:
        value = payload["local-authentication"]
        if value not in VALID_BODY_LOCAL_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("local-authentication", "")
            error_msg = f"Invalid value for 'local-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOCAL_AUTHENTICATION)}"
            error_msg += f"\n  → Example: local-authentication='{{ VALID_BODY_LOCAL_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "captive-portal" in payload:
        value = payload["captive-portal"]
        if value not in VALID_BODY_CAPTIVE_PORTAL:
            desc = FIELD_DESCRIPTIONS.get("captive-portal", "")
            error_msg = f"Invalid value for 'captive-portal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTIVE_PORTAL)}"
            error_msg += f"\n  → Example: captive-portal='{{ VALID_BODY_CAPTIVE_PORTAL[0] }}'"
            return (False, error_msg)
    if "captive-network-assistant-bypass" in payload:
        value = payload["captive-network-assistant-bypass"]
        if value not in VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS:
            desc = FIELD_DESCRIPTIONS.get("captive-network-assistant-bypass", "")
            error_msg = f"Invalid value for 'captive-network-assistant-bypass': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS)}"
            error_msg += f"\n  → Example: captive-network-assistant-bypass='{{ VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS[0] }}'"
            return (False, error_msg)
    if "portal-type" in payload:
        value = payload["portal-type"]
        if value not in VALID_BODY_PORTAL_TYPE:
            desc = FIELD_DESCRIPTIONS.get("portal-type", "")
            error_msg = f"Invalid value for 'portal-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORTAL_TYPE)}"
            error_msg += f"\n  → Example: portal-type='{{ VALID_BODY_PORTAL_TYPE[0] }}'"
            return (False, error_msg)
    if "intra-vap-privacy" in payload:
        value = payload["intra-vap-privacy"]
        if value not in VALID_BODY_INTRA_VAP_PRIVACY:
            desc = FIELD_DESCRIPTIONS.get("intra-vap-privacy", "")
            error_msg = f"Invalid value for 'intra-vap-privacy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTRA_VAP_PRIVACY)}"
            error_msg += f"\n  → Example: intra-vap-privacy='{{ VALID_BODY_INTRA_VAP_PRIVACY[0] }}'"
            return (False, error_msg)
    if "ldpc" in payload:
        value = payload["ldpc"]
        if value not in VALID_BODY_LDPC:
            desc = FIELD_DESCRIPTIONS.get("ldpc", "")
            error_msg = f"Invalid value for 'ldpc': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LDPC)}"
            error_msg += f"\n  → Example: ldpc='{{ VALID_BODY_LDPC[0] }}'"
            return (False, error_msg)
    if "high-efficiency" in payload:
        value = payload["high-efficiency"]
        if value not in VALID_BODY_HIGH_EFFICIENCY:
            desc = FIELD_DESCRIPTIONS.get("high-efficiency", "")
            error_msg = f"Invalid value for 'high-efficiency': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HIGH_EFFICIENCY)}"
            error_msg += f"\n  → Example: high-efficiency='{{ VALID_BODY_HIGH_EFFICIENCY[0] }}'"
            return (False, error_msg)
    if "target-wake-time" in payload:
        value = payload["target-wake-time"]
        if value not in VALID_BODY_TARGET_WAKE_TIME:
            desc = FIELD_DESCRIPTIONS.get("target-wake-time", "")
            error_msg = f"Invalid value for 'target-wake-time': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TARGET_WAKE_TIME)}"
            error_msg += f"\n  → Example: target-wake-time='{{ VALID_BODY_TARGET_WAKE_TIME[0] }}'"
            return (False, error_msg)
    if "port-macauth" in payload:
        value = payload["port-macauth"]
        if value not in VALID_BODY_PORT_MACAUTH:
            desc = FIELD_DESCRIPTIONS.get("port-macauth", "")
            error_msg = f"Invalid value for 'port-macauth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PORT_MACAUTH)}"
            error_msg += f"\n  → Example: port-macauth='{{ VALID_BODY_PORT_MACAUTH[0] }}'"
            return (False, error_msg)
    if "bss-color-partial" in payload:
        value = payload["bss-color-partial"]
        if value not in VALID_BODY_BSS_COLOR_PARTIAL:
            desc = FIELD_DESCRIPTIONS.get("bss-color-partial", "")
            error_msg = f"Invalid value for 'bss-color-partial': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BSS_COLOR_PARTIAL)}"
            error_msg += f"\n  → Example: bss-color-partial='{{ VALID_BODY_BSS_COLOR_PARTIAL[0] }}'"
            return (False, error_msg)
    if "split-tunneling" in payload:
        value = payload["split-tunneling"]
        if value not in VALID_BODY_SPLIT_TUNNELING:
            desc = FIELD_DESCRIPTIONS.get("split-tunneling", "")
            error_msg = f"Invalid value for 'split-tunneling': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPLIT_TUNNELING)}"
            error_msg += f"\n  → Example: split-tunneling='{{ VALID_BODY_SPLIT_TUNNELING[0] }}'"
            return (False, error_msg)
    if "nac" in payload:
        value = payload["nac"]
        if value not in VALID_BODY_NAC:
            desc = FIELD_DESCRIPTIONS.get("nac", "")
            error_msg = f"Invalid value for 'nac': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NAC)}"
            error_msg += f"\n  → Example: nac='{{ VALID_BODY_NAC[0] }}'"
            return (False, error_msg)
    if "vlan-auto" in payload:
        value = payload["vlan-auto"]
        if value not in VALID_BODY_VLAN_AUTO:
            desc = FIELD_DESCRIPTIONS.get("vlan-auto", "")
            error_msg = f"Invalid value for 'vlan-auto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLAN_AUTO)}"
            error_msg += f"\n  → Example: vlan-auto='{{ VALID_BODY_VLAN_AUTO[0] }}'"
            return (False, error_msg)
    if "dynamic-vlan" in payload:
        value = payload["dynamic-vlan"]
        if value not in VALID_BODY_DYNAMIC_VLAN:
            desc = FIELD_DESCRIPTIONS.get("dynamic-vlan", "")
            error_msg = f"Invalid value for 'dynamic-vlan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DYNAMIC_VLAN)}"
            error_msg += f"\n  → Example: dynamic-vlan='{{ VALID_BODY_DYNAMIC_VLAN[0] }}'"
            return (False, error_msg)
    if "captive-portal-fw-accounting" in payload:
        value = payload["captive-portal-fw-accounting"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING:
            desc = FIELD_DESCRIPTIONS.get("captive-portal-fw-accounting", "")
            error_msg = f"Invalid value for 'captive-portal-fw-accounting': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING)}"
            error_msg += f"\n  → Example: captive-portal-fw-accounting='{{ VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING[0] }}'"
            return (False, error_msg)
    if "multicast-rate" in payload:
        value = payload["multicast-rate"]
        if value not in VALID_BODY_MULTICAST_RATE:
            desc = FIELD_DESCRIPTIONS.get("multicast-rate", "")
            error_msg = f"Invalid value for 'multicast-rate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_RATE)}"
            error_msg += f"\n  → Example: multicast-rate='{{ VALID_BODY_MULTICAST_RATE[0] }}'"
            return (False, error_msg)
    if "multicast-enhance" in payload:
        value = payload["multicast-enhance"]
        if value not in VALID_BODY_MULTICAST_ENHANCE:
            desc = FIELD_DESCRIPTIONS.get("multicast-enhance", "")
            error_msg = f"Invalid value for 'multicast-enhance': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTICAST_ENHANCE)}"
            error_msg += f"\n  → Example: multicast-enhance='{{ VALID_BODY_MULTICAST_ENHANCE[0] }}'"
            return (False, error_msg)
    if "igmp-snooping" in payload:
        value = payload["igmp-snooping"]
        if value not in VALID_BODY_IGMP_SNOOPING:
            desc = FIELD_DESCRIPTIONS.get("igmp-snooping", "")
            error_msg = f"Invalid value for 'igmp-snooping': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IGMP_SNOOPING)}"
            error_msg += f"\n  → Example: igmp-snooping='{{ VALID_BODY_IGMP_SNOOPING[0] }}'"
            return (False, error_msg)
    if "dhcp-address-enforcement" in payload:
        value = payload["dhcp-address-enforcement"]
        if value not in VALID_BODY_DHCP_ADDRESS_ENFORCEMENT:
            desc = FIELD_DESCRIPTIONS.get("dhcp-address-enforcement", "")
            error_msg = f"Invalid value for 'dhcp-address-enforcement': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_ADDRESS_ENFORCEMENT)}"
            error_msg += f"\n  → Example: dhcp-address-enforcement='{{ VALID_BODY_DHCP_ADDRESS_ENFORCEMENT[0] }}'"
            return (False, error_msg)
    if "broadcast-suppression" in payload:
        value = payload["broadcast-suppression"]
        if value not in VALID_BODY_BROADCAST_SUPPRESSION:
            desc = FIELD_DESCRIPTIONS.get("broadcast-suppression", "")
            error_msg = f"Invalid value for 'broadcast-suppression': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BROADCAST_SUPPRESSION)}"
            error_msg += f"\n  → Example: broadcast-suppression='{{ VALID_BODY_BROADCAST_SUPPRESSION[0] }}'"
            return (False, error_msg)
    if "ipv6-rules" in payload:
        value = payload["ipv6-rules"]
        if value not in VALID_BODY_IPV6_RULES:
            desc = FIELD_DESCRIPTIONS.get("ipv6-rules", "")
            error_msg = f"Invalid value for 'ipv6-rules': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_RULES)}"
            error_msg += f"\n  → Example: ipv6-rules='{{ VALID_BODY_IPV6_RULES[0] }}'"
            return (False, error_msg)
    if "mu-mimo" in payload:
        value = payload["mu-mimo"]
        if value not in VALID_BODY_MU_MIMO:
            desc = FIELD_DESCRIPTIONS.get("mu-mimo", "")
            error_msg = f"Invalid value for 'mu-mimo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MU_MIMO)}"
            error_msg += f"\n  → Example: mu-mimo='{{ VALID_BODY_MU_MIMO[0] }}'"
            return (False, error_msg)
    if "probe-resp-suppression" in payload:
        value = payload["probe-resp-suppression"]
        if value not in VALID_BODY_PROBE_RESP_SUPPRESSION:
            desc = FIELD_DESCRIPTIONS.get("probe-resp-suppression", "")
            error_msg = f"Invalid value for 'probe-resp-suppression': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROBE_RESP_SUPPRESSION)}"
            error_msg += f"\n  → Example: probe-resp-suppression='{{ VALID_BODY_PROBE_RESP_SUPPRESSION[0] }}'"
            return (False, error_msg)
    if "radio-sensitivity" in payload:
        value = payload["radio-sensitivity"]
        if value not in VALID_BODY_RADIO_SENSITIVITY:
            desc = FIELD_DESCRIPTIONS.get("radio-sensitivity", "")
            error_msg = f"Invalid value for 'radio-sensitivity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RADIO_SENSITIVITY)}"
            error_msg += f"\n  → Example: radio-sensitivity='{{ VALID_BODY_RADIO_SENSITIVITY[0] }}'"
            return (False, error_msg)
    if "quarantine" in payload:
        value = payload["quarantine"]
        if value not in VALID_BODY_QUARANTINE:
            desc = FIELD_DESCRIPTIONS.get("quarantine", "")
            error_msg = f"Invalid value for 'quarantine': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUARANTINE)}"
            error_msg += f"\n  → Example: quarantine='{{ VALID_BODY_QUARANTINE[0] }}'"
            return (False, error_msg)
    if "vlan-pooling" in payload:
        value = payload["vlan-pooling"]
        if value not in VALID_BODY_VLAN_POOLING:
            desc = FIELD_DESCRIPTIONS.get("vlan-pooling", "")
            error_msg = f"Invalid value for 'vlan-pooling': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VLAN_POOLING)}"
            error_msg += f"\n  → Example: vlan-pooling='{{ VALID_BODY_VLAN_POOLING[0] }}'"
            return (False, error_msg)
    if "dhcp-option43-insertion" in payload:
        value = payload["dhcp-option43-insertion"]
        if value not in VALID_BODY_DHCP_OPTION43_INSERTION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option43-insertion", "")
            error_msg = f"Invalid value for 'dhcp-option43-insertion': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION43_INSERTION)}"
            error_msg += f"\n  → Example: dhcp-option43-insertion='{{ VALID_BODY_DHCP_OPTION43_INSERTION[0] }}'"
            return (False, error_msg)
    if "dhcp-option82-insertion" in payload:
        value = payload["dhcp-option82-insertion"]
        if value not in VALID_BODY_DHCP_OPTION82_INSERTION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option82-insertion", "")
            error_msg = f"Invalid value for 'dhcp-option82-insertion': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION82_INSERTION)}"
            error_msg += f"\n  → Example: dhcp-option82-insertion='{{ VALID_BODY_DHCP_OPTION82_INSERTION[0] }}'"
            return (False, error_msg)
    if "dhcp-option82-circuit-id-insertion" in payload:
        value = payload["dhcp-option82-circuit-id-insertion"]
        if value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option82-circuit-id-insertion", "")
            error_msg = f"Invalid value for 'dhcp-option82-circuit-id-insertion': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION)}"
            error_msg += f"\n  → Example: dhcp-option82-circuit-id-insertion='{{ VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION[0] }}'"
            return (False, error_msg)
    if "dhcp-option82-remote-id-insertion" in payload:
        value = payload["dhcp-option82-remote-id-insertion"]
        if value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION:
            desc = FIELD_DESCRIPTIONS.get("dhcp-option82-remote-id-insertion", "")
            error_msg = f"Invalid value for 'dhcp-option82-remote-id-insertion': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION)}"
            error_msg += f"\n  → Example: dhcp-option82-remote-id-insertion='{{ VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION[0] }}'"
            return (False, error_msg)
    if "ptk-rekey" in payload:
        value = payload["ptk-rekey"]
        if value not in VALID_BODY_PTK_REKEY:
            desc = FIELD_DESCRIPTIONS.get("ptk-rekey", "")
            error_msg = f"Invalid value for 'ptk-rekey': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PTK_REKEY)}"
            error_msg += f"\n  → Example: ptk-rekey='{{ VALID_BODY_PTK_REKEY[0] }}'"
            return (False, error_msg)
    if "gtk-rekey" in payload:
        value = payload["gtk-rekey"]
        if value not in VALID_BODY_GTK_REKEY:
            desc = FIELD_DESCRIPTIONS.get("gtk-rekey", "")
            error_msg = f"Invalid value for 'gtk-rekey': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GTK_REKEY)}"
            error_msg += f"\n  → Example: gtk-rekey='{{ VALID_BODY_GTK_REKEY[0] }}'"
            return (False, error_msg)
    if "eap-reauth" in payload:
        value = payload["eap-reauth"]
        if value not in VALID_BODY_EAP_REAUTH:
            desc = FIELD_DESCRIPTIONS.get("eap-reauth", "")
            error_msg = f"Invalid value for 'eap-reauth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAP_REAUTH)}"
            error_msg += f"\n  → Example: eap-reauth='{{ VALID_BODY_EAP_REAUTH[0] }}'"
            return (False, error_msg)
    if "roaming-acct-interim-update" in payload:
        value = payload["roaming-acct-interim-update"]
        if value not in VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE:
            desc = FIELD_DESCRIPTIONS.get("roaming-acct-interim-update", "")
            error_msg = f"Invalid value for 'roaming-acct-interim-update': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE)}"
            error_msg += f"\n  → Example: roaming-acct-interim-update='{{ VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE[0] }}'"
            return (False, error_msg)
    if "rates-11a" in payload:
        value = payload["rates-11a"]
        if value not in VALID_BODY_RATES_11A:
            desc = FIELD_DESCRIPTIONS.get("rates-11a", "")
            error_msg = f"Invalid value for 'rates-11a': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RATES_11A)}"
            error_msg += f"\n  → Example: rates-11a='{{ VALID_BODY_RATES_11A[0] }}'"
            return (False, error_msg)
    if "rates-11bg" in payload:
        value = payload["rates-11bg"]
        if value not in VALID_BODY_RATES_11BG:
            desc = FIELD_DESCRIPTIONS.get("rates-11bg", "")
            error_msg = f"Invalid value for 'rates-11bg': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RATES_11BG)}"
            error_msg += f"\n  → Example: rates-11bg='{{ VALID_BODY_RATES_11BG[0] }}'"
            return (False, error_msg)
    if "rates-11n-ss12" in payload:
        value = payload["rates-11n-ss12"]
        if value not in VALID_BODY_RATES_11N_SS12:
            desc = FIELD_DESCRIPTIONS.get("rates-11n-ss12", "")
            error_msg = f"Invalid value for 'rates-11n-ss12': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RATES_11N_SS12)}"
            error_msg += f"\n  → Example: rates-11n-ss12='{{ VALID_BODY_RATES_11N_SS12[0] }}'"
            return (False, error_msg)
    if "rates-11n-ss34" in payload:
        value = payload["rates-11n-ss34"]
        if value not in VALID_BODY_RATES_11N_SS34:
            desc = FIELD_DESCRIPTIONS.get("rates-11n-ss34", "")
            error_msg = f"Invalid value for 'rates-11n-ss34': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RATES_11N_SS34)}"
            error_msg += f"\n  → Example: rates-11n-ss34='{{ VALID_BODY_RATES_11N_SS34[0] }}'"
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
    if "utm-log" in payload:
        value = payload["utm-log"]
        if value not in VALID_BODY_UTM_LOG:
            desc = FIELD_DESCRIPTIONS.get("utm-log", "")
            error_msg = f"Invalid value for 'utm-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UTM_LOG)}"
            error_msg += f"\n  → Example: utm-log='{{ VALID_BODY_UTM_LOG[0] }}'"
            return (False, error_msg)
    if "scan-botnet-connections" in payload:
        value = payload["scan-botnet-connections"]
        if value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            desc = FIELD_DESCRIPTIONS.get("scan-botnet-connections", "")
            error_msg = f"Invalid value for 'scan-botnet-connections': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCAN_BOTNET_CONNECTIONS)}"
            error_msg += f"\n  → Example: scan-botnet-connections='{{ VALID_BODY_SCAN_BOTNET_CONNECTIONS[0] }}'"
            return (False, error_msg)
    if "address-group-policy" in payload:
        value = payload["address-group-policy"]
        if value not in VALID_BODY_ADDRESS_GROUP_POLICY:
            desc = FIELD_DESCRIPTIONS.get("address-group-policy", "")
            error_msg = f"Invalid value for 'address-group-policy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDRESS_GROUP_POLICY)}"
            error_msg += f"\n  → Example: address-group-policy='{{ VALID_BODY_ADDRESS_GROUP_POLICY[0] }}'"
            return (False, error_msg)
    if "sticky-client-remove" in payload:
        value = payload["sticky-client-remove"]
        if value not in VALID_BODY_STICKY_CLIENT_REMOVE:
            desc = FIELD_DESCRIPTIONS.get("sticky-client-remove", "")
            error_msg = f"Invalid value for 'sticky-client-remove': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STICKY_CLIENT_REMOVE)}"
            error_msg += f"\n  → Example: sticky-client-remove='{{ VALID_BODY_STICKY_CLIENT_REMOVE[0] }}'"
            return (False, error_msg)
    if "bstm-disassociation-imminent" in payload:
        value = payload["bstm-disassociation-imminent"]
        if value not in VALID_BODY_BSTM_DISASSOCIATION_IMMINENT:
            desc = FIELD_DESCRIPTIONS.get("bstm-disassociation-imminent", "")
            error_msg = f"Invalid value for 'bstm-disassociation-imminent': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BSTM_DISASSOCIATION_IMMINENT)}"
            error_msg += f"\n  → Example: bstm-disassociation-imminent='{{ VALID_BODY_BSTM_DISASSOCIATION_IMMINENT[0] }}'"
            return (False, error_msg)
    if "beacon-advertising" in payload:
        value = payload["beacon-advertising"]
        if value not in VALID_BODY_BEACON_ADVERTISING:
            desc = FIELD_DESCRIPTIONS.get("beacon-advertising", "")
            error_msg = f"Invalid value for 'beacon-advertising': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BEACON_ADVERTISING)}"
            error_msg += f"\n  → Example: beacon-advertising='{{ VALID_BODY_BEACON_ADVERTISING[0] }}'"
            return (False, error_msg)
    if "osen" in payload:
        value = payload["osen"]
        if value not in VALID_BODY_OSEN:
            desc = FIELD_DESCRIPTIONS.get("osen", "")
            error_msg = f"Invalid value for 'osen': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OSEN)}"
            error_msg += f"\n  → Example: osen='{{ VALID_BODY_OSEN[0] }}'"
            return (False, error_msg)
    if "application-detection-engine" in payload:
        value = payload["application-detection-engine"]
        if value not in VALID_BODY_APPLICATION_DETECTION_ENGINE:
            desc = FIELD_DESCRIPTIONS.get("application-detection-engine", "")
            error_msg = f"Invalid value for 'application-detection-engine': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APPLICATION_DETECTION_ENGINE)}"
            error_msg += f"\n  → Example: application-detection-engine='{{ VALID_BODY_APPLICATION_DETECTION_ENGINE[0] }}'"
            return (False, error_msg)
    if "application-dscp-marking" in payload:
        value = payload["application-dscp-marking"]
        if value not in VALID_BODY_APPLICATION_DSCP_MARKING:
            desc = FIELD_DESCRIPTIONS.get("application-dscp-marking", "")
            error_msg = f"Invalid value for 'application-dscp-marking': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APPLICATION_DSCP_MARKING)}"
            error_msg += f"\n  → Example: application-dscp-marking='{{ VALID_BODY_APPLICATION_DSCP_MARKING[0] }}'"
            return (False, error_msg)
    if "l3-roaming" in payload:
        value = payload["l3-roaming"]
        if value not in VALID_BODY_L3_ROAMING:
            desc = FIELD_DESCRIPTIONS.get("l3-roaming", "")
            error_msg = f"Invalid value for 'l3-roaming': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_L3_ROAMING)}"
            error_msg += f"\n  → Example: l3-roaming='{{ VALID_BODY_L3_ROAMING[0] }}'"
            return (False, error_msg)
    if "l3-roaming-mode" in payload:
        value = payload["l3-roaming-mode"]
        if value not in VALID_BODY_L3_ROAMING_MODE:
            desc = FIELD_DESCRIPTIONS.get("l3-roaming-mode", "")
            error_msg = f"Invalid value for 'l3-roaming-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_L3_ROAMING_MODE)}"
            error_msg += f"\n  → Example: l3-roaming-mode='{{ VALID_BODY_L3_ROAMING_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_vap_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update wireless_controller/vap."""
    # Step 1: Validate enum values
    if "pre-auth" in payload:
        value = payload["pre-auth"]
        if value not in VALID_BODY_PRE_AUTH:
            return (
                False,
                f"Invalid value for 'pre-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_PRE_AUTH)}",
            )
    if "external-pre-auth" in payload:
        value = payload["external-pre-auth"]
        if value not in VALID_BODY_EXTERNAL_PRE_AUTH:
            return (
                False,
                f"Invalid value for 'external-pre-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_PRE_AUTH)}",
            )
    if "mesh-backhaul" in payload:
        value = payload["mesh-backhaul"]
        if value not in VALID_BODY_MESH_BACKHAUL:
            return (
                False,
                f"Invalid value for 'mesh-backhaul'='{value}'. Must be one of: {', '.join(VALID_BODY_MESH_BACKHAUL)}",
            )
    if "broadcast-ssid" in payload:
        value = payload["broadcast-ssid"]
        if value not in VALID_BODY_BROADCAST_SSID:
            return (
                False,
                f"Invalid value for 'broadcast-ssid'='{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SSID)}",
            )
    if "security" in payload:
        value = payload["security"]
        if value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid value for 'security'='{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
            )
    if "pmf" in payload:
        value = payload["pmf"]
        if value not in VALID_BODY_PMF:
            return (
                False,
                f"Invalid value for 'pmf'='{value}'. Must be one of: {', '.join(VALID_BODY_PMF)}",
            )
    if "beacon-protection" in payload:
        value = payload["beacon-protection"]
        if value not in VALID_BODY_BEACON_PROTECTION:
            return (
                False,
                f"Invalid value for 'beacon-protection'='{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_PROTECTION)}",
            )
    if "okc" in payload:
        value = payload["okc"]
        if value not in VALID_BODY_OKC:
            return (
                False,
                f"Invalid value for 'okc'='{value}'. Must be one of: {', '.join(VALID_BODY_OKC)}",
            )
    if "mbo" in payload:
        value = payload["mbo"]
        if value not in VALID_BODY_MBO:
            return (
                False,
                f"Invalid value for 'mbo'='{value}'. Must be one of: {', '.join(VALID_BODY_MBO)}",
            )
    if "mbo-cell-data-conn-pref" in payload:
        value = payload["mbo-cell-data-conn-pref"]
        if value not in VALID_BODY_MBO_CELL_DATA_CONN_PREF:
            return (
                False,
                f"Invalid value for 'mbo-cell-data-conn-pref'='{value}'. Must be one of: {', '.join(VALID_BODY_MBO_CELL_DATA_CONN_PREF)}",
            )
    if "80211k" in payload:
        value = payload["80211k"]
        if value not in VALID_BODY_80211K:
            return (
                False,
                f"Invalid value for '80211k'='{value}'. Must be one of: {', '.join(VALID_BODY_80211K)}",
            )
    if "80211v" in payload:
        value = payload["80211v"]
        if value not in VALID_BODY_80211V:
            return (
                False,
                f"Invalid value for '80211v'='{value}'. Must be one of: {', '.join(VALID_BODY_80211V)}",
            )
    if "neighbor-report-dual-band" in payload:
        value = payload["neighbor-report-dual-band"]
        if value not in VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND:
            return (
                False,
                f"Invalid value for 'neighbor-report-dual-band'='{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND)}",
            )
    if "fast-bss-transition" in payload:
        value = payload["fast-bss-transition"]
        if value not in VALID_BODY_FAST_BSS_TRANSITION:
            return (
                False,
                f"Invalid value for 'fast-bss-transition'='{value}'. Must be one of: {', '.join(VALID_BODY_FAST_BSS_TRANSITION)}",
            )
    if "ft-over-ds" in payload:
        value = payload["ft-over-ds"]
        if value not in VALID_BODY_FT_OVER_DS:
            return (
                False,
                f"Invalid value for 'ft-over-ds'='{value}'. Must be one of: {', '.join(VALID_BODY_FT_OVER_DS)}",
            )
    if "sae-groups" in payload:
        value = payload["sae-groups"]
        if value not in VALID_BODY_SAE_GROUPS:
            return (
                False,
                f"Invalid value for 'sae-groups'='{value}'. Must be one of: {', '.join(VALID_BODY_SAE_GROUPS)}",
            )
    if "owe-groups" in payload:
        value = payload["owe-groups"]
        if value not in VALID_BODY_OWE_GROUPS:
            return (
                False,
                f"Invalid value for 'owe-groups'='{value}'. Must be one of: {', '.join(VALID_BODY_OWE_GROUPS)}",
            )
    if "owe-transition" in payload:
        value = payload["owe-transition"]
        if value not in VALID_BODY_OWE_TRANSITION:
            return (
                False,
                f"Invalid value for 'owe-transition'='{value}'. Must be one of: {', '.join(VALID_BODY_OWE_TRANSITION)}",
            )
    if "additional-akms" in payload:
        value = payload["additional-akms"]
        if value not in VALID_BODY_ADDITIONAL_AKMS:
            return (
                False,
                f"Invalid value for 'additional-akms'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_AKMS)}",
            )
    if "eapol-key-retries" in payload:
        value = payload["eapol-key-retries"]
        if value not in VALID_BODY_EAPOL_KEY_RETRIES:
            return (
                False,
                f"Invalid value for 'eapol-key-retries'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_KEY_RETRIES)}",
            )
    if "tkip-counter-measure" in payload:
        value = payload["tkip-counter-measure"]
        if value not in VALID_BODY_TKIP_COUNTER_MEASURE:
            return (
                False,
                f"Invalid value for 'tkip-counter-measure'='{value}'. Must be one of: {', '.join(VALID_BODY_TKIP_COUNTER_MEASURE)}",
            )
    if "external-web-format" in payload:
        value = payload["external-web-format"]
        if value not in VALID_BODY_EXTERNAL_WEB_FORMAT:
            return (
                False,
                f"Invalid value for 'external-web-format'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_WEB_FORMAT)}",
            )
    if "mac-username-delimiter" in payload:
        value = payload["mac-username-delimiter"]
        if value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-username-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )
    if "mac-password-delimiter" in payload:
        value = payload["mac-password-delimiter"]
        if value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-password-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )
    if "mac-calling-station-delimiter" in payload:
        value = payload["mac-calling-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLING_STATION_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-calling-station-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLING_STATION_DELIMITER)}",
            )
    if "mac-called-station-delimiter" in payload:
        value = payload["mac-called-station-delimiter"]
        if value not in VALID_BODY_MAC_CALLED_STATION_DELIMITER:
            return (
                False,
                f"Invalid value for 'mac-called-station-delimiter'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLED_STATION_DELIMITER)}",
            )
    if "mac-case" in payload:
        value = payload["mac-case"]
        if value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid value for 'mac-case'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )
    if "called-station-id-type" in payload:
        value = payload["called-station-id-type"]
        if value not in VALID_BODY_CALLED_STATION_ID_TYPE:
            return (
                False,
                f"Invalid value for 'called-station-id-type'='{value}'. Must be one of: {', '.join(VALID_BODY_CALLED_STATION_ID_TYPE)}",
            )
    if "mac-auth-bypass" in payload:
        value = payload["mac-auth-bypass"]
        if value not in VALID_BODY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid value for 'mac-auth-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_MAC_AUTH_BYPASS)}",
            )
    if "radius-mac-auth" in payload:
        value = payload["radius-mac-auth"]
        if value not in VALID_BODY_RADIUS_MAC_AUTH:
            return (
                False,
                f"Invalid value for 'radius-mac-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_AUTH)}",
            )
    if "radius-mac-mpsk-auth" in payload:
        value = payload["radius-mac-mpsk-auth"]
        if value not in VALID_BODY_RADIUS_MAC_MPSK_AUTH:
            return (
                False,
                f"Invalid value for 'radius-mac-mpsk-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_MPSK_AUTH)}",
            )
    if "auth" in payload:
        value = payload["auth"]
        if value not in VALID_BODY_AUTH:
            return (
                False,
                f"Invalid value for 'auth'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH)}",
            )
    if "encrypt" in payload:
        value = payload["encrypt"]
        if value not in VALID_BODY_ENCRYPT:
            return (
                False,
                f"Invalid value for 'encrypt'='{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPT)}",
            )
    if "sae-h2e-only" in payload:
        value = payload["sae-h2e-only"]
        if value not in VALID_BODY_SAE_H2E_ONLY:
            return (
                False,
                f"Invalid value for 'sae-h2e-only'='{value}'. Must be one of: {', '.join(VALID_BODY_SAE_H2E_ONLY)}",
            )
    if "sae-hnp-only" in payload:
        value = payload["sae-hnp-only"]
        if value not in VALID_BODY_SAE_HNP_ONLY:
            return (
                False,
                f"Invalid value for 'sae-hnp-only'='{value}'. Must be one of: {', '.join(VALID_BODY_SAE_HNP_ONLY)}",
            )
    if "sae-pk" in payload:
        value = payload["sae-pk"]
        if value not in VALID_BODY_SAE_PK:
            return (
                False,
                f"Invalid value for 'sae-pk'='{value}'. Must be one of: {', '.join(VALID_BODY_SAE_PK)}",
            )
    if "akm24-only" in payload:
        value = payload["akm24-only"]
        if value not in VALID_BODY_AKM24_ONLY:
            return (
                False,
                f"Invalid value for 'akm24-only'='{value}'. Must be one of: {', '.join(VALID_BODY_AKM24_ONLY)}",
            )
    if "nas-filter-rule" in payload:
        value = payload["nas-filter-rule"]
        if value not in VALID_BODY_NAS_FILTER_RULE:
            return (
                False,
                f"Invalid value for 'nas-filter-rule'='{value}'. Must be one of: {', '.join(VALID_BODY_NAS_FILTER_RULE)}",
            )
    if "domain-name-stripping" in payload:
        value = payload["domain-name-stripping"]
        if value not in VALID_BODY_DOMAIN_NAME_STRIPPING:
            return (
                False,
                f"Invalid value for 'domain-name-stripping'='{value}'. Must be one of: {', '.join(VALID_BODY_DOMAIN_NAME_STRIPPING)}",
            )
    if "mlo" in payload:
        value = payload["mlo"]
        if value not in VALID_BODY_MLO:
            return (
                False,
                f"Invalid value for 'mlo'='{value}'. Must be one of: {', '.join(VALID_BODY_MLO)}",
            )
    if "local-standalone" in payload:
        value = payload["local-standalone"]
        if value not in VALID_BODY_LOCAL_STANDALONE:
            return (
                False,
                f"Invalid value for 'local-standalone'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE)}",
            )
    if "local-standalone-nat" in payload:
        value = payload["local-standalone-nat"]
        if value not in VALID_BODY_LOCAL_STANDALONE_NAT:
            return (
                False,
                f"Invalid value for 'local-standalone-nat'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE_NAT)}",
            )
    if "local-standalone-dns" in payload:
        value = payload["local-standalone-dns"]
        if value not in VALID_BODY_LOCAL_STANDALONE_DNS:
            return (
                False,
                f"Invalid value for 'local-standalone-dns'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE_DNS)}",
            )
    if "local-lan-partition" in payload:
        value = payload["local-lan-partition"]
        if value not in VALID_BODY_LOCAL_LAN_PARTITION:
            return (
                False,
                f"Invalid value for 'local-lan-partition'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_LAN_PARTITION)}",
            )
    if "local-bridging" in payload:
        value = payload["local-bridging"]
        if value not in VALID_BODY_LOCAL_BRIDGING:
            return (
                False,
                f"Invalid value for 'local-bridging'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_BRIDGING)}",
            )
    if "local-lan" in payload:
        value = payload["local-lan"]
        if value not in VALID_BODY_LOCAL_LAN:
            return (
                False,
                f"Invalid value for 'local-lan'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_LAN)}",
            )
    if "local-authentication" in payload:
        value = payload["local-authentication"]
        if value not in VALID_BODY_LOCAL_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'local-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_AUTHENTICATION)}",
            )
    if "captive-portal" in payload:
        value = payload["captive-portal"]
        if value not in VALID_BODY_CAPTIVE_PORTAL:
            return (
                False,
                f"Invalid value for 'captive-portal'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL)}",
            )
    if "captive-network-assistant-bypass" in payload:
        value = payload["captive-network-assistant-bypass"]
        if value not in VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS:
            return (
                False,
                f"Invalid value for 'captive-network-assistant-bypass'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS)}",
            )
    if "portal-type" in payload:
        value = payload["portal-type"]
        if value not in VALID_BODY_PORTAL_TYPE:
            return (
                False,
                f"Invalid value for 'portal-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PORTAL_TYPE)}",
            )
    if "intra-vap-privacy" in payload:
        value = payload["intra-vap-privacy"]
        if value not in VALID_BODY_INTRA_VAP_PRIVACY:
            return (
                False,
                f"Invalid value for 'intra-vap-privacy'='{value}'. Must be one of: {', '.join(VALID_BODY_INTRA_VAP_PRIVACY)}",
            )
    if "ldpc" in payload:
        value = payload["ldpc"]
        if value not in VALID_BODY_LDPC:
            return (
                False,
                f"Invalid value for 'ldpc'='{value}'. Must be one of: {', '.join(VALID_BODY_LDPC)}",
            )
    if "high-efficiency" in payload:
        value = payload["high-efficiency"]
        if value not in VALID_BODY_HIGH_EFFICIENCY:
            return (
                False,
                f"Invalid value for 'high-efficiency'='{value}'. Must be one of: {', '.join(VALID_BODY_HIGH_EFFICIENCY)}",
            )
    if "target-wake-time" in payload:
        value = payload["target-wake-time"]
        if value not in VALID_BODY_TARGET_WAKE_TIME:
            return (
                False,
                f"Invalid value for 'target-wake-time'='{value}'. Must be one of: {', '.join(VALID_BODY_TARGET_WAKE_TIME)}",
            )
    if "port-macauth" in payload:
        value = payload["port-macauth"]
        if value not in VALID_BODY_PORT_MACAUTH:
            return (
                False,
                f"Invalid value for 'port-macauth'='{value}'. Must be one of: {', '.join(VALID_BODY_PORT_MACAUTH)}",
            )
    if "bss-color-partial" in payload:
        value = payload["bss-color-partial"]
        if value not in VALID_BODY_BSS_COLOR_PARTIAL:
            return (
                False,
                f"Invalid value for 'bss-color-partial'='{value}'. Must be one of: {', '.join(VALID_BODY_BSS_COLOR_PARTIAL)}",
            )
    if "split-tunneling" in payload:
        value = payload["split-tunneling"]
        if value not in VALID_BODY_SPLIT_TUNNELING:
            return (
                False,
                f"Invalid value for 'split-tunneling'='{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING)}",
            )
    if "nac" in payload:
        value = payload["nac"]
        if value not in VALID_BODY_NAC:
            return (
                False,
                f"Invalid value for 'nac'='{value}'. Must be one of: {', '.join(VALID_BODY_NAC)}",
            )
    if "vlan-auto" in payload:
        value = payload["vlan-auto"]
        if value not in VALID_BODY_VLAN_AUTO:
            return (
                False,
                f"Invalid value for 'vlan-auto'='{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_AUTO)}",
            )
    if "dynamic-vlan" in payload:
        value = payload["dynamic-vlan"]
        if value not in VALID_BODY_DYNAMIC_VLAN:
            return (
                False,
                f"Invalid value for 'dynamic-vlan'='{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_VLAN)}",
            )
    if "captive-portal-fw-accounting" in payload:
        value = payload["captive-portal-fw-accounting"]
        if value not in VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING:
            return (
                False,
                f"Invalid value for 'captive-portal-fw-accounting'='{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING)}",
            )
    if "multicast-rate" in payload:
        value = payload["multicast-rate"]
        if value not in VALID_BODY_MULTICAST_RATE:
            return (
                False,
                f"Invalid value for 'multicast-rate'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_RATE)}",
            )
    if "multicast-enhance" in payload:
        value = payload["multicast-enhance"]
        if value not in VALID_BODY_MULTICAST_ENHANCE:
            return (
                False,
                f"Invalid value for 'multicast-enhance'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_ENHANCE)}",
            )
    if "igmp-snooping" in payload:
        value = payload["igmp-snooping"]
        if value not in VALID_BODY_IGMP_SNOOPING:
            return (
                False,
                f"Invalid value for 'igmp-snooping'='{value}'. Must be one of: {', '.join(VALID_BODY_IGMP_SNOOPING)}",
            )
    if "dhcp-address-enforcement" in payload:
        value = payload["dhcp-address-enforcement"]
        if value not in VALID_BODY_DHCP_ADDRESS_ENFORCEMENT:
            return (
                False,
                f"Invalid value for 'dhcp-address-enforcement'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_ADDRESS_ENFORCEMENT)}",
            )
    if "broadcast-suppression" in payload:
        value = payload["broadcast-suppression"]
        if value not in VALID_BODY_BROADCAST_SUPPRESSION:
            return (
                False,
                f"Invalid value for 'broadcast-suppression'='{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SUPPRESSION)}",
            )
    if "ipv6-rules" in payload:
        value = payload["ipv6-rules"]
        if value not in VALID_BODY_IPV6_RULES:
            return (
                False,
                f"Invalid value for 'ipv6-rules'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_RULES)}",
            )
    if "mu-mimo" in payload:
        value = payload["mu-mimo"]
        if value not in VALID_BODY_MU_MIMO:
            return (
                False,
                f"Invalid value for 'mu-mimo'='{value}'. Must be one of: {', '.join(VALID_BODY_MU_MIMO)}",
            )
    if "probe-resp-suppression" in payload:
        value = payload["probe-resp-suppression"]
        if value not in VALID_BODY_PROBE_RESP_SUPPRESSION:
            return (
                False,
                f"Invalid value for 'probe-resp-suppression'='{value}'. Must be one of: {', '.join(VALID_BODY_PROBE_RESP_SUPPRESSION)}",
            )
    if "radio-sensitivity" in payload:
        value = payload["radio-sensitivity"]
        if value not in VALID_BODY_RADIO_SENSITIVITY:
            return (
                False,
                f"Invalid value for 'radio-sensitivity'='{value}'. Must be one of: {', '.join(VALID_BODY_RADIO_SENSITIVITY)}",
            )
    if "quarantine" in payload:
        value = payload["quarantine"]
        if value not in VALID_BODY_QUARANTINE:
            return (
                False,
                f"Invalid value for 'quarantine'='{value}'. Must be one of: {', '.join(VALID_BODY_QUARANTINE)}",
            )
    if "vlan-pooling" in payload:
        value = payload["vlan-pooling"]
        if value not in VALID_BODY_VLAN_POOLING:
            return (
                False,
                f"Invalid value for 'vlan-pooling'='{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_POOLING)}",
            )
    if "dhcp-option43-insertion" in payload:
        value = payload["dhcp-option43-insertion"]
        if value not in VALID_BODY_DHCP_OPTION43_INSERTION:
            return (
                False,
                f"Invalid value for 'dhcp-option43-insertion'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION43_INSERTION)}",
            )
    if "dhcp-option82-insertion" in payload:
        value = payload["dhcp-option82-insertion"]
        if value not in VALID_BODY_DHCP_OPTION82_INSERTION:
            return (
                False,
                f"Invalid value for 'dhcp-option82-insertion'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_INSERTION)}",
            )
    if "dhcp-option82-circuit-id-insertion" in payload:
        value = payload["dhcp-option82-circuit-id-insertion"]
        if value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION:
            return (
                False,
                f"Invalid value for 'dhcp-option82-circuit-id-insertion'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION)}",
            )
    if "dhcp-option82-remote-id-insertion" in payload:
        value = payload["dhcp-option82-remote-id-insertion"]
        if value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION:
            return (
                False,
                f"Invalid value for 'dhcp-option82-remote-id-insertion'='{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION)}",
            )
    if "ptk-rekey" in payload:
        value = payload["ptk-rekey"]
        if value not in VALID_BODY_PTK_REKEY:
            return (
                False,
                f"Invalid value for 'ptk-rekey'='{value}'. Must be one of: {', '.join(VALID_BODY_PTK_REKEY)}",
            )
    if "gtk-rekey" in payload:
        value = payload["gtk-rekey"]
        if value not in VALID_BODY_GTK_REKEY:
            return (
                False,
                f"Invalid value for 'gtk-rekey'='{value}'. Must be one of: {', '.join(VALID_BODY_GTK_REKEY)}",
            )
    if "eap-reauth" in payload:
        value = payload["eap-reauth"]
        if value not in VALID_BODY_EAP_REAUTH:
            return (
                False,
                f"Invalid value for 'eap-reauth'='{value}'. Must be one of: {', '.join(VALID_BODY_EAP_REAUTH)}",
            )
    if "roaming-acct-interim-update" in payload:
        value = payload["roaming-acct-interim-update"]
        if value not in VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE:
            return (
                False,
                f"Invalid value for 'roaming-acct-interim-update'='{value}'. Must be one of: {', '.join(VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE)}",
            )
    if "rates-11a" in payload:
        value = payload["rates-11a"]
        if value not in VALID_BODY_RATES_11A:
            return (
                False,
                f"Invalid value for 'rates-11a'='{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11A)}",
            )
    if "rates-11bg" in payload:
        value = payload["rates-11bg"]
        if value not in VALID_BODY_RATES_11BG:
            return (
                False,
                f"Invalid value for 'rates-11bg'='{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11BG)}",
            )
    if "rates-11n-ss12" in payload:
        value = payload["rates-11n-ss12"]
        if value not in VALID_BODY_RATES_11N_SS12:
            return (
                False,
                f"Invalid value for 'rates-11n-ss12'='{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11N_SS12)}",
            )
    if "rates-11n-ss34" in payload:
        value = payload["rates-11n-ss34"]
        if value not in VALID_BODY_RATES_11N_SS34:
            return (
                False,
                f"Invalid value for 'rates-11n-ss34'='{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11N_SS34)}",
            )
    if "utm-status" in payload:
        value = payload["utm-status"]
        if value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid value for 'utm-status'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )
    if "utm-log" in payload:
        value = payload["utm-log"]
        if value not in VALID_BODY_UTM_LOG:
            return (
                False,
                f"Invalid value for 'utm-log'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_LOG)}",
            )
    if "scan-botnet-connections" in payload:
        value = payload["scan-botnet-connections"]
        if value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            return (
                False,
                f"Invalid value for 'scan-botnet-connections'='{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_BOTNET_CONNECTIONS)}",
            )
    if "address-group-policy" in payload:
        value = payload["address-group-policy"]
        if value not in VALID_BODY_ADDRESS_GROUP_POLICY:
            return (
                False,
                f"Invalid value for 'address-group-policy'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDRESS_GROUP_POLICY)}",
            )
    if "sticky-client-remove" in payload:
        value = payload["sticky-client-remove"]
        if value not in VALID_BODY_STICKY_CLIENT_REMOVE:
            return (
                False,
                f"Invalid value for 'sticky-client-remove'='{value}'. Must be one of: {', '.join(VALID_BODY_STICKY_CLIENT_REMOVE)}",
            )
    if "bstm-disassociation-imminent" in payload:
        value = payload["bstm-disassociation-imminent"]
        if value not in VALID_BODY_BSTM_DISASSOCIATION_IMMINENT:
            return (
                False,
                f"Invalid value for 'bstm-disassociation-imminent'='{value}'. Must be one of: {', '.join(VALID_BODY_BSTM_DISASSOCIATION_IMMINENT)}",
            )
    if "beacon-advertising" in payload:
        value = payload["beacon-advertising"]
        if value not in VALID_BODY_BEACON_ADVERTISING:
            return (
                False,
                f"Invalid value for 'beacon-advertising'='{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_ADVERTISING)}",
            )
    if "osen" in payload:
        value = payload["osen"]
        if value not in VALID_BODY_OSEN:
            return (
                False,
                f"Invalid value for 'osen'='{value}'. Must be one of: {', '.join(VALID_BODY_OSEN)}",
            )
    if "application-detection-engine" in payload:
        value = payload["application-detection-engine"]
        if value not in VALID_BODY_APPLICATION_DETECTION_ENGINE:
            return (
                False,
                f"Invalid value for 'application-detection-engine'='{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_DETECTION_ENGINE)}",
            )
    if "application-dscp-marking" in payload:
        value = payload["application-dscp-marking"]
        if value not in VALID_BODY_APPLICATION_DSCP_MARKING:
            return (
                False,
                f"Invalid value for 'application-dscp-marking'='{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_DSCP_MARKING)}",
            )
    if "l3-roaming" in payload:
        value = payload["l3-roaming"]
        if value not in VALID_BODY_L3_ROAMING:
            return (
                False,
                f"Invalid value for 'l3-roaming'='{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING)}",
            )
    if "l3-roaming-mode" in payload:
        value = payload["l3-roaming-mode"]
        if value not in VALID_BODY_L3_ROAMING_MODE:
            return (
                False,
                f"Invalid value for 'l3-roaming-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING_MODE)}",
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
    "endpoint": "wireless_controller/vap",
    "category": "cmdb",
    "api_path": "wireless-controller/vap",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Virtual Access Points (VAPs).",
    "total_fields": 172,
    "required_fields_count": 1,
    "fields_with_defaults_count": 160,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
