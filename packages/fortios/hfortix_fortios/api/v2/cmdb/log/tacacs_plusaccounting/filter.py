"""
FortiOS CMDB - Log tacacs_plusaccounting filter

Configuration endpoint for managing cmdb log/tacacs_plusaccounting/filter objects.

API Endpoints:
    GET    /cmdb/log/tacacs_plusaccounting/filter
    POST   /cmdb/log/tacacs_plusaccounting/filter
    PUT    /cmdb/log/tacacs_plusaccounting/filter/{identifier}
    DELETE /cmdb/log/tacacs_plusaccounting/filter/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_tacacs_plusaccounting_filter.get()

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


class Filter(MetadataMixin):
    """Filter Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "filter"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Filter endpoint."""
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
        Retrieve log/tacacs_plusaccounting/filter configuration.

        Settings for TACACS+ accounting events filter.

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
            >>> # Get all log/tacacs_plusaccounting/filter objects
            >>> result = fgt.api.cmdb.log_tacacs_plusaccounting_filter.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_tacacs_plusaccounting_filter.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_tacacs_plusaccounting_filter.get(action="schema")

        See Also:
            - post(): Create new log/tacacs_plusaccounting/filter object
            - put(): Update existing log/tacacs_plusaccounting/filter object
            - delete(): Remove log/tacacs_plusaccounting/filter object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log.tacacs+accounting/filter/{name}"
        else:
            endpoint = "/log.tacacs+accounting/filter"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        login_audit: str | None = None,
        config_change_audit: str | None = None,
        cli_cmd_audit: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/tacacs_plusaccounting/filter object.

        Settings for TACACS+ accounting events filter.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            login_audit: Enable/disable TACACS+ accounting for login events audit.
            config_change_audit: Enable/disable TACACS+ accounting for configuration change events audit.
            cli_cmd_audit: Enable/disable TACACS+ accounting for CLI commands audit.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_tacacs_plusaccounting_filter.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_tacacs_plusaccounting_filter.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            login_audit=login_audit,
            config_change_audit=config_change_audit,
            cli_cmd_audit=cli_cmd_audit,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.filter import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/tacacs_plusaccounting/filter",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log.tacacs+accounting/filter/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





