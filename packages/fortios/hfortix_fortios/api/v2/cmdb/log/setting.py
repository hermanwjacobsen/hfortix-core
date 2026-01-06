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

from typing import TYPE_CHECKING, Any, Union, Literal
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
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

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
        resolve_ip: Literal["enable", "disable"] | None = None,
        resolve_port: Literal["enable", "disable"] | None = None,
        log_user_in_upper: Literal["enable", "disable"] | None = None,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = None,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = None,
        extended_log: Literal["enable", "disable"] | None = None,
        local_in_allow: Literal["enable", "disable"] | None = None,
        local_in_deny_unicast: Literal["enable", "disable"] | None = None,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = None,
        local_in_policy_log: Literal["enable", "disable"] | None = None,
        local_out: Literal["enable", "disable"] | None = None,
        local_out_ioc_detection: Literal["enable", "disable"] | None = None,
        daemon_log: Literal["enable", "disable"] | None = None,
        neighbor_event: Literal["enable", "disable"] | None = None,
        brief_traffic_format: Literal["enable", "disable"] | None = None,
        user_anonymize: Literal["enable", "disable"] | None = None,
        expolicy_implicit_log: Literal["enable", "disable"] | None = None,
        log_policy_comment: Literal["enable", "disable"] | None = None,
        faz_override: Literal["enable", "disable"] | None = None,
        syslog_override: Literal["enable", "disable"] | None = None,
        rest_api_set: Literal["enable", "disable"] | None = None,
        rest_api_get: Literal["enable", "disable"] | None = None,
        rest_api_performance: Literal["enable", "disable"] | None = None,
        long_live_session_stat: Literal["enable", "disable"] | None = None,
        extended_utm_log: Literal["enable", "disable"] | None = None,
        zone_name: Literal["enable", "disable"] | None = None,
        web_svc_perf: Literal["enable", "disable"] | None = None,
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





    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move log/setting object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.log_setting.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/log/setting",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone log/setting object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.log_setting.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/log/setting",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if log/setting object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.log_setting.exists(name="myobj"):
            ...     fgt.api.cmdb.log_setting.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
                vdom=vdom,
                raw_json=True
            )
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

