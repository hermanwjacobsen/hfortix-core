"""
FortiOS CMDB - Wireless_controller inter_controller

Configuration endpoint for managing cmdb wireless_controller/inter_controller objects.

API Endpoints:
    GET    /cmdb/wireless_controller/inter_controller
    POST   /cmdb/wireless_controller/inter_controller
    PUT    /cmdb/wireless_controller/inter_controller/{identifier}
    DELETE /cmdb/wireless_controller/inter_controller/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_inter_controller.get()

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


class InterController(MetadataMixin):
    """InterController Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "inter_controller"

    def __init__(self, client: "IHTTPClient"):
        """Initialize InterController endpoint."""
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
        Retrieve wireless_controller/inter_controller configuration.

        Configure inter wireless controller operation.

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
            >>> # Get all wireless_controller/inter_controller objects
            >>> result = fgt.api.cmdb.wireless_controller_inter_controller.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_inter_controller.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_inter_controller.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/inter_controller object
            - put(): Update existing wireless_controller/inter_controller object
            - delete(): Remove wireless_controller/inter_controller object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wireless-controller/inter-controller/{name}"
        else:
            endpoint = "/wireless-controller/inter-controller"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        inter_controller_mode: str | None = None,
        l3_roaming: str | None = None,
        inter_controller_key: Any | None = None,
        inter_controller_pri: str | None = None,
        fast_failover_max: int | None = None,
        fast_failover_wait: int | None = None,
        inter_controller_peer: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/inter_controller object.

        Configure inter wireless controller operation.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            inter_controller_mode: Configure inter-controller mode (disable, l2-roaming, 1+1, default = disable).
            l3_roaming: Enable/disable layer 3 roaming (default = disable).
            inter_controller_key: Secret key for inter-controller communications.
            inter_controller_pri: Configure inter-controller's priority (primary or secondary, default = primary).
            fast_failover_max: Maximum number of retransmissions for fast failover HA messages between peer wireless controllers (3 - 64, default = 10).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_inter_controller.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_inter_controller.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            inter_controller_mode=inter_controller_mode,
            l3_roaming=l3_roaming,
            inter_controller_key=inter_controller_key,
            inter_controller_pri=inter_controller_pri,
            fast_failover_max=fast_failover_max,
            fast_failover_wait=fast_failover_wait,
            inter_controller_peer=inter_controller_peer,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.inter_controller import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/inter_controller",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/wireless-controller/inter-controller/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





