"""
List normalization helpers for FortiOS API.

Converts various input formats (strings, lists, dicts) to the standard
FortiOS API format: [{'name': 'value'}, ...]
"""

from typing import Any, Dict, List, Union


def normalize_to_name_list(
    value: Union[str, List[str], Dict[str, str], List[Dict[str, str]], None],
) -> List[Dict[str, str]]:
    """
    Normalize various input formats to FortiOS API format: [{'name': 'value'},
    ...]

    This is the most common list format used in FortiOS API for fields like:
    - srcintf, dstintf (firewall policy)
    - member (address groups, service groups)
    - interface (router, system)
    - etc.

    Args:
        value: Can be:
            - String: 'port1' → [{'name': 'port1'}]
            - List of strings: ['port1', 'port2'] → [{'name': 'port1'},
            {'name': 'port2'}]
            - Dict: {'name': 'port1'} → [{'name': 'port1'}]
            - List of dicts: [{'name': 'port1'}, {'name': 'port2'}] → unchanged
            - None: []

    Returns:
        List of dicts in FortiOS format

    Example:
        >>> normalize_to_name_list('port1')
        [{'name': 'port1'}]
        >>> normalize_to_name_list(['port1', 'port2'])
        [{'name': 'port1'}, {'name': 'port2'}]
        >>> normalize_to_name_list([{'name': 'port1'}])
        [{'name': 'port1'}]
    """
    if value is None:
        return []

    # Already a list
    if isinstance(value, list):
        if not value:
            return []
        # If first item is a dict, assume whole list is dicts
        if isinstance(value[0], dict):
            # Filter out empty dicts that sometimes appear in API responses
            filtered: list[dict[str, Any]] = [
                item
                for item in value
                if isinstance(item, dict) and item and "name" in item
            ]
            return filtered
        # List of strings
        return [{"name": str(item)} for item in value]

    # Single dict
    if isinstance(value, dict):
        return [value] if value and "name" in value else []

    # Single string
    return [{"name": str(value)}]


def normalize_member_list(
    value: Union[str, List[str], Dict[str, Any], List[Dict[str, Any]], None],
) -> List[Dict[str, str]]:
    """
    Normalize various input formats for 'member' fields in groups.

    Used for address groups, service groups, and other grouped resources.
    Similar to normalize_to_name_list but specifically for 'member' fields.

    Args:
        value: Can be:
            - String: 'addr1' → [{'name': 'addr1'}]
            - List of strings: ['addr1', 'addr2'] → [{'name': 'addr1'},
            {'name': 'addr2'}]
            - Dict: {'name': 'addr1'} → [{'name': 'addr1'}]
            - List of dicts: [{'name': 'addr1'}, {'name': 'addr2'}] → unchanged
            - None: []

    Returns:
        List of dicts in FortiOS format

    Example:
        >>> normalize_member_list('address1')
        [{'name': 'address1'}]
        >>> normalize_member_list(['address1', 'address2'])
        [{'name': 'address1'}, {'name': 'address2'}]
    """
    # For now, this is identical to normalize_to_name_list
    # But we keep it separate because member lists might need
    # different handling in the future (e.g., additional fields)
    return normalize_to_name_list(value)
