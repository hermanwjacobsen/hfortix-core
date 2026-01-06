"""Validation helpers for user/saml - Auto-generated"""

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
    "entity-id",  # SP entity ID.
    "single-sign-on-url",  # SP single sign-on URL.
    "idp-entity-id",  # IDP entity ID.
    "idp-single-sign-on-url",  # IDP single sign-on URL.
    "idp-cert",  # IDP Certificate name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "cert": "",
    "entity-id": "",
    "single-sign-on-url": "",
    "single-logout-url": "",
    "idp-entity-id": "",
    "idp-single-sign-on-url": "",
    "idp-single-logout-url": "",
    "idp-cert": "",
    "scim-client": "",
    "scim-user-attr-type": "user-name",
    "scim-group-attr-type": "display-name",
    "user-name": "",
    "group-name": "",
    "digest-method": "sha1",
    "require-signed-resp-and-asrt": "disable",
    "limit-relaystate": "disable",
    "clock-tolerance": 15,
    "adfs-claim": "disable",
    "user-claim-type": "upn",
    "group-claim-type": "group",
    "reauth": "disable",
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
    "name": "string",  # SAML server entry name.
    "cert": "string",  # Certificate to sign SAML messages.
    "entity-id": "string",  # SP entity ID.
    "single-sign-on-url": "string",  # SP single sign-on URL.
    "single-logout-url": "string",  # SP single logout URL.
    "idp-entity-id": "string",  # IDP entity ID.
    "idp-single-sign-on-url": "string",  # IDP single sign-on URL.
    "idp-single-logout-url": "string",  # IDP single logout url.
    "idp-cert": "string",  # IDP Certificate name.
    "scim-client": "string",  # SCIM client name.
    "scim-user-attr-type": "option",  # User attribute type used to match SCIM users (default = user
    "scim-group-attr-type": "option",  # Group attribute type used to match SCIM groups (default = di
    "user-name": "string",  # User name in assertion statement.
    "group-name": "string",  # Group name in assertion statement.
    "digest-method": "option",  # Digest method algorithm.
    "require-signed-resp-and-asrt": "option",  # Require both response and assertion from IDP to be signed wh
    "limit-relaystate": "option",  # Enable/disable limiting of relay-state parameter when it exc
    "clock-tolerance": "integer",  # Clock skew tolerance in seconds (0 - 300, default = 15, 0 = 
    "adfs-claim": "option",  # Enable/disable ADFS Claim for user/group attribute in assert
    "user-claim-type": "option",  # User name claim in assertion statement.
    "group-claim-type": "option",  # Group claim in assertion statement.
    "reauth": "option",  # Enable/disable signalling of IDP to force user re-authentica
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "SAML server entry name.",
    "cert": "Certificate to sign SAML messages.",
    "entity-id": "SP entity ID.",
    "single-sign-on-url": "SP single sign-on URL.",
    "single-logout-url": "SP single logout URL.",
    "idp-entity-id": "IDP entity ID.",
    "idp-single-sign-on-url": "IDP single sign-on URL.",
    "idp-single-logout-url": "IDP single logout url.",
    "idp-cert": "IDP Certificate name.",
    "scim-client": "SCIM client name.",
    "scim-user-attr-type": "User attribute type used to match SCIM users (default = user-name).",
    "scim-group-attr-type": "Group attribute type used to match SCIM groups (default = display-name).",
    "user-name": "User name in assertion statement.",
    "group-name": "Group name in assertion statement.",
    "digest-method": "Digest method algorithm.",
    "require-signed-resp-and-asrt": "Require both response and assertion from IDP to be signed when FGT acts as SP (default = disable).",
    "limit-relaystate": "Enable/disable limiting of relay-state parameter when it exceeds SAML 2.0 specification limits (80 bytes).",
    "clock-tolerance": "Clock skew tolerance in seconds (0 - 300, default = 15, 0 = no tolerance).",
    "adfs-claim": "Enable/disable ADFS Claim for user/group attribute in assertion statement (default = disable).",
    "user-claim-type": "User name claim in assertion statement.",
    "group-claim-type": "Group claim in assertion statement.",
    "reauth": "Enable/disable signalling of IDP to force user re-authentication (default = disable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "cert": {"type": "string", "max_length": 35},
    "entity-id": {"type": "string", "max_length": 255},
    "single-sign-on-url": {"type": "string", "max_length": 255},
    "single-logout-url": {"type": "string", "max_length": 255},
    "idp-entity-id": {"type": "string", "max_length": 255},
    "idp-single-sign-on-url": {"type": "string", "max_length": 255},
    "idp-single-logout-url": {"type": "string", "max_length": 255},
    "idp-cert": {"type": "string", "max_length": 35},
    "scim-client": {"type": "string", "max_length": 35},
    "user-name": {"type": "string", "max_length": 255},
    "group-name": {"type": "string", "max_length": 255},
    "clock-tolerance": {"type": "integer", "min": 0, "max": 300},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
}


