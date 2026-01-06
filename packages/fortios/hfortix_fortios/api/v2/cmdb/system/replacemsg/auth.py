"""
FortiOS CMDB - System replacemsg auth

Configuration endpoint for managing cmdb system/replacemsg/auth objects.

📖 **Read-Only Reference Table**
   This endpoint provides read-only reference data (e.g., geography, timezone).
   - GET operations return all available data
   - POST/PUT/DELETE operations are not supported
   - Querying by identifier returns all items (filter is ignored)

API Endpoints:
    GET    /cmdb/system/replacemsg/auth

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_replacemsg_auth.get()

Important:
    - This is a **read-only** endpoint (reference data only)
    - Use **GET** to retrieve available options
    - Creation/modification/deletion not supported
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, Literal
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


class Auth(MetadataMixin):
    """Auth Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "auth"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Auth endpoint."""
        self._client = client

    def get(
        self,
        msg_type: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/replacemsg/auth configuration.

        Replacement messages.

        Args:
            msg_type: String identifier to retrieve specific object.
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
            >>> # Get all system/replacemsg/auth objects
            >>> result = fgt.api.cmdb.system_replacemsg_auth.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/replacemsg/auth by msg-type
            >>> result = fgt.api.cmdb.system_replacemsg_auth.get(msg_type=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_replacemsg_auth.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_replacemsg_auth.get(action="schema")

        See Also:
            - post(): Create new system/replacemsg/auth object
            - put(): Update existing system/replacemsg/auth object
            - delete(): Remove system/replacemsg/auth object
            - exists(): Check if object exists
        """
        # Check cache for readonly reference data (24hr TTL)
        cache_key = f"cmdb/system/replacemsg/auth"
        
        # Only use cache for full list queries (no identifier, no filters)
        is_list_query = msg_type is None and not payload_dict and not kwargs
        
        if is_list_query:
            cached_data = readonly_cache.get(cache_key)
            if cached_data is not None:
                # Return cached data
                if raw_json:
                    return cached_data
                return cached_data
        
        params = payload_dict.copy() if payload_dict else {}
        
        if msg_type:
            endpoint = "/system.replacemsg/auth/" + str(msg_type)
        else:
            endpoint = "/system.replacemsg/auth"
        
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
        msg_type: str | None = None,
        buffer: str | None = None,
        header: Literal["none", "http", "8bit"] | None = None,
        format: Literal["none", "text", "html"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/replacemsg/auth object.

        Replacement messages.

        Args:
            payload_dict: Object data as dict. Must include msg-type (primary key).
            msg_type: Message type.
            buffer: Message string.
            header: Header flag.
            format: Format flag.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If msg-type is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_replacemsg_auth.put(
            ...     msg_type=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "msg-type": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_replacemsg_auth.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.auth import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/replacemsg/auth",
            )
        
        msg_type_value = payload_data.get("msg-type")
        if not msg_type_value:
            raise ValueError("msg-type is required for PUT")
        endpoint = "/system.replacemsg/auth/" + str(msg_type_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        msg_type: str | None = None,
        buffer: str | None = None,
        header: Literal["none", "http", "8bit"] | None = None,
        format: Literal["none", "text", "html"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/replacemsg/auth object.

        Replacement messages.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            msg_type: Message type.
            buffer: Message string.
            header: Header flag.
            format: Format flag.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned msg-type.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_replacemsg_auth.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created msg-type: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Auth.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_replacemsg_auth.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Auth.required_fields()) }}
            
            Use Auth.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.auth import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/replacemsg/auth",
            )

        endpoint = "/system.replacemsg/auth"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        msg_type: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/replacemsg/auth object.

        Replacement messages.

        Args:
            msg_type: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If msg-type is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_replacemsg_auth.delete(msg_type=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not msg_type:
            raise ValueError("msg-type is required for DELETE")
        endpoint = "/system.replacemsg/auth/" + str(msg_type)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        msg_type: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/replacemsg/auth object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            msg_type: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_replacemsg_auth.exists(msg_type=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_replacemsg_auth.exists(msg_type=1):
            ...     fgt.api.cmdb.system_replacemsg_auth.delete(msg_type=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # For readonly endpoints, check by fetching all items and scanning
        # This is necessary because readonly endpoints don't support direct ID queries
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
                item.get("msg-type") == msg_type
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
                    item.get("msg-type") == msg_type
                    for item in results
                )
            return _check()


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/replacemsg/auth object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (msg-type) in the payload.

        Args:
            payload_dict: Resource data including msg-type (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If msg-type is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "msg-type": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_replacemsg_auth.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_replacemsg_auth.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("msg-type")
        if not mkey_value:
            raise ValueError("msg-type is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(msg_type=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        msg_type: str,
        action: Literal["before", "after"],
        reference_msg_type: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/replacemsg/auth object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            msg_type: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_msg_type: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_replacemsg_auth.move(
            ...     msg_type=100,
            ...     action="before",
            ...     reference_msg_type=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system.replacemsg/auth",
            params={
                "msg-type": msg_type,
                "action": "move",
                action: reference_msg_type,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        msg_type: str,
        new_msg_type: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/replacemsg/auth object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            msg_type: Identifier of object to clone
            new_msg_type: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_replacemsg_auth.clone(
            ...     msg_type=1,
            ...     new_msg_type=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system.replacemsg/auth",
            params={
                "msg-type": msg_type,
                "new_msg-type": new_msg_type,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


