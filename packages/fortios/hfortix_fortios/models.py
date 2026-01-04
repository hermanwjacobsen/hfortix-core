"""
FortiOS Object Models

Provides zero-maintenance object wrappers for FortiOS API responses.
"""

from typing import Any


class FortiObject:
    """
    Zero-maintenance wrapper for FortiOS API responses.
    
    Provides clean attribute access to API response data with automatic
    flattening of member_table fields (lists of dicts with 'name' keys).
    
    Features:
    - No schemas required - works with any FortiOS version
    - No code generation - same class for all endpoints
    - No maintenance - automatically handles new fields
    - Auto-flattening of member_table fields for clean access
    - Escape hatch via get_full() for raw data access
    
    Examples:
        >>> # From dict response
        >>> data = {"name": "policy1", "srcaddr": [{"name": "addr1"}]}
        >>> obj = FortiObject(data)
        >>> 
        >>> # Clean attribute access
        >>> obj.name
        'policy1'
        >>> 
        >>> # Auto-flattened member_table fields
        >>> obj.srcaddr
        ['addr1']
        >>> 
        >>> # Get raw data when needed
        >>> obj.get_full('srcaddr')
        [{'name': 'addr1'}]
        >>> 
        >>> # Convert back to dict
        >>> obj.to_dict()
        {'name': 'policy1', 'srcaddr': [{'name': 'addr1'}]}
    
    Args:
        data: Dictionary from FortiOS API response
    """
    
    def __init__(self, data: dict):
        """
        Initialize FortiObject with API response data.
        
        Args:
            data: Dictionary containing the API response fields
        """
        self._data = data
    
    def __getattr__(self, name: str) -> Any:
        """
        Dynamic attribute access with automatic member_table flattening.
        
        For most FortiOS fields (strings, ints, etc.), returns the value as-is.
        For member_table fields (lists of dicts with 'name' key), automatically
        flattens to a list of name strings for cleaner access.
        
        Args:
            name: Attribute name to access
            
        Returns:
            Field value, with member_table fields auto-flattened
            
        Raises:
            AttributeError: If accessing private attributes (starting with '_')
            
        Examples:
            >>> obj.srcaddr  # Member table
            ['addr1', 'addr2']
            >>> obj.action  # Regular field
            'accept'
        """
        if name.startswith('_'):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        
        value = self._data.get(name)
        
        # Auto-flatten member_table fields (lists of dicts with 'name' key)
        # This handles ~90% of FortiOS list fields
        if isinstance(value, list) and value:
            if isinstance(value[0], dict) and 'name' in value[0]:
                return [item['name'] for item in value]
        
        return value
    
    def get_full(self, name: str) -> Any:
        """
        Get raw field value without automatic processing.
        
        Use this when you need the full object structure from a member_table
        field instead of the auto-flattened name list.
        
        Args:
            name: Field name to retrieve
            
        Returns:
            Raw field value without any processing
            
        Examples:
            >>> obj.get_full('srcaddr')
            [{'name': 'addr1', 'q_origin_key': 'addr1'}]
        """
        return self._data.get(name)
    
    def to_dict(self) -> dict:
        """
        Get the original dictionary data.
        
        Returns:
            Original API response dictionary
            
        Examples:
            >>> obj.to_dict()
            {'policyid': 1, 'name': 'policy1', ...}
        """
        return self._data
    
    def __repr__(self) -> str:
        """
        String representation of the object.
        
        Returns:
            String showing object type and identifier (name or policyid)
        """
        # Try to find a meaningful identifier
        identifier = self._data.get('name') or self._data.get('policyid') or 'object'
        return f"FortiObject({identifier})"
    
    def __contains__(self, key: str) -> bool:
        """
        Check if field exists in the object.
        
        Args:
            key: Field name to check
            
        Returns:
            True if field exists, False otherwise
            
        Examples:
            >>> 'srcaddr' in obj
            True
        """
        return key in self._data
    
    def __len__(self) -> int:
        """
        Get number of fields in the object.
        
        Returns:
            Number of fields in the response data
            
        Examples:
            >>> len(obj)
            15
        """
        return len(self._data)
    
    def keys(self):
        """
        Get all field names.
        
        Returns:
            Dictionary keys view of all field names
            
        Examples:
            >>> list(obj.keys())
            ['policyid', 'name', 'srcaddr', 'dstaddr', ...]
        """
        return self._data.keys()
    
    def values(self):
        """
        Get all field values (processed).
        
        Note: This returns processed values (with auto-flattening).
        Use to_dict().values() for raw values.
        
        Returns:
            Generator of processed field values
        """
        for key in self._data.keys():
            yield getattr(self, key)
    
    def items(self):
        """
        Get all field name-value pairs (processed).
        
        Note: This returns processed values (with auto-flattening).
        Use to_dict().items() for raw values.
        
        Returns:
            Generator of (key, processed_value) tuples
        """
        for key in self._data.keys():
            yield (key, getattr(self, key))
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get field value with optional default (dict-like interface).
        
        Args:
            key: Field name to retrieve
            default: Value to return if field doesn't exist
            
        Returns:
            Processed field value or default
            
        Examples:
            >>> obj.get('action', 'deny')
            'accept'
            >>> obj.get('nonexistent', 'default')
            'default'
        """
        try:
            return getattr(self, key)
        except AttributeError:
            return default


def process_response(
    result: Any,
    response_mode: str | None,
    client: Any = None
) -> Any:
    """
    Process API response based on response_mode setting.
    
    Handles both raw_json=False (list of results) and raw_json=True (full response dict).
    
    Args:
        result: Raw API response (list or dict)
        response_mode: Response mode - "dict", "object", or None (use client default)
        client: HTTP client instance (to get default response_mode)
        
    Returns:
        Processed response - either dict/list or FortiObject/list[FortiObject]
        
    Examples:
        >>> # Dict mode with raw_json=False (default)
        >>> result = [{"name": "policy1", "srcaddr": [{"name": "addr1"}]}]
        >>> process_response(result, "dict")
        [{"name": "policy1", "srcaddr": [{"name": "addr1"}]}]
        
        >>> # Object mode with raw_json=False
        >>> objects = process_response(result, "object")
        >>> objects[0].name
        'policy1'
        >>> objects[0].srcaddr  # Auto-flattened!
        ['addr1']
        
        >>> # Object mode with raw_json=True
        >>> result = {'results': [{"name": "policy1", ...}], 'http_status': 200, ...}
        >>> response = process_response(result, "object")
        >>> response['results'][0].name  # Results are FortiObjects
        'policy1'
        >>> response['http_status']  # Metadata preserved
        200
    """
    # Determine the actual mode to use
    mode = response_mode
    if mode is None and client is not None:
        mode = getattr(client, '_response_mode', 'dict')
    if mode is None:
        mode = 'dict'
    
    # If dict mode, return as-is
    if mode == 'dict':
        return result
    
    # Object mode - wrap in FortiObject
    if isinstance(result, list):
        # raw_json=False: Direct list of results
        return [FortiObject(item) for item in result]
    elif isinstance(result, dict):
        # Check if this is a raw_json=True response with 'results' key
        if 'results' in result and isinstance(result['results'], list):
            # raw_json=True: Preserve full response but wrap results in FortiObject
            return {
                **result,
                'results': [FortiObject(item) for item in result['results']]
            }
        else:
            # Single object response (e.g., get with specific ID)
            return FortiObject(result)
    
    # Return as-is for any other type
    return result

