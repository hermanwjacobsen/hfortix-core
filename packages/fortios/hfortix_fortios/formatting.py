"""
Data formatting utilities for FortiOS objects and data structures.

Provides simple, type-agnostic conversion functions that handle any input gracefully.
Never raises exceptions - returns sensible defaults for edge cases.

"""

from __future__ import annotations

import json
from typing import Any


def to_json(data: Any, indent: int = 2, **kwargs: Any) -> str:
    """
    Convert any data to formatted JSON string.
    
    Handles objects with __dict__, converts sets/tuples to lists,
    and uses str() fallback for non-serializable types.
    
    Args:
        data: Any Python object to convert to JSON
        indent: Number of spaces for indentation (default: 2)
        **kwargs: Additional arguments passed to json.dumps()
    
    Returns:
        Formatted JSON string
    
    """
    def default_handler(obj: Any) -> Any:
        """Handle non-serializable objects."""
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        if isinstance(obj, (set, tuple)):
            return list(obj)
        return str(obj)
    
    return json.dumps(
        data,
        indent=indent,
        default=default_handler,
        **kwargs
    )


def to_csv(data: Any, separator: str = ', ') -> str:
    """
    Convert any data to comma-separated string.
    
    Args:
        data: Any Python object to convert
        separator: String to use between items (default: ', ')
    
    Returns:
        Comma-separated string
    
    Examples:
        >>> to_csv(['port1', 'port2', 'port3'])
        'port1, port2, port3'
        
        >>> to_csv({'x': 1, 'y': 2, 'z': 3})
        'x=1, y=2, z=3'
        
        >>> to_csv('already a string')
        'already a string'
        
        >>> to_csv(None)
        ''
        
        >>> to_csv([1, 2, 3], separator=' | ')
        '1 | 2 | 3'
        
        >>> class Interface:
        ...     def __init__(self):
        ...         self.name = "port1"
        ...         self.ip = "10.0.0.1"
        >>> to_csv(Interface())
        'name=port1, ip=10.0.0.1'
    """
    if data is None:
        return ''
    
    if isinstance(data, str):
        return data
    
    if isinstance(data, (int, float, bool)):
        return str(data)
    
    if isinstance(data, (list, tuple, set)):
        return separator.join(str(item) for item in data)
    
    if isinstance(data, dict):
        return separator.join(f"{k}={v}" for k, v in data.items())
    
    if hasattr(data, '__dict__'):
        return to_csv(data.__dict__, separator)
    
    return str(data)


def to_dict(data: Any) -> dict[str, Any] | dict[int, Any]:
    """
    Convert any data to dictionary.
    
    Args:
        data: Any Python object to convert
    
    Returns:
        Dictionary representation of the data
    
    Examples:
        >>> class Policy:
        ...     def __init__(self):
        ...         self.name = "Allow-All"
        ...         self.action = "accept"
        >>> to_dict(Policy())
        {'name': 'Allow-All', 'action': 'accept'}
        
        >>> to_dict({'already': 'a dict'})
        {'already': 'a dict'}
        
        >>> to_dict([('a', 1), ('b', 2)])
        {'a': 1, 'b': 2}
        
        >>> to_dict(['x', 'y', 'z'])
        {0: 'x', 1: 'y', 2: 'z'}
        
        >>> to_dict('simple string')
        {'value': 'simple string'}
        
        >>> to_dict(None)
        {'value': None}
    """
    if isinstance(data, dict):
        return data
    
    if hasattr(data, '__dict__'):
        return data.__dict__
    
    if isinstance(data, (list, tuple)):
        # Check if it's a list of tuples (can be converted to dict)
        if data and all(isinstance(item, (list, tuple)) and len(item) == 2 for item in data):
            try:
                return dict(data)
            except (TypeError, ValueError):
                pass
        # Otherwise convert to indexed dict
        return {i: v for i, v in enumerate(data)}
    
    # For primitives, wrap in value key
    return {'value': data}


def to_multiline(data: Any, separator: str = '\n') -> str:
    """
    Convert any data to newline-separated string.
    
    Args:
        data: Any Python object to convert
        separator: String to use between lines (default: '\\n')
    
    Returns:
        Newline-separated string
    
    Examples:
        >>> print(to_multiline(['port1', 'port2', 'port3']))
        port1
        port2
        port3
        
        >>> print(to_multiline({'name': 'policy1', 'action': 'accept'}))
        name: policy1
        action: accept
        
        >>> to_multiline('already a string')
        'already a string'
        
        >>> to_multiline(None)
        ''
        
        >>> class Policy:
        ...     def __init__(self):
        ...         self.name = "Allow-All"
        ...         self.policyid = 1
        >>> print(to_multiline(Policy()))
        name: Allow-All
        policyid: 1
    """
    if data is None:
        return ''
    
    if isinstance(data, str):
        return data
    
    if isinstance(data, (int, float, bool)):
        return str(data)
    
    if isinstance(data, (list, tuple, set)):
        return separator.join(str(item) for item in data)
    
    if isinstance(data, dict):
        return separator.join(f"{k}: {v}" for k, v in data.items())
    
    if hasattr(data, '__dict__'):
        return to_multiline(data.__dict__, separator)
    
    return str(data)


def to_quoted(data: Any, quote: str = '"', separator: str = ', ') -> str:
    """
    Convert any data to quoted string representation.
    
    Args:
        data: Any Python object to convert
        quote: Quote character to use (default: '"')
        separator: String to use between quoted items (default: ', ')
    
    Returns:
        Quoted string representation
    
    Examples:
        >>> to_quoted(['port1', 'port2', 'port3'])
        '"port1", "port2", "port3"'
        
        >>> to_quoted({'x': 1, 'y': 2})
        '"x", "y"'
        
        >>> to_quoted('hello')
        '"hello"'
        
        >>> to_quoted(None)
        '""'
        
        >>> to_quoted([1, 2, 3], quote="'")
        "'1', '2', '3'"
        
        >>> class Interface:
        ...     def __init__(self):
        ...         self.name = "port1"
        ...         self.vlan = 10
        >>> to_quoted(Interface())
        '"name", "vlan"'
    """
    if data is None:
        return f'{quote}{quote}'
    
    if isinstance(data, str):
        return f'{quote}{data}{quote}'
    
    if isinstance(data, (int, float, bool)):
        return f'{quote}{data}{quote}'
    
    if isinstance(data, (list, tuple, set)):
        return separator.join(f'{quote}{item}{quote}' for item in data)
    
    if isinstance(data, dict):
        # Quote the keys
        return separator.join(f'{quote}{k}{quote}' for k in data.keys())
    
    if hasattr(data, '__dict__'):
        return to_quoted(data.__dict__, quote, separator)
    
    return f'{quote}{data}{quote}'
