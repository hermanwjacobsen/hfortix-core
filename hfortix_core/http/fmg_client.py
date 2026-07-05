"""Backward-compatibility shim — module renamed to ``jsonrpc_client``.

The FortiManager/FortiAnalyzer JSON-RPC client now lives in
:mod:`hfortix_core.http.jsonrpc_client` as ``HTTPClientJSONRPC``.
This module preserves the historical import path
(``from hfortix_core.http.fmg_client import HTTPClientFMG``) used by
releases up to 0.5.162. Prefer the new path in new code.
"""

from .jsonrpc_client import HTTPClientJSONRPC

# Historical name — kept for backward compatibility.
HTTPClientFMG = HTTPClientJSONRPC

__all__ = ["HTTPClientFMG", "HTTPClientJSONRPC"]
