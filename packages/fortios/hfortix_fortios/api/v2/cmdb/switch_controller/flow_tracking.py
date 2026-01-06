"""
FortiOS CMDB - Switch_controller flow_tracking

Configuration endpoint for managing cmdb switch_controller/flow_tracking objects.

API Endpoints:
    GET    /cmdb/switch_controller/flow_tracking
    POST   /cmdb/switch_controller/flow_tracking
    PUT    /cmdb/switch_controller/flow_tracking/{identifier}
    DELETE /cmdb/switch_controller/flow_tracking/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_flow_tracking.get()

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


class FlowTracking(MetadataMixin):
    """FlowTracking Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "flow_tracking"

    def __init__(self, client: "IHTTPClient"):
        """Initialize FlowTracking endpoint."""
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
        Retrieve switch_controller/flow_tracking configuration.

        Configure FortiSwitch flow tracking and export via ipfix/netflow.

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
            >>> # Get all switch_controller/flow_tracking objects
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_flow_tracking.get(action="schema")

        See Also:
            - post(): Create new switch_controller/flow_tracking object
            - put(): Update existing switch_controller/flow_tracking object
            - delete(): Remove switch_controller/flow_tracking object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/flow-tracking/{name}"
        else:
            endpoint = "/switch-controller/flow-tracking"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        sample_mode: str | None = None,
        sample_rate: int | None = None,
        format: str | None = None,
        collectors: str | list | None = None,
        level: str | None = None,
        max_export_pkt_size: int | None = None,
        template_export_period: int | None = None,
        timeout_general: int | None = None,
        timeout_icmp: int | None = None,
        timeout_max: int | None = None,
        timeout_tcp: int | None = None,
        timeout_tcp_fin: int | None = None,
        timeout_tcp_rst: int | None = None,
        timeout_udp: int | None = None,
        aggregates: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/flow_tracking object.

        Configure FortiSwitch flow tracking and export via ipfix/netflow.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            sample_mode: Configure sample mode for the flow tracking.
            sample_rate: Configure sample rate for the perimeter and device-ingress sampling(0 - 99999).
            format: Configure flow tracking protocol.
            collectors: Configure collectors for the flow.
            level: Configure flow tracking level.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            sample_mode=sample_mode,
            sample_rate=sample_rate,
            format=format,
            collectors=collectors,
            level=level,
            max_export_pkt_size=max_export_pkt_size,
            template_export_period=template_export_period,
            timeout_general=timeout_general,
            timeout_icmp=timeout_icmp,
            timeout_max=timeout_max,
            timeout_tcp=timeout_tcp,
            timeout_tcp_fin=timeout_tcp_fin,
            timeout_tcp_rst=timeout_tcp_rst,
            timeout_udp=timeout_udp,
            aggregates=aggregates,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.flow_tracking import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/flow_tracking",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/flow-tracking/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





