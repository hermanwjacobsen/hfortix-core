"""
FortiOS CMDB - System resource_limits

Configuration endpoint for managing cmdb system/resource_limits objects.

API Endpoints:
    GET    /cmdb/system/resource_limits
    POST   /cmdb/system/resource_limits
    PUT    /cmdb/system/resource_limits/{identifier}
    DELETE /cmdb/system/resource_limits/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_resource_limits.get()

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


class ResourceLimits:
    """ResourceLimits Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize ResourceLimits endpoint."""
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
        Retrieve system/resource_limits configuration.

        Configure resource limits.

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
            >>> # Get all system/resource_limits objects
            >>> result = fgt.api.cmdb.system_resource_limits.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_resource_limits.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_resource_limits.get(action="schema")

        See Also:
            - post(): Create new system/resource_limits object
            - put(): Update existing system/resource_limits object
            - delete(): Remove system/resource_limits object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/resource-limits/{name}"
        else:
            endpoint = "/system/resource-limits"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        session: int | None = None,
        ipsec_phase1: int | None = None,
        ipsec_phase2: int | None = None,
        ipsec_phase1_interface: int | None = None,
        ipsec_phase2_interface: int | None = None,
        dialup_tunnel: int | None = None,
        firewall_policy: int | None = None,
        firewall_address: int | None = None,
        firewall_addrgrp: int | None = None,
        custom_service: int | None = None,
        service_group: int | None = None,
        onetime_schedule: int | None = None,
        recurring_schedule: int | None = None,
        user: int | None = None,
        user_group: int | None = None,
        sslvpn: int | None = None,
        proxy: int | None = None,
        log_disk_quota: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/resource_limits object.

        Configure resource limits.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            session: Maximum number of sessions.
            ipsec_phase1: Maximum number of VPN IPsec phase1 tunnels.
            ipsec_phase2: Maximum number of VPN IPsec phase2 tunnels.
            ipsec_phase1_interface: Maximum number of VPN IPsec phase1 interface tunnels.
            ipsec_phase2_interface: Maximum number of VPN IPsec phase2 interface tunnels.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_resource_limits.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_resource_limits.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            session=session,
            ipsec_phase1=ipsec_phase1,
            ipsec_phase2=ipsec_phase2,
            ipsec_phase1_interface=ipsec_phase1_interface,
            ipsec_phase2_interface=ipsec_phase2_interface,
            dialup_tunnel=dialup_tunnel,
            firewall_policy=firewall_policy,
            firewall_address=firewall_address,
            firewall_addrgrp=firewall_addrgrp,
            custom_service=custom_service,
            service_group=service_group,
            onetime_schedule=onetime_schedule,
            recurring_schedule=recurring_schedule,
            user=user,
            user_group=user_group,
            sslvpn=sslvpn,
            proxy=proxy,
            log_disk_quota=log_disk_quota,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.resource_limits import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/resource_limits",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/resource-limits/{name_value}"

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
            >>> print(ResourceLimits.help())
            
            >>> # Get field information
            >>> print(ResourceLimits.help("session"))
        """
        from ._helpers.resource_limits import (
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
            >>> fields = ResourceLimits.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = ResourceLimits.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.resource_limits import get_all_fields, get_field_metadata

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
            >>> info = ResourceLimits.field_info("session")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.resource_limits import get_field_metadata

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
            >>> is_valid, error = ResourceLimits.validate_field("session", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.resource_limits import validate_field_value

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
            >>> required = ResourceLimits.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.resource_limits import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = ResourceLimits.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.resource_limits import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = ResourceLimits.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.resource_limits import get_schema_info

        return get_schema_info()
