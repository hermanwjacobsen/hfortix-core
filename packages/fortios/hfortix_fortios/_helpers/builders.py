"""
Payload building helpers for FortiOS API.

Converts Python-style parameters to FortiOS API payloads with:
- snake_case to kebab-case conversion
- Optional list normalization
- None value filtering
"""

from typing import Any

from hfortix_fortios._helpers.normalizers import normalize_to_name_list


def build_cmdb_payload(**params: Any) -> dict[str, Any]:
    """
    Build a CMDB payload dictionary from keyword arguments (API layer - no
    normalization).

    Converts Python snake_case parameter names to FortiOS kebab-case API keys
    and filters out None values. This is the base helper used by all CMDB API
    endpoints.

    Does NOT normalize list fields - caller is responsible for providing data
    in the correct FortiOS format (unless using a wrapper with normalization).

    Args:
        **params: All resource parameters (e.g., name=..., member=..., etc.)

    Returns:
        Dictionary with FortiOS API-compatible keys and non-None values

    Example:
        >>> build_cmdb_payload(
        ...     name='my_address',
        ...     subnet='10.0.0.0 255.255.255.0',
        ...     associated_interface='port1'
        ... )
        {
            'name': 'my_address',
            'subnet': '10.0.0.0 255.255.255.0',
            'associated-interface': 'port1'
        }

        >>> build_cmdb_payload(
        ...     member=[{'name': 'addr1'}, {'name': 'addr2'}],
        ...     color=5,
        ...     comment='Test group'
        ... )
        {
            'member': [{'name': 'addr1'}, {'name': 'addr2'}],
            'color': 5,
            'comment': 'Test group'
        }
    """
    payload: dict[str, Any] = {}

    # Extract 'data' parameter if present
    # It should be merged, not added as a key
    data_dict = params.pop("data", None)

    for param_name, value in params.items():
        if value is None:
            continue

        # Convert snake_case to kebab-case for FortiOS API
        api_key = param_name.replace("_", "-")
        payload[api_key] = value

    # Merge 'data' dictionary into payload (override existing keys)
    if data_dict and isinstance(data_dict, dict):
        payload.update(data_dict)

    return payload


def build_cmdb_payload_normalized(
    normalize_fields: set[str] | None = None, **params: Any
) -> dict[str, Any]:
    """
    Build a CMDB payload with automatic normalization (convenience wrapper
    layer).

    Converts Python snake_case parameter names to FortiOS kebab-case API keys,
    filters out None values, AND normalizes specified list fields to FortiOS
    format.

    This is used by convenience wrappers to accept flexible inputs like strings
    or lists and automatically convert them to FortiOS [{'name': '...'}]
    format.

    Args:
        normalize_fields: Set of field names (snake_case) that should be
        normalized
                         to [{'name': '...'}] format. If None, common fields
                         like
                         'member', 'interface', 'allowaccess' are normalized.
        **params: All resource parameters

    Returns:
        Dictionary with FortiOS API-compatible keys and normalized values

    Example:
        >>> # Address group with member normalization
        >>> build_cmdb_payload_normalized(
        ...     normalize_fields={'member'},
        ...     name='my_group',
        ...     member=['addr1', 'addr2'],  # Gets normalized
        ...     comment='Test'
        ... )
        {
            'name': 'my_group',
            'member': [{'name': 'addr1'}, {'name': 'addr2'}],
            'comment': 'Test'
        }

        >>> # System interface with default normalization
        >>> build_cmdb_payload_normalized(
        ...     name='port1.100',
        ...     allowaccess=['ping', 'https'],  # Auto-normalized
        ...     ip='10.0.0.1 255.255.255.0'
        ... )
        {
            'name': 'port1.100',
            'allowaccess': [{'name': 'ping'}, {'name': 'https'}],
            'ip': '10.0.0.1 255.255.255.0'
        }
    """
    # Default fields that commonly need normalization across CMDB endpoints
    DEFAULT_NORMALIZE_FIELDS = {
        "member",  # address groups, service groups, user groups
        "interface",  # various config objects
        "allowaccess",  # system interfaces
        "srcintf",  # firewall policies, routes
        "dstintf",  # firewall policies, routes
        "srcaddr",  # firewall policies
        "dstaddr",  # firewall policies
        "service",  # firewall policies
        "users",  # various auth/policy objects
        "groups",  # various auth/policy objects
    }

    # Use provided fields or defaults
    fields_to_normalize = (
        normalize_fields
        if normalize_fields is not None
        else DEFAULT_NORMALIZE_FIELDS
    )

    payload: dict[str, Any] = {}

    # Extract 'data' parameter if present
    # It should be merged, not added as a key
    data_dict = params.pop("data", None)

    for param_name, value in params.items():
        if value is None:
            continue

        # Convert snake_case to kebab-case for FortiOS API
        api_key = param_name.replace("_", "-")

        # Normalize list parameters to FortiOS format if specified
        if param_name in fields_to_normalize:
            normalized = normalize_to_name_list(value)
            # Only add if normalization resulted in non-empty list
            if normalized:
                payload[api_key] = normalized
        else:
            payload[api_key] = value

    # Merge 'data' dictionary into payload (override existing keys)
    if data_dict and isinstance(data_dict, dict):
        payload.update(data_dict)

    return payload