# Valid enum values from API documentation
VALID_BODY_SCIM_USER_ATTR_TYPE = [
    "user-name",  # User name.
    "display-name",  # Display name.
    "external-id",  # External ID.
    "email",  # Email.
]
VALID_BODY_SCIM_GROUP_ATTR_TYPE = [
    "display-name",  # Display name.
    "external-id",  # External ID.
]
VALID_BODY_DIGEST_METHOD = [
    "sha1",  # Digest Method Algorithm is SHA1.
    "sha256",  # Digest Method Algorithm is SHA256.
]
VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT = [
    "enable",  # Both response and assertion must be signed and valid.
    "disable",  # At least one of response or assertion must be signed and valid.
]
VALID_BODY_LIMIT_RELAYSTATE = [
    "enable",  # Enable limiting of relay-state parameter when it exceeds SAML 2.0 specification limits (80 bytes).
    "disable",  # Disable limiting of relay-state parameter when it exceeds SAML 2.0 specification limits (80 bytes).
]
VALID_BODY_ADFS_CLAIM = [
    "enable",  # Enable ADFS Claim for user/group attribute in assertion statement.
    "disable",  # Disable ADFS Claim for user/group attribute in assertion statement.
]
VALID_BODY_USER_CLAIM_TYPE = [
    "email",  # E-mail address of the user.
    "given-name",  # Given name of the user.
    "name",  # Unique name of the user.
    "upn",  # User principal name (UPN) of the user.
    "common-name",  # Common name of the user.
    "email-adfs-1x",  # E-mail address of the user when interoperating with AD FS 1.1 or ADFS 1.0.
    "group",  # Group that the user is a member of.
    "upn-adfs-1x",  # User principal name (UPN) of the user.
    "role",  # Role that the user has.
    "sur-name",  # Surname of the user
    "ppid",  # Private identifier of the user.
    "name-identifier",  # SAML name identifier of the user.
    "authentication-method",  # Method used to authenticate the user.
    "deny-only-group-sid",  # Deny-only group SID of the user.
    "deny-only-primary-sid",  # Deny-only primary SID of the user.
    "deny-only-primary-group-sid",  # Deny-only primary group SID of the user.
    "group-sid",  # Group SID of the user.
    "primary-group-sid",  # Primary group SID of the user.
    "primary-sid",  # Primary SID of the user.
    "windows-account-name",  # Domain account name of the user in the form of <domain>\<user>.
]
VALID_BODY_GROUP_CLAIM_TYPE = [
    "email",  # E-mail address of the user.
    "given-name",  # Given name of the user.
    "name",  # Unique name of the user.
    "upn",  # User principal name (UPN) of the user.
    "common-name",  # Common name of the user.
    "email-adfs-1x",  # E-mail address of the user when interoperating with AD FS 1.1 or ADFS 1.0.
    "group",  # Group that the user is a member of.
    "upn-adfs-1x",  # User principal name (UPN) of the user.
    "role",  # Role that the user has.
    "sur-name",  # Surname of the user
    "ppid",  # Private identifier of the user.
    "name-identifier",  # SAML name identifier of the user.
    "authentication-method",  # Method used to authenticate the user.
    "deny-only-group-sid",  # Deny-only group SID of the user.
    "deny-only-primary-sid",  # Deny-only primary SID of the user.
    "deny-only-primary-group-sid",  # Deny-only primary group SID of the user.
    "group-sid",  # Group SID of the user.
    "primary-group-sid",  # Primary group SID of the user.
    "primary-sid",  # Primary SID of the user.
    "windows-account-name",  # Domain account name of the user in the form of <domain>\<user>.
]
VALID_BODY_REAUTH = [
    "enable",  # Enable signalling of IDP to force user re-authentication.
    "disable",  # Disable signalling of IDP to force user re-authentication.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_user_saml_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for user/saml."""
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
    """Validate required fields for user/saml."""
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


def validate_user_saml_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new user/saml object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "scim-user-attr-type" in payload:
        value = payload["scim-user-attr-type"]
        if value not in VALID_BODY_SCIM_USER_ATTR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("scim-user-attr-type", "")
            error_msg = f"Invalid value for 'scim-user-attr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCIM_USER_ATTR_TYPE)}"
            error_msg += f"\n  → Example: scim-user-attr-type='{{ VALID_BODY_SCIM_USER_ATTR_TYPE[0] }}'"
            return (False, error_msg)
    if "scim-group-attr-type" in payload:
        value = payload["scim-group-attr-type"]
        if value not in VALID_BODY_SCIM_GROUP_ATTR_TYPE:
            desc = FIELD_DESCRIPTIONS.get("scim-group-attr-type", "")
            error_msg = f"Invalid value for 'scim-group-attr-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCIM_GROUP_ATTR_TYPE)}"
            error_msg += f"\n  → Example: scim-group-attr-type='{{ VALID_BODY_SCIM_GROUP_ATTR_TYPE[0] }}'"
            return (False, error_msg)
    if "digest-method" in payload:
        value = payload["digest-method"]
        if value not in VALID_BODY_DIGEST_METHOD:
            desc = FIELD_DESCRIPTIONS.get("digest-method", "")
            error_msg = f"Invalid value for 'digest-method': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DIGEST_METHOD)}"
            error_msg += f"\n  → Example: digest-method='{{ VALID_BODY_DIGEST_METHOD[0] }}'"
            return (False, error_msg)
    if "require-signed-resp-and-asrt" in payload:
        value = payload["require-signed-resp-and-asrt"]
        if value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            desc = FIELD_DESCRIPTIONS.get("require-signed-resp-and-asrt", "")
            error_msg = f"Invalid value for 'require-signed-resp-and-asrt': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}"
            error_msg += f"\n  → Example: require-signed-resp-and-asrt='{{ VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT[0] }}'"
            return (False, error_msg)
    if "limit-relaystate" in payload:
        value = payload["limit-relaystate"]
        if value not in VALID_BODY_LIMIT_RELAYSTATE:
            desc = FIELD_DESCRIPTIONS.get("limit-relaystate", "")
            error_msg = f"Invalid value for 'limit-relaystate': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LIMIT_RELAYSTATE)}"
            error_msg += f"\n  → Example: limit-relaystate='{{ VALID_BODY_LIMIT_RELAYSTATE[0] }}'"
            return (False, error_msg)
    if "adfs-claim" in payload:
        value = payload["adfs-claim"]
        if value not in VALID_BODY_ADFS_CLAIM:
            desc = FIELD_DESCRIPTIONS.get("adfs-claim", "")
            error_msg = f"Invalid value for 'adfs-claim': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADFS_CLAIM)}"
            error_msg += f"\n  → Example: adfs-claim='{{ VALID_BODY_ADFS_CLAIM[0] }}'"
            return (False, error_msg)
    if "user-claim-type" in payload:
        value = payload["user-claim-type"]
        if value not in VALID_BODY_USER_CLAIM_TYPE:
            desc = FIELD_DESCRIPTIONS.get("user-claim-type", "")
            error_msg = f"Invalid value for 'user-claim-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_USER_CLAIM_TYPE)}"
            error_msg += f"\n  → Example: user-claim-type='{{ VALID_BODY_USER_CLAIM_TYPE[0] }}'"
            return (False, error_msg)
    if "group-claim-type" in payload:
        value = payload["group-claim-type"]
        if value not in VALID_BODY_GROUP_CLAIM_TYPE:
            desc = FIELD_DESCRIPTIONS.get("group-claim-type", "")
            error_msg = f"Invalid value for 'group-claim-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_GROUP_CLAIM_TYPE)}"
            error_msg += f"\n  → Example: group-claim-type='{{ VALID_BODY_GROUP_CLAIM_TYPE[0] }}'"
            return (False, error_msg)
    if "reauth" in payload:
        value = payload["reauth"]
        if value not in VALID_BODY_REAUTH:
            desc = FIELD_DESCRIPTIONS.get("reauth", "")
            error_msg = f"Invalid value for 'reauth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REAUTH)}"
            error_msg += f"\n  → Example: reauth='{{ VALID_BODY_REAUTH[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_user_saml_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update user/saml."""
    # Step 1: Validate enum values
    if "scim-user-attr-type" in payload:
        value = payload["scim-user-attr-type"]
        if value not in VALID_BODY_SCIM_USER_ATTR_TYPE:
            return (
                False,
                f"Invalid value for 'scim-user-attr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SCIM_USER_ATTR_TYPE)}",
            )
    if "scim-group-attr-type" in payload:
        value = payload["scim-group-attr-type"]
        if value not in VALID_BODY_SCIM_GROUP_ATTR_TYPE:
            return (
                False,
                f"Invalid value for 'scim-group-attr-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SCIM_GROUP_ATTR_TYPE)}",
            )
    if "digest-method" in payload:
        value = payload["digest-method"]
        if value not in VALID_BODY_DIGEST_METHOD:
            return (
                False,
                f"Invalid value for 'digest-method'='{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_METHOD)}",
            )
    if "require-signed-resp-and-asrt" in payload:
        value = payload["require-signed-resp-and-asrt"]
        if value not in VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT:
            return (
                False,
                f"Invalid value for 'require-signed-resp-and-asrt'='{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_SIGNED_RESP_AND_ASRT)}",
            )
    if "limit-relaystate" in payload:
        value = payload["limit-relaystate"]
        if value not in VALID_BODY_LIMIT_RELAYSTATE:
            return (
                False,
                f"Invalid value for 'limit-relaystate'='{value}'. Must be one of: {', '.join(VALID_BODY_LIMIT_RELAYSTATE)}",
            )
    if "adfs-claim" in payload:
        value = payload["adfs-claim"]
        if value not in VALID_BODY_ADFS_CLAIM:
            return (
                False,
                f"Invalid value for 'adfs-claim'='{value}'. Must be one of: {', '.join(VALID_BODY_ADFS_CLAIM)}",
            )
    if "user-claim-type" in payload:
        value = payload["user-claim-type"]
        if value not in VALID_BODY_USER_CLAIM_TYPE:
            return (
                False,
                f"Invalid value for 'user-claim-type'='{value}'. Must be one of: {', '.join(VALID_BODY_USER_CLAIM_TYPE)}",
            )
    if "group-claim-type" in payload:
        value = payload["group-claim-type"]
        if value not in VALID_BODY_GROUP_CLAIM_TYPE:
            return (
                False,
                f"Invalid value for 'group-claim-type'='{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_CLAIM_TYPE)}",
            )
    if "reauth" in payload:
        value = payload["reauth"]
        if value not in VALID_BODY_REAUTH:
            return (
                False,
                f"Invalid value for 'reauth'='{value}'. Must be one of: {', '.join(VALID_BODY_REAUTH)}",
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
    "endpoint": "user/saml",
    "category": "cmdb",
    "api_path": "user/saml",
    "mkey": "name",
    "mkey_type": "string",
    "help": "SAML server entry configuration.",
    "total_fields": 22,
    "required_fields_count": 5,
    "fields_with_defaults_count": 22,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
