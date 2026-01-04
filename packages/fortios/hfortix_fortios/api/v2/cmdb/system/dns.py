"""
FortiOS CMDB - System dns

Configuration endpoint for managing cmdb system/dns objects.

API Endpoints:
    GET    /cmdb/system/dns
    POST   /cmdb/system/dns
    PUT    /cmdb/system/dns/{identifier}
    DELETE /cmdb/system/dns/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_dns.get()

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


class Dns:
    """Dns Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Dns endpoint."""
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
        Retrieve system/dns configuration.

        Configure DNS.

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
            >>> # Get all system/dns objects
            >>> result = fgt.api.cmdb.system_dns.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_dns.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_dns.get(action="schema")

        See Also:
            - post(): Create new system/dns object
            - put(): Update existing system/dns object
            - delete(): Remove system/dns object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/dns/{name}"
        else:
            endpoint = "/system/dns"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        primary: str | None = None,
        secondary: str | None = None,
        protocol: str | None = None,
        ssl_certificate: str | None = None,
        server_hostname: str | list | None = None,
        domain: str | list | None = None,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        timeout: int | None = None,
        retry: int | None = None,
        dns_cache_limit: int | None = None,
        dns_cache_ttl: int | None = None,
        cache_notfound_responses: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        root_servers: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        server_select_method: str | None = None,
        alt_primary: str | None = None,
        alt_secondary: str | None = None,
        log: str | None = None,
        fqdn_cache_ttl: int | None = None,
        fqdn_max_refresh: int | None = None,
        fqdn_min_refresh: int | None = None,
        hostname_ttl: int | None = None,
        hostname_limit: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/dns object.

        Configure DNS.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            primary: Primary DNS server IP address.
            secondary: Secondary DNS server IP address.
            protocol: DNS transport protocols.
            ssl_certificate: Name of local certificate for SSL connections.
            server_hostname: DNS server host name list.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_dns.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_dns.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            primary=primary,
            secondary=secondary,
            protocol=protocol,
            ssl_certificate=ssl_certificate,
            server_hostname=server_hostname,
            domain=domain,
            ip6_primary=ip6_primary,
            ip6_secondary=ip6_secondary,
            timeout=timeout,
            retry=retry,
            dns_cache_limit=dns_cache_limit,
            dns_cache_ttl=dns_cache_ttl,
            cache_notfound_responses=cache_notfound_responses,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            root_servers=root_servers,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            server_select_method=server_select_method,
            alt_primary=alt_primary,
            alt_secondary=alt_secondary,
            log=log,
            fqdn_cache_ttl=fqdn_cache_ttl,
            fqdn_max_refresh=fqdn_max_refresh,
            fqdn_min_refresh=fqdn_min_refresh,
            hostname_ttl=hostname_ttl,
            hostname_limit=hostname_limit,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.dns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dns",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/dns/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        primary: str | None = None,
        secondary: str | None = None,
        protocol: str | None = None,
        ssl_certificate: str | None = None,
        server_hostname: str | list | None = None,
        domain: str | list | None = None,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        timeout: int | None = None,
        retry: int | None = None,
        dns_cache_limit: int | None = None,
        dns_cache_ttl: int | None = None,
        cache_notfound_responses: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        root_servers: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        server_select_method: str | None = None,
        alt_primary: str | None = None,
        alt_secondary: str | None = None,
        log: str | None = None,
        fqdn_cache_ttl: int | None = None,
        fqdn_max_refresh: int | None = None,
        fqdn_min_refresh: int | None = None,
        hostname_ttl: int | None = None,
        hostname_limit: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/dns object.

        Configure DNS.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            primary: Primary DNS server IP address.
            secondary: Secondary DNS server IP address.
            protocol: DNS transport protocols.
            ssl_certificate: Name of local certificate for SSL connections.
            server_hostname: DNS server host name list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned identifier.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_dns.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created object: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Dns.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_dns.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Dns.required_fields()) }}
            
            Use Dns.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            primary=primary,
            secondary=secondary,
            protocol=protocol,
            ssl_certificate=ssl_certificate,
            server_hostname=server_hostname,
            domain=domain,
            ip6_primary=ip6_primary,
            ip6_secondary=ip6_secondary,
            timeout=timeout,
            retry=retry,
            dns_cache_limit=dns_cache_limit,
            dns_cache_ttl=dns_cache_ttl,
            cache_notfound_responses=cache_notfound_responses,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            root_servers=root_servers,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            server_select_method=server_select_method,
            alt_primary=alt_primary,
            alt_secondary=alt_secondary,
            log=log,
            fqdn_cache_ttl=fqdn_cache_ttl,
            fqdn_max_refresh=fqdn_max_refresh,
            fqdn_min_refresh=fqdn_min_refresh,
            hostname_ttl=hostname_ttl,
            hostname_limit=hostname_limit,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.dns import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dns",
            )

        endpoint = "/system/dns"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/dns object.

        Configure DNS.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_dns.delete(name="object-to-delete")
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = f"/system/dns/{name}"

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/dns object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Object name (primary key)
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_dns.exists(name="my-object"):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_dns.exists(name="old-object"):
            ...     fgt.api.cmdb.system_dns.delete(name="old-object")

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(name=name, vdom=vdom, raw_json=True)
            
            if isinstance(response, dict):
                # Use helper function to check success
                return is_success(response)
            else:
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception:
            # Resource not found or other error - return False
            return False

    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/dns object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "name": "my-object",
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_dns.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_dns.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        if payload_dict is None:
            payload_dict = {}
        
        mkey_value = payload_dict.get("name")
        if not mkey_value:
            raise ValueError("name is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)

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
            >>> print(Dns.help())
            
            >>> # Get field information
            >>> print(Dns.help("primary"))
        """
        from ._helpers.dns import (
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
            >>> fields = Dns.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Dns.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.dns import get_all_fields, get_field_metadata

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
            >>> info = Dns.field_info("primary")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.dns import get_field_metadata

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
            >>> is_valid, error = Dns.validate_field("primary", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.dns import validate_field_value

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
            >>> required = Dns.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.dns import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Dns.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.dns import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Dns.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.dns import get_schema_info

        return get_schema_info()
