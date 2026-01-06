"""Validation helpers for system/sdwan - Auto-generated"""

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
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "status": "disable",
    "load-balance-mode": "source-ip-based",
    "speedtest-bypass-routing": "disable",
    "duplication-max-num": 2,
    "duplication-max-discrepancy": 250,
    "neighbor-hold-down": "disable",
    "neighbor-hold-down-time": 0,
    "app-perf-log-period": 0,
    "neighbor-hold-boot-time": 0,
    "fail-detect": "disable",
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
    "status": "option",  # Enable/disable SD-WAN.
    "load-balance-mode": "option",  # Algorithm or mode to use for load balancing Internet traffic
    "speedtest-bypass-routing": "option",  # Enable/disable bypass routing when speedtest on a SD-WAN mem
    "duplication-max-num": "integer",  # Maximum number of interface members a packet is duplicated i
    "duplication-max-discrepancy": "integer",  # Maximum discrepancy between two packets for deduplication in
    "neighbor-hold-down": "option",  # Enable/disable hold switching from the secondary neighbor to
    "neighbor-hold-down-time": "integer",  # Waiting period in seconds when switching from the secondary 
    "app-perf-log-period": "integer",  # Time interval in seconds that application performance logs a
    "neighbor-hold-boot-time": "integer",  # Waiting period in seconds when switching from the primary ne
    "fail-detect": "option",  # Enable/disable SD-WAN Internet connection status checking (f
    "fail-alert-interfaces": "string",  # Physical interfaces that will be alerted.
    "zone": "string",  # Configure SD-WAN zones.
    "members": "string",  # FortiGate interfaces added to the SD-WAN.
    "health-check": "string",  # SD-WAN status checking or health checking. Identify a server
    "service": "string",  # Create SD-WAN rules (also called services) to control how se
    "neighbor": "string",  # Create SD-WAN neighbor from BGP neighbor table to control ro
    "duplication": "string",  # Create SD-WAN duplication rule.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "status": "Enable/disable SD-WAN.",
    "load-balance-mode": "Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.",
    "speedtest-bypass-routing": "Enable/disable bypass routing when speedtest on a SD-WAN member.",
    "duplication-max-num": "Maximum number of interface members a packet is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3, the original packet plus 2 more copies are created).",
    "duplication-max-discrepancy": "Maximum discrepancy between two packets for deduplication in milliseconds (250 - 1000, default = 250).",
    "neighbor-hold-down": "Enable/disable hold switching from the secondary neighbor to the primary neighbor.",
    "neighbor-hold-down-time": "Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. (0 - 10000000, default = 0).",
    "app-perf-log-period": "Time interval in seconds that application performance logs are generated (0 - 3600, default = 0).",
    "neighbor-hold-boot-time": "Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. (0 - 10000000, default = 0).",
    "fail-detect": "Enable/disable SD-WAN Internet connection status checking (failure detection).",
    "fail-alert-interfaces": "Physical interfaces that will be alerted.",
    "zone": "Configure SD-WAN zones.",
    "members": "FortiGate interfaces added to the SD-WAN.",
    "health-check": "SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.",
    "service": "Create SD-WAN rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN.",
    "neighbor": "Create SD-WAN neighbor from BGP neighbor table to control route advertisements according to SLA status.",
    "duplication": "Create SD-WAN duplication rule.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "duplication-max-num": {"type": "integer", "min": 2, "max": 4},
    "duplication-max-discrepancy": {"type": "integer", "min": 250, "max": 1000},
    "neighbor-hold-down-time": {"type": "integer", "min": 0, "max": 10000000},
    "app-perf-log-period": {"type": "integer", "min": 0, "max": 3600},
    "neighbor-hold-boot-time": {"type": "integer", "min": 0, "max": 10000000},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "fail-alert-interfaces": {
        "name": {
            "type": "string",
            "help": "Physical interface name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "zone": {
        "name": {
            "type": "string",
            "help": "Zone name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "advpn-select": {
            "type": "option",
            "help": "Enable/disable selection of ADVPN based on SDWAN information.",
            "default": "disable",
            "options": [{"help": "Enable selection of ADVPN based on SDWAN information.", "label": "Enable", "name": "enable"}, {"help": "Disable selection of ADVPN based on SDWAN information.", "label": "Disable", "name": "disable"}],
        },
        "advpn-health-check": {
            "type": "string",
            "help": "Health check for ADVPN local overlay link quality.",
            "default": "",
            "max_length": 35,
        },
        "service-sla-tie-break": {
            "type": "option",
            "help": "Method of selecting member if more than one meets the SLA.",
            "default": "cfg-order",
            "options": [{"help": "Members that meet the SLA are selected in the order they are configured.", "label": "Cfg Order", "name": "cfg-order"}, {"help": "Members that meet the SLA are selected that match the longest prefix in the routing table.", "label": "Fib Best Match", "name": "fib-best-match"}, {"help": "Members that meet the SLA are reselected again based link-cost-factor.", "label": "Priority", "name": "priority"}, {"help": "Members that meet the SLA are selected by matching the input device.", "label": "Input Device", "name": "input-device"}],
        },
        "minimum-sla-meet-members": {
            "type": "integer",
            "help": "Minimum number of members which meet SLA when the neighbor is preferred.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
    },
    "members": {
        "seq-num": {
            "type": "integer",
            "help": "Sequence number(1-512).",
            "default": 0,
            "min_value": 0,
            "max_value": 512,
        },
        "interface": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 15,
        },
        "zone": {
            "type": "string",
            "help": "Zone name.",
            "default": "virtual-wan-link",
            "max_length": 35,
        },
        "gateway": {
            "type": "ipv4-address",
            "help": "The default gateway for this interface. Usually the default gateway of the Internet service provider that this interface is connected to.",
            "default": "0.0.0.0",
        },
        "preferred-source": {
            "type": "ipv4-address",
            "help": "Preferred source of route for this member.",
            "default": "0.0.0.0",
        },
        "source": {
            "type": "ipv4-address",
            "help": "Source IP address used in the health-check packet to the server.",
            "default": "0.0.0.0",
        },
        "gateway6": {
            "type": "ipv6-address",
            "help": "IPv6 gateway.",
            "default": "::",
        },
        "source6": {
            "type": "ipv6-address",
            "help": "Source IPv6 address used in the health-check packet to the server.",
            "default": "::",
        },
        "cost": {
            "type": "integer",
            "help": "Cost of this interface for services in SLA mode (0 - 4294967295, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "weight": {
            "type": "integer",
            "help": "Weight of this interface for weighted load balancing. (1 - 255) More traffic is directed to interfaces with higher weights.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "priority": {
            "type": "integer",
            "help": "Priority of the interface for IPv4 (1 - 65535, default = 1). Used for SD-WAN rules or priority rules.",
            "default": 1,
            "min_value": 1,
            "max_value": 65535,
        },
        "priority6": {
            "type": "integer",
            "help": "Priority of the interface for IPv6 (1 - 65535, default = 1024). Used for SD-WAN rules or priority rules.",
            "default": 1024,
            "min_value": 1,
            "max_value": 65535,
        },
        "priority-in-sla": {
            "type": "integer",
            "help": "Preferred priority of routes to this member when this member is in-sla (0 - 65535, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "priority-out-sla": {
            "type": "integer",
            "help": "Preferred priority of routes to this member when this member is out-of-sla (0 - 65535, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "spillover-threshold": {
            "type": "integer",
            "help": "Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN.",
            "default": 0,
            "min_value": 0,
            "max_value": 16776000,
        },
        "ingress-spillover-threshold": {
            "type": "integer",
            "help": "Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN.",
            "default": 0,
            "min_value": 0,
            "max_value": 16776000,
        },
        "volume-ratio": {
            "type": "integer",
            "help": "Measured volume ratio (this value / sum of all values = percentage of link volume, 1 - 255).",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable this interface in the SD-WAN.",
            "default": "enable",
            "options": [{"help": "Disable this interface in the SD-WAN.", "label": "Disable", "name": "disable"}, {"help": "Enable this interface in the SD-WAN.", "label": "Enable", "name": "enable"}],
        },
        "transport-group": {
            "type": "integer",
            "help": "Measured transport group (0 - 255).",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "comment": {
            "type": "var-string",
            "help": "Comments.",
            "max_length": 255,
        },
    },
    "health-check": {
        "name": {
            "type": "string",
            "help": "Status check or health check name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "fortiguard": {
            "type": "option",
            "help": "Enable/disable use of FortiGuard predefined server.",
            "default": "disable",
            "options": [{"help": "Disable use of FortiGuard predefined server.", "label": "Disable", "name": "disable"}, {"help": "Enable use of FortiGuard predefined server.", "label": "Enable", "name": "enable"}],
        },
        "fortiguard-name": {
            "type": "string",
            "help": "Predefined health-check target name.",
            "default": "",
            "max_length": 35,
        },
        "probe-packets": {
            "type": "option",
            "help": "Enable/disable transmission of probe packets.",
            "default": "enable",
            "options": [{"help": "Disable transmission of probe packets.", "label": "Disable", "name": "disable"}, {"help": "Enable transmission of probe packets.", "label": "Enable", "name": "enable"}],
        },
        "addr-mode": {
            "type": "option",
            "help": "Address mode (IPv4 or IPv6).",
            "default": "ipv4",
            "options": [{"help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}],
        },
        "system-dns": {
            "type": "option",
            "help": "Enable/disable system DNS as the probe server.",
            "default": "disable",
            "options": [{"help": "Disable system DNS as the probe server.", "label": "Disable", "name": "disable"}, {"help": "Enable system DNS as the probe server.", "label": "Enable", "name": "enable"}],
        },
        "server": {
            "type": "string",
            "help": "IP address or FQDN name of the server.",
            "default": "",
            "max_length": 79,
        },
        "detect-mode": {
            "type": "option",
            "help": "The mode determining how to detect the server.",
            "default": "active",
            "options": [{"help": "The probes are sent actively.", "label": "Active", "name": "active"}, {"help": "The traffic measures health without probes.", "label": "Passive", "name": "passive"}, {"help": "The probes are sent in case of no new traffic.", "label": "Prefer Passive", "name": "prefer-passive"}, {"help": "Link health obtained from remote peers.", "label": "Remote", "name": "remote"}, {"help": "Traffic health is measured from the fabric connectors.", "label": "Agent Based", "name": "agent-based"}],
        },
        "protocol": {
            "type": "option",
            "help": "Protocol used to determine if the FortiGate can communicate with the server.",
            "default": "ping",
            "options": [{"help": "Use PING to test the link with the server.", "label": "Ping", "name": "ping"}, {"help": "Use TCP echo to test the link with the server.", "label": "Tcp Echo", "name": "tcp-echo"}, {"help": "Use UDP echo to test the link with the server.", "label": "Udp Echo", "name": "udp-echo"}, {"help": "Use HTTP-GET to test the link with the server.", "label": "Http", "name": "http"}, {"help": "Use HTTPS-GET to test the link with the server.", "label": "Https", "name": "https"}, {"help": "Use TWAMP to test the link with the server.", "label": "Twamp", "name": "twamp"}, {"help": "Use DNS query to test the link with the server.", "label": "Dns", "name": "dns"}, {"help": "Use a full TCP connection to test the link with the server.", "label": "Tcp Connect", "name": "tcp-connect"}, {"help": "Use FTP to test the link with the server.", "label": "Ftp", "name": "ftp"}],
        },
        "port": {
            "type": "integer",
            "help": "Port number used to communicate with the server over the selected protocol (0 - 65535, default = 0, auto select. http, tcp-connect: 80, udp-echo, tcp-echo: 7, dns: 53, ftp: 21, twamp: 862).",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "quality-measured-method": {
            "type": "option",
            "help": "Method to measure the quality of tcp-connect.",
            "default": "half-open",
            "options": [{"help": "Measure the round trip between syn and ack.", "label": "Half Open", "name": "half-open"}, {"help": "Measure the round trip between fin and ack.", "label": "Half Close", "name": "half-close"}],
        },
        "security-mode": {
            "type": "option",
            "help": "Twamp controller security mode.",
            "default": "none",
            "options": [{"help": "Unauthenticated mode.", "label": "None", "name": "none"}, {"help": "Authenticated mode.", "label": "Authentication", "name": "authentication"}],
        },
        "user": {
            "type": "string",
            "help": "The user name to access probe server.",
            "default": "",
            "max_length": 64,
        },
        "password": {
            "type": "password",
            "help": "TWAMP controller password in authentication mode.",
            "max_length": 128,
        },
        "packet-size": {
            "type": "integer",
            "help": "Packet size of a TWAMP test session. (124/158 - 1024)",
            "default": 124,
            "min_value": 0,
            "max_value": 65535,
        },
        "ha-priority": {
            "type": "integer",
            "help": "HA election priority (1 - 50).",
            "default": 1,
            "min_value": 1,
            "max_value": 50,
        },
        "ftp-mode": {
            "type": "option",
            "help": "FTP mode.",
            "default": "passive",
            "options": [{"help": "The FTP health-check initiates and establishes the data connection.", "label": "Passive", "name": "passive"}, {"help": "The FTP server initiates and establishes the data connection.", "label": "Port", "name": "port"}],
        },
        "ftp-file": {
            "type": "string",
            "help": "Full path and file name on the FTP server to download for FTP health-check to probe.",
            "default": "",
            "max_length": 254,
        },
        "http-get": {
            "type": "string",
            "help": "URL used to communicate with the server if the protocol if the protocol is HTTP.",
            "default": "/",
            "max_length": 1024,
        },
        "http-agent": {
            "type": "string",
            "help": "String in the http-agent field in the HTTP header.",
            "default": "Chrome/ Safari/",
            "max_length": 1024,
        },
        "http-match": {
            "type": "string",
            "help": "Response string expected from the server if the protocol is HTTP.",
            "default": "",
            "max_length": 1024,
        },
        "dns-request-domain": {
            "type": "string",
            "help": "Fully qualified domain name to resolve for the DNS probe.",
            "default": "www.example.com",
            "max_length": 255,
        },
        "dns-match-ip": {
            "type": "ipv4-address",
            "help": "Response IP expected from DNS server if the protocol is DNS.",
            "default": "0.0.0.0",
        },
        "interval": {
            "type": "integer",
            "help": "Status check interval in milliseconds, or the time between attempting to connect to the server (20 - 3600*1000 msec, default = 500).",
            "default": 500,
            "min_value": 20,
            "max_value": 3600000,
        },
        "probe-timeout": {
            "type": "integer",
            "help": "Time to wait before a probe packet is considered lost (20 - 3600*1000 msec, default = 500).",
            "default": 500,
            "min_value": 20,
            "max_value": 3600000,
        },
        "agent-probe-timeout": {
            "type": "integer",
            "help": "Time to wait before a probe packet is considered lost when detect-mode is agent (5000 - 3600*1000 msec, default = 60000).",
            "default": 60000,
            "min_value": 5000,
            "max_value": 3600000,
        },
        "remote-probe-timeout": {
            "type": "integer",
            "help": "Time to wait before a probe packet is considered lost when detect-mode is remote (20 - 3600*1000 msec, default = 5000).",
            "default": 5000,
            "min_value": 20,
            "max_value": 3600000,
        },
        "failtime": {
            "type": "integer",
            "help": "Number of failures before server is considered lost (1 - 3600, default = 5).",
            "default": 5,
            "min_value": 1,
            "max_value": 3600,
        },
        "recoverytime": {
            "type": "integer",
            "help": "Number of successful responses received before server is considered recovered (1 - 3600, default = 5).",
            "default": 5,
            "min_value": 1,
            "max_value": 3600,
        },
        "probe-count": {
            "type": "integer",
            "help": "Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).",
            "default": 30,
            "min_value": 5,
            "max_value": 30,
        },
        "diffservcode": {
            "type": "user",
            "help": "Differentiated services code point (DSCP) in the IP header of the probe packet.",
            "default": "",
        },
        "update-cascade-interface": {
            "type": "option",
            "help": "Enable/disable update cascade interface.",
            "default": "enable",
            "options": [{"help": "Enable update cascade interface.", "label": "Enable", "name": "enable"}, {"help": "Disable update cascade interface.", "label": "Disable", "name": "disable"}],
        },
        "update-static-route": {
            "type": "option",
            "help": "Enable/disable updating the static route.",
            "default": "enable",
            "options": [{"help": "Enable updating the static route.", "label": "Enable", "name": "enable"}, {"help": "Disable updating the static route.", "label": "Disable", "name": "disable"}],
        },
        "update-bgp-route": {
            "type": "option",
            "help": "Enable/disable updating the BGP route.",
            "default": "disable",
            "options": [{"help": "Enable updating the BGP route.", "label": "Enable", "name": "enable"}, {"help": "Disable updating the BGP route.", "label": "Disable", "name": "disable"}],
        },
        "embed-measured-health": {
            "type": "option",
            "help": "Enable/disable embedding measured health information.",
            "default": "disable",
            "options": [{"help": "Enable embed measured health.", "label": "Enable", "name": "enable"}, {"help": "Disable embed measured health.", "label": "Disable", "name": "disable"}],
        },
        "sla-id-redistribute": {
            "type": "integer",
            "help": "Select the ID from the SLA sub-table. The selected SLA's priority value will be distributed into the routing table (0 - 32, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 32,
        },
        "sla-fail-log-period": {
            "type": "integer",
            "help": "Time interval in seconds that SLA fail log messages will be generated (0 - 3600, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 3600,
        },
        "sla-pass-log-period": {
            "type": "integer",
            "help": "Time interval in seconds that SLA pass log messages will be generated (0 - 3600, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 3600,
        },
        "threshold-warning-packetloss": {
            "type": "integer",
            "help": "Warning threshold for packet loss (percentage, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 100,
        },
        "threshold-alert-packetloss": {
            "type": "integer",
            "help": "Alert threshold for packet loss (percentage, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 100,
        },
        "threshold-warning-latency": {
            "type": "integer",
            "help": "Warning threshold for latency (ms, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "threshold-alert-latency": {
            "type": "integer",
            "help": "Alert threshold for latency (ms, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "threshold-warning-jitter": {
            "type": "integer",
            "help": "Warning threshold for jitter (ms, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "threshold-alert-jitter": {
            "type": "integer",
            "help": "Alert threshold for jitter (ms, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "vrf": {
            "type": "integer",
            "help": "Virtual Routing Forwarding ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 511,
        },
        "source": {
            "type": "ipv4-address",
            "help": "Source IP address used in the health-check packet to the server.",
            "default": "0.0.0.0",
        },
        "source6": {
            "type": "ipv6-address",
            "help": "Source IPv6 address used in the health-check packet to server.",
            "default": "::",
        },
        "members": {
            "type": "string",
            "help": "Member sequence number list.",
        },
        "mos-codec": {
            "type": "option",
            "help": "Codec to use for MOS calculation (default = g711).",
            "default": "g711",
            "options": [{"help": "Calculate MOS based on the G.711 codec.", "label": "G711", "name": "g711"}, {"help": "Calculate MOS based on the G.722 codec.", "label": "G722", "name": "g722"}, {"help": "Calculate MOS based on the G.729 codec.", "label": "G729", "name": "g729"}],
        },
        "class-id": {
            "type": "integer",
            "help": "Traffic class ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "packet-loss-weight": {
            "type": "integer",
            "help": "Coefficient of packet-loss in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "latency-weight": {
            "type": "integer",
            "help": "Coefficient of latency in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "jitter-weight": {
            "type": "integer",
            "help": "Coefficient of jitter in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "bandwidth-weight": {
            "type": "integer",
            "help": "Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "sla": {
            "type": "string",
            "help": "Service level agreement (SLA).",
        },
    },
    "service": {
        "id": {
            "type": "integer",
            "help": "SD-WAN rule ID (1 - 4000).",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 4000,
        },
        "name": {
            "type": "string",
            "help": "SD-WAN rule name.",
            "default": "",
            "max_length": 35,
        },
        "addr-mode": {
            "type": "option",
            "help": "Address mode (IPv4 or IPv6).",
            "default": "ipv4",
            "options": [{"help": "IPv4 mode.", "label": "Ipv4", "name": "ipv4"}, {"help": "IPv6 mode.", "label": "Ipv6", "name": "ipv6"}],
        },
        "load-balance": {
            "type": "option",
            "help": "Enable/disable load-balance.",
            "default": "disable",
            "options": [{"help": "Enable load-balance.", "label": "Enable", "name": "enable"}, {"help": "Disable load-balance.", "label": "Disable", "name": "disable"}],
        },
        "input-device": {
            "type": "string",
            "help": "Source interface name.",
        },
        "input-device-negate": {
            "type": "option",
            "help": "Enable/disable negation of input device match.",
            "default": "disable",
            "options": [{"help": "Enable negation of input device match.", "label": "Enable", "name": "enable"}, {"help": "Disable negation of input device match.", "label": "Disable", "name": "disable"}],
        },
        "input-zone": {
            "type": "string",
            "help": "Source input-zone name.",
        },
        "mode": {
            "type": "option",
            "help": "Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.",
            "default": "manual",
            "options": [{"help": "Assign interfaces a priority based on quality.", "label": "Auto", "name": "auto"}, {"help": "Assign interfaces a priority manually.", "label": "Manual", "name": "manual"}, {"help": "Assign interfaces a priority based on the link-cost-factor quality of the interface.", "label": "Priority", "name": "priority"}, {"help": "Assign interfaces a priority based on selected SLA settings.", "label": "Sla", "name": "sla"}],
        },
        "zone-mode": {
            "type": "option",
            "help": "Enable/disable zone mode.",
            "default": "disable",
            "options": [{"help": "Traffic steered based on zone.", "label": "Enable", "name": "enable"}, {"help": "Traffic steered based on member.", "label": "Disable", "name": "disable"}],
        },
        "minimum-sla-meet-members": {
            "type": "integer",
            "help": "Minimum number of members which meet SLA.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "hash-mode": {
            "type": "option",
            "help": "Hash algorithm for selected priority members for load balance mode.",
            "default": "round-robin",
            "options": [{"help": "All traffic are distributed to selected interfaces in equal portions and circular order.", "label": "Round Robin", "name": "round-robin"}, {"help": "All traffic from a source IP is sent to the same interface.", "label": "Source Ip Based", "name": "source-ip-based"}, {"help": "All traffic from a source IP to a destination IP is sent to the same interface.", "label": "Source Dest Ip Based", "name": "source-dest-ip-based"}, {"help": "All traffic are distributed to a selected interface with most available bandwidth for incoming traffic.", "label": "Inbandwidth", "name": "inbandwidth"}, {"help": "All traffic are distributed to a selected interface with most available bandwidth for outgoing traffic.", "label": "Outbandwidth", "name": "outbandwidth"}, {"help": "All traffic are distributed to a selected interface with most available bandwidth for both incoming and outgoing traffic.", "label": "Bibandwidth", "name": "bibandwidth"}],
        },
        "shortcut-priority": {
            "type": "option",
            "help": "High priority of ADVPN shortcut for this service.",
            "default": "auto",
            "options": [{"help": "Enable a high priority of ADVPN shortcut for this service.", "label": "Enable", "name": "enable"}, {"help": "Disable a high priority of ADVPN shortcut for this service.", "label": "Disable", "name": "disable"}, {"help": "Auto enable a high priority of ADVPN shortcut for this service if ADVPN2.0 enabled.", "label": "Auto", "name": "auto"}],
        },
        "role": {
            "type": "option",
            "help": "Service role to work with neighbor.",
            "default": "standalone",
            "options": [{"help": "Standalone service.", "label": "Standalone", "name": "standalone"}, {"help": "Primary service for primary neighbor.", "label": "Primary", "name": "primary"}, {"help": "Secondary service for secondary neighbor.", "label": "Secondary", "name": "secondary"}],
        },
        "standalone-action": {
            "type": "option",
            "help": "Enable/disable service when selected neighbor role is standalone while service role is not standalone.",
            "default": "disable",
            "options": [{"help": "Enable service when selected neighbor role is standalone.", "label": "Enable", "name": "enable"}, {"help": "Disable service when selected neighbor role is standalone.", "label": "Disable", "name": "disable"}],
        },
        "quality-link": {
            "type": "integer",
            "help": "Quality grade.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "tos": {
            "type": "user",
            "help": "Type of service bit pattern.",
            "default": "",
        },
        "tos-mask": {
            "type": "user",
            "help": "Type of service evaluated bits.",
            "default": "",
        },
        "protocol": {
            "type": "integer",
            "help": "Protocol number.",
            "default": 0,
            "min_value": 0,
            "max_value": 255,
        },
        "start-port": {
            "type": "integer",
            "help": "Start destination port number.",
            "default": 1,
            "min_value": 0,
            "max_value": 65535,
        },
        "end-port": {
            "type": "integer",
            "help": "End destination port number.",
            "default": 65535,
            "min_value": 0,
            "max_value": 65535,
        },
        "start-src-port": {
            "type": "integer",
            "help": "Start source port number.",
            "default": 1,
            "min_value": 0,
            "max_value": 65535,
        },
        "end-src-port": {
            "type": "integer",
            "help": "End source port number.",
            "default": 65535,
            "min_value": 0,
            "max_value": 65535,
        },
        "dst": {
            "type": "string",
            "help": "Destination address name.",
        },
        "dst-negate": {
            "type": "option",
            "help": "Enable/disable negation of destination address match.",
            "default": "disable",
            "options": [{"help": "Enable destination address negation.", "label": "Enable", "name": "enable"}, {"help": "Disable destination address negation.", "label": "Disable", "name": "disable"}],
        },
        "src": {
            "type": "string",
            "help": "Source address name.",
        },
        "dst6": {
            "type": "string",
            "help": "Destination address6 name.",
        },
        "src6": {
            "type": "string",
            "help": "Source address6 name.",
        },
        "src-negate": {
            "type": "option",
            "help": "Enable/disable negation of source address match.",
            "default": "disable",
            "options": [{"help": "Enable source address negation.", "label": "Enable", "name": "enable"}, {"help": "Disable source address negation.", "label": "Disable", "name": "disable"}],
        },
        "users": {
            "type": "string",
            "help": "User name.",
        },
        "groups": {
            "type": "string",
            "help": "User groups.",
        },
        "internet-service": {
            "type": "option",
            "help": "Enable/disable use of Internet service for application-based load balancing.",
            "default": "disable",
            "options": [{"help": "Enable cloud service to support application-based load balancing.", "label": "Enable", "name": "enable"}, {"help": "Disable cloud service to support application-based load balancing.", "label": "Disable", "name": "disable"}],
        },
        "internet-service-custom": {
            "type": "string",
            "help": "Custom Internet service name list.",
        },
        "internet-service-custom-group": {
            "type": "string",
            "help": "Custom Internet Service group list.",
        },
        "internet-service-fortiguard": {
            "type": "string",
            "help": "FortiGuard Internet service name list.",
        },
        "internet-service-name": {
            "type": "string",
            "help": "Internet service name list.",
        },
        "internet-service-group": {
            "type": "string",
            "help": "Internet Service group list.",
        },
        "internet-service-app-ctrl": {
            "type": "string",
            "help": "Application control based Internet Service ID list.",
        },
        "internet-service-app-ctrl-group": {
            "type": "string",
            "help": "Application control based Internet Service group list.",
        },
        "internet-service-app-ctrl-category": {
            "type": "string",
            "help": "IDs of one or more application control categories.",
        },
        "health-check": {
            "type": "string",
            "help": "Health check list.",
        },
        "link-cost-factor": {
            "type": "option",
            "help": "Link cost factor.",
            "default": "latency",
            "options": [{"help": "Select link based on latency.", "label": "Latency", "name": "latency"}, {"help": "Select link based on jitter.", "label": "Jitter", "name": "jitter"}, {"help": "Select link based on packet loss.", "label": "Packet Loss", "name": "packet-loss"}, {"help": "Select link based on available bandwidth of incoming traffic.", "label": "Inbandwidth", "name": "inbandwidth"}, {"help": "Select link based on available bandwidth of outgoing traffic.", "label": "Outbandwidth", "name": "outbandwidth"}, {"help": "Select link based on available bandwidth of bidirectional traffic.", "label": "Bibandwidth", "name": "bibandwidth"}, {"help": "Select link based on customized profile.", "label": "Custom Profile 1", "name": "custom-profile-1"}],
        },
        "packet-loss-weight": {
            "type": "integer",
            "help": "Coefficient of packet-loss in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "latency-weight": {
            "type": "integer",
            "help": "Coefficient of latency in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "jitter-weight": {
            "type": "integer",
            "help": "Coefficient of jitter in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "bandwidth-weight": {
            "type": "integer",
            "help": "Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "link-cost-threshold": {
            "type": "integer",
            "help": "Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).",
            "default": 10,
            "min_value": 0,
            "max_value": 10000000,
        },
        "hold-down-time": {
            "type": "integer",
            "help": "Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 10000000,
        },
        "sla-stickiness": {
            "type": "option",
            "help": "Enable/disable SLA stickiness (default = disable).",
            "default": "disable",
            "options": [{"help": "Traffic remains in the original session path if the path is within the SLA.", "label": "Enable", "name": "enable"}, {"help": "Traffic switches to the best path regardless of the SLA.", "label": "Disable", "name": "disable"}],
        },
        "dscp-forward": {
            "type": "option",
            "help": "Enable/disable forward traffic DSCP tag.",
            "default": "disable",
            "options": [{"help": "Enable use of forward DSCP tag.", "label": "Enable", "name": "enable"}, {"help": "Disable use of forward DSCP tag.", "label": "Disable", "name": "disable"}],
        },
        "dscp-reverse": {
            "type": "option",
            "help": "Enable/disable reverse traffic DSCP tag.",
            "default": "disable",
            "options": [{"help": "Enable use of reverse DSCP tag.", "label": "Enable", "name": "enable"}, {"help": "Disable use of reverse DSCP tag.", "label": "Disable", "name": "disable"}],
        },
        "dscp-forward-tag": {
            "type": "user",
            "help": "Forward traffic DSCP tag.",
            "default": "",
        },
        "dscp-reverse-tag": {
            "type": "user",
            "help": "Reverse traffic DSCP tag.",
            "default": "",
        },
        "sla": {
            "type": "string",
            "help": "Service level agreement (SLA).",
        },
        "priority-members": {
            "type": "string",
            "help": "Member sequence number list.",
        },
        "priority-zone": {
            "type": "string",
            "help": "Priority zone name list.",
        },
        "status": {
            "type": "option",
            "help": "Enable/disable SD-WAN service.",
            "default": "enable",
            "options": [{"help": "Enable SD-WAN service.", "label": "Enable", "name": "enable"}, {"help": "Disable SD-WAN service.", "label": "Disable", "name": "disable"}],
        },
        "gateway": {
            "type": "option",
            "help": "Enable/disable SD-WAN service gateway.",
            "default": "disable",
            "options": [{"help": "Enable SD-WAN service gateway.", "label": "Enable", "name": "enable"}, {"help": "Disable SD-WAN service gateway.", "label": "Disable", "name": "disable"}],
        },
        "default": {
            "type": "option",
            "help": "Enable/disable use of SD-WAN as default service.",
            "default": "disable",
            "options": [{"help": "Enable use of SD-WAN as default service.", "label": "Enable", "name": "enable"}, {"help": "Disable use of SD-WAN as default service.", "label": "Disable", "name": "disable"}],
        },
        "sla-compare-method": {
            "type": "option",
            "help": "Method to compare SLA value for SLA mode.",
            "default": "order",
            "options": [{"help": "Compare SLA value based on the order of health-check.", "label": "Order", "name": "order"}, {"help": "Compare SLA value based on the number of satisfied health-check.  Limits health-checks to only configured member interfaces.", "label": "Number", "name": "number"}],
        },
        "fib-best-match-force": {
            "type": "option",
            "help": "Enable/disable force using fib-best-match oif as outgoing interface.",
            "default": "disable",
            "options": [{"help": "Do not force using fib-best-match oif as outgoing interface.", "label": "Disable", "name": "disable"}, {"help": "Force using fib-best-match oif as outgoing interface.", "label": "Enable", "name": "enable"}],
        },
        "tie-break": {
            "type": "option",
            "help": "Method of selecting member if more than one meets the SLA.",
            "default": "zone",
            "options": [{"help": "Use the setting that is configured for the members\u0027 zone.", "label": "Zone", "name": "zone"}, {"help": "Members that meet the SLA are selected in the order they are configured.", "label": "Cfg Order", "name": "cfg-order"}, {"help": "Members that meet the SLA are selected that match the longest prefix in the routing table.", "label": "Fib Best Match", "name": "fib-best-match"}, {"help": "Select the best members that meet the SLA based on link-cost-factor.", "label": "Priority", "name": "priority"}, {"help": "Members that meet the SLA are selected by matching the input device.", "label": "Input Device", "name": "input-device"}],
        },
        "use-shortcut-sla": {
            "type": "option",
            "help": "Enable/disable use of ADVPN shortcut for quality comparison.",
            "default": "enable",
            "options": [{"help": "Enable use of ADVPN shortcut for quality comparison.", "label": "Enable", "name": "enable"}, {"help": "Disable use of ADVPN shortcut for quality comparison.", "label": "Disable", "name": "disable"}],
        },
        "passive-measurement": {
            "type": "option",
            "help": "Enable/disable passive measurement based on the service criteria.",
            "default": "disable",
            "options": [{"help": "Enable passive measurement of user traffic.", "label": "Enable", "name": "enable"}, {"help": "Disable passive measurement of user traffic.", "label": "Disable", "name": "disable"}],
        },
        "agent-exclusive": {
            "type": "option",
            "help": "Set/unset the service as agent use exclusively.",
            "default": "disable",
            "options": [{"help": "Set the service as agent use exclusively.", "label": "Enable", "name": "enable"}, {"help": "Unset the service as agent use exclusively.", "label": "Disable", "name": "disable"}],
        },
        "shortcut": {
            "type": "option",
            "help": "Enable/disable shortcut for this service.",
            "default": "enable",
            "options": [{"help": "Enable use of ADVPN shortcut for this service.", "label": "Enable", "name": "enable"}, {"help": "Disable use of ADVPN shortcut for this service.", "label": "Disable", "name": "disable"}],
        },
        "comment": {
            "type": "var-string",
            "help": "Comments.",
            "max_length": 255,
        },
    },
    "neighbor": {
        "ip": {
            "type": "string",
            "help": "IP/IPv6 address of neighbor or neighbor-group name.",
            "required": True,
            "default": "",
            "max_length": 45,
        },
        "member": {
            "type": "string",
            "help": "Member sequence number list.",
        },
        "service-id": {
            "type": "integer",
            "help": "SD-WAN service ID to work with the neighbor.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "minimum-sla-meet-members": {
            "type": "integer",
            "help": "Minimum number of members which meet SLA when the neighbor is preferred.",
            "default": 1,
            "min_value": 1,
            "max_value": 255,
        },
        "mode": {
            "type": "option",
            "help": "What metric to select the neighbor.",
            "default": "sla",
            "options": [{"help": "Select neighbor based on SLA link quality.", "label": "Sla", "name": "sla"}, {"help": "Select neighbor based on the speedtest status.", "label": "Speedtest", "name": "speedtest"}],
        },
        "role": {
            "type": "option",
            "help": "Role of neighbor.",
            "default": "standalone",
            "options": [{"help": "Standalone neighbor.", "label": "Standalone", "name": "standalone"}, {"help": "Primary neighbor.", "label": "Primary", "name": "primary"}, {"help": "Secondary neighbor.", "label": "Secondary", "name": "secondary"}],
        },
        "route-metric": {
            "type": "option",
            "help": "Route-metric of neighbor.",
            "default": "preferable",
            "options": [{"help": "Select neighbor based on its hc to match bgp preferable/unpreferable route_map.", "label": "Preferable", "name": "preferable"}, {"help": "Select neighbor based on its members\u0027 priority-in-sla/priority-out-sla value.", "label": "Priority", "name": "priority"}],
        },
        "health-check": {
            "type": "string",
            "help": "SD-WAN health-check name.",
            "default": "",
            "max_length": 35,
        },
        "sla-id": {
            "type": "integer",
            "help": "SLA ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "duplication": {
        "id": {
            "type": "integer",
            "help": "Duplication rule ID (1 - 255).",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 255,
        },
        "service-id": {
            "type": "string",
            "help": "SD-WAN service rule ID list.",
        },
        "srcaddr": {
            "type": "string",
            "help": "Source address or address group names.",
        },
        "dstaddr": {
            "type": "string",
            "help": "Destination address or address group names.",
        },
        "srcaddr6": {
            "type": "string",
            "help": "Source address6 or address6 group names.",
        },
        "dstaddr6": {
            "type": "string",
            "help": "Destination address6 or address6 group names.",
        },
        "srcintf": {
            "type": "string",
            "help": "Incoming (ingress) interfaces or zones.",
        },
        "dstintf": {
            "type": "string",
            "help": "Outgoing (egress) interfaces or zones.",
        },
        "service": {
            "type": "string",
            "help": "Service and service group name.",
        },
        "packet-duplication": {
            "type": "option",
            "help": "Configure packet duplication method.",
            "default": "disable",
            "options": [{"help": "Disable packet duplication.", "label": "Disable", "name": "disable"}, {"help": "Duplicate packets across all interface members of the SD-WAN zone.", "label": "Force", "name": "force"}, {"help": "Duplicate packets across all interface members of the SD-WAN zone based on the link quality.", "label": "On Demand", "name": "on-demand"}],
        },
        "sla-match-service": {
            "type": "option",
            "help": "Enable/disable packet duplication matching health-check SLAs in service rule.",
            "default": "disable",
            "options": [{"help": "Enable packet duplication matching health-check SLAs in service rule (matching all SLAs of current defined service).", "label": "Enable", "name": "enable"}, {"help": "Disable packet duplication matching health-check SLAs in service rule (matching all SLAs of all defined health-check).", "label": "Disable", "name": "disable"}],
        },
        "packet-de-duplication": {
            "type": "option",
            "help": "Enable/disable discarding of packets that have been duplicated.",
            "default": "disable",
            "options": [{"help": "Enable discarding of packets that have been duplicated.", "label": "Enable", "name": "enable"}, {"help": "Disable discarding of packets that have been duplicated.", "label": "Disable", "name": "disable"}],
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_STATUS = [
    "disable",  # Disable SD-WAN.
    "enable",  # Enable SD-WAN.
]
VALID_BODY_LOAD_BALANCE_MODE = [
    "source-ip-based",  # Source IP load balancing. All traffic from a source IP is sent to the same interface.
    "weight-based",  # Weight-based load balancing. Interfaces with higher weights have higher priority and get more traffic.
    "usage-based",  # Usage-based load balancing. All traffic is sent to the first interface on the list. When the bandwidth on that interface exceeds the spill-over limit new traffic is sent to the next interface.
    "source-dest-ip-based",  # Source and destination IP load balancing. All traffic from a source IP to a destination IP is sent to the same interface.
    "measured-volume-based",  # Volume-based load balancing. Traffic is load balanced based on traffic volume (in bytes). More traffic is sent to interfaces with higher volume ratios.
]
VALID_BODY_SPEEDTEST_BYPASS_ROUTING = [
    "disable",  # Disable SD-WAN.
    "enable",  # Enable SD-WAN.
]
VALID_BODY_NEIGHBOR_HOLD_DOWN = [
    "enable",  # Enable hold switching from the secondary neighbor to the primary neighbor.
    "disable",  # Disable hold switching from the secondary neighbor to the primary neighbor.
]
VALID_BODY_FAIL_DETECT = [
    "enable",  # Enable status checking.
    "disable",  # Disable status checking.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_sdwan_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for system/sdwan."""
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
    """Validate required fields for system/sdwan."""
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


def validate_system_sdwan_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new system/sdwan object."""
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
    if "load-balance-mode" in payload:
        value = payload["load-balance-mode"]
        if value not in VALID_BODY_LOAD_BALANCE_MODE:
            desc = FIELD_DESCRIPTIONS.get("load-balance-mode", "")
            error_msg = f"Invalid value for 'load-balance-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOAD_BALANCE_MODE)}"
            error_msg += f"\n  → Example: load-balance-mode='{{ VALID_BODY_LOAD_BALANCE_MODE[0] }}'"
            return (False, error_msg)
    if "speedtest-bypass-routing" in payload:
        value = payload["speedtest-bypass-routing"]
        if value not in VALID_BODY_SPEEDTEST_BYPASS_ROUTING:
            desc = FIELD_DESCRIPTIONS.get("speedtest-bypass-routing", "")
            error_msg = f"Invalid value for 'speedtest-bypass-routing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPEEDTEST_BYPASS_ROUTING)}"
            error_msg += f"\n  → Example: speedtest-bypass-routing='{{ VALID_BODY_SPEEDTEST_BYPASS_ROUTING[0] }}'"
            return (False, error_msg)
    if "neighbor-hold-down" in payload:
        value = payload["neighbor-hold-down"]
        if value not in VALID_BODY_NEIGHBOR_HOLD_DOWN:
            desc = FIELD_DESCRIPTIONS.get("neighbor-hold-down", "")
            error_msg = f"Invalid value for 'neighbor-hold-down': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NEIGHBOR_HOLD_DOWN)}"
            error_msg += f"\n  → Example: neighbor-hold-down='{{ VALID_BODY_NEIGHBOR_HOLD_DOWN[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_sdwan_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update system/sdwan."""
    # Step 1: Validate enum values
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "load-balance-mode" in payload:
        value = payload["load-balance-mode"]
        if value not in VALID_BODY_LOAD_BALANCE_MODE:
            return (
                False,
                f"Invalid value for 'load-balance-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_LOAD_BALANCE_MODE)}",
            )
    if "speedtest-bypass-routing" in payload:
        value = payload["speedtest-bypass-routing"]
        if value not in VALID_BODY_SPEEDTEST_BYPASS_ROUTING:
            return (
                False,
                f"Invalid value for 'speedtest-bypass-routing'='{value}'. Must be one of: {', '.join(VALID_BODY_SPEEDTEST_BYPASS_ROUTING)}",
            )
    if "neighbor-hold-down" in payload:
        value = payload["neighbor-hold-down"]
        if value not in VALID_BODY_NEIGHBOR_HOLD_DOWN:
            return (
                False,
                f"Invalid value for 'neighbor-hold-down'='{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_HOLD_DOWN)}",
            )
    if "fail-detect" in payload:
        value = payload["fail-detect"]
        if value not in VALID_BODY_FAIL_DETECT:
            return (
                False,
                f"Invalid value for 'fail-detect'='{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT)}",
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
    "endpoint": "system/sdwan",
    "category": "cmdb",
    "api_path": "system/sdwan",
    "help": "Configure redundant Internet connections with multiple outbound links and health-check profiles.",
    "total_fields": 17,
    "required_fields_count": 0,
    "fields_with_defaults_count": 10,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
