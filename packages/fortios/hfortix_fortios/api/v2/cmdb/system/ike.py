"""
FortiOS CMDB - System ike

Configuration endpoint for managing cmdb system/ike objects.

API Endpoints:
    GET    /cmdb/system/ike
    POST   /cmdb/system/ike
    PUT    /cmdb/system/ike/{identifier}
    DELETE /cmdb/system/ike/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_ike.get()

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


class Ike:
    """Ike Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Ike endpoint."""
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
        Retrieve system/ike configuration.

        Configure IKE global attributes.

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
            >>> # Get all system/ike objects
            >>> result = fgt.api.cmdb.system_ike.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_ike.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_ike.get(action="schema")

        See Also:
            - post(): Create new system/ike object
            - put(): Update existing system/ike object
            - delete(): Remove system/ike object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/ike/{name}"
        else:
            endpoint = "/system/ike"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        embryonic_limit: int | None = None,
        dh_multiprocess: str | None = None,
        dh_worker_count: int | None = None,
        dh_mode: str | None = None,
        dh_keypair_cache: str | None = None,
        dh_keypair_count: int | None = None,
        dh_keypair_throttle: str | None = None,
        dh_group_1: str | None = None,
        dh_group_2: str | None = None,
        dh_group_5: str | None = None,
        dh_group_14: str | None = None,
        dh_group_15: str | None = None,
        dh_group_16: str | None = None,
        dh_group_17: str | None = None,
        dh_group_18: str | None = None,
        dh_group_19: str | None = None,
        dh_group_20: str | None = None,
        dh_group_21: str | None = None,
        dh_group_27: str | None = None,
        dh_group_28: str | None = None,
        dh_group_29: str | None = None,
        dh_group_30: str | None = None,
        dh_group_31: str | None = None,
        dh_group_32: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/ike object.

        Configure IKE global attributes.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            embryonic_limit: Maximum number of IPsec tunnels to negotiate simultaneously.
            dh_multiprocess: Enable/disable multiprocess Diffie-Hellman daemon for IKE.
            dh_worker_count: Number of Diffie-Hellman workers to start.
            dh_mode: Use software (CPU) or hardware (CPX) to perform Diffie-Hellman calculations.
            dh_keypair_cache: Enable/disable Diffie-Hellman key pair cache.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_ike.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_ike.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            embryonic_limit=embryonic_limit,
            dh_multiprocess=dh_multiprocess,
            dh_worker_count=dh_worker_count,
            dh_mode=dh_mode,
            dh_keypair_cache=dh_keypair_cache,
            dh_keypair_count=dh_keypair_count,
            dh_keypair_throttle=dh_keypair_throttle,
            dh_group_1=dh_group_1,
            dh_group_2=dh_group_2,
            dh_group_5=dh_group_5,
            dh_group_14=dh_group_14,
            dh_group_15=dh_group_15,
            dh_group_16=dh_group_16,
            dh_group_17=dh_group_17,
            dh_group_18=dh_group_18,
            dh_group_19=dh_group_19,
            dh_group_20=dh_group_20,
            dh_group_21=dh_group_21,
            dh_group_27=dh_group_27,
            dh_group_28=dh_group_28,
            dh_group_29=dh_group_29,
            dh_group_30=dh_group_30,
            dh_group_31=dh_group_31,
            dh_group_32=dh_group_32,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ike import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/ike",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/ike/{name_value}"

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
            >>> print(Ike.help())
            
            >>> # Get field information
            >>> print(Ike.help("embryonic-limit"))
        """
        from ._helpers.ike import (
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
            >>> fields = Ike.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Ike.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.ike import get_all_fields, get_field_metadata

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
            >>> info = Ike.field_info("embryonic-limit")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.ike import get_field_metadata

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
            >>> is_valid, error = Ike.validate_field("embryonic-limit", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.ike import validate_field_value

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
            >>> required = Ike.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.ike import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Ike.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.ike import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Ike.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.ike import get_schema_info

        return get_schema_info()
