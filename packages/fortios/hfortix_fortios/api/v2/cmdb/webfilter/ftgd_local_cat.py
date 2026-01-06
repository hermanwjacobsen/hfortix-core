"""
FortiOS CMDB - Webfilter ftgd_local_cat

Configuration endpoint for managing cmdb webfilter/ftgd_local_cat objects.

API Endpoints:
    GET    /cmdb/webfilter/ftgd_local_cat
    POST   /cmdb/webfilter/ftgd_local_cat
    PUT    /cmdb/webfilter/ftgd_local_cat/{identifier}
    DELETE /cmdb/webfilter/ftgd_local_cat/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.webfilter_ftgd_local_cat.get()

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
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


class FtgdLocalCat(MetadataMixin):
    """FtgdLocalCat Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ftgd_local_cat"
    
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
        """Initialize FtgdLocalCat endpoint."""
        self._client = client

    def get(
        self,
        desc: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve webfilter/ftgd_local_cat configuration.

        Configure FortiGuard Web Filter local categories.

        Args:
            desc: String identifier to retrieve specific object.
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
            >>> # Get all webfilter/ftgd_local_cat objects
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific webfilter/ftgd_local_cat by desc
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.get(desc=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.webfilter_ftgd_local_cat.get(action="schema")

        See Also:
            - post(): Create new webfilter/ftgd_local_cat object
            - put(): Update existing webfilter/ftgd_local_cat object
            - delete(): Remove webfilter/ftgd_local_cat object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if desc:
            endpoint = "/webfilter/ftgd-local-cat/" + str(desc)
        else:
            endpoint = "/webfilter/ftgd-local-cat"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["enable", "disable"] | None = None,
        id: int | None = None,
        desc: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing webfilter/ftgd_local_cat object.

        Configure FortiGuard Web Filter local categories.

        Args:
            payload_dict: Object data as dict. Must include desc (primary key).
            status: Enable/disable the local category.
            id: Local category ID.
            desc: Local category description.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If desc is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.put(
            ...     desc=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "desc": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            id=id,
            desc=desc,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ftgd_local_cat import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/webfilter/ftgd_local_cat",
            )
        
        desc_value = payload_data.get("desc")
        if not desc_value:
            raise ValueError("desc is required for PUT")
        endpoint = "/webfilter/ftgd-local-cat/" + str(desc_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["enable", "disable"] | None = None,
        id: int | None = None,
        desc: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new webfilter/ftgd_local_cat object.

        Configure FortiGuard Web Filter local categories.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            status: Enable/disable the local category.
            id: Local category ID.
            desc: Local category description.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned desc.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created desc: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = FtgdLocalCat.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(FtgdLocalCat.required_fields()) }}
            
            Use FtgdLocalCat.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            id=id,
            desc=desc,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.ftgd_local_cat import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/webfilter/ftgd_local_cat",
            )

        endpoint = "/webfilter/ftgd-local-cat"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        desc: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete webfilter/ftgd_local_cat object.

        Configure FortiGuard Web Filter local categories.

        Args:
            desc: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If desc is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.delete(desc=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not desc:
            raise ValueError("desc is required for DELETE")
        endpoint = "/webfilter/ftgd-local-cat/" + str(desc)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        desc: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if webfilter/ftgd_local_cat object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            desc: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.webfilter_ftgd_local_cat.exists(desc=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.webfilter_ftgd_local_cat.exists(desc=1):
            ...     fgt.api.cmdb.webfilter_ftgd_local_cat.delete(desc=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                desc=desc,
                vdom=vdom,
                raw_json=True
            )
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update webfilter/ftgd_local_cat object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (desc) in the payload.

        Args:
            payload_dict: Resource data including desc (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If desc is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "desc": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.webfilter_ftgd_local_cat.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.webfilter_ftgd_local_cat.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("desc")
        if not mkey_value:
            raise ValueError("desc is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(desc=mkey_value, vdom=vdom):
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
        desc: str,
        action: Literal["before", "after"],
        reference_desc: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move webfilter/ftgd_local_cat object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            desc: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_desc: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.webfilter_ftgd_local_cat.move(
            ...     desc=100,
            ...     action="before",
            ...     reference_desc=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/webfilter/ftgd-local-cat",
            params={
                "desc": desc,
                "action": "move",
                action: reference_desc,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        desc: str,
        new_desc: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone webfilter/ftgd_local_cat object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            desc: Identifier of object to clone
            new_desc: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.webfilter_ftgd_local_cat.clone(
            ...     desc=1,
            ...     new_desc=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/webfilter/ftgd-local-cat",
            params={
                "desc": desc,
                "new_desc": new_desc,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        desc: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if webfilter/ftgd_local_cat object exists.
        
        Args:
            desc: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.webfilter_ftgd_local_cat.exists(desc=1):
            ...     fgt.api.cmdb.webfilter_ftgd_local_cat.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                desc=desc,
                vdom=vdom,
                raw_json=True
            )
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

