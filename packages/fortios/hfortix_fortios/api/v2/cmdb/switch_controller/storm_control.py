"""
FortiOS CMDB - Switch_controller storm_control

Configuration endpoint for managing cmdb switch_controller/storm_control objects.

API Endpoints:
    GET    /cmdb/switch_controller/storm_control
    POST   /cmdb/switch_controller/storm_control
    PUT    /cmdb/switch_controller/storm_control/{identifier}
    DELETE /cmdb/switch_controller/storm_control/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_storm_control.get()

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


class StormControl(MetadataMixin):
    """StormControl Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "storm_control"

    def __init__(self, client: "IHTTPClient"):
        """Initialize StormControl endpoint."""
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
        Retrieve switch_controller/storm_control configuration.

        Configure FortiSwitch storm control.

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
            >>> # Get all switch_controller/storm_control objects
            >>> result = fgt.api.cmdb.switch_controller_storm_control.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_storm_control.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_storm_control.get(action="schema")

        See Also:
            - post(): Create new switch_controller/storm_control object
            - put(): Update existing switch_controller/storm_control object
            - delete(): Remove switch_controller/storm_control object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/storm-control/{name}"
        else:
            endpoint = "/switch-controller/storm-control"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        rate: int | None = None,
        burst_size_level: int | None = None,
        unknown_unicast: str | None = None,
        unknown_multicast: str | None = None,
        broadcast: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/storm_control object.

        Configure FortiSwitch storm control.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            rate: Rate in packets per second at which storm control drops excess traffic(0-10000000, default=500, drop-all=0).
            burst_size_level: Increase level to handle bursty traffic (0 - 4, default = 0).
            unknown_unicast: Enable/disable storm control to drop unknown unicast traffic.
            unknown_multicast: Enable/disable storm control to drop unknown multicast traffic.
            broadcast: Enable/disable storm control to drop broadcast traffic.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_storm_control.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_storm_control.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            rate=rate,
            burst_size_level=burst_size_level,
            unknown_unicast=unknown_unicast,
            unknown_multicast=unknown_multicast,
            broadcast=broadcast,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.storm_control import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/storm_control",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/storm-control/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





