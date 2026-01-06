"""Validation helpers for firewall/security_policy - Auto-generated"""

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
    "srcintf",  # Incoming (ingress) interface.
    "dstintf",  # Outgoing (egress) interface.
    "schedule",  # Schedule name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "uuid": "00000000-0000-0000-0000-000000000000",
    "policyid": 0,
    "name": "",
    "srcaddr-negate": "disable",
    "dstaddr-negate": "disable",
    "srcaddr6-negate": "disable",
    "dstaddr6-negate": "disable",
    "internet-service": "disable",
    "internet-service-negate": "disable",
    "internet-service-src": "disable",
    "internet-service-src-negate": "disable",
    "internet-service6": "disable",
    "internet-service6-negate": "disable",
    "internet-service6-src": "disable",
    "internet-service6-src-negate": "disable",
    "enforce-default-app-port": "enable",
    "service-negate": "disable",
    "action": "deny",
    "send-deny-packet": "disable",
    "schedule": "",
    "status": "enable",
    "logtraffic": "utm",
    "learning-mode": "disable",
    "nat46": "disable",
    "nat64": "disable",
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
    "ssh-filter-profile": "",
    "casb-profile": "",
    "url-category": "",
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
    "uuid": "uuid",  # Universally Unique Identifier (UUID; automatically assigned 
    "policyid": "integer",  # Policy ID.
    "name": "string",  # Policy name.
    "comments": "var-string",  # Comment.
    "srcintf": "string",  # Incoming (ingress) interface.
    "dstintf": "string",  # Outgoing (egress) interface.
    "srcaddr": "string",  # Source IPv4 address name and address group names.
    "srcaddr-negate": "option",  # When enabled srcaddr specifies what the source address must 
    "dstaddr": "string",  # Destination IPv4 address name and address group names.
    "dstaddr-negate": "option",  # When enabled dstaddr specifies what the destination address 
    "srcaddr6": "string",  # Source IPv6 address name and address group names.
    "srcaddr6-negate": "option",  # When enabled srcaddr6 specifies what the source address must
    "dstaddr6": "string",  # Destination IPv6 address name and address group names.
    "dstaddr6-negate": "option",  # When enabled dstaddr6 specifies what the destination address
    "internet-service": "option",  # Enable/disable use of Internet Services for this policy. If 
    "internet-service-name": "string",  # Internet Service name.
    "internet-service-negate": "option",  # When enabled internet-service specifies what the service mus
    "internet-service-group": "string",  # Internet Service group name.
    "internet-service-custom": "string",  # Custom Internet Service name.
    "internet-service-custom-group": "string",  # Custom Internet Service group name.
    "internet-service-fortiguard": "string",  # FortiGuard Internet Service name.
    "internet-service-src": "option",  # Enable/disable use of Internet Services in source for this p
    "internet-service-src-name": "string",  # Internet Service source name.
    "internet-service-src-negate": "option",  # When enabled internet-service-src specifies what the service
    "internet-service-src-group": "string",  # Internet Service source group name.
    "internet-service-src-custom": "string",  # Custom Internet Service source name.
    "internet-service-src-custom-group": "string",  # Custom Internet Service source group name.
    "internet-service-src-fortiguard": "string",  # FortiGuard Internet Service source name.
    "internet-service6": "option",  # Enable/disable use of IPv6 Internet Services for this policy
    "internet-service6-name": "string",  # IPv6 Internet Service name.
    "internet-service6-negate": "option",  # When enabled internet-service6 specifies what the service mu
    "internet-service6-group": "string",  # Internet Service group name.
    "internet-service6-custom": "string",  # Custom IPv6 Internet Service name.
    "internet-service6-custom-group": "string",  # Custom IPv6 Internet Service group name.
    "internet-service6-fortiguard": "string",  # FortiGuard IPv6 Internet Service name.
    "internet-service6-src": "option",  # Enable/disable use of IPv6 Internet Services in source for t
    "internet-service6-src-name": "string",  # IPv6 Internet Service source name.
    "internet-service6-src-negate": "option",  # When enabled internet-service6-src specifies what the servic
    "internet-service6-src-group": "string",  # Internet Service6 source group name.
    "internet-service6-src-custom": "string",  # Custom IPv6 Internet Service source name.
    "internet-service6-src-custom-group": "string",  # Custom Internet Service6 source group name.
    "internet-service6-src-fortiguard": "string",  # FortiGuard IPv6 Internet Service source name.
    "enforce-default-app-port": "option",  # Enable/disable default application port enforcement for allo
    "service": "string",  # Service and service group names.
    "service-negate": "option",  # When enabled service specifies what the service must NOT be.
    "action": "option",  # Policy action (accept/deny).
    "send-deny-packet": "option",  # Enable to send a reply when a session is denied or blocked b
    "schedule": "string",  # Schedule name.
    "status": "option",  # Enable or disable this policy.
    "logtraffic": "option",  # Enable or disable logging. Log all sessions or security prof
    "learning-mode": "option",  # Enable to allow everything, but log all of the meaningful da
    "nat46": "option",  # Enable/disable NAT46.
    "nat64": "option",  # Enable/disable NAT64.
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
    "ssh-filter-profile": "string",  # Name of an existing SSH filter profile.
    "casb-profile": "string",  # Name of an existing CASB profile.
    "application": "string",  # Application ID list.
    "app-category": "string",  # Application category ID list.
    "url-category": "user",  # URL categories or groups.
    "app-group": "string",  # Application group names.
    "groups": "string",  # Names of user groups that can authenticate with this policy.
    "users": "string",  # Names of individual users that can authenticate with this po
    "fsso-groups": "string",  # Names of FSSO groups.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "policyid": "Policy ID.",
    "name": "Policy name.",
    "comments": "Comment.",
    "srcintf": "Incoming (ingress) interface.",
    "dstintf": "Outgoing (egress) interface.",
    "srcaddr": "Source IPv4 address name and address group names.",
    "srcaddr-negate": "When enabled srcaddr specifies what the source address must NOT be.",
    "dstaddr": "Destination IPv4 address name and address group names.",
    "dstaddr-negate": "When enabled dstaddr specifies what the destination address must NOT be.",
    "srcaddr6": "Source IPv6 address name and address group names.",
    "srcaddr6-negate": "When enabled srcaddr6 specifies what the source address must NOT be.",
    "dstaddr6": "Destination IPv6 address name and address group names.",
    "dstaddr6-negate": "When enabled dstaddr6 specifies what the destination address must NOT be.",
    "internet-service": "Enable/disable use of Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.",
    "internet-service-name": "Internet Service name.",
    "internet-service-negate": "When enabled internet-service specifies what the service must NOT be.",
    "internet-service-group": "Internet Service group name.",
    "internet-service-custom": "Custom Internet Service name.",
    "internet-service-custom-group": "Custom Internet Service group name.",
    "internet-service-fortiguard": "FortiGuard Internet Service name.",
    "internet-service-src": "Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.",
    "internet-service-src-name": "Internet Service source name.",
    "internet-service-src-negate": "When enabled internet-service-src specifies what the service must NOT be.",
    "internet-service-src-group": "Internet Service source group name.",
    "internet-service-src-custom": "Custom Internet Service source name.",
    "internet-service-src-custom-group": "Custom Internet Service source group name.",
    "internet-service-src-fortiguard": "FortiGuard Internet Service source name.",
    "internet-service6": "Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.",
    "internet-service6-name": "IPv6 Internet Service name.",
    "internet-service6-negate": "When enabled internet-service6 specifies what the service must NOT be.",
    "internet-service6-group": "Internet Service group name.",
    "internet-service6-custom": "Custom IPv6 Internet Service name.",
    "internet-service6-custom-group": "Custom IPv6 Internet Service group name.",
    "internet-service6-fortiguard": "FortiGuard IPv6 Internet Service name.",
    "internet-service6-src": "Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.",
    "internet-service6-src-name": "IPv6 Internet Service source name.",
    "internet-service6-src-negate": "When enabled internet-service6-src specifies what the service must NOT be.",
    "internet-service6-src-group": "Internet Service6 source group name.",
    "internet-service6-src-custom": "Custom IPv6 Internet Service source name.",
    "internet-service6-src-custom-group": "Custom Internet Service6 source group name.",
    "internet-service6-src-fortiguard": "FortiGuard IPv6 Internet Service source name.",
    "enforce-default-app-port": "Enable/disable default application port enforcement for allowed applications.",
    "service": "Service and service group names.",
    "service-negate": "When enabled service specifies what the service must NOT be.",
    "action": "Policy action (accept/deny).",
    "send-deny-packet": "Enable to send a reply when a session is denied or blocked by a firewall policy.",
    "schedule": "Schedule name.",
    "status": "Enable or disable this policy.",
    "logtraffic": "Enable or disable logging. Log all sessions or security profile sessions.",
    "learning-mode": "Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.",
    "nat46": "Enable/disable NAT46.",
    "nat64": "Enable/disable NAT64.",
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
    "ssh-filter-profile": "Name of an existing SSH filter profile.",
    "casb-profile": "Name of an existing CASB profile.",
    "application": "Application ID list.",
    "app-category": "Application category ID list.",
    "url-category": "URL categories or groups.",
    "app-group": "Application group names.",
    "groups": "Names of user groups that can authenticate with this policy.",
    "users": "Names of individual users that can authenticate with this policy.",
    "fsso-groups": "Names of FSSO groups.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967294},
    "name": {"type": "string", "max_length": 35},
    "schedule": {"type": "string", "max_length": 35},
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
    "ssh-filter-profile": {"type": "string", "max_length": 47},
    "casb-profile": {"type": "string", "max_length": 47},
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
    "internet-service-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
            "required": True,
            "default": "",
            "max_length": 79,
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
    "internet-service-src-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service group name.",
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
            "help": "Custom IPv6 Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom IPv6 Internet Service group name.",
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
    "internet-service6-src-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "service": {
        "name": {
            "type": "string",
            "help": "Service name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "application": {
        "id": {
            "type": "integer",
            "help": "Application IDs.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "app-category": {
        "id": {
            "type": "integer",
            "help": "Category IDs.",
            "required": True,
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
    },
    "app-group": {
        "name": {
            "type": "string",
            "help": "Application group names.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "groups": {
        "name": {
            "type": "string",
            "help": "User group name.",
            "default": "",
            "max_length": 79,
        },
    },
    "users": {
        "name": {
            "type": "string",
            "help": "User name.",
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
}


# Valid enum values from API documentation
VALID_BODY_SRCADDR_NEGATE = [
    "enable",  # Enable source address negate.
    "disable",  # Disable source address negate.
]
VALID_BODY_DSTADDR_NEGATE = [
    "enable",  # Enable destination address negate.
    "disable",  # Disable destination address negate.
]
VALID_BODY_SRCADDR6_NEGATE = [
    "enable",  # Enable IPv6 source address negate.
    "disable",  # Disable IPv6 source address negate.
]
VALID_BODY_DSTADDR6_NEGATE = [
    "enable",  # Enable IPv6 destination address negate.
    "disable",  # Disable IPv6 destination address negate.
]
VALID_BODY_INTERNET_SERVICE = [
    "enable",  # Enable use of Internet Services in policy.
    "disable",  # Disable use of Internet Services in policy.
]
VALID_BODY_INTERNET_SERVICE_NEGATE = [
    "enable",  # Enable negated Internet Service match.
    "disable",  # Disable negated Internet Service match.
]
VALID_BODY_INTERNET_SERVICE_SRC = [
    "enable",  # Enable use of Internet Services source in policy.
    "disable",  # Disable use of Internet Services source in policy.
]
VALID_BODY_INTERNET_SERVICE_SRC_NEGATE = [
    "enable",  # Enable negated Internet Service source match.
    "disable",  # Disable negated Internet Service source match.
]
VALID_BODY_INTERNET_SERVICE6 = [
    "enable",  # Enable use of IPv6 Internet Services in policy.
    "disable",  # Disable use of IPv6 Internet Services in policy.
]
VALID_BODY_INTERNET_SERVICE6_NEGATE = [
    "enable",  # Enable negated IPv6 Internet Service match.
    "disable",  # Disable negated IPv6 Internet Service match.
]
VALID_BODY_INTERNET_SERVICE6_SRC = [
    "enable",  # Enable use of IPv6 Internet Services source in policy.
    "disable",  # Disable use of IPv6 Internet Services source in policy.
]
VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE = [
    "enable",  # Enable negated IPv6 Internet Service source match.
    "disable",  # Disable negated IPv6 Internet Service source match.
]
VALID_BODY_ENFORCE_DEFAULT_APP_PORT = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_SERVICE_NEGATE = [
    "enable",  # Enable negated service match.
    "disable",  # Disable negated service match.
]
VALID_BODY_ACTION = [
    "accept",  # Allows session that match the firewall policy.
    "deny",  # Blocks sessions that match the firewall policy.
]
VALID_BODY_SEND_DENY_PACKET = [
    "disable",  # Disable deny-packet sending.
    "enable",  # Enable deny-packet sending.
]
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOGTRAFFIC = [
    "all",  # Log all sessions accepted or denied by this policy.
    "utm",  # Log traffic that has a security profile applied to it.
    "disable",  # Disable all logging for this policy.
]
VALID_BODY_LEARNING_MODE = [
    "enable",  # Enable learning mode.
    "disable",  # Disable learning mode.
]
VALID_BODY_NAT46 = [
    "enable",  # Enable NAT46.
    "disable",  # Disable NAT46.
]
VALID_BODY_NAT64 = [
    "enable",  # Enable NAT64.
    "disable",  # Disable NAT64.
]
VALID_BODY_PROFILE_TYPE = [
    "single",  # Do not allow security profile groups.
    "group",  # Allow security profile groups.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_security_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/security_policy."""
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
    """Validate required fields for firewall/security_policy."""
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


def validate_firewall_security_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/security_policy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "enforce-default-app-port" in payload:
        value = payload["enforce-default-app-port"]
        if value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            desc = FIELD_DESCRIPTIONS.get("enforce-default-app-port", "")
            error_msg = f"Invalid value for 'enforce-default-app-port': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}"
            error_msg += f"\n  → Example: enforce-default-app-port='{{ VALID_BODY_ENFORCE_DEFAULT_APP_PORT[0] }}'"
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
    if "learning-mode" in payload:
        value = payload["learning-mode"]
        if value not in VALID_BODY_LEARNING_MODE:
            desc = FIELD_DESCRIPTIONS.get("learning-mode", "")
            error_msg = f"Invalid value for 'learning-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LEARNING_MODE)}"
            error_msg += f"\n  → Example: learning-mode='{{ VALID_BODY_LEARNING_MODE[0] }}'"
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

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_security_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/security_policy."""
    # Step 1: Validate enum values
    if "srcaddr-negate" in payload:
        value = payload["srcaddr-negate"]
        if value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'srcaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )
    if "dstaddr-negate" in payload:
        value = payload["dstaddr-negate"]
        if value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid value for 'dstaddr-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )
    if "srcaddr6-negate" in payload:
        value = payload["srcaddr6-negate"]
        if value not in VALID_BODY_SRCADDR6_NEGATE:
            return (
                False,
                f"Invalid value for 'srcaddr6-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR6_NEGATE)}",
            )
    if "dstaddr6-negate" in payload:
        value = payload["dstaddr6-negate"]
        if value not in VALID_BODY_DSTADDR6_NEGATE:
            return (
                False,
                f"Invalid value for 'dstaddr6-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR6_NEGATE)}",
            )
    if "internet-service" in payload:
        value = payload["internet-service"]
        if value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid value for 'internet-service'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )
    if "internet-service-negate" in payload:
        value = payload["internet-service-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )
    if "internet-service-src" in payload:
        value = payload["internet-service-src"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid value for 'internet-service-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )
    if "internet-service-src-negate" in payload:
        value = payload["internet-service-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service-src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )
    if "internet-service6" in payload:
        value = payload["internet-service6"]
        if value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid value for 'internet-service6'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )
    if "internet-service6-negate" in payload:
        value = payload["internet-service6-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service6-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )
    if "internet-service6-src" in payload:
        value = payload["internet-service6-src"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid value for 'internet-service6-src'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )
    if "internet-service6-src-negate" in payload:
        value = payload["internet-service6-src-negate"]
        if value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid value for 'internet-service6-src-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )
    if "enforce-default-app-port" in payload:
        value = payload["enforce-default-app-port"]
        if value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            return (
                False,
                f"Invalid value for 'enforce-default-app-port'='{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}",
            )
    if "service-negate" in payload:
        value = payload["service-negate"]
        if value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid value for 'service-negate'='{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )
    if "send-deny-packet" in payload:
        value = payload["send-deny-packet"]
        if value not in VALID_BODY_SEND_DENY_PACKET:
            return (
                False,
                f"Invalid value for 'send-deny-packet'='{value}'. Must be one of: {', '.join(VALID_BODY_SEND_DENY_PACKET)}",
            )
    if "status" in payload:
        value = payload["status"]
        if value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid value for 'status'='{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )
    if "logtraffic" in payload:
        value = payload["logtraffic"]
        if value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid value for 'logtraffic'='{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )
    if "learning-mode" in payload:
        value = payload["learning-mode"]
        if value not in VALID_BODY_LEARNING_MODE:
            return (
                False,
                f"Invalid value for 'learning-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_LEARNING_MODE)}",
            )
    if "nat46" in payload:
        value = payload["nat46"]
        if value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid value for 'nat46'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )
    if "nat64" in payload:
        value = payload["nat64"]
        if value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid value for 'nat64'='{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )
    if "profile-type" in payload:
        value = payload["profile-type"]
        if value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid value for 'profile-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
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
    "endpoint": "firewall/security_policy",
    "category": "cmdb",
    "api_path": "firewall/security-policy",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure NGFW IPv4/IPv6 application policies.",
    "total_fields": 81,
    "required_fields_count": 3,
    "fields_with_defaults_count": 47,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
