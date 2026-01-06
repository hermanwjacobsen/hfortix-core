"""
FortiOS CMDB - Log setting

Configuration endpoint for managing cmdb log/setting objects.

API Endpoints:
    GET    /cmdb/log/setting
    POST   /cmdb/log/setting
    PUT    /cmdb/log/setting/{identifier}
    DELETE /cmdb/log/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_setting.get()

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
        Retrieve log/setting configuration.

        Configure general log settings.

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
            >>> # Get all log/setting objects
            >>> result = fgt.api.cmdb.log_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_setting.get(action="schema")

        See Also:
            - post(): Create new log/setting object
            - put(): Update existing log/setting object
            - delete(): Remove log/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log/setting/{name}"
        else:
            endpoint = "/log/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        resolve_ip: str | None = None,
        resolve_port: str | None = None,
        log_user_in_upper: str | None = None,
        fwpolicy_implicit_log: str | None = None,
        fwpolicy6_implicit_log: str | None = None,
        extended_log: str | None = None,
        local_in_allow: str | None = None,
        local_in_deny_unicast: str | None = None,
        local_in_deny_broadcast: str | None = None,
        local_in_policy_log: str | None = None,
        local_out: str | None = None,
        local_out_ioc_detection: str | None = None,
        daemon_log: str | None = None,
        neighbor_event: str | None = None,
        brief_traffic_format: str | None = None,
        user_anonymize: str | None = None,
        expolicy_implicit_log: str | None = None,
        log_policy_comment: str | None = None,
        faz_override: str | None = None,
        syslog_override: str | None = None,
        rest_api_set: str | None = None,
        rest_api_get: str | None = None,
        rest_api_performance: str | None = None,
        long_live_session_stat: str | None = None,
        extended_utm_log: str | None = None,
        zone_name: str | None = None,
        web_svc_perf: str | None = None,
        custom_log_fields: str | list | None = None,
        anonymization_hash: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/setting object.

        Configure general log settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            resolve_ip: Enable/disable adding resolved domain names to traffic logs if possible.
            resolve_port: Enable/disable adding resolved service names to traffic logs.
            log_user_in_upper: Enable/disable logs with user-in-upper.
            fwpolicy_implicit_log: Enable/disable implicit firewall policy logging.
            fwpolicy6_implicit_log: Enable/disable implicit firewall policy6 logging.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            resolve_ip=resolve_ip,
            resolve_port=resolve_port,
            log_user_in_upper=log_user_in_upper,
            fwpolicy_implicit_log=fwpolicy_implicit_log,
            fwpolicy6_implicit_log=fwpolicy6_implicit_log,
            extended_log=extended_log,
            local_in_allow=local_in_allow,
            local_in_deny_unicast=local_in_deny_unicast,
            local_in_deny_broadcast=local_in_deny_broadcast,
            local_in_policy_log=local_in_policy_log,
            local_out=local_out,
            local_out_ioc_detection=local_out_ioc_detection,
            daemon_log=daemon_log,
            neighbor_event=neighbor_event,
            brief_traffic_format=brief_traffic_format,
            user_anonymize=user_anonymize,
            expolicy_implicit_log=expolicy_implicit_log,
            log_policy_comment=log_policy_comment,
            faz_override=faz_override,
            syslog_override=syslog_override,
            rest_api_set=rest_api_set,
            rest_api_get=rest_api_get,
            rest_api_performance=rest_api_performance,
            long_live_session_stat=long_live_session_stat,
            extended_utm_log=extended_utm_log,
            zone_name=zone_name,
            web_svc_perf=web_svc_perf,
            custom_log_fields=custom_log_fields,
            anonymization_hash=anonymization_hash,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





