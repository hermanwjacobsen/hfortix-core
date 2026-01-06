"""
FortiOS MONITOR - Vpn_certificate remote import_

Configuration endpoint for managing monitor vpn_certificate/remote/import_ objects.

API Endpoints:
    GET    /monitor/vpn_certificate/remote/import_
    POST   /monitor/vpn_certificate/remote/import_
    PUT    /monitor/vpn_certificate/remote/import_/{identifier}
    DELETE /monitor/vpn_certificate/remote/import_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.monitor.vpn_certificate_remote_import_.get()

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


class Import(MetadataMixin):
    """Import Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "import_"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Import endpoint."""
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
        Retrieve vpn_certificate/remote/import_ configuration.

        Import remote certificate.

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
            >>> # Get all vpn_certificate/remote/import_ objects
            >>> result = fgt.api.monitor.vpn_certificate_remote_import_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.monitor.vpn_certificate_remote_import_.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.monitor.vpn_certificate_remote_import_.get(action="schema")

        See Also:
            - post(): Create new vpn_certificate/remote/import_ object
            - put(): Update existing vpn_certificate/remote/import_ object
            - delete(): Remove vpn_certificate/remote/import_ object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/vpn-certificate/remote/import/{name}"
        else:
            endpoint = "/vpn-certificate/remote/import"
        
        params.update(kwargs)
        return self._client.get(
            "monitor", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )







