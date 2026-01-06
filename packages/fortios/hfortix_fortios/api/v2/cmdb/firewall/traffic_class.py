"""
FortiOS CMDB - Firewall traffic_class

Configuration endpoint for managing cmdb firewall/traffic_class objects.

API Endpoints:
    GET    /cmdb/firewall/traffic_class
    POST   /cmdb/firewall/traffic_class
    PUT    /cmdb/firewall/traffic_class/{identifier}
    DELETE /cmdb/firewall/traffic_class/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_traffic_class.get()

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


class TrafficClass(MetadataMixin):
    """TrafficClass Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "traffic_class"

    def __init__(self, client: "IHTTPClient"):
        """Initialize TrafficClass endpoint."""
        self._client = client

    def get(
        self,
        class_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve firewall/traffic_class configuration.

        Configure names for shaping classes.

        Args:
            class_id: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/traffic_class objects
            >>> result = fgt.api.cmdb.firewall_traffic_class.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/traffic_class by class-id
            >>> result = fgt.api.cmdb.firewall_traffic_class.get(class_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_traffic_class.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_traffic_class.get(action="schema")

        See Also:
            - post(): Create new firewall/traffic_class object
            - put(): Update existing firewall/traffic_class object
            - delete(): Remove firewall/traffic_class object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if class_id:
            endpoint = "/firewall/traffic-class/" + str(class_id)
        else:
            endpoint = "/firewall/traffic-class"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        class_id: int | None = None,
        class_name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/traffic_class object.

        Configure names for shaping classes.

        Args:
            payload_dict: Object data as dict. Must include class-id (primary key).
            class_id: Class ID to be named.
            class_name: Define the name for this class-id.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If class-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_traffic_class.put(
            ...     class_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "class-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_traffic_class.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            class_id=class_id,
            class_name=class_name,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.traffic_class import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/traffic_class",
            )
        
        class_id_value = payload_data.get("class-id")
        if not class_id_value:
            raise ValueError("class-id is required for PUT")
        endpoint = "/firewall/traffic-class/" + str(class_id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        class_id: int | None = None,
        class_name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/traffic_class object.

        Configure names for shaping classes.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            class_id: Class ID to be named.
            class_name: Define the name for this class-id.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned class-id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_traffic_class.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created class-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = TrafficClass.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_traffic_class.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(TrafficClass.required_fields()) }}
            
            Use TrafficClass.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            class_id=class_id,
            class_name=class_name,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.traffic_class import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/traffic_class",
            )

        endpoint = "/firewall/traffic-class"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        class_id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/traffic_class object.

        Configure names for shaping classes.

        Args:
            class_id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If class-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_traffic_class.delete(class_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not class_id:
            raise ValueError("class-id is required for DELETE")
        endpoint = "/firewall/traffic-class/" + str(class_id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        class_id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/traffic_class object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            class_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_traffic_class.exists(class_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_traffic_class.exists(class_id=1):
            ...     fgt.api.cmdb.firewall_traffic_class.delete(class_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(class_id=class_id, vdom=vdom, raw_json=True)
            
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
        Create or update firewall/traffic_class object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (class-id) in the payload.

        Args:
            payload_dict: Resource data including class-id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If class-id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "class-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_traffic_class.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_traffic_class.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("class-id")
        if not mkey_value:
            raise ValueError("class-id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(class_id=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


