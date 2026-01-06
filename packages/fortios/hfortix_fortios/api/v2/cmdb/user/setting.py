"""
FortiOS CMDB - User setting

Configuration endpoint for managing cmdb user/setting objects.

API Endpoints:
    GET    /cmdb/user/setting
    POST   /cmdb/user/setting
    PUT    /cmdb/user/setting/{identifier}
    DELETE /cmdb/user/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user_setting.get()

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
        Retrieve user/setting configuration.

        Configure user authentication setting.

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
            >>> # Get all user/setting objects
            >>> result = fgt.api.cmdb.user_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.user_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.user_setting.get(action="schema")

        See Also:
            - post(): Create new user/setting object
            - put(): Update existing user/setting object
            - delete(): Remove user/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/user/setting/{name}"
        else:
            endpoint = "/user/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        auth_type: str | list | None = None,
        auth_cert: str | None = None,
        auth_ca_cert: str | None = None,
        auth_secure_http: str | None = None,
        auth_http_basic: str | None = None,
        auth_ssl_allow_renegotiation: str | None = None,
        auth_src_mac: str | None = None,
        auth_on_demand: str | None = None,
        auth_timeout: int | None = None,
        auth_timeout_type: str | None = None,
        auth_portal_timeout: int | None = None,
        radius_ses_timeout_act: str | None = None,
        auth_blackout_time: int | None = None,
        auth_invalid_max: int | None = None,
        auth_lockout_threshold: int | None = None,
        auth_lockout_duration: int | None = None,
        per_policy_disclaimer: str | None = None,
        auth_ports: str | list | None = None,
        auth_ssl_min_proto_version: str | None = None,
        auth_ssl_max_proto_version: str | None = None,
        auth_ssl_sigalgs: str | None = None,
        default_user_password_policy: str | None = None,
        cors: str | None = None,
        cors_allowed_origins: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing user/setting object.

        Configure user authentication setting.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            auth_type: Supported firewall policy authentication protocols/methods.
            auth_cert: HTTPS server certificate for policy authentication.
            auth_ca_cert: HTTPS CA certificate for policy authentication.
            auth_secure_http: Enable/disable redirecting HTTP user authentication to more secure HTTPS.
            auth_http_basic: Enable/disable use of HTTP basic authentication for identity-based firewall policies.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.user_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.user_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            auth_type=auth_type,
            auth_cert=auth_cert,
            auth_ca_cert=auth_ca_cert,
            auth_secure_http=auth_secure_http,
            auth_http_basic=auth_http_basic,
            auth_ssl_allow_renegotiation=auth_ssl_allow_renegotiation,
            auth_src_mac=auth_src_mac,
            auth_on_demand=auth_on_demand,
            auth_timeout=auth_timeout,
            auth_timeout_type=auth_timeout_type,
            auth_portal_timeout=auth_portal_timeout,
            radius_ses_timeout_act=radius_ses_timeout_act,
            auth_blackout_time=auth_blackout_time,
            auth_invalid_max=auth_invalid_max,
            auth_lockout_threshold=auth_lockout_threshold,
            auth_lockout_duration=auth_lockout_duration,
            per_policy_disclaimer=per_policy_disclaimer,
            auth_ports=auth_ports,
            auth_ssl_min_proto_version=auth_ssl_min_proto_version,
            auth_ssl_max_proto_version=auth_ssl_max_proto_version,
            auth_ssl_sigalgs=auth_ssl_sigalgs,
            default_user_password_policy=default_user_password_policy,
            cors=cors,
            cors_allowed_origins=cors_allowed_origins,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/user/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





