"""Type stubs for FortiOS API v2."""

import logging
from typing import Literal

# Re-exported from hfortix_core
from hfortix_core import APIError as APIError
from hfortix_core import AuthenticationError as AuthenticationError
from hfortix_core import AuthorizationError as AuthorizationError
from hfortix_core import BadRequestError as BadRequestError
from hfortix_core import CircuitBreakerOpenError as CircuitBreakerOpenError
from hfortix_core import ConfigurationError as ConfigurationError
from hfortix_core import DebugSession as DebugSession
from hfortix_core import DuplicateEntryError as DuplicateEntryError
from hfortix_core import EntryInUseError as EntryInUseError
from hfortix_core import FortinetError as FortinetError
from hfortix_core import InvalidValueError as InvalidValueError
from hfortix_core import MethodNotAllowedError as MethodNotAllowedError
from hfortix_core import NonRetryableError as NonRetryableError
from hfortix_core import (
    OperationNotSupportedError as OperationNotSupportedError,
)
from hfortix_core import PermissionDeniedError as PermissionDeniedError
from hfortix_core import RateLimitError as RateLimitError
from hfortix_core import ReadOnlyModeError as ReadOnlyModeError
from hfortix_core import ResourceNotFoundError as ResourceNotFoundError
from hfortix_core import RetryableError as RetryableError
from hfortix_core import ServerError as ServerError
from hfortix_core import ServiceUnavailableError as ServiceUnavailableError
from hfortix_core import TimeoutError as TimeoutError
from hfortix_core import VDOMError as VDOMError
from hfortix_core import debug_timer as debug_timer
from hfortix_core import format_connection_stats as format_connection_stats
from hfortix_core import format_request_info as format_request_info
from hfortix_core import print_debug_info as print_debug_info

# API categories (accessed via FortiOS instance, not imported directly)
# These are exposed in __all__ for documentation but accessed as client.cmdb, client.log, etc.
from .api import CMDB as CMDB
from .api import Log as Log
from .api import Monitor as Monitor
from .api import Service as Service
from .client import FortiOS as FortiOS
from .client import FortiOSDictMode as FortiOSDictMode
from .client import FortiOSObjectMode as FortiOSObjectMode
from .formatting import to_csv as to_csv
from .formatting import to_dict as to_dict
from .formatting import to_json as to_json
from .formatting import to_multiline as to_multiline
from .formatting import to_quoted as to_quoted
from .help import help as help
from .models import FortiObject as FortiObject
from .types import ActionType as ActionType
from .types import FortiOSDictResponse as FortiOSDictResponse
from .types import FortiOSErrorResponse as FortiOSErrorResponse
from .types import FortiOSListResponse as FortiOSListResponse
from .types import FortiOSResponse as FortiOSResponse
from .types import FortiOSSuccessResponse as FortiOSSuccessResponse
from .types import LogSeverity as LogSeverity
from .types import ProtocolType as ProtocolType
from .types import ScheduleType as ScheduleType
from .types import StatusType as StatusType

__version__: str

__all__ = [
    # Main client
    "FortiOS",
    "FortiOSDictMode",
    "FortiOSObjectMode",
    "FortiObject",
    "configure_logging",
    # Formatting utilities
    "to_json",
    "to_csv",
    "to_dict",
    "to_multiline",
    "to_quoted",
    # Help system
    "help",
    # Type definitions
    "FortiOSSuccessResponse",
    "FortiOSListResponse",
    "FortiOSDictResponse",
    "FortiOSErrorResponse",
    "FortiOSResponse",
    "ActionType",
    "StatusType",
    "LogSeverity",
    "ScheduleType",
    "ProtocolType",
    # Debug utilities
    "DebugSession",
    "debug_timer",
    "format_connection_stats",
    "format_request_info",
    "print_debug_info",
    # Categories (legacy)
    "CMDB",
    "Monitor",
    "Service",
    "Log",
    # Exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
    "RetryableError",
    "NonRetryableError",
    "ConfigurationError",
    "VDOMError",
    "OperationNotSupportedError",
    "ReadOnlyModeError",
    "BadRequestError",
    "ResourceNotFoundError",
    "MethodNotAllowedError",
    "RateLimitError",
    "ServerError",
    "ServiceUnavailableError",
    "CircuitBreakerOpenError",
    "TimeoutError",
    "DuplicateEntryError",
    "EntryInUseError",
    "InvalidValueError",
    "PermissionDeniedError",
]

def configure_logging(
    level: str | int = ...,
    format: Literal["json", "text"] = ...,
    handler: logging.Handler | None = ...,
    use_color: bool = ...,
    include_trace: bool = ...,
    output_file: str | None = ...,
    structured: bool = ...,
) -> None:
    """Configure logging for HFortix library."""
    ...
