"""Validation helpers for report/layout - Auto-generated"""

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
    """Validate GET request parameters for report/layout."""
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
    """Validate required fields for report/layout."""
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
    """Validate POST request to create new report/layout object."""
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
    """Validate PUT request to update report/layout."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
