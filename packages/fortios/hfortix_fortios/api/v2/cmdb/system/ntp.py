"""
FortiOS CMDB - System ntp

Configuration endpoint for managing cmdb system/ntp objects.

API Endpoints:
    GET    /cmdb/system/ntp
    POST   /cmdb/system/ntp
    PUT    /cmdb/system/ntp/{identifier}
    DELETE /cmdb/system/ntp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ntp.get()

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


class Ntp(MetadataMixin):
    """Ntp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ntp"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ntp endpoint."""
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
        Retrieve system/ntp configuration.

        Configure system NTP information.

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
            >>> # Get all system/ntp objects
            >>> result = fgt.api.cmdb.system_ntp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ntp.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ntp.get(action="schema")

        See Also:
            - post(): Create new system/ntp object
            - put(): Update existing system/ntp object
            - delete(): Remove system/ntp object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ntp/{name}"
        else:
            endpoint = "/system/ntp"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ntpsync: str | None = None,
        type: str | None = None,
        syncinterval: int | None = None,
        ntpserver: str | list | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        server_mode: str | None = None,
        authentication: str | None = None,
        key_type: str | None = None,
        key: Any | None = None,
        key_id: int | None = None,
        interface: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ntp object.

        Configure system NTP information.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ntpsync: Enable/disable setting the FortiGate system time by synchronizing with an NTP Server.
            type: Use the FortiGuard NTP server or any other available NTP Server.
            syncinterval: NTP synchronization interval (1 - 1440 min).
            ntpserver: Configure the FortiGate to connect to any available third-party NTP server.
            source_ip: Source IP address for communication to the NTP server.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ntp.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ntp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ntpsync=ntpsync,
            type=type,
            syncinterval=syncinterval,
            ntpserver=ntpserver,
            source_ip=source_ip,
            source_ip6=source_ip6,
            server_mode=server_mode,
            authentication=authentication,
            key_type=key_type,
            key=key,
            key_id=key_id,
            interface=interface,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ntp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ntp",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ntp/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





