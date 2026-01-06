"""Validation helpers for router/bgp - Auto-generated"""

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
    "as",  # Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "as": "",
    "router-id": "",
    "keepalive-timer": 60,
    "holdtime-timer": 180,
    "always-compare-med": "disable",
    "bestpath-as-path-ignore": "disable",
    "bestpath-cmp-confed-aspath": "disable",
    "bestpath-cmp-routerid": "disable",
    "bestpath-med-confed": "disable",
    "bestpath-med-missing-as-worst": "disable",
    "client-to-client-reflection": "enable",
    "dampening": "disable",
    "deterministic-med": "disable",
    "ebgp-multipath": "disable",
    "ibgp-multipath": "disable",
    "enforce-first-as": "enable",
    "fast-external-failover": "enable",
    "log-neighbour-changes": "enable",
    "network-import-check": "enable",
    "ignore-optional-capability": "enable",
    "additional-path": "disable",
    "additional-path6": "disable",
    "additional-path-vpnv4": "disable",
    "additional-path-vpnv6": "disable",
    "multipath-recursive-distance": "disable",
    "recursive-next-hop": "disable",
    "recursive-inherit-priority": "disable",
    "tag-resolve-mode": "disable",
    "cluster-id": "0.0.0.0",
    "confederation-identifier": 0,
    "dampening-route-map": "",
    "dampening-reachability-half-life": 15,
    "dampening-reuse": 750,
    "dampening-suppress": 2000,
    "dampening-max-suppress-time": 60,
    "dampening-unreachability-half-life": 15,
    "default-local-preference": 100,
    "scan-time": 60,
    "distance-external": 20,
    "distance-internal": 200,
    "distance-local": 200,
    "synchronization": "disable",
    "graceful-restart": "disable",
    "graceful-restart-time": 120,
    "graceful-stalepath-time": 360,
    "graceful-update-delay": 120,
    "graceful-end-on-timer": "disable",
    "additional-path-select": 2,
    "additional-path-select6": 2,
    "additional-path-select-vpnv4": 2,
    "additional-path-select-vpnv6": 2,
    "cross-family-conditional-adv": "disable",
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
    "as": "user",  # Router AS number, asplain/asdot/asdot+ format, 0 to disable 
    "router-id": "ipv4-address-any",  # Router ID.
    "keepalive-timer": "integer",  # Frequency to send keep alive requests.
    "holdtime-timer": "integer",  # Number of seconds to mark peer as dead.
    "always-compare-med": "option",  # Enable/disable always compare MED.
    "bestpath-as-path-ignore": "option",  # Enable/disable ignore AS path.
    "bestpath-cmp-confed-aspath": "option",  # Enable/disable compare federation AS path length.
    "bestpath-cmp-routerid": "option",  # Enable/disable compare router ID for identical EBGP paths.
    "bestpath-med-confed": "option",  # Enable/disable compare MED among confederation paths.
    "bestpath-med-missing-as-worst": "option",  # Enable/disable treat missing MED as least preferred.
    "client-to-client-reflection": "option",  # Enable/disable client-to-client route reflection.
    "dampening": "option",  # Enable/disable route-flap dampening.
    "deterministic-med": "option",  # Enable/disable enforce deterministic comparison of MED.
    "ebgp-multipath": "option",  # Enable/disable EBGP multi-path.
    "ibgp-multipath": "option",  # Enable/disable IBGP multi-path.
    "enforce-first-as": "option",  # Enable/disable enforce first AS for EBGP routes.
    "fast-external-failover": "option",  # Enable/disable reset peer BGP session if link goes down.
    "log-neighbour-changes": "option",  # Log BGP neighbor changes.
    "network-import-check": "option",  # Enable/disable ensure BGP network route exists in IGP.
    "ignore-optional-capability": "option",  # Do not send unknown optional capability notification message
    "additional-path": "option",  # Enable/disable selection of BGP IPv4 additional paths.
    "additional-path6": "option",  # Enable/disable selection of BGP IPv6 additional paths.
    "additional-path-vpnv4": "option",  # Enable/disable selection of BGP VPNv4 additional paths.
    "additional-path-vpnv6": "option",  # Enable/disable selection of BGP VPNv6 additional paths.
    "multipath-recursive-distance": "option",  # Enable/disable use of recursive distance to select multipath
    "recursive-next-hop": "option",  # Enable/disable recursive resolution of next-hop using BGP ro
    "recursive-inherit-priority": "option",  # Enable/disable priority inheritance for recursive resolution
    "tag-resolve-mode": "option",  # Configure tag-match mode. Resolves BGP routes with other rou
    "cluster-id": "ipv4-address-any",  # Route reflector cluster ID.
    "confederation-identifier": "integer",  # Confederation identifier.
    "confederation-peers": "string",  # Confederation peers.
    "dampening-route-map": "string",  # Criteria for dampening.
    "dampening-reachability-half-life": "integer",  # Reachability half-life time for penalty (min).
    "dampening-reuse": "integer",  # Threshold to reuse routes.
    "dampening-suppress": "integer",  # Threshold to suppress routes.
    "dampening-max-suppress-time": "integer",  # Maximum minutes a route can be suppressed.
    "dampening-unreachability-half-life": "integer",  # Unreachability half-life time for penalty (min).
    "default-local-preference": "integer",  # Default local preference.
    "scan-time": "integer",  # Background scanner interval (sec), 0 to disable it.
    "distance-external": "integer",  # Distance for routes external to the AS.
    "distance-internal": "integer",  # Distance for routes internal to the AS.
    "distance-local": "integer",  # Distance for routes local to the AS.
    "synchronization": "option",  # Enable/disable only advertise routes from iBGP if routes pre
    "graceful-restart": "option",  # Enable/disable BGP graceful restart capabilities.
    "graceful-restart-time": "integer",  # Time needed for neighbors to restart (sec).
    "graceful-stalepath-time": "integer",  # Time to hold stale paths of restarting neighbor (sec).
    "graceful-update-delay": "integer",  # Route advertisement/selection delay after restart (sec).
    "graceful-end-on-timer": "option",  # Enable/disable to exit graceful restart on timer only.
    "additional-path-select": "integer",  # Number of additional paths to be selected for each IPv4 NLRI
    "additional-path-select6": "integer",  # Number of additional paths to be selected for each IPv6 NLRI
    "additional-path-select-vpnv4": "integer",  # Number of additional paths to be selected for each VPNv4 NLR
    "additional-path-select-vpnv6": "integer",  # Number of additional paths to be selected for each VPNv6 NLR
    "cross-family-conditional-adv": "option",  # Enable/disable cross address family conditional advertisemen
    "aggregate-address": "string",  # BGP aggregate address table.
    "aggregate-address6": "string",  # BGP IPv6 aggregate address table.
    "neighbor": "string",  # BGP neighbor table.
    "neighbor-group": "string",  # BGP neighbor group table.
    "neighbor-range": "string",  # BGP neighbor range table.
    "neighbor-range6": "string",  # BGP IPv6 neighbor range table.
    "network": "string",  # BGP network table.
    "network6": "string",  # BGP IPv6 network table.
    "redistribute": "string",  # BGP IPv4 redistribute table.
    "redistribute6": "string",  # BGP IPv6 redistribute table.
    "admin-distance": "string",  # Administrative distance modifications.
    "vrf": "string",  # BGP VRF leaking table.
    "vrf6": "string",  # BGP IPv6 VRF leaking table.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "as": "Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP.",
    "router-id": "Router ID.",
    "keepalive-timer": "Frequency to send keep alive requests.",
    "holdtime-timer": "Number of seconds to mark peer as dead.",
    "always-compare-med": "Enable/disable always compare MED.",
    "bestpath-as-path-ignore": "Enable/disable ignore AS path.",
    "bestpath-cmp-confed-aspath": "Enable/disable compare federation AS path length.",
    "bestpath-cmp-routerid": "Enable/disable compare router ID for identical EBGP paths.",
    "bestpath-med-confed": "Enable/disable compare MED among confederation paths.",
    "bestpath-med-missing-as-worst": "Enable/disable treat missing MED as least preferred.",
    "client-to-client-reflection": "Enable/disable client-to-client route reflection.",
    "dampening": "Enable/disable route-flap dampening.",
    "deterministic-med": "Enable/disable enforce deterministic comparison of MED.",
    "ebgp-multipath": "Enable/disable EBGP multi-path.",
    "ibgp-multipath": "Enable/disable IBGP multi-path.",
    "enforce-first-as": "Enable/disable enforce first AS for EBGP routes.",
    "fast-external-failover": "Enable/disable reset peer BGP session if link goes down.",
    "log-neighbour-changes": "Log BGP neighbor changes.",
    "network-import-check": "Enable/disable ensure BGP network route exists in IGP.",
    "ignore-optional-capability": "Do not send unknown optional capability notification message.",
    "additional-path": "Enable/disable selection of BGP IPv4 additional paths.",
    "additional-path6": "Enable/disable selection of BGP IPv6 additional paths.",
    "additional-path-vpnv4": "Enable/disable selection of BGP VPNv4 additional paths.",
    "additional-path-vpnv6": "Enable/disable selection of BGP VPNv6 additional paths.",
    "multipath-recursive-distance": "Enable/disable use of recursive distance to select multipath.",
    "recursive-next-hop": "Enable/disable recursive resolution of next-hop using BGP route.",
    "recursive-inherit-priority": "Enable/disable priority inheritance for recursive resolution.",
    "tag-resolve-mode": "Configure tag-match mode. Resolves BGP routes with other routes containing the same tag.",
    "cluster-id": "Route reflector cluster ID.",
    "confederation-identifier": "Confederation identifier.",
    "confederation-peers": "Confederation peers.",
    "dampening-route-map": "Criteria for dampening.",
    "dampening-reachability-half-life": "Reachability half-life time for penalty (min).",
    "dampening-reuse": "Threshold to reuse routes.",
    "dampening-suppress": "Threshold to suppress routes.",
    "dampening-max-suppress-time": "Maximum minutes a route can be suppressed.",
    "dampening-unreachability-half-life": "Unreachability half-life time for penalty (min).",
    "default-local-preference": "Default local preference.",
    "scan-time": "Background scanner interval (sec), 0 to disable it.",
    "distance-external": "Distance for routes external to the AS.",
    "distance-internal": "Distance for routes internal to the AS.",
    "distance-local": "Distance for routes local to the AS.",
    "synchronization": "Enable/disable only advertise routes from iBGP if routes present in an IGP.",
    "graceful-restart": "Enable/disable BGP graceful restart capabilities.",
    "graceful-restart-time": "Time needed for neighbors to restart (sec).",
    "graceful-stalepath-time": "Time to hold stale paths of restarting neighbor (sec).",
    "graceful-update-delay": "Route advertisement/selection delay after restart (sec).",
    "graceful-end-on-timer": "Enable/disable to exit graceful restart on timer only.",
    "additional-path-select": "Number of additional paths to be selected for each IPv4 NLRI.",
    "additional-path-select6": "Number of additional paths to be selected for each IPv6 NLRI.",
    "additional-path-select-vpnv4": "Number of additional paths to be selected for each VPNv4 NLRI.",
    "additional-path-select-vpnv6": "Number of additional paths to be selected for each VPNv6 NLRI.",
    "cross-family-conditional-adv": "Enable/disable cross address family conditional advertisement.",
    "aggregate-address": "BGP aggregate address table.",
    "aggregate-address6": "BGP IPv6 aggregate address table.",
    "neighbor": "BGP neighbor table.",
    "neighbor-group": "BGP neighbor group table.",
    "neighbor-range": "BGP neighbor range table.",
    "neighbor-range6": "BGP IPv6 neighbor range table.",
    "network": "BGP network table.",
    "network6": "BGP IPv6 network table.",
    "redistribute": "BGP IPv4 redistribute table.",
    "redistribute6": "BGP IPv6 redistribute table.",
    "admin-distance": "Administrative distance modifications.",
    "vrf": "BGP VRF leaking table.",
    "vrf6": "BGP IPv6 VRF leaking table.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "keepalive-timer": {"type": "integer", "min": 0, "max": 65535},
    "holdtime-timer": {"type": "integer", "min": 3, "max": 65535},
    "confederation-identifier": {"type": "integer", "min": 1, "max": 4294967295},
    "dampening-route-map": {"type": "string", "max_length": 35},
    "dampening-reachability-half-life": {"type": "integer", "min": 1, "max": 45},
    "dampening-reuse": {"type": "integer", "min": 1, "max": 20000},
    "dampening-suppress": {"type": "integer", "min": 1, "max": 20000},
    "dampening-max-suppress-time": {"type": "integer", "min": 1, "max": 255},
    "dampening-unreachability-half-life": {"type": "integer", "min": 1, "max": 45},
    "default-local-preference": {"type": "integer", "min": 0, "max": 4294967295},
    "scan-time": {"type": "integer", "min": 5, "max": 60},
    "distance-external": {"type": "integer", "min": 1, "max": 255},
    "distance-internal": {"type": "integer", "min": 1, "max": 255},
    "distance-local": {"type": "integer", "min": 1, "max": 255},
    "graceful-restart-time": {"type": "integer", "min": 1, "max": 3600},
    "graceful-stalepath-time": {"type": "integer", "min": 1, "max": 3600},
    "graceful-update-delay": {"type": "integer", "min": 1, "max": 3600},
    "additional-path-select": {"type": "integer", "min": 2, "max": 255},
    "additional-path-select6": {"type": "integer", "min": 2, "max": 255},
    "additional-path-select-vpnv4": {"type": "integer", "min": 2, "max": 255},
    "additional-path-select-vpnv6": {"type": "integer", "min": 2, "max": 255},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "confederation-peers": {
        "peer": {
            "type": "string",
            "help": "Peer ID.",
            "default": "",
            "max_length": 79,
        },
    },
    "aggregate-address": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet-any",
            "help": "Aggregate prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "as-set": {
            "type": "option",
            "help": "Enable/disable generate AS set path information.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "summary-only": {
            "type": "option",
            "help": "Enable/disable filter more specific routes from updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "aggregate-address6": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix6": {
            "type": "ipv6-prefix",
            "help": "Aggregate IPv6 prefix.",
            "required": True,
            "default": "::/0",
        },
        "as-set": {
            "type": "option",
            "help": "Enable/disable generate AS set path information.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "summary-only": {
            "type": "option",
            "help": "Enable/disable filter more specific routes from updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "neighbor": {
        "ip": {
            "type": "string",
            "help": "IP/IPv6 address of neighbor.",
            "required": True,
            "default": "",
            "max_length": 45,
        },
        "advertisement-interval": {
            "type": "integer",
            "help": "Minimum interval (sec) between sending updates.",
            "default": 30,
            "min_value": 0,
            "max_value": 600,
        },
        "allowas-in-enable": {
            "type": "option",
            "help": "Enable/disable IPv4 Enable to allow my AS in AS path.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable6": {
            "type": "option",
            "help": "Enable/disable IPv6 Enable to allow my AS in AS path.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable-vpnv4": {
            "type": "option",
            "help": "Enable/disable to allow my AS in AS path for VPNv4 route.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable-vpnv6": {
            "type": "option",
            "help": "Enable/disable use of my AS in AS path for VPNv6 route.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable-evpn": {
            "type": "option",
            "help": "Enable/disable to allow my AS in AS path for L2VPN EVPN route.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in": {
            "type": "integer",
            "help": "IPv4 The maximum number of occurrence of my AS number allowed.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in6": {
            "type": "integer",
            "help": "IPv6 The maximum number of occurrence of my AS number allowed.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in-vpnv4": {
            "type": "integer",
            "help": "The maximum number of occurrence of my AS number allowed for VPNv4 route.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in-vpnv6": {
            "type": "integer",
            "help": "The maximum number of occurrence of my AS number allowed for VPNv6 route.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in-evpn": {
            "type": "integer",
            "help": "The maximum number of occurrence of my AS number allowed for L2VPN EVPN route.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "attribute-unchanged": {
            "type": "option",
            "help": "IPv4 List of attributes that should be unchanged.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "attribute-unchanged6": {
            "type": "option",
            "help": "IPv6 List of attributes that should be unchanged.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "attribute-unchanged-vpnv4": {
            "type": "option",
            "help": "List of attributes that should be unchanged for VPNv4 route.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "attribute-unchanged-vpnv6": {
            "type": "option",
            "help": "List of attributes that should not be changed for VPNv6 route.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "activate": {
            "type": "option",
            "help": "Enable/disable address family IPv4 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate6": {
            "type": "option",
            "help": "Enable/disable address family IPv6 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate-vpnv4": {
            "type": "option",
            "help": "Enable/disable address family VPNv4 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate-vpnv6": {
            "type": "option",
            "help": "Enable/disable address family VPNv6 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate-evpn": {
            "type": "option",
            "help": "Enable/disable address family L2VPN EVPN for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "bfd": {
            "type": "option",
            "help": "Enable/disable BFD for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-dynamic": {
            "type": "option",
            "help": "Enable/disable advertise dynamic capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-orf": {
            "type": "option",
            "help": "Accept/Send IPv4 ORF lists to/from this neighbor.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Receive ORF lists.", "label": "Receive", "name": "receive"}, {"help": "Send ORF list.", "label": "Send", "name": "send"}, {"help": "Send and receive ORF lists.", "label": "Both", "name": "both"}],
        },
        "capability-orf6": {
            "type": "option",
            "help": "Accept/Send IPv6 ORF lists to/from this neighbor.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Receive ORF lists.", "label": "Receive", "name": "receive"}, {"help": "Send ORF list.", "label": "Send", "name": "send"}, {"help": "Send and receive ORF lists.", "label": "Both", "name": "both"}],
        },
        "capability-graceful-restart": {
            "type": "option",
            "help": "Enable/disable advertise IPv4 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart6": {
            "type": "option",
            "help": "Enable/disable advertise IPv6 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart-vpnv4": {
            "type": "option",
            "help": "Enable/disable advertise VPNv4 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart-vpnv6": {
            "type": "option",
            "help": "Enable/disable advertisement of VPNv6 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart-evpn": {
            "type": "option",
            "help": "Enable/disable advertisement of L2VPN EVPN graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-route-refresh": {
            "type": "option",
            "help": "Enable/disable advertise route refresh capability to this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-default-originate": {
            "type": "option",
            "help": "Enable/disable advertise default IPv4 route to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-default-originate6": {
            "type": "option",
            "help": "Enable/disable advertise default IPv6 route to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "dont-capability-negotiate": {
            "type": "option",
            "help": "Do not negotiate capabilities with this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "ebgp-enforce-multihop": {
            "type": "option",
            "help": "Enable/disable allow multi-hop EBGP neighbors.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "link-down-failover": {
            "type": "option",
            "help": "Enable/disable failover upon link down.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "stale-route": {
            "type": "option",
            "help": "Enable/disable stale route after neighbor down.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self": {
            "type": "option",
            "help": "Enable/disable IPv4 next-hop calculation for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self6": {
            "type": "option",
            "help": "Enable/disable IPv6 next-hop calculation for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-rr": {
            "type": "option",
            "help": "Enable/disable setting nexthop's address to interface's IPv4 address for route-reflector routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-rr6": {
            "type": "option",
            "help": "Enable/disable setting nexthop's address to interface's IPv6 address for route-reflector routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-vpnv4": {
            "type": "option",
            "help": "Enable/disable setting VPNv4 next-hop to interface's IP address for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-vpnv6": {
            "type": "option",
            "help": "Enable/disable use of outgoing interface's IP address as VPNv6 next-hop for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "override-capability": {
            "type": "option",
            "help": "Enable/disable override result of capability negotiation.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "passive": {
            "type": "option",
            "help": "Enable/disable sending of open messages to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as": {
            "type": "option",
            "help": "Enable/disable remove private AS number from IPv4 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as6": {
            "type": "option",
            "help": "Enable/disable remove private AS number from IPv6 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as-vpnv4": {
            "type": "option",
            "help": "Enable/disable remove private AS number from VPNv4 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as-vpnv6": {
            "type": "option",
            "help": "Enable/disable to remove private AS number from VPNv6 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as-evpn": {
            "type": "option",
            "help": "Enable/disable removing private AS number from L2VPN EVPN outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client": {
            "type": "option",
            "help": "Enable/disable IPv4 AS route reflector client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client6": {
            "type": "option",
            "help": "Enable/disable IPv6 AS route reflector client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client-vpnv4": {
            "type": "option",
            "help": "Enable/disable VPNv4 AS route reflector client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 AS route reflector client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client-evpn": {
            "type": "option",
            "help": "Enable/disable L2VPN EVPN AS route reflector client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client": {
            "type": "option",
            "help": "Enable/disable IPv4 AS route server client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client6": {
            "type": "option",
            "help": "Enable/disable IPv6 AS route server client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client-vpnv4": {
            "type": "option",
            "help": "Enable/disable VPNv4 AS route server client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 AS route server client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client-evpn": {
            "type": "option",
            "help": "Enable/disable L2VPN EVPN AS route server client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to IPv4 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change6": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to IPv6 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change-vpnv4": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to VPNv4 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change-vpnv6": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to VPNv6 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change-evpn": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to L2VPN EVPN route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "shutdown": {
            "type": "option",
            "help": "Enable/disable shutdown this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration": {
            "type": "option",
            "help": "Enable/disable allow IPv4 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration6": {
            "type": "option",
            "help": "Enable/disable allow IPv6 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration-vpnv4": {
            "type": "option",
            "help": "Enable/disable allow VPNv4 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration-evpn": {
            "type": "option",
            "help": "Enable/disable L2VPN EVPN inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "as-override": {
            "type": "option",
            "help": "Enable/disable replace peer AS with own AS for IPv4.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "as-override6": {
            "type": "option",
            "help": "Enable/disable replace peer AS with own AS for IPv6.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "strict-capability-match": {
            "type": "option",
            "help": "Enable/disable strict capability matching.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "default-originate-routemap": {
            "type": "string",
            "help": "Route map to specify criteria to originate IPv4 default.",
            "default": "",
            "max_length": 35,
        },
        "default-originate-routemap6": {
            "type": "string",
            "help": "Route map to specify criteria to originate IPv6 default.",
            "default": "",
            "max_length": 35,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 63,
        },
        "distribute-list-in": {
            "type": "string",
            "help": "Filter for IPv4 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-in6": {
            "type": "string",
            "help": "Filter for IPv6 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-in-vpnv4": {
            "type": "string",
            "help": "Filter for VPNv4 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-in-vpnv6": {
            "type": "string",
            "help": "Filter for VPNv6 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out": {
            "type": "string",
            "help": "Filter for IPv4 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out6": {
            "type": "string",
            "help": "Filter for IPv6 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out-vpnv4": {
            "type": "string",
            "help": "Filter for VPNv4 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out-vpnv6": {
            "type": "string",
            "help": "Filter for VPNv6 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "ebgp-multihop-ttl": {
            "type": "integer",
            "help": "EBGP multihop TTL for this peer.",
            "default": 255,
            "min_value": 1,
            "max_value": 255,
        },
        "filter-list-in": {
            "type": "string",
            "help": "BGP filter for IPv4 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-in6": {
            "type": "string",
            "help": "BGP filter for IPv6 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-in-vpnv4": {
            "type": "string",
            "help": "BGP filter for VPNv4 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-in-vpnv6": {
            "type": "string",
            "help": "BGP filter for VPNv6 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out": {
            "type": "string",
            "help": "BGP filter for IPv4 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out6": {
            "type": "string",
            "help": "BGP filter for IPv6 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out-vpnv4": {
            "type": "string",
            "help": "BGP filter for VPNv4 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out-vpnv6": {
            "type": "string",
            "help": "BGP filter for VPNv6 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface for peer connection. For IPv6 peer, the interface should have link-local address.",
            "default": "",
            "max_length": 15,
        },
        "maximum-prefix": {
            "type": "integer",
            "help": "Maximum number of IPv4 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix6": {
            "type": "integer",
            "help": "Maximum number of IPv6 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-vpnv4": {
            "type": "integer",
            "help": "Maximum number of VPNv4 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-vpnv6": {
            "type": "integer",
            "help": "Maximum number of VPNv6 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-evpn": {
            "type": "integer",
            "help": "Maximum number of L2VPN EVPN prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-threshold": {
            "type": "integer",
            "help": "Maximum IPv4 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold6": {
            "type": "integer",
            "help": "Maximum IPv6 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold-vpnv4": {
            "type": "integer",
            "help": "Maximum VPNv4 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold-vpnv6": {
            "type": "integer",
            "help": "Maximum VPNv6 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold-evpn": {
            "type": "integer",
            "help": "Maximum L2VPN EVPN prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-warning-only": {
            "type": "option",
            "help": "Enable/disable IPv4 Only give warning message when limit is exceeded.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only6": {
            "type": "option",
            "help": "Enable/disable IPv6 Only give warning message when limit is exceeded.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only-vpnv4": {
            "type": "option",
            "help": "Enable/disable only giving warning message when limit is exceeded for VPNv4 routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only-vpnv6": {
            "type": "option",
            "help": "Enable/disable warning message when limit is exceeded for VPNv6 routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only-evpn": {
            "type": "option",
            "help": "Enable/disable only sending warning message when exceeding limit of L2VPN EVPN routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "prefix-list-in": {
            "type": "string",
            "help": "IPv4 Inbound filter for updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-in6": {
            "type": "string",
            "help": "IPv6 Inbound filter for updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-in-vpnv4": {
            "type": "string",
            "help": "Inbound filter for VPNv4 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-in-vpnv6": {
            "type": "string",
            "help": "Inbound filter for VPNv6 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out": {
            "type": "string",
            "help": "IPv4 Outbound filter for updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out6": {
            "type": "string",
            "help": "IPv6 Outbound filter for updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out-vpnv4": {
            "type": "string",
            "help": "Outbound filter for VPNv4 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out-vpnv6": {
            "type": "string",
            "help": "Outbound filter for VPNv6 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "remote-as": {
            "type": "user",
            "help": "AS number of neighbor.",
            "required": True,
            "default": "",
        },
        "local-as": {
            "type": "user",
            "help": "Local AS number of neighbor.",
            "default": "",
        },
        "local-as-no-prepend": {
            "type": "option",
            "help": "Do not prepend local-as to incoming updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "local-as-replace-as": {
            "type": "option",
            "help": "Replace real AS with local-as in outgoing updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "retain-stale-time": {
            "type": "integer",
            "help": "Time to retain stale routes.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "route-map-in": {
            "type": "string",
            "help": "IPv4 Inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in6": {
            "type": "string",
            "help": "IPv6 Inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in-vpnv4": {
            "type": "string",
            "help": "VPNv4 inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in-vpnv6": {
            "type": "string",
            "help": "VPNv6 inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in-evpn": {
            "type": "string",
            "help": "L2VPN EVPN inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out": {
            "type": "string",
            "help": "IPv4 outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-preferable": {
            "type": "string",
            "help": "IPv4 outbound route map filter if the peer is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out6": {
            "type": "string",
            "help": "IPv6 Outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out6-preferable": {
            "type": "string",
            "help": "IPv6 outbound route map filter if the peer is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv4": {
            "type": "string",
            "help": "VPNv4 outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv6": {
            "type": "string",
            "help": "VPNv6 outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv4-preferable": {
            "type": "string",
            "help": "VPNv4 outbound route map filter if the peer is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv6-preferable": {
            "type": "string",
            "help": "VPNv6 outbound route map filter if this neighbor is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-evpn": {
            "type": "string",
            "help": "L2VPN EVPN outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "send-community": {
            "type": "option",
            "help": "IPv4 Send community attribute to neighbor.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community6": {
            "type": "option",
            "help": "IPv6 Send community attribute to neighbor.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community-vpnv4": {
            "type": "option",
            "help": "Send community attribute to neighbor for VPNv4 address family.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community-vpnv6": {
            "type": "option",
            "help": "Enable/disable sending community attribute to this neighbor for VPNv6 address family.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community-evpn": {
            "type": "option",
            "help": "Enable/disable sending community attribute to neighbor for L2VPN EVPN address family.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "keep-alive-timer": {
            "type": "integer",
            "help": "Keep alive timer interval (sec).",
            "default": 4294967295,
            "min_value": 0,
            "max_value": 65535,
        },
        "holdtime-timer": {
            "type": "integer",
            "help": "Interval (sec) before peer considered dead.",
            "default": 4294967295,
            "min_value": 3,
            "max_value": 65535,
        },
        "connect-timer": {
            "type": "integer",
            "help": "Interval (sec) for connect timer.",
            "default": 4294967295,
            "min_value": 1,
            "max_value": 65535,
        },
        "unsuppress-map": {
            "type": "string",
            "help": "IPv4 Route map to selectively unsuppress suppressed routes.",
            "default": "",
            "max_length": 35,
        },
        "unsuppress-map6": {
            "type": "string",
            "help": "IPv6 Route map to selectively unsuppress suppressed routes.",
            "default": "",
            "max_length": 35,
        },
        "update-source": {
            "type": "string",
            "help": "Interface to use as source IP/IPv6 address of TCP connections.",
            "default": "",
            "max_length": 15,
        },
        "weight": {
            "type": "integer",
            "help": "Neighbor weight.",
            "default": 4294967295,
            "min_value": 0,
            "max_value": 65535,
        },
        "restart-time": {
            "type": "integer",
            "help": "Graceful restart delay time (sec, 0 = global default).",
            "default": 0,
            "min_value": 0,
            "max_value": 3600,
        },
        "additional-path": {
            "type": "option",
            "help": "Enable/disable IPv4 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "additional-path6": {
            "type": "option",
            "help": "Enable/disable IPv6 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "additional-path-vpnv4": {
            "type": "option",
            "help": "Enable/disable VPNv4 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "additional-path-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "adv-additional-path": {
            "type": "integer",
            "help": "Number of IPv4 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "adv-additional-path6": {
            "type": "integer",
            "help": "Number of IPv6 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "adv-additional-path-vpnv4": {
            "type": "integer",
            "help": "Number of VPNv4 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "adv-additional-path-vpnv6": {
            "type": "integer",
            "help": "Number of VPNv6 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "password": {
            "type": "password",
            "help": "Password used in MD5 authentication.",
            "max_length": 128,
        },
        "auth-options": {
            "type": "string",
            "help": "Key-chain name for TCP authentication options.",
            "default": "",
            "max_length": 35,
        },
        "conditional-advertise": {
            "type": "string",
            "help": "Conditional advertisement.",
        },
        "conditional-advertise6": {
            "type": "string",
            "help": "IPv6 conditional advertisement.",
        },
    },
    "neighbor-group": {
        "name": {
            "type": "string",
            "help": "Neighbor group name.",
            "required": True,
            "default": "",
            "max_length": 45,
        },
        "advertisement-interval": {
            "type": "integer",
            "help": "Minimum interval (sec) between sending updates.",
            "default": 30,
            "min_value": 0,
            "max_value": 600,
        },
        "allowas-in-enable": {
            "type": "option",
            "help": "Enable/disable IPv4 Enable to allow my AS in AS path.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable6": {
            "type": "option",
            "help": "Enable/disable IPv6 Enable to allow my AS in AS path.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable-vpnv4": {
            "type": "option",
            "help": "Enable/disable to allow my AS in AS path for VPNv4 route.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable-vpnv6": {
            "type": "option",
            "help": "Enable/disable use of my AS in AS path for VPNv6 route.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in-enable-evpn": {
            "type": "option",
            "help": "Enable/disable to allow my AS in AS path for L2VPN EVPN route.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowas-in": {
            "type": "integer",
            "help": "IPv4 The maximum number of occurrence of my AS number allowed.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in6": {
            "type": "integer",
            "help": "IPv6 The maximum number of occurrence of my AS number allowed.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in-vpnv4": {
            "type": "integer",
            "help": "The maximum number of occurrence of my AS number allowed for VPNv4 route.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in-vpnv6": {
            "type": "integer",
            "help": "The maximum number of occurrence of my AS number allowed for VPNv6 route.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "allowas-in-evpn": {
            "type": "integer",
            "help": "The maximum number of occurrence of my AS number allowed for L2VPN EVPN route.",
            "default": 3,
            "min_value": 1,
            "max_value": 10,
        },
        "attribute-unchanged": {
            "type": "option",
            "help": "IPv4 List of attributes that should be unchanged.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "attribute-unchanged6": {
            "type": "option",
            "help": "IPv6 List of attributes that should be unchanged.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "attribute-unchanged-vpnv4": {
            "type": "option",
            "help": "List of attributes that should be unchanged for VPNv4 route.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "attribute-unchanged-vpnv6": {
            "type": "option",
            "help": "List of attributes that should not be changed for VPNv6 route.",
            "default": "",
            "options": [{"help": "AS path.", "label": "As Path", "name": "as-path"}, {"help": "MED.", "label": "Med", "name": "med"}, {"help": "Next hop.", "label": "Next Hop", "name": "next-hop"}],
        },
        "activate": {
            "type": "option",
            "help": "Enable/disable address family IPv4 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate6": {
            "type": "option",
            "help": "Enable/disable address family IPv6 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate-vpnv4": {
            "type": "option",
            "help": "Enable/disable address family VPNv4 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate-vpnv6": {
            "type": "option",
            "help": "Enable/disable address family VPNv6 for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "activate-evpn": {
            "type": "option",
            "help": "Enable/disable address family L2VPN EVPN for this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "bfd": {
            "type": "option",
            "help": "Enable/disable BFD for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-dynamic": {
            "type": "option",
            "help": "Enable/disable advertise dynamic capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-orf": {
            "type": "option",
            "help": "Accept/Send IPv4 ORF lists to/from this neighbor.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Receive ORF lists.", "label": "Receive", "name": "receive"}, {"help": "Send ORF list.", "label": "Send", "name": "send"}, {"help": "Send and receive ORF lists.", "label": "Both", "name": "both"}],
        },
        "capability-orf6": {
            "type": "option",
            "help": "Accept/Send IPv6 ORF lists to/from this neighbor.",
            "default": "none",
            "options": [{"help": "None.", "label": "None", "name": "none"}, {"help": "Receive ORF lists.", "label": "Receive", "name": "receive"}, {"help": "Send ORF list.", "label": "Send", "name": "send"}, {"help": "Send and receive ORF lists.", "label": "Both", "name": "both"}],
        },
        "capability-graceful-restart": {
            "type": "option",
            "help": "Enable/disable advertise IPv4 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart6": {
            "type": "option",
            "help": "Enable/disable advertise IPv6 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart-vpnv4": {
            "type": "option",
            "help": "Enable/disable advertise VPNv4 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart-vpnv6": {
            "type": "option",
            "help": "Enable/disable advertisement of VPNv6 graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-graceful-restart-evpn": {
            "type": "option",
            "help": "Enable/disable advertisement of L2VPN EVPN graceful restart capability to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-route-refresh": {
            "type": "option",
            "help": "Enable/disable advertise route refresh capability to this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-default-originate": {
            "type": "option",
            "help": "Enable/disable advertise default IPv4 route to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "capability-default-originate6": {
            "type": "option",
            "help": "Enable/disable advertise default IPv6 route to this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "dont-capability-negotiate": {
            "type": "option",
            "help": "Do not negotiate capabilities with this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "ebgp-enforce-multihop": {
            "type": "option",
            "help": "Enable/disable allow multi-hop EBGP neighbors.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "link-down-failover": {
            "type": "option",
            "help": "Enable/disable failover upon link down.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "stale-route": {
            "type": "option",
            "help": "Enable/disable stale route after neighbor down.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self": {
            "type": "option",
            "help": "Enable/disable IPv4 next-hop calculation for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self6": {
            "type": "option",
            "help": "Enable/disable IPv6 next-hop calculation for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-rr": {
            "type": "option",
            "help": "Enable/disable setting nexthop's address to interface's IPv4 address for route-reflector routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-rr6": {
            "type": "option",
            "help": "Enable/disable setting nexthop's address to interface's IPv6 address for route-reflector routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-vpnv4": {
            "type": "option",
            "help": "Enable/disable setting VPNv4 next-hop to interface's IP address for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "next-hop-self-vpnv6": {
            "type": "option",
            "help": "Enable/disable use of outgoing interface's IP address as VPNv6 next-hop for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "override-capability": {
            "type": "option",
            "help": "Enable/disable override result of capability negotiation.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "passive": {
            "type": "option",
            "help": "Enable/disable sending of open messages to this neighbor.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as": {
            "type": "option",
            "help": "Enable/disable remove private AS number from IPv4 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as6": {
            "type": "option",
            "help": "Enable/disable remove private AS number from IPv6 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as-vpnv4": {
            "type": "option",
            "help": "Enable/disable remove private AS number from VPNv4 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as-vpnv6": {
            "type": "option",
            "help": "Enable/disable to remove private AS number from VPNv6 outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "remove-private-as-evpn": {
            "type": "option",
            "help": "Enable/disable removing private AS number from L2VPN EVPN outbound updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client": {
            "type": "option",
            "help": "Enable/disable IPv4 AS route reflector client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client6": {
            "type": "option",
            "help": "Enable/disable IPv6 AS route reflector client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client-vpnv4": {
            "type": "option",
            "help": "Enable/disable VPNv4 AS route reflector client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 AS route reflector client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-reflector-client-evpn": {
            "type": "option",
            "help": "Enable/disable L2VPN EVPN AS route reflector client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client": {
            "type": "option",
            "help": "Enable/disable IPv4 AS route server client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client6": {
            "type": "option",
            "help": "Enable/disable IPv6 AS route server client.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client-vpnv4": {
            "type": "option",
            "help": "Enable/disable VPNv4 AS route server client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 AS route server client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-server-client-evpn": {
            "type": "option",
            "help": "Enable/disable L2VPN EVPN AS route server client for this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to IPv4 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change6": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to IPv6 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change-vpnv4": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to VPNv4 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change-vpnv6": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to VPNv6 route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "rr-attr-allow-change-evpn": {
            "type": "option",
            "help": "Enable/disable allowing change of route attributes when advertising to L2VPN EVPN route reflector clients.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "shutdown": {
            "type": "option",
            "help": "Enable/disable shutdown this neighbor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration": {
            "type": "option",
            "help": "Enable/disable allow IPv4 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration6": {
            "type": "option",
            "help": "Enable/disable allow IPv6 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration-vpnv4": {
            "type": "option",
            "help": "Enable/disable allow VPNv4 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "soft-reconfiguration-evpn": {
            "type": "option",
            "help": "Enable/disable L2VPN EVPN inbound soft reconfiguration.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "as-override": {
            "type": "option",
            "help": "Enable/disable replace peer AS with own AS for IPv4.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "as-override6": {
            "type": "option",
            "help": "Enable/disable replace peer AS with own AS for IPv6.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "strict-capability-match": {
            "type": "option",
            "help": "Enable/disable strict capability matching.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "default-originate-routemap": {
            "type": "string",
            "help": "Route map to specify criteria to originate IPv4 default.",
            "default": "",
            "max_length": 35,
        },
        "default-originate-routemap6": {
            "type": "string",
            "help": "Route map to specify criteria to originate IPv6 default.",
            "default": "",
            "max_length": 35,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 63,
        },
        "distribute-list-in": {
            "type": "string",
            "help": "Filter for IPv4 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-in6": {
            "type": "string",
            "help": "Filter for IPv6 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-in-vpnv4": {
            "type": "string",
            "help": "Filter for VPNv4 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-in-vpnv6": {
            "type": "string",
            "help": "Filter for VPNv6 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out": {
            "type": "string",
            "help": "Filter for IPv4 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out6": {
            "type": "string",
            "help": "Filter for IPv6 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out-vpnv4": {
            "type": "string",
            "help": "Filter for VPNv4 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "distribute-list-out-vpnv6": {
            "type": "string",
            "help": "Filter for VPNv6 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "ebgp-multihop-ttl": {
            "type": "integer",
            "help": "EBGP multihop TTL for this peer.",
            "default": 255,
            "min_value": 1,
            "max_value": 255,
        },
        "filter-list-in": {
            "type": "string",
            "help": "BGP filter for IPv4 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-in6": {
            "type": "string",
            "help": "BGP filter for IPv6 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-in-vpnv4": {
            "type": "string",
            "help": "BGP filter for VPNv4 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-in-vpnv6": {
            "type": "string",
            "help": "BGP filter for VPNv6 inbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out": {
            "type": "string",
            "help": "BGP filter for IPv4 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out6": {
            "type": "string",
            "help": "BGP filter for IPv6 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out-vpnv4": {
            "type": "string",
            "help": "BGP filter for VPNv4 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "filter-list-out-vpnv6": {
            "type": "string",
            "help": "BGP filter for VPNv6 outbound routes.",
            "default": "",
            "max_length": 35,
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface for peer connection. For IPv6 peer, the interface should have link-local address.",
            "default": "",
            "max_length": 15,
        },
        "maximum-prefix": {
            "type": "integer",
            "help": "Maximum number of IPv4 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix6": {
            "type": "integer",
            "help": "Maximum number of IPv6 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-vpnv4": {
            "type": "integer",
            "help": "Maximum number of VPNv4 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-vpnv6": {
            "type": "integer",
            "help": "Maximum number of VPNv6 prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-evpn": {
            "type": "integer",
            "help": "Maximum number of L2VPN EVPN prefixes to accept from this peer.",
            "default": 0,
            "min_value": 1,
            "max_value": 4294967295,
        },
        "maximum-prefix-threshold": {
            "type": "integer",
            "help": "Maximum IPv4 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold6": {
            "type": "integer",
            "help": "Maximum IPv6 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold-vpnv4": {
            "type": "integer",
            "help": "Maximum VPNv4 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold-vpnv6": {
            "type": "integer",
            "help": "Maximum VPNv6 prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-threshold-evpn": {
            "type": "integer",
            "help": "Maximum L2VPN EVPN prefix threshold value (1 - 100 percent).",
            "default": 75,
            "min_value": 1,
            "max_value": 100,
        },
        "maximum-prefix-warning-only": {
            "type": "option",
            "help": "Enable/disable IPv4 Only give warning message when limit is exceeded.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only6": {
            "type": "option",
            "help": "Enable/disable IPv6 Only give warning message when limit is exceeded.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only-vpnv4": {
            "type": "option",
            "help": "Enable/disable only giving warning message when limit is exceeded for VPNv4 routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only-vpnv6": {
            "type": "option",
            "help": "Enable/disable warning message when limit is exceeded for VPNv6 routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "maximum-prefix-warning-only-evpn": {
            "type": "option",
            "help": "Enable/disable only sending warning message when exceeding limit of L2VPN EVPN routes.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "prefix-list-in": {
            "type": "string",
            "help": "IPv4 Inbound filter for updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-in6": {
            "type": "string",
            "help": "IPv6 Inbound filter for updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-in-vpnv4": {
            "type": "string",
            "help": "Inbound filter for VPNv4 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-in-vpnv6": {
            "type": "string",
            "help": "Inbound filter for VPNv6 updates from this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out": {
            "type": "string",
            "help": "IPv4 Outbound filter for updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out6": {
            "type": "string",
            "help": "IPv6 Outbound filter for updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out-vpnv4": {
            "type": "string",
            "help": "Outbound filter for VPNv4 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "prefix-list-out-vpnv6": {
            "type": "string",
            "help": "Outbound filter for VPNv6 updates to this neighbor.",
            "default": "",
            "max_length": 35,
        },
        "remote-as": {
            "type": "user",
            "help": "AS number of neighbor.",
            "required": True,
            "default": "",
        },
        "remote-as-filter": {
            "type": "string",
            "help": "BGP filter for remote AS.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "local-as": {
            "type": "user",
            "help": "Local AS number of neighbor.",
            "default": "",
        },
        "local-as-no-prepend": {
            "type": "option",
            "help": "Do not prepend local-as to incoming updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "local-as-replace-as": {
            "type": "option",
            "help": "Replace real AS with local-as in outgoing updates.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "retain-stale-time": {
            "type": "integer",
            "help": "Time to retain stale routes.",
            "default": 0,
            "min_value": 0,
            "max_value": 65535,
        },
        "route-map-in": {
            "type": "string",
            "help": "IPv4 Inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in6": {
            "type": "string",
            "help": "IPv6 Inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in-vpnv4": {
            "type": "string",
            "help": "VPNv4 inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in-vpnv6": {
            "type": "string",
            "help": "VPNv6 inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-in-evpn": {
            "type": "string",
            "help": "L2VPN EVPN inbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out": {
            "type": "string",
            "help": "IPv4 outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-preferable": {
            "type": "string",
            "help": "IPv4 outbound route map filter if the peer is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out6": {
            "type": "string",
            "help": "IPv6 Outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out6-preferable": {
            "type": "string",
            "help": "IPv6 outbound route map filter if the peer is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv4": {
            "type": "string",
            "help": "VPNv4 outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv6": {
            "type": "string",
            "help": "VPNv6 outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv4-preferable": {
            "type": "string",
            "help": "VPNv4 outbound route map filter if the peer is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-vpnv6-preferable": {
            "type": "string",
            "help": "VPNv6 outbound route map filter if this neighbor is preferred.",
            "default": "",
            "max_length": 35,
        },
        "route-map-out-evpn": {
            "type": "string",
            "help": "L2VPN EVPN outbound route map filter.",
            "default": "",
            "max_length": 35,
        },
        "send-community": {
            "type": "option",
            "help": "IPv4 Send community attribute to neighbor.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community6": {
            "type": "option",
            "help": "IPv6 Send community attribute to neighbor.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community-vpnv4": {
            "type": "option",
            "help": "Send community attribute to neighbor for VPNv4 address family.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community-vpnv6": {
            "type": "option",
            "help": "Enable/disable sending community attribute to this neighbor for VPNv6 address family.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "send-community-evpn": {
            "type": "option",
            "help": "Enable/disable sending community attribute to neighbor for L2VPN EVPN address family.",
            "default": "both",
            "options": [{"help": "Standard.", "label": "Standard", "name": "standard"}, {"help": "Extended.", "label": "Extended", "name": "extended"}, {"help": "Both.", "label": "Both", "name": "both"}, {"help": "Disable", "label": "Disable", "name": "disable"}],
        },
        "keep-alive-timer": {
            "type": "integer",
            "help": "Keep alive timer interval (sec).",
            "default": 4294967295,
            "min_value": 0,
            "max_value": 65535,
        },
        "holdtime-timer": {
            "type": "integer",
            "help": "Interval (sec) before peer considered dead.",
            "default": 4294967295,
            "min_value": 3,
            "max_value": 65535,
        },
        "connect-timer": {
            "type": "integer",
            "help": "Interval (sec) for connect timer.",
            "default": 4294967295,
            "min_value": 1,
            "max_value": 65535,
        },
        "unsuppress-map": {
            "type": "string",
            "help": "IPv4 Route map to selectively unsuppress suppressed routes.",
            "default": "",
            "max_length": 35,
        },
        "unsuppress-map6": {
            "type": "string",
            "help": "IPv6 Route map to selectively unsuppress suppressed routes.",
            "default": "",
            "max_length": 35,
        },
        "update-source": {
            "type": "string",
            "help": "Interface to use as source IP/IPv6 address of TCP connections.",
            "default": "",
            "max_length": 15,
        },
        "weight": {
            "type": "integer",
            "help": "Neighbor weight.",
            "default": 4294967295,
            "min_value": 0,
            "max_value": 65535,
        },
        "restart-time": {
            "type": "integer",
            "help": "Graceful restart delay time (sec, 0 = global default).",
            "default": 0,
            "min_value": 0,
            "max_value": 3600,
        },
        "additional-path": {
            "type": "option",
            "help": "Enable/disable IPv4 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "additional-path6": {
            "type": "option",
            "help": "Enable/disable IPv6 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "additional-path-vpnv4": {
            "type": "option",
            "help": "Enable/disable VPNv4 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "additional-path-vpnv6": {
            "type": "option",
            "help": "Enable/disable VPNv6 additional-path capability.",
            "default": "disable",
            "options": [{"help": "Enable sending additional paths.", "label": "Send", "name": "send"}, {"help": "Enable receiving additional paths.", "label": "Receive", "name": "receive"}, {"help": "Enable sending and receiving additional paths.", "label": "Both", "name": "both"}, {"help": "Disable additional paths.", "label": "Disable", "name": "disable"}],
        },
        "adv-additional-path": {
            "type": "integer",
            "help": "Number of IPv4 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "adv-additional-path6": {
            "type": "integer",
            "help": "Number of IPv6 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "adv-additional-path-vpnv4": {
            "type": "integer",
            "help": "Number of VPNv4 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "adv-additional-path-vpnv6": {
            "type": "integer",
            "help": "Number of VPNv6 additional paths that can be advertised to this neighbor.",
            "default": 2,
            "min_value": 2,
            "max_value": 255,
        },
        "password": {
            "type": "password",
            "help": "Password used in MD5 authentication.",
            "max_length": 128,
        },
        "auth-options": {
            "type": "string",
            "help": "Key-chain name for TCP authentication options.",
            "default": "",
            "max_length": 35,
        },
    },
    "neighbor-range": {
        "id": {
            "type": "integer",
            "help": "Neighbor range ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Neighbor range prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "max-neighbor-num": {
            "type": "integer",
            "help": "Maximum number of neighbors.",
            "default": 0,
            "min_value": 1,
            "max_value": 1000,
        },
        "neighbor-group": {
            "type": "string",
            "help": "Neighbor group name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
    },
    "neighbor-range6": {
        "id": {
            "type": "integer",
            "help": "IPv6 neighbor range ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix6": {
            "type": "ipv6-network",
            "help": "IPv6 prefix.",
            "required": True,
            "default": "::/0",
        },
        "max-neighbor-num": {
            "type": "integer",
            "help": "Maximum number of neighbors.",
            "default": 0,
            "min_value": 1,
            "max_value": 1000,
        },
        "neighbor-group": {
            "type": "string",
            "help": "Neighbor group name.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
    },
    "network": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix": {
            "type": "ipv4-classnet",
            "help": "Network prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "network-import-check": {
            "type": "option",
            "help": "Configure insurance of BGP network route existence in IGP.",
            "default": "global",
            "options": [{"help": "Use global network sync value.", "label": "Global", "name": "global"}, {"help": "Enable network sync per prefix.", "label": "Enable", "name": "enable"}, {"help": "Disable network sync per prefix.", "label": "Disable", "name": "disable"}],
        },
        "backdoor": {
            "type": "option",
            "help": "Enable/disable route as backdoor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-map": {
            "type": "string",
            "help": "Route map to modify generated route.",
            "default": "",
            "max_length": 35,
        },
        "prefix-name": {
            "type": "string",
            "help": "Name of firewall address or address group.",
            "default": "",
            "max_length": 79,
        },
    },
    "network6": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "prefix6": {
            "type": "ipv6-network",
            "help": "Network IPv6 prefix.",
            "required": True,
            "default": "::/0",
        },
        "network-import-check": {
            "type": "option",
            "help": "Configure insurance of BGP network route existence in IGP.",
            "default": "global",
            "options": [{"help": "Use global network sync value.", "label": "Global", "name": "global"}, {"help": "Enable network sync per prefix.", "label": "Enable", "name": "enable"}, {"help": "Disable network sync per prefix.", "label": "Disable", "name": "disable"}],
        },
        "backdoor": {
            "type": "option",
            "help": "Enable/disable route as backdoor.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-map": {
            "type": "string",
            "help": "Route map to modify generated route.",
            "default": "",
            "max_length": 35,
        },
    },
    "redistribute": {
        "name": {
            "type": "string",
            "help": "Distribute list entry name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-map": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
    "redistribute6": {
        "name": {
            "type": "string",
            "help": "Distribute list entry name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
        "status": {
            "type": "option",
            "help": "Status.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "route-map": {
            "type": "string",
            "help": "Route map name.",
            "default": "",
            "max_length": 35,
        },
    },
    "admin-distance": {
        "id": {
            "type": "integer",
            "help": "ID.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "neighbour-prefix": {
            "type": "ipv4-classnet",
            "help": "Neighbor address prefix.",
            "required": True,
            "default": "0.0.0.0 0.0.0.0",
        },
        "route-list": {
            "type": "string",
            "help": "Access list of routes to apply new distance to.",
            "default": "",
            "max_length": 35,
        },
        "distance": {
            "type": "integer",
            "help": "Administrative distance to apply (1 - 255).",
            "required": True,
            "default": 0,
            "min_value": 1,
            "max_value": 255,
        },
    },
    "vrf": {
        "vrf": {
            "type": "string",
            "help": "Origin VRF ID <0-511>.",
            "default": "",
            "max_length": 7,
        },
        "role": {
            "type": "option",
            "help": "VRF role.",
            "default": "standalone",
            "options": [{"help": "Stand-alone VRF.", "label": "Standalone", "name": "standalone"}, {"help": "CE VRF.", "label": "Ce", "name": "ce"}, {"help": "PE VRF.", "label": "Pe", "name": "pe"}],
        },
        "rd": {
            "type": "string",
            "help": "Route Distinguisher: AA:NN|A.B.C.D:NN.",
            "default": "",
            "max_length": 79,
        },
        "export-rt": {
            "type": "string",
            "help": "List of export route target.",
        },
        "import-rt": {
            "type": "string",
            "help": "List of import route target.",
        },
        "import-route-map": {
            "type": "string",
            "help": "Import route map.",
            "default": "",
            "max_length": 35,
        },
        "leak-target": {
            "type": "string",
            "help": "Target VRF table.",
        },
    },
    "vrf6": {
        "vrf": {
            "type": "string",
            "help": "Origin VRF ID <0-511>.",
            "default": "",
            "max_length": 7,
        },
        "role": {
            "type": "option",
            "help": "VRF role.",
            "default": "standalone",
            "options": [{"help": "Stand-alone VRF.", "label": "Standalone", "name": "standalone"}, {"help": "CE VRF.", "label": "Ce", "name": "ce"}, {"help": "PE VRF.", "label": "Pe", "name": "pe"}],
        },
        "rd": {
            "type": "string",
            "help": "Route Distinguisher: AA:NN|A.B.C.D:NN.",
            "default": "",
            "max_length": 79,
        },
        "export-rt": {
            "type": "string",
            "help": "List of export route target.",
        },
        "import-rt": {
            "type": "string",
            "help": "List of import route target.",
        },
        "import-route-map": {
            "type": "string",
            "help": "Import route map.",
            "default": "",
            "max_length": 35,
        },
        "leak-target": {
            "type": "string",
            "help": "Target VRF table.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_ALWAYS_COMPARE_MED = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BESTPATH_AS_PATH_IGNORE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BESTPATH_CMP_CONFED_ASPATH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BESTPATH_CMP_ROUTERID = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BESTPATH_MED_CONFED = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_BESTPATH_MED_MISSING_AS_WORST = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_CLIENT_TO_CLIENT_REFLECTION = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DAMPENING = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_DETERMINISTIC_MED = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EBGP_MULTIPATH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_IBGP_MULTIPATH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ENFORCE_FIRST_AS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_FAST_EXTERNAL_FAILOVER = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOG_NEIGHBOUR_CHANGES = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_NETWORK_IMPORT_CHECK = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_IGNORE_OPTIONAL_CAPABILITY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ADDITIONAL_PATH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ADDITIONAL_PATH6 = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ADDITIONAL_PATH_VPNV4 = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_ADDITIONAL_PATH_VPNV6 = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_RECURSIVE_NEXT_HOP = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_RECURSIVE_INHERIT_PRIORITY = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_TAG_RESOLVE_MODE = [
    "disable",  # Disable tag-match mode.
    "preferred",  # Use tag-match if a BGP route resolution with another route containing the same tag is successful.
    "merge",  # Merge tag-match with best-match if they are using different routes. The result will exclude the next hops of tag-match whose interfaces or child interfaces have appeared in best-match.
    "merge-all",  # Merge tag-match with best-match if they are using different routes. The result will exclude the next hops of tag-match whose interfaces have appeared in best-match.
]
VALID_BODY_SYNCHRONIZATION = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_GRACEFUL_RESTART = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_GRACEFUL_END_ON_TIMER = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_router_bgp_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for router/bgp."""
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
    """Validate required fields for router/bgp."""
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


def validate_router_bgp_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new router/bgp object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "always-compare-med" in payload:
        value = payload["always-compare-med"]
        if value not in VALID_BODY_ALWAYS_COMPARE_MED:
            desc = FIELD_DESCRIPTIONS.get("always-compare-med", "")
            error_msg = f"Invalid value for 'always-compare-med': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ALWAYS_COMPARE_MED)}"
            error_msg += f"\n  → Example: always-compare-med='{{ VALID_BODY_ALWAYS_COMPARE_MED[0] }}'"
            return (False, error_msg)
    if "bestpath-as-path-ignore" in payload:
        value = payload["bestpath-as-path-ignore"]
        if value not in VALID_BODY_BESTPATH_AS_PATH_IGNORE:
            desc = FIELD_DESCRIPTIONS.get("bestpath-as-path-ignore", "")
            error_msg = f"Invalid value for 'bestpath-as-path-ignore': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BESTPATH_AS_PATH_IGNORE)}"
            error_msg += f"\n  → Example: bestpath-as-path-ignore='{{ VALID_BODY_BESTPATH_AS_PATH_IGNORE[0] }}'"
            return (False, error_msg)
    if "bestpath-cmp-confed-aspath" in payload:
        value = payload["bestpath-cmp-confed-aspath"]
        if value not in VALID_BODY_BESTPATH_CMP_CONFED_ASPATH:
            desc = FIELD_DESCRIPTIONS.get("bestpath-cmp-confed-aspath", "")
            error_msg = f"Invalid value for 'bestpath-cmp-confed-aspath': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BESTPATH_CMP_CONFED_ASPATH)}"
            error_msg += f"\n  → Example: bestpath-cmp-confed-aspath='{{ VALID_BODY_BESTPATH_CMP_CONFED_ASPATH[0] }}'"
            return (False, error_msg)
    if "bestpath-cmp-routerid" in payload:
        value = payload["bestpath-cmp-routerid"]
        if value not in VALID_BODY_BESTPATH_CMP_ROUTERID:
            desc = FIELD_DESCRIPTIONS.get("bestpath-cmp-routerid", "")
            error_msg = f"Invalid value for 'bestpath-cmp-routerid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BESTPATH_CMP_ROUTERID)}"
            error_msg += f"\n  → Example: bestpath-cmp-routerid='{{ VALID_BODY_BESTPATH_CMP_ROUTERID[0] }}'"
            return (False, error_msg)
    if "bestpath-med-confed" in payload:
        value = payload["bestpath-med-confed"]
        if value not in VALID_BODY_BESTPATH_MED_CONFED:
            desc = FIELD_DESCRIPTIONS.get("bestpath-med-confed", "")
            error_msg = f"Invalid value for 'bestpath-med-confed': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BESTPATH_MED_CONFED)}"
            error_msg += f"\n  → Example: bestpath-med-confed='{{ VALID_BODY_BESTPATH_MED_CONFED[0] }}'"
            return (False, error_msg)
    if "bestpath-med-missing-as-worst" in payload:
        value = payload["bestpath-med-missing-as-worst"]
        if value not in VALID_BODY_BESTPATH_MED_MISSING_AS_WORST:
            desc = FIELD_DESCRIPTIONS.get("bestpath-med-missing-as-worst", "")
            error_msg = f"Invalid value for 'bestpath-med-missing-as-worst': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BESTPATH_MED_MISSING_AS_WORST)}"
            error_msg += f"\n  → Example: bestpath-med-missing-as-worst='{{ VALID_BODY_BESTPATH_MED_MISSING_AS_WORST[0] }}'"
            return (False, error_msg)
    if "client-to-client-reflection" in payload:
        value = payload["client-to-client-reflection"]
        if value not in VALID_BODY_CLIENT_TO_CLIENT_REFLECTION:
            desc = FIELD_DESCRIPTIONS.get("client-to-client-reflection", "")
            error_msg = f"Invalid value for 'client-to-client-reflection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_TO_CLIENT_REFLECTION)}"
            error_msg += f"\n  → Example: client-to-client-reflection='{{ VALID_BODY_CLIENT_TO_CLIENT_REFLECTION[0] }}'"
            return (False, error_msg)
    if "dampening" in payload:
        value = payload["dampening"]
        if value not in VALID_BODY_DAMPENING:
            desc = FIELD_DESCRIPTIONS.get("dampening", "")
            error_msg = f"Invalid value for 'dampening': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DAMPENING)}"
            error_msg += f"\n  → Example: dampening='{{ VALID_BODY_DAMPENING[0] }}'"
            return (False, error_msg)
    if "deterministic-med" in payload:
        value = payload["deterministic-med"]
        if value not in VALID_BODY_DETERMINISTIC_MED:
            desc = FIELD_DESCRIPTIONS.get("deterministic-med", "")
            error_msg = f"Invalid value for 'deterministic-med': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DETERMINISTIC_MED)}"
            error_msg += f"\n  → Example: deterministic-med='{{ VALID_BODY_DETERMINISTIC_MED[0] }}'"
            return (False, error_msg)
    if "ebgp-multipath" in payload:
        value = payload["ebgp-multipath"]
        if value not in VALID_BODY_EBGP_MULTIPATH:
            desc = FIELD_DESCRIPTIONS.get("ebgp-multipath", "")
            error_msg = f"Invalid value for 'ebgp-multipath': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EBGP_MULTIPATH)}"
            error_msg += f"\n  → Example: ebgp-multipath='{{ VALID_BODY_EBGP_MULTIPATH[0] }}'"
            return (False, error_msg)
    if "ibgp-multipath" in payload:
        value = payload["ibgp-multipath"]
        if value not in VALID_BODY_IBGP_MULTIPATH:
            desc = FIELD_DESCRIPTIONS.get("ibgp-multipath", "")
            error_msg = f"Invalid value for 'ibgp-multipath': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IBGP_MULTIPATH)}"
            error_msg += f"\n  → Example: ibgp-multipath='{{ VALID_BODY_IBGP_MULTIPATH[0] }}'"
            return (False, error_msg)
    if "enforce-first-as" in payload:
        value = payload["enforce-first-as"]
        if value not in VALID_BODY_ENFORCE_FIRST_AS:
            desc = FIELD_DESCRIPTIONS.get("enforce-first-as", "")
            error_msg = f"Invalid value for 'enforce-first-as': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_FIRST_AS)}"
            error_msg += f"\n  → Example: enforce-first-as='{{ VALID_BODY_ENFORCE_FIRST_AS[0] }}'"
            return (False, error_msg)
    if "fast-external-failover" in payload:
        value = payload["fast-external-failover"]
        if value not in VALID_BODY_FAST_EXTERNAL_FAILOVER:
            desc = FIELD_DESCRIPTIONS.get("fast-external-failover", "")
            error_msg = f"Invalid value for 'fast-external-failover': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAST_EXTERNAL_FAILOVER)}"
            error_msg += f"\n  → Example: fast-external-failover='{{ VALID_BODY_FAST_EXTERNAL_FAILOVER[0] }}'"
            return (False, error_msg)
    if "log-neighbour-changes" in payload:
        value = payload["log-neighbour-changes"]
        if value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            desc = FIELD_DESCRIPTIONS.get("log-neighbour-changes", "")
            error_msg = f"Invalid value for 'log-neighbour-changes': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_NEIGHBOUR_CHANGES)}"
            error_msg += f"\n  → Example: log-neighbour-changes='{{ VALID_BODY_LOG_NEIGHBOUR_CHANGES[0] }}'"
            return (False, error_msg)
    if "network-import-check" in payload:
        value = payload["network-import-check"]
        if value not in VALID_BODY_NETWORK_IMPORT_CHECK:
            desc = FIELD_DESCRIPTIONS.get("network-import-check", "")
            error_msg = f"Invalid value for 'network-import-check': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NETWORK_IMPORT_CHECK)}"
            error_msg += f"\n  → Example: network-import-check='{{ VALID_BODY_NETWORK_IMPORT_CHECK[0] }}'"
            return (False, error_msg)
    if "ignore-optional-capability" in payload:
        value = payload["ignore-optional-capability"]
        if value not in VALID_BODY_IGNORE_OPTIONAL_CAPABILITY:
            desc = FIELD_DESCRIPTIONS.get("ignore-optional-capability", "")
            error_msg = f"Invalid value for 'ignore-optional-capability': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_IGNORE_OPTIONAL_CAPABILITY)}"
            error_msg += f"\n  → Example: ignore-optional-capability='{{ VALID_BODY_IGNORE_OPTIONAL_CAPABILITY[0] }}'"
            return (False, error_msg)
    if "additional-path" in payload:
        value = payload["additional-path"]
        if value not in VALID_BODY_ADDITIONAL_PATH:
            desc = FIELD_DESCRIPTIONS.get("additional-path", "")
            error_msg = f"Invalid value for 'additional-path': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDITIONAL_PATH)}"
            error_msg += f"\n  → Example: additional-path='{{ VALID_BODY_ADDITIONAL_PATH[0] }}'"
            return (False, error_msg)
    if "additional-path6" in payload:
        value = payload["additional-path6"]
        if value not in VALID_BODY_ADDITIONAL_PATH6:
            desc = FIELD_DESCRIPTIONS.get("additional-path6", "")
            error_msg = f"Invalid value for 'additional-path6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDITIONAL_PATH6)}"
            error_msg += f"\n  → Example: additional-path6='{{ VALID_BODY_ADDITIONAL_PATH6[0] }}'"
            return (False, error_msg)
    if "additional-path-vpnv4" in payload:
        value = payload["additional-path-vpnv4"]
        if value not in VALID_BODY_ADDITIONAL_PATH_VPNV4:
            desc = FIELD_DESCRIPTIONS.get("additional-path-vpnv4", "")
            error_msg = f"Invalid value for 'additional-path-vpnv4': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDITIONAL_PATH_VPNV4)}"
            error_msg += f"\n  → Example: additional-path-vpnv4='{{ VALID_BODY_ADDITIONAL_PATH_VPNV4[0] }}'"
            return (False, error_msg)
    if "additional-path-vpnv6" in payload:
        value = payload["additional-path-vpnv6"]
        if value not in VALID_BODY_ADDITIONAL_PATH_VPNV6:
            desc = FIELD_DESCRIPTIONS.get("additional-path-vpnv6", "")
            error_msg = f"Invalid value for 'additional-path-vpnv6': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADDITIONAL_PATH_VPNV6)}"
            error_msg += f"\n  → Example: additional-path-vpnv6='{{ VALID_BODY_ADDITIONAL_PATH_VPNV6[0] }}'"
            return (False, error_msg)
    if "multipath-recursive-distance" in payload:
        value = payload["multipath-recursive-distance"]
        if value not in VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE:
            desc = FIELD_DESCRIPTIONS.get("multipath-recursive-distance", "")
            error_msg = f"Invalid value for 'multipath-recursive-distance': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE)}"
            error_msg += f"\n  → Example: multipath-recursive-distance='{{ VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE[0] }}'"
            return (False, error_msg)
    if "recursive-next-hop" in payload:
        value = payload["recursive-next-hop"]
        if value not in VALID_BODY_RECURSIVE_NEXT_HOP:
            desc = FIELD_DESCRIPTIONS.get("recursive-next-hop", "")
            error_msg = f"Invalid value for 'recursive-next-hop': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RECURSIVE_NEXT_HOP)}"
            error_msg += f"\n  → Example: recursive-next-hop='{{ VALID_BODY_RECURSIVE_NEXT_HOP[0] }}'"
            return (False, error_msg)
    if "recursive-inherit-priority" in payload:
        value = payload["recursive-inherit-priority"]
        if value not in VALID_BODY_RECURSIVE_INHERIT_PRIORITY:
            desc = FIELD_DESCRIPTIONS.get("recursive-inherit-priority", "")
            error_msg = f"Invalid value for 'recursive-inherit-priority': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RECURSIVE_INHERIT_PRIORITY)}"
            error_msg += f"\n  → Example: recursive-inherit-priority='{{ VALID_BODY_RECURSIVE_INHERIT_PRIORITY[0] }}'"
            return (False, error_msg)
    if "tag-resolve-mode" in payload:
        value = payload["tag-resolve-mode"]
        if value not in VALID_BODY_TAG_RESOLVE_MODE:
            desc = FIELD_DESCRIPTIONS.get("tag-resolve-mode", "")
            error_msg = f"Invalid value for 'tag-resolve-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TAG_RESOLVE_MODE)}"
            error_msg += f"\n  → Example: tag-resolve-mode='{{ VALID_BODY_TAG_RESOLVE_MODE[0] }}'"
            return (False, error_msg)
    if "synchronization" in payload:
        value = payload["synchronization"]
        if value not in VALID_BODY_SYNCHRONIZATION:
            desc = FIELD_DESCRIPTIONS.get("synchronization", "")
            error_msg = f"Invalid value for 'synchronization': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYNCHRONIZATION)}"
            error_msg += f"\n  → Example: synchronization='{{ VALID_BODY_SYNCHRONIZATION[0] }}'"
            return (False, error_msg)
    if "graceful-restart" in payload:
        value = payload["graceful-restart"]
        if value not in VALID_BODY_GRACEFUL_RESTART:
            desc = FIELD_DESCRIPTIONS.get("graceful-restart", "")
            error_msg = f"Invalid value for 'graceful-restart': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GRACEFUL_RESTART)}"
            error_msg += f"\n  → Example: graceful-restart='{{ VALID_BODY_GRACEFUL_RESTART[0] }}'"
            return (False, error_msg)
    if "graceful-end-on-timer" in payload:
        value = payload["graceful-end-on-timer"]
        if value not in VALID_BODY_GRACEFUL_END_ON_TIMER:
            desc = FIELD_DESCRIPTIONS.get("graceful-end-on-timer", "")
            error_msg = f"Invalid value for 'graceful-end-on-timer': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GRACEFUL_END_ON_TIMER)}"
            error_msg += f"\n  → Example: graceful-end-on-timer='{{ VALID_BODY_GRACEFUL_END_ON_TIMER[0] }}'"
            return (False, error_msg)
    if "cross-family-conditional-adv" in payload:
        value = payload["cross-family-conditional-adv"]
        if value not in VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV:
            desc = FIELD_DESCRIPTIONS.get("cross-family-conditional-adv", "")
            error_msg = f"Invalid value for 'cross-family-conditional-adv': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV)}"
            error_msg += f"\n  → Example: cross-family-conditional-adv='{{ VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_router_bgp_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update router/bgp."""
    # Step 1: Validate enum values
    if "always-compare-med" in payload:
        value = payload["always-compare-med"]
        if value not in VALID_BODY_ALWAYS_COMPARE_MED:
            return (
                False,
                f"Invalid value for 'always-compare-med'='{value}'. Must be one of: {', '.join(VALID_BODY_ALWAYS_COMPARE_MED)}",
            )
    if "bestpath-as-path-ignore" in payload:
        value = payload["bestpath-as-path-ignore"]
        if value not in VALID_BODY_BESTPATH_AS_PATH_IGNORE:
            return (
                False,
                f"Invalid value for 'bestpath-as-path-ignore'='{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_AS_PATH_IGNORE)}",
            )
    if "bestpath-cmp-confed-aspath" in payload:
        value = payload["bestpath-cmp-confed-aspath"]
        if value not in VALID_BODY_BESTPATH_CMP_CONFED_ASPATH:
            return (
                False,
                f"Invalid value for 'bestpath-cmp-confed-aspath'='{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_CMP_CONFED_ASPATH)}",
            )
    if "bestpath-cmp-routerid" in payload:
        value = payload["bestpath-cmp-routerid"]
        if value not in VALID_BODY_BESTPATH_CMP_ROUTERID:
            return (
                False,
                f"Invalid value for 'bestpath-cmp-routerid'='{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_CMP_ROUTERID)}",
            )
    if "bestpath-med-confed" in payload:
        value = payload["bestpath-med-confed"]
        if value not in VALID_BODY_BESTPATH_MED_CONFED:
            return (
                False,
                f"Invalid value for 'bestpath-med-confed'='{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_MED_CONFED)}",
            )
    if "bestpath-med-missing-as-worst" in payload:
        value = payload["bestpath-med-missing-as-worst"]
        if value not in VALID_BODY_BESTPATH_MED_MISSING_AS_WORST:
            return (
                False,
                f"Invalid value for 'bestpath-med-missing-as-worst'='{value}'. Must be one of: {', '.join(VALID_BODY_BESTPATH_MED_MISSING_AS_WORST)}",
            )
    if "client-to-client-reflection" in payload:
        value = payload["client-to-client-reflection"]
        if value not in VALID_BODY_CLIENT_TO_CLIENT_REFLECTION:
            return (
                False,
                f"Invalid value for 'client-to-client-reflection'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_TO_CLIENT_REFLECTION)}",
            )
    if "dampening" in payload:
        value = payload["dampening"]
        if value not in VALID_BODY_DAMPENING:
            return (
                False,
                f"Invalid value for 'dampening'='{value}'. Must be one of: {', '.join(VALID_BODY_DAMPENING)}",
            )
    if "deterministic-med" in payload:
        value = payload["deterministic-med"]
        if value not in VALID_BODY_DETERMINISTIC_MED:
            return (
                False,
                f"Invalid value for 'deterministic-med'='{value}'. Must be one of: {', '.join(VALID_BODY_DETERMINISTIC_MED)}",
            )
    if "ebgp-multipath" in payload:
        value = payload["ebgp-multipath"]
        if value not in VALID_BODY_EBGP_MULTIPATH:
            return (
                False,
                f"Invalid value for 'ebgp-multipath'='{value}'. Must be one of: {', '.join(VALID_BODY_EBGP_MULTIPATH)}",
            )
    if "ibgp-multipath" in payload:
        value = payload["ibgp-multipath"]
        if value not in VALID_BODY_IBGP_MULTIPATH:
            return (
                False,
                f"Invalid value for 'ibgp-multipath'='{value}'. Must be one of: {', '.join(VALID_BODY_IBGP_MULTIPATH)}",
            )
    if "enforce-first-as" in payload:
        value = payload["enforce-first-as"]
        if value not in VALID_BODY_ENFORCE_FIRST_AS:
            return (
                False,
                f"Invalid value for 'enforce-first-as'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_FIRST_AS)}",
            )
    if "fast-external-failover" in payload:
        value = payload["fast-external-failover"]
        if value not in VALID_BODY_FAST_EXTERNAL_FAILOVER:
            return (
                False,
                f"Invalid value for 'fast-external-failover'='{value}'. Must be one of: {', '.join(VALID_BODY_FAST_EXTERNAL_FAILOVER)}",
            )
    if "log-neighbour-changes" in payload:
        value = payload["log-neighbour-changes"]
        if value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            return (
                False,
                f"Invalid value for 'log-neighbour-changes'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_NEIGHBOUR_CHANGES)}",
            )
    if "network-import-check" in payload:
        value = payload["network-import-check"]
        if value not in VALID_BODY_NETWORK_IMPORT_CHECK:
            return (
                False,
                f"Invalid value for 'network-import-check'='{value}'. Must be one of: {', '.join(VALID_BODY_NETWORK_IMPORT_CHECK)}",
            )
    if "ignore-optional-capability" in payload:
        value = payload["ignore-optional-capability"]
        if value not in VALID_BODY_IGNORE_OPTIONAL_CAPABILITY:
            return (
                False,
                f"Invalid value for 'ignore-optional-capability'='{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_OPTIONAL_CAPABILITY)}",
            )
    if "additional-path" in payload:
        value = payload["additional-path"]
        if value not in VALID_BODY_ADDITIONAL_PATH:
            return (
                False,
                f"Invalid value for 'additional-path'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH)}",
            )
    if "additional-path6" in payload:
        value = payload["additional-path6"]
        if value not in VALID_BODY_ADDITIONAL_PATH6:
            return (
                False,
                f"Invalid value for 'additional-path6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH6)}",
            )
    if "additional-path-vpnv4" in payload:
        value = payload["additional-path-vpnv4"]
        if value not in VALID_BODY_ADDITIONAL_PATH_VPNV4:
            return (
                False,
                f"Invalid value for 'additional-path-vpnv4'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH_VPNV4)}",
            )
    if "additional-path-vpnv6" in payload:
        value = payload["additional-path-vpnv6"]
        if value not in VALID_BODY_ADDITIONAL_PATH_VPNV6:
            return (
                False,
                f"Invalid value for 'additional-path-vpnv6'='{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_PATH_VPNV6)}",
            )
    if "multipath-recursive-distance" in payload:
        value = payload["multipath-recursive-distance"]
        if value not in VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE:
            return (
                False,
                f"Invalid value for 'multipath-recursive-distance'='{value}'. Must be one of: {', '.join(VALID_BODY_MULTIPATH_RECURSIVE_DISTANCE)}",
            )
    if "recursive-next-hop" in payload:
        value = payload["recursive-next-hop"]
        if value not in VALID_BODY_RECURSIVE_NEXT_HOP:
            return (
                False,
                f"Invalid value for 'recursive-next-hop'='{value}'. Must be one of: {', '.join(VALID_BODY_RECURSIVE_NEXT_HOP)}",
            )
    if "recursive-inherit-priority" in payload:
        value = payload["recursive-inherit-priority"]
        if value not in VALID_BODY_RECURSIVE_INHERIT_PRIORITY:
            return (
                False,
                f"Invalid value for 'recursive-inherit-priority'='{value}'. Must be one of: {', '.join(VALID_BODY_RECURSIVE_INHERIT_PRIORITY)}",
            )
    if "tag-resolve-mode" in payload:
        value = payload["tag-resolve-mode"]
        if value not in VALID_BODY_TAG_RESOLVE_MODE:
            return (
                False,
                f"Invalid value for 'tag-resolve-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_TAG_RESOLVE_MODE)}",
            )
    if "synchronization" in payload:
        value = payload["synchronization"]
        if value not in VALID_BODY_SYNCHRONIZATION:
            return (
                False,
                f"Invalid value for 'synchronization'='{value}'. Must be one of: {', '.join(VALID_BODY_SYNCHRONIZATION)}",
            )
    if "graceful-restart" in payload:
        value = payload["graceful-restart"]
        if value not in VALID_BODY_GRACEFUL_RESTART:
            return (
                False,
                f"Invalid value for 'graceful-restart'='{value}'. Must be one of: {', '.join(VALID_BODY_GRACEFUL_RESTART)}",
            )
    if "graceful-end-on-timer" in payload:
        value = payload["graceful-end-on-timer"]
        if value not in VALID_BODY_GRACEFUL_END_ON_TIMER:
            return (
                False,
                f"Invalid value for 'graceful-end-on-timer'='{value}'. Must be one of: {', '.join(VALID_BODY_GRACEFUL_END_ON_TIMER)}",
            )
    if "cross-family-conditional-adv" in payload:
        value = payload["cross-family-conditional-adv"]
        if value not in VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV:
            return (
                False,
                f"Invalid value for 'cross-family-conditional-adv'='{value}'. Must be one of: {', '.join(VALID_BODY_CROSS_FAMILY_CONDITIONAL_ADV)}",
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
    "endpoint": "router/bgp",
    "category": "cmdb",
    "api_path": "router/bgp",
    "help": "Configure BGP.",
    "total_fields": 66,
    "required_fields_count": 1,
    "fields_with_defaults_count": 52,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
