"""
FortiOS CMDB - Web_proxy global_

Configuration endpoint for managing cmdb web_proxy/global_ objects.

API Endpoints:
    GET    /cmdb/web_proxy/global_
    POST   /cmdb/web_proxy/global_
    PUT    /cmdb/web_proxy/global_/{identifier}
    DELETE /cmdb/web_proxy/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy_global_.get()

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


class Global:
    """Global Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Global endpoint."""
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
        Retrieve web_proxy/global_ configuration.

        Configure Web proxy global settings.

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
            >>> # Get all web_proxy/global_ objects
            >>> result = fgt.api.cmdb.web_proxy_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.web_proxy_global_.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.web_proxy_global_.get(action="schema")

        See Also:
            - post(): Create new web_proxy/global_ object
            - put(): Update existing web_proxy/global_ object
            - delete(): Remove web_proxy/global_ object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/web-proxy/global/{name}"
        else:
            endpoint = "/web-proxy/global"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ssl_cert: str | None = None,
        ssl_ca_cert: str | None = None,
        fast_policy_match: str | None = None,
        ldap_user_cache: str | None = None,
        proxy_fqdn: str | None = None,
        max_request_length: int | None = None,
        max_message_length: int | None = None,
        http2_client_window_size: int | None = None,
        http2_server_window_size: int | None = None,
        auth_sign_timeout: int | None = None,
        strict_web_check: str | None = None,
        forward_proxy_auth: str | None = None,
        forward_server_affinity_timeout: int | None = None,
        max_waf_body_cache_length: int | None = None,
        webproxy_profile: str | None = None,
        learn_client_ip: str | None = None,
        always_learn_client_ip: str | None = None,
        learn_client_ip_from_header: str | list | None = None,
        learn_client_ip_srcaddr: str | list | None = None,
        learn_client_ip_srcaddr6: str | list | None = None,
        src_affinity_exempt_addr: str | list | None = None,
        src_affinity_exempt_addr6: str | list | None = None,
        policy_partial_match: str | None = None,
        log_policy_pending: str | None = None,
        log_forward_server: str | None = None,
        log_app_id: str | None = None,
        proxy_transparent_cert_inspection: str | None = None,
        request_obs_fold: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing web_proxy/global_ object.

        Configure Web proxy global settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            ssl_cert: SSL certificate for SSL interception.
            ssl_ca_cert: SSL CA certificate for SSL interception.
            fast_policy_match: Enable/disable fast matching algorithm for explicit and transparent proxy policy.
            ldap_user_cache: Enable/disable LDAP user cache for explicit and transparent proxy user.
            proxy_fqdn: Fully Qualified Domain Name of the explicit web proxy (default = default.fqdn) that clients connect to.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.web_proxy_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.web_proxy_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ssl_cert=ssl_cert,
            ssl_ca_cert=ssl_ca_cert,
            fast_policy_match=fast_policy_match,
            ldap_user_cache=ldap_user_cache,
            proxy_fqdn=proxy_fqdn,
            max_request_length=max_request_length,
            max_message_length=max_message_length,
            http2_client_window_size=http2_client_window_size,
            http2_server_window_size=http2_server_window_size,
            auth_sign_timeout=auth_sign_timeout,
            strict_web_check=strict_web_check,
            forward_proxy_auth=forward_proxy_auth,
            forward_server_affinity_timeout=forward_server_affinity_timeout,
            max_waf_body_cache_length=max_waf_body_cache_length,
            webproxy_profile=webproxy_profile,
            learn_client_ip=learn_client_ip,
            always_learn_client_ip=always_learn_client_ip,
            learn_client_ip_from_header=learn_client_ip_from_header,
            learn_client_ip_srcaddr=learn_client_ip_srcaddr,
            learn_client_ip_srcaddr6=learn_client_ip_srcaddr6,
            src_affinity_exempt_addr=src_affinity_exempt_addr,
            src_affinity_exempt_addr6=src_affinity_exempt_addr6,
            policy_partial_match=policy_partial_match,
            log_policy_pending=log_policy_pending,
            log_forward_server=log_forward_server,
            log_app_id=log_app_id,
            proxy_transparent_cert_inspection=proxy_transparent_cert_inspection,
            request_obs_fold=request_obs_fold,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/web_proxy/global_",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/web-proxy/global/{name_value}"

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
            >>> print(Global.help())
            
            >>> # Get field information
            >>> print(Global.help("ssl-cert"))
        """
        from ._helpers.global_ import (
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
            >>> fields = Global.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Global.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.global_ import get_all_fields, get_field_metadata

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
            >>> info = Global.field_info("ssl-cert")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.global_ import get_field_metadata

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
            >>> is_valid, error = Global.validate_field("ssl-cert", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.global_ import validate_field_value

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
            >>> required = Global.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.global_ import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Global.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.global_ import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Global.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.global_ import get_schema_info

        return get_schema_info()
