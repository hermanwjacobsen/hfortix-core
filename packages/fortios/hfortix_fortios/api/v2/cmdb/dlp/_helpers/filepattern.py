"""Validation helpers for dlp/filepattern - Auto-generated"""

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
    """Validate GET request parameters for dlp/filepattern."""
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
    """Validate required fields for dlp/filepattern."""
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
    """Validate POST request to create new dlp/filepattern object."""
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
    """Validate PUT request to update dlp/filepattern."""
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
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()
