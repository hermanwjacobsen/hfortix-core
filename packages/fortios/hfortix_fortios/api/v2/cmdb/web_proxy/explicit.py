"""
FortiOS CMDB - Web_proxy explicit

Configuration endpoint for managing cmdb web_proxy/explicit objects.

API Endpoints:
    GET    /cmdb/web_proxy/explicit
    POST   /cmdb/web_proxy/explicit
    PUT    /cmdb/web_proxy/explicit/{identifier}
    DELETE /cmdb/web_proxy/explicit/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy_explicit.get()

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


class Explicit(MetadataMixin):
    """Explicit Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "explicit"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Explicit endpoint."""
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
        Retrieve web_proxy/explicit configuration.

        Configure explicit Web proxy settings.

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
            >>> # Get all web_proxy/explicit objects
            >>> result = fgt.api.cmdb.web_proxy_explicit.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.web_proxy_explicit.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.web_proxy_explicit.get(action="schema")

        See Also:
            - post(): Create new web_proxy/explicit object
            - put(): Update existing web_proxy/explicit object
            - delete(): Remove web_proxy/explicit object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/web-proxy/explicit/{name}"
        else:
            endpoint = "/web-proxy/explicit"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        secure_web_proxy: str | None = None,
        ftp_over_http: str | None = None,
        socks: str | None = None,
        http_incoming_port: str | None = None,
        http_connection_mode: str | None = None,
        https_incoming_port: str | None = None,
        secure_web_proxy_cert: str | list | None = None,
        client_cert: str | None = None,
        user_agent_detect: str | None = None,
        empty_cert_action: str | None = None,
        ssl_dh_bits: str | None = None,
        ftp_incoming_port: str | None = None,
        socks_incoming_port: str | None = None,
        incoming_ip: str | None = None,
        outgoing_ip: str | list | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        ipv6_status: str | None = None,
        incoming_ip6: str | None = None,
        outgoing_ip6: str | list | None = None,
        strict_guest: str | None = None,
        pref_dns_result: str | None = None,
        unknown_http_version: str | None = None,
        realm: str | None = None,
        sec_default_action: str | None = None,
        https_replacement_message: str | None = None,
        message_upon_server_error: str | None = None,
        pac_file_server_status: str | None = None,
        pac_file_url: str | None = None,
        pac_file_server_port: str | None = None,
        pac_file_through_https: str | None = None,
        pac_file_name: str | None = None,
        pac_file_data: str | None = None,
        pac_policy: str | list | None = None,
        ssl_algorithm: str | None = None,
        trace_auth_no_rsp: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing web_proxy/explicit object.

        Configure explicit Web proxy settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable the explicit Web proxy for HTTP and HTTPS session.
            secure_web_proxy: Enable/disable/require the secure web proxy for HTTP and HTTPS session.
            ftp_over_http: Enable to proxy FTP-over-HTTP sessions sent from a web browser.
            socks: Enable/disable the SOCKS proxy.
            http_incoming_port: Accept incoming HTTP requests on one or more ports (0 - 65535, default = 8080).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.web_proxy_explicit.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.web_proxy_explicit.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            secure_web_proxy=secure_web_proxy,
            ftp_over_http=ftp_over_http,
            socks=socks,
            http_incoming_port=http_incoming_port,
            http_connection_mode=http_connection_mode,
            https_incoming_port=https_incoming_port,
            secure_web_proxy_cert=secure_web_proxy_cert,
            client_cert=client_cert,
            user_agent_detect=user_agent_detect,
            empty_cert_action=empty_cert_action,
            ssl_dh_bits=ssl_dh_bits,
            ftp_incoming_port=ftp_incoming_port,
            socks_incoming_port=socks_incoming_port,
            incoming_ip=incoming_ip,
            outgoing_ip=outgoing_ip,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            ipv6_status=ipv6_status,
            incoming_ip6=incoming_ip6,
            outgoing_ip6=outgoing_ip6,
            strict_guest=strict_guest,
            pref_dns_result=pref_dns_result,
            unknown_http_version=unknown_http_version,
            realm=realm,
            sec_default_action=sec_default_action,
            https_replacement_message=https_replacement_message,
            message_upon_server_error=message_upon_server_error,
            pac_file_server_status=pac_file_server_status,
            pac_file_url=pac_file_url,
            pac_file_server_port=pac_file_server_port,
            pac_file_through_https=pac_file_through_https,
            pac_file_name=pac_file_name,
            pac_file_data=pac_file_data,
            pac_policy=pac_policy,
            ssl_algorithm=ssl_algorithm,
            trace_auth_no_rsp=trace_auth_no_rsp,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.explicit import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/web_proxy/explicit",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/web-proxy/explicit/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





