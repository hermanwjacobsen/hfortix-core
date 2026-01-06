"""
Validation helpers for dlp/filepattern endpoint.

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
    "name",  # Name of table containing the file pattern list.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "id": 0,
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
    "id": "integer",  # ID.
    "name": "string",  # Name of table containing the file pattern list.
    "comment": "var-string",  # Optional comments.
    "entries": "string",  # Configure file patterns used by DLP blocking.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "id": "ID.",
    "name": "Name of table containing the file pattern list.",
    "comment": "Optional comments.",
    "entries": "Configure file patterns used by DLP blocking.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "id": {"type": "integer", "min": 0, "max": 4294967295},
    "name": {"type": "string", "max_length": 63},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "entries": {
        "filter-type": {
            "type": "option",
            "help": "Filter by file name pattern or by file type.",
            "required": True,
            "default": "pattern",
            "options": [{"help": "Filter by file name pattern.", "label": "Pattern", "name": "pattern"}, {"help": "Filter by file type.", "label": "Type", "name": "type"}],
        },
        "pattern": {
            "type": "string",
            "help": "Add a file name pattern.",
            "default": "",
            "max_length": 79,
        },
        "file-type": {
            "type": "option",
            "help": "Select a file type.",
            "required": True,
            "default": "unknown",
            "options": [{"help": "Match 7-zip files.", "label": "7Z", "name": "7z"}, {"help": "Match arj compressed files.", "label": "Arj", "name": "arj"}, {"help": "Match Windows cab files.", "label": "Cab", "name": "cab"}, {"help": "Match lzh compressed files.", "label": "Lzh", "name": "lzh"}, {"help": "Match rar archives.", "label": "Rar", "name": "rar"}, {"help": "Match tar files.", "label": "Tar", "name": "tar"}, {"help": "Match zip files.", "label": "Zip", "name": "zip"}, {"help": "Match bzip files.", "label": "Bzip", "name": "bzip"}, {"help": "Match gzip files.", "label": "Gzip", "name": "gzip"}, {"help": "Match bzip2 files.", "label": "Bzip2", "name": "bzip2"}, {"help": "Match xz files.", "label": "Xz", "name": "xz"}, {"help": "Match Windows batch files.", "label": "Bat", "name": "bat"}, {"help": "Match uue files.", "label": "Uue", "name": "uue"}, {"help": "Match mime files.", "label": "Mime", "name": "mime"}, {"help": "Match base64 files.", "label": "Base64", "name": "base64"}, {"help": "Match binhex files.", "label": "Binhex", "name": "binhex"}, {"help": "Match elf files.", "label": "Elf", "name": "elf"}, {"help": "Match Windows executable files.", "label": "Exe", "name": "exe"}, {"help": "Match dll files.", "label": "Dll", "name": "dll"}, {"help": "Match jnlp files.", "label": "Jnlp", "name": "jnlp"}, {"help": "Match hta files.", "label": "Hta", "name": "hta"}, {"help": "Match html files.", "label": "Html", "name": "html"}, {"help": "Match jad files.", "label": "Jad", "name": "jad"}, {"help": "Match class files.", "label": "Class", "name": "class"}, {"help": "Match cod files.", "label": "Cod", "name": "cod"}, {"help": "Match javascript files.", "label": "Javascript", "name": "javascript"}, {"help": "Match legacy MS-Office files. doc, ppt, and xls.", "label": "Msoffice", "name": "msoffice"}, {"help": "Match MS-Office XML files. docm, docx, pptm, pptx, xlsm, and xlsx.", "label": "Msofficex", "name": "msofficex"}, {"help": "Match fsg files.", "label": "Fsg", "name": "fsg"}, {"help": "Match upx files.", "label": "Upx", "name": "upx"}, {"help": "Match petite files.", "label": "Petite", "name": "petite"}, {"help": "Match aspack files.", "label": "Aspack", "name": "aspack"}, {"help": "Match sis files.", "label": "Sis", "name": "sis"}, {"help": "Match Windows help files.", "label": "Hlp", "name": "hlp"}, {"help": "Match activemime files.", "label": "Activemime", "name": "activemime"}, {"help": "Match jpeg files.", "label": "Jpeg", "name": "jpeg"}, {"help": "Match gif files.", "label": "Gif", "name": "gif"}, {"help": "Match tiff files.", "label": "Tiff", "name": "tiff"}, {"help": "Match png files.", "label": "Png", "name": "png"}, {"help": "Match bmp files.", "label": "Bmp", "name": "bmp"}, {"help": "Match unknown files.", "label": "Unknown", "name": "unknown"}, {"help": "Match mpeg files.", "label": "Mpeg", "name": "mpeg"}, {"help": "Match mov files.", "label": "Mov", "name": "mov"}, {"help": "Match mp3 files.", "label": "Mp3", "name": "mp3"}, {"help": "Match wma files.", "label": "Wma", "name": "wma"}, {"help": "Match wav files.", "label": "Wav", "name": "wav"}, {"help": "Match Acrobat PDF files.", "label": "Pdf", "name": "pdf"}, {"help": "Match avi files.", "label": "Avi", "name": "avi"}, {"help": "Match rm files.", "label": "Rm", "name": "rm"}, {"help": "Match torrent files.", "label": "Torrent", "name": "torrent"}, {"help": "Match special-file-23-support files.", "label": "Hibun", "name": "hibun"}, {"help": "Match Windows Installer msi files.", "label": "Msi", "name": "msi"}, {"help": "Match Mach object files.", "label": "Mach O", "name": "mach-o"}, {"help": "Match Apple disk image files.", "label": "Dmg", "name": "dmg"}, {"help": "Match .NET files.", "label": ".Net", "name": ".net"}, {"help": "Match xar archive files.", "label": "Xar", "name": "xar"}, {"help": "Match Windows compiled HTML help files.", "label": "Chm", "name": "chm"}, {"help": "Match ISO archive files.", "label": "Iso", "name": "iso"}, {"help": "Match Chrome extension files.", "label": "Crx", "name": "crx"}, {"help": "Match flac files.", "label": "Flac", "name": "flac"}, {"help": "Match registry files.", "label": "Registry", "name": "registry"}, {"help": "Match hwp files.", "label": "Hwp", "name": "hwp"}, {"help": "Match rpm files.", "label": "Rpm", "name": "rpm"}, {"help": "Match generic script files.", "label": "Genscript", "name": "genscript"}, {"help": "Match python files.", "label": "Python", "name": "python"}, {"help": "Match c/cpp files.", "label": "C/Cpp", "name": "c/cpp"}, {"help": "Match pfile files.", "label": "Pfile", "name": "pfile"}, {"help": "Match lzip files.", "label": "Lzip", "name": "lzip"}, {"help": "Match WebAssembly files.", "label": "Wasm", "name": "wasm"}, {"help": "Match Microsoft symbolic link files.", "label": "Sylk", "name": "sylk"}, {"help": "Match shell script files.", "label": "Shellscript", "name": "shellscript"}],
        },
    },
}


# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dlp_filepattern_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for dlp/filepattern.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_dlp_filepattern_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by id
        >>> is_valid, error = validate_dlp_filepattern_get(id="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_dlp_filepattern_get(
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
    Validate required fields for dlp/filepattern.

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


def validate_dlp_filepattern_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new dlp/filepattern object.

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
        ...     "name": True,  # Name of table containing the file pattern list.
        ... }
        >>> is_valid, error = validate_dlp_filepattern_post(payload)
        >>> assert is_valid == True
        
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_dlp_filepattern_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dlp_filepattern_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update dlp/filepattern.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_dlp_filepattern_put(payload)
    """
    # Step 1: Validate enum values

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
    "endpoint": "dlp/filepattern",
    "category": "cmdb",
    "api_path": "dlp/filepattern",
    "mkey": "id",
    "mkey_type": "integer",
    "help": "Configure file patterns used by DLP blocking.",
    "total_fields": 4,
    "required_fields_count": 1,
    "fields_with_defaults_count": 2,
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
