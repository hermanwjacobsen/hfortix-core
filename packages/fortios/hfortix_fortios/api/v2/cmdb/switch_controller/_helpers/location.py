"""Validation helpers for switch_controller/location - Auto-generated"""

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
    "name": "",
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
    "name": "string",  # Unique location item name.
    "address-civic": "string",  # Configure location civic address.
    "coordinates": "string",  # Configure location GPS coordinates.
    "elin-number": "string",  # Configure location ELIN number.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Unique location item name.",
    "address-civic": "Configure location civic address.",
    "coordinates": "Configure location GPS coordinates.",
    "elin-number": "Configure location ELIN number.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "address-civic": {
        "additional": {
            "type": "string",
            "help": "Location additional details.",
            "default": "",
            "max_length": 47,
        },
        "additional-code": {
            "type": "string",
            "help": "Location additional code details.",
            "default": "",
            "max_length": 47,
        },
        "block": {
            "type": "string",
            "help": "Location block details.",
            "default": "",
            "max_length": 47,
        },
        "branch-road": {
            "type": "string",
            "help": "Location branch road details.",
            "default": "",
            "max_length": 47,
        },
        "building": {
            "type": "string",
            "help": "Location building details.",
            "default": "",
            "max_length": 47,
        },
        "city": {
            "type": "string",
            "help": "Location city details.",
            "default": "",
            "max_length": 47,
        },
        "city-division": {
            "type": "string",
            "help": "Location city division details.",
            "default": "",
            "max_length": 47,
        },
        "country": {
            "type": "string",
            "help": "The two-letter ISO 3166 country code in capital ASCII letters eg. US, CA, DK, DE.",
            "required": True,
            "default": "",
            "max_length": 47,
        },
        "country-subdivision": {
            "type": "string",
            "help": "National subdivisions (state, canton, region, province, or prefecture).",
            "default": "",
            "max_length": 47,
        },
        "county": {
            "type": "string",
            "help": "County, parish, gun (JP), or district (IN).",
            "default": "",
            "max_length": 47,
        },
        "direction": {
            "type": "string",
            "help": "Leading street direction.",
            "default": "",
            "max_length": 47,
        },
        "floor": {
            "type": "string",
            "help": "Floor.",
            "default": "",
            "max_length": 47,
        },
        "landmark": {
            "type": "string",
            "help": "Landmark or vanity address.",
            "default": "",
            "max_length": 47,
        },
        "language": {
            "type": "string",
            "help": "Language.",
            "default": "",
            "max_length": 47,
        },
        "name": {
            "type": "string",
            "help": "Name (residence and office occupant).",
            "default": "",
            "max_length": 47,
        },
        "number": {
            "type": "string",
            "help": "House number.",
            "default": "",
            "max_length": 47,
        },
        "number-suffix": {
            "type": "string",
            "help": "House number suffix.",
            "default": "",
            "max_length": 47,
        },
        "place-type": {
            "type": "string",
            "help": "Place type.",
            "default": "",
            "max_length": 47,
        },
        "post-office-box": {
            "type": "string",
            "help": "Post office box.",
            "default": "",
            "max_length": 47,
        },
        "postal-community": {
            "type": "string",
            "help": "Postal community name.",
            "default": "",
            "max_length": 47,
        },
        "primary-road": {
            "type": "string",
            "help": "Primary road name.",
            "default": "",
            "max_length": 47,
        },
        "road-section": {
            "type": "string",
            "help": "Road section.",
            "default": "",
            "max_length": 47,
        },
        "room": {
            "type": "string",
            "help": "Room number.",
            "default": "",
            "max_length": 47,
        },
        "script": {
            "type": "string",
            "help": "Script used to present the address information.",
            "default": "",
            "max_length": 47,
        },
        "seat": {
            "type": "string",
            "help": "Seat number.",
            "default": "",
            "max_length": 47,
        },
        "street": {
            "type": "string",
            "help": "Street.",
            "default": "",
            "max_length": 47,
        },
        "street-name-post-mod": {
            "type": "string",
            "help": "Street name post modifier.",
            "default": "",
            "max_length": 47,
        },
        "street-name-pre-mod": {
            "type": "string",
            "help": "Street name pre modifier.",
            "default": "",
            "max_length": 47,
        },
        "street-suffix": {
            "type": "string",
            "help": "Street suffix.",
            "default": "",
            "max_length": 47,
        },
        "sub-branch-road": {
            "type": "string",
            "help": "Sub branch road name.",
            "default": "",
            "max_length": 47,
        },
        "trailing-str-suffix": {
            "type": "string",
            "help": "Trailing street suffix.",
            "default": "",
            "max_length": 47,
        },
        "unit": {
            "type": "string",
            "help": "Unit (apartment, suite).",
            "default": "",
            "max_length": 47,
        },
        "zip": {
            "type": "string",
            "help": "Postal/zip code.",
            "default": "",
            "max_length": 47,
        },
        "parent-key": {
            "type": "string",
            "help": "Parent key name.",
            "default": "",
            "max_length": 63,
        },
    },
    "coordinates": {
        "altitude": {
            "type": "string",
            "help": "Plus or minus floating point number. For example, 117.47.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "altitude-unit": {
            "type": "option",
            "help": "Configure the unit for which the altitude is to (m = meters, f = floors of a building).",
            "required": True,
            "default": "m",
            "options": [{"help": "set altitude unit meters", "label": "M", "name": "m"}, {"help": "set altitude unit floors", "label": "F", "name": "f"}],
        },
        "datum": {
            "type": "option",
            "help": "WGS84, NAD83, NAD83/MLLW.",
            "required": True,
            "default": "WGS84",
            "options": [{"help": "set coordinates datum WGS84", "label": "Wgs84", "name": "WGS84"}, {"help": "set coordinates datum NAD83", "label": "Nad83", "name": "NAD83"}, {"help": "set coordinates datum NAD83/MLLW", "label": "Nad83/Mllw", "name": "NAD83/MLLW"}],
        },
        "latitude": {
            "type": "string",
            "help": "Floating point starting with +/- or ending with (N or S). For example, +/-16.67 or 16.67N.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "longitude": {
            "type": "string",
            "help": "Floating point starting with +/- or ending with (N or S). For example, +/-26.789 or 26.789E.",
            "required": True,
            "default": "",
            "max_length": 15,
        },
        "parent-key": {
            "type": "string",
            "help": "Parent key name.",
            "default": "",
            "max_length": 63,
        },
    },
    "elin-number": {
        "elin-num": {
            "type": "string",
            "help": "Configure ELIN callback number.",
            "default": "",
            "max_length": 31,
        },
        "parent-key": {
            "type": "string",
            "help": "Parent key name.",
            "default": "",
            "max_length": 63,
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_switch_controller_location_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for switch_controller/location."""
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
    """Validate required fields for switch_controller/location."""
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


def validate_switch_controller_location_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new switch_controller/location object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_switch_controller_location_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update switch_controller/location."""
    # Step 1: Validate enum values

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
    "endpoint": "switch_controller/location",
    "category": "cmdb",
    "api_path": "switch-controller/location",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure FortiSwitch location services.",
    "total_fields": 4,
    "required_fields_count": 0,
    "fields_with_defaults_count": 1,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
