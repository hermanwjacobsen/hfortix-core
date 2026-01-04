"""
FortiOS CMDB - Switch_controller initial_config vlans

Configuration endpoint for managing cmdb switch_controller/initial_config/vlans objects.

API Endpoints:
    GET    /cmdb/switch_controller/initial_config/vlans
    POST   /cmdb/switch_controller/initial_config/vlans
    PUT    /cmdb/switch_controller/initial_config/vlans/{identifier}
    DELETE /cmdb/switch_controller/initial_config/vlans/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_initial_config_vlans.get()

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


class Vlans:
    """Vlans Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vlans endpoint."""
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
        Retrieve switch_controller/initial_config/vlans configuration.

        Configure initial template for auto-generated VLAN interfaces.

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
            >>> # Get all switch_controller/initial_config/vlans objects
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_initial_config_vlans.get(action="schema")

        See Also:
            - post(): Create new switch_controller/initial_config/vlans object
            - put(): Update existing switch_controller/initial_config/vlans object
            - delete(): Remove switch_controller/initial_config/vlans object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller.initial-config/vlans/{name}"
        else:
            endpoint = "/switch-controller.initial-config/vlans"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        optional_vlans: str | None = None,
        default_vlan: str | None = None,
        quarantine: str | None = None,
        rspan: str | None = None,
        voice: str | None = None,
        video: str | None = None,
        nac: str | None = None,
        nac_segment: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/initial_config/vlans object.

        Configure initial template for auto-generated VLAN interfaces.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            optional_vlans: Auto-generate pre-configured VLANs upon switch discovery.
            default_vlan: Default VLAN (native) assigned to all switch ports upon discovery.
            quarantine: VLAN for quarantined traffic.
            rspan: VLAN for RSPAN/ERSPAN mirrored traffic.
            voice: VLAN dedicated for voice devices.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            optional_vlans=optional_vlans,
            default_vlan=default_vlan,
            quarantine=quarantine,
            rspan=rspan,
            voice=voice,
            video=video,
            nac=nac,
            nac_segment=nac_segment,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vlans import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/initial_config/vlans",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller.initial-config/vlans/{name_value}"

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
            >>> print(Vlans.help())
            
            >>> # Get field information
            >>> print(Vlans.help("optional-vlans"))
        """
        from ._helpers.vlans import (
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
            >>> fields = Vlans.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Vlans.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.vlans import get_all_fields, get_field_metadata

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
            >>> info = Vlans.field_info("optional-vlans")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.vlans import get_field_metadata

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
            >>> is_valid, error = Vlans.validate_field("optional-vlans", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.vlans import validate_field_value

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
            >>> required = Vlans.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.vlans import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Vlans.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.vlans import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Vlans.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.vlans import get_schema_info

        return get_schema_info()
