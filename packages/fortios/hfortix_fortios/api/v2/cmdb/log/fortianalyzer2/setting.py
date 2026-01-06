"""
FortiOS CMDB - Log fortianalyzer2 setting

Configuration endpoint for managing cmdb log/fortianalyzer2/setting objects.

API Endpoints:
    GET    /cmdb/log/fortianalyzer2/setting
    POST   /cmdb/log/fortianalyzer2/setting
    PUT    /cmdb/log/fortianalyzer2/setting/{identifier}
    DELETE /cmdb/log/fortianalyzer2/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_fortianalyzer2_setting.get()

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
        Retrieve log/fortianalyzer2/setting configuration.

        Global FortiAnalyzer settings.

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
            >>> # Get all log/fortianalyzer2/setting objects
            >>> result = fgt.api.cmdb.log_fortianalyzer2_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_fortianalyzer2_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_fortianalyzer2_setting.get(action="schema")

        See Also:
            - post(): Create new log/fortianalyzer2/setting object
            - put(): Update existing log/fortianalyzer2/setting object
            - delete(): Remove log/fortianalyzer2/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log.fortianalyzer2/setting/{name}"
        else:
            endpoint = "/log.fortianalyzer2/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        ips_archive: str | None = None,
        server: str | None = None,
        alt_server: str | None = None,
        fallback_to_primary: str | None = None,
        certificate_verification: str | None = None,
        serial: str | list | None = None,
        server_cert_ca: str | None = None,
        preshared_key: str | None = None,
        access_config: str | None = None,
        hmac_algorithm: str | None = None,
        enc_algorithm: str | None = None,
        ssl_min_proto_version: str | None = None,
        conn_timeout: int | None = None,
        monitor_keepalive_period: int | None = None,
        monitor_failure_retry_period: int | None = None,
        certificate: str | None = None,
        source_ip: str | None = None,
        upload_option: str | None = None,
        upload_interval: str | None = None,
        upload_day: str | None = None,
        upload_time: str | None = None,
        reliable: str | None = None,
        priority: str | None = None,
        max_log_rate: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/fortianalyzer2/setting object.

        Global FortiAnalyzer settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable logging to FortiAnalyzer.
            ips_archive: Enable/disable IPS packet archive logging.
            server: The remote FortiAnalyzer.
            alt_server: Alternate FortiAnalyzer.
            fallback_to_primary: Enable/disable this FortiGate unit to fallback to the primary FortiAnalyzer when it is available.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_fortianalyzer2_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_fortianalyzer2_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            ips_archive=ips_archive,
            server=server,
            alt_server=alt_server,
            fallback_to_primary=fallback_to_primary,
            certificate_verification=certificate_verification,
            serial=serial,
            server_cert_ca=server_cert_ca,
            preshared_key=preshared_key,
            access_config=access_config,
            hmac_algorithm=hmac_algorithm,
            enc_algorithm=enc_algorithm,
            ssl_min_proto_version=ssl_min_proto_version,
            conn_timeout=conn_timeout,
            monitor_keepalive_period=monitor_keepalive_period,
            monitor_failure_retry_period=monitor_failure_retry_period,
            certificate=certificate,
            source_ip=source_ip,
            upload_option=upload_option,
            upload_interval=upload_interval,
            upload_day=upload_day,
            upload_time=upload_time,
            reliable=reliable,
            priority=priority,
            max_log_rate=max_log_rate,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/fortianalyzer2/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log.fortianalyzer2/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





