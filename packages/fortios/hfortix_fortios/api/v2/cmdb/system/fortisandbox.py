"""
FortiOS CMDB - System fortisandbox

Configuration endpoint for managing cmdb system/fortisandbox objects.

API Endpoints:
    GET    /cmdb/system/fortisandbox
    POST   /cmdb/system/fortisandbox
    PUT    /cmdb/system/fortisandbox/{identifier}
    DELETE /cmdb/system/fortisandbox/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_fortisandbox.get()

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


class Fortisandbox(MetadataMixin):
    """Fortisandbox Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fortisandbox"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortisandbox endpoint."""
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
        Retrieve system/fortisandbox configuration.

        Configure FortiSandbox.

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
            >>> # Get all system/fortisandbox objects
            >>> result = fgt.api.cmdb.system_fortisandbox.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_fortisandbox.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_fortisandbox.get(action="schema")

        See Also:
            - post(): Create new system/fortisandbox object
            - put(): Update existing system/fortisandbox object
            - delete(): Remove system/fortisandbox object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/fortisandbox/{name}"
        else:
            endpoint = "/system/fortisandbox"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        forticloud: str | None = None,
        inline_scan: str | None = None,
        server: str | None = None,
        source_ip: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        enc_algorithm: str | None = None,
        ssl_min_proto_version: str | None = None,
        email: str | None = None,
        ca: str | None = None,
        cn: str | None = None,
        certificate_verification: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/fortisandbox object.

        Configure FortiSandbox.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable FortiSandbox.
            forticloud: Enable/disable FortiSandbox Cloud.
            inline_scan: Enable/disable FortiSandbox inline scan.
            server: Server IP address or FQDN of the remote FortiSandbox.
            source_ip: Source IP address for communications to FortiSandbox.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_fortisandbox.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_fortisandbox.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            forticloud=forticloud,
            inline_scan=inline_scan,
            server=server,
            source_ip=source_ip,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            enc_algorithm=enc_algorithm,
            ssl_min_proto_version=ssl_min_proto_version,
            email=email,
            ca=ca,
            cn=cn,
            certificate_verification=certificate_verification,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fortisandbox import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/fortisandbox",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/fortisandbox/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





