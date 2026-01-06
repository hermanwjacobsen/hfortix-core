"""
FortiOS CMDB - Wireless_controller timers

Configuration endpoint for managing cmdb wireless_controller/timers objects.

API Endpoints:
    GET    /cmdb/wireless_controller/timers
    POST   /cmdb/wireless_controller/timers
    PUT    /cmdb/wireless_controller/timers/{identifier}
    DELETE /cmdb/wireless_controller/timers/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_timers.get()

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


class Timers(MetadataMixin):
    """Timers Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "timers"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Timers endpoint."""
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
        Retrieve wireless_controller/timers configuration.

        Configure CAPWAP timers.

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
            >>> # Get all wireless_controller/timers objects
            >>> result = fgt.api.cmdb.wireless_controller_timers.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_timers.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_timers.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/timers object
            - put(): Update existing wireless_controller/timers object
            - delete(): Remove wireless_controller/timers object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wireless-controller/timers/{name}"
        else:
            endpoint = "/wireless-controller/timers"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        echo_interval: int | None = None,
        nat_session_keep_alive: int | None = None,
        discovery_interval: int | None = None,
        client_idle_timeout: int | None = None,
        client_idle_rehome_timeout: int | None = None,
        auth_timeout: int | None = None,
        rogue_ap_log: int | None = None,
        fake_ap_log: int | None = None,
        sta_offline_cleanup: int | None = None,
        sta_offline_ip2mac_cleanup: int | None = None,
        sta_cap_cleanup: int | None = None,
        rogue_ap_cleanup: int | None = None,
        rogue_sta_cleanup: int | None = None,
        wids_entry_cleanup: int | None = None,
        ble_device_cleanup: int | None = None,
        sta_stats_interval: int | None = None,
        vap_stats_interval: int | None = None,
        radio_stats_interval: int | None = None,
        sta_capability_interval: int | None = None,
        sta_locate_timer: int | None = None,
        ipsec_intf_cleanup: int | None = None,
        ble_scan_report_intv: int | None = None,
        drma_interval: int | None = None,
        ap_reboot_wait_interval1: int | None = None,
        ap_reboot_wait_time: str | None = None,
        ap_reboot_wait_interval2: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/timers object.

        Configure CAPWAP timers.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            echo_interval: Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).
            nat_session_keep_alive: Maximal time in seconds between control requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec, default = 0).
            discovery_interval: Time between discovery requests (2 - 180 sec, default = 5).
            client_idle_timeout: Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).
            client_idle_rehome_timeout: Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec, default = 20, 0 for no timeout).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_timers.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_timers.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            echo_interval=echo_interval,
            nat_session_keep_alive=nat_session_keep_alive,
            discovery_interval=discovery_interval,
            client_idle_timeout=client_idle_timeout,
            client_idle_rehome_timeout=client_idle_rehome_timeout,
            auth_timeout=auth_timeout,
            rogue_ap_log=rogue_ap_log,
            fake_ap_log=fake_ap_log,
            sta_offline_cleanup=sta_offline_cleanup,
            sta_offline_ip2mac_cleanup=sta_offline_ip2mac_cleanup,
            sta_cap_cleanup=sta_cap_cleanup,
            rogue_ap_cleanup=rogue_ap_cleanup,
            rogue_sta_cleanup=rogue_sta_cleanup,
            wids_entry_cleanup=wids_entry_cleanup,
            ble_device_cleanup=ble_device_cleanup,
            sta_stats_interval=sta_stats_interval,
            vap_stats_interval=vap_stats_interval,
            radio_stats_interval=radio_stats_interval,
            sta_capability_interval=sta_capability_interval,
            sta_locate_timer=sta_locate_timer,
            ipsec_intf_cleanup=ipsec_intf_cleanup,
            ble_scan_report_intv=ble_scan_report_intv,
            drma_interval=drma_interval,
            ap_reboot_wait_interval1=ap_reboot_wait_interval1,
            ap_reboot_wait_time=ap_reboot_wait_time,
            ap_reboot_wait_interval2=ap_reboot_wait_interval2,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.timers import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/timers",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/wireless-controller/timers/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





