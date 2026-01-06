"""
FortiOS CMDB - Switch_controller snmp_sysinfo

Configuration endpoint for managing cmdb switch_controller/snmp_sysinfo objects.

API Endpoints:
    GET    /cmdb/switch_controller/snmp_sysinfo
    POST   /cmdb/switch_controller/snmp_sysinfo
    PUT    /cmdb/switch_controller/snmp_sysinfo/{identifier}
    DELETE /cmdb/switch_controller/snmp_sysinfo/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_snmp_sysinfo.get()

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


class SnmpSysinfo(MetadataMixin):
    """SnmpSysinfo Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "snmp_sysinfo"

    def __init__(self, client: "IHTTPClient"):
        """Initialize SnmpSysinfo endpoint."""
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
        Retrieve switch_controller/snmp_sysinfo configuration.

        Configure FortiSwitch SNMP system information globally.

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
            >>> # Get all switch_controller/snmp_sysinfo objects
            >>> result = fgt.api.cmdb.switch_controller_snmp_sysinfo.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_snmp_sysinfo.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_snmp_sysinfo.get(action="schema")

        See Also:
            - post(): Create new switch_controller/snmp_sysinfo object
            - put(): Update existing switch_controller/snmp_sysinfo object
            - delete(): Remove switch_controller/snmp_sysinfo object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/snmp-sysinfo/{name}"
        else:
            endpoint = "/switch-controller/snmp-sysinfo"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        engine_id: str | None = None,
        description: str | None = None,
        contact_info: str | None = None,
        location: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/snmp_sysinfo object.

        Configure FortiSwitch SNMP system information globally.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable SNMP.
            engine_id: Local SNMP engine ID string (max 24 char).
            description: System description.
            contact_info: Contact information.
            location: System location.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_snmp_sysinfo.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_snmp_sysinfo.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            engine_id=engine_id,
            description=description,
            contact_info=contact_info,
            location=location,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.snmp_sysinfo import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/snmp_sysinfo",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/snmp-sysinfo/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





