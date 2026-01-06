"""Validation helpers for certificate/hsm_local - Auto-generated"""

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
    "name",  # Name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "comments": "",
    "vendor": "unknown",
    "api-version": "unknown",
    "certificate": "",
    "range": "global",
    "source": "user",
    "gch-url": "",
    "gch-project": "",
    "gch-location": "",
    "gch-keyring": "",
    "gch-cryptokey": "",
    "gch-cryptokey-version": "",
    "gch-cloud-service-name": "",
    "gch-cryptokey-algorithm": "rsa-sign-pkcs1-2048-sha256",
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
    "name": "string",  # Name.
    "comments": "string",  # Comment.
    "vendor": "option",  # HSM vendor.
    "api-version": "option",  # API version for communicating with HSM.
    "certificate": "user",  # PEM format certificate.
    "range": "option",  # Either a global or VDOM IP address range for the certificate
    "source": "option",  # Certificate source type.
    "gch-url": "string",  # Google Cloud HSM key URL (e.g. "https://cloudkms.googleapis.
    "gch-project": "string",  # Google Cloud HSM project ID.
    "gch-location": "string",  # Google Cloud HSM location.
    "gch-keyring": "string",  # Google Cloud HSM keyring.
    "gch-cryptokey": "string",  # Google Cloud HSM cryptokey.
    "gch-cryptokey-version": "string",  # Google Cloud HSM cryptokey version.
    "gch-cloud-service-name": "string",  # Cloud service config name to generate access token.
    "gch-cryptokey-algorithm": "option",  # Google Cloud HSM cryptokey algorithm.
    "details": "key",  # Print hsm-local certificate detailed information.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "comments": "Comment.",
    "vendor": "HSM vendor.",
    "api-version": "API version for communicating with HSM.",
    "certificate": "PEM format certificate.",
    "range": "Either a global or VDOM IP address range for the certificate.",
    "source": "Certificate source type.",
    "gch-url": "Google Cloud HSM key URL (e.g. \"https://cloudkms.googleapis.com/v1/projects/sampleproject/locations/samplelocation/keyRings/samplekeyring/cryptoKeys/sampleKeyName/cryptoKeyVersions/1\").",
    "gch-project": "Google Cloud HSM project ID.",
    "gch-location": "Google Cloud HSM location.",
    "gch-keyring": "Google Cloud HSM keyring.",
    "gch-cryptokey": "Google Cloud HSM cryptokey.",
    "gch-cryptokey-version": "Google Cloud HSM cryptokey version.",
    "gch-cloud-service-name": "Cloud service config name to generate access token.",
    "gch-cryptokey-algorithm": "Google Cloud HSM cryptokey algorithm.",
    "details": "Print hsm-local certificate detailed information.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comments": {"type": "string", "max_length": 511},
    "gch-url": {"type": "string", "max_length": 1024},
    "gch-project": {"type": "string", "max_length": 31},
    "gch-location": {"type": "string", "max_length": 63},
    "gch-keyring": {"type": "string", "max_length": 63},
    "gch-cryptokey": {"type": "string", "max_length": 63},
    "gch-cryptokey-version": {"type": "string", "max_length": 31},
    "gch-cloud-service-name": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "details": {
        "<certficate name>": {
            "type": "value",
            "help": "Hsm-local certificate name.",
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_VENDOR = [
    "unknown",  # Unknown type of HSM.
    "gch",  # Google Cloud HSM.
]
VALID_BODY_API_VERSION = [
    "unknown",  # Unknown API version.
    "gch-default",  # Google Cloud HSM default API.
]
VALID_BODY_RANGE = [
    "global",  # Global range.
    "vdom",  # VDOM IP address range.
]
VALID_BODY_SOURCE = [
    "factory",  # Factory installed certificate.
    "user",  # User generated certificate.
    "bundle",  # Bundle file certificate.
]
VALID_BODY_GCH_CRYPTOKEY_ALGORITHM = [
    "rsa-sign-pkcs1-2048-sha256",  # 2048 bit RSA - PKCS#1 v1.5 padding - SHA256 Digest.
    "rsa-sign-pkcs1-3072-sha256",  # 3072 bit RSA - PKCS#1 v1.5 padding - SHA256 Digest.
    "rsa-sign-pkcs1-4096-sha256",  # 4096 bit RSA - PKCS#1 v1.5 padding - SHA256 Digest.
    "rsa-sign-pkcs1-4096-sha512",  # 4096 bit RSA - PKCS#1 v1.5 padding - SHA512 Digest.
    "rsa-sign-pss-2048-sha256",  # 2048 bit RSA - PSS padding - SHA256 Digest.
    "rsa-sign-pss-3072-sha256",  # 3072 bit RSA - PSS padding - SHA256 Digest.
    "rsa-sign-pss-4096-sha256",  # 4096 bit RSA - PSS padding - SHA256 Digest.
    "rsa-sign-pss-4096-sha512",  # 4096 bit RSA - PSS padding - SHA256 Digest.
    "ec-sign-p256-sha256",  # Elliptic Curve P-256 - SHA256 Digest.
    "ec-sign-p384-sha384",  # Elliptic Curve P-384 - SHA384 Digest.
    "ec-sign-secp256k1-sha256",  # Elliptic Curvesecp256k1 - SHA256 Digest.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_hsm_local_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for certificate/hsm_local."""
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
    """Validate required fields for certificate/hsm_local."""
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


def validate_certificate_hsm_local_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new certificate/hsm_local object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "vendor" in payload:
        value = payload["vendor"]
        if value not in VALID_BODY_VENDOR:
            desc = FIELD_DESCRIPTIONS.get("vendor", "")
            error_msg = f"Invalid value for 'vendor': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VENDOR)}"
            error_msg += f"\n  → Example: vendor='{{ VALID_BODY_VENDOR[0] }}'"
            return (False, error_msg)
    if "api-version" in payload:
        value = payload["api-version"]
        if value not in VALID_BODY_API_VERSION:
            desc = FIELD_DESCRIPTIONS.get("api-version", "")
            error_msg = f"Invalid value for 'api-version': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_API_VERSION)}"
            error_msg += f"\n  → Example: api-version='{{ VALID_BODY_API_VERSION[0] }}'"
            return (False, error_msg)
    if "range" in payload:
        value = payload["range"]
        if value not in VALID_BODY_RANGE:
            desc = FIELD_DESCRIPTIONS.get("range", "")
            error_msg = f"Invalid value for 'range': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RANGE)}"
            error_msg += f"\n  → Example: range='{{ VALID_BODY_RANGE[0] }}'"
            return (False, error_msg)
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            desc = FIELD_DESCRIPTIONS.get("source", "")
            error_msg = f"Invalid value for 'source': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SOURCE)}"
            error_msg += f"\n  → Example: source='{{ VALID_BODY_SOURCE[0] }}'"
            return (False, error_msg)
    if "gch-cryptokey-algorithm" in payload:
        value = payload["gch-cryptokey-algorithm"]
        if value not in VALID_BODY_GCH_CRYPTOKEY_ALGORITHM:
            desc = FIELD_DESCRIPTIONS.get("gch-cryptokey-algorithm", "")
            error_msg = f"Invalid value for 'gch-cryptokey-algorithm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GCH_CRYPTOKEY_ALGORITHM)}"
            error_msg += f"\n  → Example: gch-cryptokey-algorithm='{{ VALID_BODY_GCH_CRYPTOKEY_ALGORITHM[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_certificate_hsm_local_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update certificate/hsm_local."""
    # Step 1: Validate enum values
    if "vendor" in payload:
        value = payload["vendor"]
        if value not in VALID_BODY_VENDOR:
            return (
                False,
                f"Invalid value for 'vendor'='{value}'. Must be one of: {', '.join(VALID_BODY_VENDOR)}",
            )
    if "api-version" in payload:
        value = payload["api-version"]
        if value not in VALID_BODY_API_VERSION:
            return (
                False,
                f"Invalid value for 'api-version'='{value}'. Must be one of: {', '.join(VALID_BODY_API_VERSION)}",
            )
    if "range" in payload:
        value = payload["range"]
        if value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid value for 'range'='{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )
    if "source" in payload:
        value = payload["source"]
        if value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid value for 'source'='{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )
    if "gch-cryptokey-algorithm" in payload:
        value = payload["gch-cryptokey-algorithm"]
        if value not in VALID_BODY_GCH_CRYPTOKEY_ALGORITHM:
            return (
                False,
                f"Invalid value for 'gch-cryptokey-algorithm'='{value}'. Must be one of: {', '.join(VALID_BODY_GCH_CRYPTOKEY_ALGORITHM)}",
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
    "endpoint": "certificate/hsm_local",
    "category": "cmdb",
    "api_path": "certificate/hsm-local",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Local certificates whose keys are stored on HSM.",
    "total_fields": 16,
    "required_fields_count": 1,
    "fields_with_defaults_count": 15,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
