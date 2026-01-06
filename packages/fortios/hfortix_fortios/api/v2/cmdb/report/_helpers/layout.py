"""
Validation helpers for report/layout endpoint.

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
    "style-theme",  # Report style theme.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "title": "",
    "subtitle": "",
    "description": "",
    "style-theme": "",
    "options": "include-table-of-content auto-numbering-heading view-chart-as-heading",
    "format": "pdf",
    "schedule-type": "daily",
    "day": "sunday",
    "time": "",
    "cutoff-option": "run-time",
    "cutoff-time": "",
    "email-send": "disable",
    "email-recipients": "",
    "max-pdf-report": 31,
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
    "name": "string",  # Report layout name.
    "title": "string",  # Report title.
    "subtitle": "string",  # Report subtitle.
    "description": "string",  # Description.
    "style-theme": "string",  # Report style theme.
    "options": "option",  # Report layout options.
    "format": "option",  # Report format.
    "schedule-type": "option",  # Report schedule type.
    "day": "option",  # Schedule days of week to generate report.
    "time": "user",  # Schedule time to generate report (format = hh:mm).
    "cutoff-option": "option",  # Cutoff-option is either run-time or custom.
    "cutoff-time": "user",  # Custom cutoff time to generate report (format = hh:mm).
    "email-send": "option",  # Enable/disable sending emails after reports are generated.
    "email-recipients": "string",  # Email recipients for generated reports.
    "max-pdf-report": "integer",  # Maximum number of PDF reports to keep at one time (oldest re
    "page": "string",  # Configure report page.
    "body-item": "string",  # Configure report body item.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Report layout name.",
    "title": "Report title.",
    "subtitle": "Report subtitle.",
    "description": "Description.",
    "style-theme": "Report style theme.",
    "options": "Report layout options.",
    "format": "Report format.",
    "schedule-type": "Report schedule type.",
    "day": "Schedule days of week to generate report.",
    "time": "Schedule time to generate report (format = hh:mm).",
    "cutoff-option": "Cutoff-option is either run-time or custom.",
    "cutoff-time": "Custom cutoff time to generate report (format = hh:mm).",
    "email-send": "Enable/disable sending emails after reports are generated.",
    "email-recipients": "Email recipients for generated reports.",
    "max-pdf-report": "Maximum number of PDF reports to keep at one time (oldest report is overwritten).",
    "page": "Configure report page.",
    "body-item": "Configure report body item.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "title": {"type": "string", "max_length": 127},
    "subtitle": {"type": "string", "max_length": 127},
    "description": {"type": "string", "max_length": 127},
    "style-theme": {"type": "string", "max_length": 35},
    "email-recipients": {"type": "string", "max_length": 511},
    "max-pdf-report": {"type": "integer", "min": 1, "max": 365},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "page": {
        "paper": {
            "type": "option",
            "help": "Report page paper.",
            "default": "a4",
            "options": [{"help": "A4 paper.", "label": "A4", "name": "a4"}, {"help": "Letter paper.", "label": "Letter", "name": "letter"}],
        },
        "column-break-before": {
            "type": "option",
            "help": "Report page auto column break before heading.",
            "default": "",
            "options": [{"help": "Column break before heading 1.", "label": "Heading1", "name": "heading1"}, {"help": "Column break before heading 2.", "label": "Heading2", "name": "heading2"}, {"help": "Column break before heading 3.", "label": "Heading3", "name": "heading3"}],
        },
        "page-break-before": {
            "type": "option",
            "help": "Report page auto page break before heading.",
            "default": "",
            "options": [{"help": "Page break before heading 1.", "label": "Heading1", "name": "heading1"}, {"help": "Page break before heading 2.", "label": "Heading2", "name": "heading2"}, {"help": "Page break before heading 3.", "label": "Heading3", "name": "heading3"}],
        },
        "options": {
            "type": "option",
            "help": "Report page options.",
            "default": "",
            "options": [{"help": "Show header on first page.", "label": "Header On First Page", "name": "header-on-first-page"}, {"help": "Show footer on first page.", "label": "Footer On First Page", "name": "footer-on-first-page"}],
        },
        "header": {
            "type": "string",
            "help": "Configure report page header.",
        },
        "footer": {
            "type": "string",
            "help": "Configure report page footer.",
        },
    },
    "body-item": {
        "id": {
            "type": "integer",
            "help": "Report item ID.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "description": {
            "type": "string",
            "help": "Description.",
            "default": "",
            "max_length": 63,
        },
        "type": {
            "type": "option",
            "help": "Report item type.",
            "default": "text",
            "options": [{"help": "Text.", "label": "Text", "name": "text"}, {"help": "Image.", "label": "Image", "name": "image"}, {"help": "Chart.", "label": "Chart", "name": "chart"}, {"help": "Miscellaneous.", "label": "Misc", "name": "misc"}],
        },
        "style": {
            "type": "string",
            "help": "Report item style.",
            "default": "",
            "max_length": 71,
        },
        "top-n": {
            "type": "integer",
            "help": "Value of top.",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "parameters": {
            "type": "string",
            "help": "Parameters.",
        },
        "text-component": {
            "type": "option",
            "help": "Report item text component.",
            "default": "text",
            "options": [{"help": "Normal text.", "label": "Text", "name": "text"}, {"help": "Heading 1.", "label": "Heading1", "name": "heading1"}, {"help": "Heading 2.", "label": "Heading2", "name": "heading2"}, {"help": "Heading 3.", "label": "Heading3", "name": "heading3"}],
        },
        "content": {
            "type": "string",
            "help": "Report item text content.",
            "default": "",
            "max_length": 511,
        },
        "img-src": {
            "type": "string",
            "help": "Report item image file name.",
            "default": "",
            "max_length": 127,
        },
        "chart": {
            "type": "string",
            "help": "Report item chart name.",
            "default": "",
            "max_length": 71,
        },
        "chart-options": {
            "type": "option",
            "help": "Report chart options.",
            "default": "include-no-data hide-title show-caption",
            "options": [{"help": "Include chart with no data.", "label": "Include No Data", "name": "include-no-data"}, {"help": "Hide chart title.", "label": "Hide Title", "name": "hide-title"}, {"help": "Show chart caption.", "label": "Show Caption", "name": "show-caption"}],
        },
        "misc-component": {
            "type": "option",
            "help": "Report item miscellaneous component.",
            "default": "hline",
            "options": [{"help": "Horizontal line.", "label": "Hline", "name": "hline"}, {"help": "Page break.", "label": "Page Break", "name": "page-break"}, {"help": "Column break.", "label": "Column Break", "name": "column-break"}, {"help": "Section start.", "label": "Section Start", "name": "section-start"}],
        },
        "title": {
            "type": "string",
            "help": "Report section title.",
            "default": "",
            "max_length": 511,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_OPTIONS = [
    "include-table-of-content",  # Include table of content in the report.
    "auto-numbering-heading",  # Prepend heading with auto numbering.
    "view-chart-as-heading",  # Auto add heading for each chart.
    "show-html-navbar-before-heading",  # Show HTML navigation bar before each heading.
    "dummy-option",  # Use this option if you need none of the above options.
]
VALID_BODY_FORMAT = [
    "pdf",  # PDF.
]
VALID_BODY_SCHEDULE_TYPE = [
    "demand",  # Run on demand.
    "daily",  # Schedule daily.
    "weekly",  # Schedule weekly.
]
VALID_BODY_DAY = [
    "sunday",  # Sunday.
    "monday",  # Monday.
    "tuesday",  # Tuesday.
    "wednesday",  # Wednesday.
    "thursday",  # Thursday.
    "friday",  # Friday.
    "saturday",  # Saturday.
]
VALID_BODY_CUTOFF_OPTION = [
    "run-time",  # Run time.
    "custom",  # Custom.
]
VALID_BODY_EMAIL_SEND = [
    "enable",  # Enable sending emails after generating reports.
    "disable",  # Disable sending emails after generating reports.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_report_layout_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for report/layout.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_report_layout_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_report_layout_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_report_layout_get(
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
    Validate required fields for report/layout.

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


def validate_report_layout_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new report/layout object.

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
        ...     "style-theme": True,  # Report style theme.
        ... }
        >>> is_valid, error = validate_report_layout_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "style-theme": True,
        ...     "options": "{'name': 'include-table-of-content', 'help': 'Include table of content in the report.', 'label': 'Include Table Of Content', 'description': 'Include table of content in the report'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_report_layout_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["options"] = "invalid-value"
        >>> is_valid, error = validate_report_layout_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_report_layout_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
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
    if "format" in payload:
        value = payload["format"]
        if value not in VALID_BODY_FORMAT:
            desc = FIELD_DESCRIPTIONS.get("format", "")
            error_msg = f"Invalid value for 'format': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORMAT)}"
            error_msg += f"\n  → Example: format='{{ VALID_BODY_FORMAT[0] }}'"
            return (False, error_msg)
    if "schedule-type" in payload:
        value = payload["schedule-type"]
        if value not in VALID_BODY_SCHEDULE_TYPE:
            desc = FIELD_DESCRIPTIONS.get("schedule-type", "")
            error_msg = f"Invalid value for 'schedule-type': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCHEDULE_TYPE)}"
            error_msg += f"\n  → Example: schedule-type='{{ VALID_BODY_SCHEDULE_TYPE[0] }}'"
            return (False, error_msg)
    if "day" in payload:
        value = payload["day"]
        if value not in VALID_BODY_DAY:
            desc = FIELD_DESCRIPTIONS.get("day", "")
            error_msg = f"Invalid value for 'day': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DAY)}"
            error_msg += f"\n  → Example: day='{{ VALID_BODY_DAY[0] }}'"
            return (False, error_msg)
    if "cutoff-option" in payload:
        value = payload["cutoff-option"]
        if value not in VALID_BODY_CUTOFF_OPTION:
            desc = FIELD_DESCRIPTIONS.get("cutoff-option", "")
            error_msg = f"Invalid value for 'cutoff-option': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CUTOFF_OPTION)}"
            error_msg += f"\n  → Example: cutoff-option='{{ VALID_BODY_CUTOFF_OPTION[0] }}'"
            return (False, error_msg)
    if "email-send" in payload:
        value = payload["email-send"]
        if value not in VALID_BODY_EMAIL_SEND:
            desc = FIELD_DESCRIPTIONS.get("email-send", "")
            error_msg = f"Invalid value for 'email-send': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMAIL_SEND)}"
            error_msg += f"\n  → Example: email-send='{{ VALID_BODY_EMAIL_SEND[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_report_layout_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update report/layout.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_report_layout_put(payload)
    """
    # Step 1: Validate enum values
    if "options" in payload:
        value = payload["options"]
        if value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid value for 'options'='{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )
    if "format" in payload:
        value = payload["format"]
        if value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid value for 'format'='{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )
    if "schedule-type" in payload:
        value = payload["schedule-type"]
        if value not in VALID_BODY_SCHEDULE_TYPE:
            return (
                False,
                f"Invalid value for 'schedule-type'='{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_TYPE)}",
            )
    if "day" in payload:
        value = payload["day"]
        if value not in VALID_BODY_DAY:
            return (
                False,
                f"Invalid value for 'day'='{value}'. Must be one of: {', '.join(VALID_BODY_DAY)}",
            )
    if "cutoff-option" in payload:
        value = payload["cutoff-option"]
        if value not in VALID_BODY_CUTOFF_OPTION:
            return (
                False,
                f"Invalid value for 'cutoff-option'='{value}'. Must be one of: {', '.join(VALID_BODY_CUTOFF_OPTION)}",
            )
    if "email-send" in payload:
        value = payload["email-send"]
        if value not in VALID_BODY_EMAIL_SEND:
            return (
                False,
                f"Invalid value for 'email-send'='{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_SEND)}",
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
    "endpoint": "report/layout",
    "category": "cmdb",
    "api_path": "report/layout",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Report layout configuration.",
    "total_fields": 17,
    "required_fields_count": 1,
    "fields_with_defaults_count": 15,
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
