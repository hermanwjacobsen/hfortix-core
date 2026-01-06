"""
FortiOS CMDB - Wireless_controller hotspot20 anqp_ip_address_type

Configuration endpoint for managing cmdb wireless_controller/hotspot20/anqp_ip_address_type objects.

API Endpoints:
    GET    /cmdb/wireless_controller/hotspot20/anqp_ip_address_type
    POST   /cmdb/wireless_controller/hotspot20/anqp_ip_address_type
    PUT    /cmdb/wireless_controller/hotspot20/anqp_ip_address_type/{identifier}
    DELETE /cmdb/wireless_controller/hotspot20/anqp_ip_address_type/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.get()

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


class AnqpIpAddressType(MetadataMixin):
    """AnqpIpAddressType Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "anqp_ip_address_type"

    def __init__(self, client: "IHTTPClient"):
        """Initialize AnqpIpAddressType endpoint."""
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
        Retrieve wireless_controller/hotspot20/anqp_ip_address_type configuration.

        Configure IP address type availability.

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
            >>> # Get all wireless_controller/hotspot20/anqp_ip_address_type objects
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/hotspot20/anqp_ip_address_type by name
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/hotspot20/anqp_ip_address_type object
            - put(): Update existing wireless_controller/hotspot20/anqp_ip_address_type object
            - delete(): Remove wireless_controller/hotspot20/anqp_ip_address_type object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/wireless-controller.hotspot20/anqp-ip-address-type/" + str(name)
        else:
            endpoint = "/wireless-controller.hotspot20/anqp-ip-address-type"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        ipv6_address_type: str | None = None,
        ipv4_address_type: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/hotspot20/anqp_ip_address_type object.

        Configure IP address type availability.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IP type name.
            ipv6_address_type: IPv6 address type.
            ipv4_address_type: IPv4 address type.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            ipv6_address_type=ipv6_address_type,
            ipv4_address_type=ipv4_address_type,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.anqp_ip_address_type import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/hotspot20/anqp_ip_address_type",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller.hotspot20/anqp-ip-address-type/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        ipv6_address_type: str | None = None,
        ipv4_address_type: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/hotspot20/anqp_ip_address_type object.

        Configure IP address type availability.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IP type name.
            ipv6_address_type: IPv6 address type.
            ipv4_address_type: IPv4 address type.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = AnqpIpAddressType.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(AnqpIpAddressType.required_fields()) }}
            
            Use AnqpIpAddressType.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            ipv6_address_type=ipv6_address_type,
            ipv4_address_type=ipv4_address_type,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.anqp_ip_address_type import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/hotspot20/anqp_ip_address_type",
            )

        endpoint = "/wireless-controller.hotspot20/anqp-ip-address-type"
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
        Delete wireless_controller/hotspot20/anqp_ip_address_type object.

        Configure IP address type availability.

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
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller.hotspot20/anqp-ip-address-type/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/hotspot20/anqp_ip_address_type object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(name=name, vdom=vdom, raw_json=True)
            
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
        Create or update wireless_controller/hotspot20/anqp_ip_address_type object (intelligent operation).

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
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_hotspot20_anqp_ip_address_type.set(payload_dict=obj_data)
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


