"""
FortiOS CMDB - System ike

Configuration endpoint for managing cmdb system/ike objects.

API Endpoints:
    GET    /cmdb/system/ike
    POST   /cmdb/system/ike
    PUT    /cmdb/system/ike/{identifier}
    DELETE /cmdb/system/ike/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ike.get()

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


class Ike(MetadataMixin):
    """Ike Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ike"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ike endpoint."""
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
        Retrieve system/ike configuration.

        Configure IKE global attributes.

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
            >>> # Get all system/ike objects
            >>> result = fgt.api.cmdb.system_ike.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ike.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ike.get(action="schema")

        See Also:
            - post(): Create new system/ike object
            - put(): Update existing system/ike object
            - delete(): Remove system/ike object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ike/{name}"
        else:
            endpoint = "/system/ike"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        embryonic_limit: int | None = None,
        dh_multiprocess: Literal["enable", "disable"] | None = None,
        dh_worker_count: int | None = None,
        dh_mode: Literal["software", "hardware"] | None = None,
        dh_keypair_cache: Literal["enable", "disable"] | None = None,
        dh_keypair_count: int | None = None,
        dh_keypair_throttle: Literal["enable", "disable"] | None = None,
        dh_group_1: str | None = None,
        dh_group_2: str | None = None,
        dh_group_5: str | None = None,
        dh_group_14: str | None = None,
        dh_group_15: str | None = None,
        dh_group_16: str | None = None,
        dh_group_17: str | None = None,
        dh_group_18: str | None = None,
        dh_group_19: str | None = None,
        dh_group_20: str | None = None,
        dh_group_21: str | None = None,
        dh_group_27: str | None = None,
        dh_group_28: str | None = None,
        dh_group_29: str | None = None,
        dh_group_30: str | None = None,
        dh_group_31: str | None = None,
        dh_group_32: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ike object.

        Configure IKE global attributes.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            embryonic_limit: Maximum number of IPsec tunnels to negotiate simultaneously.
            dh_multiprocess: Enable/disable multiprocess Diffie-Hellman daemon for IKE.
            dh_worker_count: Number of Diffie-Hellman workers to start.
            dh_mode: Use software (CPU) or hardware (CPX) to perform Diffie-Hellman calculations.
            dh_keypair_cache: Enable/disable Diffie-Hellman key pair cache.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ike.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ike.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            embryonic_limit=embryonic_limit,
            dh_multiprocess=dh_multiprocess,
            dh_worker_count=dh_worker_count,
            dh_mode=dh_mode,
            dh_keypair_cache=dh_keypair_cache,
            dh_keypair_count=dh_keypair_count,
            dh_keypair_throttle=dh_keypair_throttle,
            dh_group_1=dh_group_1,
            dh_group_2=dh_group_2,
            dh_group_5=dh_group_5,
            dh_group_14=dh_group_14,
            dh_group_15=dh_group_15,
            dh_group_16=dh_group_16,
            dh_group_17=dh_group_17,
            dh_group_18=dh_group_18,
            dh_group_19=dh_group_19,
            dh_group_20=dh_group_20,
            dh_group_21=dh_group_21,
            dh_group_27=dh_group_27,
            dh_group_28=dh_group_28,
            dh_group_29=dh_group_29,
            dh_group_30=dh_group_30,
            dh_group_31=dh_group_31,
            dh_group_32=dh_group_32,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ike import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ike",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ike/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/ike object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_ike.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/ike",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/ike object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_ike.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/ike",
            params={
                "name": name,
                "new_name": new_name,
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
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/ike object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_ike.exists(name="myobj"):
            ...     fgt.api.cmdb.system_ike.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
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

