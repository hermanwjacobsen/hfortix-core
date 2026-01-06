"""
FortiOS CMDB - Switch_controller system

Configuration endpoint for managing cmdb switch_controller/system objects.

API Endpoints:
    GET    /cmdb/switch_controller/system
    POST   /cmdb/switch_controller/system
    PUT    /cmdb/switch_controller/system/{identifier}
    DELETE /cmdb/switch_controller/system/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_system.get()

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


class System(MetadataMixin):
    """System Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "system"

    def __init__(self, client: "IHTTPClient"):
        """Initialize System endpoint."""
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
        Retrieve switch_controller/system configuration.

        Configure system-wide switch controller settings.

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
            >>> # Get all switch_controller/system objects
            >>> result = fgt.api.cmdb.switch_controller_system.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_system.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_system.get(action="schema")

        See Also:
            - post(): Create new switch_controller/system object
            - put(): Update existing switch_controller/system object
            - delete(): Remove switch_controller/system object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/system/{name}"
        else:
            endpoint = "/switch-controller/system"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        parallel_process_override: str | None = None,
        parallel_process: int | None = None,
        data_sync_interval: int | None = None,
        iot_weight_threshold: int | None = None,
        iot_scan_interval: int | None = None,
        iot_holdoff: int | None = None,
        iot_mac_idle: int | None = None,
        nac_periodic_interval: int | None = None,
        dynamic_periodic_interval: int | None = None,
        tunnel_mode: str | None = None,
        caputp_echo_interval: int | None = None,
        caputp_max_retransmit: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/system object.

        Configure system-wide switch controller settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            parallel_process_override: Enable/disable parallel process override.
            parallel_process: Maximum number of parallel processes.
            data_sync_interval: Time interval between collection of switch data (30 - 1800 sec, default = 60, 0 = disable).
            iot_weight_threshold: MAC entry's confidence value. Value is re-queried when below this value (default = 1, 0 = disable).
            iot_scan_interval: IoT scan interval (2 - 10080 mins, default = 60 mins, 0 = disable).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_system.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_system.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            parallel_process_override=parallel_process_override,
            parallel_process=parallel_process,
            data_sync_interval=data_sync_interval,
            iot_weight_threshold=iot_weight_threshold,
            iot_scan_interval=iot_scan_interval,
            iot_holdoff=iot_holdoff,
            iot_mac_idle=iot_mac_idle,
            nac_periodic_interval=nac_periodic_interval,
            dynamic_periodic_interval=dynamic_periodic_interval,
            tunnel_mode=tunnel_mode,
            caputp_echo_interval=caputp_echo_interval,
            caputp_max_retransmit=caputp_max_retransmit,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.system import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/system",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/system/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





