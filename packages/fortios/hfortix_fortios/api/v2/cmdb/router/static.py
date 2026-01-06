"""
FortiOS CMDB - Router static

Configuration endpoint for managing cmdb router/static objects.

API Endpoints:
    GET    /cmdb/router/static
    POST   /cmdb/router/static
    PUT    /cmdb/router/static/{identifier}
    DELETE /cmdb/router/static/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_static.get()

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


class Static(MetadataMixin):
    """Static Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "static"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Static endpoint."""
        self._client = client

    def get(
        self,
        seq_num: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve router/static configuration.

        Configure IPv4 static routing tables.

        Args:
            seq_num: Integer identifier to retrieve specific object.
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
            >>> # Get all router/static objects
            >>> result = fgt.api.cmdb.router_static.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific router/static by seq-num
            >>> result = fgt.api.cmdb.router_static.get(seq_num=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_static.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_static.get(action="schema")

        See Also:
            - post(): Create new router/static object
            - put(): Update existing router/static object
            - delete(): Remove router/static object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if seq_num:
            endpoint = "/router/static/" + str(seq_num)
        else:
            endpoint = "/router/static"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        status: str | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: str | list | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: str | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/static object.

        Configure IPv4 static routing tables.

        Args:
            payload_dict: Object data as dict. Must include seq-num (primary key).
            seq_num: Sequence number.
            status: Enable/disable this static route.
            dst: Destination IP and mask for this route.
            src: Source prefix for this route.
            gateway: Gateway IP for this route.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_static.put(
            ...     seq_num=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_static.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            seq_num=seq_num,
            status=status,
            dst=dst,
            src=src,
            gateway=gateway,
            preferred_source=preferred_source,
            distance=distance,
            weight=weight,
            priority=priority,
            device=device,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            internet_service=internet_service,
            internet_service_custom=internet_service_custom,
            internet_service_fortiguard=internet_service_fortiguard,
            link_monitor_exempt=link_monitor_exempt,
            tag=tag,
            vrf=vrf,
            bfd=bfd,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.static import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/static",
            )
        
        seq_num_value = payload_data.get("seq-num")
        if not seq_num_value:
            raise ValueError("seq-num is required for PUT")
        endpoint = "/router/static/" + str(seq_num_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        status: str | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: str | list | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: str | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new router/static object.

        Configure IPv4 static routing tables.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            seq_num: Sequence number.
            status: Enable/disable this static route.
            dst: Destination IP and mask for this route.
            src: Source prefix for this route.
            gateway: Gateway IP for this route.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned seq-num.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.router_static.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created seq-num: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Static.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.router_static.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Static.required_fields()) }}
            
            Use Static.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            seq_num=seq_num,
            status=status,
            dst=dst,
            src=src,
            gateway=gateway,
            preferred_source=preferred_source,
            distance=distance,
            weight=weight,
            priority=priority,
            device=device,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            internet_service=internet_service,
            internet_service_custom=internet_service_custom,
            internet_service_fortiguard=internet_service_fortiguard,
            link_monitor_exempt=link_monitor_exempt,
            tag=tag,
            vrf=vrf,
            bfd=bfd,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.static import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/static",
            )

        endpoint = "/router/static"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        seq_num: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete router/static object.

        Configure IPv4 static routing tables.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If seq-num is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.router_static.delete(seq_num=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not seq_num:
            raise ValueError("seq-num is required for DELETE")
        endpoint = "/router/static/" + str(seq_num)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if router/static object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.router_static.exists(seq_num=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.router_static.exists(seq_num=1):
            ...     fgt.api.cmdb.router_static.delete(seq_num=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(seq_num=seq_num, vdom=vdom, raw_json=True)
            
            if isinstance(response, dict):
                # Use helper function to check success
                return is_success(response)
            else:
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception:
            # Resource not found or other error - return False
            return False


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update router/static object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (seq-num) in the payload.

        Args:
            payload_dict: Resource data including seq-num (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.router_static.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.router_static.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("seq-num")
        if not mkey_value:
            raise ValueError("seq-num is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(seq_num=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


