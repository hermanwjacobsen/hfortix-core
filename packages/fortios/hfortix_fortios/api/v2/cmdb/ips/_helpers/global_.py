"""Validation helpers for ips/global_ - Auto-generated"""

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
    "fail-open": "disable",
    "database": "extended",
    "traffic-submit": "disable",
    "anomaly-mode": "continuous",
    "session-limit-mode": "heuristic",
    "socket-size": 256,
    "engine-count": 0,
    "sync-session-ttl": "enable",
    "deep-app-insp-timeout": 0,
    "deep-app-insp-db-limit": 0,
    "exclude-signatures": "ot",
    "packet-log-queue-depth": 128,
    "ngfw-max-scan-range": 4096,
    "av-mem-limit": 0,
    "machine-learning-detection": "enable",
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
    "fail-open": "option",  # Enable to allow traffic if the IPS buffer is full. Default i
    "database": "option",  # Regular or extended IPS database. Regular protects against t
    "traffic-submit": "option",  # Enable/disable submitting attack data found by this FortiGat
    "anomaly-mode": "option",  # Global blocking mode for rate-based anomalies.
    "session-limit-mode": "option",  # Method of counting concurrent sessions used by session limit
    "socket-size": "integer",  # IPS socket buffer size. Max and default value depend on avai
    "engine-count": "integer",  # Number of IPS engines running. If set to the default value o
    "sync-session-ttl": "option",  # Enable/disable use of kernel session TTL for IPS sessions.
    "deep-app-insp-timeout": "integer",  # Timeout for Deep application inspection (1 - 2147483647 sec.
    "deep-app-insp-db-limit": "integer",  # Limit on number of entries in deep application inspection da
    "exclude-signatures": "option",  # Excluded signatures.
    "packet-log-queue-depth": "integer",  # Packet/pcap log queue depth per IPS engine.
    "ngfw-max-scan-range": "integer",  # NGFW policy-mode app detection threshold.
    "av-mem-limit": "integer",  # Maximum percentage of system memory allowed for use on AV sc
    "machine-learning-detection": "option",  # Enable/disable machine learning detection.
    "tls-active-probe": "string",  # TLS active probe configuration.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "fail-open": "Enable to allow traffic if the IPS buffer is full. Default is disable and IPS traffic is blocked when the IPS buffer is full.",
    "database": "Regular or extended IPS database. Regular protects against the latest common and in-the-wild attacks. Extended includes protection from legacy attacks.",
    "traffic-submit": "Enable/disable submitting attack data found by this FortiGate to FortiGuard.",
    "anomaly-mode": "Global blocking mode for rate-based anomalies.",
    "session-limit-mode": "Method of counting concurrent sessions used by session limit anomalies. Choose between greater accuracy (accurate) or improved performance (heuristics).",
    "socket-size": "IPS socket buffer size. Max and default value depend on available memory. Can be changed to tune performance.",
    "engine-count": "Number of IPS engines running. If set to the default value of 0, FortiOS sets the number to optimize performance depending on the number of CPU cores.",
    "sync-session-ttl": "Enable/disable use of kernel session TTL for IPS sessions.",
    "deep-app-insp-timeout": "Timeout for Deep application inspection (1 - 2147483647 sec., 0 = use recommended setting).",
    "deep-app-insp-db-limit": "Limit on number of entries in deep application inspection database (1 - 2147483647, use recommended setting = 0).",
    "exclude-signatures": "Excluded signatures.",
    "packet-log-queue-depth": "Packet/pcap log queue depth per IPS engine.",
    "ngfw-max-scan-range": "NGFW policy-mode app detection threshold.",
    "av-mem-limit": "Maximum percentage of system memory allowed for use on AV scanning (10 - 50, default = zero). To disable set to zero. When disabled, there is no limit on the AV memory usage.",
    "machine-learning-detection": "Enable/disable machine learning detection.",
    "tls-active-probe": "TLS active probe configuration.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "socket-size": {"type": "integer", "min": 0, "max": 512},
    "engine-count": {"type": "integer", "min": 0, "max": 255},
    "deep-app-insp-timeout": {"type": "integer", "min": 0, "max": 2147483647},
    "deep-app-insp-db-limit": {"type": "integer", "min": 0, "max": 2147483647},
    "packet-log-queue-depth": {"type": "integer", "min": 128, "max": 4096},
    "ngfw-max-scan-range": {"type": "integer", "min": 0, "max": 4294967295},
    "av-mem-limit": {"type": "integer", "min": 10, "max": 50},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "tls-active-probe": {
        "interface-select-method": {
            "type": "option",
            "help": "Specify how to select outgoing interface to reach server.",
            "default": "auto",
            "options": [{"help": "Set outgoing interface automatically.", "label": "Auto", "name": "auto"}, {"help": "Set outgoing interface by SD-WAN or policy routing rules.", "label": "Sdwan", "name": "sdwan"}, {"help": "Set outgoing interface manually.", "label": "Specify", "name": "specify"}],
        },
        "interface": {
            "type": "string",
            "help": "Specify outgoing interface to reach server.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "vdom": {
            "type": "string",
            "help": "Virtual domain name for TLS active probe.",
            "required": True,
            "default": "",
            "max_length": 31,
        },
        "source-ip": {
            "type": "ipv4-address",
            "help": "Source IP address used for TLS active probe.",
            "default": "0.0.0.0",
        },
        "source-ip6": {
            "type": "ipv6-address",
            "help": "Source IPv6 address used for TLS active probe.",
            "default": "::",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FAIL_OPEN = [
    "enable",  # Enable IPS fail open.
    "disable",  # Disable IPS fail open.
]
VALID_BODY_DATABASE = [
    "regular",  # IPS regular database package.
    "extended",  # IPS extended database package.
]
VALID_BODY_TRAFFIC_SUBMIT = [
    "enable",  # Enable traffic submit.
    "disable",  # Disable traffic submit.
]
VALID_BODY_ANOMALY_MODE = [
    "periodical",  # After an anomaly is detected, allow the number of packets per second according to the anomaly configuration.
    "continuous",  # Block packets once an anomaly is detected. Overrides individual anomaly settings.
]
VALID_BODY_SESSION_LIMIT_MODE = [
    "accurate",  # Accurately count concurrent sessions, demands more resources.
    "heuristic",  # Use heuristics to estimate the number of concurrent sessions. Acceptable in most cases.
]
VALID_BODY_SYNC_SESSION_TTL = [
    "enable",  # Enable use of kernel session TTL for IPS sessions.
    "disable",  # Disable use of kernel session TTL for IPS sessions.
]
VALID_BODY_EXCLUDE_SIGNATURES = [
    "none",  # No signatures excluded.
    "ot",  # Exclude ot signatures.
]
VALID_BODY_MACHINE_LEARNING_DETECTION = [
    "enable",  # Enable ML detection.
    "disable",  # Disable ML detection.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ips_global__get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for ips/global_."""
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
    """Validate required fields for ips/global_."""
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


def validate_ips_global__post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new ips/global_ object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "fail-open" in payload:
        value = payload["fail-open"]
        if value not in VALID_BODY_FAIL_OPEN:
            desc = FIELD_DESCRIPTIONS.get("fail-open", "")
            error_msg = f"Invalid value for 'fail-open': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FAIL_OPEN)}"
            error_msg += f"\n  → Example: fail-open='{{ VALID_BODY_FAIL_OPEN[0] }}'"
            return (False, error_msg)
    if "database" in payload:
        value = payload["database"]
        if value not in VALID_BODY_DATABASE:
            desc = FIELD_DESCRIPTIONS.get("database", "")
            error_msg = f"Invalid value for 'database': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DATABASE)}"
            error_msg += f"\n  → Example: database='{{ VALID_BODY_DATABASE[0] }}'"
            return (False, error_msg)
    if "traffic-submit" in payload:
        value = payload["traffic-submit"]
        if value not in VALID_BODY_TRAFFIC_SUBMIT:
            desc = FIELD_DESCRIPTIONS.get("traffic-submit", "")
            error_msg = f"Invalid value for 'traffic-submit': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_TRAFFIC_SUBMIT)}"
            error_msg += f"\n  → Example: traffic-submit='{{ VALID_BODY_TRAFFIC_SUBMIT[0] }}'"
            return (False, error_msg)
    if "anomaly-mode" in payload:
        value = payload["anomaly-mode"]
        if value not in VALID_BODY_ANOMALY_MODE:
            desc = FIELD_DESCRIPTIONS.get("anomaly-mode", "")
            error_msg = f"Invalid value for 'anomaly-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANOMALY_MODE)}"
            error_msg += f"\n  → Example: anomaly-mode='{{ VALID_BODY_ANOMALY_MODE[0] }}'"
            return (False, error_msg)
    if "session-limit-mode" in payload:
        value = payload["session-limit-mode"]
        if value not in VALID_BODY_SESSION_LIMIT_MODE:
            desc = FIELD_DESCRIPTIONS.get("session-limit-mode", "")
            error_msg = f"Invalid value for 'session-limit-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SESSION_LIMIT_MODE)}"
            error_msg += f"\n  → Example: session-limit-mode='{{ VALID_BODY_SESSION_LIMIT_MODE[0] }}'"
            return (False, error_msg)
    if "sync-session-ttl" in payload:
        value = payload["sync-session-ttl"]
        if value not in VALID_BODY_SYNC_SESSION_TTL:
            desc = FIELD_DESCRIPTIONS.get("sync-session-ttl", "")
            error_msg = f"Invalid value for 'sync-session-ttl': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SYNC_SESSION_TTL)}"
            error_msg += f"\n  → Example: sync-session-ttl='{{ VALID_BODY_SYNC_SESSION_TTL[0] }}'"
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
    if "machine-learning-detection" in payload:
        value = payload["machine-learning-detection"]
        if value not in VALID_BODY_MACHINE_LEARNING_DETECTION:
            desc = FIELD_DESCRIPTIONS.get("machine-learning-detection", "")
            error_msg = f"Invalid value for 'machine-learning-detection': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MACHINE_LEARNING_DETECTION)}"
            error_msg += f"\n  → Example: machine-learning-detection='{{ VALID_BODY_MACHINE_LEARNING_DETECTION[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ips_global__put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update ips/global_."""
    # Step 1: Validate enum values
    if "fail-open" in payload:
        value = payload["fail-open"]
        if value not in VALID_BODY_FAIL_OPEN:
            return (
                False,
                f"Invalid value for 'fail-open'='{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_OPEN)}",
            )
    if "database" in payload:
        value = payload["database"]
        if value not in VALID_BODY_DATABASE:
            return (
                False,
                f"Invalid value for 'database'='{value}'. Must be one of: {', '.join(VALID_BODY_DATABASE)}",
            )
    if "traffic-submit" in payload:
        value = payload["traffic-submit"]
        if value not in VALID_BODY_TRAFFIC_SUBMIT:
            return (
                False,
                f"Invalid value for 'traffic-submit'='{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_SUBMIT)}",
            )
    if "anomaly-mode" in payload:
        value = payload["anomaly-mode"]
        if value not in VALID_BODY_ANOMALY_MODE:
            return (
                False,
                f"Invalid value for 'anomaly-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_ANOMALY_MODE)}",
            )
    if "session-limit-mode" in payload:
        value = payload["session-limit-mode"]
        if value not in VALID_BODY_SESSION_LIMIT_MODE:
            return (
                False,
                f"Invalid value for 'session-limit-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SESSION_LIMIT_MODE)}",
            )
    if "sync-session-ttl" in payload:
        value = payload["sync-session-ttl"]
        if value not in VALID_BODY_SYNC_SESSION_TTL:
            return (
                False,
                f"Invalid value for 'sync-session-ttl'='{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_SESSION_TTL)}",
            )
    if "exclude-signatures" in payload:
        value = payload["exclude-signatures"]
        if value not in VALID_BODY_EXCLUDE_SIGNATURES:
            return (
                False,
                f"Invalid value for 'exclude-signatures'='{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE_SIGNATURES)}",
            )
    if "machine-learning-detection" in payload:
        value = payload["machine-learning-detection"]
        if value not in VALID_BODY_MACHINE_LEARNING_DETECTION:
            return (
                False,
                f"Invalid value for 'machine-learning-detection'='{value}'. Must be one of: {', '.join(VALID_BODY_MACHINE_LEARNING_DETECTION)}",
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
    "endpoint": "ips/global_",
    "category": "cmdb",
    "api_path": "ips/global",
    "help": "Configure IPS global parameter.",
    "total_fields": 16,
    "required_fields_count": 0,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
