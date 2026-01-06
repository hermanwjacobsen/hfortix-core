"""
FortiOS CMDB - Switch_controller ip_source_guard_log

Configuration endpoint for managing cmdb switch_controller/ip_source_guard_log objects.

API Endpoints:
    GET    /cmdb/switch_controller/ip_source_guard_log
    POST   /cmdb/switch_controller/ip_source_guard_log
    PUT    /cmdb/switch_controller/ip_source_guard_log/{identifier}
    DELETE /cmdb/switch_controller/ip_source_guard_log/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_ip_source_guard_log.get()

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


class IpSourceGuardLog(MetadataMixin):
    """IpSourceGuardLog Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ip_source_guard_log"

    def __init__(self, client: "IHTTPClient"):
        """Initialize IpSourceGuardLog endpoint."""
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
        Retrieve switch_controller/ip_source_guard_log configuration.

        Configure FortiSwitch ip source guard log.

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
            >>> # Get all switch_controller/ip_source_guard_log objects
            >>> result = fgt.api.cmdb.switch_controller_ip_source_guard_log.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_ip_source_guard_log.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_ip_source_guard_log.get(action="schema")

        See Also:
            - post(): Create new switch_controller/ip_source_guard_log object
            - put(): Update existing switch_controller/ip_source_guard_log object
            - delete(): Remove switch_controller/ip_source_guard_log object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/ip-source-guard-log/{name}"
        else:
            endpoint = "/switch-controller/ip-source-guard-log"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        log_violations: str | None = None,
        violation_timer: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/ip_source_guard_log object.

        Configure FortiSwitch ip source guard log.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            log_violations: Enable/Disable log violations for IP source guard logging.
            violation_timer: IP source gurad log violation timer in seconds (0 - 1500, default = 0).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_ip_source_guard_log.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_ip_source_guard_log.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            log_violations=log_violations,
            violation_timer=violation_timer,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ip_source_guard_log import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/ip_source_guard_log",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/ip-source-guard-log/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





