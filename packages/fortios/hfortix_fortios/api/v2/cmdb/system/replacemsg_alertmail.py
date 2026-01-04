"""
FortiOS CMDB - System replacemsg_alertmail

Configuration endpoint for managing cmdb system/replacemsg_alertmail objects.

📖 **Read-Only Reference Table**
   This endpoint provides read-only reference data (e.g., geography, timezone).
   - GET operations return all available data
   - POST/PUT/DELETE operations are not supported
   - Querying by identifier returns all items (filter is ignored)

API Endpoints:
    GET    /cmdb/system/replacemsg_alertmail

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_replacemsg_alertmail.get()

Important:
    - This is a **read-only** endpoint (reference data only)
    - Use **GET** to retrieve available options
    - Creation/modification/deletion not supported
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

# Import cache for readonly reference data
from hfortix_core.cache import readonly_cache


class ReplacemsgAlertmail:
    """ReplacemsgAlertmail Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize ReplacemsgAlertmail endpoint."""
        self._client = client

    def get(
        self,
        msg_type: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve system/replacemsg_alertmail configuration.

        Replacement messages.

        Args:
            msg_type: String identifier to retrieve specific object.
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
            >>> # Get all system/replacemsg_alertmail objects
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/replacemsg_alertmail by msg-type
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.get(msg_type=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_replacemsg_alertmail.get(action="schema")

        See Also:
            - post(): Create new system/replacemsg_alertmail object
            - put(): Update existing system/replacemsg_alertmail object
            - delete(): Remove system/replacemsg_alertmail object
            - exists(): Check if object exists
        """
        # Check cache for readonly reference data (24hr TTL)
        cache_key = f"cmdb/system/replacemsg_alertmail"
        
        # Only use cache for full list queries (no identifier, no filters)
        is_list_query = msg_type is None and not payload_dict and not kwargs
        
        if is_list_query:
            cached_data = readonly_cache.get(cache_key)
            if cached_data is not None:
                # Return cached data
                if raw_json:
                    return cached_data
                return cached_data
        
        params = payload_dict.copy() if payload_dict else {}
        
        if msg_type:
            endpoint = "/system.replacemsg/alertmail/" + str(msg_type)
        else:
            endpoint = "/system.replacemsg/alertmail"
        
        params.update(kwargs)
        
        # Fetch data and cache if this is a list query
        response = self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )
        
        # Cache the response for list queries
        if is_list_query:
            if isinstance(response, dict):
                readonly_cache.set(cache_key, response)
            # For async responses, we can't cache easily without awaiting
            # User will benefit from cache on subsequent sync calls
        
        return response

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        msg_type: str | None = None,
        buffer: str | None = None,
        header: str | None = None,
        format: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/replacemsg_alertmail object.

        Replacement messages.

        Args:
            payload_dict: Object data as dict. Must include msg-type (primary key).
            msg_type: Message type.
            buffer: Message string.
            header: Header flag.
            format: Format flag.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If msg-type is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.put(
            ...     msg_type=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "msg-type": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.replacemsg_alertmail import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/replacemsg_alertmail",
            )
        
        msg_type_value = payload_data.get("msg-type")
        if not msg_type_value:
            raise ValueError("msg-type is required for PUT")
        endpoint = "/system.replacemsg/alertmail/" + str(msg_type_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        msg_type: str | None = None,
        buffer: str | None = None,
        header: str | None = None,
        format: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/replacemsg_alertmail object.

        Replacement messages.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            msg_type: Message type.
            buffer: Message string.
            header: Header flag.
            format: Format flag.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned msg-type.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created msg-type: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ReplacemsgAlertmail.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ReplacemsgAlertmail.required_fields()) }}
            
            Use ReplacemsgAlertmail.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.replacemsg_alertmail import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/replacemsg_alertmail",
            )

        endpoint = "/system.replacemsg/alertmail"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        msg_type: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete system/replacemsg_alertmail object.

        Replacement messages.

        Args:
            msg_type: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If msg-type is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.delete(msg_type=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not msg_type:
            raise ValueError("msg-type is required for DELETE")
        endpoint = "/system.replacemsg/alertmail/" + str(msg_type)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        msg_type: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/replacemsg_alertmail object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            msg_type: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_replacemsg_alertmail.exists(msg_type=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_replacemsg_alertmail.exists(msg_type=1):
            ...     fgt.api.cmdb.system_replacemsg_alertmail.delete(msg_type=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # For readonly endpoints, check by fetching all items and scanning
        # This is necessary because readonly endpoints don't support direct ID queries
        try:
            response = self.get(vdom=vdom, raw_json=True)
            
            if isinstance(response, dict):
                # Synchronous response
                if not is_success(response):
                    return False
                
                results = response.get("results", [])
                if not isinstance(results, list):
                    return False
                
                # Scan for matching identifier
                return any(
                    item.get("msg-type") == msg_type
                    for item in results
                )
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    if not is_success(r):
                        return False
                    
                    results = r.get("results", [])
                    if not isinstance(results, list):
                        return False
                    
                    return any(
                        item.get("msg-type") == msg_type
                        for item in results
                    )
                return _check()
        except Exception:
            # Error fetching list - return False
            return False

    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/replacemsg_alertmail object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (msg-type) in the payload.

        Args:
            payload_dict: Resource data including msg-type (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If msg-type is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "msg-type": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_replacemsg_alertmail.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_replacemsg_alertmail.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("msg-type")
        if not mkey_value:
            raise ValueError("msg-type is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(msg_type=mkey_value, vdom=vdom):
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
            >>> print(ReplacemsgAlertmail.help())
            
            >>> # Get field information
            >>> print(ReplacemsgAlertmail.help("msg-type"))
        """
        from ._helpers.replacemsg_alertmail import (
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
            >>> fields = ReplacemsgAlertmail.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = ReplacemsgAlertmail.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.replacemsg_alertmail import get_all_fields, get_field_metadata

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
            >>> info = ReplacemsgAlertmail.field_info("msg-type")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.replacemsg_alertmail import get_field_metadata

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
            >>> is_valid, error = ReplacemsgAlertmail.validate_field("msg-type", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.replacemsg_alertmail import validate_field_value

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
            >>> required = ReplacemsgAlertmail.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.replacemsg_alertmail import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = ReplacemsgAlertmail.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.replacemsg_alertmail import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = ReplacemsgAlertmail.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.replacemsg_alertmail import get_schema_info

        return get_schema_info()
