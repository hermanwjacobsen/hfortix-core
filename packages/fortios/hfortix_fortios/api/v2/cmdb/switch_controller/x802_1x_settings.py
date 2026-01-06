"""
FortiOS CMDB - Switch_controller x802_1x_settings

Configuration endpoint for managing cmdb switch_controller/x802_1x_settings objects.

API Endpoints:
    GET    /cmdb/switch_controller/x802_1x_settings
    POST   /cmdb/switch_controller/x802_1x_settings
    PUT    /cmdb/switch_controller/x802_1x_settings/{identifier}
    DELETE /cmdb/switch_controller/x802_1x_settings/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_x802_1x_settings.get()

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


class X8021xSettings(MetadataMixin):
    """X8021xSettings Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "x802_1x_settings"

    def __init__(self, client: "IHTTPClient"):
        """Initialize X8021xSettings endpoint."""
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
        Retrieve switch_controller/x802_1x_settings configuration.

        Configure global 802.1X settings.

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
            >>> # Get all switch_controller/x802_1x_settings objects
            >>> result = fgt.api.cmdb.switch_controller_x802_1x_settings.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_x802_1x_settings.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_x802_1x_settings.get(action="schema")

        See Also:
            - post(): Create new switch_controller/x802_1x_settings object
            - put(): Update existing switch_controller/x802_1x_settings object
            - delete(): Remove switch_controller/x802_1x_settings object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/802-1X-settings/{name}"
        else:
            endpoint = "/switch-controller/802-1X-settings"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        link_down_auth: str | None = None,
        reauth_period: int | None = None,
        max_reauth_attempt: int | None = None,
        tx_period: int | None = None,
        mab_reauth: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_calling_station_delimiter: str | None = None,
        mac_called_station_delimiter: str | None = None,
        mac_case: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/x802_1x_settings object.

        Configure global 802.1X settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            link_down_auth: Interface-reauthentication state to set if a link is down.
            reauth_period: Period of time to allow for reauthentication (1 - 1440 sec, default = 60, 0 = disable reauthentication).
            max_reauth_attempt: Maximum number of authentication attempts (0 - 15, default = 3).
            tx_period: 802.1X Tx period (seconds, default=30).
            mab_reauth: Enable/disable MAB re-authentication.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_x802_1x_settings.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_x802_1x_settings.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            link_down_auth=link_down_auth,
            reauth_period=reauth_period,
            max_reauth_attempt=max_reauth_attempt,
            tx_period=tx_period,
            mab_reauth=mab_reauth,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_calling_station_delimiter=mac_calling_station_delimiter,
            mac_called_station_delimiter=mac_called_station_delimiter,
            mac_case=mac_case,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.x802_1x_settings import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/x802_1x_settings",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/802-1X-settings/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





