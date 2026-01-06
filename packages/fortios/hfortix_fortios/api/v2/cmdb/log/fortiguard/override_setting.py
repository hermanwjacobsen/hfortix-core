"""
FortiOS CMDB - Log fortiguard override_setting

Configuration endpoint for managing cmdb log/fortiguard/override_setting objects.

API Endpoints:
    GET    /cmdb/log/fortiguard/override_setting
    POST   /cmdb/log/fortiguard/override_setting
    PUT    /cmdb/log/fortiguard/override_setting/{identifier}
    DELETE /cmdb/log/fortiguard/override_setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_fortiguard_override_setting.get()

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


class OverrideSetting(MetadataMixin):
    """OverrideSetting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "override_setting"

    def __init__(self, client: "IHTTPClient"):
        """Initialize OverrideSetting endpoint."""
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
        Retrieve log/fortiguard/override_setting configuration.

        Override global FortiCloud logging settings for this VDOM.

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
            >>> # Get all log/fortiguard/override_setting objects
            >>> result = fgt.api.cmdb.log_fortiguard_override_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_fortiguard_override_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_fortiguard_override_setting.get(action="schema")

        See Also:
            - post(): Create new log/fortiguard/override_setting object
            - put(): Update existing log/fortiguard/override_setting object
            - delete(): Remove log/fortiguard/override_setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log.fortiguard/override-setting/{name}"
        else:
            endpoint = "/log.fortiguard/override-setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        override: str | None = None,
        status: str | None = None,
        upload_option: str | None = None,
        upload_interval: str | None = None,
        upload_day: str | None = None,
        upload_time: str | None = None,
        priority: str | None = None,
        max_log_rate: int | None = None,
        access_config: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/fortiguard/override_setting object.

        Override global FortiCloud logging settings for this VDOM.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            override: Overriding FortiCloud settings for this VDOM or use global settings.
            status: Enable/disable logging to FortiCloud.
            upload_option: Configure how log messages are sent to FortiCloud.
            upload_interval: Frequency of uploading log files to FortiCloud.
            upload_day: Day of week to roll logs.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_fortiguard_override_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_fortiguard_override_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            override=override,
            status=status,
            upload_option=upload_option,
            upload_interval=upload_interval,
            upload_day=upload_day,
            upload_time=upload_time,
            priority=priority,
            max_log_rate=max_log_rate,
            access_config=access_config,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.override_setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/fortiguard/override_setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log.fortiguard/override-setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





