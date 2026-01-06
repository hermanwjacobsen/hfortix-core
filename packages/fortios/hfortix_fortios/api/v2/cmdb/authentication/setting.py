"""
FortiOS CMDB - Authentication setting

Configuration endpoint for managing cmdb authentication/setting objects.

API Endpoints:
    GET    /cmdb/authentication/setting
    POST   /cmdb/authentication/setting
    PUT    /cmdb/authentication/setting/{identifier}
    DELETE /cmdb/authentication/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.authentication_setting.get()

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
        Retrieve authentication/setting configuration.

        Configure authentication setting.

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
            >>> # Get all authentication/setting objects
            >>> result = fgt.api.cmdb.authentication_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.authentication_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.authentication_setting.get(action="schema")

        See Also:
            - post(): Create new authentication/setting object
            - put(): Update existing authentication/setting object
            - delete(): Remove authentication/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/authentication/setting/{name}"
        else:
            endpoint = "/authentication/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        active_auth_scheme: str | None = None,
        sso_auth_scheme: str | None = None,
        update_time: str | None = None,
        persistent_cookie: str | None = None,
        ip_auth_cookie: str | None = None,
        cookie_max_age: int | None = None,
        cookie_refresh_div: int | None = None,
        captive_portal_type: str | None = None,
        captive_portal_ip: str | None = None,
        captive_portal_ip6: str | None = None,
        captive_portal: str | None = None,
        captive_portal6: str | None = None,
        cert_auth: str | None = None,
        cert_captive_portal: str | None = None,
        cert_captive_portal_ip: str | None = None,
        cert_captive_portal_port: int | None = None,
        captive_portal_port: int | None = None,
        auth_https: str | None = None,
        captive_portal_ssl_port: int | None = None,
        user_cert_ca: str | list | None = None,
        dev_range: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing authentication/setting object.

        Configure authentication setting.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            active_auth_scheme: Active authentication method (scheme name).
            sso_auth_scheme: Single-Sign-On authentication method (scheme name).
            update_time: Time of the last update.
            persistent_cookie: Enable/disable persistent cookie on web portal authentication (default = enable).
            ip_auth_cookie: Enable/disable persistent cookie on IP based web portal authentication (default = disable).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.authentication_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.authentication_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            active_auth_scheme=active_auth_scheme,
            sso_auth_scheme=sso_auth_scheme,
            update_time=update_time,
            persistent_cookie=persistent_cookie,
            ip_auth_cookie=ip_auth_cookie,
            cookie_max_age=cookie_max_age,
            cookie_refresh_div=cookie_refresh_div,
            captive_portal_type=captive_portal_type,
            captive_portal_ip=captive_portal_ip,
            captive_portal_ip6=captive_portal_ip6,
            captive_portal=captive_portal,
            captive_portal6=captive_portal6,
            cert_auth=cert_auth,
            cert_captive_portal=cert_captive_portal,
            cert_captive_portal_ip=cert_captive_portal_ip,
            cert_captive_portal_port=cert_captive_portal_port,
            captive_portal_port=captive_portal_port,
            auth_https=auth_https,
            captive_portal_ssl_port=captive_portal_ssl_port,
            user_cert_ca=user_cert_ca,
            dev_range=dev_range,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/authentication/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/authentication/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





