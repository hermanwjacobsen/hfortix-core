"""
FortiOS CMDB - Firewall auth_portal

Configuration endpoint for managing cmdb firewall/auth_portal objects.

API Endpoints:
    GET    /cmdb/firewall/auth_portal
    POST   /cmdb/firewall/auth_portal
    PUT    /cmdb/firewall/auth_portal/{identifier}
    DELETE /cmdb/firewall/auth_portal/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_auth_portal.get()

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


class AuthPortal(MetadataMixin):
    """AuthPortal Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "auth_portal"

    def __init__(self, client: "IHTTPClient"):
        """Initialize AuthPortal endpoint."""
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
        Retrieve firewall/auth_portal configuration.

        Configure firewall authentication portals.

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
            >>> # Get all firewall/auth_portal objects
            >>> result = fgt.api.cmdb.firewall_auth_portal.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_auth_portal.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_auth_portal.get(action="schema")

        See Also:
            - post(): Create new firewall/auth_portal object
            - put(): Update existing firewall/auth_portal object
            - delete(): Remove firewall/auth_portal object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/firewall/auth-portal/{name}"
        else:
            endpoint = "/firewall/auth-portal"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        groups: str | list | None = None,
        portal_addr: str | None = None,
        portal_addr6: str | None = None,
        identity_based_route: str | None = None,
        proxy_auth: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/auth_portal object.

        Configure firewall authentication portals.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            groups: Firewall user groups permitted to authenticate through this portal. Separate group names with spaces.
            portal_addr: Address (or FQDN) of the authentication portal.
            portal_addr6: IPv6 address (or FQDN) of authentication portal.
            identity_based_route: Name of the identity-based route that applies to this portal.
            proxy_auth: Enable/disable authentication by proxy daemon (default = disable).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_auth_portal.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_auth_portal.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            groups=groups,
            portal_addr=portal_addr,
            portal_addr6=portal_addr6,
            identity_based_route=identity_based_route,
            proxy_auth=proxy_auth,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.auth_portal import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/auth_portal",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/firewall/auth-portal/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





