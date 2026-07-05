"""Type stubs for the fmg_client backward-compatibility shim.

The real client is ``HTTPClientJSONRPC`` in ``jsonrpc_client``; this module
re-exports it under the historical names.
"""

from .jsonrpc_client import HTTPClientJSONRPC as HTTPClientJSONRPC

HTTPClientFMG = HTTPClientJSONRPC

__all__ = ["HTTPClientFMG", "HTTPClientJSONRPC"]
