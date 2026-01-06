"""
FortiOS CMDB - Application name

Configuration endpoint for managing cmdb application/name objects.

📖 **Read-Only Reference Table**
   This endpoint provides read-only reference data (e.g., geography, timezone).
   - GET operations return all available data
   - POST/PUT/DELETE operations are not supported
   - Querying by identifier returns all items (filter is ignored)

API Endpoints:
    GET    /cmdb/application/name

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.application_name.get()

Important:
    - This is a **read-only** endpoint (reference data only)
    - Use **GET** to retrieve available options
    - Creation/modification/deletion not supported
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

# Import cache for readonly reference data
from hfortix_core.cache import readonly_cache


class Name(MetadataMixin):
    """Name Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "name"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Name endpoint."""
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
        Retrieve application/name configuration.

        Configure application signatures.

        Args:
            name: String identifier to retrieve specific object.
                If None, returns all objects.
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
            >>> # Get all application/name objects
            >>> result = fgt.api.cmdb.application_name.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific application/name by name
            >>> result = fgt.api.cmdb.application_name.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.application_name.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.application_name.get(action="schema")

        See Also:
            - post(): Create new application/name object
            - put(): Update existing application/name object
            - delete(): Remove application/name object
            - exists(): Check if object exists
        """
        # Check cache for readonly reference data (24hr TTL)
        cache_key = f"cmdb/application/name"
        
        # Only use cache for full list queries (no identifier, no filters)
        is_list_query = name is None and not payload_dict and not kwargs
        
        if is_list_query:
            cached_data = readonly_cache.get(cache_key)
            if cached_data is not None:
                # Return cached data
                if raw_json:
                    return cached_data
                return cached_data
        
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/application/name/" + str(name)
        else:
            endpoint = "/application/name"
        
        params.update(kwargs)
        
        # Fetch data and cache if this is a list query
        response = self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )
        
        # Cache the response for list queries
        if is_list_query:
            if isinstance(response, dict):
                readonly_cache.set(cache_key, response)
            # For async responses, we can't cache easily without awaiting
            # User will benefit from cache on subsequent sync calls
        
        return response


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        category: int | None = None,
        popularity: int | None = None,
        risk: int | None = None,
        weight: int | None = None,
        protocol: str | None = None,
        technology: str | None = None,
        behavior: str | None = None,
        vendor: str | None = None,
        parameters: str | list | None = None,
        metadata: str | list | None = None,
        status: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing application/name object.

        Configure application signatures.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Application name.
            id: Application ID.
            category: Application category ID.
            popularity: Application popularity.
            risk: Application risk.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.application_name.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.application_name.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            id=id,
            category=category,
            popularity=popularity,
            risk=risk,
            weight=weight,
            protocol=protocol,
            technology=technology,
            behavior=behavior,
            vendor=vendor,
            parameters=parameters,
            metadata=metadata,
            status=status,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.name import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/application/name",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/application/name/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        category: int | None = None,
        popularity: int | None = None,
        risk: int | None = None,
        weight: int | None = None,
        protocol: str | None = None,
        technology: str | None = None,
        behavior: str | None = None,
        vendor: str | None = None,
        parameters: str | list | None = None,
        metadata: str | list | None = None,
        status: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new application/name object.

        Configure application signatures.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Application name.
            id: Application ID.
            category: Application category ID.
            popularity: Application popularity.
            risk: Application risk.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.application_name.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Name.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.application_name.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Name.required_fields()) }}
            
            Use Name.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            id=id,
            category=category,
            popularity=popularity,
            risk=risk,
            weight=weight,
            protocol=protocol,
            technology=technology,
            behavior=behavior,
            vendor=vendor,
            parameters=parameters,
            metadata=metadata,
            status=status,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.name import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/application/name",
            )

        endpoint = "/application/name"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete application/name object.

        Configure application signatures.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.application_name.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/application/name/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if application/name object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.application_name.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.application_name.exists(name=1):
            ...     fgt.api.cmdb.application_name.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # For readonly endpoints, check by fetching all items and scanning
        # This is necessary because readonly endpoints don't support direct ID queries
        try:
            response = self.get(vdom=vdom, raw_json=True)
            
            if isinstance(response, dict):
                # Synchronous response
                if not is_success(response):
                    return False
                
                results = response.get("results", [])
                if not isinstance(results, list):
                    return False
                
                # Scan for matching identifier
                return any(
                    item.get("name") == name
                    for item in results
                )
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    if not is_success(r):
                        return False
                    
                    results = r.get("results", [])
                    if not isinstance(results, list):
                        return False
                    
                    return any(
                        item.get("name") == name
                        for item in results
                    )
                return _check()
        except Exception:
            # Error fetching list - return False
            return False


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update application/name object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.application_name.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.application_name.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        if payload_dict is None:
            payload_dict = {}
        
        mkey_value = payload_dict.get("name")
        if not mkey_value:
            raise ValueError("name is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


