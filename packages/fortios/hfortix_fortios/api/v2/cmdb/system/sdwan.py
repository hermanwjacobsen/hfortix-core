"""
FortiOS CMDB - System sdwan

Configuration endpoint for managing cmdb system/sdwan objects.

API Endpoints:
    GET    /cmdb/system/sdwan
    POST   /cmdb/system/sdwan
    PUT    /cmdb/system/sdwan/{identifier}
    DELETE /cmdb/system/sdwan/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_sdwan.get()

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


class Sdwan(MetadataMixin):
    """Sdwan Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "sdwan"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Sdwan endpoint."""
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
        Retrieve system/sdwan configuration.

        Configure redundant Internet connections with multiple outbound links and health-check profiles.

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
            >>> # Get all system/sdwan objects
            >>> result = fgt.api.cmdb.system_sdwan.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_sdwan.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_sdwan.get(action="schema")

        See Also:
            - post(): Create new system/sdwan object
            - put(): Update existing system/sdwan object
            - delete(): Remove system/sdwan object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/sdwan/{name}"
        else:
            endpoint = "/system/sdwan"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        load_balance_mode: str | None = None,
        speedtest_bypass_routing: str | None = None,
        duplication_max_num: int | None = None,
        duplication_max_discrepancy: int | None = None,
        neighbor_hold_down: str | None = None,
        neighbor_hold_down_time: int | None = None,
        app_perf_log_period: int | None = None,
        neighbor_hold_boot_time: int | None = None,
        fail_detect: str | None = None,
        fail_alert_interfaces: str | list | None = None,
        zone: str | list | None = None,
        members: str | list | None = None,
        health_check: str | list | None = None,
        service: str | list | None = None,
        neighbor: str | list | None = None,
        duplication: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/sdwan object.

        Configure redundant Internet connections with multiple outbound links and health-check profiles.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable SD-WAN.
            load_balance_mode: Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.
            speedtest_bypass_routing: Enable/disable bypass routing when speedtest on a SD-WAN member.
            duplication_max_num: Maximum number of interface members a packet is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3, the original packet plus 2 more copies are created).
            duplication_max_discrepancy: Maximum discrepancy between two packets for deduplication in milliseconds (250 - 1000, default = 250).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_sdwan.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_sdwan.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            load_balance_mode=load_balance_mode,
            speedtest_bypass_routing=speedtest_bypass_routing,
            duplication_max_num=duplication_max_num,
            duplication_max_discrepancy=duplication_max_discrepancy,
            neighbor_hold_down=neighbor_hold_down,
            neighbor_hold_down_time=neighbor_hold_down_time,
            app_perf_log_period=app_perf_log_period,
            neighbor_hold_boot_time=neighbor_hold_boot_time,
            fail_detect=fail_detect,
            fail_alert_interfaces=fail_alert_interfaces,
            zone=zone,
            members=members,
            health_check=health_check,
            service=service,
            neighbor=neighbor,
            duplication=duplication,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.sdwan import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdwan",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/sdwan/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





