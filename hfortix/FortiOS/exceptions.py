"""FortiOS exception exports.

Historically this module existed as a compatibility wrapper. In the hfortix
package layout, it simply re-exports the shared exception hierarchy and the
FortiOS-specific helpers.
"""

from ..exceptions import (
    HTTP_STATUS_CODES,
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    FortinetError,
    MethodNotAllowedError,
    RateLimitError,
    ResourceNotFoundError,
    ServerError,
    get_http_status_description,
)

from ..exceptions_forti import (
    FORTIOS_ERROR_CODES,
    DuplicateEntryError,
    EntryInUseError,
    InvalidValueError,
    PermissionDeniedError,
    get_error_description,
    raise_for_status,
)

__all__ = [
    # Base exceptions
    'FortinetError',
    'AuthenticationError',
    'AuthorizationError',
    'APIError',

    # Specific exceptions
    'ResourceNotFoundError',
    'BadRequestError',
    'MethodNotAllowedError',
    'RateLimitError',
    'ServerError',
    'DuplicateEntryError',
    'EntryInUseError',
    'InvalidValueError',
    'PermissionDeniedError',

    # Helper functions
    'get_error_description',
    'get_http_status_description',
    'raise_for_status',

    # Data
    'HTTP_STATUS_CODES',
    'FORTIOS_ERROR_CODES',
]