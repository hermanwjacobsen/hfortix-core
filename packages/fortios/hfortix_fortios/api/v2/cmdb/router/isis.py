"""
FortiOS CMDB - Router isis

Configuration endpoint for managing cmdb router/isis objects.

API Endpoints:
    GET    /cmdb/router/isis
    POST   /cmdb/router/isis
    PUT    /cmdb/router/isis/{identifier}
    DELETE /cmdb/router/isis/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_isis.get()

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


class Isis:
    """Isis Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Isis endpoint."""
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
        Retrieve router/isis configuration.

        Configure IS-IS.

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
            >>> # Get all router/isis objects
            >>> result = fgt.api.cmdb.router_isis.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_isis.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_isis.get(action="schema")

        See Also:
            - post(): Create new router/isis object
            - put(): Update existing router/isis object
            - delete(): Remove router/isis object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/isis/{name}"
        else:
            endpoint = "/router/isis"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        is_type: str | None = None,
        adv_passive_only: str | None = None,
        adv_passive_only6: str | None = None,
        auth_mode_l1: str | None = None,
        auth_mode_l2: str | None = None,
        auth_password_l1: Any | None = None,
        auth_password_l2: Any | None = None,
        auth_keychain_l1: str | None = None,
        auth_keychain_l2: str | None = None,
        auth_sendonly_l1: str | None = None,
        auth_sendonly_l2: str | None = None,
        ignore_lsp_errors: str | None = None,
        lsp_gen_interval_l1: int | None = None,
        lsp_gen_interval_l2: int | None = None,
        lsp_refresh_interval: int | None = None,
        max_lsp_lifetime: int | None = None,
        spf_interval_exp_l1: str | None = None,
        spf_interval_exp_l2: str | None = None,
        dynamic_hostname: str | None = None,
        adjacency_check: str | None = None,
        adjacency_check6: str | None = None,
        overload_bit: str | None = None,
        overload_bit_suppress: str | list | None = None,
        overload_bit_on_startup: int | None = None,
        default_originate: str | None = None,
        default_originate6: str | None = None,
        metric_style: str | None = None,
        redistribute_l1: str | None = None,
        redistribute_l1_list: str | None = None,
        redistribute_l2: str | None = None,
        redistribute_l2_list: str | None = None,
        redistribute6_l1: str | None = None,
        redistribute6_l1_list: str | None = None,
        redistribute6_l2: str | None = None,
        redistribute6_l2_list: str | None = None,
        isis_net: str | list | None = None,
        isis_interface: str | list | None = None,
        summary_address: str | list | None = None,
        summary_address6: str | list | None = None,
        redistribute: str | list | None = None,
        redistribute6: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/isis object.

        Configure IS-IS.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            is_type: IS type.
            adv_passive_only: Enable/disable IS-IS advertisement of passive interfaces only.
            adv_passive_only6: Enable/disable IPv6 IS-IS advertisement of passive interfaces only.
            auth_mode_l1: Level 1 authentication mode.
            auth_mode_l2: Level 2 authentication mode.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_isis.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_isis.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            is_type=is_type,
            adv_passive_only=adv_passive_only,
            adv_passive_only6=adv_passive_only6,
            auth_mode_l1=auth_mode_l1,
            auth_mode_l2=auth_mode_l2,
            auth_password_l1=auth_password_l1,
            auth_password_l2=auth_password_l2,
            auth_keychain_l1=auth_keychain_l1,
            auth_keychain_l2=auth_keychain_l2,
            auth_sendonly_l1=auth_sendonly_l1,
            auth_sendonly_l2=auth_sendonly_l2,
            ignore_lsp_errors=ignore_lsp_errors,
            lsp_gen_interval_l1=lsp_gen_interval_l1,
            lsp_gen_interval_l2=lsp_gen_interval_l2,
            lsp_refresh_interval=lsp_refresh_interval,
            max_lsp_lifetime=max_lsp_lifetime,
            spf_interval_exp_l1=spf_interval_exp_l1,
            spf_interval_exp_l2=spf_interval_exp_l2,
            dynamic_hostname=dynamic_hostname,
            adjacency_check=adjacency_check,
            adjacency_check6=adjacency_check6,
            overload_bit=overload_bit,
            overload_bit_suppress=overload_bit_suppress,
            overload_bit_on_startup=overload_bit_on_startup,
            default_originate=default_originate,
            default_originate6=default_originate6,
            metric_style=metric_style,
            redistribute_l1=redistribute_l1,
            redistribute_l1_list=redistribute_l1_list,
            redistribute_l2=redistribute_l2,
            redistribute_l2_list=redistribute_l2_list,
            redistribute6_l1=redistribute6_l1,
            redistribute6_l1_list=redistribute6_l1_list,
            redistribute6_l2=redistribute6_l2,
            redistribute6_l2_list=redistribute6_l2_list,
            isis_net=isis_net,
            isis_interface=isis_interface,
            summary_address=summary_address,
            summary_address6=summary_address6,
            redistribute=redistribute,
            redistribute6=redistribute6,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.isis import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/isis",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/isis/{name_value}"

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
            >>> print(Isis.help())
            
            >>> # Get field information
            >>> print(Isis.help("is-type"))
        """
        from ._helpers.isis import (
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
            >>> fields = Isis.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Isis.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.isis import get_all_fields, get_field_metadata

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
            >>> info = Isis.field_info("is-type")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.isis import get_field_metadata

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
            >>> is_valid, error = Isis.validate_field("is-type", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.isis import validate_field_value

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
            >>> required = Isis.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.isis import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Isis.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.isis import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Isis.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.isis import get_schema_info

        return get_schema_info()
