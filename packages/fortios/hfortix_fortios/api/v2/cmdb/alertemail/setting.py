"""
FortiOS CMDB - Alertemail setting

Configuration endpoint for managing cmdb alertemail/setting objects.

API Endpoints:
    GET    /cmdb/alertemail/setting
    POST   /cmdb/alertemail/setting
    PUT    /cmdb/alertemail/setting/{identifier}
    DELETE /cmdb/alertemail/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.alertemail_setting.get()

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


class Setting:
    """Setting Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Setting endpoint."""
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
        Retrieve alertemail/setting configuration.

        Configure alert email settings.

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
            >>> # Get all alertemail/setting objects
            >>> result = fgt.api.cmdb.alertemail_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.alertemail_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.alertemail_setting.get(action="schema")

        See Also:
            - post(): Create new alertemail/setting object
            - put(): Update existing alertemail/setting object
            - delete(): Remove alertemail/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/alertemail/setting/{name}"
        else:
            endpoint = "/alertemail/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        username: str | None = None,
        mailto1: str | None = None,
        mailto2: str | None = None,
        mailto3: str | None = None,
        filter_mode: str | None = None,
        email_interval: int | None = None,
        IPS_logs: str | None = None,
        firewall_authentication_failure_logs: str | None = None,
        HA_logs: str | None = None,
        IPsec_errors_logs: str | None = None,
        FDS_update_logs: str | None = None,
        PPP_errors_logs: str | None = None,
        sslvpn_authentication_errors_logs: str | None = None,
        antivirus_logs: str | None = None,
        webfilter_logs: str | None = None,
        configuration_changes_logs: str | None = None,
        violation_traffic_logs: str | None = None,
        admin_login_logs: str | None = None,
        FDS_license_expiring_warning: str | None = None,
        log_disk_usage_warning: str | None = None,
        fortiguard_log_quota_warning: str | None = None,
        amc_interface_bypass_mode: str | None = None,
        FIPS_CC_errors: str | None = None,
        FSSO_disconnect_logs: str | None = None,
        ssh_logs: str | None = None,
        local_disk_usage: int | None = None,
        emergency_interval: int | None = None,
        alert_interval: int | None = None,
        critical_interval: int | None = None,
        error_interval: int | None = None,
        warning_interval: int | None = None,
        notification_interval: int | None = None,
        information_interval: int | None = None,
        debug_interval: int | None = None,
        severity: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing alertemail/setting object.

        Configure alert email settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            username: Name that appears in the From: field of alert emails (max. 63 characters).
            mailto1: Email address to send alert email to (usually a system administrator) (max. 63 characters).
            mailto2: Optional second email address to send alert email to (max. 63 characters).
            mailto3: Optional third email address to send alert email to (max. 63 characters).
            filter_mode: How to filter log messages that are sent to alert emails.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.alertemail_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.alertemail_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            username=username,
            mailto1=mailto1,
            mailto2=mailto2,
            mailto3=mailto3,
            filter_mode=filter_mode,
            email_interval=email_interval,
            IPS_logs=IPS_logs,
            firewall_authentication_failure_logs=firewall_authentication_failure_logs,
            HA_logs=HA_logs,
            IPsec_errors_logs=IPsec_errors_logs,
            FDS_update_logs=FDS_update_logs,
            PPP_errors_logs=PPP_errors_logs,
            sslvpn_authentication_errors_logs=sslvpn_authentication_errors_logs,
            antivirus_logs=antivirus_logs,
            webfilter_logs=webfilter_logs,
            configuration_changes_logs=configuration_changes_logs,
            violation_traffic_logs=violation_traffic_logs,
            admin_login_logs=admin_login_logs,
            FDS_license_expiring_warning=FDS_license_expiring_warning,
            log_disk_usage_warning=log_disk_usage_warning,
            fortiguard_log_quota_warning=fortiguard_log_quota_warning,
            amc_interface_bypass_mode=amc_interface_bypass_mode,
            FIPS_CC_errors=FIPS_CC_errors,
            FSSO_disconnect_logs=FSSO_disconnect_logs,
            ssh_logs=ssh_logs,
            local_disk_usage=local_disk_usage,
            emergency_interval=emergency_interval,
            alert_interval=alert_interval,
            critical_interval=critical_interval,
            error_interval=error_interval,
            warning_interval=warning_interval,
            notification_interval=notification_interval,
            information_interval=information_interval,
            debug_interval=debug_interval,
            severity=severity,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/alertemail/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/alertemail/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        username: str | None = None,
        mailto1: str | None = None,
        mailto2: str | None = None,
        mailto3: str | None = None,
        filter_mode: str | None = None,
        email_interval: int | None = None,
        IPS_logs: str | None = None,
        firewall_authentication_failure_logs: str | None = None,
        HA_logs: str | None = None,
        IPsec_errors_logs: str | None = None,
        FDS_update_logs: str | None = None,
        PPP_errors_logs: str | None = None,
        sslvpn_authentication_errors_logs: str | None = None,
        antivirus_logs: str | None = None,
        webfilter_logs: str | None = None,
        configuration_changes_logs: str | None = None,
        violation_traffic_logs: str | None = None,
        admin_login_logs: str | None = None,
        FDS_license_expiring_warning: str | None = None,
        log_disk_usage_warning: str | None = None,
        fortiguard_log_quota_warning: str | None = None,
        amc_interface_bypass_mode: str | None = None,
        FIPS_CC_errors: str | None = None,
        FSSO_disconnect_logs: str | None = None,
        ssh_logs: str | None = None,
        local_disk_usage: int | None = None,
        emergency_interval: int | None = None,
        alert_interval: int | None = None,
        critical_interval: int | None = None,
        error_interval: int | None = None,
        warning_interval: int | None = None,
        notification_interval: int | None = None,
        information_interval: int | None = None,
        debug_interval: int | None = None,
        severity: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new alertemail/setting object.

        Configure alert email settings.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            username: Name that appears in the From: field of alert emails (max. 63 characters).
            mailto1: Email address to send alert email to (usually a system administrator) (max. 63 characters).
            mailto2: Optional second email address to send alert email to (max. 63 characters).
            mailto3: Optional third email address to send alert email to (max. 63 characters).
            filter_mode: How to filter log messages that are sent to alert emails.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned identifier.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.alertemail_setting.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created object: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Setting.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.alertemail_setting.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Setting.required_fields()) }}
            
            Use Setting.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            username=username,
            mailto1=mailto1,
            mailto2=mailto2,
            mailto3=mailto3,
            filter_mode=filter_mode,
            email_interval=email_interval,
            IPS_logs=IPS_logs,
            firewall_authentication_failure_logs=firewall_authentication_failure_logs,
            HA_logs=HA_logs,
            IPsec_errors_logs=IPsec_errors_logs,
            FDS_update_logs=FDS_update_logs,
            PPP_errors_logs=PPP_errors_logs,
            sslvpn_authentication_errors_logs=sslvpn_authentication_errors_logs,
            antivirus_logs=antivirus_logs,
            webfilter_logs=webfilter_logs,
            configuration_changes_logs=configuration_changes_logs,
            violation_traffic_logs=violation_traffic_logs,
            admin_login_logs=admin_login_logs,
            FDS_license_expiring_warning=FDS_license_expiring_warning,
            log_disk_usage_warning=log_disk_usage_warning,
            fortiguard_log_quota_warning=fortiguard_log_quota_warning,
            amc_interface_bypass_mode=amc_interface_bypass_mode,
            FIPS_CC_errors=FIPS_CC_errors,
            FSSO_disconnect_logs=FSSO_disconnect_logs,
            ssh_logs=ssh_logs,
            local_disk_usage=local_disk_usage,
            emergency_interval=emergency_interval,
            alert_interval=alert_interval,
            critical_interval=critical_interval,
            error_interval=error_interval,
            warning_interval=warning_interval,
            notification_interval=notification_interval,
            information_interval=information_interval,
            debug_interval=debug_interval,
            severity=severity,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/alertemail/setting",
            )

        endpoint = "/alertemail/setting"
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
        Delete alertemail/setting object.

        Configure alert email settings.

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
            >>> result = fgt.api.cmdb.alertemail_setting.delete(name="object-to-delete")
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = f"/alertemail/setting/{name}"

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if alertemail/setting object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.alertemail_setting.exists(name="my-object"):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.alertemail_setting.exists(name="old-object"):
            ...     fgt.api.cmdb.alertemail_setting.delete(name="old-object")

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
        Create or update alertemail/setting object (intelligent operation).

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
            >>> result = fgt.api.cmdb.alertemail_setting.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.alertemail_setting.set(payload_dict=obj_data)
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
            >>> print(Setting.help())
            
            >>> # Get field information
            >>> print(Setting.help("username"))
        """
        from ._helpers.setting import (
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
            >>> fields = Setting.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Setting.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.setting import get_all_fields, get_field_metadata

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
            >>> info = Setting.field_info("username")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.setting import get_field_metadata

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
            >>> is_valid, error = Setting.validate_field("username", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.setting import validate_field_value

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
            >>> required = Setting.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.setting import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Setting.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.setting import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Setting.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.setting import get_schema_info

        return get_schema_info()
