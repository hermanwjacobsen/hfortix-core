"""
FortiOS CMDB - Antivirus quarantine

Configuration endpoint for managing cmdb antivirus/quarantine objects.

API Endpoints:
    GET    /cmdb/antivirus/quarantine
    POST   /cmdb/antivirus/quarantine
    PUT    /cmdb/antivirus/quarantine/{identifier}
    DELETE /cmdb/antivirus/quarantine/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.antivirus_quarantine.get()

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


class Quarantine(MetadataMixin):
    """Quarantine Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "quarantine"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Quarantine endpoint."""
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
        Retrieve antivirus/quarantine configuration.

        Configure quarantine options.

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
            >>> # Get all antivirus/quarantine objects
            >>> result = fgt.api.cmdb.antivirus_quarantine.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.antivirus_quarantine.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.antivirus_quarantine.get(action="schema")

        See Also:
            - post(): Create new antivirus/quarantine object
            - put(): Update existing antivirus/quarantine object
            - delete(): Remove antivirus/quarantine object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/antivirus/quarantine/{name}"
        else:
            endpoint = "/antivirus/quarantine"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        agelimit: int | None = None,
        maxfilesize: int | None = None,
        quarantine_quota: int | None = None,
        drop_infected: str | list | None = None,
        store_infected: str | list | None = None,
        drop_machine_learning: str | list | None = None,
        store_machine_learning: str | list | None = None,
        lowspace: str | None = None,
        destination: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing antivirus/quarantine object.

        Configure quarantine options.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            agelimit: Age limit for quarantined files (0 - 479 hours, 0 means forever).
            maxfilesize: Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited).
            quarantine_quota: The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbytes, 0 means unlimited and depends on disk space).
            drop_infected: Do not quarantine infected files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.
            store_infected: Quarantine infected files found in sessions using the selected protocols.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.antivirus_quarantine.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.antivirus_quarantine.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            agelimit=agelimit,
            maxfilesize=maxfilesize,
            quarantine_quota=quarantine_quota,
            drop_infected=drop_infected,
            store_infected=store_infected,
            drop_machine_learning=drop_machine_learning,
            store_machine_learning=store_machine_learning,
            lowspace=lowspace,
            destination=destination,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.quarantine import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/antivirus/quarantine",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/antivirus/quarantine/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





