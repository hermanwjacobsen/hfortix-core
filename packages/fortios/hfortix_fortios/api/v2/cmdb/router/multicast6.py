"""
FortiOS CMDB - Router multicast6

Configuration endpoint for managing cmdb router/multicast6 objects.

API Endpoints:
    GET    /cmdb/router/multicast6
    POST   /cmdb/router/multicast6
    PUT    /cmdb/router/multicast6/{identifier}
    DELETE /cmdb/router/multicast6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_multicast6.get()

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


class Multicast6(MetadataMixin):
    """Multicast6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "multicast6"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Multicast6 endpoint."""
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
        Retrieve router/multicast6 configuration.

        Configure IPv6 multicast.

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
            >>> # Get all router/multicast6 objects
            >>> result = fgt.api.cmdb.router_multicast6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_multicast6.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_multicast6.get(action="schema")

        See Also:
            - post(): Create new router/multicast6 object
            - put(): Update existing router/multicast6 object
            - delete(): Remove router/multicast6 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/multicast6/{name}"
        else:
            endpoint = "/router/multicast6"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        multicast_routing: str | None = None,
        multicast_pmtu: str | None = None,
        interface: str | list | None = None,
        pim_sm_global: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/multicast6 object.

        Configure IPv6 multicast.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            multicast_routing: Enable/disable IPv6 multicast routing.
            multicast_pmtu: Enable/disable PMTU for IPv6 multicast.
            interface: Protocol Independent Multicast (PIM) interfaces.
            pim_sm_global: PIM sparse-mode global settings.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_multicast6.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_multicast6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            multicast_routing=multicast_routing,
            multicast_pmtu=multicast_pmtu,
            interface=interface,
            pim_sm_global=pim_sm_global,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.multicast6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/multicast6",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/multicast6/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





