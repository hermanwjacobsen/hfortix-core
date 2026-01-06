"""
FortiOS CMDB - System device_upgrade

Configuration endpoint for managing cmdb system/device_upgrade objects.

API Endpoints:
    GET    /cmdb/system/device_upgrade
    POST   /cmdb/system/device_upgrade
    PUT    /cmdb/system/device_upgrade/{identifier}
    DELETE /cmdb/system/device_upgrade/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_device_upgrade.get()

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


class DeviceUpgrade(MetadataMixin):
    """DeviceUpgrade Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "device_upgrade"
    
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
        """Initialize DeviceUpgrade endpoint."""
        self._client = client

    def get(
        self,
        serial: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/device_upgrade configuration.

        Independent upgrades for managed devices.

        Args:
            serial: String identifier to retrieve specific object.
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
            >>> # Get all system/device_upgrade objects
            >>> result = fgt.api.cmdb.system_device_upgrade.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/device_upgrade by serial
            >>> result = fgt.api.cmdb.system_device_upgrade.get(serial=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_device_upgrade.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_device_upgrade.get(action="schema")

        See Also:
            - post(): Create new system/device_upgrade object
            - put(): Update existing system/device_upgrade object
            - delete(): Remove system/device_upgrade object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if serial:
            endpoint = "/system/device-upgrade/" + str(serial)
        else:
            endpoint = "/system/device-upgrade"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: str | list | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        serial: str | None = None,
        timing: Literal["immediate", "scheduled"] | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = None,
        allow_download: Literal["enable", "disable"] | None = None,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/device_upgrade object.

        Independent upgrades for managed devices.

        Args:
            payload_dict: Object data as dict. Must include serial (primary key).
            vdom: Limit upgrade to this virtual domain (VDOM).
            status: Current status of the upgrade.
            ha_reboot_controller: Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.
            next_path_index: The index of the next image to upgrade to.
            known_ha_members: Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If serial is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_device_upgrade.put(
            ...     serial=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "serial": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_device_upgrade.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            ha_reboot_controller=ha_reboot_controller,
            next_path_index=next_path_index,
            known_ha_members=known_ha_members,
            initial_version=initial_version,
            starter_admin=starter_admin,
            serial=serial,
            timing=timing,
            maximum_minutes=maximum_minutes,
            time=time,
            setup_time=setup_time,
            upgrade_path=upgrade_path,
            device_type=device_type,
            allow_download=allow_download,
            failure_reason=failure_reason,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.device_upgrade import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/device_upgrade",
            )
        
        serial_value = payload_data.get("serial")
        if not serial_value:
            raise ValueError("serial is required for PUT")
        endpoint = "/system/device-upgrade/" + str(serial_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: Literal["disabled", "initialized", "downloading", "device-disconnected", "ready", "coordinating", "staging", "final-check", "upgrade-devices", "cancelled", "confirmed", "done", "failed"] | None = None,
        ha_reboot_controller: str | None = None,
        next_path_index: int | None = None,
        known_ha_members: str | list | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        serial: str | None = None,
        timing: Literal["immediate", "scheduled"] | None = None,
        maximum_minutes: int | None = None,
        time: str | None = None,
        setup_time: str | None = None,
        upgrade_path: str | None = None,
        device_type: Literal["fortigate", "fortiswitch", "fortiap", "fortiextender"] | None = None,
        allow_download: Literal["enable", "disable"] | None = None,
        failure_reason: Literal["none", "internal", "timeout", "device-type-unsupported", "download-failed", "device-missing", "version-unavailable", "staging-failed", "reboot-failed", "device-not-reconnected", "node-not-ready", "no-final-confirmation", "no-confirmation-query", "config-error-log-nonempty", "csf-tree-not-supported", "firmware-changed", "node-failed", "image-missing"] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/device_upgrade object.

        Independent upgrades for managed devices.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            vdom: Limit upgrade to this virtual domain (VDOM).
            status: Current status of the upgrade.
            ha_reboot_controller: Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.
            next_path_index: The index of the next image to upgrade to.
            known_ha_members: Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned serial.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_device_upgrade.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created serial: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = DeviceUpgrade.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_device_upgrade.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(DeviceUpgrade.required_fields()) }}
            
            Use DeviceUpgrade.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            ha_reboot_controller=ha_reboot_controller,
            next_path_index=next_path_index,
            known_ha_members=known_ha_members,
            initial_version=initial_version,
            starter_admin=starter_admin,
            serial=serial,
            timing=timing,
            maximum_minutes=maximum_minutes,
            time=time,
            setup_time=setup_time,
            upgrade_path=upgrade_path,
            device_type=device_type,
            allow_download=allow_download,
            failure_reason=failure_reason,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.device_upgrade import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/device_upgrade",
            )

        endpoint = "/system/device-upgrade"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        serial: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/device_upgrade object.

        Independent upgrades for managed devices.

        Args:
            serial: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If serial is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_device_upgrade.delete(serial=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not serial:
            raise ValueError("serial is required for DELETE")
        endpoint = "/system/device-upgrade/" + str(serial)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        serial: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/device_upgrade object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            serial: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_device_upgrade.exists(serial=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_device_upgrade.exists(serial=1):
            ...     fgt.api.cmdb.system_device_upgrade.delete(serial=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                serial=serial,
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
        Create or update system/device_upgrade object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (serial) in the payload.

        Args:
            payload_dict: Resource data including serial (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If serial is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "serial": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_device_upgrade.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_device_upgrade.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("serial")
        if not mkey_value:
            raise ValueError("serial is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(serial=mkey_value, vdom=vdom):
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
        serial: str,
        action: Literal["before", "after"],
        reference_serial: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/device_upgrade object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            serial: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_serial: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_device_upgrade.move(
            ...     serial=100,
            ...     action="before",
            ...     reference_serial=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/device-upgrade",
            params={
                "serial": serial,
                "action": "move",
                action: reference_serial,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        serial: str,
        new_serial: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/device_upgrade object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            serial: Identifier of object to clone
            new_serial: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_device_upgrade.clone(
            ...     serial=1,
            ...     new_serial=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/device-upgrade",
            params={
                "serial": serial,
                "new_serial": new_serial,
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
        serial: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/device_upgrade object exists.
        
        Args:
            serial: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_device_upgrade.exists(serial=1):
            ...     fgt.api.cmdb.system_device_upgrade.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                serial=serial,
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

