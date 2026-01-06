"""
FortiOS CMDB - Ftp_proxy explicit

Configuration endpoint for managing cmdb ftp_proxy/explicit objects.

API Endpoints:
    GET    /cmdb/ftp_proxy/explicit
    POST   /cmdb/ftp_proxy/explicit
    PUT    /cmdb/ftp_proxy/explicit/{identifier}
    DELETE /cmdb/ftp_proxy/explicit/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.ftp_proxy_explicit.get()

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


class Explicit(MetadataMixin):
    """Explicit Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "explicit"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Explicit endpoint."""
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
        Retrieve ftp_proxy/explicit configuration.

        Configure explicit FTP proxy settings.

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
            >>> # Get all ftp_proxy/explicit objects
            >>> result = fgt.api.cmdb.ftp_proxy_explicit.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.ftp_proxy_explicit.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.ftp_proxy_explicit.get(action="schema")

        See Also:
            - post(): Create new ftp_proxy/explicit object
            - put(): Update existing ftp_proxy/explicit object
            - delete(): Remove ftp_proxy/explicit object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/ftp-proxy/explicit/{name}"
        else:
            endpoint = "/ftp-proxy/explicit"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        incoming_port: str | None = None,
        incoming_ip: str | None = None,
        outgoing_ip: str | list | None = None,
        sec_default_action: str | None = None,
        server_data_mode: str | None = None,
        ssl: str | None = None,
        ssl_cert: str | list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing ftp_proxy/explicit object.

        Configure explicit FTP proxy settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable the explicit FTP proxy.
            incoming_port: Accept incoming FTP requests on one or more ports.
            incoming_ip: Accept incoming FTP requests from this IP address. An interface must have this IP address.
            outgoing_ip: Outgoing FTP requests will leave from this IP address. An interface must have this IP address.
            sec_default_action: Accept or deny explicit FTP proxy sessions when no FTP proxy firewall policy exists.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.ftp_proxy_explicit.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.ftp_proxy_explicit.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            incoming_port=incoming_port,
            incoming_ip=incoming_ip,
            outgoing_ip=outgoing_ip,
            sec_default_action=sec_default_action,
            server_data_mode=server_data_mode,
            ssl=ssl,
            ssl_cert=ssl_cert,
            ssl_dh_bits=ssl_dh_bits,
            ssl_algorithm=ssl_algorithm,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.explicit import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/ftp_proxy/explicit",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/ftp-proxy/explicit/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





