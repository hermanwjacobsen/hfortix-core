"""
FortiOS CMDB - Web_proxy explicit

Configuration endpoint for managing cmdb web_proxy/explicit objects.

API Endpoints:
    GET    /cmdb/web_proxy/explicit
    POST   /cmdb/web_proxy/explicit
    PUT    /cmdb/web_proxy/explicit/{identifier}
    DELETE /cmdb/web_proxy/explicit/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy_explicit.get()

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


class Explicit:
    """Explicit Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Explicit endpoint."""
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
        Retrieve web_proxy/explicit configuration.

        Configure explicit Web proxy settings.

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
            >>> # Get all web_proxy/explicit objects
            >>> result = fgt.api.cmdb.web_proxy_explicit.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.web_proxy_explicit.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.web_proxy_explicit.get(action="schema")

        See Also:
            - post(): Create new web_proxy/explicit object
            - put(): Update existing web_proxy/explicit object
            - delete(): Remove web_proxy/explicit object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/web-proxy/explicit/{name}"
        else:
            endpoint = "/web-proxy/explicit"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        secure_web_proxy: str | None = None,
        ftp_over_http: str | None = None,
        socks: str | None = None,
        http_incoming_port: str | None = None,
        http_connection_mode: str | None = None,
        https_incoming_port: str | None = None,
        secure_web_proxy_cert: str | list | None = None,
        client_cert: str | None = None,
        user_agent_detect: str | None = None,
        empty_cert_action: str | None = None,
        ssl_dh_bits: str | None = None,
        ftp_incoming_port: str | None = None,
        socks_incoming_port: str | None = None,
        incoming_ip: str | None = None,
        outgoing_ip: str | list | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        ipv6_status: str | None = None,
        incoming_ip6: str | None = None,
        outgoing_ip6: str | list | None = None,
        strict_guest: str | None = None,
        pref_dns_result: str | None = None,
        unknown_http_version: str | None = None,
        realm: str | None = None,
        sec_default_action: str | None = None,
        https_replacement_message: str | None = None,
        message_upon_server_error: str | None = None,
        pac_file_server_status: str | None = None,
        pac_file_url: str | None = None,
        pac_file_server_port: str | None = None,
        pac_file_through_https: str | None = None,
        pac_file_name: str | None = None,
        pac_file_data: str | None = None,
        pac_policy: str | list | None = None,
        ssl_algorithm: str | None = None,
        trace_auth_no_rsp: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing web_proxy/explicit object.

        Configure explicit Web proxy settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Enable/disable the explicit Web proxy for HTTP and HTTPS session.
            secure_web_proxy: Enable/disable/require the secure web proxy for HTTP and HTTPS session.
            ftp_over_http: Enable to proxy FTP-over-HTTP sessions sent from a web browser.
            socks: Enable/disable the SOCKS proxy.
            http_incoming_port: Accept incoming HTTP requests on one or more ports (0 - 65535, default = 8080).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.web_proxy_explicit.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.web_proxy_explicit.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            secure_web_proxy=secure_web_proxy,
            ftp_over_http=ftp_over_http,
            socks=socks,
            http_incoming_port=http_incoming_port,
            http_connection_mode=http_connection_mode,
            https_incoming_port=https_incoming_port,
            secure_web_proxy_cert=secure_web_proxy_cert,
            client_cert=client_cert,
            user_agent_detect=user_agent_detect,
            empty_cert_action=empty_cert_action,
            ssl_dh_bits=ssl_dh_bits,
            ftp_incoming_port=ftp_incoming_port,
            socks_incoming_port=socks_incoming_port,
            incoming_ip=incoming_ip,
            outgoing_ip=outgoing_ip,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            ipv6_status=ipv6_status,
            incoming_ip6=incoming_ip6,
            outgoing_ip6=outgoing_ip6,
            strict_guest=strict_guest,
            pref_dns_result=pref_dns_result,
            unknown_http_version=unknown_http_version,
            realm=realm,
            sec_default_action=sec_default_action,
            https_replacement_message=https_replacement_message,
            message_upon_server_error=message_upon_server_error,
            pac_file_server_status=pac_file_server_status,
            pac_file_url=pac_file_url,
            pac_file_server_port=pac_file_server_port,
            pac_file_through_https=pac_file_through_https,
            pac_file_name=pac_file_name,
            pac_file_data=pac_file_data,
            pac_policy=pac_policy,
            ssl_algorithm=ssl_algorithm,
            trace_auth_no_rsp=trace_auth_no_rsp,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.explicit import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/web_proxy/explicit",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/web-proxy/explicit/{name_value}"

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
            >>> print(Explicit.help())
            
            >>> # Get field information
            >>> print(Explicit.help("status"))
        """
        from ._helpers.explicit import (
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
            >>> fields = Explicit.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Explicit.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.explicit import get_all_fields, get_field_metadata

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
            >>> info = Explicit.field_info("status")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.explicit import get_field_metadata

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
            >>> is_valid, error = Explicit.validate_field("status", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.explicit import validate_field_value

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
            >>> required = Explicit.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.explicit import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Explicit.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.explicit import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Explicit.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.explicit import get_schema_info

        return get_schema_info()
