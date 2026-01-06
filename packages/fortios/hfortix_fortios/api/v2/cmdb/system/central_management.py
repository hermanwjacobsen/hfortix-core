"""
FortiOS CMDB - System central_management

Configuration endpoint for managing cmdb system/central_management objects.

API Endpoints:
    GET    /cmdb/system/central_management
    POST   /cmdb/system/central_management
    PUT    /cmdb/system/central_management/{identifier}
    DELETE /cmdb/system/central_management/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_central_management.get()

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


class CentralManagement(MetadataMixin):
    """CentralManagement Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "central_management"

    def __init__(self, client: "IHTTPClient"):
        """Initialize CentralManagement endpoint."""
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
        Retrieve system/central_management configuration.

        Configure central management.

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
            >>> # Get all system/central_management objects
            >>> result = fgt.api.cmdb.system_central_management.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_central_management.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_central_management.get(action="schema")

        See Also:
            - post(): Create new system/central_management object
            - put(): Update existing system/central_management object
            - delete(): Remove system/central_management object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/central-management/{name}"
        else:
            endpoint = "/system/central-management"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        mode: str | None = None,
        type: str | None = None,
        fortigate_cloud_sso_default_profile: str | None = None,
        schedule_config_restore: str | None = None,
        schedule_script_restore: str | None = None,
        allow_push_configuration: str | None = None,
        allow_push_firmware: str | None = None,
        allow_remote_firmware_upgrade: str | None = None,
        allow_monitor: str | None = None,
        serial_number: str | None = None,
        fmg: str | None = None,
        fmg_source_ip: str | None = None,
        fmg_source_ip6: str | None = None,
        local_cert: str | None = None,
        ca_cert: str | None = None,
        server_list: str | list | None = None,
        fmg_update_port: str | None = None,
        fmg_update_http_header: str | None = None,
        include_default_servers: str | None = None,
        enc_algorithm: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/central_management object.

        Configure central management.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            mode: Central management mode.
            type: Central management type.
            fortigate_cloud_sso_default_profile: Override access profile. Permission is set to read-only without a FortiGate Cloud Central Management license.
            schedule_config_restore: Enable/disable allowing the central management server to restore the configuration of this FortiGate.
            schedule_script_restore: Enable/disable allowing the central management server to restore the scripts stored on this FortiGate.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_central_management.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_central_management.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            mode=mode,
            type=type,
            fortigate_cloud_sso_default_profile=fortigate_cloud_sso_default_profile,
            schedule_config_restore=schedule_config_restore,
            schedule_script_restore=schedule_script_restore,
            allow_push_configuration=allow_push_configuration,
            allow_push_firmware=allow_push_firmware,
            allow_remote_firmware_upgrade=allow_remote_firmware_upgrade,
            allow_monitor=allow_monitor,
            serial_number=serial_number,
            fmg=fmg,
            fmg_source_ip=fmg_source_ip,
            fmg_source_ip6=fmg_source_ip6,
            local_cert=local_cert,
            ca_cert=ca_cert,
            server_list=server_list,
            fmg_update_port=fmg_update_port,
            fmg_update_http_header=fmg_update_http_header,
            include_default_servers=include_default_servers,
            enc_algorithm=enc_algorithm,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.central_management import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/central_management",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/central-management/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





