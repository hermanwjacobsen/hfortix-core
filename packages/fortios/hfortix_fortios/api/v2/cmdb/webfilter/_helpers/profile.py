"""
Validation helpers for webfilter/profile endpoint.

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "feature-set": "flow",
    "replacemsg-group": "",
    "options": "",
    "https-replacemsg": "enable",
    "web-flow-log-encoding": "utf-8",
    "ovrd-perm": "",
    "post-action": "normal",
    "wisp": "disable",
    "wisp-algorithm": "auto-learning",
    "log-all-url": "disable",
    "web-content-log": "enable",
    "web-filter-activex-log": "enable",
    "web-filter-command-block-log": "enable",
    "web-filter-cookie-log": "enable",
    "web-filter-applet-log": "enable",
    "web-filter-jscript-log": "enable",
    "web-filter-js-log": "enable",
    "web-filter-vbs-log": "enable",
    "web-filter-unknown-log": "enable",
    "web-filter-referer-log": "enable",
    "web-filter-cookie-removal-log": "enable",
    "web-url-log": "enable",
    "web-invalid-domain-log": "enable",
    "web-ftgd-err-log": "enable",
    "web-ftgd-quota-usage": "enable",
    "extended-log": "disable",
    "web-extended-all-action-log": "disable",
    "web-antiphishing-log": "enable",
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
    "name": "string",  # Profile name.
    "comment": "var-string",  # Optional comments.
    "feature-set": "option",  # Flow/proxy feature set.
    "replacemsg-group": "string",  # Replacement message group.
    "options": "option",  # Options.
    "https-replacemsg": "option",  # Enable replacement messages for HTTPS.
    "web-flow-log-encoding": "option",  # Log encoding in flow mode.
    "ovrd-perm": "option",  # Permitted override types.
    "post-action": "option",  # Action taken for HTTP POST traffic.
    "override": "string",  # Web Filter override settings.
    "web": "string",  # Web content filtering settings.
    "ftgd-wf": "string",  # FortiGuard Web Filter settings.
    "antiphish": "string",  # AntiPhishing profile.
    "wisp": "option",  # Enable/disable web proxy WISP.
    "wisp-servers": "string",  # WISP servers.
    "wisp-algorithm": "option",  # WISP server selection algorithm.
    "log-all-url": "option",  # Enable/disable logging all URLs visited.
    "web-content-log": "option",  # Enable/disable logging logging blocked web content.
    "web-filter-activex-log": "option",  # Enable/disable logging ActiveX.
    "web-filter-command-block-log": "option",  # Enable/disable logging blocked commands.
    "web-filter-cookie-log": "option",  # Enable/disable logging cookie filtering.
    "web-filter-applet-log": "option",  # Enable/disable logging Java applets.
    "web-filter-jscript-log": "option",  # Enable/disable logging JScripts.
    "web-filter-js-log": "option",  # Enable/disable logging Java scripts.
    "web-filter-vbs-log": "option",  # Enable/disable logging VBS scripts.
    "web-filter-unknown-log": "option",  # Enable/disable logging unknown scripts.
    "web-filter-referer-log": "option",  # Enable/disable logging referrers.
    "web-filter-cookie-removal-log": "option",  # Enable/disable logging blocked cookies.
    "web-url-log": "option",  # Enable/disable logging URL filtering.
    "web-invalid-domain-log": "option",  # Enable/disable logging invalid domain names.
    "web-ftgd-err-log": "option",  # Enable/disable logging rating errors.
    "web-ftgd-quota-usage": "option",  # Enable/disable logging daily quota usage.
    "extended-log": "option",  # Enable/disable extended logging for web filtering.
    "web-extended-all-action-log": "option",  # Enable/disable extended any filter action logging for web fi
    "web-antiphishing-log": "option",  # Enable/disable logging of AntiPhishing checks.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "comment": "Optional comments.",
    "feature-set": "Flow/proxy feature set.",
    "replacemsg-group": "Replacement message group.",
    "options": "Options.",
    "https-replacemsg": "Enable replacement messages for HTTPS.",
    "web-flow-log-encoding": "Log encoding in flow mode.",
    "ovrd-perm": "Permitted override types.",
    "post-action": "Action taken for HTTP POST traffic.",
    "override": "Web Filter override settings.",
    "web": "Web content filtering settings.",
    "ftgd-wf": "FortiGuard Web Filter settings.",
    "antiphish": "AntiPhishing profile.",
    "wisp": "Enable/disable web proxy WISP.",
    "wisp-servers": "WISP servers.",
    "wisp-algorithm": "WISP server selection algorithm.",
    "log-all-url": "Enable/disable logging all URLs visited.",
    "web-content-log": "Enable/disable logging logging blocked web content.",
    "web-filter-activex-log": "Enable/disable logging ActiveX.",
    "web-filter-command-block-log": "Enable/disable logging blocked commands.",
    "web-filter-cookie-log": "Enable/disable logging cookie filtering.",
    "web-filter-applet-log": "Enable/disable logging Java applets.",
    "web-filter-jscript-log": "Enable/disable logging JScripts.",
    "web-filter-js-log": "Enable/disable logging Java scripts.",
    "web-filter-vbs-log": "Enable/disable logging VBS scripts.",
    "web-filter-unknown-log": "Enable/disable logging unknown scripts.",
    "web-filter-referer-log": "Enable/disable logging referrers.",
    "web-filter-cookie-removal-log": "Enable/disable logging blocked cookies.",
    "web-url-log": "Enable/disable logging URL filtering.",
    "web-invalid-domain-log": "Enable/disable logging invalid domain names.",
    "web-ftgd-err-log": "Enable/disable logging rating errors.",
    "web-ftgd-quota-usage": "Enable/disable logging daily quota usage.",
    "extended-log": "Enable/disable extended logging for web filtering.",
    "web-extended-all-action-log": "Enable/disable extended any filter action logging for web filtering.",
    "web-antiphishing-log": "Enable/disable logging of AntiPhishing checks.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "override": {
        "ovrd-cookie": {
            "type": "option",
            "help": "Allow/deny browser-based (cookie) overrides.",
            "default": "deny",
            "options": [{"help": "Allow browser-based (cookie) override.", "label": "Allow", "name": "allow"}, {"help": "Deny browser-based (cookie) override.", "label": "Deny", "name": "deny"}],
        },
        "ovrd-scope": {
            "type": "option",
            "help": "Override scope.",
            "default": "user",
            "options": [{"help": "Override for the user.", "label": "User", "name": "user"}, {"help": "Override for the user\u0027s group.", "label": "User Group", "name": "user-group"}, {"help": "Override for the initiating IP.", "label": "Ip", "name": "ip"}, {"help": "Create browser-based (cookie) override.", "label": "Browser", "name": "browser"}, {"help": "Prompt for scope when initiating an override.", "label": "Ask", "name": "ask"}],
        },
        "profile-type": {
            "type": "option",
            "help": "Override profile type.",
            "default": "list",
            "options": [{"help": "Profile chosen from list.", "label": "List", "name": "list"}, {"help": "Profile determined by RADIUS server.", "label": "Radius", "name": "radius"}],
        },
        "ovrd-dur-mode": {
            "type": "option",
            "help": "Override duration mode.",
            "default": "constant",
            "options": [{"help": "Constant mode.", "label": "Constant", "name": "constant"}, {"help": "Prompt for duration when initiating an override.", "label": "Ask", "name": "ask"}],
        },
        "ovrd-dur": {
            "type": "user",
            "help": "Override duration.",
            "default": "15m",
        },
        "profile-attribute": {
            "type": "option",
            "help": "Profile attribute to retrieve from the RADIUS server.",
            "default": "Login-LAT-Service",
            "options": [{"help": "Use this attribute.", "label": "User Name", "name": "User-Name"}, {"help": "Use this attribute.", "label": "Nas Ip Address", "name": "NAS-IP-Address"}, {"help": "Use this attribute.", "label": "Framed Ip Address", "name": "Framed-IP-Address"}, {"help": "Use this attribute.", "label": "Framed Ip Netmask", "name": "Framed-IP-Netmask"}, {"help": "Use this attribute.", "label": "Filter Id", "name": "Filter-Id"}, {"help": "Use this attribute.", "label": "Login Ip Host", "name": "Login-IP-Host"}, {"help": "Use this attribute.", "label": "Reply Message", "name": "Reply-Message"}, {"help": "Use this attribute.", "label": "Callback Number", "name": "Callback-Number"}, {"help": "Use this attribute.", "label": "Callback Id", "name": "Callback-Id"}, {"help": "Use this attribute.", "label": "Framed Route", "name": "Framed-Route"}, {"help": "Use this attribute.", "label": "Framed Ipx Network", "name": "Framed-IPX-Network"}, {"help": "Use this attribute.", "label": "Class", "name": "Class"}, {"help": "Use this attribute.", "label": "Called Station Id", "name": "Called-Station-Id"}, {"help": "Use this attribute.", "label": "Calling Station Id", "name": "Calling-Station-Id"}, {"help": "Use this attribute.", "label": "Nas Identifier", "name": "NAS-Identifier"}, {"help": "Use this attribute.", "label": "Proxy State", "name": "Proxy-State"}, {"help": "Use this attribute.", "label": "Login Lat Service", "name": "Login-LAT-Service"}, {"help": "Use this attribute.", "label": "Login Lat Node", "name": "Login-LAT-Node"}, {"help": "Use this attribute.", "label": "Login Lat Group", "name": "Login-LAT-Group"}, {"help": "Use this attribute.", "label": "Framed Appletalk Zone", "name": "Framed-AppleTalk-Zone"}, {"help": "Use this attribute.", "label": "Acct Session Id", "name": "Acct-Session-Id"}, {"help": "Use this attribute.", "label": "Acct Multi Session Id", "name": "Acct-Multi-Session-Id"}],
        },
        "ovrd-user-group": {
            "type": "string",
            "help": "User groups with permission to use the override.",
        },
        "profile": {
            "type": "string",
            "help": "Web filter profile with permission to create overrides.",
        },
    },
    "web": {
        "bword-threshold": {
            "type": "integer",
            "help": "Banned word score threshold.",
            "default": 10,
            "min_value": 0,
            "max_value": 2147483647,
        },
        "bword-table": {
            "type": "integer",
            "help": "Banned word table ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "urlfilter-table": {
            "type": "integer",
            "help": "URL filter table ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "content-header-list": {
            "type": "integer",
            "help": "Content header list.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "blocklist": {
            "type": "option",
            "help": "Enable/disable automatic addition of URLs detected by FortiSandbox to blocklist.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "allowlist": {
            "type": "option",
            "help": "FortiGuard allowlist settings.",
            "default": "",
            "options": [{"help": "Exempt antivirus.", "label": "Exempt Av", "name": "exempt-av"}, {"help": "Exempt web content.", "label": "Exempt Webcontent", "name": "exempt-webcontent"}, {"help": "Exempt ActiveX-JAVA-Cookie.", "label": "Exempt Activex Java Cookie", "name": "exempt-activex-java-cookie"}, {"help": "Exempt DLP.", "label": "Exempt Dlp", "name": "exempt-dlp"}, {"help": "Exempt RangeBlock.", "label": "Exempt Rangeblock", "name": "exempt-rangeblock"}, {"help": "Support extended log.", "label": "Extended Log Others", "name": "extended-log-others"}],
        },
        "safe-search": {
            "type": "option",
            "help": "Safe search type.",
            "default": "",
            "options": [{"help": "Insert safe search string into URL.", "label": "Url", "name": "url"}, {"help": "Insert safe search header.", "label": "Header", "name": "header"}],
        },
        "youtube-restrict": {
            "type": "option",
            "help": "YouTube EDU filter level.",
            "default": "none",
            "options": [{"help": "Full access for YouTube.", "label": "None", "name": "none"}, {"help": "Strict access for YouTube.", "label": "Strict", "name": "strict"}, {"help": "Moderate access for YouTube.", "label": "Moderate", "name": "moderate"}],
        },
        "vimeo-restrict": {
            "type": "string",
            "help": "Set Vimeo-restrict (\"7\" = don't show mature content, \"134\" = don't show unrated and mature content). A value of cookie \"content_rating\".",
            "default": "",
            "max_length": 63,
        },
        "log-search": {
            "type": "option",
            "help": "Enable/disable logging all search phrases.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "keyword-match": {
            "type": "string",
            "help": "Search keywords to log when match is found.",
        },
    },
    "ftgd-wf": {
        "options": {
            "type": "option",
            "help": "Options for FortiGuard Web Filter.",
            "default": "ftgd-disable",
            "options": [{"help": "Allow web pages with a rating error to pass through.", "label": "Error Allow", "name": "error-allow"}, {"help": "Rate the server IP in addition to the domain name.", "label": "Rate Server Ip", "name": "rate-server-ip"}, {"help": "Bypass connection which has CONNECT request.", "label": "Connect Request Bypass", "name": "connect-request-bypass"}, {"help": "Disable FortiGuard scanning.", "label": "Ftgd Disable", "name": "ftgd-disable"}],
        },
        "exempt-quota": {
            "type": "user",
            "help": "Do not stop quota for these categories.",
            "default": "17",
        },
        "ovrd": {
            "type": "user",
            "help": "Allow web filter profile overrides.",
            "default": "",
        },
        "filters": {
            "type": "string",
            "help": "FortiGuard filters.",
        },
        "risk": {
            "type": "string",
            "help": "FortiGuard risk level settings.",
        },
        "quota": {
            "type": "string",
            "help": "FortiGuard traffic quota settings.",
        },
        "max-quota-timeout": {
            "type": "integer",
            "help": "Maximum FortiGuard quota used by single page view in seconds (excludes streams).",
            "default": 300,
            "min_value": 1,
            "max_value": 86400,
        },
        "rate-javascript-urls": {
            "type": "option",
            "help": "Enable/disable rating JavaScript by URL.",
            "default": "enable",
            "options": [{"help": "Disable rating JavaScript by URL.", "label": "Disable", "name": "disable"}, {"help": "Enable rating JavaScript by URL.", "label": "Enable", "name": "enable"}],
        },
        "rate-css-urls": {
            "type": "option",
            "help": "Enable/disable rating CSS by URL.",
            "default": "enable",
            "options": [{"help": "Disable rating CSS by URL.", "label": "Disable", "name": "disable"}, {"help": "Enable rating CSS by URL.", "label": "Enable", "name": "enable"}],
        },
        "rate-crl-urls": {
            "type": "option",
            "help": "Enable/disable rating CRL by URL.",
            "default": "enable",
            "options": [{"help": "Disable rating CRL by URL.", "label": "Disable", "name": "disable"}, {"help": "Enable rating CRL by URL.", "label": "Enable", "name": "enable"}],
        },
    },
    "antiphish": {
        "status": {
            "type": "option",
            "help": "Toggle AntiPhishing functionality.",
            "default": "disable",
            "options": [{"help": "Enable AntiPhishing functionality.", "label": "Enable", "name": "enable"}, {"help": "Disable AntiPhishing functionality.", "label": "Disable", "name": "disable"}],
        },
        "default-action": {
            "type": "option",
            "help": "Action to be taken when there is no matching rule.",
            "default": "exempt",
            "options": [{"help": "Exempt requests from matching.", "label": "Exempt", "name": "exempt"}, {"help": "Log all matched requests.", "label": "Log", "name": "log"}, {"help": "Block all matched requests.", "label": "Block", "name": "block"}],
        },
        "check-uri": {
            "type": "option",
            "help": "Enable/disable checking of GET URI parameters for known credentials.",
            "default": "disable",
            "options": [{"help": "Enable checking of GET URI for username and password fields.", "label": "Enable", "name": "enable"}, {"help": "Disable checking of GET URI for username and password fields.", "label": "Disable", "name": "disable"}],
        },
        "check-basic-auth": {
            "type": "option",
            "help": "Enable/disable checking of HTTP Basic Auth field for known credentials.",
            "default": "disable",
            "options": [{"help": "Enable checking of HTTP Basic Auth field for known credentials.", "label": "Enable", "name": "enable"}, {"help": "Disable checking of HTTP Basic Auth field for known credentials.", "label": "Disable", "name": "disable"}],
        },
        "check-username-only": {
            "type": "option",
            "help": "Enable/disable username only matching of credentials. Action will be taken for valid usernames regardless of password validity.",
            "default": "disable",
            "options": [{"help": "Enable username only credential matches.", "label": "Enable", "name": "enable"}, {"help": "Disable username only credential matches.", "label": "Disable", "name": "disable"}],
        },
        "max-body-len": {
            "type": "integer",
            "help": "Maximum size of a POST body to check for credentials.",
            "default": 1024,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "inspection-entries": {
            "type": "string",
            "help": "AntiPhishing entries.",
        },
        "custom-patterns": {
            "type": "string",
            "help": "Custom username and password regex patterns.",
        },
        "authentication": {
            "type": "option",
            "help": "Authentication methods.",
            "required": True,
            "default": "domain-controller",
            "options": [{"help": "Domain Controller to verify user credential.", "label": "Domain Controller", "name": "domain-controller"}, {"help": "LDAP to verify user credential.", "label": "Ldap", "name": "ldap"}],
        },
        "domain-controller": {
            "type": "string",
            "help": "Domain for which to verify received credentials against.",
            "default": "",
            "max_length": 63,
        },
        "ldap": {
            "type": "string",
            "help": "LDAP server for which to verify received credentials against.",
            "default": "",
            "max_length": 63,
        },
    },
    "wisp-servers": {
        "name": {
            "type": "string",
            "help": "Server name.",
            "required": True,
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = [
    "flow",  # Flow feature set.
    "proxy",  # Proxy feature set.
]
VALID_BODY_OPTIONS = [
    "activexfilter",  # ActiveX filter.
    "cookiefilter",  # Cookie filter.
    "javafilter",  # Java applet filter.
    "block-invalid-url",  # Block sessions contained an invalid domain name.
    "jscript",  # Javascript block.
    "js",  # JS block.
    "vbs",  # VB script block.
    "unknown",  # Unknown script block.
    "intrinsic",  # Intrinsic script block.
    "wf-referer",  # Referring block.
    "wf-cookie",  # Cookie block.
    "per-user-bal",  # Per-user block/allow list filter
]
VALID_BODY_HTTPS_REPLACEMSG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FLOW_LOG_ENCODING = [
    "utf-8",  # UTF-8 encoding.
    "punycode",  # Punycode encoding.
]
VALID_BODY_OVRD_PERM = [
    "bannedword-override",  # Banned word override.
    "urlfilter-override",  # URL filter override.
    "fortiguard-wf-override",  # FortiGuard Web Filter override.
    "contenttype-check-override",  # Content-type header override.
]
VALID_BODY_POST_ACTION = [
    "normal",  # Normal, POST requests are allowed.
    "block",  # POST requests are blocked.
]
VALID_BODY_WISP = [
    "enable",  # Enable web proxy WISP.
    "disable",  # Disable web proxy WISP.
]
VALID_BODY_WISP_ALGORITHM = [
    "primary-secondary",  # Select the first healthy server in order.
    "round-robin",  # Select the next healthy server.
    "auto-learning",  # Select the lightest loading healthy server.
]
VALID_BODY_LOG_ALL_URL = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_CONTENT_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_ACTIVEX_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_COOKIE_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_APPLET_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_JSCRIPT_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_JS_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_VBS_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_UNKNOWN_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_REFERER_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_URL_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_INVALID_DOMAIN_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FTGD_ERR_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_FTGD_QUOTA_USAGE = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EXTENDED_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_WEB_ANTIPHISHING_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_webfilter_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for webfilter/profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_webfilter_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_webfilter_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_webfilter_profile_get(
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
    Validate required fields for webfilter/profile.

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


def validate_webfilter_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new webfilter/profile object.

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
        ...     "name": True,  # Profile name.
        ... }
        >>> is_valid, error = validate_webfilter_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "name": True,
        ...     "feature-set": "{'name': 'flow', 'help': 'Flow feature set.', 'label': 'Flow', 'description': 'Flow feature set'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_webfilter_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["feature-set"] = "invalid-value"
        >>> is_valid, error = validate_webfilter_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_webfilter_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            desc = FIELD_DESCRIPTIONS.get("feature-set", "")
            error_msg = f"Invalid value for 'feature-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEATURE_SET)}"
            error_msg += f"\n  → Example: feature-set='{{ VALID_BODY_FEATURE_SET[0] }}'"
            return (False, error_msg)
    if "options" in payload:
        value = payload["options"]
        if value not in VALID_BODY_OPTIONS:
            desc = FIELD_DESCRIPTIONS.get("options", "")
            error_msg = f"Invalid value for 'options': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OPTIONS)}"
            error_msg += f"\n  → Example: options='{{ VALID_BODY_OPTIONS[0] }}'"
            return (False, error_msg)
    if "https-replacemsg" in payload:
        value = payload["https-replacemsg"]
        if value not in VALID_BODY_HTTPS_REPLACEMSG:
            desc = FIELD_DESCRIPTIONS.get("https-replacemsg", "")
            error_msg = f"Invalid value for 'https-replacemsg': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HTTPS_REPLACEMSG)}"
            error_msg += f"\n  → Example: https-replacemsg='{{ VALID_BODY_HTTPS_REPLACEMSG[0] }}'"
            return (False, error_msg)
    if "web-flow-log-encoding" in payload:
        value = payload["web-flow-log-encoding"]
        if value not in VALID_BODY_WEB_FLOW_LOG_ENCODING:
            desc = FIELD_DESCRIPTIONS.get("web-flow-log-encoding", "")
            error_msg = f"Invalid value for 'web-flow-log-encoding': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FLOW_LOG_ENCODING)}"
            error_msg += f"\n  → Example: web-flow-log-encoding='{{ VALID_BODY_WEB_FLOW_LOG_ENCODING[0] }}'"
            return (False, error_msg)
    if "ovrd-perm" in payload:
        value = payload["ovrd-perm"]
        if value not in VALID_BODY_OVRD_PERM:
            desc = FIELD_DESCRIPTIONS.get("ovrd-perm", "")
            error_msg = f"Invalid value for 'ovrd-perm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVRD_PERM)}"
            error_msg += f"\n  → Example: ovrd-perm='{{ VALID_BODY_OVRD_PERM[0] }}'"
            return (False, error_msg)
    if "post-action" in payload:
        value = payload["post-action"]
        if value not in VALID_BODY_POST_ACTION:
            desc = FIELD_DESCRIPTIONS.get("post-action", "")
            error_msg = f"Invalid value for 'post-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_POST_ACTION)}"
            error_msg += f"\n  → Example: post-action='{{ VALID_BODY_POST_ACTION[0] }}'"
            return (False, error_msg)
    if "wisp" in payload:
        value = payload["wisp"]
        if value not in VALID_BODY_WISP:
            desc = FIELD_DESCRIPTIONS.get("wisp", "")
            error_msg = f"Invalid value for 'wisp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WISP)}"
            error_msg += f"\n  → Example: wisp='{{ VALID_BODY_WISP[0] }}'"
            return (False, error_msg)
    if "wisp-algorithm" in payload:
        value = payload["wisp-algorithm"]
        if value not in VALID_BODY_WISP_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("wisp-algorithm", "")
            error_msg = f"Invalid value for 'wisp-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WISP_ALGORITHM)}"
            error_msg += f"\n  → Example: wisp-algorithm='{{ VALID_BODY_WISP_ALGORITHM[0] }}'"
            return (False, error_msg)
    if "log-all-url" in payload:
        value = payload["log-all-url"]
        if value not in VALID_BODY_LOG_ALL_URL:
            desc = FIELD_DESCRIPTIONS.get("log-all-url", "")
            error_msg = f"Invalid value for 'log-all-url': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LOG_ALL_URL)}"
            error_msg += f"\n  → Example: log-all-url='{{ VALID_BODY_LOG_ALL_URL[0] }}'"
            return (False, error_msg)
    if "web-content-log" in payload:
        value = payload["web-content-log"]
        if value not in VALID_BODY_WEB_CONTENT_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-content-log", "")
            error_msg = f"Invalid value for 'web-content-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_CONTENT_LOG)}"
            error_msg += f"\n  → Example: web-content-log='{{ VALID_BODY_WEB_CONTENT_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-activex-log" in payload:
        value = payload["web-filter-activex-log"]
        if value not in VALID_BODY_WEB_FILTER_ACTIVEX_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-activex-log", "")
            error_msg = f"Invalid value for 'web-filter-activex-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_ACTIVEX_LOG)}"
            error_msg += f"\n  → Example: web-filter-activex-log='{{ VALID_BODY_WEB_FILTER_ACTIVEX_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-command-block-log" in payload:
        value = payload["web-filter-command-block-log"]
        if value not in VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-command-block-log", "")
            error_msg = f"Invalid value for 'web-filter-command-block-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG)}"
            error_msg += f"\n  → Example: web-filter-command-block-log='{{ VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-cookie-log" in payload:
        value = payload["web-filter-cookie-log"]
        if value not in VALID_BODY_WEB_FILTER_COOKIE_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-cookie-log", "")
            error_msg = f"Invalid value for 'web-filter-cookie-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_COOKIE_LOG)}"
            error_msg += f"\n  → Example: web-filter-cookie-log='{{ VALID_BODY_WEB_FILTER_COOKIE_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-applet-log" in payload:
        value = payload["web-filter-applet-log"]
        if value not in VALID_BODY_WEB_FILTER_APPLET_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-applet-log", "")
            error_msg = f"Invalid value for 'web-filter-applet-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_APPLET_LOG)}"
            error_msg += f"\n  → Example: web-filter-applet-log='{{ VALID_BODY_WEB_FILTER_APPLET_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-jscript-log" in payload:
        value = payload["web-filter-jscript-log"]
        if value not in VALID_BODY_WEB_FILTER_JSCRIPT_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-jscript-log", "")
            error_msg = f"Invalid value for 'web-filter-jscript-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_JSCRIPT_LOG)}"
            error_msg += f"\n  → Example: web-filter-jscript-log='{{ VALID_BODY_WEB_FILTER_JSCRIPT_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-js-log" in payload:
        value = payload["web-filter-js-log"]
        if value not in VALID_BODY_WEB_FILTER_JS_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-js-log", "")
            error_msg = f"Invalid value for 'web-filter-js-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_JS_LOG)}"
            error_msg += f"\n  → Example: web-filter-js-log='{{ VALID_BODY_WEB_FILTER_JS_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-vbs-log" in payload:
        value = payload["web-filter-vbs-log"]
        if value not in VALID_BODY_WEB_FILTER_VBS_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-vbs-log", "")
            error_msg = f"Invalid value for 'web-filter-vbs-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_VBS_LOG)}"
            error_msg += f"\n  → Example: web-filter-vbs-log='{{ VALID_BODY_WEB_FILTER_VBS_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-unknown-log" in payload:
        value = payload["web-filter-unknown-log"]
        if value not in VALID_BODY_WEB_FILTER_UNKNOWN_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-unknown-log", "")
            error_msg = f"Invalid value for 'web-filter-unknown-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_UNKNOWN_LOG)}"
            error_msg += f"\n  → Example: web-filter-unknown-log='{{ VALID_BODY_WEB_FILTER_UNKNOWN_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-referer-log" in payload:
        value = payload["web-filter-referer-log"]
        if value not in VALID_BODY_WEB_FILTER_REFERER_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-referer-log", "")
            error_msg = f"Invalid value for 'web-filter-referer-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_REFERER_LOG)}"
            error_msg += f"\n  → Example: web-filter-referer-log='{{ VALID_BODY_WEB_FILTER_REFERER_LOG[0] }}'"
            return (False, error_msg)
    if "web-filter-cookie-removal-log" in payload:
        value = payload["web-filter-cookie-removal-log"]
        if value not in VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-filter-cookie-removal-log", "")
            error_msg = f"Invalid value for 'web-filter-cookie-removal-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG)}"
            error_msg += f"\n  → Example: web-filter-cookie-removal-log='{{ VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG[0] }}'"
            return (False, error_msg)
    if "web-url-log" in payload:
        value = payload["web-url-log"]
        if value not in VALID_BODY_WEB_URL_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-url-log", "")
            error_msg = f"Invalid value for 'web-url-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_URL_LOG)}"
            error_msg += f"\n  → Example: web-url-log='{{ VALID_BODY_WEB_URL_LOG[0] }}'"
            return (False, error_msg)
    if "web-invalid-domain-log" in payload:
        value = payload["web-invalid-domain-log"]
        if value not in VALID_BODY_WEB_INVALID_DOMAIN_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-invalid-domain-log", "")
            error_msg = f"Invalid value for 'web-invalid-domain-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_INVALID_DOMAIN_LOG)}"
            error_msg += f"\n  → Example: web-invalid-domain-log='{{ VALID_BODY_WEB_INVALID_DOMAIN_LOG[0] }}'"
            return (False, error_msg)
    if "web-ftgd-err-log" in payload:
        value = payload["web-ftgd-err-log"]
        if value not in VALID_BODY_WEB_FTGD_ERR_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-ftgd-err-log", "")
            error_msg = f"Invalid value for 'web-ftgd-err-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FTGD_ERR_LOG)}"
            error_msg += f"\n  → Example: web-ftgd-err-log='{{ VALID_BODY_WEB_FTGD_ERR_LOG[0] }}'"
            return (False, error_msg)
    if "web-ftgd-quota-usage" in payload:
        value = payload["web-ftgd-quota-usage"]
        if value not in VALID_BODY_WEB_FTGD_QUOTA_USAGE:
            desc = FIELD_DESCRIPTIONS.get("web-ftgd-quota-usage", "")
            error_msg = f"Invalid value for 'web-ftgd-quota-usage': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_FTGD_QUOTA_USAGE)}"
            error_msg += f"\n  → Example: web-ftgd-quota-usage='{{ VALID_BODY_WEB_FTGD_QUOTA_USAGE[0] }}'"
            return (False, error_msg)
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            desc = FIELD_DESCRIPTIONS.get("extended-log", "")
            error_msg = f"Invalid value for 'extended-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENDED_LOG)}"
            error_msg += f"\n  → Example: extended-log='{{ VALID_BODY_EXTENDED_LOG[0] }}'"
            return (False, error_msg)
    if "web-extended-all-action-log" in payload:
        value = payload["web-extended-all-action-log"]
        if value not in VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-extended-all-action-log", "")
            error_msg = f"Invalid value for 'web-extended-all-action-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG)}"
            error_msg += f"\n  → Example: web-extended-all-action-log='{{ VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG[0] }}'"
            return (False, error_msg)
    if "web-antiphishing-log" in payload:
        value = payload["web-antiphishing-log"]
        if value not in VALID_BODY_WEB_ANTIPHISHING_LOG:
            desc = FIELD_DESCRIPTIONS.get("web-antiphishing-log", "")
            error_msg = f"Invalid value for 'web-antiphishing-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEB_ANTIPHISHING_LOG)}"
            error_msg += f"\n  → Example: web-antiphishing-log='{{ VALID_BODY_WEB_ANTIPHISHING_LOG[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_webfilter_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update webfilter/profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_webfilter_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid value for 'feature-set'='{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )
    if "options" in payload:
        value = payload["options"]
        if value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid value for 'options'='{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )
    if "https-replacemsg" in payload:
        value = payload["https-replacemsg"]
        if value not in VALID_BODY_HTTPS_REPLACEMSG:
            return (
                False,
                f"Invalid value for 'https-replacemsg'='{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_REPLACEMSG)}",
            )
    if "web-flow-log-encoding" in payload:
        value = payload["web-flow-log-encoding"]
        if value not in VALID_BODY_WEB_FLOW_LOG_ENCODING:
            return (
                False,
                f"Invalid value for 'web-flow-log-encoding'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FLOW_LOG_ENCODING)}",
            )
    if "ovrd-perm" in payload:
        value = payload["ovrd-perm"]
        if value not in VALID_BODY_OVRD_PERM:
            return (
                False,
                f"Invalid value for 'ovrd-perm'='{value}'. Must be one of: {', '.join(VALID_BODY_OVRD_PERM)}",
            )
    if "post-action" in payload:
        value = payload["post-action"]
        if value not in VALID_BODY_POST_ACTION:
            return (
                False,
                f"Invalid value for 'post-action'='{value}'. Must be one of: {', '.join(VALID_BODY_POST_ACTION)}",
            )
    if "wisp" in payload:
        value = payload["wisp"]
        if value not in VALID_BODY_WISP:
            return (
                False,
                f"Invalid value for 'wisp'='{value}'. Must be one of: {', '.join(VALID_BODY_WISP)}",
            )
    if "wisp-algorithm" in payload:
        value = payload["wisp-algorithm"]
        if value not in VALID_BODY_WISP_ALGORITHM:
            return (
                False,
                f"Invalid value for 'wisp-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_WISP_ALGORITHM)}",
            )
    if "log-all-url" in payload:
        value = payload["log-all-url"]
        if value not in VALID_BODY_LOG_ALL_URL:
            return (
                False,
                f"Invalid value for 'log-all-url'='{value}'. Must be one of: {', '.join(VALID_BODY_LOG_ALL_URL)}",
            )
    if "web-content-log" in payload:
        value = payload["web-content-log"]
        if value not in VALID_BODY_WEB_CONTENT_LOG:
            return (
                False,
                f"Invalid value for 'web-content-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_CONTENT_LOG)}",
            )
    if "web-filter-activex-log" in payload:
        value = payload["web-filter-activex-log"]
        if value not in VALID_BODY_WEB_FILTER_ACTIVEX_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-activex-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_ACTIVEX_LOG)}",
            )
    if "web-filter-command-block-log" in payload:
        value = payload["web-filter-command-block-log"]
        if value not in VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-command-block-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COMMAND_BLOCK_LOG)}",
            )
    if "web-filter-cookie-log" in payload:
        value = payload["web-filter-cookie-log"]
        if value not in VALID_BODY_WEB_FILTER_COOKIE_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-cookie-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COOKIE_LOG)}",
            )
    if "web-filter-applet-log" in payload:
        value = payload["web-filter-applet-log"]
        if value not in VALID_BODY_WEB_FILTER_APPLET_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-applet-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_APPLET_LOG)}",
            )
    if "web-filter-jscript-log" in payload:
        value = payload["web-filter-jscript-log"]
        if value not in VALID_BODY_WEB_FILTER_JSCRIPT_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-jscript-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_JSCRIPT_LOG)}",
            )
    if "web-filter-js-log" in payload:
        value = payload["web-filter-js-log"]
        if value not in VALID_BODY_WEB_FILTER_JS_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-js-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_JS_LOG)}",
            )
    if "web-filter-vbs-log" in payload:
        value = payload["web-filter-vbs-log"]
        if value not in VALID_BODY_WEB_FILTER_VBS_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-vbs-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_VBS_LOG)}",
            )
    if "web-filter-unknown-log" in payload:
        value = payload["web-filter-unknown-log"]
        if value not in VALID_BODY_WEB_FILTER_UNKNOWN_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-unknown-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_UNKNOWN_LOG)}",
            )
    if "web-filter-referer-log" in payload:
        value = payload["web-filter-referer-log"]
        if value not in VALID_BODY_WEB_FILTER_REFERER_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-referer-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_REFERER_LOG)}",
            )
    if "web-filter-cookie-removal-log" in payload:
        value = payload["web-filter-cookie-removal-log"]
        if value not in VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG:
            return (
                False,
                f"Invalid value for 'web-filter-cookie-removal-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FILTER_COOKIE_REMOVAL_LOG)}",
            )
    if "web-url-log" in payload:
        value = payload["web-url-log"]
        if value not in VALID_BODY_WEB_URL_LOG:
            return (
                False,
                f"Invalid value for 'web-url-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_URL_LOG)}",
            )
    if "web-invalid-domain-log" in payload:
        value = payload["web-invalid-domain-log"]
        if value not in VALID_BODY_WEB_INVALID_DOMAIN_LOG:
            return (
                False,
                f"Invalid value for 'web-invalid-domain-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_INVALID_DOMAIN_LOG)}",
            )
    if "web-ftgd-err-log" in payload:
        value = payload["web-ftgd-err-log"]
        if value not in VALID_BODY_WEB_FTGD_ERR_LOG:
            return (
                False,
                f"Invalid value for 'web-ftgd-err-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FTGD_ERR_LOG)}",
            )
    if "web-ftgd-quota-usage" in payload:
        value = payload["web-ftgd-quota-usage"]
        if value not in VALID_BODY_WEB_FTGD_QUOTA_USAGE:
            return (
                False,
                f"Invalid value for 'web-ftgd-quota-usage'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_FTGD_QUOTA_USAGE)}",
            )
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid value for 'extended-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )
    if "web-extended-all-action-log" in payload:
        value = payload["web-extended-all-action-log"]
        if value not in VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG:
            return (
                False,
                f"Invalid value for 'web-extended-all-action-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_EXTENDED_ALL_ACTION_LOG)}",
            )
    if "web-antiphishing-log" in payload:
        value = payload["web-antiphishing-log"]
        if value not in VALID_BODY_WEB_ANTIPHISHING_LOG:
            return (
                False,
                f"Invalid value for 'web-antiphishing-log'='{value}'. Must be one of: {', '.join(VALID_BODY_WEB_ANTIPHISHING_LOG)}",
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
    "endpoint": "webfilter/profile",
    "category": "cmdb",
    "api_path": "webfilter/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure Web filter profiles.",
    "total_fields": 35,
    "required_fields_count": 1,
    "fields_with_defaults_count": 29,
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
