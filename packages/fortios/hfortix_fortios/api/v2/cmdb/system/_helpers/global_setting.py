"""
Validation helpers for system/global_setting endpoint.

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
    "restart-time",  # Daily restart time (hh:mm).
    "wad-restart-start-time",  # WAD workers daily restart time (hh:mm).
    "wad-restart-end-time",  # WAD workers daily restart end time (hh:mm).
    "timezone",  # Timezone database name. Enter ? to view the list of timezone.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "language": "english",
    "gui-ipv6": "disable",
    "gui-replacement-message-groups": "disable",
    "gui-local-out": "disable",
    "gui-certificates": "enable",
    "gui-custom-language": "disable",
    "gui-wireless-opensecurity": "disable",
    "gui-app-detection-sdwan": "disable",
    "gui-display-hostname": "disable",
    "gui-fortigate-cloud-sandbox": "disable",
    "gui-firmware-upgrade-warning": "enable",
    "gui-forticare-registration-setup-warning": "enable",
    "gui-auto-upgrade-setup-warning": "enable",
    "gui-workflow-management": "disable",
    "gui-cdn-usage": "enable",
    "admin-https-ssl-versions": "tlsv1-2 tlsv1-3",
    "admin-https-ssl-ciphersuites": "TLS-AES-128-GCM-SHA256 TLS-AES-256-GCM-SHA384 TLS-CHACHA20-POLY1305-SHA256",
    "admin-https-ssl-banned-ciphers": "",
    "admintimeout": 5,
    "admin-console-timeout": 0,
    "ssd-trim-freq": "weekly",
    "ssd-trim-hour": 1,
    "ssd-trim-min": 60,
    "ssd-trim-weekday": "sunday",
    "ssd-trim-date": 1,
    "admin-concurrent": "enable",
    "admin-lockout-threshold": 3,
    "admin-lockout-duration": 60,
    "refresh": 0,
    "interval": 5,
    "failtime": 5,
    "purdue-level": "3",
    "daily-restart": "disable",
    "restart-time": "",
    "wad-restart-mode": "none",
    "wad-restart-start-time": "",
    "wad-restart-end-time": "",
    "wad-p2s-max-body-size": 4,
    "radius-port": 1812,
    "speedtestd-server-port": 5201,
    "speedtestd-ctrl-port": 5200,
    "admin-login-max": 100,
    "remoteauthtimeout": 5,
    "ldapconntimeout": 500,
    "batch-cmdb": "enable",
    "multi-factor-authentication": "optional",
    "ssl-min-proto-version": "TLSv1-2",
    "autorun-log-fsck": "disable",
    "timezone": "",
    "traffic-priority": "tos",
    "traffic-priority-level": "medium",
    "quic-congestion-control-algo": "cubic",
    "quic-max-datagram-size": 1500,
    "quic-udp-payload-size-shaping-per-cid": "enable",
    "quic-ack-thresold": 3,
    "quic-pmtud": "enable",
    "quic-tls-handshake-timeout": 5,
    "anti-replay": "strict",
    "send-pmtu-icmp": "enable",
    "honor-df": "enable",
    "pmtu-discovery": "disable",
    "revision-image-auto-backup": "disable",
    "revision-backup-on-logout": "disable",
    "management-vdom": "root",
    "hostname": "",
    "alias": "",
    "strong-crypto": "enable",
    "ssl-static-key-ciphers": "enable",
    "snat-route-change": "disable",
    "ipv6-snat-route-change": "disable",
    "speedtest-server": "disable",
    "cli-audit-log": "disable",
    "dh-params": "2048",
    "fds-statistics": "enable",
    "fds-statistics-period": 60,
    "tcp-option": "enable",
    "lldp-transmission": "disable",
    "lldp-reception": "disable",
    "proxy-auth-timeout": 10,
    "proxy-keep-alive-mode": "session",
    "proxy-re-authentication-time": 30,
    "proxy-auth-lifetime": "disable",
    "proxy-auth-lifetime-timeout": 480,
    "proxy-resource-mode": "disable",
    "proxy-cert-use-mgmt-vdom": "disable",
    "sys-perf-log-interval": 5,
    "check-protocol-header": "loose",
    "vip-arp-range": "restricted",
    "reset-sessionless-tcp": "disable",
    "allow-traffic-redirect": "enable",
    "ipv6-allow-traffic-redirect": "enable",
    "strict-dirty-session-check": "enable",
    "tcp-halfclose-timer": 120,
    "tcp-halfopen-timer": 10,
    "tcp-timewait-timer": 1,
    "tcp-rst-timer": 5,
    "udp-idle-timer": 180,
    "block-session-timer": 30,
    "ip-src-port-range": "1024-25000",
    "pre-login-banner": "disable",
    "post-login-banner": "disable",
    "tftp": "enable",
    "av-failopen": "pass",
    "av-failopen-session": "disable",
    "memory-use-threshold-extreme": 95,
    "memory-use-threshold-red": 88,
    "memory-use-threshold-green": 82,
    "ip-fragment-mem-thresholds": 32,
    "ip-fragment-timeout": 30,
    "ipv6-fragment-timeout": 60,
    "cpu-use-threshold": 90,
    "log-single-cpu-high": "disable",
    "check-reset-range": "disable",
    "upgrade-report": "enable",
    "admin-port": 80,
    "admin-sport": 443,
    "admin-host": "",
    "admin-https-redirect": "enable",
    "admin-hsts-max-age": 63072000,
    "admin-ssh-password": "enable",
    "admin-restrict-local": "disable",
    "admin-ssh-port": 22,
    "admin-ssh-grace-time": 120,
    "admin-ssh-v1": "disable",
    "admin-telnet": "enable",
    "admin-telnet-port": 23,
    "admin-forticloud-sso-login": "disable",
    "admin-forticloud-sso-default-profile": "",
    "default-service-source-port": "",
    "admin-server-cert": "Fortinet_GUI_Server",
    "admin-https-pki-required": "disable",
    "wifi-certificate": "Fortinet_Wifi",
    "dhcp-lease-backup-interval": 60,
    "wifi-ca-certificate": "Fortinet_Wifi_CA",
    "auth-http-port": 1000,
    "auth-https-port": 1003,
    "auth-ike-saml-port": 1001,
    "auth-keepalive": "disable",
    "policy-auth-concurrent": 0,
    "auth-session-limit": "block-new",
    "auth-cert": "Fortinet_Factory",
    "clt-cert-req": "disable",
    "fortiservice-port": 8013,
    "cfg-save": "automatic",
    "cfg-revert-timeout": 600,
    "reboot-upon-config-restore": "enable",
    "admin-scp": "disable",
    "wireless-controller": "enable",
    "wireless-controller-port": 5246,
    "fortiextender-data-port": 25246,
    "fortiextender": "disable",
    "extender-controller-reserved-network": "10.252.0.1 255.255.0.0",
    "fortiextender-discovery-lockdown": "disable",
    "fortiextender-vlan-mode": "disable",
    "fortiextender-provision-on-authorization": "disable",
    "switch-controller": "disable",
    "switch-controller-reserved-network": "10.255.0.1 255.255.0.0",
    "dnsproxy-worker-count": 1,
    "url-filter-count": 1,
    "httpd-max-worker-count": 0,
    "proxy-worker-count": 0,
    "scanunit-count": 0,
    "fgd-alert-subscription": "",
    "ipv6-accept-dad": 1,
    "ipv6-allow-anycast-probe": "disable",
    "ipv6-allow-multicast-probe": "disable",
    "ipv6-allow-local-in-silent-drop": "enable",
    "csr-ca-attribute": "enable",
    "wimax-4g-usb": "disable",
    "cert-chain-max": 8,
    "sslvpn-max-worker-count": 0,
    "sslvpn-affinity": "0",
    "sslvpn-web-mode": "disable",
    "two-factor-ftk-expiry": 60,
    "two-factor-email-expiry": 60,
    "two-factor-sms-expiry": 60,
    "two-factor-fac-expiry": 60,
    "two-factor-ftm-expiry": 72,
    "per-user-bal": "disable",
    "wad-worker-count": 0,
    "wad-csvc-cs-count": 1,
    "wad-csvc-db-count": 0,
    "wad-source-affinity": "enable",
    "wad-memory-change-granularity": 10,
    "login-timestamp": "disable",
    "ip-conflict-detection": "disable",
    "miglogd-children": 0,
    "special-file-23-support": "disable",
    "log-uuid-address": "disable",
    "log-ssl-connection": "disable",
    "gui-rest-api-cache": "enable",
    "rest-api-key-url-query": "disable",
    "arp-max-entry": 131072,
    "ha-affinity": "1",
    "bfd-affinity": "1",
    "cmdbsvr-affinity": "1",
    "av-affinity": "0",
    "wad-affinity": "0",
    "ips-affinity": "0",
    "miglog-affinity": "0",
    "syslog-affinity": "0",
    "url-filter-affinity": "0",
    "router-affinity": "0",
    "ndp-max-entry": 0,
    "br-fdb-max-entry": 8192,
    "max-route-cache-size": 0,
    "ipsec-qat-offload": "enable",
    "device-idle-timeout": 300,
    "user-device-store-max-devices": 62524,
    "user-device-store-max-device-mem": 2,
    "user-device-store-max-users": 62524,
    "user-device-store-max-unified-mem": 312622899,
    "gui-device-latitude": "",
    "gui-device-longitude": "",
    "private-data-encryption": "disable",
    "auto-auth-extension-device": "enable",
    "gui-theme": "jade",
    "gui-date-format": "yyyy/MM/dd",
    "gui-date-time-source": "system",
    "igmp-state-limit": 3200,
    "cloud-communication": "enable",
    "ipsec-ha-seqjump-rate": 10,
    "fortitoken-cloud": "enable",
    "fortitoken-cloud-push-status": "enable",
    "fortitoken-cloud-region": "",
    "fortitoken-cloud-sync-interval": 24,
    "faz-disk-buffer-size": 0,
    "irq-time-accounting": "auto",
    "management-ip": "",
    "management-port": 443,
    "management-port-use-admin-sport": "enable",
    "forticonverter-integration": "disable",
    "forticonverter-config-upload": "disable",
    "internet-service-database": "full",
    "early-tcp-npu-session": "disable",
    "npu-neighbor-update": "disable",
    "delay-tcp-npu-session": "disable",
    "interface-subnet-usage": "enable",
    "sflowd-max-children-num": 1,
    "fortigslb-integration": "disable",
    "user-history-password-threshold": 3,
    "auth-session-auto-backup": "disable",
    "auth-session-auto-backup-interval": "15min",
    "scim-https-port": 44559,
    "scim-http-port": 44558,
    "scim-server-cert": "Fortinet_Factory",
    "application-bandwidth-tracking": "disable",
    "tls-session-cache": "enable",
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
    "language": "option",  # GUI display language.
    "gui-ipv6": "option",  # Enable/disable IPv6 settings on the GUI.
    "gui-replacement-message-groups": "option",  # Enable/disable replacement message groups on the GUI.
    "gui-local-out": "option",  # Enable/disable Local-out traffic on the GUI.
    "gui-certificates": "option",  # Enable/disable the System > Certificate GUI page, allowing y
    "gui-custom-language": "option",  # Enable/disable custom languages in GUI.
    "gui-wireless-opensecurity": "option",  # Enable/disable wireless open security option on the GUI.
    "gui-app-detection-sdwan": "option",  # Enable/disable Allow app-detection based SD-WAN.
    "gui-display-hostname": "option",  # Enable/disable displaying the FortiGate's hostname on the GU
    "gui-fortigate-cloud-sandbox": "option",  # Enable/disable displaying FortiGate Cloud Sandbox on the GUI
    "gui-firmware-upgrade-warning": "option",  # Enable/disable the firmware upgrade warning on the GUI.
    "gui-forticare-registration-setup-warning": "option",  # Enable/disable the FortiCare registration setup warning on t
    "gui-auto-upgrade-setup-warning": "option",  # Enable/disable the automatic patch upgrade setup prompt on t
    "gui-workflow-management": "option",  # Enable/disable Workflow management features on the GUI.
    "gui-cdn-usage": "option",  # Enable/disable Load GUI static files from a CDN.
    "admin-https-ssl-versions": "option",  # Allowed TLS versions for web administration.
    "admin-https-ssl-ciphersuites": "option",  # Select one or more TLS 1.3 ciphersuites to enable. Does not 
    "admin-https-ssl-banned-ciphers": "option",  # Select one or more cipher technologies that cannot be used i
    "admintimeout": "integer",  # Number of minutes before an idle administrator session times
    "admin-console-timeout": "integer",  # Console login timeout that overrides the admin timeout value
    "ssd-trim-freq": "option",  # How often to run SSD Trim (default = weekly). SSD Trim preve
    "ssd-trim-hour": "integer",  # Hour of the day on which to run SSD Trim (0 - 23, default = 
    "ssd-trim-min": "integer",  # Minute of the hour on which to run SSD Trim (0 - 59, 60 for 
    "ssd-trim-weekday": "option",  # Day of week to run SSD Trim.
    "ssd-trim-date": "integer",  # Date within a month to run ssd trim.
    "admin-concurrent": "option",  # Enable/disable concurrent administrator logins. Use policy-a
    "admin-lockout-threshold": "integer",  # Number of failed login attempts before an administrator acco
    "admin-lockout-duration": "integer",  # Amount of time in seconds that an administrator account is l
    "refresh": "integer",  # Statistics refresh interval second(s) in GUI.
    "interval": "integer",  # Dead gateway detection interval.
    "failtime": "integer",  # Fail-time for server lost.
    "purdue-level": "option",  # Purdue Level of this FortiGate.
    "daily-restart": "option",  # Enable/disable daily restart of FortiGate unit. Use the rest
    "restart-time": "user",  # Daily restart time (hh:mm).
    "wad-restart-mode": "option",  # WAD worker restart mode (default = none).
    "wad-restart-start-time": "user",  # WAD workers daily restart time (hh:mm).
    "wad-restart-end-time": "user",  # WAD workers daily restart end time (hh:mm).
    "wad-p2s-max-body-size": "integer",  # Maximum size of the body of the local out HTTP request (1 - 
    "radius-port": "integer",  # RADIUS service port number.
    "speedtestd-server-port": "integer",  # Speedtest server port number.
    "speedtestd-ctrl-port": "integer",  # Speedtest server controller port number.
    "admin-login-max": "integer",  # Maximum number of administrators who can be logged in at the
    "remoteauthtimeout": "integer",  # Number of seconds that the FortiGate waits for responses fro
    "ldapconntimeout": "integer",  # Global timeout for connections with remote LDAP servers in m
    "batch-cmdb": "option",  # Enable/disable batch mode, allowing you to enter a series of
    "multi-factor-authentication": "option",  # Enforce all login methods to require an additional authentic
    "ssl-min-proto-version": "option",  # Minimum supported protocol version for SSL/TLS connections (
    "autorun-log-fsck": "option",  # Enable/disable automatic log partition check after ungracefu
    "timezone": "string",  # Timezone database name. Enter ? to view the list of timezone
    "traffic-priority": "option",  # Choose Type of Service (ToS) or Differentiated Services Code
    "traffic-priority-level": "option",  # Default system-wide level of priority for traffic prioritiza
    "quic-congestion-control-algo": "option",  # QUIC congestion control algorithm (default = cubic).
    "quic-max-datagram-size": "integer",  # Maximum transmit datagram size (1200 - 1500, default = 1500)
    "quic-udp-payload-size-shaping-per-cid": "option",  # Enable/disable UDP payload size shaping per connection ID (d
    "quic-ack-thresold": "integer",  # Maximum number of unacknowledged packets before sending ACK 
    "quic-pmtud": "option",  # Enable/disable path MTU discovery (default = enable).
    "quic-tls-handshake-timeout": "integer",  # Time-to-live (TTL) for TLS handshake in seconds (1 - 60, def
    "anti-replay": "option",  # Level of checking for packet replay and TCP sequence checkin
    "send-pmtu-icmp": "option",  # Enable/disable sending of path maximum transmission unit (PM
    "honor-df": "option",  # Enable/disable honoring of Don't-Fragment (DF) flag.
    "pmtu-discovery": "option",  # Enable/disable path MTU discovery.
    "revision-image-auto-backup": "option",  # Enable/disable back-up of the latest image revision after th
    "revision-backup-on-logout": "option",  # Enable/disable back-up of the latest configuration revision 
    "management-vdom": "string",  # Management virtual domain name.
    "hostname": "string",  # FortiGate unit's hostname. Most models will truncate names l
    "alias": "string",  # Alias for your FortiGate unit.
    "strong-crypto": "option",  # Enable to use strong encryption and only allow strong cipher
    "ssl-static-key-ciphers": "option",  # Enable/disable static key ciphers in SSL/TLS connections (e.
    "snat-route-change": "option",  # Enable/disable the ability to change the source NAT route.
    "ipv6-snat-route-change": "option",  # Enable/disable the ability to change the IPv6 source NAT rou
    "speedtest-server": "option",  # Enable/disable speed test server.
    "cli-audit-log": "option",  # Enable/disable CLI audit log.
    "dh-params": "option",  # Number of bits to use in the Diffie-Hellman exchange for HTT
    "fds-statistics": "option",  # Enable/disable sending IPS, Application Control, and AntiVir
    "fds-statistics-period": "integer",  # FortiGuard statistics collection period in minutes. (1 - 144
    "tcp-option": "option",  # Enable SACK, timestamp and MSS TCP options.
    "lldp-transmission": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) transmis
    "lldp-reception": "option",  # Enable/disable Link Layer Discovery Protocol (LLDP) receptio
    "proxy-auth-timeout": "integer",  # Authentication timeout in minutes for authenticated users (1
    "proxy-keep-alive-mode": "option",  # Control if users must re-authenticate after a session is clo
    "proxy-re-authentication-time": "integer",  # The time limit that users must re-authenticate if proxy-keep
    "proxy-auth-lifetime": "option",  # Enable/disable authenticated users lifetime control. This is
    "proxy-auth-lifetime-timeout": "integer",  # Lifetime timeout in minutes for authenticated users (5  - 65
    "proxy-resource-mode": "option",  # Enable/disable use of the maximum memory usage on the FortiG
    "proxy-cert-use-mgmt-vdom": "option",  # Enable/disable using management VDOM to send requests.
    "sys-perf-log-interval": "integer",  # Time in minutes between updates of performance statistics lo
    "check-protocol-header": "option",  # Level of checking performed on protocol headers. Strict chec
    "vip-arp-range": "option",  # Controls the number of ARPs that the FortiGate sends for a V
    "reset-sessionless-tcp": "option",  # Action to perform if the FortiGate receives a TCP packet but
    "allow-traffic-redirect": "option",  # Disable to prevent traffic with same local ingress and egres
    "ipv6-allow-traffic-redirect": "option",  # Disable to prevent IPv6 traffic with same local ingress and 
    "strict-dirty-session-check": "option",  # Enable to check the session against the original policy when
    "tcp-halfclose-timer": "integer",  # Number of seconds the FortiGate unit should wait to close a 
    "tcp-halfopen-timer": "integer",  # Number of seconds the FortiGate unit should wait to close a 
    "tcp-timewait-timer": "integer",  # Length of the TCP TIME-WAIT state in seconds (1 - 300 sec, d
    "tcp-rst-timer": "integer",  # Length of the TCP CLOSE state in seconds (5 - 300 sec, defau
    "udp-idle-timer": "integer",  # UDP connection session timeout. This command can be useful i
    "block-session-timer": "integer",  # Duration in seconds for blocked sessions (1 - 300 sec  (5 mi
    "ip-src-port-range": "user",  # IP source port range used for traffic originating from the F
    "pre-login-banner": "option",  # Enable/disable displaying the administrator access disclaime
    "post-login-banner": "option",  # Enable/disable displaying the administrator access disclaime
    "tftp": "option",  # Enable/disable TFTP.
    "av-failopen": "option",  # Set the action to take if the FortiGate is running low on me
    "av-failopen-session": "option",  # When enabled and a proxy for a protocol runs out of room in 
    "memory-use-threshold-extreme": "integer",  # Threshold at which memory usage is considered extreme (new s
    "memory-use-threshold-red": "integer",  # Threshold at which memory usage forces the FortiGate to ente
    "memory-use-threshold-green": "integer",  # Threshold at which memory usage forces the FortiGate to exit
    "ip-fragment-mem-thresholds": "integer",  # Maximum memory (MB) used to reassemble IPv4/IPv6 fragments.
    "ip-fragment-timeout": "integer",  # Timeout value in seconds for any fragment not being reassemb
    "ipv6-fragment-timeout": "integer",  # Timeout value in seconds for any IPv6 fragment not being rea
    "cpu-use-threshold": "integer",  # Threshold at which CPU usage is reported (% of total CPU, de
    "log-single-cpu-high": "option",  # Enable/disable logging the event of a single CPU core reachi
    "check-reset-range": "option",  # Configure ICMP error message verification. You can either ap
    "upgrade-report": "option",  # Enable/disable the generation of an upgrade report when upgr
    "admin-port": "integer",  # Administrative access port for HTTP. (1 - 65535, default = 8
    "admin-sport": "integer",  # Administrative access port for HTTPS. (1 - 65535, default = 
    "admin-host": "string",  # Administrative host for HTTP and HTTPS. When set, will be us
    "admin-https-redirect": "option",  # Enable/disable redirection of HTTP administration access to 
    "admin-hsts-max-age": "integer",  # HTTPS Strict-Transport-Security header max-age in seconds. A
    "admin-ssh-password": "option",  # Enable/disable password authentication for SSH admin access.
    "admin-restrict-local": "option",  # Enable/disable local admin authentication restriction when r
    "admin-ssh-port": "integer",  # Administrative access port for SSH. (1 - 65535, default = 22
    "admin-ssh-grace-time": "integer",  # Maximum time in seconds permitted between making an SSH conn
    "admin-ssh-v1": "option",  # Enable/disable SSH v1 compatibility.
    "admin-telnet": "option",  # Enable/disable TELNET service.
    "admin-telnet-port": "integer",  # Administrative access port for TELNET. (1 - 65535, default =
    "admin-forticloud-sso-login": "option",  # Enable/disable FortiCloud admin login via SSO.
    "admin-forticloud-sso-default-profile": "string",  # Override access profile.
    "default-service-source-port": "user",  # Default service source port range (default = 1 - 65535).
    "admin-server-cert": "string",  # Server certificate that the FortiGate uses for HTTPS adminis
    "admin-https-pki-required": "option",  # Enable/disable admin login method. Enable to force administr
    "wifi-certificate": "string",  # Certificate to use for WiFi authentication.
    "dhcp-lease-backup-interval": "integer",  # DHCP leases backup interval in seconds (10 - 3600, default =
    "wifi-ca-certificate": "string",  # CA certificate that verifies the WiFi certificate.
    "auth-http-port": "integer",  # User authentication HTTP port. (1 - 65535, default = 1000).
    "auth-https-port": "integer",  # User authentication HTTPS port. (1 - 65535, default = 1003).
    "auth-ike-saml-port": "integer",  # User IKE SAML authentication port (0 - 65535, default = 1001
    "auth-keepalive": "option",  # Enable to prevent user authentication sessions from timing o
    "policy-auth-concurrent": "integer",  # Number of concurrent firewall use logins from the same user 
    "auth-session-limit": "option",  # Action to take when the number of allowed user authenticated
    "auth-cert": "string",  # Server certificate that the FortiGate uses for HTTPS firewal
    "clt-cert-req": "option",  # Enable/disable requiring administrators to have a client cer
    "fortiservice-port": "integer",  # FortiService port (1 - 65535, default = 8013). Used by Forti
    "cfg-save": "option",  # Configuration file save mode for CLI changes.
    "cfg-revert-timeout": "integer",  # Time-out for reverting to the last saved configuration. (10 
    "reboot-upon-config-restore": "option",  # Enable/disable reboot of system upon restoring configuration
    "admin-scp": "option",  # Enable/disable SCP support for system configuration backup, 
    "wireless-controller": "option",  # Enable/disable the wireless controller feature to use the Fo
    "wireless-controller-port": "integer",  # Port used for the control channel in wireless controller mod
    "fortiextender-data-port": "integer",  # FortiExtender data port (1024 - 49150, default = 25246).
    "fortiextender": "option",  # Enable/disable FortiExtender.
    "extender-controller-reserved-network": "ipv4-classnet-host",  # Configure reserved network subnet for managed LAN extension 
    "fortiextender-discovery-lockdown": "option",  # Enable/disable FortiExtender CAPWAP lockdown.
    "fortiextender-vlan-mode": "option",  # Enable/disable FortiExtender VLAN mode.
    "fortiextender-provision-on-authorization": "option",  # Enable/disable automatic provisioning of latest FortiExtende
    "switch-controller": "option",  # Enable/disable switch controller feature. Switch controller 
    "switch-controller-reserved-network": "ipv4-classnet-host",  # Configure reserved network subnet for managed switches. This
    "dnsproxy-worker-count": "integer",  # DNS proxy worker count. For a FortiGate with multiple logica
    "url-filter-count": "integer",  # URL filter daemon count.
    "httpd-max-worker-count": "integer",  # Maximum number of simultaneous HTTP requests that will be se
    "proxy-worker-count": "integer",  # Proxy worker count.
    "scanunit-count": "integer",  # Number of scanunits. The range and the default depend on the
    "fgd-alert-subscription": "option",  # Type of alert to retrieve from FortiGuard.
    "ipv6-accept-dad": "integer",  # Enable/disable acceptance of IPv6 Duplicate Address Detectio
    "ipv6-allow-anycast-probe": "option",  # Enable/disable IPv6 address probe through Anycast.
    "ipv6-allow-multicast-probe": "option",  # Enable/disable IPv6 address probe through Multicast.
    "ipv6-allow-local-in-silent-drop": "option",  # Enable/disable silent drop of IPv6 local-in traffic.
    "csr-ca-attribute": "option",  # Enable/disable the CA attribute in certificates. Some CA ser
    "wimax-4g-usb": "option",  # Enable/disable comparability with WiMAX 4G USB devices.
    "cert-chain-max": "integer",  # Maximum number of certificates that can be traversed in a ce
    "sslvpn-max-worker-count": "integer",  # Maximum number of Agentless VPN processes. Upper limit for t
    "sslvpn-affinity": "string",  # Agentless VPN CPU affinity.
    "sslvpn-web-mode": "option",  # Enable/disable Agentless VPN web mode.
    "two-factor-ftk-expiry": "integer",  # FortiToken authentication session timeout (60 - 600 sec (10 
    "two-factor-email-expiry": "integer",  # Email-based two-factor authentication session timeout (30 - 
    "two-factor-sms-expiry": "integer",  # SMS-based two-factor authentication session timeout (30 - 30
    "two-factor-fac-expiry": "integer",  # FortiAuthenticator token authentication session timeout (10 
    "two-factor-ftm-expiry": "integer",  # FortiToken Mobile session timeout (1 - 168 hours (7 days), d
    "per-user-bal": "option",  # Enable/disable per-user block/allow list filter.
    "wad-worker-count": "integer",  # Number of explicit proxy WAN optimization daemon (WAD) proce
    "wad-csvc-cs-count": "integer",  # Number of concurrent WAD-cache-service object-cache processe
    "wad-csvc-db-count": "integer",  # Number of concurrent WAD-cache-service byte-cache processes.
    "wad-source-affinity": "option",  # Enable/disable dispatching traffic to WAD workers based on s
    "wad-memory-change-granularity": "integer",  # Minimum percentage change in system memory usage detected by
    "login-timestamp": "option",  # Enable/disable login time recording.
    "ip-conflict-detection": "option",  # Enable/disable logging of IPv4 address conflict detection.
    "miglogd-children": "integer",  # Number of logging (miglogd) processes to be allowed to run. 
    "special-file-23-support": "option",  # Enable/disable detection of those special format files when 
    "log-uuid-address": "option",  # Enable/disable insertion of address UUIDs to traffic logs.
    "log-ssl-connection": "option",  # Enable/disable logging of SSL connection events.
    "gui-rest-api-cache": "option",  # Enable/disable REST API result caching on FortiGate.
    "rest-api-key-url-query": "option",  # Enable/disable support for passing REST API keys through URL
    "arp-max-entry": "integer",  # Maximum number of dynamically learned MAC addresses that can
    "ha-affinity": "string",  # Affinity setting for HA daemons (hexadecimal value up to 256
    "bfd-affinity": "string",  # Affinity setting for BFD daemon (hexadecimal value up to 256
    "cmdbsvr-affinity": "string",  # Affinity setting for cmdbsvr (hexadecimal value up to 256 bi
    "av-affinity": "string",  # Affinity setting for AV scanning (hexadecimal value up to 25
    "wad-affinity": "string",  # Affinity setting for wad (hexadecimal value up to 256 bits i
    "ips-affinity": "string",  # Affinity setting for IPS (hexadecimal value up to 256 bits i
    "miglog-affinity": "string",  # Affinity setting for logging (hexadecimal value up to 256 bi
    "syslog-affinity": "string",  # Affinity setting for syslog (hexadecimal value up to 256 bit
    "url-filter-affinity": "string",  # URL filter CPU affinity.
    "router-affinity": "string",  # Affinity setting for BFD/VRRP/BGP/OSPF daemons (hexadecimal 
    "ndp-max-entry": "integer",  # Maximum number of NDP table entries (set to 65,536 or higher
    "br-fdb-max-entry": "integer",  # Maximum number of bridge forwarding database (FDB) entries.
    "max-route-cache-size": "integer",  # Maximum number of IP route cache entries (0 - 2147483647).
    "ipsec-qat-offload": "option",  # Enable/disable QAT offloading (Intel QuickAssist) for IPsec 
    "device-idle-timeout": "integer",  # Time in seconds that a device must be idle to automatically 
    "user-device-store-max-devices": "integer",  # Maximum number of devices allowed in user device store.
    "user-device-store-max-device-mem": "integer",  # Maximum percentage of total system memory allowed to be used
    "user-device-store-max-users": "integer",  # Maximum number of users allowed in user device store.
    "user-device-store-max-unified-mem": "integer",  # Maximum unified memory allowed in user device store.
    "gui-device-latitude": "string",  # Add the latitude of the location of this FortiGate to positi
    "gui-device-longitude": "string",  # Add the longitude of the location of this FortiGate to posit
    "private-data-encryption": "option",  # Enable/disable private data encryption using an AES 128-bit 
    "auto-auth-extension-device": "option",  # Enable/disable automatic authorization of dedicated Fortinet
    "gui-theme": "option",  # Color scheme for the administration GUI.
    "gui-date-format": "option",  # Default date format used throughout GUI.
    "gui-date-time-source": "option",  # Source from which the FortiGate GUI uses to display date and
    "igmp-state-limit": "integer",  # Maximum number of IGMP memberships (96 - 64000, default = 32
    "cloud-communication": "option",  # Enable/disable all cloud communication.
    "ipsec-ha-seqjump-rate": "integer",  # ESP jump ahead rate (1G - 10G pps equivalent).
    "fortitoken-cloud": "option",  # Enable/disable FortiToken Cloud service.
    "fortitoken-cloud-push-status": "option",  # Enable/disable FTM push service of FortiToken Cloud.
    "fortitoken-cloud-region": "string",  # Region domain of FortiToken Cloud(unset to non-region).
    "fortitoken-cloud-sync-interval": "integer",  # Interval in which to clean up remote users in FortiToken Clo
    "faz-disk-buffer-size": "integer",  # Maximum disk buffer size to temporarily store logs destined 
    "irq-time-accounting": "option",  # Configure CPU IRQ time accounting mode.
    "management-ip": "string",  # Management IP address of this FortiGate. Used to log into th
    "management-port": "integer",  # Overriding port for management connection (Overrides admin p
    "management-port-use-admin-sport": "option",  # Enable/disable use of the admin-sport setting for the manage
    "forticonverter-integration": "option",  # Enable/disable FortiConverter integration service.
    "forticonverter-config-upload": "option",  # Enable/disable config upload to FortiConverter.
    "internet-service-database": "option",  # Configure which Internet Service database size to download f
    "internet-service-download-list": "string",  # Configure which on-demand Internet Service IDs are to be dow
    "early-tcp-npu-session": "option",  # Enable/disable early TCP NPU session.
    "npu-neighbor-update": "option",  # Enable/disable sending of ARP/ICMP6 probing packets to updat
    "delay-tcp-npu-session": "option",  # Enable TCP NPU session delay to guarantee packet order of 3-
    "interface-subnet-usage": "option",  # Enable/disable allowing use of interface-subnet setting in f
    "sflowd-max-children-num": "integer",  # Maximum number of sflowd child processes allowed to run.
    "fortigslb-integration": "option",  # Enable/disable integration with the FortiGSLB cloud service.
    "user-history-password-threshold": "integer",  # Maximum number of previous passwords saved per admin/user (3
    "auth-session-auto-backup": "option",  # Enable/disable automatic and periodic backup of authenticati
    "auth-session-auto-backup-interval": "option",  # Configure automatic authentication session backup interval (
    "scim-https-port": "integer",  # SCIM port (0 - 65535, default = 44559).
    "scim-http-port": "integer",  # SCIM http port (0 - 65535, default = 44558).
    "scim-server-cert": "string",  # Server certificate that the FortiGate uses for SCIM connecti
    "application-bandwidth-tracking": "option",  # Enable/disable application bandwidth tracking.
    "tls-session-cache": "option",  # Enable/disable TLS session cache.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "language": "GUI display language.",
    "gui-ipv6": "Enable/disable IPv6 settings on the GUI.",
    "gui-replacement-message-groups": "Enable/disable replacement message groups on the GUI.",
    "gui-local-out": "Enable/disable Local-out traffic on the GUI.",
    "gui-certificates": "Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI.",
    "gui-custom-language": "Enable/disable custom languages in GUI.",
    "gui-wireless-opensecurity": "Enable/disable wireless open security option on the GUI.",
    "gui-app-detection-sdwan": "Enable/disable Allow app-detection based SD-WAN.",
    "gui-display-hostname": "Enable/disable displaying the FortiGate's hostname on the GUI login page.",
    "gui-fortigate-cloud-sandbox": "Enable/disable displaying FortiGate Cloud Sandbox on the GUI.",
    "gui-firmware-upgrade-warning": "Enable/disable the firmware upgrade warning on the GUI.",
    "gui-forticare-registration-setup-warning": "Enable/disable the FortiCare registration setup warning on the GUI.",
    "gui-auto-upgrade-setup-warning": "Enable/disable the automatic patch upgrade setup prompt on the GUI.",
    "gui-workflow-management": "Enable/disable Workflow management features on the GUI.",
    "gui-cdn-usage": "Enable/disable Load GUI static files from a CDN.",
    "admin-https-ssl-versions": "Allowed TLS versions for web administration.",
    "admin-https-ssl-ciphersuites": "Select one or more TLS 1.3 ciphersuites to enable. Does not affect ciphers in TLS 1.2 and below. At least one must be enabled. To disable all, remove TLS1.3 from admin-https-ssl-versions.",
    "admin-https-ssl-banned-ciphers": "Select one or more cipher technologies that cannot be used in GUI HTTPS negotiations. Only applies to TLS 1.2 and below.",
    "admintimeout": "Number of minutes before an idle administrator session times out (1 - 480 minutes (8 hours), default = 5). A shorter idle timeout is more secure.",
    "admin-console-timeout": "Console login timeout that overrides the admin timeout value (15 - 300 seconds, default = 0, which disables the timeout).",
    "ssd-trim-freq": "How often to run SSD Trim (default = weekly). SSD Trim prevents SSD drive data loss by finding and isolating errors.",
    "ssd-trim-hour": "Hour of the day on which to run SSD Trim (0 - 23, default = 1).",
    "ssd-trim-min": "Minute of the hour on which to run SSD Trim (0 - 59, 60 for random).",
    "ssd-trim-weekday": "Day of week to run SSD Trim.",
    "ssd-trim-date": "Date within a month to run ssd trim.",
    "admin-concurrent": "Enable/disable concurrent administrator logins. Use policy-auth-concurrent for firewall authenticated users.",
    "admin-lockout-threshold": "Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration.",
    "admin-lockout-duration": "Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed login attempts.",
    "refresh": "Statistics refresh interval second(s) in GUI.",
    "interval": "Dead gateway detection interval.",
    "failtime": "Fail-time for server lost.",
    "purdue-level": "Purdue Level of this FortiGate.",
    "daily-restart": "Enable/disable daily restart of FortiGate unit. Use the restart-time option to set the time of day for the restart.",
    "restart-time": "Daily restart time (hh:mm).",
    "wad-restart-mode": "WAD worker restart mode (default = none).",
    "wad-restart-start-time": "WAD workers daily restart time (hh:mm).",
    "wad-restart-end-time": "WAD workers daily restart end time (hh:mm).",
    "wad-p2s-max-body-size": "Maximum size of the body of the local out HTTP request (1 - 32 Mbytes, default = 4).",
    "radius-port": "RADIUS service port number.",
    "speedtestd-server-port": "Speedtest server port number.",
    "speedtestd-ctrl-port": "Speedtest server controller port number.",
    "admin-login-max": "Maximum number of administrators who can be logged in at the same time (1 - 100, default = 100).",
    "remoteauthtimeout": "Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers. (1-300 sec, default = 5).",
    "ldapconntimeout": "Global timeout for connections with remote LDAP servers in milliseconds (1 - 300000, default 500).",
    "batch-cmdb": "Enable/disable batch mode, allowing you to enter a series of CLI commands that will execute as a group once they are loaded.",
    "multi-factor-authentication": "Enforce all login methods to require an additional authentication factor (default = optional).",
    "ssl-min-proto-version": "Minimum supported protocol version for SSL/TLS connections (default = TLSv1.2).",
    "autorun-log-fsck": "Enable/disable automatic log partition check after ungraceful shutdown.",
    "timezone": "Timezone database name. Enter ? to view the list of timezone.",
    "traffic-priority": "Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for traffic prioritization in traffic shaping.",
    "traffic-priority-level": "Default system-wide level of priority for traffic prioritization.",
    "quic-congestion-control-algo": "QUIC congestion control algorithm (default = cubic).",
    "quic-max-datagram-size": "Maximum transmit datagram size (1200 - 1500, default = 1500).",
    "quic-udp-payload-size-shaping-per-cid": "Enable/disable UDP payload size shaping per connection ID (default = enable).",
    "quic-ack-thresold": "Maximum number of unacknowledged packets before sending ACK (2 - 5, default = 3).",
    "quic-pmtud": "Enable/disable path MTU discovery (default = enable).",
    "quic-tls-handshake-timeout": "Time-to-live (TTL) for TLS handshake in seconds (1 - 60, default = 5).",
    "anti-replay": "Level of checking for packet replay and TCP sequence checking.",
    "send-pmtu-icmp": "Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destination unreachable packet and to support PMTUD protocol on your network to reduce fragmentation of packets.",
    "honor-df": "Enable/disable honoring of Don't-Fragment (DF) flag.",
    "pmtu-discovery": "Enable/disable path MTU discovery.",
    "revision-image-auto-backup": "Enable/disable back-up of the latest image revision after the firmware is upgraded.",
    "revision-backup-on-logout": "Enable/disable back-up of the latest configuration revision when an administrator logs out of the CLI or GUI.",
    "management-vdom": "Management virtual domain name.",
    "hostname": "FortiGate unit's hostname. Most models will truncate names longer than 24 characters. Some models support hostnames up to 35 characters.",
    "alias": "Alias for your FortiGate unit.",
    "strong-crypto": "Enable to use strong encryption and only allow strong ciphers and digest for HTTPS/SSH/TLS/SSL functions.",
    "ssl-static-key-ciphers": "Enable/disable static key ciphers in SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256).",
    "snat-route-change": "Enable/disable the ability to change the source NAT route.",
    "ipv6-snat-route-change": "Enable/disable the ability to change the IPv6 source NAT route.",
    "speedtest-server": "Enable/disable speed test server.",
    "cli-audit-log": "Enable/disable CLI audit log.",
    "dh-params": "Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.",
    "fds-statistics": "Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuard. This data is used to improve FortiGuard services and is not shared with external parties and is protected by Fortinet's privacy policy.",
    "fds-statistics-period": "FortiGuard statistics collection period in minutes. (1 - 1440 min (1 min to 24 hours), default = 60).",
    "tcp-option": "Enable SACK, timestamp and MSS TCP options.",
    "lldp-transmission": "Enable/disable Link Layer Discovery Protocol (LLDP) transmission.",
    "lldp-reception": "Enable/disable Link Layer Discovery Protocol (LLDP) reception.",
    "proxy-auth-timeout": "Authentication timeout in minutes for authenticated users (1 - 10000 min, default = 10).",
    "proxy-keep-alive-mode": "Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was authenticated.",
    "proxy-re-authentication-time": "The time limit that users must re-authenticate if proxy-keep-alive-mode is set to re-authenticate (1  - 86400 sec, default=30s.",
    "proxy-auth-lifetime": "Enable/disable authenticated users lifetime control. This is a cap on the total time a proxy user can be authenticated for after which re-authentication will take place.",
    "proxy-auth-lifetime-timeout": "Lifetime timeout in minutes for authenticated users (5  - 65535 min, default=480 (8 hours)).",
    "proxy-resource-mode": "Enable/disable use of the maximum memory usage on the FortiGate unit's proxy processing of resources, such as block lists, allow lists, and external resources.",
    "proxy-cert-use-mgmt-vdom": "Enable/disable using management VDOM to send requests.",
    "sys-perf-log-interval": "Time in minutes between updates of performance statistics logging. (1 - 15 min, default = 5, 0 = disabled).",
    "check-protocol-header": "Level of checking performed on protocol headers. Strict checking is more thorough but may affect performance. Loose checking is OK in most cases.",
    "vip-arp-range": "Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) address range.",
    "reset-sessionless-tcp": "Action to perform if the FortiGate receives a TCP packet but cannot find a corresponding session in its session table. NAT/Route mode only.",
    "allow-traffic-redirect": "Disable to prevent traffic with same local ingress and egress interface from being forwarded without policy check.",
    "ipv6-allow-traffic-redirect": "Disable to prevent IPv6 traffic with same local ingress and egress interface from being forwarded without policy check.",
    "strict-dirty-session-check": "Enable to check the session against the original policy when revalidating. This can prevent dropping of redirected sessions when web-filtering and authentication are enabled together. If this option is enabled, the FortiGate unit deletes a session if a routing or policy change causes the session to no longer match the policy that originally allowed the session.",
    "tcp-halfclose-timer": "Number of seconds the FortiGate unit should wait to close a session after one peer has sent a FIN packet but the other has not responded (1 - 86400 sec (1 day), default = 120).",
    "tcp-halfopen-timer": "Number of seconds the FortiGate unit should wait to close a session after one peer has sent an open session packet but the other has not responded (1 - 86400 sec (1 day), default = 10).",
    "tcp-timewait-timer": "Length of the TCP TIME-WAIT state in seconds (1 - 300 sec, default = 1).",
    "tcp-rst-timer": "Length of the TCP CLOSE state in seconds (5 - 300 sec, default = 5).",
    "udp-idle-timer": "UDP connection session timeout. This command can be useful in managing CPU and memory resources (1 - 86400 seconds (1 day), default = 60).",
    "block-session-timer": "Duration in seconds for blocked sessions (1 - 300 sec  (5 minutes), default = 30).",
    "ip-src-port-range": "IP source port range used for traffic originating from the FortiGate unit.",
    "pre-login-banner": "Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in.",
    "post-login-banner": "Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in.",
    "tftp": "Enable/disable TFTP.",
    "av-failopen": "Set the action to take if the FortiGate is running low on memory or the proxy connection limit has been reached.",
    "av-failopen-session": "When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the action specified by av-failopen.",
    "memory-use-threshold-extreme": "Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total RAM, default = 95).",
    "memory-use-threshold-red": "Threshold at which memory usage forces the FortiGate to enter conserve mode (% of total RAM, default = 88).",
    "memory-use-threshold-green": "Threshold at which memory usage forces the FortiGate to exit conserve mode (% of total RAM, default = 82).",
    "ip-fragment-mem-thresholds": "Maximum memory (MB) used to reassemble IPv4/IPv6 fragments.",
    "ip-fragment-timeout": "Timeout value in seconds for any fragment not being reassembled",
    "ipv6-fragment-timeout": "Timeout value in seconds for any IPv6 fragment not being reassembled",
    "cpu-use-threshold": "Threshold at which CPU usage is reported (% of total CPU, default = 90).",
    "log-single-cpu-high": "Enable/disable logging the event of a single CPU core reaching CPU usage threshold.",
    "check-reset-range": "Configure ICMP error message verification. You can either apply strict RST range checking or disable it.",
    "upgrade-report": "Enable/disable the generation of an upgrade report when upgrading the firmware.",
    "admin-port": "Administrative access port for HTTP. (1 - 65535, default = 80).",
    "admin-sport": "Administrative access port for HTTPS. (1 - 65535, default = 443).",
    "admin-host": "Administrative host for HTTP and HTTPS. When set, will be used in lieu of the client's Host header for any redirection.",
    "admin-https-redirect": "Enable/disable redirection of HTTP administration access to HTTPS.",
    "admin-hsts-max-age": "HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will reset any HSTS records in the browser.When admin-https-redirect is disabled the header max-age will be 0.",
    "admin-ssh-password": "Enable/disable password authentication for SSH admin access.",
    "admin-restrict-local": "Enable/disable local admin authentication restriction when remote authenticator is up and running (default = disable).",
    "admin-ssh-port": "Administrative access port for SSH. (1 - 65535, default = 22).",
    "admin-ssh-grace-time": "Maximum time in seconds permitted between making an SSH connection to the FortiGate unit and authenticating (10 - 3600 sec (1 hour), default 120).",
    "admin-ssh-v1": "Enable/disable SSH v1 compatibility.",
    "admin-telnet": "Enable/disable TELNET service.",
    "admin-telnet-port": "Administrative access port for TELNET. (1 - 65535, default = 23).",
    "admin-forticloud-sso-login": "Enable/disable FortiCloud admin login via SSO.",
    "admin-forticloud-sso-default-profile": "Override access profile.",
    "default-service-source-port": "Default service source port range (default = 1 - 65535).",
    "admin-server-cert": "Server certificate that the FortiGate uses for HTTPS administrative connections.",
    "admin-https-pki-required": "Enable/disable admin login method. Enable to force administrators to provide a valid certificate to log in if PKI is enabled. Disable to allow administrators to log in with a certificate or password.",
    "wifi-certificate": "Certificate to use for WiFi authentication.",
    "dhcp-lease-backup-interval": "DHCP leases backup interval in seconds (10 - 3600, default = 60).",
    "wifi-ca-certificate": "CA certificate that verifies the WiFi certificate.",
    "auth-http-port": "User authentication HTTP port. (1 - 65535, default = 1000).",
    "auth-https-port": "User authentication HTTPS port. (1 - 65535, default = 1003).",
    "auth-ike-saml-port": "User IKE SAML authentication port (0 - 65535, default = 1001).",
    "auth-keepalive": "Enable to prevent user authentication sessions from timing out when idle.",
    "policy-auth-concurrent": "Number of concurrent firewall use logins from the same user (1 - 100, default = 0 means no limit).",
    "auth-session-limit": "Action to take when the number of allowed user authenticated sessions is reached.",
    "auth-cert": "Server certificate that the FortiGate uses for HTTPS firewall authentication connections.",
    "clt-cert-req": "Enable/disable requiring administrators to have a client certificate to log into the GUI using HTTPS.",
    "fortiservice-port": "FortiService port (1 - 65535, default = 8013). Used by FortiClient endpoint compliance. Older versions of FortiClient used a different port.",
    "cfg-save": "Configuration file save mode for CLI changes.",
    "cfg-revert-timeout": "Time-out for reverting to the last saved configuration. (10 - 4294967295 seconds, default = 600).",
    "reboot-upon-config-restore": "Enable/disable reboot of system upon restoring configuration.",
    "admin-scp": "Enable/disable SCP support for system configuration backup, restore, and firmware file upload.",
    "wireless-controller": "Enable/disable the wireless controller feature to use the FortiGate unit to manage FortiAPs.",
    "wireless-controller-port": "Port used for the control channel in wireless controller mode (wireless-mode is ac). The data channel port is the control channel port number plus one (1024 - 49150, default = 5246).",
    "fortiextender-data-port": "FortiExtender data port (1024 - 49150, default = 25246).",
    "fortiextender": "Enable/disable FortiExtender.",
    "extender-controller-reserved-network": "Configure reserved network subnet for managed LAN extension FortiExtender units. This is available when the FortiExtender daemon is running.",
    "fortiextender-discovery-lockdown": "Enable/disable FortiExtender CAPWAP lockdown.",
    "fortiextender-vlan-mode": "Enable/disable FortiExtender VLAN mode.",
    "fortiextender-provision-on-authorization": "Enable/disable automatic provisioning of latest FortiExtender firmware on authorization.",
    "switch-controller": "Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself.",
    "switch-controller-reserved-network": "Configure reserved network subnet for managed switches. This is available when the switch controller is enabled.",
    "dnsproxy-worker-count": "DNS proxy worker count. For a FortiGate with multiple logical CPUs, you can set the DNS process number from 1 to the number of logical CPUs.",
    "url-filter-count": "URL filter daemon count.",
    "httpd-max-worker-count": "Maximum number of simultaneous HTTP requests that will be served. This number may affect GUI and REST API performance (0 - 128, default = 0 means let system decide).",
    "proxy-worker-count": "Proxy worker count.",
    "scanunit-count": "Number of scanunits. The range and the default depend on the number of CPUs. Only available on FortiGate units with multiple CPUs.",
    "fgd-alert-subscription": "Type of alert to retrieve from FortiGuard.",
    "ipv6-accept-dad": "Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD).",
    "ipv6-allow-anycast-probe": "Enable/disable IPv6 address probe through Anycast.",
    "ipv6-allow-multicast-probe": "Enable/disable IPv6 address probe through Multicast.",
    "ipv6-allow-local-in-silent-drop": "Enable/disable silent drop of IPv6 local-in traffic.",
    "csr-ca-attribute": "Enable/disable the CA attribute in certificates. Some CA servers reject CSRs that have the CA attribute.",
    "wimax-4g-usb": "Enable/disable comparability with WiMAX 4G USB devices.",
    "cert-chain-max": "Maximum number of certificates that can be traversed in a certificate chain.",
    "sslvpn-max-worker-count": "Maximum number of Agentless VPN processes. Upper limit for this value is the number of CPUs and depends on the model. Default value of zero means the sslvpnd daemon decides the number of worker processes.",
    "sslvpn-affinity": "Agentless VPN CPU affinity.",
    "sslvpn-web-mode": "Enable/disable Agentless VPN web mode.",
    "two-factor-ftk-expiry": "FortiToken authentication session timeout (60 - 600 sec (10 minutes), default = 60).",
    "two-factor-email-expiry": "Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes), default = 60).",
    "two-factor-sms-expiry": "SMS-based two-factor authentication session timeout (30 - 300 sec, default = 60).",
    "two-factor-fac-expiry": "FortiAuthenticator token authentication session timeout (10 - 3600 seconds (1 hour), default = 60).",
    "two-factor-ftm-expiry": "FortiToken Mobile session timeout (1 - 168 hours (7 days), default = 72).",
    "per-user-bal": "Enable/disable per-user block/allow list filter.",
    "wad-worker-count": "Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN optimization, explicit proxy, and web caching is handled by all of the CPU cores in a FortiGate unit.",
    "wad-csvc-cs-count": "Number of concurrent WAD-cache-service object-cache processes.",
    "wad-csvc-db-count": "Number of concurrent WAD-cache-service byte-cache processes.",
    "wad-source-affinity": "Enable/disable dispatching traffic to WAD workers based on source affinity.",
    "wad-memory-change-granularity": "Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting TCP window size for any active connection.",
    "login-timestamp": "Enable/disable login time recording.",
    "ip-conflict-detection": "Enable/disable logging of IPv4 address conflict detection.",
    "miglogd-children": "Number of logging (miglogd) processes to be allowed to run. Higher number can reduce performance; lower number can slow log processing time. ",
    "special-file-23-support": "Enable/disable detection of those special format files when using Data Loss Prevention.",
    "log-uuid-address": "Enable/disable insertion of address UUIDs to traffic logs.",
    "log-ssl-connection": "Enable/disable logging of SSL connection events.",
    "gui-rest-api-cache": "Enable/disable REST API result caching on FortiGate.",
    "rest-api-key-url-query": "Enable/disable support for passing REST API keys through URL query parameters.",
    "arp-max-entry": "Maximum number of dynamically learned MAC addresses that can be added to the ARP table (131072 - 2147483647, default = 131072).",
    "ha-affinity": "Affinity setting for HA daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "bfd-affinity": "Affinity setting for BFD daemon (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "cmdbsvr-affinity": "Affinity setting for cmdbsvr (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "av-affinity": "Affinity setting for AV scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "wad-affinity": "Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "ips-affinity": "Affinity setting for IPS (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed CPUs must be less than total number of IPS engine daemons).",
    "miglog-affinity": "Affinity setting for logging (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "syslog-affinity": "Affinity setting for syslog (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "url-filter-affinity": "URL filter CPU affinity.",
    "router-affinity": "Affinity setting for BFD/VRRP/BGP/OSPF daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).",
    "ndp-max-entry": "Maximum number of NDP table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries).",
    "br-fdb-max-entry": "Maximum number of bridge forwarding database (FDB) entries.",
    "max-route-cache-size": "Maximum number of IP route cache entries (0 - 2147483647).",
    "ipsec-qat-offload": "Enable/disable QAT offloading (Intel QuickAssist) for IPsec VPN traffic. QuickAssist can accelerate IPsec encryption and decryption.",
    "device-idle-timeout": "Time in seconds that a device must be idle to automatically log the device user out. (30 - 31536000 sec (30 sec to 1 year), default = 300).",
    "user-device-store-max-devices": "Maximum number of devices allowed in user device store.",
    "user-device-store-max-device-mem": "Maximum percentage of total system memory allowed to be used for devices in the user device store.",
    "user-device-store-max-users": "Maximum number of users allowed in user device store.",
    "user-device-store-max-unified-mem": "Maximum unified memory allowed in user device store.",
    "gui-device-latitude": "Add the latitude of the location of this FortiGate to position it on the Threat Map.",
    "gui-device-longitude": "Add the longitude of the location of this FortiGate to position it on the Threat Map.",
    "private-data-encryption": "Enable/disable private data encryption using an AES 128-bit key or passpharse.",
    "auto-auth-extension-device": "Enable/disable automatic authorization of dedicated Fortinet extension devices.",
    "gui-theme": "Color scheme for the administration GUI.",
    "gui-date-format": "Default date format used throughout GUI.",
    "gui-date-time-source": "Source from which the FortiGate GUI uses to display date and time entries.",
    "igmp-state-limit": "Maximum number of IGMP memberships (96 - 64000, default = 3200).",
    "cloud-communication": "Enable/disable all cloud communication.",
    "ipsec-ha-seqjump-rate": "ESP jump ahead rate (1G - 10G pps equivalent).",
    "fortitoken-cloud": "Enable/disable FortiToken Cloud service.",
    "fortitoken-cloud-push-status": "Enable/disable FTM push service of FortiToken Cloud.",
    "fortitoken-cloud-region": "Region domain of FortiToken Cloud(unset to non-region).",
    "fortitoken-cloud-sync-interval": "Interval in which to clean up remote users in FortiToken Cloud (0 - 336 hours (14 days), default = 24, disable = 0).",
    "faz-disk-buffer-size": "Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. To be used in the event that FortiAnalyzer is unavailable.",
    "irq-time-accounting": "Configure CPU IRQ time accounting mode.",
    "management-ip": "Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric.",
    "management-port": "Overriding port for management connection (Overrides admin port).",
    "management-port-use-admin-sport": "Enable/disable use of the admin-sport setting for the management port. If disabled, FortiGate will allow user to specify management-port.",
    "forticonverter-integration": "Enable/disable FortiConverter integration service.",
    "forticonverter-config-upload": "Enable/disable config upload to FortiConverter.",
    "internet-service-database": "Configure which Internet Service database size to download from FortiGuard and use.",
    "internet-service-download-list": "Configure which on-demand Internet Service IDs are to be downloaded.",
    "early-tcp-npu-session": "Enable/disable early TCP NPU session.",
    "npu-neighbor-update": "Enable/disable sending of ARP/ICMP6 probing packets to update neighbors for offloaded sessions.",
    "delay-tcp-npu-session": "Enable TCP NPU session delay to guarantee packet order of 3-way handshake.",
    "interface-subnet-usage": "Enable/disable allowing use of interface-subnet setting in firewall addresses (default = enable).",
    "sflowd-max-children-num": "Maximum number of sflowd child processes allowed to run.",
    "fortigslb-integration": "Enable/disable integration with the FortiGSLB cloud service.",
    "user-history-password-threshold": "Maximum number of previous passwords saved per admin/user (3 - 15, default = 3).",
    "auth-session-auto-backup": "Enable/disable automatic and periodic backup of authentication sessions (default = disable). Sessions are restored upon bootup.",
    "auth-session-auto-backup-interval": "Configure automatic authentication session backup interval (default = 15min).",
    "scim-https-port": "SCIM port (0 - 65535, default = 44559).",
    "scim-http-port": "SCIM http port (0 - 65535, default = 44558).",
    "scim-server-cert": "Server certificate that the FortiGate uses for SCIM connections.",
    "application-bandwidth-tracking": "Enable/disable application bandwidth tracking.",
    "tls-session-cache": "Enable/disable TLS session cache.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "admintimeout": {"type": "integer", "min": 1, "max": 480},
    "admin-console-timeout": {"type": "integer", "min": 15, "max": 300},
    "ssd-trim-hour": {"type": "integer", "min": 0, "max": 23},
    "ssd-trim-min": {"type": "integer", "min": 0, "max": 60},
    "ssd-trim-date": {"type": "integer", "min": 1, "max": 31},
    "admin-lockout-threshold": {"type": "integer", "min": 1, "max": 10},
    "admin-lockout-duration": {"type": "integer", "min": 1, "max": 2147483647},
    "refresh": {"type": "integer", "min": 0, "max": 4294967295},
    "interval": {"type": "integer", "min": 0, "max": 4294967295},
    "failtime": {"type": "integer", "min": 0, "max": 4294967295},
    "wad-p2s-max-body-size": {"type": "integer", "min": 1, "max": 32},
    "radius-port": {"type": "integer", "min": 1, "max": 65535},
    "speedtestd-server-port": {"type": "integer", "min": 1, "max": 65535},
    "speedtestd-ctrl-port": {"type": "integer", "min": 1, "max": 65535},
    "admin-login-max": {"type": "integer", "min": 1, "max": 100},
    "remoteauthtimeout": {"type": "integer", "min": 1, "max": 300},
    "ldapconntimeout": {"type": "integer", "min": 1, "max": 300000},
    "timezone": {"type": "string", "max_length": 63},
    "quic-max-datagram-size": {"type": "integer", "min": 1200, "max": 1500},
    "quic-ack-thresold": {"type": "integer", "min": 2, "max": 5},
    "quic-tls-handshake-timeout": {"type": "integer", "min": 1, "max": 60},
    "management-vdom": {"type": "string", "max_length": 31},
    "hostname": {"type": "string", "max_length": 35},
    "alias": {"type": "string", "max_length": 35},
    "fds-statistics-period": {"type": "integer", "min": 1, "max": 1440},
    "proxy-auth-timeout": {"type": "integer", "min": 1, "max": 10000},
    "proxy-re-authentication-time": {"type": "integer", "min": 1, "max": 86400},
    "proxy-auth-lifetime-timeout": {"type": "integer", "min": 5, "max": 65535},
    "sys-perf-log-interval": {"type": "integer", "min": 0, "max": 15},
    "tcp-halfclose-timer": {"type": "integer", "min": 1, "max": 86400},
    "tcp-halfopen-timer": {"type": "integer", "min": 1, "max": 86400},
    "tcp-timewait-timer": {"type": "integer", "min": 0, "max": 300},
    "tcp-rst-timer": {"type": "integer", "min": 5, "max": 300},
    "udp-idle-timer": {"type": "integer", "min": 1, "max": 86400},
    "block-session-timer": {"type": "integer", "min": 1, "max": 300},
    "memory-use-threshold-extreme": {"type": "integer", "min": 70, "max": 97},
    "memory-use-threshold-red": {"type": "integer", "min": 70, "max": 97},
    "memory-use-threshold-green": {"type": "integer", "min": 70, "max": 97},
    "ip-fragment-mem-thresholds": {"type": "integer", "min": 32, "max": 2047},
    "ip-fragment-timeout": {"type": "integer", "min": 3, "max": 30},
    "ipv6-fragment-timeout": {"type": "integer", "min": 5, "max": 60},
    "cpu-use-threshold": {"type": "integer", "min": 50, "max": 99},
    "admin-port": {"type": "integer", "min": 1, "max": 65535},
    "admin-sport": {"type": "integer", "min": 1, "max": 65535},
    "admin-host": {"type": "string", "max_length": 255},
    "admin-hsts-max-age": {"type": "integer", "min": 0, "max": 2147483647},
    "admin-ssh-port": {"type": "integer", "min": 1, "max": 65535},
    "admin-ssh-grace-time": {"type": "integer", "min": 10, "max": 3600},
    "admin-telnet-port": {"type": "integer", "min": 1, "max": 65535},
    "admin-forticloud-sso-default-profile": {"type": "string", "max_length": 35},
    "admin-server-cert": {"type": "string", "max_length": 35},
    "wifi-certificate": {"type": "string", "max_length": 35},
    "dhcp-lease-backup-interval": {"type": "integer", "min": 10, "max": 3600},
    "wifi-ca-certificate": {"type": "string", "max_length": 79},
    "auth-http-port": {"type": "integer", "min": 1, "max": 65535},
    "auth-https-port": {"type": "integer", "min": 1, "max": 65535},
    "auth-ike-saml-port": {"type": "integer", "min": 0, "max": 65535},
    "policy-auth-concurrent": {"type": "integer", "min": 0, "max": 100},
    "auth-cert": {"type": "string", "max_length": 35},
    "fortiservice-port": {"type": "integer", "min": 1, "max": 65535},
    "cfg-revert-timeout": {"type": "integer", "min": 10, "max": 4294967295},
    "wireless-controller-port": {"type": "integer", "min": 1024, "max": 49150},
    "fortiextender-data-port": {"type": "integer", "min": 1024, "max": 49150},
    "dnsproxy-worker-count": {"type": "integer", "min": 1, "max": 2},
    "url-filter-count": {"type": "integer", "min": 1, "max": 1},
    "httpd-max-worker-count": {"type": "integer", "min": 0, "max": 128},
    "proxy-worker-count": {"type": "integer", "min": 1, "max": 2},
    "scanunit-count": {"type": "integer", "min": 2, "max": 2},
    "ipv6-accept-dad": {"type": "integer", "min": 0, "max": 2},
    "cert-chain-max": {"type": "integer", "min": 1, "max": 2147483647},
    "sslvpn-max-worker-count": {"type": "integer", "min": 0, "max": 1},
    "sslvpn-affinity": {"type": "string", "max_length": 79},
    "two-factor-ftk-expiry": {"type": "integer", "min": 60, "max": 600},
    "two-factor-email-expiry": {"type": "integer", "min": 30, "max": 300},
    "two-factor-sms-expiry": {"type": "integer", "min": 30, "max": 300},
    "two-factor-fac-expiry": {"type": "integer", "min": 10, "max": 3600},
    "two-factor-ftm-expiry": {"type": "integer", "min": 1, "max": 168},
    "wad-worker-count": {"type": "integer", "min": 0, "max": 2},
    "wad-csvc-cs-count": {"type": "integer", "min": 1, "max": 1},
    "wad-csvc-db-count": {"type": "integer", "min": 0, "max": 2},
    "wad-memory-change-granularity": {"type": "integer", "min": 5, "max": 25},
    "miglogd-children": {"type": "integer", "min": 0, "max": 15},
    "arp-max-entry": {"type": "integer", "min": 131072, "max": 2147483647},
    "ha-affinity": {"type": "string", "max_length": 79},
    "bfd-affinity": {"type": "string", "max_length": 79},
    "cmdbsvr-affinity": {"type": "string", "max_length": 79},
    "av-affinity": {"type": "string", "max_length": 79},
    "wad-affinity": {"type": "string", "max_length": 79},
    "ips-affinity": {"type": "string", "max_length": 79},
    "miglog-affinity": {"type": "string", "max_length": 79},
    "syslog-affinity": {"type": "string", "max_length": 79},
    "url-filter-affinity": {"type": "string", "max_length": 79},
    "router-affinity": {"type": "string", "max_length": 79},
    "ndp-max-entry": {"type": "integer", "min": 65536, "max": 2147483647},
    "br-fdb-max-entry": {"type": "integer", "min": 8192, "max": 2147483647},
    "max-route-cache-size": {"type": "integer", "min": 0, "max": 2147483647},
    "device-idle-timeout": {"type": "integer", "min": 30, "max": 31536000},
    "user-device-store-max-devices": {"type": "integer", "min": 31262, "max": 89320},
    "user-device-store-max-device-mem": {"type": "integer", "min": 1, "max": 5},
    "user-device-store-max-users": {"type": "integer", "min": 31262, "max": 89320},
    "user-device-store-max-unified-mem": {"type": "integer", "min": 62524579, "max": 625245798},
    "gui-device-latitude": {"type": "string", "max_length": 19},
    "gui-device-longitude": {"type": "string", "max_length": 19},
    "igmp-state-limit": {"type": "integer", "min": 96, "max": 128000},
    "ipsec-ha-seqjump-rate": {"type": "integer", "min": 1, "max": 10},
    "fortitoken-cloud-region": {"type": "string", "max_length": 63},
    "fortitoken-cloud-sync-interval": {"type": "integer", "min": 0, "max": 336},
    "management-ip": {"type": "string", "max_length": 255},
    "management-port": {"type": "integer", "min": 1, "max": 65535},
    "sflowd-max-children-num": {"type": "integer", "min": 0, "max": 1},
    "user-history-password-threshold": {"type": "integer", "min": 3, "max": 15},
    "scim-https-port": {"type": "integer", "min": 0, "max": 65535},
    "scim-http-port": {"type": "integer", "min": 0, "max": 65535},
    "scim-server-cert": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "internet-service-download-list": {
        "id": {
            "type": "integer",
            "help": "Internet Service ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_LANGUAGE = [
    "english",
    "french",
    "spanish",
    "portuguese",
    "japanese",
    "trach",
    "simch",
    "korean",
]
VALID_BODY_GUI_IPV6 = [
    "enable",
    "disable",
]
VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS = [
    "enable",
    "disable",
]
VALID_BODY_GUI_LOCAL_OUT = [
    "enable",
    "disable",
]
VALID_BODY_GUI_CERTIFICATES = [
    "enable",
    "disable",
]
VALID_BODY_GUI_CUSTOM_LANGUAGE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WIRELESS_OPENSECURITY = [
    "enable",
    "disable",
]
VALID_BODY_GUI_APP_DETECTION_SDWAN = [
    "enable",
    "disable",
]
VALID_BODY_GUI_DISPLAY_HOSTNAME = [
    "enable",
    "disable",
]
VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX = [
    "enable",
    "disable",
]
VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING = [
    "enable",
    "disable",
]
VALID_BODY_GUI_WORKFLOW_MANAGEMENT = [
    "enable",
    "disable",
]
VALID_BODY_GUI_CDN_USAGE = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS = [
    "tlsv1-1",
    "tlsv1-2",
    "tlsv1-3",
]
VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES = [
    "TLS-AES-128-GCM-SHA256",
    "TLS-AES-256-GCM-SHA384",
    "TLS-CHACHA20-POLY1305-SHA256",
    "TLS-AES-128-CCM-SHA256",
    "TLS-AES-128-CCM-8-SHA256",
]
VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS = [
    "RSA",
    "DHE",
    "ECDHE",
    "DSS",
    "ECDSA",
    "AES",
    "AESGCM",
    "CAMELLIA",
    "3DES",
    "SHA1",
    "SHA256",
    "SHA384",
    "STATIC",
    "CHACHA20",
    "ARIA",
    "AESCCM",
]
VALID_BODY_SSD_TRIM_FREQ = [
    "never",
    "hourly",
    "daily",
    "weekly",
    "monthly",
]
VALID_BODY_SSD_TRIM_WEEKDAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_ADMIN_CONCURRENT = [
    "enable",
    "disable",
]
VALID_BODY_PURDUE_LEVEL = [
    "1",
    "1.5",
    "2",
    "2.5",
    "3",
    "3.5",
    "4",
    "5",
    "5.5",
]
VALID_BODY_DAILY_RESTART = [
    "enable",
    "disable",
]
VALID_BODY_WAD_RESTART_MODE = [
    "none",
    "time",
    "memory",
]
VALID_BODY_BATCH_CMDB = [
    "enable",
    "disable",
]
VALID_BODY_MULTI_FACTOR_AUTHENTICATION = [
    "optional",
    "mandatory",
]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_AUTORUN_LOG_FSCK = [
    "enable",
    "disable",
]
VALID_BODY_TRAFFIC_PRIORITY = [
    "tos",
    "dscp",
]
VALID_BODY_TRAFFIC_PRIORITY_LEVEL = [
    "low",
    "medium",
    "high",
]
VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO = [
    "cubic",
    "bbr",
    "bbr2",
    "reno",
]
VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID = [
    "enable",
    "disable",
]
VALID_BODY_QUIC_PMTUD = [
    "enable",
    "disable",
]
VALID_BODY_ANTI_REPLAY = [
    "disable",
    "loose",
    "strict",
]
VALID_BODY_SEND_PMTU_ICMP = [
    "enable",
    "disable",
]
VALID_BODY_HONOR_DF = [
    "enable",
    "disable",
]
VALID_BODY_PMTU_DISCOVERY = [
    "enable",
    "disable",
]
VALID_BODY_REVISION_IMAGE_AUTO_BACKUP = [
    "enable",
    "disable",
]
VALID_BODY_REVISION_BACKUP_ON_LOGOUT = [
    "enable",
    "disable",
]
VALID_BODY_STRONG_CRYPTO = [
    "enable",
    "disable",
]
VALID_BODY_SSL_STATIC_KEY_CIPHERS = [
    "enable",
    "disable",
]
VALID_BODY_SNAT_ROUTE_CHANGE = [
    "enable",
    "disable",
]
VALID_BODY_IPV6_SNAT_ROUTE_CHANGE = [
    "enable",
    "disable",
]
VALID_BODY_SPEEDTEST_SERVER = [
    "enable",
    "disable",
]
VALID_BODY_CLI_AUDIT_LOG = [
    "enable",
    "disable",
]
VALID_BODY_DH_PARAMS = [
    "1024",
    "1536",
    "2048",
    "3072",
    "4096",
    "6144",
    "8192",
]
VALID_BODY_FDS_STATISTICS = [
    "enable",
    "disable",
]
VALID_BODY_TCP_OPTION = [
    "enable",
    "disable",
]
VALID_BODY_LLDP_TRANSMISSION = [
    "enable",
    "disable",
]
VALID_BODY_LLDP_RECEPTION = [
    "enable",
    "disable",
]
VALID_BODY_PROXY_KEEP_ALIVE_MODE = [
    "session",
    "traffic",
    "re-authentication",
]
VALID_BODY_PROXY_AUTH_LIFETIME = [
    "enable",
    "disable",
]
VALID_BODY_PROXY_RESOURCE_MODE = [
    "enable",
    "disable",
]
VALID_BODY_PROXY_CERT_USE_MGMT_VDOM = [
    "enable",
    "disable",
]
VALID_BODY_CHECK_PROTOCOL_HEADER = [
    "loose",
    "strict",
]
VALID_BODY_VIP_ARP_RANGE = [
    "unlimited",
    "restricted",
]
VALID_BODY_RESET_SESSIONLESS_TCP = [
    "enable",
    "disable",
]
VALID_BODY_ALLOW_TRAFFIC_REDIRECT = [
    "enable",
    "disable",
]
VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT = [
    "enable",
    "disable",
]
VALID_BODY_STRICT_DIRTY_SESSION_CHECK = [
    "enable",
    "disable",
]
VALID_BODY_PRE_LOGIN_BANNER = [
    "enable",
    "disable",
]
VALID_BODY_POST_LOGIN_BANNER = [
    "disable",
    "enable",
]
VALID_BODY_TFTP = [
    "enable",
    "disable",
]
VALID_BODY_AV_FAILOPEN = [
    "pass",
    "off",
    "one-shot",
]
VALID_BODY_AV_FAILOPEN_SESSION = [
    "enable",
    "disable",
]
VALID_BODY_LOG_SINGLE_CPU_HIGH = [
    "enable",
    "disable",
]
VALID_BODY_CHECK_RESET_RANGE = [
    "strict",
    "disable",
]
VALID_BODY_UPGRADE_REPORT = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_HTTPS_REDIRECT = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_SSH_PASSWORD = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_RESTRICT_LOCAL = [
    "all",
    "non-console-only",
    "disable",
]
VALID_BODY_ADMIN_SSH_V1 = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_TELNET = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_KEEPALIVE = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_SESSION_LIMIT = [
    "block-new",
    "logout-inactive",
]
VALID_BODY_CLT_CERT_REQ = [
    "enable",
    "disable",
]
VALID_BODY_CFG_SAVE = [
    "automatic",
    "manual",
    "revert",
]
VALID_BODY_REBOOT_UPON_CONFIG_RESTORE = [
    "enable",
    "disable",
]
VALID_BODY_ADMIN_SCP = [
    "enable",
    "disable",
]
VALID_BODY_WIRELESS_CONTROLLER = [
    "enable",
    "disable",
]
VALID_BODY_FORTIEXTENDER = [
    "disable",
    "enable",
]
VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN = [
    "disable",
    "enable",
]
VALID_BODY_FORTIEXTENDER_VLAN_MODE = [
    "enable",
    "disable",
]
VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION = [
    "enable",
    "disable",
]
VALID_BODY_SWITCH_CONTROLLER = [
    "disable",
    "enable",
]
VALID_BODY_FGD_ALERT_SUBSCRIPTION = [
    "advisory",
    "latest-threat",
    "latest-virus",
    "latest-attack",
    "new-antivirus-db",
    "new-attack-db",
]
VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE = [
    "enable",
    "disable",
]
VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE = [
    "enable",
    "disable",
]
VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP = [
    "enable",
    "disable",
]
VALID_BODY_CSR_CA_ATTRIBUTE = [
    "enable",
    "disable",
]
VALID_BODY_WIMAX_4G_USB = [
    "enable",
    "disable",
]
VALID_BODY_SSLVPN_WEB_MODE = [
    "enable",
    "disable",
]
VALID_BODY_PER_USER_BAL = [
    "enable",
    "disable",
]
VALID_BODY_WAD_SOURCE_AFFINITY = [
    "disable",
    "enable",
]
VALID_BODY_LOGIN_TIMESTAMP = [
    "enable",
    "disable",
]
VALID_BODY_IP_CONFLICT_DETECTION = [
    "enable",
    "disable",
]
VALID_BODY_SPECIAL_FILE_23_SUPPORT = [
    "disable",
    "enable",
]
VALID_BODY_LOG_UUID_ADDRESS = [
    "enable",
    "disable",
]
VALID_BODY_LOG_SSL_CONNECTION = [
    "enable",
    "disable",
]
VALID_BODY_GUI_REST_API_CACHE = [
    "enable",
    "disable",
]
VALID_BODY_REST_API_KEY_URL_QUERY = [
    "enable",
    "disable",
]
VALID_BODY_IPSEC_QAT_OFFLOAD = [
    "enable",
    "disable",
]
VALID_BODY_PRIVATE_DATA_ENCRYPTION = [
    "disable",
    "enable",
]
VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE = [
    "enable",
    "disable",
]
VALID_BODY_GUI_THEME = [
    "jade",
    "neutrino",
    "mariner",
    "graphite",
    "melongene",
    "jet-stream",
    "security-fabric",
    "retro",
    "dark-matter",
    "onyx",
    "eclipse",
]
VALID_BODY_GUI_DATE_FORMAT = [
    "yyyy/MM/dd",
    "dd/MM/yyyy",
    "MM/dd/yyyy",
    "yyyy-MM-dd",
    "dd-MM-yyyy",
    "MM-dd-yyyy",
]
VALID_BODY_GUI_DATE_TIME_SOURCE = [
    "system",
    "browser",
]
VALID_BODY_CLOUD_COMMUNICATION = [
    "enable",
    "disable",
]
VALID_BODY_FORTITOKEN_CLOUD = [
    "enable",
    "disable",
]
VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_IRQ_TIME_ACCOUNTING = [
    "auto",
    "force",
]
VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT = [
    "enable",
    "disable",
]
VALID_BODY_FORTICONVERTER_INTEGRATION = [
    "enable",
    "disable",
]
VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD = [
    "once",
    "disable",
]
VALID_BODY_INTERNET_SERVICE_DATABASE = [
    "mini",
    "standard",
    "full",
    "on-demand",
]
VALID_BODY_EARLY_TCP_NPU_SESSION = [
    "enable",
    "disable",
]
VALID_BODY_NPU_NEIGHBOR_UPDATE = [
    "enable",
    "disable",
]
VALID_BODY_DELAY_TCP_NPU_SESSION = [
    "enable",
    "disable",
]
VALID_BODY_INTERFACE_SUBNET_USAGE = [
    "disable",
    "enable",
]
VALID_BODY_FORTIGSLB_INTEGRATION = [
    "disable",
    "enable",
]
VALID_BODY_AUTH_SESSION_AUTO_BACKUP = [
    "enable",
    "disable",
]
VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL = [
    "1min",
    "5min",
    "15min",
    "30min",
    "1hr",
]
VALID_BODY_APPLICATION_BANDWIDTH_TRACKING = [
    "disable",
    "enable",
]
VALID_BODY_TLS_SESSION_CACHE = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_global_setting_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/global_setting.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_global_setting_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_global_setting_get(
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
    Validate required fields for system/global_setting.

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


def validate_system_global_setting_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/global_setting object.

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
        ...     "restart-time": True,  # Daily restart time (hh:mm).
        ...     "wad-restart-start-time": True,  # WAD workers daily restart time (hh:mm).
        ... }
        >>> is_valid, error = validate_system_global_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "restart-time": True,
        ...     "language": "english",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_global_setting_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["language"] = "invalid-value"
        >>> is_valid, error = validate_system_global_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_global_setting_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "language" in payload:
        value = payload["language"]
        if value not in VALID_BODY_LANGUAGE:
            desc = FIELD_DESCRIPTIONS.get("language", "")
            error_msg = f"Invalid value for 'language': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LANGUAGE)}"
            error_msg += f"\n  → Example: language='{{ VALID_BODY_LANGUAGE[0] }}'"
            return (False, error_msg)
    if "gui-ipv6" in payload:
        value = payload["gui-ipv6"]
        if value not in VALID_BODY_GUI_IPV6:
            desc = FIELD_DESCRIPTIONS.get("gui-ipv6", "")
            error_msg = f"Invalid value for 'gui-ipv6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_IPV6)}"
            error_msg += f"\n  → Example: gui-ipv6='{{ VALID_BODY_GUI_IPV6[0] }}'"
            return (False, error_msg)
    if "gui-replacement-message-groups" in payload:
        value = payload["gui-replacement-message-groups"]
        if value not in VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS:
            desc = FIELD_DESCRIPTIONS.get("gui-replacement-message-groups", "")
            error_msg = f"Invalid value for 'gui-replacement-message-groups': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS)}"
            error_msg += f"\n  → Example: gui-replacement-message-groups='{{ VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS[0] }}'"
            return (False, error_msg)
    if "gui-local-out" in payload:
        value = payload["gui-local-out"]
        if value not in VALID_BODY_GUI_LOCAL_OUT:
            desc = FIELD_DESCRIPTIONS.get("gui-local-out", "")
            error_msg = f"Invalid value for 'gui-local-out': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_LOCAL_OUT)}"
            error_msg += f"\n  → Example: gui-local-out='{{ VALID_BODY_GUI_LOCAL_OUT[0] }}'"
            return (False, error_msg)
    if "gui-certificates" in payload:
        value = payload["gui-certificates"]
        if value not in VALID_BODY_GUI_CERTIFICATES:
            desc = FIELD_DESCRIPTIONS.get("gui-certificates", "")
            error_msg = f"Invalid value for 'gui-certificates': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_CERTIFICATES)}"
            error_msg += f"\n  → Example: gui-certificates='{{ VALID_BODY_GUI_CERTIFICATES[0] }}'"
            return (False, error_msg)
    if "gui-custom-language" in payload:
        value = payload["gui-custom-language"]
        if value not in VALID_BODY_GUI_CUSTOM_LANGUAGE:
            desc = FIELD_DESCRIPTIONS.get("gui-custom-language", "")
            error_msg = f"Invalid value for 'gui-custom-language': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_CUSTOM_LANGUAGE)}"
            error_msg += f"\n  → Example: gui-custom-language='{{ VALID_BODY_GUI_CUSTOM_LANGUAGE[0] }}'"
            return (False, error_msg)
    if "gui-wireless-opensecurity" in payload:
        value = payload["gui-wireless-opensecurity"]
        if value not in VALID_BODY_GUI_WIRELESS_OPENSECURITY:
            desc = FIELD_DESCRIPTIONS.get("gui-wireless-opensecurity", "")
            error_msg = f"Invalid value for 'gui-wireless-opensecurity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WIRELESS_OPENSECURITY)}"
            error_msg += f"\n  → Example: gui-wireless-opensecurity='{{ VALID_BODY_GUI_WIRELESS_OPENSECURITY[0] }}'"
            return (False, error_msg)
    if "gui-app-detection-sdwan" in payload:
        value = payload["gui-app-detection-sdwan"]
        if value not in VALID_BODY_GUI_APP_DETECTION_SDWAN:
            desc = FIELD_DESCRIPTIONS.get("gui-app-detection-sdwan", "")
            error_msg = f"Invalid value for 'gui-app-detection-sdwan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_APP_DETECTION_SDWAN)}"
            error_msg += f"\n  → Example: gui-app-detection-sdwan='{{ VALID_BODY_GUI_APP_DETECTION_SDWAN[0] }}'"
            return (False, error_msg)
    if "gui-display-hostname" in payload:
        value = payload["gui-display-hostname"]
        if value not in VALID_BODY_GUI_DISPLAY_HOSTNAME:
            desc = FIELD_DESCRIPTIONS.get("gui-display-hostname", "")
            error_msg = f"Invalid value for 'gui-display-hostname': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DISPLAY_HOSTNAME)}"
            error_msg += f"\n  → Example: gui-display-hostname='{{ VALID_BODY_GUI_DISPLAY_HOSTNAME[0] }}'"
            return (False, error_msg)
    if "gui-fortigate-cloud-sandbox" in payload:
        value = payload["gui-fortigate-cloud-sandbox"]
        if value not in VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX:
            desc = FIELD_DESCRIPTIONS.get("gui-fortigate-cloud-sandbox", "")
            error_msg = f"Invalid value for 'gui-fortigate-cloud-sandbox': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX)}"
            error_msg += f"\n  → Example: gui-fortigate-cloud-sandbox='{{ VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX[0] }}'"
            return (False, error_msg)
    if "gui-firmware-upgrade-warning" in payload:
        value = payload["gui-firmware-upgrade-warning"]
        if value not in VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING:
            desc = FIELD_DESCRIPTIONS.get("gui-firmware-upgrade-warning", "")
            error_msg = f"Invalid value for 'gui-firmware-upgrade-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING)}"
            error_msg += f"\n  → Example: gui-firmware-upgrade-warning='{{ VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING[0] }}'"
            return (False, error_msg)
    if "gui-forticare-registration-setup-warning" in payload:
        value = payload["gui-forticare-registration-setup-warning"]
        if value not in VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING:
            desc = FIELD_DESCRIPTIONS.get("gui-forticare-registration-setup-warning", "")
            error_msg = f"Invalid value for 'gui-forticare-registration-setup-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING)}"
            error_msg += f"\n  → Example: gui-forticare-registration-setup-warning='{{ VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING[0] }}'"
            return (False, error_msg)
    if "gui-auto-upgrade-setup-warning" in payload:
        value = payload["gui-auto-upgrade-setup-warning"]
        if value not in VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING:
            desc = FIELD_DESCRIPTIONS.get("gui-auto-upgrade-setup-warning", "")
            error_msg = f"Invalid value for 'gui-auto-upgrade-setup-warning': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING)}"
            error_msg += f"\n  → Example: gui-auto-upgrade-setup-warning='{{ VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING[0] }}'"
            return (False, error_msg)
    if "gui-workflow-management" in payload:
        value = payload["gui-workflow-management"]
        if value not in VALID_BODY_GUI_WORKFLOW_MANAGEMENT:
            desc = FIELD_DESCRIPTIONS.get("gui-workflow-management", "")
            error_msg = f"Invalid value for 'gui-workflow-management': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_WORKFLOW_MANAGEMENT)}"
            error_msg += f"\n  → Example: gui-workflow-management='{{ VALID_BODY_GUI_WORKFLOW_MANAGEMENT[0] }}'"
            return (False, error_msg)
    if "gui-cdn-usage" in payload:
        value = payload["gui-cdn-usage"]
        if value not in VALID_BODY_GUI_CDN_USAGE:
            desc = FIELD_DESCRIPTIONS.get("gui-cdn-usage", "")
            error_msg = f"Invalid value for 'gui-cdn-usage': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_CDN_USAGE)}"
            error_msg += f"\n  → Example: gui-cdn-usage='{{ VALID_BODY_GUI_CDN_USAGE[0] }}'"
            return (False, error_msg)
    if "admin-https-ssl-versions" in payload:
        value = payload["admin-https-ssl-versions"]
        if value not in VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS:
            desc = FIELD_DESCRIPTIONS.get("admin-https-ssl-versions", "")
            error_msg = f"Invalid value for 'admin-https-ssl-versions': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS)}"
            error_msg += f"\n  → Example: admin-https-ssl-versions='{{ VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS[0] }}'"
            return (False, error_msg)
    if "admin-https-ssl-ciphersuites" in payload:
        value = payload["admin-https-ssl-ciphersuites"]
        if value not in VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES:
            desc = FIELD_DESCRIPTIONS.get("admin-https-ssl-ciphersuites", "")
            error_msg = f"Invalid value for 'admin-https-ssl-ciphersuites': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES)}"
            error_msg += f"\n  → Example: admin-https-ssl-ciphersuites='{{ VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES[0] }}'"
            return (False, error_msg)
    if "admin-https-ssl-banned-ciphers" in payload:
        value = payload["admin-https-ssl-banned-ciphers"]
        if value not in VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS:
            desc = FIELD_DESCRIPTIONS.get("admin-https-ssl-banned-ciphers", "")
            error_msg = f"Invalid value for 'admin-https-ssl-banned-ciphers': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS)}"
            error_msg += f"\n  → Example: admin-https-ssl-banned-ciphers='{{ VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS[0] }}'"
            return (False, error_msg)
    if "ssd-trim-freq" in payload:
        value = payload["ssd-trim-freq"]
        if value not in VALID_BODY_SSD_TRIM_FREQ:
            desc = FIELD_DESCRIPTIONS.get("ssd-trim-freq", "")
            error_msg = f"Invalid value for 'ssd-trim-freq': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSD_TRIM_FREQ)}"
            error_msg += f"\n  → Example: ssd-trim-freq='{{ VALID_BODY_SSD_TRIM_FREQ[0] }}'"
            return (False, error_msg)
    if "ssd-trim-weekday" in payload:
        value = payload["ssd-trim-weekday"]
        if value not in VALID_BODY_SSD_TRIM_WEEKDAY:
            desc = FIELD_DESCRIPTIONS.get("ssd-trim-weekday", "")
            error_msg = f"Invalid value for 'ssd-trim-weekday': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSD_TRIM_WEEKDAY)}"
            error_msg += f"\n  → Example: ssd-trim-weekday='{{ VALID_BODY_SSD_TRIM_WEEKDAY[0] }}'"
            return (False, error_msg)
    if "admin-concurrent" in payload:
        value = payload["admin-concurrent"]
        if value not in VALID_BODY_ADMIN_CONCURRENT:
            desc = FIELD_DESCRIPTIONS.get("admin-concurrent", "")
            error_msg = f"Invalid value for 'admin-concurrent': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_CONCURRENT)}"
            error_msg += f"\n  → Example: admin-concurrent='{{ VALID_BODY_ADMIN_CONCURRENT[0] }}'"
            return (False, error_msg)
    if "purdue-level" in payload:
        value = payload["purdue-level"]
        if value not in VALID_BODY_PURDUE_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("purdue-level", "")
            error_msg = f"Invalid value for 'purdue-level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PURDUE_LEVEL)}"
            error_msg += f"\n  → Example: purdue-level='{{ VALID_BODY_PURDUE_LEVEL[0] }}'"
            return (False, error_msg)
    if "daily-restart" in payload:
        value = payload["daily-restart"]
        if value not in VALID_BODY_DAILY_RESTART:
            desc = FIELD_DESCRIPTIONS.get("daily-restart", "")
            error_msg = f"Invalid value for 'daily-restart': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DAILY_RESTART)}"
            error_msg += f"\n  → Example: daily-restart='{{ VALID_BODY_DAILY_RESTART[0] }}'"
            return (False, error_msg)
    if "wad-restart-mode" in payload:
        value = payload["wad-restart-mode"]
        if value not in VALID_BODY_WAD_RESTART_MODE:
            desc = FIELD_DESCRIPTIONS.get("wad-restart-mode", "")
            error_msg = f"Invalid value for 'wad-restart-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAD_RESTART_MODE)}"
            error_msg += f"\n  → Example: wad-restart-mode='{{ VALID_BODY_WAD_RESTART_MODE[0] }}'"
            return (False, error_msg)
    if "batch-cmdb" in payload:
        value = payload["batch-cmdb"]
        if value not in VALID_BODY_BATCH_CMDB:
            desc = FIELD_DESCRIPTIONS.get("batch-cmdb", "")
            error_msg = f"Invalid value for 'batch-cmdb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BATCH_CMDB)}"
            error_msg += f"\n  → Example: batch-cmdb='{{ VALID_BODY_BATCH_CMDB[0] }}'"
            return (False, error_msg)
    if "multi-factor-authentication" in payload:
        value = payload["multi-factor-authentication"]
        if value not in VALID_BODY_MULTI_FACTOR_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("multi-factor-authentication", "")
            error_msg = f"Invalid value for 'multi-factor-authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTI_FACTOR_AUTHENTICATION)}"
            error_msg += f"\n  → Example: multi-factor-authentication='{{ VALID_BODY_MULTI_FACTOR_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            desc = FIELD_DESCRIPTIONS.get("ssl-min-proto-version", "")
            error_msg = f"Invalid value for 'ssl-min-proto-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_MIN_PROTO_VERSION)}"
            error_msg += f"\n  → Example: ssl-min-proto-version='{{ VALID_BODY_SSL_MIN_PROTO_VERSION[0] }}'"
            return (False, error_msg)
    if "autorun-log-fsck" in payload:
        value = payload["autorun-log-fsck"]
        if value not in VALID_BODY_AUTORUN_LOG_FSCK:
            desc = FIELD_DESCRIPTIONS.get("autorun-log-fsck", "")
            error_msg = f"Invalid value for 'autorun-log-fsck': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTORUN_LOG_FSCK)}"
            error_msg += f"\n  → Example: autorun-log-fsck='{{ VALID_BODY_AUTORUN_LOG_FSCK[0] }}'"
            return (False, error_msg)
    if "traffic-priority" in payload:
        value = payload["traffic-priority"]
        if value not in VALID_BODY_TRAFFIC_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("traffic-priority", "")
            error_msg = f"Invalid value for 'traffic-priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAFFIC_PRIORITY)}"
            error_msg += f"\n  → Example: traffic-priority='{{ VALID_BODY_TRAFFIC_PRIORITY[0] }}'"
            return (False, error_msg)
    if "traffic-priority-level" in payload:
        value = payload["traffic-priority-level"]
        if value not in VALID_BODY_TRAFFIC_PRIORITY_LEVEL:
            desc = FIELD_DESCRIPTIONS.get("traffic-priority-level", "")
            error_msg = f"Invalid value for 'traffic-priority-level': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAFFIC_PRIORITY_LEVEL)}"
            error_msg += f"\n  → Example: traffic-priority-level='{{ VALID_BODY_TRAFFIC_PRIORITY_LEVEL[0] }}'"
            return (False, error_msg)
    if "quic-congestion-control-algo" in payload:
        value = payload["quic-congestion-control-algo"]
        if value not in VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO:
            desc = FIELD_DESCRIPTIONS.get("quic-congestion-control-algo", "")
            error_msg = f"Invalid value for 'quic-congestion-control-algo': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO)}"
            error_msg += f"\n  → Example: quic-congestion-control-algo='{{ VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO[0] }}'"
            return (False, error_msg)
    if "quic-udp-payload-size-shaping-per-cid" in payload:
        value = payload["quic-udp-payload-size-shaping-per-cid"]
        if value not in VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID:
            desc = FIELD_DESCRIPTIONS.get("quic-udp-payload-size-shaping-per-cid", "")
            error_msg = f"Invalid value for 'quic-udp-payload-size-shaping-per-cid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID)}"
            error_msg += f"\n  → Example: quic-udp-payload-size-shaping-per-cid='{{ VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID[0] }}'"
            return (False, error_msg)
    if "quic-pmtud" in payload:
        value = payload["quic-pmtud"]
        if value not in VALID_BODY_QUIC_PMTUD:
            desc = FIELD_DESCRIPTIONS.get("quic-pmtud", "")
            error_msg = f"Invalid value for 'quic-pmtud': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_QUIC_PMTUD)}"
            error_msg += f"\n  → Example: quic-pmtud='{{ VALID_BODY_QUIC_PMTUD[0] }}'"
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
    if "send-pmtu-icmp" in payload:
        value = payload["send-pmtu-icmp"]
        if value not in VALID_BODY_SEND_PMTU_ICMP:
            desc = FIELD_DESCRIPTIONS.get("send-pmtu-icmp", "")
            error_msg = f"Invalid value for 'send-pmtu-icmp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SEND_PMTU_ICMP)}"
            error_msg += f"\n  → Example: send-pmtu-icmp='{{ VALID_BODY_SEND_PMTU_ICMP[0] }}'"
            return (False, error_msg)
    if "honor-df" in payload:
        value = payload["honor-df"]
        if value not in VALID_BODY_HONOR_DF:
            desc = FIELD_DESCRIPTIONS.get("honor-df", "")
            error_msg = f"Invalid value for 'honor-df': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HONOR_DF)}"
            error_msg += f"\n  → Example: honor-df='{{ VALID_BODY_HONOR_DF[0] }}'"
            return (False, error_msg)
    if "pmtu-discovery" in payload:
        value = payload["pmtu-discovery"]
        if value not in VALID_BODY_PMTU_DISCOVERY:
            desc = FIELD_DESCRIPTIONS.get("pmtu-discovery", "")
            error_msg = f"Invalid value for 'pmtu-discovery': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PMTU_DISCOVERY)}"
            error_msg += f"\n  → Example: pmtu-discovery='{{ VALID_BODY_PMTU_DISCOVERY[0] }}'"
            return (False, error_msg)
    if "revision-image-auto-backup" in payload:
        value = payload["revision-image-auto-backup"]
        if value not in VALID_BODY_REVISION_IMAGE_AUTO_BACKUP:
            desc = FIELD_DESCRIPTIONS.get("revision-image-auto-backup", "")
            error_msg = f"Invalid value for 'revision-image-auto-backup': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REVISION_IMAGE_AUTO_BACKUP)}"
            error_msg += f"\n  → Example: revision-image-auto-backup='{{ VALID_BODY_REVISION_IMAGE_AUTO_BACKUP[0] }}'"
            return (False, error_msg)
    if "revision-backup-on-logout" in payload:
        value = payload["revision-backup-on-logout"]
        if value not in VALID_BODY_REVISION_BACKUP_ON_LOGOUT:
            desc = FIELD_DESCRIPTIONS.get("revision-backup-on-logout", "")
            error_msg = f"Invalid value for 'revision-backup-on-logout': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REVISION_BACKUP_ON_LOGOUT)}"
            error_msg += f"\n  → Example: revision-backup-on-logout='{{ VALID_BODY_REVISION_BACKUP_ON_LOGOUT[0] }}'"
            return (False, error_msg)
    if "strong-crypto" in payload:
        value = payload["strong-crypto"]
        if value not in VALID_BODY_STRONG_CRYPTO:
            desc = FIELD_DESCRIPTIONS.get("strong-crypto", "")
            error_msg = f"Invalid value for 'strong-crypto': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRONG_CRYPTO)}"
            error_msg += f"\n  → Example: strong-crypto='{{ VALID_BODY_STRONG_CRYPTO[0] }}'"
            return (False, error_msg)
    if "ssl-static-key-ciphers" in payload:
        value = payload["ssl-static-key-ciphers"]
        if value not in VALID_BODY_SSL_STATIC_KEY_CIPHERS:
            desc = FIELD_DESCRIPTIONS.get("ssl-static-key-ciphers", "")
            error_msg = f"Invalid value for 'ssl-static-key-ciphers': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSL_STATIC_KEY_CIPHERS)}"
            error_msg += f"\n  → Example: ssl-static-key-ciphers='{{ VALID_BODY_SSL_STATIC_KEY_CIPHERS[0] }}'"
            return (False, error_msg)
    if "snat-route-change" in payload:
        value = payload["snat-route-change"]
        if value not in VALID_BODY_SNAT_ROUTE_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("snat-route-change", "")
            error_msg = f"Invalid value for 'snat-route-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SNAT_ROUTE_CHANGE)}"
            error_msg += f"\n  → Example: snat-route-change='{{ VALID_BODY_SNAT_ROUTE_CHANGE[0] }}'"
            return (False, error_msg)
    if "ipv6-snat-route-change" in payload:
        value = payload["ipv6-snat-route-change"]
        if value not in VALID_BODY_IPV6_SNAT_ROUTE_CHANGE:
            desc = FIELD_DESCRIPTIONS.get("ipv6-snat-route-change", "")
            error_msg = f"Invalid value for 'ipv6-snat-route-change': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_SNAT_ROUTE_CHANGE)}"
            error_msg += f"\n  → Example: ipv6-snat-route-change='{{ VALID_BODY_IPV6_SNAT_ROUTE_CHANGE[0] }}'"
            return (False, error_msg)
    if "speedtest-server" in payload:
        value = payload["speedtest-server"]
        if value not in VALID_BODY_SPEEDTEST_SERVER:
            desc = FIELD_DESCRIPTIONS.get("speedtest-server", "")
            error_msg = f"Invalid value for 'speedtest-server': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPEEDTEST_SERVER)}"
            error_msg += f"\n  → Example: speedtest-server='{{ VALID_BODY_SPEEDTEST_SERVER[0] }}'"
            return (False, error_msg)
    if "cli-audit-log" in payload:
        value = payload["cli-audit-log"]
        if value not in VALID_BODY_CLI_AUDIT_LOG:
            desc = FIELD_DESCRIPTIONS.get("cli-audit-log", "")
            error_msg = f"Invalid value for 'cli-audit-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLI_AUDIT_LOG)}"
            error_msg += f"\n  → Example: cli-audit-log='{{ VALID_BODY_CLI_AUDIT_LOG[0] }}'"
            return (False, error_msg)
    if "dh-params" in payload:
        value = payload["dh-params"]
        if value not in VALID_BODY_DH_PARAMS:
            desc = FIELD_DESCRIPTIONS.get("dh-params", "")
            error_msg = f"Invalid value for 'dh-params': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DH_PARAMS)}"
            error_msg += f"\n  → Example: dh-params='{{ VALID_BODY_DH_PARAMS[0] }}'"
            return (False, error_msg)
    if "fds-statistics" in payload:
        value = payload["fds-statistics"]
        if value not in VALID_BODY_FDS_STATISTICS:
            desc = FIELD_DESCRIPTIONS.get("fds-statistics", "")
            error_msg = f"Invalid value for 'fds-statistics': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FDS_STATISTICS)}"
            error_msg += f"\n  → Example: fds-statistics='{{ VALID_BODY_FDS_STATISTICS[0] }}'"
            return (False, error_msg)
    if "tcp-option" in payload:
        value = payload["tcp-option"]
        if value not in VALID_BODY_TCP_OPTION:
            desc = FIELD_DESCRIPTIONS.get("tcp-option", "")
            error_msg = f"Invalid value for 'tcp-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TCP_OPTION)}"
            error_msg += f"\n  → Example: tcp-option='{{ VALID_BODY_TCP_OPTION[0] }}'"
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
    if "proxy-keep-alive-mode" in payload:
        value = payload["proxy-keep-alive-mode"]
        if value not in VALID_BODY_PROXY_KEEP_ALIVE_MODE:
            desc = FIELD_DESCRIPTIONS.get("proxy-keep-alive-mode", "")
            error_msg = f"Invalid value for 'proxy-keep-alive-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_KEEP_ALIVE_MODE)}"
            error_msg += f"\n  → Example: proxy-keep-alive-mode='{{ VALID_BODY_PROXY_KEEP_ALIVE_MODE[0] }}'"
            return (False, error_msg)
    if "proxy-auth-lifetime" in payload:
        value = payload["proxy-auth-lifetime"]
        if value not in VALID_BODY_PROXY_AUTH_LIFETIME:
            desc = FIELD_DESCRIPTIONS.get("proxy-auth-lifetime", "")
            error_msg = f"Invalid value for 'proxy-auth-lifetime': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_AUTH_LIFETIME)}"
            error_msg += f"\n  → Example: proxy-auth-lifetime='{{ VALID_BODY_PROXY_AUTH_LIFETIME[0] }}'"
            return (False, error_msg)
    if "proxy-resource-mode" in payload:
        value = payload["proxy-resource-mode"]
        if value not in VALID_BODY_PROXY_RESOURCE_MODE:
            desc = FIELD_DESCRIPTIONS.get("proxy-resource-mode", "")
            error_msg = f"Invalid value for 'proxy-resource-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_RESOURCE_MODE)}"
            error_msg += f"\n  → Example: proxy-resource-mode='{{ VALID_BODY_PROXY_RESOURCE_MODE[0] }}'"
            return (False, error_msg)
    if "proxy-cert-use-mgmt-vdom" in payload:
        value = payload["proxy-cert-use-mgmt-vdom"]
        if value not in VALID_BODY_PROXY_CERT_USE_MGMT_VDOM:
            desc = FIELD_DESCRIPTIONS.get("proxy-cert-use-mgmt-vdom", "")
            error_msg = f"Invalid value for 'proxy-cert-use-mgmt-vdom': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY_CERT_USE_MGMT_VDOM)}"
            error_msg += f"\n  → Example: proxy-cert-use-mgmt-vdom='{{ VALID_BODY_PROXY_CERT_USE_MGMT_VDOM[0] }}'"
            return (False, error_msg)
    if "check-protocol-header" in payload:
        value = payload["check-protocol-header"]
        if value not in VALID_BODY_CHECK_PROTOCOL_HEADER:
            desc = FIELD_DESCRIPTIONS.get("check-protocol-header", "")
            error_msg = f"Invalid value for 'check-protocol-header': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHECK_PROTOCOL_HEADER)}"
            error_msg += f"\n  → Example: check-protocol-header='{{ VALID_BODY_CHECK_PROTOCOL_HEADER[0] }}'"
            return (False, error_msg)
    if "vip-arp-range" in payload:
        value = payload["vip-arp-range"]
        if value not in VALID_BODY_VIP_ARP_RANGE:
            desc = FIELD_DESCRIPTIONS.get("vip-arp-range", "")
            error_msg = f"Invalid value for 'vip-arp-range': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VIP_ARP_RANGE)}"
            error_msg += f"\n  → Example: vip-arp-range='{{ VALID_BODY_VIP_ARP_RANGE[0] }}'"
            return (False, error_msg)
    if "reset-sessionless-tcp" in payload:
        value = payload["reset-sessionless-tcp"]
        if value not in VALID_BODY_RESET_SESSIONLESS_TCP:
            desc = FIELD_DESCRIPTIONS.get("reset-sessionless-tcp", "")
            error_msg = f"Invalid value for 'reset-sessionless-tcp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RESET_SESSIONLESS_TCP)}"
            error_msg += f"\n  → Example: reset-sessionless-tcp='{{ VALID_BODY_RESET_SESSIONLESS_TCP[0] }}'"
            return (False, error_msg)
    if "allow-traffic-redirect" in payload:
        value = payload["allow-traffic-redirect"]
        if value not in VALID_BODY_ALLOW_TRAFFIC_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("allow-traffic-redirect", "")
            error_msg = f"Invalid value for 'allow-traffic-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALLOW_TRAFFIC_REDIRECT)}"
            error_msg += f"\n  → Example: allow-traffic-redirect='{{ VALID_BODY_ALLOW_TRAFFIC_REDIRECT[0] }}'"
            return (False, error_msg)
    if "ipv6-allow-traffic-redirect" in payload:
        value = payload["ipv6-allow-traffic-redirect"]
        if value not in VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("ipv6-allow-traffic-redirect", "")
            error_msg = f"Invalid value for 'ipv6-allow-traffic-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT)}"
            error_msg += f"\n  → Example: ipv6-allow-traffic-redirect='{{ VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT[0] }}'"
            return (False, error_msg)
    if "strict-dirty-session-check" in payload:
        value = payload["strict-dirty-session-check"]
        if value not in VALID_BODY_STRICT_DIRTY_SESSION_CHECK:
            desc = FIELD_DESCRIPTIONS.get("strict-dirty-session-check", "")
            error_msg = f"Invalid value for 'strict-dirty-session-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STRICT_DIRTY_SESSION_CHECK)}"
            error_msg += f"\n  → Example: strict-dirty-session-check='{{ VALID_BODY_STRICT_DIRTY_SESSION_CHECK[0] }}'"
            return (False, error_msg)
    if "pre-login-banner" in payload:
        value = payload["pre-login-banner"]
        if value not in VALID_BODY_PRE_LOGIN_BANNER:
            desc = FIELD_DESCRIPTIONS.get("pre-login-banner", "")
            error_msg = f"Invalid value for 'pre-login-banner': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRE_LOGIN_BANNER)}"
            error_msg += f"\n  → Example: pre-login-banner='{{ VALID_BODY_PRE_LOGIN_BANNER[0] }}'"
            return (False, error_msg)
    if "post-login-banner" in payload:
        value = payload["post-login-banner"]
        if value not in VALID_BODY_POST_LOGIN_BANNER:
            desc = FIELD_DESCRIPTIONS.get("post-login-banner", "")
            error_msg = f"Invalid value for 'post-login-banner': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POST_LOGIN_BANNER)}"
            error_msg += f"\n  → Example: post-login-banner='{{ VALID_BODY_POST_LOGIN_BANNER[0] }}'"
            return (False, error_msg)
    if "tftp" in payload:
        value = payload["tftp"]
        if value not in VALID_BODY_TFTP:
            desc = FIELD_DESCRIPTIONS.get("tftp", "")
            error_msg = f"Invalid value for 'tftp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TFTP)}"
            error_msg += f"\n  → Example: tftp='{{ VALID_BODY_TFTP[0] }}'"
            return (False, error_msg)
    if "av-failopen" in payload:
        value = payload["av-failopen"]
        if value not in VALID_BODY_AV_FAILOPEN:
            desc = FIELD_DESCRIPTIONS.get("av-failopen", "")
            error_msg = f"Invalid value for 'av-failopen': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AV_FAILOPEN)}"
            error_msg += f"\n  → Example: av-failopen='{{ VALID_BODY_AV_FAILOPEN[0] }}'"
            return (False, error_msg)
    if "av-failopen-session" in payload:
        value = payload["av-failopen-session"]
        if value not in VALID_BODY_AV_FAILOPEN_SESSION:
            desc = FIELD_DESCRIPTIONS.get("av-failopen-session", "")
            error_msg = f"Invalid value for 'av-failopen-session': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AV_FAILOPEN_SESSION)}"
            error_msg += f"\n  → Example: av-failopen-session='{{ VALID_BODY_AV_FAILOPEN_SESSION[0] }}'"
            return (False, error_msg)
    if "log-single-cpu-high" in payload:
        value = payload["log-single-cpu-high"]
        if value not in VALID_BODY_LOG_SINGLE_CPU_HIGH:
            desc = FIELD_DESCRIPTIONS.get("log-single-cpu-high", "")
            error_msg = f"Invalid value for 'log-single-cpu-high': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_SINGLE_CPU_HIGH)}"
            error_msg += f"\n  → Example: log-single-cpu-high='{{ VALID_BODY_LOG_SINGLE_CPU_HIGH[0] }}'"
            return (False, error_msg)
    if "check-reset-range" in payload:
        value = payload["check-reset-range"]
        if value not in VALID_BODY_CHECK_RESET_RANGE:
            desc = FIELD_DESCRIPTIONS.get("check-reset-range", "")
            error_msg = f"Invalid value for 'check-reset-range': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHECK_RESET_RANGE)}"
            error_msg += f"\n  → Example: check-reset-range='{{ VALID_BODY_CHECK_RESET_RANGE[0] }}'"
            return (False, error_msg)
    if "upgrade-report" in payload:
        value = payload["upgrade-report"]
        if value not in VALID_BODY_UPGRADE_REPORT:
            desc = FIELD_DESCRIPTIONS.get("upgrade-report", "")
            error_msg = f"Invalid value for 'upgrade-report': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPGRADE_REPORT)}"
            error_msg += f"\n  → Example: upgrade-report='{{ VALID_BODY_UPGRADE_REPORT[0] }}'"
            return (False, error_msg)
    if "admin-https-redirect" in payload:
        value = payload["admin-https-redirect"]
        if value not in VALID_BODY_ADMIN_HTTPS_REDIRECT:
            desc = FIELD_DESCRIPTIONS.get("admin-https-redirect", "")
            error_msg = f"Invalid value for 'admin-https-redirect': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_HTTPS_REDIRECT)}"
            error_msg += f"\n  → Example: admin-https-redirect='{{ VALID_BODY_ADMIN_HTTPS_REDIRECT[0] }}'"
            return (False, error_msg)
    if "admin-ssh-password" in payload:
        value = payload["admin-ssh-password"]
        if value not in VALID_BODY_ADMIN_SSH_PASSWORD:
            desc = FIELD_DESCRIPTIONS.get("admin-ssh-password", "")
            error_msg = f"Invalid value for 'admin-ssh-password': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_SSH_PASSWORD)}"
            error_msg += f"\n  → Example: admin-ssh-password='{{ VALID_BODY_ADMIN_SSH_PASSWORD[0] }}'"
            return (False, error_msg)
    if "admin-restrict-local" in payload:
        value = payload["admin-restrict-local"]
        if value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            desc = FIELD_DESCRIPTIONS.get("admin-restrict-local", "")
            error_msg = f"Invalid value for 'admin-restrict-local': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_RESTRICT_LOCAL)}"
            error_msg += f"\n  → Example: admin-restrict-local='{{ VALID_BODY_ADMIN_RESTRICT_LOCAL[0] }}'"
            return (False, error_msg)
    if "admin-ssh-v1" in payload:
        value = payload["admin-ssh-v1"]
        if value not in VALID_BODY_ADMIN_SSH_V1:
            desc = FIELD_DESCRIPTIONS.get("admin-ssh-v1", "")
            error_msg = f"Invalid value for 'admin-ssh-v1': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_SSH_V1)}"
            error_msg += f"\n  → Example: admin-ssh-v1='{{ VALID_BODY_ADMIN_SSH_V1[0] }}'"
            return (False, error_msg)
    if "admin-telnet" in payload:
        value = payload["admin-telnet"]
        if value not in VALID_BODY_ADMIN_TELNET:
            desc = FIELD_DESCRIPTIONS.get("admin-telnet", "")
            error_msg = f"Invalid value for 'admin-telnet': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_TELNET)}"
            error_msg += f"\n  → Example: admin-telnet='{{ VALID_BODY_ADMIN_TELNET[0] }}'"
            return (False, error_msg)
    if "admin-forticloud-sso-login" in payload:
        value = payload["admin-forticloud-sso-login"]
        if value not in VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN:
            desc = FIELD_DESCRIPTIONS.get("admin-forticloud-sso-login", "")
            error_msg = f"Invalid value for 'admin-forticloud-sso-login': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN)}"
            error_msg += f"\n  → Example: admin-forticloud-sso-login='{{ VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN[0] }}'"
            return (False, error_msg)
    if "admin-https-pki-required" in payload:
        value = payload["admin-https-pki-required"]
        if value not in VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED:
            desc = FIELD_DESCRIPTIONS.get("admin-https-pki-required", "")
            error_msg = f"Invalid value for 'admin-https-pki-required': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED)}"
            error_msg += f"\n  → Example: admin-https-pki-required='{{ VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED[0] }}'"
            return (False, error_msg)
    if "auth-keepalive" in payload:
        value = payload["auth-keepalive"]
        if value not in VALID_BODY_AUTH_KEEPALIVE:
            desc = FIELD_DESCRIPTIONS.get("auth-keepalive", "")
            error_msg = f"Invalid value for 'auth-keepalive': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_KEEPALIVE)}"
            error_msg += f"\n  → Example: auth-keepalive='{{ VALID_BODY_AUTH_KEEPALIVE[0] }}'"
            return (False, error_msg)
    if "auth-session-limit" in payload:
        value = payload["auth-session-limit"]
        if value not in VALID_BODY_AUTH_SESSION_LIMIT:
            desc = FIELD_DESCRIPTIONS.get("auth-session-limit", "")
            error_msg = f"Invalid value for 'auth-session-limit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SESSION_LIMIT)}"
            error_msg += f"\n  → Example: auth-session-limit='{{ VALID_BODY_AUTH_SESSION_LIMIT[0] }}'"
            return (False, error_msg)
    if "clt-cert-req" in payload:
        value = payload["clt-cert-req"]
        if value not in VALID_BODY_CLT_CERT_REQ:
            desc = FIELD_DESCRIPTIONS.get("clt-cert-req", "")
            error_msg = f"Invalid value for 'clt-cert-req': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLT_CERT_REQ)}"
            error_msg += f"\n  → Example: clt-cert-req='{{ VALID_BODY_CLT_CERT_REQ[0] }}'"
            return (False, error_msg)
    if "cfg-save" in payload:
        value = payload["cfg-save"]
        if value not in VALID_BODY_CFG_SAVE:
            desc = FIELD_DESCRIPTIONS.get("cfg-save", "")
            error_msg = f"Invalid value for 'cfg-save': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CFG_SAVE)}"
            error_msg += f"\n  → Example: cfg-save='{{ VALID_BODY_CFG_SAVE[0] }}'"
            return (False, error_msg)
    if "reboot-upon-config-restore" in payload:
        value = payload["reboot-upon-config-restore"]
        if value not in VALID_BODY_REBOOT_UPON_CONFIG_RESTORE:
            desc = FIELD_DESCRIPTIONS.get("reboot-upon-config-restore", "")
            error_msg = f"Invalid value for 'reboot-upon-config-restore': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REBOOT_UPON_CONFIG_RESTORE)}"
            error_msg += f"\n  → Example: reboot-upon-config-restore='{{ VALID_BODY_REBOOT_UPON_CONFIG_RESTORE[0] }}'"
            return (False, error_msg)
    if "admin-scp" in payload:
        value = payload["admin-scp"]
        if value not in VALID_BODY_ADMIN_SCP:
            desc = FIELD_DESCRIPTIONS.get("admin-scp", "")
            error_msg = f"Invalid value for 'admin-scp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADMIN_SCP)}"
            error_msg += f"\n  → Example: admin-scp='{{ VALID_BODY_ADMIN_SCP[0] }}'"
            return (False, error_msg)
    if "wireless-controller" in payload:
        value = payload["wireless-controller"]
        if value not in VALID_BODY_WIRELESS_CONTROLLER:
            desc = FIELD_DESCRIPTIONS.get("wireless-controller", "")
            error_msg = f"Invalid value for 'wireless-controller': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIRELESS_CONTROLLER)}"
            error_msg += f"\n  → Example: wireless-controller='{{ VALID_BODY_WIRELESS_CONTROLLER[0] }}'"
            return (False, error_msg)
    if "fortiextender" in payload:
        value = payload["fortiextender"]
        if value not in VALID_BODY_FORTIEXTENDER:
            desc = FIELD_DESCRIPTIONS.get("fortiextender", "")
            error_msg = f"Invalid value for 'fortiextender': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIEXTENDER)}"
            error_msg += f"\n  → Example: fortiextender='{{ VALID_BODY_FORTIEXTENDER[0] }}'"
            return (False, error_msg)
    if "fortiextender-discovery-lockdown" in payload:
        value = payload["fortiextender-discovery-lockdown"]
        if value not in VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN:
            desc = FIELD_DESCRIPTIONS.get("fortiextender-discovery-lockdown", "")
            error_msg = f"Invalid value for 'fortiextender-discovery-lockdown': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN)}"
            error_msg += f"\n  → Example: fortiextender-discovery-lockdown='{{ VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN[0] }}'"
            return (False, error_msg)
    if "fortiextender-vlan-mode" in payload:
        value = payload["fortiextender-vlan-mode"]
        if value not in VALID_BODY_FORTIEXTENDER_VLAN_MODE:
            desc = FIELD_DESCRIPTIONS.get("fortiextender-vlan-mode", "")
            error_msg = f"Invalid value for 'fortiextender-vlan-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIEXTENDER_VLAN_MODE)}"
            error_msg += f"\n  → Example: fortiextender-vlan-mode='{{ VALID_BODY_FORTIEXTENDER_VLAN_MODE[0] }}'"
            return (False, error_msg)
    if "fortiextender-provision-on-authorization" in payload:
        value = payload["fortiextender-provision-on-authorization"]
        if value not in VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION:
            desc = FIELD_DESCRIPTIONS.get("fortiextender-provision-on-authorization", "")
            error_msg = f"Invalid value for 'fortiextender-provision-on-authorization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION)}"
            error_msg += f"\n  → Example: fortiextender-provision-on-authorization='{{ VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION[0] }}'"
            return (False, error_msg)
    if "switch-controller" in payload:
        value = payload["switch-controller"]
        if value not in VALID_BODY_SWITCH_CONTROLLER:
            desc = FIELD_DESCRIPTIONS.get("switch-controller", "")
            error_msg = f"Invalid value for 'switch-controller': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCH_CONTROLLER)}"
            error_msg += f"\n  → Example: switch-controller='{{ VALID_BODY_SWITCH_CONTROLLER[0] }}'"
            return (False, error_msg)
    if "fgd-alert-subscription" in payload:
        value = payload["fgd-alert-subscription"]
        if value not in VALID_BODY_FGD_ALERT_SUBSCRIPTION:
            desc = FIELD_DESCRIPTIONS.get("fgd-alert-subscription", "")
            error_msg = f"Invalid value for 'fgd-alert-subscription': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FGD_ALERT_SUBSCRIPTION)}"
            error_msg += f"\n  → Example: fgd-alert-subscription='{{ VALID_BODY_FGD_ALERT_SUBSCRIPTION[0] }}'"
            return (False, error_msg)
    if "ipv6-allow-anycast-probe" in payload:
        value = payload["ipv6-allow-anycast-probe"]
        if value not in VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE:
            desc = FIELD_DESCRIPTIONS.get("ipv6-allow-anycast-probe", "")
            error_msg = f"Invalid value for 'ipv6-allow-anycast-probe': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE)}"
            error_msg += f"\n  → Example: ipv6-allow-anycast-probe='{{ VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE[0] }}'"
            return (False, error_msg)
    if "ipv6-allow-multicast-probe" in payload:
        value = payload["ipv6-allow-multicast-probe"]
        if value not in VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE:
            desc = FIELD_DESCRIPTIONS.get("ipv6-allow-multicast-probe", "")
            error_msg = f"Invalid value for 'ipv6-allow-multicast-probe': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE)}"
            error_msg += f"\n  → Example: ipv6-allow-multicast-probe='{{ VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE[0] }}'"
            return (False, error_msg)
    if "ipv6-allow-local-in-silent-drop" in payload:
        value = payload["ipv6-allow-local-in-silent-drop"]
        if value not in VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP:
            desc = FIELD_DESCRIPTIONS.get("ipv6-allow-local-in-silent-drop", "")
            error_msg = f"Invalid value for 'ipv6-allow-local-in-silent-drop': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP)}"
            error_msg += f"\n  → Example: ipv6-allow-local-in-silent-drop='{{ VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP[0] }}'"
            return (False, error_msg)
    if "csr-ca-attribute" in payload:
        value = payload["csr-ca-attribute"]
        if value not in VALID_BODY_CSR_CA_ATTRIBUTE:
            desc = FIELD_DESCRIPTIONS.get("csr-ca-attribute", "")
            error_msg = f"Invalid value for 'csr-ca-attribute': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CSR_CA_ATTRIBUTE)}"
            error_msg += f"\n  → Example: csr-ca-attribute='{{ VALID_BODY_CSR_CA_ATTRIBUTE[0] }}'"
            return (False, error_msg)
    if "wimax-4g-usb" in payload:
        value = payload["wimax-4g-usb"]
        if value not in VALID_BODY_WIMAX_4G_USB:
            desc = FIELD_DESCRIPTIONS.get("wimax-4g-usb", "")
            error_msg = f"Invalid value for 'wimax-4g-usb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIMAX_4G_USB)}"
            error_msg += f"\n  → Example: wimax-4g-usb='{{ VALID_BODY_WIMAX_4G_USB[0] }}'"
            return (False, error_msg)
    if "sslvpn-web-mode" in payload:
        value = payload["sslvpn-web-mode"]
        if value not in VALID_BODY_SSLVPN_WEB_MODE:
            desc = FIELD_DESCRIPTIONS.get("sslvpn-web-mode", "")
            error_msg = f"Invalid value for 'sslvpn-web-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSLVPN_WEB_MODE)}"
            error_msg += f"\n  → Example: sslvpn-web-mode='{{ VALID_BODY_SSLVPN_WEB_MODE[0] }}'"
            return (False, error_msg)
    if "per-user-bal" in payload:
        value = payload["per-user-bal"]
        if value not in VALID_BODY_PER_USER_BAL:
            desc = FIELD_DESCRIPTIONS.get("per-user-bal", "")
            error_msg = f"Invalid value for 'per-user-bal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PER_USER_BAL)}"
            error_msg += f"\n  → Example: per-user-bal='{{ VALID_BODY_PER_USER_BAL[0] }}'"
            return (False, error_msg)
    if "wad-source-affinity" in payload:
        value = payload["wad-source-affinity"]
        if value not in VALID_BODY_WAD_SOURCE_AFFINITY:
            desc = FIELD_DESCRIPTIONS.get("wad-source-affinity", "")
            error_msg = f"Invalid value for 'wad-source-affinity': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WAD_SOURCE_AFFINITY)}"
            error_msg += f"\n  → Example: wad-source-affinity='{{ VALID_BODY_WAD_SOURCE_AFFINITY[0] }}'"
            return (False, error_msg)
    if "login-timestamp" in payload:
        value = payload["login-timestamp"]
        if value not in VALID_BODY_LOGIN_TIMESTAMP:
            desc = FIELD_DESCRIPTIONS.get("login-timestamp", "")
            error_msg = f"Invalid value for 'login-timestamp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOGIN_TIMESTAMP)}"
            error_msg += f"\n  → Example: login-timestamp='{{ VALID_BODY_LOGIN_TIMESTAMP[0] }}'"
            return (False, error_msg)
    if "ip-conflict-detection" in payload:
        value = payload["ip-conflict-detection"]
        if value not in VALID_BODY_IP_CONFLICT_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("ip-conflict-detection", "")
            error_msg = f"Invalid value for 'ip-conflict-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IP_CONFLICT_DETECTION)}"
            error_msg += f"\n  → Example: ip-conflict-detection='{{ VALID_BODY_IP_CONFLICT_DETECTION[0] }}'"
            return (False, error_msg)
    if "special-file-23-support" in payload:
        value = payload["special-file-23-support"]
        if value not in VALID_BODY_SPECIAL_FILE_23_SUPPORT:
            desc = FIELD_DESCRIPTIONS.get("special-file-23-support", "")
            error_msg = f"Invalid value for 'special-file-23-support': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPECIAL_FILE_23_SUPPORT)}"
            error_msg += f"\n  → Example: special-file-23-support='{{ VALID_BODY_SPECIAL_FILE_23_SUPPORT[0] }}'"
            return (False, error_msg)
    if "log-uuid-address" in payload:
        value = payload["log-uuid-address"]
        if value not in VALID_BODY_LOG_UUID_ADDRESS:
            desc = FIELD_DESCRIPTIONS.get("log-uuid-address", "")
            error_msg = f"Invalid value for 'log-uuid-address': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_UUID_ADDRESS)}"
            error_msg += f"\n  → Example: log-uuid-address='{{ VALID_BODY_LOG_UUID_ADDRESS[0] }}'"
            return (False, error_msg)
    if "log-ssl-connection" in payload:
        value = payload["log-ssl-connection"]
        if value not in VALID_BODY_LOG_SSL_CONNECTION:
            desc = FIELD_DESCRIPTIONS.get("log-ssl-connection", "")
            error_msg = f"Invalid value for 'log-ssl-connection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_SSL_CONNECTION)}"
            error_msg += f"\n  → Example: log-ssl-connection='{{ VALID_BODY_LOG_SSL_CONNECTION[0] }}'"
            return (False, error_msg)
    if "gui-rest-api-cache" in payload:
        value = payload["gui-rest-api-cache"]
        if value not in VALID_BODY_GUI_REST_API_CACHE:
            desc = FIELD_DESCRIPTIONS.get("gui-rest-api-cache", "")
            error_msg = f"Invalid value for 'gui-rest-api-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_REST_API_CACHE)}"
            error_msg += f"\n  → Example: gui-rest-api-cache='{{ VALID_BODY_GUI_REST_API_CACHE[0] }}'"
            return (False, error_msg)
    if "rest-api-key-url-query" in payload:
        value = payload["rest-api-key-url-query"]
        if value not in VALID_BODY_REST_API_KEY_URL_QUERY:
            desc = FIELD_DESCRIPTIONS.get("rest-api-key-url-query", "")
            error_msg = f"Invalid value for 'rest-api-key-url-query': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REST_API_KEY_URL_QUERY)}"
            error_msg += f"\n  → Example: rest-api-key-url-query='{{ VALID_BODY_REST_API_KEY_URL_QUERY[0] }}'"
            return (False, error_msg)
    if "ipsec-qat-offload" in payload:
        value = payload["ipsec-qat-offload"]
        if value not in VALID_BODY_IPSEC_QAT_OFFLOAD:
            desc = FIELD_DESCRIPTIONS.get("ipsec-qat-offload", "")
            error_msg = f"Invalid value for 'ipsec-qat-offload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPSEC_QAT_OFFLOAD)}"
            error_msg += f"\n  → Example: ipsec-qat-offload='{{ VALID_BODY_IPSEC_QAT_OFFLOAD[0] }}'"
            return (False, error_msg)
    if "private-data-encryption" in payload:
        value = payload["private-data-encryption"]
        if value not in VALID_BODY_PRIVATE_DATA_ENCRYPTION:
            desc = FIELD_DESCRIPTIONS.get("private-data-encryption", "")
            error_msg = f"Invalid value for 'private-data-encryption': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PRIVATE_DATA_ENCRYPTION)}"
            error_msg += f"\n  → Example: private-data-encryption='{{ VALID_BODY_PRIVATE_DATA_ENCRYPTION[0] }}'"
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
    if "gui-theme" in payload:
        value = payload["gui-theme"]
        if value not in VALID_BODY_GUI_THEME:
            desc = FIELD_DESCRIPTIONS.get("gui-theme", "")
            error_msg = f"Invalid value for 'gui-theme': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_THEME)}"
            error_msg += f"\n  → Example: gui-theme='{{ VALID_BODY_GUI_THEME[0] }}'"
            return (False, error_msg)
    if "gui-date-format" in payload:
        value = payload["gui-date-format"]
        if value not in VALID_BODY_GUI_DATE_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("gui-date-format", "")
            error_msg = f"Invalid value for 'gui-date-format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DATE_FORMAT)}"
            error_msg += f"\n  → Example: gui-date-format='{{ VALID_BODY_GUI_DATE_FORMAT[0] }}'"
            return (False, error_msg)
    if "gui-date-time-source" in payload:
        value = payload["gui-date-time-source"]
        if value not in VALID_BODY_GUI_DATE_TIME_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("gui-date-time-source", "")
            error_msg = f"Invalid value for 'gui-date-time-source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GUI_DATE_TIME_SOURCE)}"
            error_msg += f"\n  → Example: gui-date-time-source='{{ VALID_BODY_GUI_DATE_TIME_SOURCE[0] }}'"
            return (False, error_msg)
    if "cloud-communication" in payload:
        value = payload["cloud-communication"]
        if value not in VALID_BODY_CLOUD_COMMUNICATION:
            desc = FIELD_DESCRIPTIONS.get("cloud-communication", "")
            error_msg = f"Invalid value for 'cloud-communication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLOUD_COMMUNICATION)}"
            error_msg += f"\n  → Example: cloud-communication='{{ VALID_BODY_CLOUD_COMMUNICATION[0] }}'"
            return (False, error_msg)
    if "fortitoken-cloud" in payload:
        value = payload["fortitoken-cloud"]
        if value not in VALID_BODY_FORTITOKEN_CLOUD:
            desc = FIELD_DESCRIPTIONS.get("fortitoken-cloud", "")
            error_msg = f"Invalid value for 'fortitoken-cloud': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTITOKEN_CLOUD)}"
            error_msg += f"\n  → Example: fortitoken-cloud='{{ VALID_BODY_FORTITOKEN_CLOUD[0] }}'"
            return (False, error_msg)
    if "fortitoken-cloud-push-status" in payload:
        value = payload["fortitoken-cloud-push-status"]
        if value not in VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS:
            desc = FIELD_DESCRIPTIONS.get("fortitoken-cloud-push-status", "")
            error_msg = f"Invalid value for 'fortitoken-cloud-push-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS)}"
            error_msg += f"\n  → Example: fortitoken-cloud-push-status='{{ VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS[0] }}'"
            return (False, error_msg)
    if "irq-time-accounting" in payload:
        value = payload["irq-time-accounting"]
        if value not in VALID_BODY_IRQ_TIME_ACCOUNTING:
            desc = FIELD_DESCRIPTIONS.get("irq-time-accounting", "")
            error_msg = f"Invalid value for 'irq-time-accounting': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IRQ_TIME_ACCOUNTING)}"
            error_msg += f"\n  → Example: irq-time-accounting='{{ VALID_BODY_IRQ_TIME_ACCOUNTING[0] }}'"
            return (False, error_msg)
    if "management-port-use-admin-sport" in payload:
        value = payload["management-port-use-admin-sport"]
        if value not in VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT:
            desc = FIELD_DESCRIPTIONS.get("management-port-use-admin-sport", "")
            error_msg = f"Invalid value for 'management-port-use-admin-sport': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT)}"
            error_msg += f"\n  → Example: management-port-use-admin-sport='{{ VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT[0] }}'"
            return (False, error_msg)
    if "forticonverter-integration" in payload:
        value = payload["forticonverter-integration"]
        if value not in VALID_BODY_FORTICONVERTER_INTEGRATION:
            desc = FIELD_DESCRIPTIONS.get("forticonverter-integration", "")
            error_msg = f"Invalid value for 'forticonverter-integration': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTICONVERTER_INTEGRATION)}"
            error_msg += f"\n  → Example: forticonverter-integration='{{ VALID_BODY_FORTICONVERTER_INTEGRATION[0] }}'"
            return (False, error_msg)
    if "forticonverter-config-upload" in payload:
        value = payload["forticonverter-config-upload"]
        if value not in VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD:
            desc = FIELD_DESCRIPTIONS.get("forticonverter-config-upload", "")
            error_msg = f"Invalid value for 'forticonverter-config-upload': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD)}"
            error_msg += f"\n  → Example: forticonverter-config-upload='{{ VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD[0] }}'"
            return (False, error_msg)
    if "internet-service-database" in payload:
        value = payload["internet-service-database"]
        if value not in VALID_BODY_INTERNET_SERVICE_DATABASE:
            desc = FIELD_DESCRIPTIONS.get("internet-service-database", "")
            error_msg = f"Invalid value for 'internet-service-database': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERNET_SERVICE_DATABASE)}"
            error_msg += f"\n  → Example: internet-service-database='{{ VALID_BODY_INTERNET_SERVICE_DATABASE[0] }}'"
            return (False, error_msg)
    if "early-tcp-npu-session" in payload:
        value = payload["early-tcp-npu-session"]
        if value not in VALID_BODY_EARLY_TCP_NPU_SESSION:
            desc = FIELD_DESCRIPTIONS.get("early-tcp-npu-session", "")
            error_msg = f"Invalid value for 'early-tcp-npu-session': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EARLY_TCP_NPU_SESSION)}"
            error_msg += f"\n  → Example: early-tcp-npu-session='{{ VALID_BODY_EARLY_TCP_NPU_SESSION[0] }}'"
            return (False, error_msg)
    if "npu-neighbor-update" in payload:
        value = payload["npu-neighbor-update"]
        if value not in VALID_BODY_NPU_NEIGHBOR_UPDATE:
            desc = FIELD_DESCRIPTIONS.get("npu-neighbor-update", "")
            error_msg = f"Invalid value for 'npu-neighbor-update': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NPU_NEIGHBOR_UPDATE)}"
            error_msg += f"\n  → Example: npu-neighbor-update='{{ VALID_BODY_NPU_NEIGHBOR_UPDATE[0] }}'"
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
    if "interface-subnet-usage" in payload:
        value = payload["interface-subnet-usage"]
        if value not in VALID_BODY_INTERFACE_SUBNET_USAGE:
            desc = FIELD_DESCRIPTIONS.get("interface-subnet-usage", "")
            error_msg = f"Invalid value for 'interface-subnet-usage': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INTERFACE_SUBNET_USAGE)}"
            error_msg += f"\n  → Example: interface-subnet-usage='{{ VALID_BODY_INTERFACE_SUBNET_USAGE[0] }}'"
            return (False, error_msg)
    if "fortigslb-integration" in payload:
        value = payload["fortigslb-integration"]
        if value not in VALID_BODY_FORTIGSLB_INTEGRATION:
            desc = FIELD_DESCRIPTIONS.get("fortigslb-integration", "")
            error_msg = f"Invalid value for 'fortigslb-integration': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTIGSLB_INTEGRATION)}"
            error_msg += f"\n  → Example: fortigslb-integration='{{ VALID_BODY_FORTIGSLB_INTEGRATION[0] }}'"
            return (False, error_msg)
    if "auth-session-auto-backup" in payload:
        value = payload["auth-session-auto-backup"]
        if value not in VALID_BODY_AUTH_SESSION_AUTO_BACKUP:
            desc = FIELD_DESCRIPTIONS.get("auth-session-auto-backup", "")
            error_msg = f"Invalid value for 'auth-session-auto-backup': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SESSION_AUTO_BACKUP)}"
            error_msg += f"\n  → Example: auth-session-auto-backup='{{ VALID_BODY_AUTH_SESSION_AUTO_BACKUP[0] }}'"
            return (False, error_msg)
    if "auth-session-auto-backup-interval" in payload:
        value = payload["auth-session-auto-backup-interval"]
        if value not in VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL:
            desc = FIELD_DESCRIPTIONS.get("auth-session-auto-backup-interval", "")
            error_msg = f"Invalid value for 'auth-session-auto-backup-interval': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL)}"
            error_msg += f"\n  → Example: auth-session-auto-backup-interval='{{ VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL[0] }}'"
            return (False, error_msg)
    if "application-bandwidth-tracking" in payload:
        value = payload["application-bandwidth-tracking"]
        if value not in VALID_BODY_APPLICATION_BANDWIDTH_TRACKING:
            desc = FIELD_DESCRIPTIONS.get("application-bandwidth-tracking", "")
            error_msg = f"Invalid value for 'application-bandwidth-tracking': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_APPLICATION_BANDWIDTH_TRACKING)}"
            error_msg += f"\n  → Example: application-bandwidth-tracking='{{ VALID_BODY_APPLICATION_BANDWIDTH_TRACKING[0] }}'"
            return (False, error_msg)
    if "tls-session-cache" in payload:
        value = payload["tls-session-cache"]
        if value not in VALID_BODY_TLS_SESSION_CACHE:
            desc = FIELD_DESCRIPTIONS.get("tls-session-cache", "")
            error_msg = f"Invalid value for 'tls-session-cache': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TLS_SESSION_CACHE)}"
            error_msg += f"\n  → Example: tls-session-cache='{{ VALID_BODY_TLS_SESSION_CACHE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_global_setting_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/global_setting.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_global_setting_put(payload)
    """
    # Step 1: Validate enum values
    if "language" in payload:
        value = payload["language"]
        if value not in VALID_BODY_LANGUAGE:
            return (
                False,
                f"Invalid value for 'language'='{value}'. Must be one of: {', '.join(VALID_BODY_LANGUAGE)}",
            )
    if "gui-ipv6" in payload:
        value = payload["gui-ipv6"]
        if value not in VALID_BODY_GUI_IPV6:
            return (
                False,
                f"Invalid value for 'gui-ipv6'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_IPV6)}",
            )
    if "gui-replacement-message-groups" in payload:
        value = payload["gui-replacement-message-groups"]
        if value not in VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS:
            return (
                False,
                f"Invalid value for 'gui-replacement-message-groups'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS)}",
            )
    if "gui-local-out" in payload:
        value = payload["gui-local-out"]
        if value not in VALID_BODY_GUI_LOCAL_OUT:
            return (
                False,
                f"Invalid value for 'gui-local-out'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_LOCAL_OUT)}",
            )
    if "gui-certificates" in payload:
        value = payload["gui-certificates"]
        if value not in VALID_BODY_GUI_CERTIFICATES:
            return (
                False,
                f"Invalid value for 'gui-certificates'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CERTIFICATES)}",
            )
    if "gui-custom-language" in payload:
        value = payload["gui-custom-language"]
        if value not in VALID_BODY_GUI_CUSTOM_LANGUAGE:
            return (
                False,
                f"Invalid value for 'gui-custom-language'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CUSTOM_LANGUAGE)}",
            )
    if "gui-wireless-opensecurity" in payload:
        value = payload["gui-wireless-opensecurity"]
        if value not in VALID_BODY_GUI_WIRELESS_OPENSECURITY:
            return (
                False,
                f"Invalid value for 'gui-wireless-opensecurity'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WIRELESS_OPENSECURITY)}",
            )
    if "gui-app-detection-sdwan" in payload:
        value = payload["gui-app-detection-sdwan"]
        if value not in VALID_BODY_GUI_APP_DETECTION_SDWAN:
            return (
                False,
                f"Invalid value for 'gui-app-detection-sdwan'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_APP_DETECTION_SDWAN)}",
            )
    if "gui-display-hostname" in payload:
        value = payload["gui-display-hostname"]
        if value not in VALID_BODY_GUI_DISPLAY_HOSTNAME:
            return (
                False,
                f"Invalid value for 'gui-display-hostname'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DISPLAY_HOSTNAME)}",
            )
    if "gui-fortigate-cloud-sandbox" in payload:
        value = payload["gui-fortigate-cloud-sandbox"]
        if value not in VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX:
            return (
                False,
                f"Invalid value for 'gui-fortigate-cloud-sandbox'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX)}",
            )
    if "gui-firmware-upgrade-warning" in payload:
        value = payload["gui-firmware-upgrade-warning"]
        if value not in VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING:
            return (
                False,
                f"Invalid value for 'gui-firmware-upgrade-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING)}",
            )
    if "gui-forticare-registration-setup-warning" in payload:
        value = payload["gui-forticare-registration-setup-warning"]
        if value not in VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING:
            return (
                False,
                f"Invalid value for 'gui-forticare-registration-setup-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING)}",
            )
    if "gui-auto-upgrade-setup-warning" in payload:
        value = payload["gui-auto-upgrade-setup-warning"]
        if value not in VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING:
            return (
                False,
                f"Invalid value for 'gui-auto-upgrade-setup-warning'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING)}",
            )
    if "gui-workflow-management" in payload:
        value = payload["gui-workflow-management"]
        if value not in VALID_BODY_GUI_WORKFLOW_MANAGEMENT:
            return (
                False,
                f"Invalid value for 'gui-workflow-management'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WORKFLOW_MANAGEMENT)}",
            )
    if "gui-cdn-usage" in payload:
        value = payload["gui-cdn-usage"]
        if value not in VALID_BODY_GUI_CDN_USAGE:
            return (
                False,
                f"Invalid value for 'gui-cdn-usage'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CDN_USAGE)}",
            )
    if "admin-https-ssl-versions" in payload:
        value = payload["admin-https-ssl-versions"]
        if value not in VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS:
            return (
                False,
                f"Invalid value for 'admin-https-ssl-versions'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS)}",
            )
    if "admin-https-ssl-ciphersuites" in payload:
        value = payload["admin-https-ssl-ciphersuites"]
        if value not in VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES:
            return (
                False,
                f"Invalid value for 'admin-https-ssl-ciphersuites'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES)}",
            )
    if "admin-https-ssl-banned-ciphers" in payload:
        value = payload["admin-https-ssl-banned-ciphers"]
        if value not in VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS:
            return (
                False,
                f"Invalid value for 'admin-https-ssl-banned-ciphers'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS)}",
            )
    if "ssd-trim-freq" in payload:
        value = payload["ssd-trim-freq"]
        if value not in VALID_BODY_SSD_TRIM_FREQ:
            return (
                False,
                f"Invalid value for 'ssd-trim-freq'='{value}'. Must be one of: {', '.join(VALID_BODY_SSD_TRIM_FREQ)}",
            )
    if "ssd-trim-weekday" in payload:
        value = payload["ssd-trim-weekday"]
        if value not in VALID_BODY_SSD_TRIM_WEEKDAY:
            return (
                False,
                f"Invalid value for 'ssd-trim-weekday'='{value}'. Must be one of: {', '.join(VALID_BODY_SSD_TRIM_WEEKDAY)}",
            )
    if "admin-concurrent" in payload:
        value = payload["admin-concurrent"]
        if value not in VALID_BODY_ADMIN_CONCURRENT:
            return (
                False,
                f"Invalid value for 'admin-concurrent'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_CONCURRENT)}",
            )
    if "purdue-level" in payload:
        value = payload["purdue-level"]
        if value not in VALID_BODY_PURDUE_LEVEL:
            return (
                False,
                f"Invalid value for 'purdue-level'='{value}'. Must be one of: {', '.join(VALID_BODY_PURDUE_LEVEL)}",
            )
    if "daily-restart" in payload:
        value = payload["daily-restart"]
        if value not in VALID_BODY_DAILY_RESTART:
            return (
                False,
                f"Invalid value for 'daily-restart'='{value}'. Must be one of: {', '.join(VALID_BODY_DAILY_RESTART)}",
            )
    if "wad-restart-mode" in payload:
        value = payload["wad-restart-mode"]
        if value not in VALID_BODY_WAD_RESTART_MODE:
            return (
                False,
                f"Invalid value for 'wad-restart-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_WAD_RESTART_MODE)}",
            )
    if "batch-cmdb" in payload:
        value = payload["batch-cmdb"]
        if value not in VALID_BODY_BATCH_CMDB:
            return (
                False,
                f"Invalid value for 'batch-cmdb'='{value}'. Must be one of: {', '.join(VALID_BODY_BATCH_CMDB)}",
            )
    if "multi-factor-authentication" in payload:
        value = payload["multi-factor-authentication"]
        if value not in VALID_BODY_MULTI_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'multi-factor-authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTI_FACTOR_AUTHENTICATION)}",
            )
    if "ssl-min-proto-version" in payload:
        value = payload["ssl-min-proto-version"]
        if value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid value for 'ssl-min-proto-version'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )
    if "autorun-log-fsck" in payload:
        value = payload["autorun-log-fsck"]
        if value not in VALID_BODY_AUTORUN_LOG_FSCK:
            return (
                False,
                f"Invalid value for 'autorun-log-fsck'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTORUN_LOG_FSCK)}",
            )
    if "traffic-priority" in payload:
        value = payload["traffic-priority"]
        if value not in VALID_BODY_TRAFFIC_PRIORITY:
            return (
                False,
                f"Invalid value for 'traffic-priority'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_PRIORITY)}",
            )
    if "traffic-priority-level" in payload:
        value = payload["traffic-priority-level"]
        if value not in VALID_BODY_TRAFFIC_PRIORITY_LEVEL:
            return (
                False,
                f"Invalid value for 'traffic-priority-level'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_PRIORITY_LEVEL)}",
            )
    if "quic-congestion-control-algo" in payload:
        value = payload["quic-congestion-control-algo"]
        if value not in VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO:
            return (
                False,
                f"Invalid value for 'quic-congestion-control-algo'='{value}'. Must be one of: {', '.join(VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO)}",
            )
    if "quic-udp-payload-size-shaping-per-cid" in payload:
        value = payload["quic-udp-payload-size-shaping-per-cid"]
        if value not in VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID:
            return (
                False,
                f"Invalid value for 'quic-udp-payload-size-shaping-per-cid'='{value}'. Must be one of: {', '.join(VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID)}",
            )
    if "quic-pmtud" in payload:
        value = payload["quic-pmtud"]
        if value not in VALID_BODY_QUIC_PMTUD:
            return (
                False,
                f"Invalid value for 'quic-pmtud'='{value}'. Must be one of: {', '.join(VALID_BODY_QUIC_PMTUD)}",
            )
    if "anti-replay" in payload:
        value = payload["anti-replay"]
        if value not in VALID_BODY_ANTI_REPLAY:
            return (
                False,
                f"Invalid value for 'anti-replay'='{value}'. Must be one of: {', '.join(VALID_BODY_ANTI_REPLAY)}",
            )
    if "send-pmtu-icmp" in payload:
        value = payload["send-pmtu-icmp"]
        if value not in VALID_BODY_SEND_PMTU_ICMP:
            return (
                False,
                f"Invalid value for 'send-pmtu-icmp'='{value}'. Must be one of: {', '.join(VALID_BODY_SEND_PMTU_ICMP)}",
            )
    if "honor-df" in payload:
        value = payload["honor-df"]
        if value not in VALID_BODY_HONOR_DF:
            return (
                False,
                f"Invalid value for 'honor-df'='{value}'. Must be one of: {', '.join(VALID_BODY_HONOR_DF)}",
            )
    if "pmtu-discovery" in payload:
        value = payload["pmtu-discovery"]
        if value not in VALID_BODY_PMTU_DISCOVERY:
            return (
                False,
                f"Invalid value for 'pmtu-discovery'='{value}'. Must be one of: {', '.join(VALID_BODY_PMTU_DISCOVERY)}",
            )
    if "revision-image-auto-backup" in payload:
        value = payload["revision-image-auto-backup"]
        if value not in VALID_BODY_REVISION_IMAGE_AUTO_BACKUP:
            return (
                False,
                f"Invalid value for 'revision-image-auto-backup'='{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_IMAGE_AUTO_BACKUP)}",
            )
    if "revision-backup-on-logout" in payload:
        value = payload["revision-backup-on-logout"]
        if value not in VALID_BODY_REVISION_BACKUP_ON_LOGOUT:
            return (
                False,
                f"Invalid value for 'revision-backup-on-logout'='{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_BACKUP_ON_LOGOUT)}",
            )
    if "strong-crypto" in payload:
        value = payload["strong-crypto"]
        if value not in VALID_BODY_STRONG_CRYPTO:
            return (
                False,
                f"Invalid value for 'strong-crypto'='{value}'. Must be one of: {', '.join(VALID_BODY_STRONG_CRYPTO)}",
            )
    if "ssl-static-key-ciphers" in payload:
        value = payload["ssl-static-key-ciphers"]
        if value not in VALID_BODY_SSL_STATIC_KEY_CIPHERS:
            return (
                False,
                f"Invalid value for 'ssl-static-key-ciphers'='{value}'. Must be one of: {', '.join(VALID_BODY_SSL_STATIC_KEY_CIPHERS)}",
            )
    if "snat-route-change" in payload:
        value = payload["snat-route-change"]
        if value not in VALID_BODY_SNAT_ROUTE_CHANGE:
            return (
                False,
                f"Invalid value for 'snat-route-change'='{value}'. Must be one of: {', '.join(VALID_BODY_SNAT_ROUTE_CHANGE)}",
            )
    if "ipv6-snat-route-change" in payload:
        value = payload["ipv6-snat-route-change"]
        if value not in VALID_BODY_IPV6_SNAT_ROUTE_CHANGE:
            return (
                False,
                f"Invalid value for 'ipv6-snat-route-change'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_SNAT_ROUTE_CHANGE)}",
            )
    if "speedtest-server" in payload:
        value = payload["speedtest-server"]
        if value not in VALID_BODY_SPEEDTEST_SERVER:
            return (
                False,
                f"Invalid value for 'speedtest-server'='{value}'. Must be one of: {', '.join(VALID_BODY_SPEEDTEST_SERVER)}",
            )
    if "cli-audit-log" in payload:
        value = payload["cli-audit-log"]
        if value not in VALID_BODY_CLI_AUDIT_LOG:
            return (
                False,
                f"Invalid value for 'cli-audit-log'='{value}'. Must be one of: {', '.join(VALID_BODY_CLI_AUDIT_LOG)}",
            )
    if "dh-params" in payload:
        value = payload["dh-params"]
        if value not in VALID_BODY_DH_PARAMS:
            return (
                False,
                f"Invalid value for 'dh-params'='{value}'. Must be one of: {', '.join(VALID_BODY_DH_PARAMS)}",
            )
    if "fds-statistics" in payload:
        value = payload["fds-statistics"]
        if value not in VALID_BODY_FDS_STATISTICS:
            return (
                False,
                f"Invalid value for 'fds-statistics'='{value}'. Must be one of: {', '.join(VALID_BODY_FDS_STATISTICS)}",
            )
    if "tcp-option" in payload:
        value = payload["tcp-option"]
        if value not in VALID_BODY_TCP_OPTION:
            return (
                False,
                f"Invalid value for 'tcp-option'='{value}'. Must be one of: {', '.join(VALID_BODY_TCP_OPTION)}",
            )
    if "lldp-transmission" in payload:
        value = payload["lldp-transmission"]
        if value not in VALID_BODY_LLDP_TRANSMISSION:
            return (
                False,
                f"Invalid value for 'lldp-transmission'='{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_TRANSMISSION)}",
            )
    if "lldp-reception" in payload:
        value = payload["lldp-reception"]
        if value not in VALID_BODY_LLDP_RECEPTION:
            return (
                False,
                f"Invalid value for 'lldp-reception'='{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_RECEPTION)}",
            )
    if "proxy-keep-alive-mode" in payload:
        value = payload["proxy-keep-alive-mode"]
        if value not in VALID_BODY_PROXY_KEEP_ALIVE_MODE:
            return (
                False,
                f"Invalid value for 'proxy-keep-alive-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_KEEP_ALIVE_MODE)}",
            )
    if "proxy-auth-lifetime" in payload:
        value = payload["proxy-auth-lifetime"]
        if value not in VALID_BODY_PROXY_AUTH_LIFETIME:
            return (
                False,
                f"Invalid value for 'proxy-auth-lifetime'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_AUTH_LIFETIME)}",
            )
    if "proxy-resource-mode" in payload:
        value = payload["proxy-resource-mode"]
        if value not in VALID_BODY_PROXY_RESOURCE_MODE:
            return (
                False,
                f"Invalid value for 'proxy-resource-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_RESOURCE_MODE)}",
            )
    if "proxy-cert-use-mgmt-vdom" in payload:
        value = payload["proxy-cert-use-mgmt-vdom"]
        if value not in VALID_BODY_PROXY_CERT_USE_MGMT_VDOM:
            return (
                False,
                f"Invalid value for 'proxy-cert-use-mgmt-vdom'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_CERT_USE_MGMT_VDOM)}",
            )
    if "check-protocol-header" in payload:
        value = payload["check-protocol-header"]
        if value not in VALID_BODY_CHECK_PROTOCOL_HEADER:
            return (
                False,
                f"Invalid value for 'check-protocol-header'='{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_PROTOCOL_HEADER)}",
            )
    if "vip-arp-range" in payload:
        value = payload["vip-arp-range"]
        if value not in VALID_BODY_VIP_ARP_RANGE:
            return (
                False,
                f"Invalid value for 'vip-arp-range'='{value}'. Must be one of: {', '.join(VALID_BODY_VIP_ARP_RANGE)}",
            )
    if "reset-sessionless-tcp" in payload:
        value = payload["reset-sessionless-tcp"]
        if value not in VALID_BODY_RESET_SESSIONLESS_TCP:
            return (
                False,
                f"Invalid value for 'reset-sessionless-tcp'='{value}'. Must be one of: {', '.join(VALID_BODY_RESET_SESSIONLESS_TCP)}",
            )
    if "allow-traffic-redirect" in payload:
        value = payload["allow-traffic-redirect"]
        if value not in VALID_BODY_ALLOW_TRAFFIC_REDIRECT:
            return (
                False,
                f"Invalid value for 'allow-traffic-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_TRAFFIC_REDIRECT)}",
            )
    if "ipv6-allow-traffic-redirect" in payload:
        value = payload["ipv6-allow-traffic-redirect"]
        if value not in VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT:
            return (
                False,
                f"Invalid value for 'ipv6-allow-traffic-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT)}",
            )
    if "strict-dirty-session-check" in payload:
        value = payload["strict-dirty-session-check"]
        if value not in VALID_BODY_STRICT_DIRTY_SESSION_CHECK:
            return (
                False,
                f"Invalid value for 'strict-dirty-session-check'='{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_DIRTY_SESSION_CHECK)}",
            )
    if "pre-login-banner" in payload:
        value = payload["pre-login-banner"]
        if value not in VALID_BODY_PRE_LOGIN_BANNER:
            return (
                False,
                f"Invalid value for 'pre-login-banner'='{value}'. Must be one of: {', '.join(VALID_BODY_PRE_LOGIN_BANNER)}",
            )
    if "post-login-banner" in payload:
        value = payload["post-login-banner"]
        if value not in VALID_BODY_POST_LOGIN_BANNER:
            return (
                False,
                f"Invalid value for 'post-login-banner'='{value}'. Must be one of: {', '.join(VALID_BODY_POST_LOGIN_BANNER)}",
            )
    if "tftp" in payload:
        value = payload["tftp"]
        if value not in VALID_BODY_TFTP:
            return (
                False,
                f"Invalid value for 'tftp'='{value}'. Must be one of: {', '.join(VALID_BODY_TFTP)}",
            )
    if "av-failopen" in payload:
        value = payload["av-failopen"]
        if value not in VALID_BODY_AV_FAILOPEN:
            return (
                False,
                f"Invalid value for 'av-failopen'='{value}'. Must be one of: {', '.join(VALID_BODY_AV_FAILOPEN)}",
            )
    if "av-failopen-session" in payload:
        value = payload["av-failopen-session"]
        if value not in VALID_BODY_AV_FAILOPEN_SESSION:
            return (
                False,
                f"Invalid value for 'av-failopen-session'='{value}'. Must be one of: {', '.join(VALID_BODY_AV_FAILOPEN_SESSION)}",
            )
    if "log-single-cpu-high" in payload:
        value = payload["log-single-cpu-high"]
        if value not in VALID_BODY_LOG_SINGLE_CPU_HIGH:
            return (
                False,
                f"Invalid value for 'log-single-cpu-high'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_SINGLE_CPU_HIGH)}",
            )
    if "check-reset-range" in payload:
        value = payload["check-reset-range"]
        if value not in VALID_BODY_CHECK_RESET_RANGE:
            return (
                False,
                f"Invalid value for 'check-reset-range'='{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_RESET_RANGE)}",
            )
    if "upgrade-report" in payload:
        value = payload["upgrade-report"]
        if value not in VALID_BODY_UPGRADE_REPORT:
            return (
                False,
                f"Invalid value for 'upgrade-report'='{value}'. Must be one of: {', '.join(VALID_BODY_UPGRADE_REPORT)}",
            )
    if "admin-https-redirect" in payload:
        value = payload["admin-https-redirect"]
        if value not in VALID_BODY_ADMIN_HTTPS_REDIRECT:
            return (
                False,
                f"Invalid value for 'admin-https-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_REDIRECT)}",
            )
    if "admin-ssh-password" in payload:
        value = payload["admin-ssh-password"]
        if value not in VALID_BODY_ADMIN_SSH_PASSWORD:
            return (
                False,
                f"Invalid value for 'admin-ssh-password'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_SSH_PASSWORD)}",
            )
    if "admin-restrict-local" in payload:
        value = payload["admin-restrict-local"]
        if value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            return (
                False,
                f"Invalid value for 'admin-restrict-local'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_RESTRICT_LOCAL)}",
            )
    if "admin-ssh-v1" in payload:
        value = payload["admin-ssh-v1"]
        if value not in VALID_BODY_ADMIN_SSH_V1:
            return (
                False,
                f"Invalid value for 'admin-ssh-v1'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_SSH_V1)}",
            )
    if "admin-telnet" in payload:
        value = payload["admin-telnet"]
        if value not in VALID_BODY_ADMIN_TELNET:
            return (
                False,
                f"Invalid value for 'admin-telnet'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_TELNET)}",
            )
    if "admin-forticloud-sso-login" in payload:
        value = payload["admin-forticloud-sso-login"]
        if value not in VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN:
            return (
                False,
                f"Invalid value for 'admin-forticloud-sso-login'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN)}",
            )
    if "admin-https-pki-required" in payload:
        value = payload["admin-https-pki-required"]
        if value not in VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED:
            return (
                False,
                f"Invalid value for 'admin-https-pki-required'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED)}",
            )
    if "auth-keepalive" in payload:
        value = payload["auth-keepalive"]
        if value not in VALID_BODY_AUTH_KEEPALIVE:
            return (
                False,
                f"Invalid value for 'auth-keepalive'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_KEEPALIVE)}",
            )
    if "auth-session-limit" in payload:
        value = payload["auth-session-limit"]
        if value not in VALID_BODY_AUTH_SESSION_LIMIT:
            return (
                False,
                f"Invalid value for 'auth-session-limit'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SESSION_LIMIT)}",
            )
    if "clt-cert-req" in payload:
        value = payload["clt-cert-req"]
        if value not in VALID_BODY_CLT_CERT_REQ:
            return (
                False,
                f"Invalid value for 'clt-cert-req'='{value}'. Must be one of: {', '.join(VALID_BODY_CLT_CERT_REQ)}",
            )
    if "cfg-save" in payload:
        value = payload["cfg-save"]
        if value not in VALID_BODY_CFG_SAVE:
            return (
                False,
                f"Invalid value for 'cfg-save'='{value}'. Must be one of: {', '.join(VALID_BODY_CFG_SAVE)}",
            )
    if "reboot-upon-config-restore" in payload:
        value = payload["reboot-upon-config-restore"]
        if value not in VALID_BODY_REBOOT_UPON_CONFIG_RESTORE:
            return (
                False,
                f"Invalid value for 'reboot-upon-config-restore'='{value}'. Must be one of: {', '.join(VALID_BODY_REBOOT_UPON_CONFIG_RESTORE)}",
            )
    if "admin-scp" in payload:
        value = payload["admin-scp"]
        if value not in VALID_BODY_ADMIN_SCP:
            return (
                False,
                f"Invalid value for 'admin-scp'='{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_SCP)}",
            )
    if "wireless-controller" in payload:
        value = payload["wireless-controller"]
        if value not in VALID_BODY_WIRELESS_CONTROLLER:
            return (
                False,
                f"Invalid value for 'wireless-controller'='{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_CONTROLLER)}",
            )
    if "fortiextender" in payload:
        value = payload["fortiextender"]
        if value not in VALID_BODY_FORTIEXTENDER:
            return (
                False,
                f"Invalid value for 'fortiextender'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER)}",
            )
    if "fortiextender-discovery-lockdown" in payload:
        value = payload["fortiextender-discovery-lockdown"]
        if value not in VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN:
            return (
                False,
                f"Invalid value for 'fortiextender-discovery-lockdown'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN)}",
            )
    if "fortiextender-vlan-mode" in payload:
        value = payload["fortiextender-vlan-mode"]
        if value not in VALID_BODY_FORTIEXTENDER_VLAN_MODE:
            return (
                False,
                f"Invalid value for 'fortiextender-vlan-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER_VLAN_MODE)}",
            )
    if "fortiextender-provision-on-authorization" in payload:
        value = payload["fortiextender-provision-on-authorization"]
        if value not in VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION:
            return (
                False,
                f"Invalid value for 'fortiextender-provision-on-authorization'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION)}",
            )
    if "switch-controller" in payload:
        value = payload["switch-controller"]
        if value not in VALID_BODY_SWITCH_CONTROLLER:
            return (
                False,
                f"Invalid value for 'switch-controller'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER)}",
            )
    if "fgd-alert-subscription" in payload:
        value = payload["fgd-alert-subscription"]
        if value not in VALID_BODY_FGD_ALERT_SUBSCRIPTION:
            return (
                False,
                f"Invalid value for 'fgd-alert-subscription'='{value}'. Must be one of: {', '.join(VALID_BODY_FGD_ALERT_SUBSCRIPTION)}",
            )
    if "ipv6-allow-anycast-probe" in payload:
        value = payload["ipv6-allow-anycast-probe"]
        if value not in VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE:
            return (
                False,
                f"Invalid value for 'ipv6-allow-anycast-probe'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE)}",
            )
    if "ipv6-allow-multicast-probe" in payload:
        value = payload["ipv6-allow-multicast-probe"]
        if value not in VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE:
            return (
                False,
                f"Invalid value for 'ipv6-allow-multicast-probe'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE)}",
            )
    if "ipv6-allow-local-in-silent-drop" in payload:
        value = payload["ipv6-allow-local-in-silent-drop"]
        if value not in VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP:
            return (
                False,
                f"Invalid value for 'ipv6-allow-local-in-silent-drop'='{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP)}",
            )
    if "csr-ca-attribute" in payload:
        value = payload["csr-ca-attribute"]
        if value not in VALID_BODY_CSR_CA_ATTRIBUTE:
            return (
                False,
                f"Invalid value for 'csr-ca-attribute'='{value}'. Must be one of: {', '.join(VALID_BODY_CSR_CA_ATTRIBUTE)}",
            )
    if "wimax-4g-usb" in payload:
        value = payload["wimax-4g-usb"]
        if value not in VALID_BODY_WIMAX_4G_USB:
            return (
                False,
                f"Invalid value for 'wimax-4g-usb'='{value}'. Must be one of: {', '.join(VALID_BODY_WIMAX_4G_USB)}",
            )
    if "sslvpn-web-mode" in payload:
        value = payload["sslvpn-web-mode"]
        if value not in VALID_BODY_SSLVPN_WEB_MODE:
            return (
                False,
                f"Invalid value for 'sslvpn-web-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SSLVPN_WEB_MODE)}",
            )
    if "per-user-bal" in payload:
        value = payload["per-user-bal"]
        if value not in VALID_BODY_PER_USER_BAL:
            return (
                False,
                f"Invalid value for 'per-user-bal'='{value}'. Must be one of: {', '.join(VALID_BODY_PER_USER_BAL)}",
            )
    if "wad-source-affinity" in payload:
        value = payload["wad-source-affinity"]
        if value not in VALID_BODY_WAD_SOURCE_AFFINITY:
            return (
                False,
                f"Invalid value for 'wad-source-affinity'='{value}'. Must be one of: {', '.join(VALID_BODY_WAD_SOURCE_AFFINITY)}",
            )
    if "login-timestamp" in payload:
        value = payload["login-timestamp"]
        if value not in VALID_BODY_LOGIN_TIMESTAMP:
            return (
                False,
                f"Invalid value for 'login-timestamp'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_TIMESTAMP)}",
            )
    if "ip-conflict-detection" in payload:
        value = payload["ip-conflict-detection"]
        if value not in VALID_BODY_IP_CONFLICT_DETECTION:
            return (
                False,
                f"Invalid value for 'ip-conflict-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_IP_CONFLICT_DETECTION)}",
            )
    if "special-file-23-support" in payload:
        value = payload["special-file-23-support"]
        if value not in VALID_BODY_SPECIAL_FILE_23_SUPPORT:
            return (
                False,
                f"Invalid value for 'special-file-23-support'='{value}'. Must be one of: {', '.join(VALID_BODY_SPECIAL_FILE_23_SUPPORT)}",
            )
    if "log-uuid-address" in payload:
        value = payload["log-uuid-address"]
        if value not in VALID_BODY_LOG_UUID_ADDRESS:
            return (
                False,
                f"Invalid value for 'log-uuid-address'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_UUID_ADDRESS)}",
            )
    if "log-ssl-connection" in payload:
        value = payload["log-ssl-connection"]
        if value not in VALID_BODY_LOG_SSL_CONNECTION:
            return (
                False,
                f"Invalid value for 'log-ssl-connection'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_SSL_CONNECTION)}",
            )
    if "gui-rest-api-cache" in payload:
        value = payload["gui-rest-api-cache"]
        if value not in VALID_BODY_GUI_REST_API_CACHE:
            return (
                False,
                f"Invalid value for 'gui-rest-api-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_REST_API_CACHE)}",
            )
    if "rest-api-key-url-query" in payload:
        value = payload["rest-api-key-url-query"]
        if value not in VALID_BODY_REST_API_KEY_URL_QUERY:
            return (
                False,
                f"Invalid value for 'rest-api-key-url-query'='{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_KEY_URL_QUERY)}",
            )
    if "ipsec-qat-offload" in payload:
        value = payload["ipsec-qat-offload"]
        if value not in VALID_BODY_IPSEC_QAT_OFFLOAD:
            return (
                False,
                f"Invalid value for 'ipsec-qat-offload'='{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_QAT_OFFLOAD)}",
            )
    if "private-data-encryption" in payload:
        value = payload["private-data-encryption"]
        if value not in VALID_BODY_PRIVATE_DATA_ENCRYPTION:
            return (
                False,
                f"Invalid value for 'private-data-encryption'='{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_DATA_ENCRYPTION)}",
            )
    if "auto-auth-extension-device" in payload:
        value = payload["auto-auth-extension-device"]
        if value not in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE:
            return (
                False,
                f"Invalid value for 'auto-auth-extension-device'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE)}",
            )
    if "gui-theme" in payload:
        value = payload["gui-theme"]
        if value not in VALID_BODY_GUI_THEME:
            return (
                False,
                f"Invalid value for 'gui-theme'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_THEME)}",
            )
    if "gui-date-format" in payload:
        value = payload["gui-date-format"]
        if value not in VALID_BODY_GUI_DATE_FORMAT:
            return (
                False,
                f"Invalid value for 'gui-date-format'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DATE_FORMAT)}",
            )
    if "gui-date-time-source" in payload:
        value = payload["gui-date-time-source"]
        if value not in VALID_BODY_GUI_DATE_TIME_SOURCE:
            return (
                False,
                f"Invalid value for 'gui-date-time-source'='{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DATE_TIME_SOURCE)}",
            )
    if "cloud-communication" in payload:
        value = payload["cloud-communication"]
        if value not in VALID_BODY_CLOUD_COMMUNICATION:
            return (
                False,
                f"Invalid value for 'cloud-communication'='{value}'. Must be one of: {', '.join(VALID_BODY_CLOUD_COMMUNICATION)}",
            )
    if "fortitoken-cloud" in payload:
        value = payload["fortitoken-cloud"]
        if value not in VALID_BODY_FORTITOKEN_CLOUD:
            return (
                False,
                f"Invalid value for 'fortitoken-cloud'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTITOKEN_CLOUD)}",
            )
    if "fortitoken-cloud-push-status" in payload:
        value = payload["fortitoken-cloud-push-status"]
        if value not in VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS:
            return (
                False,
                f"Invalid value for 'fortitoken-cloud-push-status'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS)}",
            )
    if "irq-time-accounting" in payload:
        value = payload["irq-time-accounting"]
        if value not in VALID_BODY_IRQ_TIME_ACCOUNTING:
            return (
                False,
                f"Invalid value for 'irq-time-accounting'='{value}'. Must be one of: {', '.join(VALID_BODY_IRQ_TIME_ACCOUNTING)}",
            )
    if "management-port-use-admin-sport" in payload:
        value = payload["management-port-use-admin-sport"]
        if value not in VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT:
            return (
                False,
                f"Invalid value for 'management-port-use-admin-sport'='{value}'. Must be one of: {', '.join(VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT)}",
            )
    if "forticonverter-integration" in payload:
        value = payload["forticonverter-integration"]
        if value not in VALID_BODY_FORTICONVERTER_INTEGRATION:
            return (
                False,
                f"Invalid value for 'forticonverter-integration'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTICONVERTER_INTEGRATION)}",
            )
    if "forticonverter-config-upload" in payload:
        value = payload["forticonverter-config-upload"]
        if value not in VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD:
            return (
                False,
                f"Invalid value for 'forticonverter-config-upload'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD)}",
            )
    if "internet-service-database" in payload:
        value = payload["internet-service-database"]
        if value not in VALID_BODY_INTERNET_SERVICE_DATABASE:
            return (
                False,
                f"Invalid value for 'internet-service-database'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_DATABASE)}",
            )
    if "early-tcp-npu-session" in payload:
        value = payload["early-tcp-npu-session"]
        if value not in VALID_BODY_EARLY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid value for 'early-tcp-npu-session'='{value}'. Must be one of: {', '.join(VALID_BODY_EARLY_TCP_NPU_SESSION)}",
            )
    if "npu-neighbor-update" in payload:
        value = payload["npu-neighbor-update"]
        if value not in VALID_BODY_NPU_NEIGHBOR_UPDATE:
            return (
                False,
                f"Invalid value for 'npu-neighbor-update'='{value}'. Must be one of: {', '.join(VALID_BODY_NPU_NEIGHBOR_UPDATE)}",
            )
    if "delay-tcp-npu-session" in payload:
        value = payload["delay-tcp-npu-session"]
        if value not in VALID_BODY_DELAY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid value for 'delay-tcp-npu-session'='{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_TCP_NPU_SESSION)}",
            )
    if "interface-subnet-usage" in payload:
        value = payload["interface-subnet-usage"]
        if value not in VALID_BODY_INTERFACE_SUBNET_USAGE:
            return (
                False,
                f"Invalid value for 'interface-subnet-usage'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SUBNET_USAGE)}",
            )
    if "fortigslb-integration" in payload:
        value = payload["fortigslb-integration"]
        if value not in VALID_BODY_FORTIGSLB_INTEGRATION:
            return (
                False,
                f"Invalid value for 'fortigslb-integration'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGSLB_INTEGRATION)}",
            )
    if "auth-session-auto-backup" in payload:
        value = payload["auth-session-auto-backup"]
        if value not in VALID_BODY_AUTH_SESSION_AUTO_BACKUP:
            return (
                False,
                f"Invalid value for 'auth-session-auto-backup'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SESSION_AUTO_BACKUP)}",
            )
    if "auth-session-auto-backup-interval" in payload:
        value = payload["auth-session-auto-backup-interval"]
        if value not in VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL:
            return (
                False,
                f"Invalid value for 'auth-session-auto-backup-interval'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL)}",
            )
    if "application-bandwidth-tracking" in payload:
        value = payload["application-bandwidth-tracking"]
        if value not in VALID_BODY_APPLICATION_BANDWIDTH_TRACKING:
            return (
                False,
                f"Invalid value for 'application-bandwidth-tracking'='{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_BANDWIDTH_TRACKING)}",
            )
    if "tls-session-cache" in payload:
        value = payload["tls-session-cache"]
        if value not in VALID_BODY_TLS_SESSION_CACHE:
            return (
                False,
                f"Invalid value for 'tls-session-cache'='{value}'. Must be one of: {', '.join(VALID_BODY_TLS_SESSION_CACHE)}",
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
    "endpoint": "system/global_setting",
    "category": "cmdb",
    "api_path": "system/global",
    "help": "Configure global attributes.",
    "total_fields": 249,
    "required_fields_count": 4,
    "fields_with_defaults_count": 248,
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
