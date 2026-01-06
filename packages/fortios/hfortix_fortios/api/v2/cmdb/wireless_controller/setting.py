"""
FortiOS CMDB - Wireless_controller setting

Configuration endpoint for managing cmdb wireless_controller/setting objects.

API Endpoints:
    GET    /cmdb/wireless_controller/setting
    POST   /cmdb/wireless_controller/setting
    PUT    /cmdb/wireless_controller/setting/{identifier}
    DELETE /cmdb/wireless_controller/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_setting.get()

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


class Setting(MetadataMixin):
    """Setting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "setting"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Setting endpoint."""
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
        Retrieve wireless_controller/setting configuration.

        VDOM wireless controller configuration.

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
            >>> # Get all wireless_controller/setting objects
            >>> result = fgt.api.cmdb.wireless_controller_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_setting.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/setting object
            - put(): Update existing wireless_controller/setting object
            - delete(): Remove wireless_controller/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wireless-controller/setting/{name}"
        else:
            endpoint = "/wireless-controller/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        account_id: str | None = None,
        country: str | None = None,
        duplicate_ssid: str | None = None,
        fapc_compatibility: str | None = None,
        wfa_compatibility: str | None = None,
        phishing_ssid_detect: str | None = None,
        fake_ssid_action: str | list | None = None,
        offending_ssid: str | list | None = None,
        device_weight: int | None = None,
        device_holdoff: int | None = None,
        device_idle: int | None = None,
        firmware_provision_on_authorization: str | None = None,
        rolling_wtp_upgrade: str | None = None,
        darrp_optimize: int | None = None,
        darrp_optimize_schedules: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/setting object.

        VDOM wireless controller configuration.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            account_id: FortiCloud customer account ID.
            country: Country or region in which the FortiGate is located. The country determines the 802.11 bands and channels that are available.
            duplicate_ssid: Enable/disable allowing Virtual Access Points (VAPs) to use the same SSID name in the same VDOM.
            fapc_compatibility: Enable/disable FAP-C series compatibility.
            wfa_compatibility: Enable/disable WFA compatibility.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            account_id=account_id,
            country=country,
            duplicate_ssid=duplicate_ssid,
            fapc_compatibility=fapc_compatibility,
            wfa_compatibility=wfa_compatibility,
            phishing_ssid_detect=phishing_ssid_detect,
            fake_ssid_action=fake_ssid_action,
            offending_ssid=offending_ssid,
            device_weight=device_weight,
            device_holdoff=device_holdoff,
            device_idle=device_idle,
            firmware_provision_on_authorization=firmware_provision_on_authorization,
            rolling_wtp_upgrade=rolling_wtp_upgrade,
            darrp_optimize=darrp_optimize,
            darrp_optimize_schedules=darrp_optimize_schedules,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/wireless-controller/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





