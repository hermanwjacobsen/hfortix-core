"""
Validation helpers for vpn ipsec_manualkey endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# ============================================================================
# Required Fields Validation
# Auto-generated from schema using required_fields_analyzer.py
# ============================================================================

# NOTE: The FortiOS schema has known bugs where some specialized optional
# features are incorrectly marked as required. See SCHEMA_FALSE_POSITIVES
# for fields that should be OPTIONAL despite being marked required in
# the schema. The REQUIRED_FIELDS list below reflects the ACTUAL
# requirements based on API testing and schema analysis.

# Always required fields (no alternatives)
REQUIRED_FIELDS = [
    "authentication",  # Authentication algorithm. Must be the same for both ends of
    "authkey",  # Hexadecimal authentication key in 16-digit (8-byte) segments
    "enckey",  # Hexadecimal encryption key in 16-digit (8-byte) segments sep
    "encryption",  # Encryption algorithm. Must be the same for both ends of the
    "interface",  # Name of the physical, aggregate, or VLAN interface.
    "localspi",  # Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns betw
    "name",  # IPsec tunnel name.
    "remote-gw",  # Peer gateway.
    "remotespi",  # Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns bet
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "authentication": "null",
    "encryption": "null",
    "local-gw": "0.0.0.0",
    "npu-offload": "enable",
    "remote-gw": "0.0.0.0",
}


# Valid enum values from API documentation
VALID_BODY_AUTHENTICATION = [
    "null",
    "md5",
    "sha1",
    "sha256",
    "sha384",
    "sha512",
]
VALID_BODY_ENCRYPTION = [
    "null",
    "des",
    "3des",
    "aes128",
    "aes192",
    "aes256",
    "aria128",
    "aria192",
    "aria256",
    "seed",
]
VALID_BODY_NPU_OFFLOAD = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ipsec_manualkey_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> # List all objects
        >>> is_valid, error = {func_name}()
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
    Validate required fields for vpn_ipsec_manualkey.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_required_fields({
        ...     "authentication": "value",
        ...     # ... other fields
        ... })
    """
    # Check always-required fields
    missing = []
    for field in REQUIRED_FIELDS:
        # Skip fields with defaults
        if field in FIELDS_WITH_DEFAULTS:
            continue
        if field not in payload or payload.get(field) is None:
            missing.append(field)

    if missing:
        return (False, f"Missing required fields: {', '.join(missing)}")

    return (True, None)


# ============================================================================
# Endpoint Validation (Enhanced with Required Fields)
# ============================================================================


def validate_ipsec_manualkey_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload.

    This validator performs two-stage validation:
    1. Required fields validation (schema-based)
    2. Field value validation (enums, ranges, formats)

    Required fields:
      - authentication: Authentication algorithm. Must be the same for both ends of
      - authkey: Hexadecimal authentication key in 16-digit (8-byte) segments
      - enckey: Hexadecimal encryption key in 16-digit (8-byte) segments sep
      - encryption: Encryption algorithm. Must be the same for both ends of the
      - interface: Name of the physical, aggregate, or VLAN interface.
      - localspi: Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns betw
      - name: IPsec tunnel name.
      - remote-gw: Peer gateway.
      - remotespi: Remote SPI, a hexadecimal 8-digit (4-byte) tag. Discerns bet

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Validate payload exists
    if not payload:
        payload = {}

    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate field values (enums, ranges, etc.)
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate encryption if present
    if "encryption" in payload:
        value = payload.get("encryption")
        if value and value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid encryption '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )

    # Validate npu-offload if present
    if "npu-offload" in payload:
        value = payload.get("npu-offload")
        if value and value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid npu-offload '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ipsec_manualkey_put(
    name: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        name: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # name is required for updates
    if not name:
        return (False, "name is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate encryption if present
    if "encryption" in payload:
        value = payload.get("encryption")
        if value and value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid encryption '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )

    # Validate npu-offload if present
    if "npu-offload" in payload:
        value = payload.get("npu-offload")
        if value and value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid npu-offload '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ipsec_manualkey_delete(
    name: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        name: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return (False, "name is required for DELETE operation")

    return (True, None)
