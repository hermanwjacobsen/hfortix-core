"""
FortiOS CMDB - Firewall ssl setting

Configuration endpoint for managing cmdb firewall/ssl/setting objects.

API Endpoints:
    GET    /cmdb/firewall/ssl/setting
    POST   /cmdb/firewall/ssl/setting
    PUT    /cmdb/firewall/ssl/setting/{identifier}
    DELETE /cmdb/firewall/ssl/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_ssl_setting.get()

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
        Retrieve firewall/ssl/setting configuration.

        SSL proxy settings.

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
            >>> # Get all firewall/ssl/setting objects
            >>> result = fgt.api.cmdb.firewall_ssl_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_ssl_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_ssl_setting.get(action="schema")

        See Also:
            - post(): Create new firewall/ssl/setting object
            - put(): Update existing firewall/ssl/setting object
            - delete(): Remove firewall/ssl/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/firewall.ssl/setting/{name}"
        else:
            endpoint = "/firewall.ssl/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        proxy_connect_timeout: int | None = None,
        ssl_dh_bits: str | None = None,
        ssl_send_empty_frags: str | None = None,
        no_matching_cipher_action: str | None = None,
        cert_manager_cache_timeout: int | None = None,
        resigned_short_lived_certificate: str | None = None,
        cert_cache_capacity: int | None = None,
        cert_cache_timeout: int | None = None,
        session_cache_capacity: int | None = None,
        session_cache_timeout: int | None = None,
        abbreviate_handshake: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/ssl/setting object.

        SSL proxy settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            proxy_connect_timeout: Time limit to make an internal connection to the appropriate proxy process (1 - 60 sec, default = 30).
            ssl_dh_bits: Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).
            ssl_send_empty_frags: Enable/disable sending empty fragments to avoid attack on CBC IV (for SSL 3.0 and TLS 1.0 only).
            no_matching_cipher_action: Bypass or drop the connection when no matching cipher is found.
            cert_manager_cache_timeout: Time limit for certificate manager to keep FortiGate re-signed server certificate (24 - 720 hours, default = 72).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_ssl_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_ssl_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            proxy_connect_timeout=proxy_connect_timeout,
            ssl_dh_bits=ssl_dh_bits,
            ssl_send_empty_frags=ssl_send_empty_frags,
            no_matching_cipher_action=no_matching_cipher_action,
            cert_manager_cache_timeout=cert_manager_cache_timeout,
            resigned_short_lived_certificate=resigned_short_lived_certificate,
            cert_cache_capacity=cert_cache_capacity,
            cert_cache_timeout=cert_cache_timeout,
            session_cache_capacity=session_cache_capacity,
            session_cache_timeout=session_cache_timeout,
            abbreviate_handshake=abbreviate_handshake,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/ssl/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/firewall.ssl/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





