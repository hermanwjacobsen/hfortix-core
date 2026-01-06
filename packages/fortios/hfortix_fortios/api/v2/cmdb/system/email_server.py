"""
FortiOS CMDB - System email_server

Configuration endpoint for managing cmdb system/email_server objects.

API Endpoints:
    GET    /cmdb/system/email_server
    POST   /cmdb/system/email_server
    PUT    /cmdb/system/email_server/{identifier}
    DELETE /cmdb/system/email_server/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_email_server.get()

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


class EmailServer(MetadataMixin):
    """EmailServer Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "email_server"

    def __init__(self, client: "IHTTPClient"):
        """Initialize EmailServer endpoint."""
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
        Retrieve system/email_server configuration.

        Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.

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
            >>> # Get all system/email_server objects
            >>> result = fgt.api.cmdb.system_email_server.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_email_server.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_email_server.get(action="schema")

        See Also:
            - post(): Create new system/email_server object
            - put(): Update existing system/email_server object
            - delete(): Remove system/email_server object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/email-server/{name}"
        else:
            endpoint = "/system/email-server"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        type: str | None = None,
        server: str | None = None,
        port: int | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        authenticate: str | None = None,
        validate_server: str | None = None,
        username: str | None = None,
        password: Any | None = None,
        security: str | None = None,
        ssl_min_proto_version: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/email_server object.

        Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            type: Use FortiGuard Message service or custom email server.
            server: SMTP server IP address or hostname.
            port: SMTP server port.
            source_ip: SMTP server IPv4 source IP.
            source_ip6: SMTP server IPv6 source IP.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_email_server.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_email_server.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            type=type,
            server=server,
            port=port,
            source_ip=source_ip,
            source_ip6=source_ip6,
            authenticate=authenticate,
            validate_server=validate_server,
            username=username,
            password=password,
            security=security,
            ssl_min_proto_version=ssl_min_proto_version,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.email_server import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/email_server",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/email-server/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





