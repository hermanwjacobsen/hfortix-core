"""HTTP client framework."""

from .async_client import AsyncHTTPClient
from .base import BaseHTTPClient
from .client import HTTPClient
from .cloud_client import CloudHTTPClient
from .jsonrpc_client import HTTPClientJSONRPC
from .interface import IHTTPClient
from .oauth import FortiCloudAuth, get_oauth_token

# Backward compatibility alias
HTTPClientFMG = HTTPClientJSONRPC

__all__ = [
    "IHTTPClient",
    "BaseHTTPClient",
    "HTTPClient",
    "HTTPClientJSONRPC",
    "HTTPClientFMG",  # Backward compatibility
    "CloudHTTPClient",
    "AsyncHTTPClient",
    "FortiCloudAuth",
    "get_oauth_token",
]
