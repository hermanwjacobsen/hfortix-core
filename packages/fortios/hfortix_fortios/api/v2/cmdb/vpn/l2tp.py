"""
FortiOS CMDB - Vpn l2tp

Configuration endpoint for managing cmdb vpn/l2tp objects.

API Endpoints:
    GET    /cmdb/vpn/l2tp
    POST   /cmdb/vpn/l2tp
    PUT    /cmdb/vpn/l2tp/{identifier}
    DELETE /cmdb/vpn/l2tp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_l2tp.get()

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


class L2tp(MetadataMixin):
    """L2tp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "l2tp"

    def __init__(self, client: "IHTTPClient"):
        """Initialize L2tp endpoint."""
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
        Retrieve vpn/l2tp configuration.

        Configure L2TP.

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
            >>> # Get all vpn/l2tp objects
            >>> result = fgt.api.cmdb.vpn_l2tp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_l2tp.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_l2tp.get(action="schema")

        See Also:
            - post(): Create new vpn/l2tp object
            - put(): Update existing vpn/l2tp object
            - delete(): Remove vpn/l2tp object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/vpn/l2tp/{name}"
        else:
            endpoint = "/vpn/l2tp"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        eip: str | None = None,
        sip: str | None = None,
        usrgrp: str | None = None,
        enforce_ipsec: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        hello_interval: int | None = None,
        compress: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/l2tp object.

        Configure L2TP.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable FortiGate as a L2TP gateway.
            eip: End IP.
            sip: Start IP.
            usrgrp: User group.
            enforce_ipsec: Enable/disable IPsec enforcement.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_l2tp.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_l2tp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            eip=eip,
            sip=sip,
            usrgrp=usrgrp,
            enforce_ipsec=enforce_ipsec,
            lcp_echo_interval=lcp_echo_interval,
            lcp_max_echo_fails=lcp_max_echo_fails,
            hello_interval=hello_interval,
            compress=compress,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.l2tp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/l2tp",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/vpn/l2tp/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





