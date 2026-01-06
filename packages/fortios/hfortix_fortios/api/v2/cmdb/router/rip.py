"""
FortiOS CMDB - Router rip

Configuration endpoint for managing cmdb router/rip objects.

API Endpoints:
    GET    /cmdb/router/rip
    POST   /cmdb/router/rip
    PUT    /cmdb/router/rip/{identifier}
    DELETE /cmdb/router/rip/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_rip.get()

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


class Rip(MetadataMixin):
    """Rip Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "rip"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Rip endpoint."""
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
        Retrieve router/rip configuration.

        Configure RIP.

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
            >>> # Get all router/rip objects
            >>> result = fgt.api.cmdb.router_rip.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_rip.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_rip.get(action="schema")

        See Also:
            - post(): Create new router/rip object
            - put(): Update existing router/rip object
            - delete(): Remove router/rip object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/rip/{name}"
        else:
            endpoint = "/router/rip"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        default_information_originate: str | None = None,
        default_metric: int | None = None,
        max_out_metric: int | None = None,
        distance: str | list | None = None,
        distribute_list: str | list | None = None,
        neighbor: str | list | None = None,
        network: str | list | None = None,
        offset_list: str | list | None = None,
        passive_interface: str | list | None = None,
        redistribute: str | list | None = None,
        update_timer: int | None = None,
        timeout_timer: int | None = None,
        garbage_timer: int | None = None,
        version: str | None = None,
        interface: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/rip object.

        Configure RIP.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            default_information_originate: Enable/disable generation of default route.
            default_metric: Default metric.
            max_out_metric: Maximum metric allowed to output(0 means 'not set').
            distance: Distance.
            distribute_list: Distribute list.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_rip.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_rip.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            default_information_originate=default_information_originate,
            default_metric=default_metric,
            max_out_metric=max_out_metric,
            distance=distance,
            distribute_list=distribute_list,
            neighbor=neighbor,
            network=network,
            offset_list=offset_list,
            passive_interface=passive_interface,
            redistribute=redistribute,
            update_timer=update_timer,
            timeout_timer=timeout_timer,
            garbage_timer=garbage_timer,
            version=version,
            interface=interface,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.rip import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/rip",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/rip/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





