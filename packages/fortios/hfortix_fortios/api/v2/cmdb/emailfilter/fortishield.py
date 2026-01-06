"""
FortiOS CMDB - Emailfilter fortishield

Configuration endpoint for managing cmdb emailfilter/fortishield objects.

API Endpoints:
    GET    /cmdb/emailfilter/fortishield
    POST   /cmdb/emailfilter/fortishield
    PUT    /cmdb/emailfilter/fortishield/{identifier}
    DELETE /cmdb/emailfilter/fortishield/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.emailfilter_fortishield.get()

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


class Fortishield(MetadataMixin):
    """Fortishield Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fortishield"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortishield endpoint."""
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
        Retrieve emailfilter/fortishield configuration.

        Configure FortiGuard - AntiSpam.

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
            >>> # Get all emailfilter/fortishield objects
            >>> result = fgt.api.cmdb.emailfilter_fortishield.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.emailfilter_fortishield.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.emailfilter_fortishield.get(action="schema")

        See Also:
            - post(): Create new emailfilter/fortishield object
            - put(): Update existing emailfilter/fortishield object
            - delete(): Remove emailfilter/fortishield object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/emailfilter/fortishield/{name}"
        else:
            endpoint = "/emailfilter/fortishield"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        spam_submit_srv: str | None = None,
        spam_submit_force: str | None = None,
        spam_submit_txt2htm: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing emailfilter/fortishield object.

        Configure FortiGuard - AntiSpam.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            spam_submit_srv: Hostname of the spam submission server.
            spam_submit_force: Enable/disable force insertion of a new mime entity for the submission text.
            spam_submit_txt2htm: Enable/disable conversion of text email to HTML email.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.emailfilter_fortishield.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.emailfilter_fortishield.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            spam_submit_srv=spam_submit_srv,
            spam_submit_force=spam_submit_force,
            spam_submit_txt2htm=spam_submit_txt2htm,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fortishield import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/emailfilter/fortishield",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/emailfilter/fortishield/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





