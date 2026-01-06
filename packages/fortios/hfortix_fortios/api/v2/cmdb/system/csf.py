"""
FortiOS CMDB - System csf

Configuration endpoint for managing cmdb system/csf objects.

API Endpoints:
    GET    /cmdb/system/csf
    POST   /cmdb/system/csf
    PUT    /cmdb/system/csf/{identifier}
    DELETE /cmdb/system/csf/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_csf.get()

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


class Csf(MetadataMixin):
    """Csf Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "csf"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Csf endpoint."""
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
        Retrieve system/csf configuration.

        Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.

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
            >>> # Get all system/csf objects
            >>> result = fgt.api.cmdb.system_csf.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_csf.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_csf.get(action="schema")

        See Also:
            - post(): Create new system/csf object
            - put(): Update existing system/csf object
            - delete(): Remove system/csf object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/csf/{name}"
        else:
            endpoint = "/system/csf"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        uid: str | None = None,
        upstream: str | None = None,
        source_ip: str | None = None,
        upstream_interface_select_method: str | None = None,
        upstream_interface: str | None = None,
        upstream_port: int | None = None,
        group_name: str | None = None,
        group_password: Any | None = None,
        accept_auth_by_cert: str | None = None,
        log_unification: str | None = None,
        authorization_request_type: str | None = None,
        certificate: str | None = None,
        fabric_workers: int | None = None,
        downstream_access: str | None = None,
        legacy_authentication: str | None = None,
        downstream_accprofile: str | None = None,
        configuration_sync: str | None = None,
        fabric_object_unification: str | None = None,
        saml_configuration_sync: str | None = None,
        trusted_list: str | list | None = None,
        fabric_connector: str | list | None = None,
        forticloud_account_enforcement: str | None = None,
        file_mgmt: str | None = None,
        file_quota: int | None = None,
        file_quota_warning: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/csf object.

        Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable Security Fabric.
            uid: Unique ID of the current CSF node
            upstream: IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric.
            source_ip: Source IP address for communication with the upstream FortiGate.
            upstream_interface_select_method: Specify how to select outgoing interface to reach server.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_csf.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_csf.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            uid=uid,
            upstream=upstream,
            source_ip=source_ip,
            upstream_interface_select_method=upstream_interface_select_method,
            upstream_interface=upstream_interface,
            upstream_port=upstream_port,
            group_name=group_name,
            group_password=group_password,
            accept_auth_by_cert=accept_auth_by_cert,
            log_unification=log_unification,
            authorization_request_type=authorization_request_type,
            certificate=certificate,
            fabric_workers=fabric_workers,
            downstream_access=downstream_access,
            legacy_authentication=legacy_authentication,
            downstream_accprofile=downstream_accprofile,
            configuration_sync=configuration_sync,
            fabric_object_unification=fabric_object_unification,
            saml_configuration_sync=saml_configuration_sync,
            trusted_list=trusted_list,
            fabric_connector=fabric_connector,
            forticloud_account_enforcement=forticloud_account_enforcement,
            file_mgmt=file_mgmt,
            file_quota=file_quota,
            file_quota_warning=file_quota_warning,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.csf import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/csf",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/csf/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





