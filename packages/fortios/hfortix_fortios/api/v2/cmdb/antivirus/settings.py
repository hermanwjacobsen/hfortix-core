"""
FortiOS CMDB - Antivirus settings

Configuration endpoint for managing cmdb antivirus/settings objects.

API Endpoints:
    GET    /cmdb/antivirus/settings
    POST   /cmdb/antivirus/settings
    PUT    /cmdb/antivirus/settings/{identifier}
    DELETE /cmdb/antivirus/settings/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.antivirus_settings.get()

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


class Settings(MetadataMixin):
    """Settings Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "settings"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Settings endpoint."""
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
        Retrieve antivirus/settings configuration.

        Configure AntiVirus settings.

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
            >>> # Get all antivirus/settings objects
            >>> result = fgt.api.cmdb.antivirus_settings.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.antivirus_settings.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.antivirus_settings.get(action="schema")

        See Also:
            - post(): Create new antivirus/settings object
            - put(): Update existing antivirus/settings object
            - delete(): Remove antivirus/settings object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/antivirus/settings/{name}"
        else:
            endpoint = "/antivirus/settings"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        machine_learning_detection: str | None = None,
        use_extreme_db: str | None = None,
        grayware: str | None = None,
        override_timeout: int | None = None,
        cache_infected_result: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing antivirus/settings object.

        Configure AntiVirus settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            machine_learning_detection: Use machine learning based malware detection.
            use_extreme_db: Enable/disable the use of Extreme AVDB.
            grayware: Enable/disable grayware detection when an AntiVirus profile is applied to traffic.
            override_timeout: Override the large file scan timeout value in seconds (30 - 3600). Zero is the default value and is used to disable this command. When disabled, the daemon adjusts the large file scan timeout based on the file size.
            cache_infected_result: Enable/disable cache of infected scan results (default = enable).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.antivirus_settings.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.antivirus_settings.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            machine_learning_detection=machine_learning_detection,
            use_extreme_db=use_extreme_db,
            grayware=grayware,
            override_timeout=override_timeout,
            cache_infected_result=cache_infected_result,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.settings import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/antivirus/settings",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/antivirus/settings/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





