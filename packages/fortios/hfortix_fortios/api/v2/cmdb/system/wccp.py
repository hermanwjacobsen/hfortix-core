"""
FortiOS CMDB - System wccp

Configuration endpoint for managing cmdb system/wccp objects.

API Endpoints:
    GET    /cmdb/system/wccp
    POST   /cmdb/system/wccp
    PUT    /cmdb/system/wccp/{identifier}
    DELETE /cmdb/system/wccp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_wccp.get()

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


class Wccp(MetadataMixin):
    """Wccp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "wccp"
    
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
        """Initialize Wccp endpoint."""
        self._client = client

    def get(
        self,
        service_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/wccp configuration.

        Configure WCCP.

        Args:
            service_id: String identifier to retrieve specific object.
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
            >>> # Get all system/wccp objects
            >>> result = fgt.api.cmdb.system_wccp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/wccp by service-id
            >>> result = fgt.api.cmdb.system_wccp.get(service_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_wccp.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_wccp.get(action="schema")

        See Also:
            - post(): Create new system/wccp object
            - put(): Update existing system/wccp object
            - delete(): Remove system/wccp object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if service_id:
            endpoint = "/system/wccp/" + str(service_id)
        else:
            endpoint = "/system/wccp"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        service_id: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: Any | None = None,
        server_list: str | list | None = None,
        router_list: str | list | None = None,
        ports_defined: Literal["source", "destination"] | None = None,
        server_type: Literal["forward", "proxy"] | None = None,
        ports: str | list | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        forward_method: Literal["GRE", "L2", "any"] | None = None,
        cache_engine_method: Literal["GRE", "L2"] | None = None,
        service_type: Literal["auto", "standard", "dynamic"] | None = None,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = None,
        return_method: Literal["GRE", "L2", "any"] | None = None,
        assignment_method: Literal["HASH", "MASK", "any"] | None = None,
        assignment_srcaddr_mask: Any | None = None,
        assignment_dstaddr_mask: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/wccp object.

        Configure WCCP.

        Args:
            payload_dict: Object data as dict. Must include service-id (primary key).
            service_id: Service ID.
            router_id: IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.
            cache_id: IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.
            group_address: IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.
            server_list: IP addresses and netmasks for up to four cache servers.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If service-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_wccp.put(
            ...     service_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "service-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_wccp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            service_id=service_id,
            router_id=router_id,
            cache_id=cache_id,
            group_address=group_address,
            server_list=server_list,
            router_list=router_list,
            ports_defined=ports_defined,
            server_type=server_type,
            ports=ports,
            authentication=authentication,
            password=password,
            forward_method=forward_method,
            cache_engine_method=cache_engine_method,
            service_type=service_type,
            primary_hash=primary_hash,
            priority=priority,
            protocol=protocol,
            assignment_weight=assignment_weight,
            assignment_bucket_format=assignment_bucket_format,
            return_method=return_method,
            assignment_method=assignment_method,
            assignment_srcaddr_mask=assignment_srcaddr_mask,
            assignment_dstaddr_mask=assignment_dstaddr_mask,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wccp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/wccp",
            )
        
        service_id_value = payload_data.get("service-id")
        if not service_id_value:
            raise ValueError("service-id is required for PUT")
        endpoint = "/system/wccp/" + str(service_id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        service_id: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: Any | None = None,
        server_list: str | list | None = None,
        router_list: str | list | None = None,
        ports_defined: Literal["source", "destination"] | None = None,
        server_type: Literal["forward", "proxy"] | None = None,
        ports: str | list | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        forward_method: Literal["GRE", "L2", "any"] | None = None,
        cache_engine_method: Literal["GRE", "L2"] | None = None,
        service_type: Literal["auto", "standard", "dynamic"] | None = None,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = None,
        return_method: Literal["GRE", "L2", "any"] | None = None,
        assignment_method: Literal["HASH", "MASK", "any"] | None = None,
        assignment_srcaddr_mask: Any | None = None,
        assignment_dstaddr_mask: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/wccp object.

        Configure WCCP.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            service_id: Service ID.
            router_id: IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.
            cache_id: IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.
            group_address: IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.
            server_list: IP addresses and netmasks for up to four cache servers.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned service-id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_wccp.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created service-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Wccp.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_wccp.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Wccp.required_fields()) }}
            
            Use Wccp.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            service_id=service_id,
            router_id=router_id,
            cache_id=cache_id,
            group_address=group_address,
            server_list=server_list,
            router_list=router_list,
            ports_defined=ports_defined,
            server_type=server_type,
            ports=ports,
            authentication=authentication,
            password=password,
            forward_method=forward_method,
            cache_engine_method=cache_engine_method,
            service_type=service_type,
            primary_hash=primary_hash,
            priority=priority,
            protocol=protocol,
            assignment_weight=assignment_weight,
            assignment_bucket_format=assignment_bucket_format,
            return_method=return_method,
            assignment_method=assignment_method,
            assignment_srcaddr_mask=assignment_srcaddr_mask,
            assignment_dstaddr_mask=assignment_dstaddr_mask,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wccp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/wccp",
            )

        endpoint = "/system/wccp"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        service_id: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/wccp object.

        Configure WCCP.

        Args:
            service_id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If service-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_wccp.delete(service_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not service_id:
            raise ValueError("service-id is required for DELETE")
        endpoint = "/system/wccp/" + str(service_id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        service_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/wccp object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            service_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_wccp.exists(service_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_wccp.exists(service_id=1):
            ...     fgt.api.cmdb.system_wccp.delete(service_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                service_id=service_id,
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
        Create or update system/wccp object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (service-id) in the payload.

        Args:
            payload_dict: Resource data including service-id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If service-id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "service-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_wccp.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_wccp.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("service-id")
        if not mkey_value:
            raise ValueError("service-id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(service_id=mkey_value, vdom=vdom):
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
        service_id: str,
        action: Literal["before", "after"],
        reference_service_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/wccp object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            service_id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_service_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_wccp.move(
            ...     service_id=100,
            ...     action="before",
            ...     reference_service_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/wccp",
            params={
                "service-id": service_id,
                "action": "move",
                action: reference_service_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        service_id: str,
        new_service_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/wccp object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            service_id: Identifier of object to clone
            new_service_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_wccp.clone(
            ...     service_id=1,
            ...     new_service_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/wccp",
            params={
                "service-id": service_id,
                "new_service-id": new_service_id,
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
        service_id: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/wccp object exists.
        
        Args:
            service_id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_wccp.exists(service_id=1):
            ...     fgt.api.cmdb.system_wccp.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                service_id=service_id,
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

