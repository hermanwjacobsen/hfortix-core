"""
FortiOS CMDB - Vpn certificate setting

Configuration endpoint for managing cmdb vpn/certificate/setting objects.

API Endpoints:
    GET    /cmdb/vpn/certificate/setting
    POST   /cmdb/vpn/certificate/setting
    PUT    /cmdb/vpn/certificate/setting/{identifier}
    DELETE /cmdb/vpn/certificate/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_certificate_setting.get()

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
        Retrieve vpn/certificate/setting configuration.

        VPN certificate setting.

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
            >>> # Get all vpn/certificate/setting objects
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_certificate_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_certificate_setting.get(action="schema")

        See Also:
            - post(): Create new vpn/certificate/setting object
            - put(): Update existing vpn/certificate/setting object
            - delete(): Remove vpn/certificate/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/vpn.certificate/setting/{name}"
        else:
            endpoint = "/vpn.certificate/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ocsp_status: str | None = None,
        ocsp_option: str | None = None,
        proxy: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: Any | None = None,
        source_ip: str | None = None,
        ocsp_default_server: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        check_ca_cert: str | None = None,
        check_ca_chain: str | None = None,
        subject_match: str | None = None,
        subject_set: str | None = None,
        cn_match: str | None = None,
        cn_allow_multi: str | None = None,
        crl_verification: str | None = None,
        strict_ocsp_check: str | None = None,
        ssl_min_proto_version: str | None = None,
        cmp_save_extra_certs: str | None = None,
        cmp_key_usage_checking: str | None = None,
        cert_expire_warning: int | None = None,
        certname_rsa1024: str | None = None,
        certname_rsa2048: str | None = None,
        certname_rsa4096: str | None = None,
        certname_dsa1024: str | None = None,
        certname_dsa2048: str | None = None,
        certname_ecdsa256: str | None = None,
        certname_ecdsa384: str | None = None,
        certname_ecdsa521: str | None = None,
        certname_ed25519: str | None = None,
        certname_ed448: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/certificate/setting object.

        VPN certificate setting.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ocsp_status: Enable/disable receiving certificates using the OCSP.
            ocsp_option: Specify whether the OCSP URL is from certificate or configured OCSP server.
            proxy: Proxy server FQDN or IP for OCSP/CA queries during certificate verification.
            proxy_port: Proxy server port (1 - 65535, default = 8080).
            proxy_username: Proxy server user name.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_certificate_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_certificate_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ocsp_status=ocsp_status,
            ocsp_option=ocsp_option,
            proxy=proxy,
            proxy_port=proxy_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
            source_ip=source_ip,
            ocsp_default_server=ocsp_default_server,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            check_ca_cert=check_ca_cert,
            check_ca_chain=check_ca_chain,
            subject_match=subject_match,
            subject_set=subject_set,
            cn_match=cn_match,
            cn_allow_multi=cn_allow_multi,
            crl_verification=crl_verification,
            strict_ocsp_check=strict_ocsp_check,
            ssl_min_proto_version=ssl_min_proto_version,
            cmp_save_extra_certs=cmp_save_extra_certs,
            cmp_key_usage_checking=cmp_key_usage_checking,
            cert_expire_warning=cert_expire_warning,
            certname_rsa1024=certname_rsa1024,
            certname_rsa2048=certname_rsa2048,
            certname_rsa4096=certname_rsa4096,
            certname_dsa1024=certname_dsa1024,
            certname_dsa2048=certname_dsa2048,
            certname_ecdsa256=certname_ecdsa256,
            certname_ecdsa384=certname_ecdsa384,
            certname_ecdsa521=certname_ecdsa521,
            certname_ed25519=certname_ed25519,
            certname_ed448=certname_ed448,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/certificate/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/vpn.certificate/setting/{name_value}"

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
            >>> print(Setting.help())
            
            >>> # Get field information
            >>> print(Setting.help("ocsp-status"))
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
            >>> info = Setting.field_info("ocsp-status")
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
            >>> is_valid, error = Setting.validate_field("ocsp-status", "test")
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
