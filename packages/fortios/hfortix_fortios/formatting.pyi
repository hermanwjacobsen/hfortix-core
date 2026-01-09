"""Type stubs for formatting utilities."""

from __future__ import annotations

from typing import Any

def to_json(data: Any, indent: int = 2, **kwargs: Any) -> str:
    """
    Convert any data to formatted JSON string.

    Args:
        data: Any Python object to convert to JSON
        indent: Number of spaces for indentation (default: 2)
        **kwargs: Additional arguments passed to json.dumps()

    Returns:
        Formatted JSON string
    """
    ...

def to_csv(data: Any, separator: str = ", ") -> str:
    """
    Convert any data to comma-separated string.

    Args:
        data: Any Python object to convert
        separator: String to use between items (default: ', ')

    Returns:
        Comma-separated string
    """
    ...

def to_dict(data: Any) -> dict[str, Any] | dict[int, Any]:
    """
    Convert any data to dictionary.

    Args:
        data: Any Python object to convert

    Returns:
        Dictionary representation of the data
    """
    ...

def to_multiline(data: Any, separator: str = "\n") -> str:
    """
    Convert any data to newline-separated string.

    Args:
        data: Any Python object to convert
        separator: String to use between lines (default: '\\n')

    Returns:
        Newline-separated string
    """
    ...

def to_quoted(data: Any, quote: str = '"', separator: str = ", ") -> str:
    """
    Convert any data to quoted string representation.

    Args:
        data: Any Python object to convert
        quote: Quote character to use (default: '"')
        separator: String to use between quoted items (default: ', ')

    Returns:
        Quoted string representation
    """
    ...
