"""
FortiOS CMDB - System ha_monitor

Configuration endpoint for managing cmdb system/ha_monitor objects.

API Endpoints:
    GET    /cmdb/system/ha_monitor
    POST   /cmdb/system/ha_monitor
    PUT    /cmdb/system/ha_monitor/{identifier}
    DELETE /cmdb/system/ha_monitor/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ha_monitor.get()

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


class HaMonitor(MetadataMixin):
    """HaMonitor Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ha_monitor"

    def __init__(self, client: "IHTTPClient"):
        """Initialize HaMonitor endpoint."""
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
        Retrieve system/ha_monitor configuration.

        Configure HA monitor.

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
            >>> # Get all system/ha_monitor objects
            >>> result = fgt.api.cmdb.system_ha_monitor.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ha_monitor.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ha_monitor.get(action="schema")

        See Also:
            - post(): Create new system/ha_monitor object
            - put(): Update existing system/ha_monitor object
            - delete(): Remove system/ha_monitor object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ha-monitor/{name}"
        else:
            endpoint = "/system/ha-monitor"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        monitor_vlan: str | None = None,
        vlan_hb_interval: int | None = None,
        vlan_hb_lost_threshold: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ha_monitor object.

        Configure HA monitor.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            monitor_vlan: Enable/disable monitor VLAN interfaces.
            vlan_hb_interval: Configure heartbeat interval (seconds).
            vlan_hb_lost_threshold: VLAN lost heartbeat threshold (1 - 60).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ha_monitor.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ha_monitor.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            monitor_vlan=monitor_vlan,
            vlan_hb_interval=vlan_hb_interval,
            vlan_hb_lost_threshold=vlan_hb_lost_threshold,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ha_monitor import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ha_monitor",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ha-monitor/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





