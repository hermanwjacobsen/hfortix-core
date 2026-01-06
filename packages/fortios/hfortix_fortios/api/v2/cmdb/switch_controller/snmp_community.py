"""
FortiOS CMDB - Switch_controller snmp_community

Configuration endpoint for managing cmdb switch_controller/snmp_community objects.

API Endpoints:
    GET    /cmdb/switch_controller/snmp_community
    POST   /cmdb/switch_controller/snmp_community
    PUT    /cmdb/switch_controller/snmp_community/{identifier}
    DELETE /cmdb/switch_controller/snmp_community/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_snmp_community.get()

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


class SnmpCommunity(MetadataMixin):
    """SnmpCommunity Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "snmp_community"

    def __init__(self, client: "IHTTPClient"):
        """Initialize SnmpCommunity endpoint."""
        self._client = client

    def get(
        self,
        id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve switch_controller/snmp_community configuration.

        Configure FortiSwitch SNMP v1/v2c communities globally.

        Args:
            id: Integer identifier to retrieve specific object.
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
            >>> # Get all switch_controller/snmp_community objects
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific switch_controller/snmp_community by id
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.get(id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_snmp_community.get(action="schema")

        See Also:
            - post(): Create new switch_controller/snmp_community object
            - put(): Update existing switch_controller/snmp_community object
            - delete(): Remove switch_controller/snmp_community object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if id:
            endpoint = "/switch-controller/snmp-community/" + str(id)
        else:
            endpoint = "/switch-controller/snmp-community"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        name: str | None = None,
        status: str | None = None,
        hosts: str | list | None = None,
        query_v1_status: str | None = None,
        query_v1_port: int | None = None,
        query_v2c_status: str | None = None,
        query_v2c_port: int | None = None,
        trap_v1_status: str | None = None,
        trap_v1_lport: int | None = None,
        trap_v1_rport: int | None = None,
        trap_v2c_status: str | None = None,
        trap_v2c_lport: int | None = None,
        trap_v2c_rport: int | None = None,
        events: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/snmp_community object.

        Configure FortiSwitch SNMP v1/v2c communities globally.

        Args:
            payload_dict: Object data as dict. Must include id (primary key).
            id: SNMP community ID.
            name: SNMP community name.
            status: Enable/disable this SNMP community.
            hosts: Configure IPv4 SNMP managers (hosts).
            query_v1_status: Enable/disable SNMP v1 queries.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.put(
            ...     id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            name=name,
            status=status,
            hosts=hosts,
            query_v1_status=query_v1_status,
            query_v1_port=query_v1_port,
            query_v2c_status=query_v2c_status,
            query_v2c_port=query_v2c_port,
            trap_v1_status=trap_v1_status,
            trap_v1_lport=trap_v1_lport,
            trap_v1_rport=trap_v1_rport,
            trap_v2c_status=trap_v2c_status,
            trap_v2c_lport=trap_v2c_lport,
            trap_v2c_rport=trap_v2c_rport,
            events=events,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.snmp_community import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/snmp_community",
            )
        
        id_value = payload_data.get("id")
        if not id_value:
            raise ValueError("id is required for PUT")
        endpoint = "/switch-controller/snmp-community/" + str(id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        name: str | None = None,
        status: str | None = None,
        hosts: str | list | None = None,
        query_v1_status: str | None = None,
        query_v1_port: int | None = None,
        query_v2c_status: str | None = None,
        query_v2c_port: int | None = None,
        trap_v1_status: str | None = None,
        trap_v1_lport: int | None = None,
        trap_v1_rport: int | None = None,
        trap_v2c_status: str | None = None,
        trap_v2c_lport: int | None = None,
        trap_v2c_rport: int | None = None,
        events: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new switch_controller/snmp_community object.

        Configure FortiSwitch SNMP v1/v2c communities globally.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            id: SNMP community ID.
            name: SNMP community name.
            status: Enable/disable this SNMP community.
            hosts: Configure IPv4 SNMP managers (hosts).
            query_v1_status: Enable/disable SNMP v1 queries.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SnmpCommunity.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SnmpCommunity.required_fields()) }}
            
            Use SnmpCommunity.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            name=name,
            status=status,
            hosts=hosts,
            query_v1_status=query_v1_status,
            query_v1_port=query_v1_port,
            query_v2c_status=query_v2c_status,
            query_v2c_port=query_v2c_port,
            trap_v1_status=trap_v1_status,
            trap_v1_lport=trap_v1_lport,
            trap_v1_rport=trap_v1_rport,
            trap_v2c_status=trap_v2c_status,
            trap_v2c_lport=trap_v2c_lport,
            trap_v2c_rport=trap_v2c_rport,
            events=events,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.snmp_community import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/snmp_community",
            )

        endpoint = "/switch-controller/snmp-community"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete switch_controller/snmp_community object.

        Configure FortiSwitch SNMP v1/v2c communities globally.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.delete(id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not id:
            raise ValueError("id is required for DELETE")
        endpoint = "/switch-controller/snmp-community/" + str(id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if switch_controller/snmp_community object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.switch_controller_snmp_community.exists(id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.switch_controller_snmp_community.exists(id=1):
            ...     fgt.api.cmdb.switch_controller_snmp_community.delete(id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(id=id, vdom=vdom, raw_json=True)
            
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
        Create or update switch_controller/snmp_community object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (id) in the payload.

        Args:
            payload_dict: Resource data including id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_snmp_community.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.switch_controller_snmp_community.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("id")
        if not mkey_value:
            raise ValueError("id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(id=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


