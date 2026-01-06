"""
FortiOS CMDB - System speed_test_schedule

Configuration endpoint for managing cmdb system/speed_test_schedule objects.

API Endpoints:
    GET    /cmdb/system/speed_test_schedule
    POST   /cmdb/system/speed_test_schedule
    PUT    /cmdb/system/speed_test_schedule/{identifier}
    DELETE /cmdb/system/speed_test_schedule/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_speed_test_schedule.get()

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


class SpeedTestSchedule(MetadataMixin):
    """SpeedTestSchedule Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "speed_test_schedule"
    
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
        """Initialize SpeedTestSchedule endpoint."""
        self._client = client

    def get(
        self,
        interface: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/speed_test_schedule configuration.

        Speed test schedule for each interface.

        Args:
            interface: String identifier to retrieve specific object.
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
            >>> # Get all system/speed_test_schedule objects
            >>> result = fgt.api.cmdb.system_speed_test_schedule.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/speed_test_schedule by interface
            >>> result = fgt.api.cmdb.system_speed_test_schedule.get(interface=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_speed_test_schedule.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_speed_test_schedule.get(action="schema")

        See Also:
            - post(): Create new system/speed_test_schedule object
            - put(): Update existing system/speed_test_schedule object
            - delete(): Remove system/speed_test_schedule object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if interface:
            endpoint = "/system/speed-test-schedule/" + str(interface)
        else:
            endpoint = "/system/speed-test-schedule"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        interface: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        diffserv: str | None = None,
        server_name: str | None = None,
        mode: Literal["UDP", "TCP", "Auto"] | None = None,
        schedules: str | list | None = None,
        dynamic_server: Literal["disable", "enable"] | None = None,
        ctrl_port: int | None = None,
        server_port: int | None = None,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = None,
        update_inbandwidth: Literal["disable", "enable"] | None = None,
        update_outbandwidth: Literal["disable", "enable"] | None = None,
        update_interface_shaping: Literal["disable", "enable"] | None = None,
        update_inbandwidth_maximum: int | None = None,
        update_inbandwidth_minimum: int | None = None,
        update_outbandwidth_maximum: int | None = None,
        update_outbandwidth_minimum: int | None = None,
        expected_inbandwidth_minimum: int | None = None,
        expected_inbandwidth_maximum: int | None = None,
        expected_outbandwidth_minimum: int | None = None,
        expected_outbandwidth_maximum: int | None = None,
        retries: int | None = None,
        retry_pause: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/speed_test_schedule object.

        Speed test schedule for each interface.

        Args:
            payload_dict: Object data as dict. Must include interface (primary key).
            interface: Interface name.
            status: Enable/disable scheduled speed test.
            diffserv: DSCP used for speed test.
            server_name: Speed test server name in system.speed-test-server list or leave it as empty to choose default server "FTNT_Auto".
            mode: Protocol Auto(default), TCP or UDP used for speed test.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If interface is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_speed_test_schedule.put(
            ...     interface=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "interface": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_speed_test_schedule.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            interface=interface,
            status=status,
            diffserv=diffserv,
            server_name=server_name,
            mode=mode,
            schedules=schedules,
            dynamic_server=dynamic_server,
            ctrl_port=ctrl_port,
            server_port=server_port,
            update_shaper=update_shaper,
            update_inbandwidth=update_inbandwidth,
            update_outbandwidth=update_outbandwidth,
            update_interface_shaping=update_interface_shaping,
            update_inbandwidth_maximum=update_inbandwidth_maximum,
            update_inbandwidth_minimum=update_inbandwidth_minimum,
            update_outbandwidth_maximum=update_outbandwidth_maximum,
            update_outbandwidth_minimum=update_outbandwidth_minimum,
            expected_inbandwidth_minimum=expected_inbandwidth_minimum,
            expected_inbandwidth_maximum=expected_inbandwidth_maximum,
            expected_outbandwidth_minimum=expected_outbandwidth_minimum,
            expected_outbandwidth_maximum=expected_outbandwidth_maximum,
            retries=retries,
            retry_pause=retry_pause,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.speed_test_schedule import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/speed_test_schedule",
            )
        
        interface_value = payload_data.get("interface")
        if not interface_value:
            raise ValueError("interface is required for PUT")
        endpoint = "/system/speed-test-schedule/" + str(interface_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        interface: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        diffserv: str | None = None,
        server_name: str | None = None,
        mode: Literal["UDP", "TCP", "Auto"] | None = None,
        schedules: str | list | None = None,
        dynamic_server: Literal["disable", "enable"] | None = None,
        ctrl_port: int | None = None,
        server_port: int | None = None,
        update_shaper: Literal["disable", "local", "remote", "both"] | None = None,
        update_inbandwidth: Literal["disable", "enable"] | None = None,
        update_outbandwidth: Literal["disable", "enable"] | None = None,
        update_interface_shaping: Literal["disable", "enable"] | None = None,
        update_inbandwidth_maximum: int | None = None,
        update_inbandwidth_minimum: int | None = None,
        update_outbandwidth_maximum: int | None = None,
        update_outbandwidth_minimum: int | None = None,
        expected_inbandwidth_minimum: int | None = None,
        expected_inbandwidth_maximum: int | None = None,
        expected_outbandwidth_minimum: int | None = None,
        expected_outbandwidth_maximum: int | None = None,
        retries: int | None = None,
        retry_pause: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/speed_test_schedule object.

        Speed test schedule for each interface.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            interface: Interface name.
            status: Enable/disable scheduled speed test.
            diffserv: DSCP used for speed test.
            server_name: Speed test server name in system.speed-test-server list or leave it as empty to choose default server "FTNT_Auto".
            mode: Protocol Auto(default), TCP or UDP used for speed test.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned interface.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_speed_test_schedule.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created interface: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SpeedTestSchedule.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_speed_test_schedule.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SpeedTestSchedule.required_fields()) }}
            
            Use SpeedTestSchedule.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            interface=interface,
            status=status,
            diffserv=diffserv,
            server_name=server_name,
            mode=mode,
            schedules=schedules,
            dynamic_server=dynamic_server,
            ctrl_port=ctrl_port,
            server_port=server_port,
            update_shaper=update_shaper,
            update_inbandwidth=update_inbandwidth,
            update_outbandwidth=update_outbandwidth,
            update_interface_shaping=update_interface_shaping,
            update_inbandwidth_maximum=update_inbandwidth_maximum,
            update_inbandwidth_minimum=update_inbandwidth_minimum,
            update_outbandwidth_maximum=update_outbandwidth_maximum,
            update_outbandwidth_minimum=update_outbandwidth_minimum,
            expected_inbandwidth_minimum=expected_inbandwidth_minimum,
            expected_inbandwidth_maximum=expected_inbandwidth_maximum,
            expected_outbandwidth_minimum=expected_outbandwidth_minimum,
            expected_outbandwidth_maximum=expected_outbandwidth_maximum,
            retries=retries,
            retry_pause=retry_pause,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.speed_test_schedule import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/speed_test_schedule",
            )

        endpoint = "/system/speed-test-schedule"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        interface: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/speed_test_schedule object.

        Speed test schedule for each interface.

        Args:
            interface: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If interface is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_speed_test_schedule.delete(interface=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not interface:
            raise ValueError("interface is required for DELETE")
        endpoint = "/system/speed-test-schedule/" + str(interface)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        interface: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/speed_test_schedule object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            interface: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_speed_test_schedule.exists(interface=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_speed_test_schedule.exists(interface=1):
            ...     fgt.api.cmdb.system_speed_test_schedule.delete(interface=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                interface=interface,
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
        Create or update system/speed_test_schedule object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (interface) in the payload.

        Args:
            payload_dict: Resource data including interface (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If interface is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "interface": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_speed_test_schedule.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_speed_test_schedule.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("interface")
        if not mkey_value:
            raise ValueError("interface is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(interface=mkey_value, vdom=vdom):
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
        interface: str,
        action: Literal["before", "after"],
        reference_interface: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/speed_test_schedule object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            interface: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_interface: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_speed_test_schedule.move(
            ...     interface=100,
            ...     action="before",
            ...     reference_interface=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/speed-test-schedule",
            params={
                "interface": interface,
                "action": "move",
                action: reference_interface,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        interface: str,
        new_interface: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/speed_test_schedule object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            interface: Identifier of object to clone
            new_interface: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_speed_test_schedule.clone(
            ...     interface=1,
            ...     new_interface=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/speed-test-schedule",
            params={
                "interface": interface,
                "new_interface": new_interface,
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
        interface: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/speed_test_schedule object exists.
        
        Args:
            interface: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_speed_test_schedule.exists(interface=1):
            ...     fgt.api.cmdb.system_speed_test_schedule.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                interface=interface,
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

