"""Validation helpers for firewall/proxy_policy - Auto-generated"""

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
    "proxy",  # Type of explicit proxy.
    "srcintf",  # Source interface names.
    "dstintf",  # Destination interface names.
    "schedule",  # Name of schedule object.
    "isolator-server",  # Isolator server name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "uuid": "00000000-0000-0000-0000-000000000000",
    "policyid": 0,
    "name": "",
    "proxy": "",
    "ztna-tags-match-logic": "or",
    "device-ownership": "disable",
    "internet-service": "disable",
    "internet-service-negate": "disable",
    "internet-service6": "disable",
    "internet-service6-negate": "disable",
    "srcaddr-negate": "disable",
    "dstaddr-negate": "disable",
    "ztna-ems-tag-negate": "disable",
    "service-negate": "disable",
    "action": "deny",
    "status": "enable",
    "schedule": "",
    "logtraffic": "utm",
    "session-ttl": 0,
    "http-tunnel-auth": "disable",
    "ssh-policy-redirect": "disable",
    "webproxy-forward-server": "",
    "isolator-server": "",
    "webproxy-profile": "",
    "transparent": "disable",
    "webcache": "disable",
    "webcache-https": "disable",
    "disclaimer": "disable",
    "utm-status": "disable",
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
    "ips-voip-filter": "",
    "sctp-filter-profile": "",
    "icap-profile": "",
    "videofilter-profile": "",
    "waf-profile": "",
    "ssh-filter-profile": "",
    "casb-profile": "",
    "replacemsg-override-group": "",
    "logtraffic-start": "disable",
    "log-http-transaction": "disable",
    "block-notification": "disable",
    "https-sub-category": "disable",
    "decrypted-traffic-mirror": "",
    "detect-https-in-http-request": "disable",
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
    "proxy": "option",  # Type of explicit proxy.
    "access-proxy": "string",  # IPv4 access proxy.
    "access-proxy6": "string",  # IPv6 access proxy.
    "ztna-proxy": "string",  # ZTNA proxies.
    "srcintf": "string",  # Source interface names.
    "dstintf": "string",  # Destination interface names.
    "srcaddr": "string",  # Source address objects.
    "poolname": "string",  # Name of IP pool object.
    "poolname6": "string",  # Name of IPv6 pool object.
    "dstaddr": "string",  # Destination address objects.
    "ztna-ems-tag": "string",  # ZTNA EMS Tag names.
    "ztna-tags-match-logic": "option",  # ZTNA tag matching logic.
    "device-ownership": "option",  # When enabled, the ownership enforcement will be done at poli
    "url-risk": "string",  # URL risk level name.
    "internet-service": "option",  # Enable/disable use of Internet Services for this policy. If 
    "internet-service-negate": "option",  # When enabled, Internet Services match against any internet s
    "internet-service-name": "string",  # Internet Service name.
    "internet-service-group": "string",  # Internet Service group name.
    "internet-service-custom": "string",  # Custom Internet Service name.
    "internet-service-custom-group": "string",  # Custom Internet Service group name.
    "internet-service-fortiguard": "string",  # FortiGuard Internet Service name.
    "internet-service6": "option",  # Enable/disable use of Internet Services IPv6 for this policy
    "internet-service6-negate": "option",  # When enabled, Internet Services match against any internet s
    "internet-service6-name": "string",  # Internet Service IPv6 name.
    "internet-service6-group": "string",  # Internet Service IPv6 group name.
    "internet-service6-custom": "string",  # Custom Internet Service IPv6 name.
    "internet-service6-custom-group": "string",  # Custom Internet Service IPv6 group name.
    "internet-service6-fortiguard": "string",  # FortiGuard Internet Service IPv6 name.
    "service": "string",  # Name of service objects.
    "srcaddr-negate": "option",  # When enabled, source addresses match against any address EXC
    "dstaddr-negate": "option",  # When enabled, destination addresses match against any addres
    "ztna-ems-tag-negate": "option",  # When enabled, ZTNA EMS tags match against any tag EXCEPT the
    "service-negate": "option",  # When enabled, services match against any service EXCEPT the 
    "action": "option",  # Accept or deny traffic matching the policy parameters.
    "status": "option",  # Enable/disable the active status of the policy.
    "schedule": "string",  # Name of schedule object.
    "logtraffic": "option",  # Enable/disable logging traffic through the policy.
    "session-ttl": "integer",  # TTL in seconds for sessions accepted by this policy (0 means
    "srcaddr6": "string",  # IPv6 source address objects.
    "dstaddr6": "string",  # IPv6 destination address objects.
    "groups": "string",  # Names of group objects.
    "users": "string",  # Names of user objects.
    "http-tunnel-auth": "option",  # Enable/disable HTTP tunnel authentication.
    "ssh-policy-redirect": "option",  # Redirect SSH traffic to matching transparent proxy policy.
    "webproxy-forward-server": "string",  # Web proxy forward server name.
    "isolator-server": "string",  # Isolator server name.
    "webproxy-profile": "string",  # Name of web proxy profile.
    "transparent": "option",  # Enable to use the IP address of the client to connect to the
    "webcache": "option",  # Enable/disable web caching.
    "webcache-https": "option",  # Enable/disable web caching for HTTPS (Requires deep-inspecti
    "disclaimer": "option",  # Web proxy disclaimer setting: by domain, policy, or user.
    "utm-status": "option",  # Enable the use of UTM profiles/sensors/lists.
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
    "ips-voip-filter": "string",  # Name of an existing VoIP (ips) profile.
    "sctp-filter-profile": "string",  # Name of an existing SCTP filter profile.
    "icap-profile": "string",  # Name of an existing ICAP profile.
    "videofilter-profile": "string",  # Name of an existing VideoFilter profile.
    "waf-profile": "string",  # Name of an existing Web application firewall profile.
    "ssh-filter-profile": "string",  # Name of an existing SSH filter profile.
    "casb-profile": "string",  # Name of an existing CASB profile.
    "replacemsg-override-group": "string",  # Authentication replacement message override group.
    "logtraffic-start": "option",  # Enable/disable policy log traffic start.
    "log-http-transaction": "option",  # Enable/disable HTTP transaction log.
    "comments": "var-string",  # Optional comments.
    "block-notification": "option",  # Enable/disable block notification.
    "redirect-url": "var-string",  # Redirect URL for further explicit web proxy processing.
    "https-sub-category": "option",  # Enable/disable HTTPS sub-category policy matching.
    "decrypted-traffic-mirror": "string",  # Decrypted traffic mirror.
    "detect-https-in-http-request": "option",  # Enable/disable detection of HTTPS in HTTP request.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "uuid": "Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    "policyid": "Policy ID.",
    "name": "Policy name.",
    "proxy": "Type of explicit proxy.",
    "access-proxy": "IPv4 access proxy.",
    "access-proxy6": "IPv6 access proxy.",
    "ztna-proxy": "ZTNA proxies.",
    "srcintf": "Source interface names.",
    "dstintf": "Destination interface names.",
    "srcaddr": "Source address objects.",
    "poolname": "Name of IP pool object.",
    "poolname6": "Name of IPv6 pool object.",
    "dstaddr": "Destination address objects.",
    "ztna-ems-tag": "ZTNA EMS Tag names.",
    "ztna-tags-match-logic": "ZTNA tag matching logic.",
    "device-ownership": "When enabled, the ownership enforcement will be done at policy level.",
    "url-risk": "URL risk level name.",
    "internet-service": "Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.",
    "internet-service-negate": "When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.",
    "internet-service-name": "Internet Service name.",
    "internet-service-group": "Internet Service group name.",
    "internet-service-custom": "Custom Internet Service name.",
    "internet-service-custom-group": "Custom Internet Service group name.",
    "internet-service-fortiguard": "FortiGuard Internet Service name.",
    "internet-service6": "Enable/disable use of Internet Services IPv6 for this policy. If enabled, destination IPv6 address and service are not used.",
    "internet-service6-negate": "When enabled, Internet Services match against any internet service IPv6 EXCEPT the selected Internet Service IPv6.",
    "internet-service6-name": "Internet Service IPv6 name.",
    "internet-service6-group": "Internet Service IPv6 group name.",
    "internet-service6-custom": "Custom Internet Service IPv6 name.",
    "internet-service6-custom-group": "Custom Internet Service IPv6 group name.",
    "internet-service6-fortiguard": "FortiGuard Internet Service IPv6 name.",
    "service": "Name of service objects.",
    "srcaddr-negate": "When enabled, source addresses match against any address EXCEPT the specified source addresses.",
    "dstaddr-negate": "When enabled, destination addresses match against any address EXCEPT the specified destination addresses.",
    "ztna-ems-tag-negate": "When enabled, ZTNA EMS tags match against any tag EXCEPT the specified ZTNA EMS tags.",
    "service-negate": "When enabled, services match against any service EXCEPT the specified destination services.",
    "action": "Accept or deny traffic matching the policy parameters.",
    "status": "Enable/disable the active status of the policy.",
    "schedule": "Name of schedule object.",
    "logtraffic": "Enable/disable logging traffic through the policy.",
    "session-ttl": "TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).",
    "srcaddr6": "IPv6 source address objects.",
    "dstaddr6": "IPv6 destination address objects.",
    "groups": "Names of group objects.",
    "users": "Names of user objects.",
    "http-tunnel-auth": "Enable/disable HTTP tunnel authentication.",
    "ssh-policy-redirect": "Redirect SSH traffic to matching transparent proxy policy.",
    "webproxy-forward-server": "Web proxy forward server name.",
    "isolator-server": "Isolator server name.",
    "webproxy-profile": "Name of web proxy profile.",
    "transparent": "Enable to use the IP address of the client to connect to the server.",
    "webcache": "Enable/disable web caching.",
    "webcache-https": "Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).",
    "disclaimer": "Web proxy disclaimer setting: by domain, policy, or user.",
    "utm-status": "Enable the use of UTM profiles/sensors/lists.",
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
    "ips-voip-filter": "Name of an existing VoIP (ips) profile.",
    "sctp-filter-profile": "Name of an existing SCTP filter profile.",
    "icap-profile": "Name of an existing ICAP profile.",
    "videofilter-profile": "Name of an existing VideoFilter profile.",
    "waf-profile": "Name of an existing Web application firewall profile.",
    "ssh-filter-profile": "Name of an existing SSH filter profile.",
    "casb-profile": "Name of an existing CASB profile.",
    "replacemsg-override-group": "Authentication replacement message override group.",
    "logtraffic-start": "Enable/disable policy log traffic start.",
    "log-http-transaction": "Enable/disable HTTP transaction log.",
    "comments": "Optional comments.",
    "block-notification": "Enable/disable block notification.",
    "redirect-url": "Redirect URL for further explicit web proxy processing.",
    "https-sub-category": "Enable/disable HTTPS sub-category policy matching.",
    "decrypted-traffic-mirror": "Decrypted traffic mirror.",
    "detect-https-in-http-request": "Enable/disable detection of HTTPS in HTTP request.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "policyid": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 35},
    "schedule": {"type": "string", "max_length": 35},
    "session-ttl": {"type": "integer", "min": 300, "max": 2764800},
    "webproxy-forward-server": {"type": "string", "max_length": 63},
    "isolator-server": {"type": "string", "max_length": 63},
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
    "ips-voip-filter": {"type": "string", "max_length": 47},
    "sctp-filter-profile": {"type": "string", "max_length": 47},
    "icap-profile": {"type": "string", "max_length": 47},
    "videofilter-profile": {"type": "string", "max_length": 47},
    "waf-profile": {"type": "string", "max_length": 47},
    "ssh-filter-profile": {"type": "string", "max_length": 47},
    "casb-profile": {"type": "string", "max_length": 47},
    "replacemsg-override-group": {"type": "string", "max_length": 35},
    "decrypted-traffic-mirror": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "access-proxy": {
        "name": {
            "type": "string",
            "help": "Access Proxy name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "access-proxy6": {
        "name": {
            "type": "string",
            "help": "Access proxy name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "ztna-proxy": {
        "name": {
            "type": "string",
            "help": "ZTNA proxy name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
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
    "dstaddr": {
        "name": {
            "type": "string",
            "help": "Address name.",
            "default": "",
            "max_length": 79,
        },
    },
    "ztna-ems-tag": {
        "name": {
            "type": "string",
            "help": "EMS Tag name.",
            "default": "",
            "max_length": 79,
        },
    },
    "url-risk": {
        "name": {
            "type": "string",
            "help": "Risk level name.",
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service-name": {
        "name": {
            "type": "string",
            "help": "Internet Service name.",
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
    "internet-service6-name": {
        "name": {
            "type": "string",
            "help": "Internet Service IPv6 name.",
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-group": {
        "name": {
            "type": "string",
            "help": "Internet Service IPv6 group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-custom": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service IPv6 name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-custom-group": {
        "name": {
            "type": "string",
            "help": "Custom Internet Service IPv6 group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "internet-service6-fortiguard": {
        "name": {
            "type": "string",
            "help": "FortiGuard Internet Service IPv6 name.",
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
    "groups": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
    "users": {
        "name": {
            "type": "string",
            "help": "Group name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_PROXY = [
    "explicit-web",  # Explicit Web Proxy
    "transparent-web",  # Transparent Web Proxy
    "ftp",  # Explicit FTP Proxy
    "ssh",  # SSH Proxy
    "ssh-tunnel",  # SSH Tunnel
    "access-proxy",  # Access Proxy
    "ztna-proxy",  # ZTNA Proxy
    "wanopt",  # WANopt Tunnel
]
VALID_BODY_ZTNA_TAGS_MATCH_LOGIC = [
    "or",  # Match ZTNA tags using a logical OR operator.
    "and",  # Match ZTNA tags using a logical AND operator.
]
VALID_BODY_DEVICE_OWNERSHIP = [
    "enable",  # Enable device ownership.
    "disable",  # Disable device ownership.
]
VALID_BODY_INTERNET_SERVICE = [
    "enable",  # Enable use of Internet Services in policy.
    "disable",  # Disable use of Internet Services in policy.
]
VALID_BODY_INTERNET_SERVICE_NEGATE = [
    "enable",  # Enable negated Internet Service match.
    "disable",  # Disable negated Internet Service match.
]
VALID_BODY_INTERNET_SERVICE6 = [
    "enable",  # Enable use of IPv6 Internet Services in policy.
    "disable",  # Disable use of IPv6 Internet Services in policy.
]
VALID_BODY_INTERNET_SERVICE6_NEGATE = [
    "enable",  # Enable negated IPv6 Internet Service match.
    "disable",  # Disable negated IPv6 Internet Service match.
]
VALID_BODY_SRCADDR_NEGATE = [
    "enable",  # Enable source address negate.
    "disable",  # Disable destination address negate.
]
VALID_BODY_DSTADDR_NEGATE = [
    "enable",  # Enable source address negate.
    "disable",  # Disable destination address negate.
]
VALID_BODY_ZTNA_EMS_TAG_NEGATE = [
    "enable",  # Enable ZTNA EMS tags negate.
    "disable",  # Disable ZTNA EMS tags negate.
]
VALID_BODY_SERVICE_NEGATE = [
    "enable",  # Enable negated service match.
    "disable",  # Disable negated service match.
]
VALID_BODY_ACTION = [
    "accept",  # Action accept.
    "deny",  # Action deny.
    "redirect",  # Action redirect.
    "isolate",  # Action isolate.
]
VALID_BODY_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOGTRAFFIC = [
    "all",  # Log all sessions.
    "utm",  # UTM event and matched application traffic log.
    "disable",  # Disable traffic and application log.
]
VALID_BODY_HTTP_TUNNEL_AUTH = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_SSH_POLICY_REDIRECT = [
    "enable",  # Enable SSH policy redirect.
    "disable",  # Disable SSH policy redirect.
]
VALID_BODY_TRANSPARENT = [
    "enable",  # Enable use of IP address of client to connect to server.
    "disable",  # Disable use of IP address of client to connect to server.
]
VALID_BODY_WEBCACHE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEBCACHE_HTTPS = [
    "disable",  # Disable web cache for HTTPS.
    "enable",  # Enable web cache for HTTPS.
]
VALID_BODY_DISCLAIMER = [
    "disable",  # Disable disclaimer.
    "domain",  # Display disclaimer for domain
    "policy",  # Display disclaimer for policy
    "user",  # Display disclaimer for current user
]
VALID_BODY_UTM_STATUS = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_PROFILE_TYPE = [
    "single",  # Do not allow security profile groups.
    "group",  # Allow security profile groups.
]
VALID_BODY_LOGTRAFFIC_START = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_LOG_HTTP_TRANSACTION = [
    "enable",  # Enable HTTP transaction log.
    "disable",  # Disable HTTP transaction log.
]
VALID_BODY_BLOCK_NOTIFICATION = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_HTTPS_SUB_CATEGORY = [
    "enable",  # Enable HTTPS sub-category policy matching.
    "disable",  # Disable HTTPS sub-category policy matching.
]
VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST = [
    "enable",  # Enable detection of HTTPS in HTTP request.
    "disable",  # Disable detection of HTTPS in HTTP request.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_proxy_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/proxy_policy."""
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
    """Validate required fields for firewall/proxy_policy."""
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


def validate_firewall_proxy_policy_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/proxy_policy object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "proxy" in payload:
        value = payload["proxy"]
        if value not in VALID_BODY_PROXY:
            desc = FIELD_DESCRIPTIONS.get("proxy", "")
            error_msg = f"Invalid value for 'proxy': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROXY)}"
            error_msg += f"\n  → Example: proxy='{{ VALID_BODY_PROXY[0] }}'"
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
    if "device-ownership" in payload:
        value = payload["device-ownership"]
        if value not in VALID_BODY_DEVICE_OWNERSHIP:
            desc = FIELD_DESCRIPTIONS.get("device-ownership", "")
            error_msg = f"Invalid value for 'device-ownership': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEVICE_OWNERSHIP)}"
            error_msg += f"\n  → Example: device-ownership='{{ VALID_BODY_DEVICE_OWNERSHIP[0] }}'"
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
    if "http-tunnel-auth" in payload:
        value = payload["http-tunnel-auth"]
        if value not in VALID_BODY_HTTP_TUNNEL_AUTH:
            desc = FIELD_DESCRIPTIONS.get("http-tunnel-auth", "")
            error_msg = f"Invalid value for 'http-tunnel-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTP_TUNNEL_AUTH)}"
            error_msg += f"\n  → Example: http-tunnel-auth='{{ VALID_BODY_HTTP_TUNNEL_AUTH[0] }}'"
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
    if "transparent" in payload:
        value = payload["transparent"]
        if value not in VALID_BODY_TRANSPARENT:
            desc = FIELD_DESCRIPTIONS.get("transparent", "")
            error_msg = f"Invalid value for 'transparent': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRANSPARENT)}"
            error_msg += f"\n  → Example: transparent='{{ VALID_BODY_TRANSPARENT[0] }}'"
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
    if "https-sub-category" in payload:
        value = payload["https-sub-category"]
        if value not in VALID_BODY_HTTPS_SUB_CATEGORY:
            desc = FIELD_DESCRIPTIONS.get("https-sub-category", "")
            error_msg = f"Invalid value for 'https-sub-category': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTPS_SUB_CATEGORY)}"
            error_msg += f"\n  → Example: https-sub-category='{{ VALID_BODY_HTTPS_SUB_CATEGORY[0] }}'"
            return (False, error_msg)
    if "detect-https-in-http-request" in payload:
        value = payload["detect-https-in-http-request"]
        if value not in VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST:
            desc = FIELD_DESCRIPTIONS.get("detect-https-in-http-request", "")
            error_msg = f"Invalid value for 'detect-https-in-http-request': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST)}"
            error_msg += f"\n  → Example: detect-https-in-http-request='{{ VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_proxy_policy_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/proxy_policy."""
    # Step 1: Validate enum values
    if "proxy" in payload:
        value = payload["proxy"]
        if value not in VALID_BODY_PROXY:
            return (
                False,
                f"Invalid value for 'proxy'='{value}'. Must be one of: {', '.join(VALID_BODY_PROXY)}",
            )
    if "ztna-tags-match-logic" in payload:
        value = payload["ztna-tags-match-logic"]
        if value not in VALID_BODY_ZTNA_TAGS_MATCH_LOGIC:
            return (
                False,
                f"Invalid value for 'ztna-tags-match-logic'='{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TAGS_MATCH_LOGIC)}",
            )
    if "device-ownership" in payload:
        value = payload["device-ownership"]
        if value not in VALID_BODY_DEVICE_OWNERSHIP:
            return (
                False,
                f"Invalid value for 'device-ownership'='{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_OWNERSHIP)}",
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
    if "action" in payload:
        value = payload["action"]
        if value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid value for 'action'='{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
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
    if "http-tunnel-auth" in payload:
        value = payload["http-tunnel-auth"]
        if value not in VALID_BODY_HTTP_TUNNEL_AUTH:
            return (
                False,
                f"Invalid value for 'http-tunnel-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_TUNNEL_AUTH)}",
            )
    if "ssh-policy-redirect" in payload:
        value = payload["ssh-policy-redirect"]
        if value not in VALID_BODY_SSH_POLICY_REDIRECT:
            return (
                False,
                f"Invalid value for 'ssh-policy-redirect'='{value}'. Must be one of: {', '.join(VALID_BODY_SSH_POLICY_REDIRECT)}",
            )
    if "transparent" in payload:
        value = payload["transparent"]
        if value not in VALID_BODY_TRANSPARENT:
            return (
                False,
                f"Invalid value for 'transparent'='{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPARENT)}",
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
    if "disclaimer" in payload:
        value = payload["disclaimer"]
        if value not in VALID_BODY_DISCLAIMER:
            return (
                False,
                f"Invalid value for 'disclaimer'='{value}'. Must be one of: {', '.join(VALID_BODY_DISCLAIMER)}",
            )
    if "utm-status" in payload:
        value = payload["utm-status"]
        if value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid value for 'utm-status'='{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )
    if "profile-type" in payload:
        value = payload["profile-type"]
        if value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid value for 'profile-type'='{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
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
    if "block-notification" in payload:
        value = payload["block-notification"]
        if value not in VALID_BODY_BLOCK_NOTIFICATION:
            return (
                False,
                f"Invalid value for 'block-notification'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_NOTIFICATION)}",
            )
    if "https-sub-category" in payload:
        value = payload["https-sub-category"]
        if value not in VALID_BODY_HTTPS_SUB_CATEGORY:
            return (
                False,
                f"Invalid value for 'https-sub-category'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_SUB_CATEGORY)}",
            )
    if "detect-https-in-http-request" in payload:
        value = payload["detect-https-in-http-request"]
        if value not in VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST:
            return (
                False,
                f"Invalid value for 'detect-https-in-http-request'='{value}'. Must be one of: {', '.join(VALID_BODY_DETECT_HTTPS_IN_HTTP_REQUEST)}",
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
    "endpoint": "firewall/proxy_policy",
    "category": "cmdb",
    "api_path": "firewall/proxy-policy",
    "mkey": "policyid",
    "mkey_type": "integer",
    "help": "Configure proxy policies.",
    "total_fields": 83,
    "required_fields_count": 5,
    "fields_with_defaults_count": 55,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
