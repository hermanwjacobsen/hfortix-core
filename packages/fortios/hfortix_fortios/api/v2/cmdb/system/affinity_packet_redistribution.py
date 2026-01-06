"""
FortiOS CMDB - System affinity_packet_redistribution

Configuration endpoint for managing cmdb system/affinity_packet_redistribution objects.

API Endpoints:
    GET    /cmdb/system/affinity_packet_redistribution
    POST   /cmdb/system/affinity_packet_redistribution
    PUT    /cmdb/system/affinity_packet_redistribution/{identifier}
    DELETE /cmdb/system/affinity_packet_redistribution/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_affinity_packet_redistribution.get()

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


class AffinityPacketRedistribution(MetadataMixin):
    """AffinityPacketRedistribution Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "affinity_packet_redistribution"

    def __init__(self, client: "IHTTPClient"):
        """Initialize AffinityPacketRedistribution endpoint."""
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
        Retrieve system/affinity_packet_redistribution configuration.

        Configure packet redistribution.

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
            >>> # Get all system/affinity_packet_redistribution objects
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/affinity_packet_redistribution by id
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.get(id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_affinity_packet_redistribution.get(action="schema")

        See Also:
            - post(): Create new system/affinity_packet_redistribution object
            - put(): Update existing system/affinity_packet_redistribution object
            - delete(): Remove system/affinity_packet_redistribution object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if id:
            endpoint = "/system/affinity-packet-redistribution/" + str(id)
        else:
            endpoint = "/system/affinity-packet-redistribution"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        interface: str | None = None,
        rxqid: int | None = None,
        round_robin: str | None = None,
        affinity_cpumask: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/affinity_packet_redistribution object.

        Configure packet redistribution.

        Args:
            payload_dict: Object data as dict. Must include id (primary key).
            id: ID of the packet redistribution setting.
            interface: Physical interface name on which to perform packet redistribution.
            rxqid: ID of the receive queue (when the interface has multiple queues) on which to perform packet redistribution (255 = all queues).
            round_robin: Enable/disable round-robin redistribution to multiple CPUs.
            affinity_cpumask: Hexadecimal cpumask, empty value means all CPUs.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.put(
            ...     id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            interface=interface,
            rxqid=rxqid,
            round_robin=round_robin,
            affinity_cpumask=affinity_cpumask,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.affinity_packet_redistribution import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/affinity_packet_redistribution",
            )
        
        id_value = payload_data.get("id")
        if not id_value:
            raise ValueError("id is required for PUT")
        endpoint = "/system/affinity-packet-redistribution/" + str(id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        interface: str | None = None,
        rxqid: int | None = None,
        round_robin: str | None = None,
        affinity_cpumask: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/affinity_packet_redistribution object.

        Configure packet redistribution.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            id: ID of the packet redistribution setting.
            interface: Physical interface name on which to perform packet redistribution.
            rxqid: ID of the receive queue (when the interface has multiple queues) on which to perform packet redistribution (255 = all queues).
            round_robin: Enable/disable round-robin redistribution to multiple CPUs.
            affinity_cpumask: Hexadecimal cpumask, empty value means all CPUs.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = AffinityPacketRedistribution.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(AffinityPacketRedistribution.required_fields()) }}
            
            Use AffinityPacketRedistribution.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            interface=interface,
            rxqid=rxqid,
            round_robin=round_robin,
            affinity_cpumask=affinity_cpumask,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.affinity_packet_redistribution import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/affinity_packet_redistribution",
            )

        endpoint = "/system/affinity-packet-redistribution"
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
        Delete system/affinity_packet_redistribution object.

        Configure packet redistribution.

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
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.delete(id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not id:
            raise ValueError("id is required for DELETE")
        endpoint = "/system/affinity-packet-redistribution/" + str(id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/affinity_packet_redistribution object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_affinity_packet_redistribution.exists(id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_affinity_packet_redistribution.exists(id=1):
            ...     fgt.api.cmdb.system_affinity_packet_redistribution.delete(id=1)

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
        Create or update system/affinity_packet_redistribution object (intelligent operation).

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
            >>> result = fgt.api.cmdb.system_affinity_packet_redistribution.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_affinity_packet_redistribution.set(payload_dict=obj_data)
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


