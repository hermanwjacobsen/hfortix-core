"""
Validation helpers for system/ha endpoint.

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
    "ipsec-phase2-proposal",  # IPsec phase2 proposal.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "group-id": 0,
    "group-name": "",
    "mode": "standalone",
    "sync-packet-balance": "disable",
    "hbdev": "",
    "unicast-hb": "disable",
    "unicast-hb-peerip": "0.0.0.0",
    "unicast-hb-netmask": "0.0.0.0",
    "session-sync-dev": "",
    "route-ttl": 10,
    "route-wait": 0,
    "route-hold": 10,
    "multicast-ttl": 600,
    "evpn-ttl": 60,
    "load-balance-all": "disable",
    "sync-config": "enable",
    "encryption": "disable",
    "authentication": "disable",
    "hb-interval": 2,
    "hb-interval-in-milliseconds": "100ms",
    "hb-lost-threshold": 20,
    "hello-holddown": 20,
    "gratuitous-arps": "enable",
    "arps": 5,
    "arps-interval": 8,
    "session-pickup": "disable",
    "session-pickup-connectionless": "disable",
    "session-pickup-expectation": "disable",
    "session-pickup-nat": "disable",
    "session-pickup-delay": "disable",
    "link-failed-signal": "disable",
    "upgrade-mode": "uninterruptible",
    "uninterruptible-primary-wait": 30,
    "standalone-mgmt-vdom": "disable",
    "ha-mgmt-status": "disable",
    "ha-eth-type": "8890",
    "hc-eth-type": "8891",
    "l2ep-eth-type": "8893",
    "ha-uptime-diff-margin": 300,
    "standalone-config-sync": "disable",
    "unicast-status": "disable",
    "unicast-gateway": "0.0.0.0",
    "schedule": "round-robin",
    "weight": "0 40",
    "cpu-threshold": "",
    "memory-threshold": "",
    "http-proxy-threshold": "",
    "ftp-proxy-threshold": "",
    "imap-proxy-threshold": "",
    "nntp-proxy-threshold": "",
    "pop3-proxy-threshold": "",
    "smtp-proxy-threshold": "",
    "override": "disable",
    "priority": 128,
    "override-wait-time": 0,
    "monitor": "",
    "pingserver-monitor-interface": "",
    "pingserver-failover-threshold": 0,
    "pingserver-secondary-force-reset": "enable",
    "pingserver-flip-timeout": 60,
    "vcluster-status": "disable",
    "ha-direct": "disable",
    "ssd-failover": "disable",
    "memory-compatible-mode": "disable",
    "memory-based-failover": "disable",
    "memory-failover-threshold": 0,
    "memory-failover-monitor-period": 60,
    "memory-failover-sample-rate": 1,
    "memory-failover-flip-timeout": 6,
    "failover-hold-time": 0,
    "check-secondary-dev-health": "disable",
    "ipsec-phase2-proposal": "",
    "bounce-intf-upon-failover": "disable",
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
    "group-id": "integer",  # HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2
    "group-name": "string",  # Cluster group name. Must be the same for all members.
    "mode": "option",  # HA mode. Must be the same for all members. FGSP requires sta
    "sync-packet-balance": "option",  # Enable/disable HA packet distribution to multiple CPUs.
    "password": "password",  # Cluster password. Must be the same for all members.
    "key": "password",  # Key.
    "hbdev": "user",  # Heartbeat interfaces. Must be the same for all members.
    "auto-virtual-mac-interface": "string",  # The physical interface that will be assigned an auto-generat
    "backup-hbdev": "string",  # Backup heartbeat interfaces. Must be the same for all member
    "unicast-hb": "option",  # Enable/disable unicast heartbeat.
    "unicast-hb-peerip": "ipv4-address",  # Unicast heartbeat peer IP.
    "unicast-hb-netmask": "ipv4-netmask",  # Unicast heartbeat netmask.
    "session-sync-dev": "user",  # Offload session-sync process to kernel and sync sessions usi
    "route-ttl": "integer",  # TTL for primary unit routes (5 - 3600 sec). Increase to main
    "route-wait": "integer",  # Time to wait before sending new routes to the cluster (0 - 3
    "route-hold": "integer",  # Time to wait between routing table updates to the cluster (0
    "multicast-ttl": "integer",  # HA multicast TTL on primary (5 - 3600 sec).
    "evpn-ttl": "integer",  # HA EVPN FDB TTL on primary box (5 - 3600 sec).
    "load-balance-all": "option",  # Enable to load balance TCP sessions. Disable to load balance
    "sync-config": "option",  # Enable/disable configuration synchronization.
    "encryption": "option",  # Enable/disable heartbeat message encryption.
    "authentication": "option",  # Enable/disable heartbeat message authentication.
    "hb-interval": "integer",  # Time between sending heartbeat packets (1 - 20). Increase to
    "hb-interval-in-milliseconds": "option",  # Units of heartbeat interval time between sending heartbeat p
    "hb-lost-threshold": "integer",  # Number of lost heartbeats to signal a failure (1 - 60). Incr
    "hello-holddown": "integer",  # Time to wait before changing from hello to work state (5 - 3
    "gratuitous-arps": "option",  # Enable/disable gratuitous ARPs. Disable if link-failed-signa
    "arps": "integer",  # Number of gratuitous ARPs (1 - 60). Lower to reduce traffic.
    "arps-interval": "integer",  # Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce 
    "session-pickup": "option",  # Enable/disable session pickup. Enabling it can reduce sessio
    "session-pickup-connectionless": "option",  # Enable/disable UDP and ICMP session sync.
    "session-pickup-expectation": "option",  # Enable/disable session helper expectation session sync for F
    "session-pickup-nat": "option",  # Enable/disable NAT session sync for FGSP.
    "session-pickup-delay": "option",  # Enable to sync sessions longer than 30 sec. Only longer live
    "link-failed-signal": "option",  # Enable to shut down all interfaces for 1 sec after a failove
    "upgrade-mode": "option",  # The mode to upgrade a cluster.
    "uninterruptible-primary-wait": "integer",  # Number of minutes the primary HA unit waits before the secon
    "standalone-mgmt-vdom": "option",  # Enable/disable standalone management VDOM.
    "ha-mgmt-status": "option",  # Enable to reserve interfaces to manage individual cluster un
    "ha-mgmt-interfaces": "string",  # Reserve interfaces to manage individual cluster units.
    "ha-eth-type": "string",  # HA heartbeat packet Ethertype (4-digit hex).
    "hc-eth-type": "string",  # Transparent mode HA heartbeat packet Ethertype (4-digit hex)
    "l2ep-eth-type": "string",  # Telnet session HA heartbeat packet Ethertype (4-digit hex).
    "ha-uptime-diff-margin": "integer",  # Normally you would only reduce this value for failover testi
    "standalone-config-sync": "option",  # Enable/disable FGSP configuration synchronization.
    "unicast-status": "option",  # Enable/disable unicast connection.
    "unicast-gateway": "ipv4-address",  # Default route gateway for unicast interface.
    "unicast-peers": "string",  # Number of unicast peers.
    "schedule": "option",  # Type of A-A load balancing. Use none if you have external lo
    "weight": "user",  # Weight-round-robin weight for each cluster unit. Syntax <pri
    "cpu-threshold": "user",  # Dynamic weighted load balancing CPU usage weight and high an
    "memory-threshold": "user",  # Dynamic weighted load balancing memory usage weight and high
    "http-proxy-threshold": "user",  # Dynamic weighted load balancing weight and high and low numb
    "ftp-proxy-threshold": "user",  # Dynamic weighted load balancing weight and high and low numb
    "imap-proxy-threshold": "user",  # Dynamic weighted load balancing weight and high and low numb
    "nntp-proxy-threshold": "user",  # Dynamic weighted load balancing weight and high and low numb
    "pop3-proxy-threshold": "user",  # Dynamic weighted load balancing weight and high and low numb
    "smtp-proxy-threshold": "user",  # Dynamic weighted load balancing weight and high and low numb
    "override": "option",  # Enable and increase the priority of the unit that should alw
    "priority": "integer",  # Increase the priority to select the primary unit (0 - 255).
    "override-wait-time": "integer",  # Delay negotiating if override is enabled (0 - 3600 sec). Red
    "monitor": "user",  # Interfaces to check for port monitoring (or link failure).
    "pingserver-monitor-interface": "user",  # Interfaces to check for remote IP monitoring.
    "pingserver-failover-threshold": "integer",  # Remote IP monitoring failover threshold (0 - 50).
    "pingserver-secondary-force-reset": "option",  # Enable to force the cluster to negotiate after a remote IP m
    "pingserver-flip-timeout": "integer",  # Time to wait in minutes before renegotiating after a remote 
    "vcluster-status": "option",  # Enable/disable virtual cluster for virtual clustering.
    "vcluster": "string",  # Virtual cluster table.
    "ha-direct": "option",  # Enable/disable using ha-mgmt interface for syslog, remote au
    "ssd-failover": "option",  # Enable/disable automatic HA failover on SSD disk failure.
    "memory-compatible-mode": "option",  # Enable/disable memory compatible mode.
    "memory-based-failover": "option",  # Enable/disable memory based failover.
    "memory-failover-threshold": "integer",  # Memory usage threshold to trigger memory based failover (0 m
    "memory-failover-monitor-period": "integer",  # Duration of high memory usage before memory based failover i
    "memory-failover-sample-rate": "integer",  # Rate at which memory usage is sampled in order to measure me
    "memory-failover-flip-timeout": "integer",  # Time to wait between subsequent memory based failovers in mi
    "failover-hold-time": "integer",  # Time to wait before failover (0 - 300 sec, default = 0), to 
    "check-secondary-dev-health": "option",  # Enable/disable secondary dev health check for session load-b
    "ipsec-phase2-proposal": "option",  # IPsec phase2 proposal.
    "bounce-intf-upon-failover": "option",  # Enable/disable notification of kernel to bring down and up a
    "status": "key",  # list ha status information
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "group-id": "HA group ID  (0 - 1023;  or 0 - 7 when there are more than 2 vclusters). Must be the same for all members.",
    "group-name": "Cluster group name. Must be the same for all members.",
    "mode": "HA mode. Must be the same for all members. FGSP requires standalone.",
    "sync-packet-balance": "Enable/disable HA packet distribution to multiple CPUs.",
    "password": "Cluster password. Must be the same for all members.",
    "key": "Key.",
    "hbdev": "Heartbeat interfaces. Must be the same for all members.",
    "auto-virtual-mac-interface": "The physical interface that will be assigned an auto-generated virtual MAC address.",
    "backup-hbdev": "Backup heartbeat interfaces. Must be the same for all members.",
    "unicast-hb": "Enable/disable unicast heartbeat.",
    "unicast-hb-peerip": "Unicast heartbeat peer IP.",
    "unicast-hb-netmask": "Unicast heartbeat netmask.",
    "session-sync-dev": "Offload session-sync process to kernel and sync sessions using connected interface(s) directly.",
    "route-ttl": "TTL for primary unit routes (5 - 3600 sec). Increase to maintain active routes during failover.",
    "route-wait": "Time to wait before sending new routes to the cluster (0 - 3600 sec).",
    "route-hold": "Time to wait between routing table updates to the cluster (0 - 3600 sec).",
    "multicast-ttl": "HA multicast TTL on primary (5 - 3600 sec).",
    "evpn-ttl": "HA EVPN FDB TTL on primary box (5 - 3600 sec).",
    "load-balance-all": "Enable to load balance TCP sessions. Disable to load balance proxy sessions only.",
    "sync-config": "Enable/disable configuration synchronization.",
    "encryption": "Enable/disable heartbeat message encryption.",
    "authentication": "Enable/disable heartbeat message authentication.",
    "hb-interval": "Time between sending heartbeat packets (1 - 20). Increase to reduce false positives.",
    "hb-interval-in-milliseconds": "Units of heartbeat interval time between sending heartbeat packets. Default is 100ms.",
    "hb-lost-threshold": "Number of lost heartbeats to signal a failure (1 - 60). Increase to reduce false positives.",
    "hello-holddown": "Time to wait before changing from hello to work state (5 - 300 sec).",
    "gratuitous-arps": "Enable/disable gratuitous ARPs. Disable if link-failed-signal enabled.",
    "arps": "Number of gratuitous ARPs (1 - 60). Lower to reduce traffic. Higher to reduce failover time.",
    "arps-interval": "Time between gratuitous ARPs  (1 - 20 sec). Lower to reduce failover time. Higher to reduce traffic.",
    "session-pickup": "Enable/disable session pickup. Enabling it can reduce session down time when fail over happens.",
    "session-pickup-connectionless": "Enable/disable UDP and ICMP session sync.",
    "session-pickup-expectation": "Enable/disable session helper expectation session sync for FGSP.",
    "session-pickup-nat": "Enable/disable NAT session sync for FGSP.",
    "session-pickup-delay": "Enable to sync sessions longer than 30 sec. Only longer lived sessions need to be synced.",
    "link-failed-signal": "Enable to shut down all interfaces for 1 sec after a failover. Use if gratuitous ARPs do not update network.",
    "upgrade-mode": "The mode to upgrade a cluster.",
    "uninterruptible-primary-wait": "Number of minutes the primary HA unit waits before the secondary HA unit is considered upgraded and the system is started before starting its own upgrade (15 - 300, default = 30).",
    "standalone-mgmt-vdom": "Enable/disable standalone management VDOM.",
    "ha-mgmt-status": "Enable to reserve interfaces to manage individual cluster units.",
    "ha-mgmt-interfaces": "Reserve interfaces to manage individual cluster units.",
    "ha-eth-type": "HA heartbeat packet Ethertype (4-digit hex).",
    "hc-eth-type": "Transparent mode HA heartbeat packet Ethertype (4-digit hex).",
    "l2ep-eth-type": "Telnet session HA heartbeat packet Ethertype (4-digit hex).",
    "ha-uptime-diff-margin": "Normally you would only reduce this value for failover testing.",
    "standalone-config-sync": "Enable/disable FGSP configuration synchronization.",
    "unicast-status": "Enable/disable unicast connection.",
    "unicast-gateway": "Default route gateway for unicast interface.",
    "unicast-peers": "Number of unicast peers.",
    "schedule": "Type of A-A load balancing. Use none if you have external load balancers.",
    "weight": "Weight-round-robin weight for each cluster unit. Syntax <priority> <weight>.",
    "cpu-threshold": "Dynamic weighted load balancing CPU usage weight and high and low thresholds.",
    "memory-threshold": "Dynamic weighted load balancing memory usage weight and high and low thresholds.",
    "http-proxy-threshold": "Dynamic weighted load balancing weight and high and low number of HTTP proxy sessions.",
    "ftp-proxy-threshold": "Dynamic weighted load balancing weight and high and low number of FTP proxy sessions.",
    "imap-proxy-threshold": "Dynamic weighted load balancing weight and high and low number of IMAP proxy sessions.",
    "nntp-proxy-threshold": "Dynamic weighted load balancing weight and high and low number of NNTP proxy sessions.",
    "pop3-proxy-threshold": "Dynamic weighted load balancing weight and high and low number of POP3 proxy sessions.",
    "smtp-proxy-threshold": "Dynamic weighted load balancing weight and high and low number of SMTP proxy sessions.",
    "override": "Enable and increase the priority of the unit that should always be primary (master).",
    "priority": "Increase the priority to select the primary unit (0 - 255).",
    "override-wait-time": "Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates.",
    "monitor": "Interfaces to check for port monitoring (or link failure).",
    "pingserver-monitor-interface": "Interfaces to check for remote IP monitoring.",
    "pingserver-failover-threshold": "Remote IP monitoring failover threshold (0 - 50).",
    "pingserver-secondary-force-reset": "Enable to force the cluster to negotiate after a remote IP monitoring failover.",
    "pingserver-flip-timeout": "Time to wait in minutes before renegotiating after a remote IP monitoring failover.",
    "vcluster-status": "Enable/disable virtual cluster for virtual clustering.",
    "vcluster": "Virtual cluster table.",
    "ha-direct": "Enable/disable using ha-mgmt interface for syslog, remote authentication (RADIUS), FortiAnalyzer, FortiSandbox, sFlow, and Netflow.",
    "ssd-failover": "Enable/disable automatic HA failover on SSD disk failure.",
    "memory-compatible-mode": "Enable/disable memory compatible mode.",
    "memory-based-failover": "Enable/disable memory based failover.",
    "memory-failover-threshold": "Memory usage threshold to trigger memory based failover (0 means using conserve mode threshold in system.global).",
    "memory-failover-monitor-period": "Duration of high memory usage before memory based failover is triggered in seconds (1 - 300, default = 60).",
    "memory-failover-sample-rate": "Rate at which memory usage is sampled in order to measure memory usage in seconds (1 - 60, default = 1).",
    "memory-failover-flip-timeout": "Time to wait between subsequent memory based failovers in minutes (6 - 2147483647, default = 6).",
    "failover-hold-time": "Time to wait before failover (0 - 300 sec, default = 0), to avoid flip.",
    "check-secondary-dev-health": "Enable/disable secondary dev health check for session load-balance in HA A-A mode.",
    "ipsec-phase2-proposal": "IPsec phase2 proposal.",
    "bounce-intf-upon-failover": "Enable/disable notification of kernel to bring down and up all monitored interfaces. The setting is used during failovers if gratuitous ARPs do not update the network.",
    "status": "list ha status information",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "group-id": {"type": "integer", "min": 0, "max": 1023},
    "group-name": {"type": "string", "max_length": 32},
    "route-ttl": {"type": "integer", "min": 5, "max": 3600},
    "route-wait": {"type": "integer", "min": 0, "max": 3600},
    "route-hold": {"type": "integer", "min": 0, "max": 3600},
    "multicast-ttl": {"type": "integer", "min": 5, "max": 3600},
    "evpn-ttl": {"type": "integer", "min": 5, "max": 3600},
    "hb-interval": {"type": "integer", "min": 1, "max": 20},
    "hb-lost-threshold": {"type": "integer", "min": 1, "max": 60},
    "hello-holddown": {"type": "integer", "min": 5, "max": 300},
    "arps": {"type": "integer", "min": 1, "max": 60},
    "arps-interval": {"type": "integer", "min": 1, "max": 20},
    "uninterruptible-primary-wait": {"type": "integer", "min": 15, "max": 300},
    "ha-eth-type": {"type": "string", "max_length": 4},
    "hc-eth-type": {"type": "string", "max_length": 4},
    "l2ep-eth-type": {"type": "string", "max_length": 4},
    "ha-uptime-diff-margin": {"type": "integer", "min": 1, "max": 65535},
    "priority": {"type": "integer", "min": 0, "max": 255},
    "override-wait-time": {"type": "integer", "min": 0, "max": 3600},
    "pingserver-failover-threshold": {"type": "integer", "min": 0, "max": 50},
    "pingserver-flip-timeout": {"type": "integer", "min": 6, "max": 2147483647},
    "memory-failover-threshold": {"type": "integer", "min": 0, "max": 95},
    "memory-failover-monitor-period": {"type": "integer", "min": 1, "max": 300},
    "memory-failover-sample-rate": {"type": "integer", "min": 1, "max": 60},
    "memory-failover-flip-timeout": {"type": "integer", "min": 6, "max": 2147483647},
    "failover-hold-time": {"type": "integer", "min": 0, "max": 300},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "auto-virtual-mac-interface": {
        "interface-name": {
            "type": "string",
            "help": "Interface name.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
    },
    "backup-hbdev": {
        "name": {
            "type": "string",
            "help": "Interface name.",
            "default": "",
            "max_length": 79,
        },
    },
    "ha-mgmt-interfaces": {
        "id": {
            "type": "integer",
            "help": "Table ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "interface": {
            "type": "string",
            "help": "Interface to reserve for HA management.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "dst": {
            "type": "ipv4-classnet",
            "help": "Default route destination for reserved HA management interface.",
            "default": "0.0.0.0 0.0.0.0",
        },
        "gateway": {
            "type": "ipv4-address",
            "help": "Default route gateway for reserved HA management interface.",
            "default": "0.0.0.0",
        },
        "dst6": {
            "type": "ipv6-prefix",
            "help": "Default IPv6 destination for reserved HA management interface.",
            "default": "::/0",
        },
        "gateway6": {
            "type": "ipv6-address",
            "help": "Default IPv6 gateway for reserved HA management interface.",
            "default": "::",
        },
    },
    "unicast-peers": {
        "id": {
            "type": "integer",
            "help": "Table ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "peer-ip": {
            "type": "ipv4-address",
            "help": "Unicast peer IP.",
            "default": "0.0.0.0",
        },
    },
    "vcluster": {
        "vcluster-id": {
            "type": "integer",
            "help": "ID.",
            "default": 1,
            "min_value": 1,
            "max_value": 30,
        },
        "override": {
            "type": "option",
            "help": "Enable and increase the priority of the unit that should always be primary (master).",
            "default": "disable",
            "options": ["enable", "disable"],
        },
        "priority": {
            "type": "integer",
            "help": "Increase the priority to select the primary unit (0 - 255).",
            "default": 128,
            "min_value": 0,
            "max_value": 255,
        },
        "override-wait-time": {
            "type": "integer",
            "help": "Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates.",
            "default": 0,
            "min_value": 0,
            "max_value": 3600,
        },
        "monitor": {
            "type": "user",
            "help": "Interfaces to check for port monitoring (or link failure).",
            "default": "",
        },
        "pingserver-monitor-interface": {
            "type": "user",
            "help": "Interfaces to check for remote IP monitoring.",
            "default": "",
        },
        "pingserver-failover-threshold": {
            "type": "integer",
            "help": "Remote IP monitoring failover threshold (0 - 50).",
            "default": 0,
            "min_value": 0,
            "max_value": 50,
        },
        "pingserver-secondary-force-reset": {
            "type": "option",
            "help": "Enable to force the cluster to negotiate after a remote IP monitoring failover.",
            "default": "enable",
            "options": ["enable", "disable"],
        },
        "pingserver-flip-timeout": {
            "type": "integer",
            "help": "Time to wait in minutes before renegotiating after a remote IP monitoring failover.",
            "default": 60,
            "min_value": 6,
            "max_value": 2147483647,
        },
        "vdom": {
            "type": "string",
            "help": "Virtual domain(s) in the virtual cluster.",
        },
    },
    "status": {
        "vcluster-id": {
            "type": "value",
            "help": "<enter> to show all vcluster or input vcluster-id",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_MODE = [
    "standalone",
    "a-a",
    "a-p",
]
VALID_BODY_SYNC_PACKET_BALANCE = [
    "enable",
    "disable",
]
VALID_BODY_UNICAST_HB = [
    "enable",
    "disable",
]
VALID_BODY_LOAD_BALANCE_ALL = [
    "enable",
    "disable",
]
VALID_BODY_SYNC_CONFIG = [
    "enable",
    "disable",
]
VALID_BODY_ENCRYPTION = [
    "enable",
    "disable",
]
VALID_BODY_AUTHENTICATION = [
    "enable",
    "disable",
]
VALID_BODY_HB_INTERVAL_IN_MILLISECONDS = [
    "100ms",
    "10ms",
]
VALID_BODY_GRATUITOUS_ARPS = [
    "enable",
    "disable",
]
VALID_BODY_SESSION_PICKUP = [
    "enable",
    "disable",
]
VALID_BODY_SESSION_PICKUP_CONNECTIONLESS = [
    "enable",
    "disable",
]
VALID_BODY_SESSION_PICKUP_EXPECTATION = [
    "enable",
    "disable",
]
VALID_BODY_SESSION_PICKUP_NAT = [
    "enable",
    "disable",
]
VALID_BODY_SESSION_PICKUP_DELAY = [
    "enable",
    "disable",
]
VALID_BODY_LINK_FAILED_SIGNAL = [
    "enable",
    "disable",
]
VALID_BODY_UPGRADE_MODE = [
    "simultaneous",
    "uninterruptible",
    "local-only",
    "secondary-only",
]
VALID_BODY_STANDALONE_MGMT_VDOM = [
    "enable",
    "disable",
]
VALID_BODY_HA_MGMT_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_STANDALONE_CONFIG_SYNC = [
    "enable",
    "disable",
]
VALID_BODY_UNICAST_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_SCHEDULE = [
    "none",
    "leastconnection",
    "round-robin",
    "weight-round-robin",
    "random",
    "ip",
    "ipport",
]
VALID_BODY_OVERRIDE = [
    "enable",
    "disable",
]
VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET = [
    "enable",
    "disable",
]
VALID_BODY_VCLUSTER_STATUS = [
    "enable",
    "disable",
]
VALID_BODY_HA_DIRECT = [
    "enable",
    "disable",
]
VALID_BODY_SSD_FAILOVER = [
    "enable",
    "disable",
]
VALID_BODY_MEMORY_COMPATIBLE_MODE = [
    "enable",
    "disable",
]
VALID_BODY_MEMORY_BASED_FAILOVER = [
    "enable",
    "disable",
]
VALID_BODY_CHECK_SECONDARY_DEV_HEALTH = [
    "enable",
    "disable",
]
VALID_BODY_IPSEC_PHASE2_PROPOSAL = [
    "aes128-sha1",
    "aes128-sha256",
    "aes128-sha384",
    "aes128-sha512",
    "aes192-sha1",
    "aes192-sha256",
    "aes192-sha384",
    "aes192-sha512",
    "aes256-sha1",
    "aes256-sha256",
    "aes256-sha384",
    "aes256-sha512",
    "aes128gcm",
    "aes256gcm",
    "chacha20poly1305",
]
VALID_BODY_BOUNCE_INTF_UPON_FAILOVER = [
    "enable",
    "disable",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_system_ha_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for system/ha.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_system_ha_get()
        >>> assert is_valid == True
        
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_system_ha_get(
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
    Validate required fields for system/ha.

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


def validate_system_ha_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new system/ha object.

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
        ...     "ipsec-phase2-proposal": True,  # IPsec phase2 proposal.
        ... }
        >>> is_valid, error = validate_system_ha_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "ipsec-phase2-proposal": True,
        ...     "mode": "standalone",  # Valid enum value
        ... }
        >>> is_valid, error = validate_system_ha_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["mode"] = "invalid-value"
        >>> is_valid, error = validate_system_ha_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_system_ha_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "sync-packet-balance" in payload:
        value = payload["sync-packet-balance"]
        if value not in VALID_BODY_SYNC_PACKET_BALANCE:
            desc = FIELD_DESCRIPTIONS.get("sync-packet-balance", "")
            error_msg = f"Invalid value for 'sync-packet-balance': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYNC_PACKET_BALANCE)}"
            error_msg += f"\n  → Example: sync-packet-balance='{{ VALID_BODY_SYNC_PACKET_BALANCE[0] }}'"
            return (False, error_msg)
    if "unicast-hb" in payload:
        value = payload["unicast-hb"]
        if value not in VALID_BODY_UNICAST_HB:
            desc = FIELD_DESCRIPTIONS.get("unicast-hb", "")
            error_msg = f"Invalid value for 'unicast-hb': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNICAST_HB)}"
            error_msg += f"\n  → Example: unicast-hb='{{ VALID_BODY_UNICAST_HB[0] }}'"
            return (False, error_msg)
    if "load-balance-all" in payload:
        value = payload["load-balance-all"]
        if value not in VALID_BODY_LOAD_BALANCE_ALL:
            desc = FIELD_DESCRIPTIONS.get("load-balance-all", "")
            error_msg = f"Invalid value for 'load-balance-all': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOAD_BALANCE_ALL)}"
            error_msg += f"\n  → Example: load-balance-all='{{ VALID_BODY_LOAD_BALANCE_ALL[0] }}'"
            return (False, error_msg)
    if "sync-config" in payload:
        value = payload["sync-config"]
        if value not in VALID_BODY_SYNC_CONFIG:
            desc = FIELD_DESCRIPTIONS.get("sync-config", "")
            error_msg = f"Invalid value for 'sync-config': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYNC_CONFIG)}"
            error_msg += f"\n  → Example: sync-config='{{ VALID_BODY_SYNC_CONFIG[0] }}'"
            return (False, error_msg)
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            desc = FIELD_DESCRIPTIONS.get("encryption", "")
            error_msg = f"Invalid value for 'encryption': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENCRYPTION)}"
            error_msg += f"\n  → Example: encryption='{{ VALID_BODY_ENCRYPTION[0] }}'"
            return (False, error_msg)
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            desc = FIELD_DESCRIPTIONS.get("authentication", "")
            error_msg = f"Invalid value for 'authentication': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTHENTICATION)}"
            error_msg += f"\n  → Example: authentication='{{ VALID_BODY_AUTHENTICATION[0] }}'"
            return (False, error_msg)
    if "hb-interval-in-milliseconds" in payload:
        value = payload["hb-interval-in-milliseconds"]
        if value not in VALID_BODY_HB_INTERVAL_IN_MILLISECONDS:
            desc = FIELD_DESCRIPTIONS.get("hb-interval-in-milliseconds", "")
            error_msg = f"Invalid value for 'hb-interval-in-milliseconds': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HB_INTERVAL_IN_MILLISECONDS)}"
            error_msg += f"\n  → Example: hb-interval-in-milliseconds='{{ VALID_BODY_HB_INTERVAL_IN_MILLISECONDS[0] }}'"
            return (False, error_msg)
    if "gratuitous-arps" in payload:
        value = payload["gratuitous-arps"]
        if value not in VALID_BODY_GRATUITOUS_ARPS:
            desc = FIELD_DESCRIPTIONS.get("gratuitous-arps", "")
            error_msg = f"Invalid value for 'gratuitous-arps': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GRATUITOUS_ARPS)}"
            error_msg += f"\n  → Example: gratuitous-arps='{{ VALID_BODY_GRATUITOUS_ARPS[0] }}'"
            return (False, error_msg)
    if "session-pickup" in payload:
        value = payload["session-pickup"]
        if value not in VALID_BODY_SESSION_PICKUP:
            desc = FIELD_DESCRIPTIONS.get("session-pickup", "")
            error_msg = f"Invalid value for 'session-pickup': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_PICKUP)}"
            error_msg += f"\n  → Example: session-pickup='{{ VALID_BODY_SESSION_PICKUP[0] }}'"
            return (False, error_msg)
    if "session-pickup-connectionless" in payload:
        value = payload["session-pickup-connectionless"]
        if value not in VALID_BODY_SESSION_PICKUP_CONNECTIONLESS:
            desc = FIELD_DESCRIPTIONS.get("session-pickup-connectionless", "")
            error_msg = f"Invalid value for 'session-pickup-connectionless': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_PICKUP_CONNECTIONLESS)}"
            error_msg += f"\n  → Example: session-pickup-connectionless='{{ VALID_BODY_SESSION_PICKUP_CONNECTIONLESS[0] }}'"
            return (False, error_msg)
    if "session-pickup-expectation" in payload:
        value = payload["session-pickup-expectation"]
        if value not in VALID_BODY_SESSION_PICKUP_EXPECTATION:
            desc = FIELD_DESCRIPTIONS.get("session-pickup-expectation", "")
            error_msg = f"Invalid value for 'session-pickup-expectation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_PICKUP_EXPECTATION)}"
            error_msg += f"\n  → Example: session-pickup-expectation='{{ VALID_BODY_SESSION_PICKUP_EXPECTATION[0] }}'"
            return (False, error_msg)
    if "session-pickup-nat" in payload:
        value = payload["session-pickup-nat"]
        if value not in VALID_BODY_SESSION_PICKUP_NAT:
            desc = FIELD_DESCRIPTIONS.get("session-pickup-nat", "")
            error_msg = f"Invalid value for 'session-pickup-nat': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_PICKUP_NAT)}"
            error_msg += f"\n  → Example: session-pickup-nat='{{ VALID_BODY_SESSION_PICKUP_NAT[0] }}'"
            return (False, error_msg)
    if "session-pickup-delay" in payload:
        value = payload["session-pickup-delay"]
        if value not in VALID_BODY_SESSION_PICKUP_DELAY:
            desc = FIELD_DESCRIPTIONS.get("session-pickup-delay", "")
            error_msg = f"Invalid value for 'session-pickup-delay': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_PICKUP_DELAY)}"
            error_msg += f"\n  → Example: session-pickup-delay='{{ VALID_BODY_SESSION_PICKUP_DELAY[0] }}'"
            return (False, error_msg)
    if "link-failed-signal" in payload:
        value = payload["link-failed-signal"]
        if value not in VALID_BODY_LINK_FAILED_SIGNAL:
            desc = FIELD_DESCRIPTIONS.get("link-failed-signal", "")
            error_msg = f"Invalid value for 'link-failed-signal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LINK_FAILED_SIGNAL)}"
            error_msg += f"\n  → Example: link-failed-signal='{{ VALID_BODY_LINK_FAILED_SIGNAL[0] }}'"
            return (False, error_msg)
    if "upgrade-mode" in payload:
        value = payload["upgrade-mode"]
        if value not in VALID_BODY_UPGRADE_MODE:
            desc = FIELD_DESCRIPTIONS.get("upgrade-mode", "")
            error_msg = f"Invalid value for 'upgrade-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UPGRADE_MODE)}"
            error_msg += f"\n  → Example: upgrade-mode='{{ VALID_BODY_UPGRADE_MODE[0] }}'"
            return (False, error_msg)
    if "standalone-mgmt-vdom" in payload:
        value = payload["standalone-mgmt-vdom"]
        if value not in VALID_BODY_STANDALONE_MGMT_VDOM:
            desc = FIELD_DESCRIPTIONS.get("standalone-mgmt-vdom", "")
            error_msg = f"Invalid value for 'standalone-mgmt-vdom': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STANDALONE_MGMT_VDOM)}"
            error_msg += f"\n  → Example: standalone-mgmt-vdom='{{ VALID_BODY_STANDALONE_MGMT_VDOM[0] }}'"
            return (False, error_msg)
    if "ha-mgmt-status" in payload:
        value = payload["ha-mgmt-status"]
        if value not in VALID_BODY_HA_MGMT_STATUS:
            desc = FIELD_DESCRIPTIONS.get("ha-mgmt-status", "")
            error_msg = f"Invalid value for 'ha-mgmt-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_MGMT_STATUS)}"
            error_msg += f"\n  → Example: ha-mgmt-status='{{ VALID_BODY_HA_MGMT_STATUS[0] }}'"
            return (False, error_msg)
    if "standalone-config-sync" in payload:
        value = payload["standalone-config-sync"]
        if value not in VALID_BODY_STANDALONE_CONFIG_SYNC:
            desc = FIELD_DESCRIPTIONS.get("standalone-config-sync", "")
            error_msg = f"Invalid value for 'standalone-config-sync': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_STANDALONE_CONFIG_SYNC)}"
            error_msg += f"\n  → Example: standalone-config-sync='{{ VALID_BODY_STANDALONE_CONFIG_SYNC[0] }}'"
            return (False, error_msg)
    if "unicast-status" in payload:
        value = payload["unicast-status"]
        if value not in VALID_BODY_UNICAST_STATUS:
            desc = FIELD_DESCRIPTIONS.get("unicast-status", "")
            error_msg = f"Invalid value for 'unicast-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNICAST_STATUS)}"
            error_msg += f"\n  → Example: unicast-status='{{ VALID_BODY_UNICAST_STATUS[0] }}'"
            return (False, error_msg)
    if "schedule" in payload:
        value = payload["schedule"]
        if value not in VALID_BODY_SCHEDULE:
            desc = FIELD_DESCRIPTIONS.get("schedule", "")
            error_msg = f"Invalid value for 'schedule': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCHEDULE)}"
            error_msg += f"\n  → Example: schedule='{{ VALID_BODY_SCHEDULE[0] }}'"
            return (False, error_msg)
    if "override" in payload:
        value = payload["override"]
        if value not in VALID_BODY_OVERRIDE:
            desc = FIELD_DESCRIPTIONS.get("override", "")
            error_msg = f"Invalid value for 'override': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERRIDE)}"
            error_msg += f"\n  → Example: override='{{ VALID_BODY_OVERRIDE[0] }}'"
            return (False, error_msg)
    if "pingserver-secondary-force-reset" in payload:
        value = payload["pingserver-secondary-force-reset"]
        if value not in VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET:
            desc = FIELD_DESCRIPTIONS.get("pingserver-secondary-force-reset", "")
            error_msg = f"Invalid value for 'pingserver-secondary-force-reset': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET)}"
            error_msg += f"\n  → Example: pingserver-secondary-force-reset='{{ VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET[0] }}'"
            return (False, error_msg)
    if "vcluster-status" in payload:
        value = payload["vcluster-status"]
        if value not in VALID_BODY_VCLUSTER_STATUS:
            desc = FIELD_DESCRIPTIONS.get("vcluster-status", "")
            error_msg = f"Invalid value for 'vcluster-status': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VCLUSTER_STATUS)}"
            error_msg += f"\n  → Example: vcluster-status='{{ VALID_BODY_VCLUSTER_STATUS[0] }}'"
            return (False, error_msg)
    if "ha-direct" in payload:
        value = payload["ha-direct"]
        if value not in VALID_BODY_HA_DIRECT:
            desc = FIELD_DESCRIPTIONS.get("ha-direct", "")
            error_msg = f"Invalid value for 'ha-direct': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HA_DIRECT)}"
            error_msg += f"\n  → Example: ha-direct='{{ VALID_BODY_HA_DIRECT[0] }}'"
            return (False, error_msg)
    if "ssd-failover" in payload:
        value = payload["ssd-failover"]
        if value not in VALID_BODY_SSD_FAILOVER:
            desc = FIELD_DESCRIPTIONS.get("ssd-failover", "")
            error_msg = f"Invalid value for 'ssd-failover': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SSD_FAILOVER)}"
            error_msg += f"\n  → Example: ssd-failover='{{ VALID_BODY_SSD_FAILOVER[0] }}'"
            return (False, error_msg)
    if "memory-compatible-mode" in payload:
        value = payload["memory-compatible-mode"]
        if value not in VALID_BODY_MEMORY_COMPATIBLE_MODE:
            desc = FIELD_DESCRIPTIONS.get("memory-compatible-mode", "")
            error_msg = f"Invalid value for 'memory-compatible-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MEMORY_COMPATIBLE_MODE)}"
            error_msg += f"\n  → Example: memory-compatible-mode='{{ VALID_BODY_MEMORY_COMPATIBLE_MODE[0] }}'"
            return (False, error_msg)
    if "memory-based-failover" in payload:
        value = payload["memory-based-failover"]
        if value not in VALID_BODY_MEMORY_BASED_FAILOVER:
            desc = FIELD_DESCRIPTIONS.get("memory-based-failover", "")
            error_msg = f"Invalid value for 'memory-based-failover': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MEMORY_BASED_FAILOVER)}"
            error_msg += f"\n  → Example: memory-based-failover='{{ VALID_BODY_MEMORY_BASED_FAILOVER[0] }}'"
            return (False, error_msg)
    if "check-secondary-dev-health" in payload:
        value = payload["check-secondary-dev-health"]
        if value not in VALID_BODY_CHECK_SECONDARY_DEV_HEALTH:
            desc = FIELD_DESCRIPTIONS.get("check-secondary-dev-health", "")
            error_msg = f"Invalid value for 'check-secondary-dev-health': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHECK_SECONDARY_DEV_HEALTH)}"
            error_msg += f"\n  → Example: check-secondary-dev-health='{{ VALID_BODY_CHECK_SECONDARY_DEV_HEALTH[0] }}'"
            return (False, error_msg)
    if "ipsec-phase2-proposal" in payload:
        value = payload["ipsec-phase2-proposal"]
        if value not in VALID_BODY_IPSEC_PHASE2_PROPOSAL:
            desc = FIELD_DESCRIPTIONS.get("ipsec-phase2-proposal", "")
            error_msg = f"Invalid value for 'ipsec-phase2-proposal': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IPSEC_PHASE2_PROPOSAL)}"
            error_msg += f"\n  → Example: ipsec-phase2-proposal='{{ VALID_BODY_IPSEC_PHASE2_PROPOSAL[0] }}'"
            return (False, error_msg)
    if "bounce-intf-upon-failover" in payload:
        value = payload["bounce-intf-upon-failover"]
        if value not in VALID_BODY_BOUNCE_INTF_UPON_FAILOVER:
            desc = FIELD_DESCRIPTIONS.get("bounce-intf-upon-failover", "")
            error_msg = f"Invalid value for 'bounce-intf-upon-failover': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BOUNCE_INTF_UPON_FAILOVER)}"
            error_msg += f"\n  → Example: bounce-intf-upon-failover='{{ VALID_BODY_BOUNCE_INTF_UPON_FAILOVER[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_system_ha_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update system/ha.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_system_ha_put(payload)
    """
    # Step 1: Validate enum values
    if "mode" in payload:
        value = payload["mode"]
        if value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid value for 'mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )
    if "sync-packet-balance" in payload:
        value = payload["sync-packet-balance"]
        if value not in VALID_BODY_SYNC_PACKET_BALANCE:
            return (
                False,
                f"Invalid value for 'sync-packet-balance'='{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_PACKET_BALANCE)}",
            )
    if "unicast-hb" in payload:
        value = payload["unicast-hb"]
        if value not in VALID_BODY_UNICAST_HB:
            return (
                False,
                f"Invalid value for 'unicast-hb'='{value}'. Must be one of: {', '.join(VALID_BODY_UNICAST_HB)}",
            )
    if "load-balance-all" in payload:
        value = payload["load-balance-all"]
        if value not in VALID_BODY_LOAD_BALANCE_ALL:
            return (
                False,
                f"Invalid value for 'load-balance-all'='{value}'. Must be one of: {', '.join(VALID_BODY_LOAD_BALANCE_ALL)}",
            )
    if "sync-config" in payload:
        value = payload["sync-config"]
        if value not in VALID_BODY_SYNC_CONFIG:
            return (
                False,
                f"Invalid value for 'sync-config'='{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_CONFIG)}",
            )
    if "encryption" in payload:
        value = payload["encryption"]
        if value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid value for 'encryption'='{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )
    if "authentication" in payload:
        value = payload["authentication"]
        if value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid value for 'authentication'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )
    if "hb-interval-in-milliseconds" in payload:
        value = payload["hb-interval-in-milliseconds"]
        if value not in VALID_BODY_HB_INTERVAL_IN_MILLISECONDS:
            return (
                False,
                f"Invalid value for 'hb-interval-in-milliseconds'='{value}'. Must be one of: {', '.join(VALID_BODY_HB_INTERVAL_IN_MILLISECONDS)}",
            )
    if "gratuitous-arps" in payload:
        value = payload["gratuitous-arps"]
        if value not in VALID_BODY_GRATUITOUS_ARPS:
            return (
                False,
                f"Invalid value for 'gratuitous-arps'='{value}'. Must be one of: {', '.join(VALID_BODY_GRATUITOUS_ARPS)}",
            )
    if "session-pickup" in payload:
        value = payload["session-pickup"]
        if value not in VALID_BODY_SESSION_PICKUP:
            return (
                False,
                f"Invalid value for 'session-pickup'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP)}",
            )
    if "session-pickup-connectionless" in payload:
        value = payload["session-pickup-connectionless"]
        if value not in VALID_BODY_SESSION_PICKUP_CONNECTIONLESS:
            return (
                False,
                f"Invalid value for 'session-pickup-connectionless'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_CONNECTIONLESS)}",
            )
    if "session-pickup-expectation" in payload:
        value = payload["session-pickup-expectation"]
        if value not in VALID_BODY_SESSION_PICKUP_EXPECTATION:
            return (
                False,
                f"Invalid value for 'session-pickup-expectation'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_EXPECTATION)}",
            )
    if "session-pickup-nat" in payload:
        value = payload["session-pickup-nat"]
        if value not in VALID_BODY_SESSION_PICKUP_NAT:
            return (
                False,
                f"Invalid value for 'session-pickup-nat'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_NAT)}",
            )
    if "session-pickup-delay" in payload:
        value = payload["session-pickup-delay"]
        if value not in VALID_BODY_SESSION_PICKUP_DELAY:
            return (
                False,
                f"Invalid value for 'session-pickup-delay'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_PICKUP_DELAY)}",
            )
    if "link-failed-signal" in payload:
        value = payload["link-failed-signal"]
        if value not in VALID_BODY_LINK_FAILED_SIGNAL:
            return (
                False,
                f"Invalid value for 'link-failed-signal'='{value}'. Must be one of: {', '.join(VALID_BODY_LINK_FAILED_SIGNAL)}",
            )
    if "upgrade-mode" in payload:
        value = payload["upgrade-mode"]
        if value not in VALID_BODY_UPGRADE_MODE:
            return (
                False,
                f"Invalid value for 'upgrade-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_UPGRADE_MODE)}",
            )
    if "standalone-mgmt-vdom" in payload:
        value = payload["standalone-mgmt-vdom"]
        if value not in VALID_BODY_STANDALONE_MGMT_VDOM:
            return (
                False,
                f"Invalid value for 'standalone-mgmt-vdom'='{value}'. Must be one of: {', '.join(VALID_BODY_STANDALONE_MGMT_VDOM)}",
            )
    if "ha-mgmt-status" in payload:
        value = payload["ha-mgmt-status"]
        if value not in VALID_BODY_HA_MGMT_STATUS:
            return (
                False,
                f"Invalid value for 'ha-mgmt-status'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_MGMT_STATUS)}",
            )
    if "standalone-config-sync" in payload:
        value = payload["standalone-config-sync"]
        if value not in VALID_BODY_STANDALONE_CONFIG_SYNC:
            return (
                False,
                f"Invalid value for 'standalone-config-sync'='{value}'. Must be one of: {', '.join(VALID_BODY_STANDALONE_CONFIG_SYNC)}",
            )
    if "unicast-status" in payload:
        value = payload["unicast-status"]
        if value not in VALID_BODY_UNICAST_STATUS:
            return (
                False,
                f"Invalid value for 'unicast-status'='{value}'. Must be one of: {', '.join(VALID_BODY_UNICAST_STATUS)}",
            )
    if "schedule" in payload:
        value = payload["schedule"]
        if value not in VALID_BODY_SCHEDULE:
            return (
                False,
                f"Invalid value for 'schedule'='{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE)}",
            )
    if "override" in payload:
        value = payload["override"]
        if value not in VALID_BODY_OVERRIDE:
            return (
                False,
                f"Invalid value for 'override'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE)}",
            )
    if "pingserver-secondary-force-reset" in payload:
        value = payload["pingserver-secondary-force-reset"]
        if value not in VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET:
            return (
                False,
                f"Invalid value for 'pingserver-secondary-force-reset'='{value}'. Must be one of: {', '.join(VALID_BODY_PINGSERVER_SECONDARY_FORCE_RESET)}",
            )
    if "vcluster-status" in payload:
        value = payload["vcluster-status"]
        if value not in VALID_BODY_VCLUSTER_STATUS:
            return (
                False,
                f"Invalid value for 'vcluster-status'='{value}'. Must be one of: {', '.join(VALID_BODY_VCLUSTER_STATUS)}",
            )
    if "ha-direct" in payload:
        value = payload["ha-direct"]
        if value not in VALID_BODY_HA_DIRECT:
            return (
                False,
                f"Invalid value for 'ha-direct'='{value}'. Must be one of: {', '.join(VALID_BODY_HA_DIRECT)}",
            )
    if "ssd-failover" in payload:
        value = payload["ssd-failover"]
        if value not in VALID_BODY_SSD_FAILOVER:
            return (
                False,
                f"Invalid value for 'ssd-failover'='{value}'. Must be one of: {', '.join(VALID_BODY_SSD_FAILOVER)}",
            )
    if "memory-compatible-mode" in payload:
        value = payload["memory-compatible-mode"]
        if value not in VALID_BODY_MEMORY_COMPATIBLE_MODE:
            return (
                False,
                f"Invalid value for 'memory-compatible-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_MEMORY_COMPATIBLE_MODE)}",
            )
    if "memory-based-failover" in payload:
        value = payload["memory-based-failover"]
        if value not in VALID_BODY_MEMORY_BASED_FAILOVER:
            return (
                False,
                f"Invalid value for 'memory-based-failover'='{value}'. Must be one of: {', '.join(VALID_BODY_MEMORY_BASED_FAILOVER)}",
            )
    if "check-secondary-dev-health" in payload:
        value = payload["check-secondary-dev-health"]
        if value not in VALID_BODY_CHECK_SECONDARY_DEV_HEALTH:
            return (
                False,
                f"Invalid value for 'check-secondary-dev-health'='{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_SECONDARY_DEV_HEALTH)}",
            )
    if "ipsec-phase2-proposal" in payload:
        value = payload["ipsec-phase2-proposal"]
        if value not in VALID_BODY_IPSEC_PHASE2_PROPOSAL:
            return (
                False,
                f"Invalid value for 'ipsec-phase2-proposal'='{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_PHASE2_PROPOSAL)}",
            )
    if "bounce-intf-upon-failover" in payload:
        value = payload["bounce-intf-upon-failover"]
        if value not in VALID_BODY_BOUNCE_INTF_UPON_FAILOVER:
            return (
                False,
                f"Invalid value for 'bounce-intf-upon-failover'='{value}'. Must be one of: {', '.join(VALID_BODY_BOUNCE_INTF_UPON_FAILOVER)}",
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
    "endpoint": "system/ha",
    "category": "cmdb",
    "api_path": "system/ha",
    "help": "Configure HA.",
    "total_fields": 81,
    "required_fields_count": 1,
    "fields_with_defaults_count": 73,
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
