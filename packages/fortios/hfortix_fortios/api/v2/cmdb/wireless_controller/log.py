"""
FortiOS CMDB - Wireless_controller log

Configuration endpoint for managing cmdb wireless_controller/log objects.

API Endpoints:
    GET    /cmdb/wireless_controller/log
    POST   /cmdb/wireless_controller/log
    PUT    /cmdb/wireless_controller/log/{identifier}
    DELETE /cmdb/wireless_controller/log/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_log.get()

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


class Log(MetadataMixin):
    """Log Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "log"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Log endpoint."""
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
        Retrieve wireless_controller/log configuration.

        Configure wireless controller event log filters.

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
            >>> # Get all wireless_controller/log objects
            >>> result = fgt.api.cmdb.wireless_controller_log.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_log.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_log.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/log object
            - put(): Update existing wireless_controller/log object
            - delete(): Remove wireless_controller/log object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wireless-controller/log/{name}"
        else:
            endpoint = "/wireless-controller/log"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        addrgrp_log: str | None = None,
        ble_log: str | None = None,
        clb_log: str | None = None,
        dhcp_starv_log: str | None = None,
        led_sched_log: str | None = None,
        radio_event_log: str | None = None,
        rogue_event_log: str | None = None,
        sta_event_log: str | None = None,
        sta_locate_log: str | None = None,
        wids_log: str | None = None,
        wtp_event_log: str | None = None,
        wtp_fips_event_log: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/log object.

        Configure wireless controller event log filters.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable wireless event logging.
            addrgrp_log: Lowest severity level to log address group message.
            ble_log: Lowest severity level to log BLE detection message.
            clb_log: Lowest severity level to log client load balancing message.
            dhcp_starv_log: Lowest severity level to log DHCP starvation event message.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_log.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_log.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            addrgrp_log=addrgrp_log,
            ble_log=ble_log,
            clb_log=clb_log,
            dhcp_starv_log=dhcp_starv_log,
            led_sched_log=led_sched_log,
            radio_event_log=radio_event_log,
            rogue_event_log=rogue_event_log,
            sta_event_log=sta_event_log,
            sta_locate_log=sta_locate_log,
            wids_log=wids_log,
            wtp_event_log=wtp_event_log,
            wtp_fips_event_log=wtp_fips_event_log,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.log import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/log",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/wireless-controller/log/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





