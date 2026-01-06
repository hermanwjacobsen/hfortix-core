"""
FortiOS CMDB - Switch_controller igmp_snooping

Configuration endpoint for managing cmdb switch_controller/igmp_snooping objects.

API Endpoints:
    GET    /cmdb/switch_controller/igmp_snooping
    POST   /cmdb/switch_controller/igmp_snooping
    PUT    /cmdb/switch_controller/igmp_snooping/{identifier}
    DELETE /cmdb/switch_controller/igmp_snooping/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_igmp_snooping.get()

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


class IgmpSnooping(MetadataMixin):
    """IgmpSnooping Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "igmp_snooping"

    def __init__(self, client: "IHTTPClient"):
        """Initialize IgmpSnooping endpoint."""
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
        Retrieve switch_controller/igmp_snooping configuration.

        Configure FortiSwitch IGMP snooping global settings.

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
            >>> # Get all switch_controller/igmp_snooping objects
            >>> result = fgt.api.cmdb.switch_controller_igmp_snooping.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_igmp_snooping.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_igmp_snooping.get(action="schema")

        See Also:
            - post(): Create new switch_controller/igmp_snooping object
            - put(): Update existing switch_controller/igmp_snooping object
            - delete(): Remove switch_controller/igmp_snooping object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/igmp-snooping/{name}"
        else:
            endpoint = "/switch-controller/igmp-snooping"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        aging_time: int | None = None,
        flood_unknown_multicast: str | None = None,
        query_interval: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/igmp_snooping object.

        Configure FortiSwitch IGMP snooping global settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            aging_time: Maximum number of seconds to retain a multicast snooping entry for which no packets have been seen (15 - 3600 sec, default = 300).
            flood_unknown_multicast: Enable/disable unknown multicast flooding.
            query_interval: Maximum time after which IGMP query will be sent (10 - 1200 sec, default = 125).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_igmp_snooping.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_igmp_snooping.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            aging_time=aging_time,
            flood_unknown_multicast=flood_unknown_multicast,
            query_interval=query_interval,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.igmp_snooping import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/igmp_snooping",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/igmp-snooping/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





