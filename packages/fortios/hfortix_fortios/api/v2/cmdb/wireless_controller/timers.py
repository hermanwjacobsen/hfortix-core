"""
FortiOS CMDB - Wireless_controller timers

Configuration endpoint for managing cmdb wireless_controller/timers objects.

API Endpoints:
    GET    /cmdb/wireless_controller/timers
    POST   /cmdb/wireless_controller/timers
    PUT    /cmdb/wireless_controller/timers/{identifier}
    DELETE /cmdb/wireless_controller/timers/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_timers.get()

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


class Timers:
    """Timers Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Timers endpoint."""
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
        Retrieve wireless_controller/timers configuration.

        Configure CAPWAP timers.

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
            >>> # Get all wireless_controller/timers objects
            >>> result = fgt.api.cmdb.wireless_controller_timers.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_timers.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_timers.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/timers object
            - put(): Update existing wireless_controller/timers object
            - delete(): Remove wireless_controller/timers object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wireless-controller/timers/{name}"
        else:
            endpoint = "/wireless-controller/timers"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        echo_interval: int | None = None,
        nat_session_keep_alive: int | None = None,
        discovery_interval: int | None = None,
        client_idle_timeout: int | None = None,
        client_idle_rehome_timeout: int | None = None,
        auth_timeout: int | None = None,
        rogue_ap_log: int | None = None,
        fake_ap_log: int | None = None,
        sta_offline_cleanup: int | None = None,
        sta_offline_ip2mac_cleanup: int | None = None,
        sta_cap_cleanup: int | None = None,
        rogue_ap_cleanup: int | None = None,
        rogue_sta_cleanup: int | None = None,
        wids_entry_cleanup: int | None = None,
        ble_device_cleanup: int | None = None,
        sta_stats_interval: int | None = None,
        vap_stats_interval: int | None = None,
        radio_stats_interval: int | None = None,
        sta_capability_interval: int | None = None,
        sta_locate_timer: int | None = None,
        ipsec_intf_cleanup: int | None = None,
        ble_scan_report_intv: int | None = None,
        drma_interval: int | None = None,
        ap_reboot_wait_interval1: int | None = None,
        ap_reboot_wait_time: str | None = None,
        ap_reboot_wait_interval2: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/timers object.

        Configure CAPWAP timers.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            echo_interval: Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).
            nat_session_keep_alive: Maximal time in seconds between control requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec, default = 0).
            discovery_interval: Time between discovery requests (2 - 180 sec, default = 5).
            client_idle_timeout: Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).
            client_idle_rehome_timeout: Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec, default = 20, 0 for no timeout).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_timers.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_timers.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            echo_interval=echo_interval,
            nat_session_keep_alive=nat_session_keep_alive,
            discovery_interval=discovery_interval,
            client_idle_timeout=client_idle_timeout,
            client_idle_rehome_timeout=client_idle_rehome_timeout,
            auth_timeout=auth_timeout,
            rogue_ap_log=rogue_ap_log,
            fake_ap_log=fake_ap_log,
            sta_offline_cleanup=sta_offline_cleanup,
            sta_offline_ip2mac_cleanup=sta_offline_ip2mac_cleanup,
            sta_cap_cleanup=sta_cap_cleanup,
            rogue_ap_cleanup=rogue_ap_cleanup,
            rogue_sta_cleanup=rogue_sta_cleanup,
            wids_entry_cleanup=wids_entry_cleanup,
            ble_device_cleanup=ble_device_cleanup,
            sta_stats_interval=sta_stats_interval,
            vap_stats_interval=vap_stats_interval,
            radio_stats_interval=radio_stats_interval,
            sta_capability_interval=sta_capability_interval,
            sta_locate_timer=sta_locate_timer,
            ipsec_intf_cleanup=ipsec_intf_cleanup,
            ble_scan_report_intv=ble_scan_report_intv,
            drma_interval=drma_interval,
            ap_reboot_wait_interval1=ap_reboot_wait_interval1,
            ap_reboot_wait_time=ap_reboot_wait_time,
            ap_reboot_wait_interval2=ap_reboot_wait_interval2,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.timers import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/timers",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/wireless-controller/timers/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        echo_interval: int | None = None,
        nat_session_keep_alive: int | None = None,
        discovery_interval: int | None = None,
        client_idle_timeout: int | None = None,
        client_idle_rehome_timeout: int | None = None,
        auth_timeout: int | None = None,
        rogue_ap_log: int | None = None,
        fake_ap_log: int | None = None,
        sta_offline_cleanup: int | None = None,
        sta_offline_ip2mac_cleanup: int | None = None,
        sta_cap_cleanup: int | None = None,
        rogue_ap_cleanup: int | None = None,
        rogue_sta_cleanup: int | None = None,
        wids_entry_cleanup: int | None = None,
        ble_device_cleanup: int | None = None,
        sta_stats_interval: int | None = None,
        vap_stats_interval: int | None = None,
        radio_stats_interval: int | None = None,
        sta_capability_interval: int | None = None,
        sta_locate_timer: int | None = None,
        ipsec_intf_cleanup: int | None = None,
        ble_scan_report_intv: int | None = None,
        drma_interval: int | None = None,
        ap_reboot_wait_interval1: int | None = None,
        ap_reboot_wait_time: str | None = None,
        ap_reboot_wait_interval2: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/timers object.

        Configure CAPWAP timers.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            echo_interval: Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).
            nat_session_keep_alive: Maximal time in seconds between control requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec, default = 0).
            discovery_interval: Time between discovery requests (2 - 180 sec, default = 5).
            client_idle_timeout: Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).
            client_idle_rehome_timeout: Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec, default = 20, 0 for no timeout).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned identifier.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_timers.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created object: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Timers.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_timers.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Timers.required_fields()) }}
            
            Use Timers.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            echo_interval=echo_interval,
            nat_session_keep_alive=nat_session_keep_alive,
            discovery_interval=discovery_interval,
            client_idle_timeout=client_idle_timeout,
            client_idle_rehome_timeout=client_idle_rehome_timeout,
            auth_timeout=auth_timeout,
            rogue_ap_log=rogue_ap_log,
            fake_ap_log=fake_ap_log,
            sta_offline_cleanup=sta_offline_cleanup,
            sta_offline_ip2mac_cleanup=sta_offline_ip2mac_cleanup,
            sta_cap_cleanup=sta_cap_cleanup,
            rogue_ap_cleanup=rogue_ap_cleanup,
            rogue_sta_cleanup=rogue_sta_cleanup,
            wids_entry_cleanup=wids_entry_cleanup,
            ble_device_cleanup=ble_device_cleanup,
            sta_stats_interval=sta_stats_interval,
            vap_stats_interval=vap_stats_interval,
            radio_stats_interval=radio_stats_interval,
            sta_capability_interval=sta_capability_interval,
            sta_locate_timer=sta_locate_timer,
            ipsec_intf_cleanup=ipsec_intf_cleanup,
            ble_scan_report_intv=ble_scan_report_intv,
            drma_interval=drma_interval,
            ap_reboot_wait_interval1=ap_reboot_wait_interval1,
            ap_reboot_wait_time=ap_reboot_wait_time,
            ap_reboot_wait_interval2=ap_reboot_wait_interval2,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.timers import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/timers",
            )

        endpoint = "/wireless-controller/timers"
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
        Delete wireless_controller/timers object.

        Configure CAPWAP timers.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.wireless_controller_timers.delete(name="object-to-delete")
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = f"/wireless-controller/timers/{name}"

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/timers object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_timers.exists(name="my-object"):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_timers.exists(name="old-object"):
            ...     fgt.api.cmdb.wireless_controller_timers.delete(name="old-object")

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
        Create or update wireless_controller/timers object (intelligent operation).

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
            ...     "name": "my-object",
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_timers.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_timers.set(payload_dict=obj_data)
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

    # ========================================================================
    # Metadata Helper Methods
    # Provide easy access to schema metadata without separate imports
    # ========================================================================

    @staticmethod
    def help(field_name: str | None = None) -> str:
        """
        Get help text for endpoint or specific field.

        Args:
            field_name: Optional field name to get help for. If None, shows endpoint help.

        Returns:
            Formatted help text

        Examples:
            >>> # Get endpoint information
            >>> print(Timers.help())
            
            >>> # Get field information
            >>> print(Timers.help("echo-interval"))
        """
        from ._helpers.timers import (
            get_schema_info,
            get_field_metadata,
        )

        if field_name is None:
            # Endpoint help
            info = get_schema_info()
            lines = [
                f"Endpoint: {info['endpoint']}",
                f"Category: {info['category']}",
                f"Help: {info.get('help', 'N/A')}",
                "",
                f"Total Fields: {info['total_fields']}",
                f"Required Fields: {info['required_fields_count']}",
                f"Fields with Defaults: {info['fields_with_defaults_count']}",
            ]
            if 'mkey' in info:
                lines.append(f"\nPrimary Key: {info['mkey']} ({info['mkey_type']})")
            return "\n".join(lines)
        
        # Field help
        meta = get_field_metadata(field_name)
        if meta is None:
            return f"Unknown field: {field_name}"

        lines = [
            f"Field: {meta['name']}",
            f"Type: {meta['type']}",
        ]
        if 'description' in meta:
            lines.append(f"Description: {meta['description']}")
        lines.append(f"Required: {'Yes' if meta.get('required', False) else 'No'}")
        if 'default' in meta:
            lines.append(f"Default: {meta['default']}")
        if 'options' in meta:
            lines.append(f"Options: {', '.join(meta['options'])}")
        if 'constraints' in meta:
            constraints = meta['constraints']
            if 'min' in constraints or 'max' in constraints:
                min_val = constraints.get('min', '?')
                max_val = constraints.get('max', '?')
                lines.append(f"Range: {min_val} - {max_val}")
            if 'max_length' in constraints:
                lines.append(f"Max Length: {constraints['max_length']}")

        return "\n".join(lines)

    @staticmethod
    def fields(detailed: bool = False) -> Union[list[str], dict[str, dict]]:
        """
        Get list of all field names or detailed field information.

        Args:
            detailed: If True, return dict with field metadata

        Returns:
            List of field names or dict of field metadata

        Examples:
            >>> # Simple list
            >>> fields = Timers.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Timers.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.timers import get_all_fields, get_field_metadata

        field_names = get_all_fields()

        if not detailed:
            return field_names

        # Build detailed dict
        detailed_fields = {}
        for fname in field_names:
            meta = get_field_metadata(fname)
            if meta:
                detailed_fields[fname] = meta

        return detailed_fields

    @staticmethod
    def field_info(field_name: str) -> dict[str, Any] | None:
        """
        Get complete metadata for a specific field.

        Args:
            field_name: Name of the field

        Returns:
            Field metadata dict or None if field doesn't exist

        Examples:
            >>> info = Timers.field_info("echo-interval")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.timers import get_field_metadata

        return get_field_metadata(field_name)

    @staticmethod
    def validate_field(field_name: str, value: Any) -> tuple[bool, str | None]:
        """
        Validate a field value against its constraints.

        Args:
            field_name: Name of the field
            value: Value to validate

        Returns:
            Tuple of (is_valid, error_message)

        Examples:
            >>> is_valid, error = Timers.validate_field("echo-interval", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.timers import validate_field_value

        return validate_field_value(field_name, value)

    @staticmethod
    def required_fields() -> list[str]:
        """
        Get list of required field names.

        Note: Due to FortiOS schema quirks, some fields may be conditionally required.
        Always test with the actual API for authoritative requirements.

        Returns:
            List of required field names

        Examples:
            >>> required = Timers.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.timers import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Timers.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.timers import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Timers.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.timers import get_schema_info

        return get_schema_info()
