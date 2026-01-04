"""
FortiOS CMDB - Switch_controller flow_tracking

Configuration endpoint for managing cmdb switch_controller/flow_tracking objects.

API Endpoints:
    GET    /cmdb/switch_controller/flow_tracking
    POST   /cmdb/switch_controller/flow_tracking
    PUT    /cmdb/switch_controller/flow_tracking/{identifier}
    DELETE /cmdb/switch_controller/flow_tracking/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_flow_tracking.get()

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


class FlowTracking:
    """FlowTracking Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize FlowTracking endpoint."""
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
        Retrieve switch_controller/flow_tracking configuration.

        Configure FortiSwitch flow tracking and export via ipfix/netflow.

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
            >>> # Get all switch_controller/flow_tracking objects
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_flow_tracking.get(action="schema")

        See Also:
            - post(): Create new switch_controller/flow_tracking object
            - put(): Update existing switch_controller/flow_tracking object
            - delete(): Remove switch_controller/flow_tracking object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/flow-tracking/{name}"
        else:
            endpoint = "/switch-controller/flow-tracking"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        sample_mode: str | None = None,
        sample_rate: int | None = None,
        format: str | None = None,
        collectors: str | list | None = None,
        level: str | None = None,
        max_export_pkt_size: int | None = None,
        template_export_period: int | None = None,
        timeout_general: int | None = None,
        timeout_icmp: int | None = None,
        timeout_max: int | None = None,
        timeout_tcp: int | None = None,
        timeout_tcp_fin: int | None = None,
        timeout_tcp_rst: int | None = None,
        timeout_udp: int | None = None,
        aggregates: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/flow_tracking object.

        Configure FortiSwitch flow tracking and export via ipfix/netflow.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            sample_mode: Configure sample mode for the flow tracking.
            sample_rate: Configure sample rate for the perimeter and device-ingress sampling(0 - 99999).
            format: Configure flow tracking protocol.
            collectors: Configure collectors for the flow.
            level: Configure flow tracking level.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_flow_tracking.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            sample_mode=sample_mode,
            sample_rate=sample_rate,
            format=format,
            collectors=collectors,
            level=level,
            max_export_pkt_size=max_export_pkt_size,
            template_export_period=template_export_period,
            timeout_general=timeout_general,
            timeout_icmp=timeout_icmp,
            timeout_max=timeout_max,
            timeout_tcp=timeout_tcp,
            timeout_tcp_fin=timeout_tcp_fin,
            timeout_tcp_rst=timeout_tcp_rst,
            timeout_udp=timeout_udp,
            aggregates=aggregates,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.flow_tracking import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/flow_tracking",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/flow-tracking/{name_value}"

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
            >>> print(FlowTracking.help())
            
            >>> # Get field information
            >>> print(FlowTracking.help("sample-mode"))
        """
        from ._helpers.flow_tracking import (
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
            >>> fields = FlowTracking.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = FlowTracking.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.flow_tracking import get_all_fields, get_field_metadata

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
            >>> info = FlowTracking.field_info("sample-mode")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.flow_tracking import get_field_metadata

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
            >>> is_valid, error = FlowTracking.validate_field("sample-mode", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.flow_tracking import validate_field_value

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
            >>> required = FlowTracking.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.flow_tracking import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = FlowTracking.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.flow_tracking import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = FlowTracking.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.flow_tracking import get_schema_info

        return get_schema_info()
