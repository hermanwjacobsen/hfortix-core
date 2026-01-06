"""
FortiOS MONITOR - Wifi ssid generate_keys

Configuration endpoint for managing monitor wifi/ssid/generate_keys objects.

API Endpoints:
    GET    /monitor/wifi/ssid/generate_keys
    POST   /monitor/wifi/ssid/generate_keys
    PUT    /monitor/wifi/ssid/generate_keys/{identifier}
    DELETE /monitor/wifi/ssid/generate_keys/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.wifi_ssid_generate_keys.get()

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin


class GenerateKeys(MetadataMixin):
    """GenerateKeys Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "generate_keys"

    def __init__(self, client: "IHTTPClient"):
        """Initialize GenerateKeys endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve wifi/ssid/generate_keys configuration.

        Generate pre-shared keys for specific multi pre-shared key profile.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
            payload_dict: Additional query parameters (filters, format, etc.)
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional query parameters (action, format, etc.)

        Returns:
            Configuration data as dict. Returns Coroutine if using async client.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all wifi/ssid/generate_keys objects
            >>> result = fgt.api.monitor.wifi_ssid_generate_keys.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.wifi_ssid_generate_keys.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.monitor.wifi_ssid_generate_keys.get(action="schema")

        See Also:
            - post(): Create new wifi/ssid/generate_keys object
            - put(): Update existing wifi/ssid/generate_keys object
            - delete(): Remove wifi/ssid/generate_keys object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wifi/ssid/generate-keys/{name}"
        else:
            endpoint = "/wifi/ssid/generate-keys"
        
        params.update(kwargs)
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )







