"""
FortiOS CMDB - Log disk_setting

Configuration endpoint for managing cmdb log/disk_setting objects.

API Endpoints:
    GET    /cmdb/log/disk_setting
    POST   /cmdb/log/disk_setting
    PUT    /cmdb/log/disk_setting/{identifier}
    DELETE /cmdb/log/disk_setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_disk_setting.get()

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


class DiskSetting:
    """DiskSetting Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize DiskSetting endpoint."""
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
        Retrieve log/disk_setting configuration.

        Settings for local disk logging.

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
            >>> # Get all log/disk_setting objects
            >>> result = fgt.api.cmdb.log_disk_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_disk_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_disk_setting.get(action="schema")

        See Also:
            - post(): Create new log/disk_setting object
            - put(): Update existing log/disk_setting object
            - delete(): Remove log/disk_setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log.disk/setting/{name}"
        else:
            endpoint = "/log.disk/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        ips_archive: str | None = None,
        max_log_file_size: int | None = None,
        max_policy_packet_capture_size: int | None = None,
        roll_schedule: str | None = None,
        roll_day: str | None = None,
        roll_time: str | None = None,
        diskfull: str | None = None,
        log_quota: int | None = None,
        dlp_archive_quota: int | None = None,
        report_quota: int | None = None,
        maximum_log_age: int | None = None,
        upload: str | None = None,
        upload_destination: str | None = None,
        uploadip: str | None = None,
        uploadport: int | None = None,
        source_ip: str | None = None,
        uploaduser: str | None = None,
        uploadpass: Any | None = None,
        uploaddir: str | None = None,
        uploadtype: str | None = None,
        uploadsched: str | None = None,
        uploadtime: str | None = None,
        upload_delete_files: str | None = None,
        upload_ssl_conn: str | None = None,
        full_first_warning_threshold: int | None = None,
        full_second_warning_threshold: int | None = None,
        full_final_warning_threshold: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/disk_setting object.

        Settings for local disk logging.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable local disk logging.
            ips_archive: Enable/disable IPS packet archiving to the local disk.
            max_log_file_size: Maximum log file size before rolling (1 - 100 Mbytes).
            max_policy_packet_capture_size: Maximum size of policy sniffer in MB (0 means unlimited).
            roll_schedule: Frequency to check log file for rolling.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_disk_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_disk_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            ips_archive=ips_archive,
            max_log_file_size=max_log_file_size,
            max_policy_packet_capture_size=max_policy_packet_capture_size,
            roll_schedule=roll_schedule,
            roll_day=roll_day,
            roll_time=roll_time,
            diskfull=diskfull,
            log_quota=log_quota,
            dlp_archive_quota=dlp_archive_quota,
            report_quota=report_quota,
            maximum_log_age=maximum_log_age,
            upload=upload,
            upload_destination=upload_destination,
            uploadip=uploadip,
            uploadport=uploadport,
            source_ip=source_ip,
            uploaduser=uploaduser,
            uploadpass=uploadpass,
            uploaddir=uploaddir,
            uploadtype=uploadtype,
            uploadsched=uploadsched,
            uploadtime=uploadtime,
            upload_delete_files=upload_delete_files,
            upload_ssl_conn=upload_ssl_conn,
            full_first_warning_threshold=full_first_warning_threshold,
            full_second_warning_threshold=full_second_warning_threshold,
            full_final_warning_threshold=full_final_warning_threshold,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.disk_setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/disk_setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log.disk/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        ips_archive: str | None = None,
        max_log_file_size: int | None = None,
        max_policy_packet_capture_size: int | None = None,
        roll_schedule: str | None = None,
        roll_day: str | None = None,
        roll_time: str | None = None,
        diskfull: str | None = None,
        log_quota: int | None = None,
        dlp_archive_quota: int | None = None,
        report_quota: int | None = None,
        maximum_log_age: int | None = None,
        upload: str | None = None,
        upload_destination: str | None = None,
        uploadip: str | None = None,
        uploadport: int | None = None,
        source_ip: str | None = None,
        uploaduser: str | None = None,
        uploadpass: Any | None = None,
        uploaddir: str | None = None,
        uploadtype: str | None = None,
        uploadsched: str | None = None,
        uploadtime: str | None = None,
        upload_delete_files: str | None = None,
        upload_ssl_conn: str | None = None,
        full_first_warning_threshold: int | None = None,
        full_second_warning_threshold: int | None = None,
        full_final_warning_threshold: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new log/disk_setting object.

        Settings for local disk logging.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            status: Enable/disable local disk logging.
            ips_archive: Enable/disable IPS packet archiving to the local disk.
            max_log_file_size: Maximum log file size before rolling (1 - 100 Mbytes).
            max_policy_packet_capture_size: Maximum size of policy sniffer in MB (0 means unlimited).
            roll_schedule: Frequency to check log file for rolling.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned identifier.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.log_disk_setting.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created object: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = DiskSetting.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.log_disk_setting.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(DiskSetting.required_fields()) }}
            
            Use DiskSetting.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            ips_archive=ips_archive,
            max_log_file_size=max_log_file_size,
            max_policy_packet_capture_size=max_policy_packet_capture_size,
            roll_schedule=roll_schedule,
            roll_day=roll_day,
            roll_time=roll_time,
            diskfull=diskfull,
            log_quota=log_quota,
            dlp_archive_quota=dlp_archive_quota,
            report_quota=report_quota,
            maximum_log_age=maximum_log_age,
            upload=upload,
            upload_destination=upload_destination,
            uploadip=uploadip,
            uploadport=uploadport,
            source_ip=source_ip,
            uploaduser=uploaduser,
            uploadpass=uploadpass,
            uploaddir=uploaddir,
            uploadtype=uploadtype,
            uploadsched=uploadsched,
            uploadtime=uploadtime,
            upload_delete_files=upload_delete_files,
            upload_ssl_conn=upload_ssl_conn,
            full_first_warning_threshold=full_first_warning_threshold,
            full_second_warning_threshold=full_second_warning_threshold,
            full_final_warning_threshold=full_final_warning_threshold,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.disk_setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/disk_setting",
            )

        endpoint = "/log.disk/setting"
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
        Delete log/disk_setting object.

        Settings for local disk logging.

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
            >>> result = fgt.api.cmdb.log_disk_setting.delete(name="object-to-delete")
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = f"/log.disk/setting/{name}"

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if log/disk_setting object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.log_disk_setting.exists(name="my-object"):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.log_disk_setting.exists(name="old-object"):
            ...     fgt.api.cmdb.log_disk_setting.delete(name="old-object")

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
        Create or update log/disk_setting object (intelligent operation).

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
            >>> result = fgt.api.cmdb.log_disk_setting.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.log_disk_setting.set(payload_dict=obj_data)
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
            >>> print(DiskSetting.help())
            
            >>> # Get field information
            >>> print(DiskSetting.help("status"))
        """
        from ._helpers.disk_setting import (
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
            >>> fields = DiskSetting.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = DiskSetting.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.disk_setting import get_all_fields, get_field_metadata

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
            >>> info = DiskSetting.field_info("status")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.disk_setting import get_field_metadata

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
            >>> is_valid, error = DiskSetting.validate_field("status", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.disk_setting import validate_field_value

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
            >>> required = DiskSetting.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.disk_setting import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = DiskSetting.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.disk_setting import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = DiskSetting.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.disk_setting import get_schema_info

        return get_schema_info()
