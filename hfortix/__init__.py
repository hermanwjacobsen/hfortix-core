"""
HFortix - Python client library for Fortinet products

This package provides Python SDKs for Fortinet products:
- FortiOS: FortiGate firewall management
- FortiManager: Centralized management (coming soon)
- FortiAnalyzer: Log analysis and reporting (coming soon)

Each product module can be used independently or as part of the complete package.

Examples:
    # Recommended: Import from main package
    from hfortix import FortiOS
    
    # Also works: Import from submodule
    from hfortix.FortiOS import FortiOS
    
    # Import base exceptions
    from hfortix import FortinetError, APIError
"""

from __future__ import annotations

# Canonical public API for the hfortix package.
#
# Backward compatibility shims are intentionally not provided here.

from .FortiOS import __author__, __version__, FortiOS
from .exceptions import (
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    FortinetError,
    HTTP_STATUS_CODES,
    MethodNotAllowedError,
    RateLimitError,
    ResourceNotFoundError,
    ServerError,
    get_http_status_description,
)

# Export what's available
__all__ = [
    # Version info
    '__version__',
    '__author__',
    
    # Base exceptions (always available)
    'FortinetError',
    'AuthenticationError',
    'AuthorizationError',
    'APIError',
    'ResourceNotFoundError',
    'BadRequestError',
    'MethodNotAllowedError',
    'RateLimitError',
    'ServerError',
    'get_http_status_description',
    'HTTP_STATUS_CODES',
]

__all__.append('FortiOS')


def get_available_modules():
    """
    Get list of available Fortinet product modules.
    
    Returns:
        dict: Dictionary with module names as keys and availability as values
        
    Example:
    >>> from hfortix import get_available_modules
        >>> modules = get_available_modules()
        >>> print(modules)
        {'FortiOS': True, 'FortiManager': False, 'FortiAnalyzer': False}
    """
    return {
        'FortiOS': True,
        'FortiManager': False,
        'FortiAnalyzer': False,
    }


def get_version():
    """
    Get the current version of the Fortinet SDK.
    
    Returns:
        str: Version string
        
    Example:
    >>> from hfortix import get_version
        >>> print(get_version())
        '0.1.0'
    """
    return __version__
