"""
FortiOS CMDB - Firewall shaper_traffic_shaper

Configuration endpoint for managing cmdb firewall/shaper_traffic_shaper objects.

API Endpoints:
    GET    /cmdb/firewall/shaper_traffic_shaper
    POST   /cmdb/firewall/shaper_traffic_shaper
    PUT    /cmdb/firewall/shaper_traffic_shaper/{identifier}
    DELETE /cmdb/firewall/shaper_traffic_shaper/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_shaper_traffic_shaper.get()

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


class ShaperTrafficShaper:
    """ShaperTrafficShaper Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize ShaperTrafficShaper endpoint."""
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
        Retrieve firewall/shaper_traffic_shaper configuration.

        Configure shared traffic shaper.

        Args:
            name: String identifier to retrieve specific object.
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
            >>> # Get all firewall/shaper_traffic_shaper objects
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/shaper_traffic_shaper by name
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_shaper_traffic_shaper.get(action="schema")

        See Also:
            - post(): Create new firewall/shaper_traffic_shaper object
            - put(): Update existing firewall/shaper_traffic_shaper object
            - delete(): Remove firewall/shaper_traffic_shaper object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/firewall.shaper/traffic-shaper/" + str(name)
        else:
            endpoint = "/firewall.shaper/traffic-shaper"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        guaranteed_bandwidth: int | None = None,
        maximum_bandwidth: int | None = None,
        bandwidth_unit: str | None = None,
        priority: str | None = None,
        per_policy: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        dscp_marking_method: str | None = None,
        exceed_bandwidth: int | None = None,
        exceed_dscp: str | None = None,
        maximum_dscp: str | None = None,
        cos_marking: str | None = None,
        cos_marking_method: str | None = None,
        cos: str | None = None,
        exceed_cos: str | None = None,
        maximum_cos: str | None = None,
        overhead: int | None = None,
        exceed_class_id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/shaper_traffic_shaper object.

        Configure shared traffic shaper.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Traffic shaper name.
            guaranteed_bandwidth: Amount of bandwidth guaranteed for this shaper (0 - 80000000). Units depend on the bandwidth-unit setting.
            maximum_bandwidth: Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting.
            bandwidth_unit: Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps).
            priority: Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            guaranteed_bandwidth=guaranteed_bandwidth,
            maximum_bandwidth=maximum_bandwidth,
            bandwidth_unit=bandwidth_unit,
            priority=priority,
            per_policy=per_policy,
            diffserv=diffserv,
            diffservcode=diffservcode,
            dscp_marking_method=dscp_marking_method,
            exceed_bandwidth=exceed_bandwidth,
            exceed_dscp=exceed_dscp,
            maximum_dscp=maximum_dscp,
            cos_marking=cos_marking,
            cos_marking_method=cos_marking_method,
            cos=cos,
            exceed_cos=exceed_cos,
            maximum_cos=maximum_cos,
            overhead=overhead,
            exceed_class_id=exceed_class_id,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.shaper_traffic_shaper import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/shaper_traffic_shaper",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/firewall.shaper/traffic-shaper/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        guaranteed_bandwidth: int | None = None,
        maximum_bandwidth: int | None = None,
        bandwidth_unit: str | None = None,
        priority: str | None = None,
        per_policy: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        dscp_marking_method: str | None = None,
        exceed_bandwidth: int | None = None,
        exceed_dscp: str | None = None,
        maximum_dscp: str | None = None,
        cos_marking: str | None = None,
        cos_marking_method: str | None = None,
        cos: str | None = None,
        exceed_cos: str | None = None,
        maximum_cos: str | None = None,
        overhead: int | None = None,
        exceed_class_id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/shaper_traffic_shaper object.

        Configure shared traffic shaper.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Traffic shaper name.
            guaranteed_bandwidth: Amount of bandwidth guaranteed for this shaper (0 - 80000000). Units depend on the bandwidth-unit setting.
            maximum_bandwidth: Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting.
            bandwidth_unit: Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps).
            priority: Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ShaperTrafficShaper.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ShaperTrafficShaper.required_fields()) }}
            
            Use ShaperTrafficShaper.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            guaranteed_bandwidth=guaranteed_bandwidth,
            maximum_bandwidth=maximum_bandwidth,
            bandwidth_unit=bandwidth_unit,
            priority=priority,
            per_policy=per_policy,
            diffserv=diffserv,
            diffservcode=diffservcode,
            dscp_marking_method=dscp_marking_method,
            exceed_bandwidth=exceed_bandwidth,
            exceed_dscp=exceed_dscp,
            maximum_dscp=maximum_dscp,
            cos_marking=cos_marking,
            cos_marking_method=cos_marking_method,
            cos=cos,
            exceed_cos=exceed_cos,
            maximum_cos=maximum_cos,
            overhead=overhead,
            exceed_class_id=exceed_class_id,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.shaper_traffic_shaper import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/shaper_traffic_shaper",
            )

        endpoint = "/firewall.shaper/traffic-shaper"
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
        Delete firewall/shaper_traffic_shaper object.

        Configure shared traffic shaper.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/firewall.shaper/traffic-shaper/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/shaper_traffic_shaper object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_shaper_traffic_shaper.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_shaper_traffic_shaper.exists(name=1):
            ...     fgt.api.cmdb.firewall_shaper_traffic_shaper.delete(name=1)

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
        Create or update firewall/shaper_traffic_shaper object (intelligent operation).

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
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_shaper_traffic_shaper.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_shaper_traffic_shaper.set(payload_dict=obj_data)
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
            >>> print(ShaperTrafficShaper.help())
            
            >>> # Get field information
            >>> print(ShaperTrafficShaper.help("name"))
        """
        from ._helpers.shaper_traffic_shaper import (
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
            >>> fields = ShaperTrafficShaper.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = ShaperTrafficShaper.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.shaper_traffic_shaper import get_all_fields, get_field_metadata

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
            >>> info = ShaperTrafficShaper.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.shaper_traffic_shaper import get_field_metadata

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
            >>> is_valid, error = ShaperTrafficShaper.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.shaper_traffic_shaper import validate_field_value

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
            >>> required = ShaperTrafficShaper.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.shaper_traffic_shaper import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = ShaperTrafficShaper.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.shaper_traffic_shaper import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = ShaperTrafficShaper.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.shaper_traffic_shaper import get_schema_info

        return get_schema_info()
