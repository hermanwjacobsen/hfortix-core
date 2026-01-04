"""
FortiOS CMDB - Router static6

Configuration endpoint for managing cmdb router/static6 objects.

API Endpoints:
    GET    /cmdb/router/static6
    POST   /cmdb/router/static6
    PUT    /cmdb/router/static6/{identifier}
    DELETE /cmdb/router/static6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_static6.get()

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


class Static6:
    """Static6 Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Static6 endpoint."""
        self._client = client

    def get(
        self,
        seq_num: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve router/static6 configuration.

        Configure IPv6 static routing tables.

        Args:
            seq_num: Integer identifier to retrieve specific object.
                If None, returns all objects.
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
            >>> # Get all router/static6 objects
            >>> result = fgt.api.cmdb.router_static6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific router/static6 by seq-num
            >>> result = fgt.api.cmdb.router_static6.get(seq_num=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_static6.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_static6.get(action="schema")

        See Also:
            - post(): Create new router/static6 object
            - put(): Update existing router/static6 object
            - delete(): Remove router/static6 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if seq_num:
            endpoint = "/router/static6/" + str(seq_num)
        else:
            endpoint = "/router/static6"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        status: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        device: str | None = None,
        devindex: int | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: str | list | None = None,
        dstaddr: str | None = None,
        link_monitor_exempt: str | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        tag: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/static6 object.

        Configure IPv6 static routing tables.

        Args:
            payload_dict: Object data as dict. Must include seq-num (primary key).
            seq_num: Sequence number.
            status: Enable/disable this static route.
            dst: Destination IPv6 prefix.
            gateway: IPv6 address of the gateway.
            device: Gateway out interface or tunnel.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_static6.put(
            ...     seq_num=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_static6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            seq_num=seq_num,
            status=status,
            dst=dst,
            gateway=gateway,
            device=device,
            devindex=devindex,
            distance=distance,
            weight=weight,
            priority=priority,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            link_monitor_exempt=link_monitor_exempt,
            vrf=vrf,
            bfd=bfd,
            tag=tag,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.static6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/static6",
            )
        
        seq_num_value = payload_data.get("seq-num")
        if not seq_num_value:
            raise ValueError("seq-num is required for PUT")
        endpoint = "/router/static6/" + str(seq_num_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        status: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        device: str | None = None,
        devindex: int | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: str | list | None = None,
        dstaddr: str | None = None,
        link_monitor_exempt: str | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        tag: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new router/static6 object.

        Configure IPv6 static routing tables.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            seq_num: Sequence number.
            status: Enable/disable this static route.
            dst: Destination IPv6 prefix.
            gateway: IPv6 address of the gateway.
            device: Gateway out interface or tunnel.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned seq-num.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.router_static6.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created seq-num: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Static6.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.router_static6.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Static6.required_fields()) }}
            
            Use Static6.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            seq_num=seq_num,
            status=status,
            dst=dst,
            gateway=gateway,
            device=device,
            devindex=devindex,
            distance=distance,
            weight=weight,
            priority=priority,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            link_monitor_exempt=link_monitor_exempt,
            vrf=vrf,
            bfd=bfd,
            tag=tag,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.static6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/static6",
            )

        endpoint = "/router/static6"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        seq_num: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete router/static6 object.

        Configure IPv6 static routing tables.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If seq-num is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.router_static6.delete(seq_num=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not seq_num:
            raise ValueError("seq-num is required for DELETE")
        endpoint = "/router/static6/" + str(seq_num)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if router/static6 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.router_static6.exists(seq_num=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.router_static6.exists(seq_num=1):
            ...     fgt.api.cmdb.router_static6.delete(seq_num=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(seq_num=seq_num, vdom=vdom, raw_json=True)
            
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
        Create or update router/static6 object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (seq-num) in the payload.

        Args:
            payload_dict: Resource data including seq-num (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.router_static6.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.router_static6.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("seq-num")
        if not mkey_value:
            raise ValueError("seq-num is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(seq_num=mkey_value, vdom=vdom):
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
            >>> print(Static6.help())
            
            >>> # Get field information
            >>> print(Static6.help("seq-num"))
        """
        from ._helpers.static6 import (
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
            >>> fields = Static6.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Static6.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.static6 import get_all_fields, get_field_metadata

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
            >>> info = Static6.field_info("seq-num")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.static6 import get_field_metadata

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
            >>> is_valid, error = Static6.validate_field("seq-num", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.static6 import validate_field_value

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
            >>> required = Static6.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.static6 import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Static6.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.static6 import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Static6.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.static6 import get_schema_info

        return get_schema_info()
