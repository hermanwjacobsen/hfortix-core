"""
FortiOS CMDB - Router ospf

Configuration endpoint for managing cmdb router/ospf objects.

API Endpoints:
    GET    /cmdb/router/ospf
    POST   /cmdb/router/ospf
    PUT    /cmdb/router/ospf/{identifier}
    DELETE /cmdb/router/ospf/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_ospf.get()

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


class Ospf:
    """Ospf Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ospf endpoint."""
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
        Retrieve router/ospf configuration.

        Configure OSPF.

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
            >>> # Get all router/ospf objects
            >>> result = fgt.api.cmdb.router_ospf.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_ospf.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_ospf.get(action="schema")

        See Also:
            - post(): Create new router/ospf object
            - put(): Update existing router/ospf object
            - delete(): Remove router/ospf object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/ospf/{name}"
        else:
            endpoint = "/router/ospf"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        abr_type: str | None = None,
        auto_cost_ref_bandwidth: int | None = None,
        distance_external: int | None = None,
        distance_inter_area: int | None = None,
        distance_intra_area: int | None = None,
        database_overflow: str | None = None,
        database_overflow_max_lsas: int | None = None,
        database_overflow_time_to_recover: int | None = None,
        default_information_originate: str | None = None,
        default_information_metric: int | None = None,
        default_information_metric_type: str | None = None,
        default_information_route_map: str | None = None,
        default_metric: int | None = None,
        distance: int | None = None,
        lsa_refresh_interval: int | None = None,
        rfc1583_compatible: str | None = None,
        router_id: str | None = None,
        spf_timers: str | None = None,
        bfd: str | None = None,
        log_neighbour_changes: str | None = None,
        distribute_list_in: str | None = None,
        distribute_route_map_in: str | None = None,
        restart_mode: str | None = None,
        restart_period: int | None = None,
        restart_on_topology_change: str | None = None,
        area: str | list | None = None,
        ospf_interface: str | list | None = None,
        network: str | list | None = None,
        neighbor: str | list | None = None,
        passive_interface: str | list | None = None,
        summary_address: str | list | None = None,
        distribute_list: str | list | None = None,
        redistribute: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/ospf object.

        Configure OSPF.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            abr_type: Area border router type.
            auto_cost_ref_bandwidth: Reference bandwidth in terms of megabits per second.
            distance_external: Administrative external distance.
            distance_inter_area: Administrative inter-area distance.
            distance_intra_area: Administrative intra-area distance.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_ospf.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_ospf.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            abr_type=abr_type,
            auto_cost_ref_bandwidth=auto_cost_ref_bandwidth,
            distance_external=distance_external,
            distance_inter_area=distance_inter_area,
            distance_intra_area=distance_intra_area,
            database_overflow=database_overflow,
            database_overflow_max_lsas=database_overflow_max_lsas,
            database_overflow_time_to_recover=database_overflow_time_to_recover,
            default_information_originate=default_information_originate,
            default_information_metric=default_information_metric,
            default_information_metric_type=default_information_metric_type,
            default_information_route_map=default_information_route_map,
            default_metric=default_metric,
            distance=distance,
            lsa_refresh_interval=lsa_refresh_interval,
            rfc1583_compatible=rfc1583_compatible,
            router_id=router_id,
            spf_timers=spf_timers,
            bfd=bfd,
            log_neighbour_changes=log_neighbour_changes,
            distribute_list_in=distribute_list_in,
            distribute_route_map_in=distribute_route_map_in,
            restart_mode=restart_mode,
            restart_period=restart_period,
            restart_on_topology_change=restart_on_topology_change,
            area=area,
            ospf_interface=ospf_interface,
            network=network,
            neighbor=neighbor,
            passive_interface=passive_interface,
            summary_address=summary_address,
            distribute_list=distribute_list,
            redistribute=redistribute,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ospf import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/ospf",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/ospf/{name_value}"

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
            >>> print(Ospf.help())
            
            >>> # Get field information
            >>> print(Ospf.help("abr-type"))
        """
        from ._helpers.ospf import (
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
            >>> fields = Ospf.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Ospf.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.ospf import get_all_fields, get_field_metadata

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
            >>> info = Ospf.field_info("abr-type")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.ospf import get_field_metadata

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
            >>> is_valid, error = Ospf.validate_field("abr-type", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.ospf import validate_field_value

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
            >>> required = Ospf.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.ospf import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Ospf.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.ospf import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Ospf.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.ospf import get_schema_info

        return get_schema_info()
