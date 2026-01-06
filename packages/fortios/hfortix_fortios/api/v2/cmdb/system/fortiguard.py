"""
FortiOS CMDB - System fortiguard

Configuration endpoint for managing cmdb system/fortiguard objects.

API Endpoints:
    GET    /cmdb/system/fortiguard
    POST   /cmdb/system/fortiguard
    PUT    /cmdb/system/fortiguard/{identifier}
    DELETE /cmdb/system/fortiguard/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_fortiguard.get()

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


class Fortiguard:
    """Fortiguard Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Fortiguard endpoint."""
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
        Retrieve system/fortiguard configuration.

        Configure FortiGuard services.

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
            >>> # Get all system/fortiguard objects
            >>> result = fgt.api.cmdb.system_fortiguard.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_fortiguard.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_fortiguard.get(action="schema")

        See Also:
            - post(): Create new system/fortiguard object
            - put(): Update existing system/fortiguard object
            - delete(): Remove system/fortiguard object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/fortiguard/{name}"
        else:
            endpoint = "/system/fortiguard"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        fortiguard_anycast: str | None = None,
        fortiguard_anycast_source: str | None = None,
        protocol: str | None = None,
        port: str | None = None,
        load_balance_servers: int | None = None,
        auto_join_forticloud: str | None = None,
        update_server_location: str | None = None,
        sandbox_region: str | None = None,
        sandbox_inline_scan: str | None = None,
        update_ffdb: str | None = None,
        update_uwdb: str | None = None,
        update_dldb: str | None = None,
        update_extdb: str | None = None,
        update_build_proxy: str | None = None,
        persistent_connection: str | None = None,
        auto_firmware_upgrade: str | None = None,
        auto_firmware_upgrade_day: str | list | None = None,
        auto_firmware_upgrade_delay: int | None = None,
        auto_firmware_upgrade_start_hour: int | None = None,
        auto_firmware_upgrade_end_hour: int | None = None,
        FDS_license_expiring_days: int | None = None,
        subscribe_update_notification: str | None = None,
        antispam_force_off: str | None = None,
        antispam_cache: str | None = None,
        antispam_cache_ttl: int | None = None,
        antispam_cache_mpermille: int | None = None,
        antispam_license: int | None = None,
        antispam_expiration: int | None = None,
        antispam_timeout: int | None = None,
        outbreak_prevention_force_off: str | None = None,
        outbreak_prevention_cache: str | None = None,
        outbreak_prevention_cache_ttl: int | None = None,
        outbreak_prevention_cache_mpermille: int | None = None,
        outbreak_prevention_license: int | None = None,
        outbreak_prevention_expiration: int | None = None,
        outbreak_prevention_timeout: int | None = None,
        webfilter_force_off: str | None = None,
        webfilter_cache: str | None = None,
        webfilter_cache_ttl: int | None = None,
        webfilter_license: int | None = None,
        webfilter_expiration: int | None = None,
        webfilter_timeout: int | None = None,
        sdns_server_ip: str | list | None = None,
        sdns_server_port: int | None = None,
        anycast_sdns_server_ip: str | None = None,
        anycast_sdns_server_port: int | None = None,
        sdns_options: str | list | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        proxy_server_ip: str | None = None,
        proxy_server_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: Any | None = None,
        ddns_server_ip: str | None = None,
        ddns_server_ip6: str | None = None,
        ddns_server_port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/fortiguard object.

        Configure FortiGuard services.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            fortiguard_anycast: Enable/disable use of FortiGuard's Anycast network.
            fortiguard_anycast_source: Configure which of Fortinet's servers to provide FortiGuard services in FortiGuard's anycast network. Default is Fortinet.
            protocol: Protocol used to communicate with the FortiGuard servers.
            port: Port used to communicate with the FortiGuard servers.
            load_balance_servers: Number of servers to alternate between as first FortiGuard option.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_fortiguard.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_fortiguard.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            fortiguard_anycast=fortiguard_anycast,
            fortiguard_anycast_source=fortiguard_anycast_source,
            protocol=protocol,
            port=port,
            load_balance_servers=load_balance_servers,
            auto_join_forticloud=auto_join_forticloud,
            update_server_location=update_server_location,
            sandbox_region=sandbox_region,
            sandbox_inline_scan=sandbox_inline_scan,
            update_ffdb=update_ffdb,
            update_uwdb=update_uwdb,
            update_dldb=update_dldb,
            update_extdb=update_extdb,
            update_build_proxy=update_build_proxy,
            persistent_connection=persistent_connection,
            auto_firmware_upgrade=auto_firmware_upgrade,
            auto_firmware_upgrade_day=auto_firmware_upgrade_day,
            auto_firmware_upgrade_delay=auto_firmware_upgrade_delay,
            auto_firmware_upgrade_start_hour=auto_firmware_upgrade_start_hour,
            auto_firmware_upgrade_end_hour=auto_firmware_upgrade_end_hour,
            FDS_license_expiring_days=FDS_license_expiring_days,
            subscribe_update_notification=subscribe_update_notification,
            antispam_force_off=antispam_force_off,
            antispam_cache=antispam_cache,
            antispam_cache_ttl=antispam_cache_ttl,
            antispam_cache_mpermille=antispam_cache_mpermille,
            antispam_license=antispam_license,
            antispam_expiration=antispam_expiration,
            antispam_timeout=antispam_timeout,
            outbreak_prevention_force_off=outbreak_prevention_force_off,
            outbreak_prevention_cache=outbreak_prevention_cache,
            outbreak_prevention_cache_ttl=outbreak_prevention_cache_ttl,
            outbreak_prevention_cache_mpermille=outbreak_prevention_cache_mpermille,
            outbreak_prevention_license=outbreak_prevention_license,
            outbreak_prevention_expiration=outbreak_prevention_expiration,
            outbreak_prevention_timeout=outbreak_prevention_timeout,
            webfilter_force_off=webfilter_force_off,
            webfilter_cache=webfilter_cache,
            webfilter_cache_ttl=webfilter_cache_ttl,
            webfilter_license=webfilter_license,
            webfilter_expiration=webfilter_expiration,
            webfilter_timeout=webfilter_timeout,
            sdns_server_ip=sdns_server_ip,
            sdns_server_port=sdns_server_port,
            anycast_sdns_server_ip=anycast_sdns_server_ip,
            anycast_sdns_server_port=anycast_sdns_server_port,
            sdns_options=sdns_options,
            source_ip=source_ip,
            source_ip6=source_ip6,
            proxy_server_ip=proxy_server_ip,
            proxy_server_port=proxy_server_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
            ddns_server_ip=ddns_server_ip,
            ddns_server_ip6=ddns_server_ip6,
            ddns_server_port=ddns_server_port,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fortiguard import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/fortiguard",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/fortiguard/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





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
            >>> print(Fortiguard.help())
            
            >>> # Get field information
            >>> print(Fortiguard.help("fortiguard-anycast"))
        """
        from ._helpers.fortiguard import (
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
            >>> fields = Fortiguard.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Fortiguard.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.fortiguard import get_all_fields, get_field_metadata

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
            >>> info = Fortiguard.field_info("fortiguard-anycast")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.fortiguard import get_field_metadata

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
            >>> is_valid, error = Fortiguard.validate_field("fortiguard-anycast", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.fortiguard import validate_field_value

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
            >>> required = Fortiguard.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.fortiguard import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Fortiguard.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.fortiguard import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Fortiguard.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.fortiguard import get_schema_info

        return get_schema_info()
