"""
FortiOS CMDB - Log eventfilter

Configuration endpoint for managing cmdb log/eventfilter objects.

API Endpoints:
    GET    /cmdb/log/eventfilter
    POST   /cmdb/log/eventfilter
    PUT    /cmdb/log/eventfilter/{identifier}
    DELETE /cmdb/log/eventfilter/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_eventfilter.get()

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


class Eventfilter(MetadataMixin):
    """Eventfilter Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "eventfilter"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Eventfilter endpoint."""
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
        Retrieve log/eventfilter configuration.

        Configure log event filters.

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
            >>> # Get all log/eventfilter objects
            >>> result = fgt.api.cmdb.log_eventfilter.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_eventfilter.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_eventfilter.get(action="schema")

        See Also:
            - post(): Create new log/eventfilter object
            - put(): Update existing log/eventfilter object
            - delete(): Remove log/eventfilter object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log/eventfilter/{name}"
        else:
            endpoint = "/log/eventfilter"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        event: str | None = None,
        system: str | None = None,
        vpn: str | None = None,
        user: str | None = None,
        router: str | None = None,
        wireless_activity: str | None = None,
        wan_opt: str | None = None,
        endpoint: str | None = None,
        ha: str | None = None,
        security_rating: str | None = None,
        fortiextender: str | None = None,
        connector: str | None = None,
        sdwan: str | None = None,
        cifs: str | None = None,
        switch_controller: str | None = None,
        rest_api: str | None = None,
        web_svc: str | None = None,
        webproxy: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/eventfilter object.

        Configure log event filters.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            event: Enable/disable event logging.
            system: Enable/disable system event logging.
            vpn: Enable/disable VPN event logging.
            user: Enable/disable user authentication event logging.
            router: Enable/disable router event logging.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_eventfilter.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_eventfilter.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            event=event,
            system=system,
            vpn=vpn,
            user=user,
            router=router,
            wireless_activity=wireless_activity,
            wan_opt=wan_opt,
            endpoint=endpoint,
            ha=ha,
            security_rating=security_rating,
            fortiextender=fortiextender,
            connector=connector,
            sdwan=sdwan,
            cifs=cifs,
            switch_controller=switch_controller,
            rest_api=rest_api,
            web_svc=web_svc,
            webproxy=webproxy,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.eventfilter import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/eventfilter",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log/eventfilter/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





