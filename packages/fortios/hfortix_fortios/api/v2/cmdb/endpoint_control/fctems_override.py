"""
FortiOS CMDB - Endpoint_control fctems_override

Configuration endpoint for managing cmdb endpoint_control/fctems_override objects.

API Endpoints:
    GET    /cmdb/endpoint_control/fctems_override
    POST   /cmdb/endpoint_control/fctems_override
    PUT    /cmdb/endpoint_control/fctems_override/{identifier}
    DELETE /cmdb/endpoint_control/fctems_override/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.endpoint_control_fctems_override.get()

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


class FctemsOverride:
    """FctemsOverride Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize FctemsOverride endpoint."""
        self._client = client

    def get(
        self,
        ems_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve endpoint_control/fctems_override configuration.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            ems_id: Integer identifier to retrieve specific object.
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
            >>> # Get all endpoint_control/fctems_override objects
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific endpoint_control/fctems_override by ems-id
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get(ems_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.endpoint_control_fctems_override.get(action="schema")

        See Also:
            - post(): Create new endpoint_control/fctems_override object
            - put(): Update existing endpoint_control/fctems_override object
            - delete(): Remove endpoint_control/fctems_override object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if ems_id:
            endpoint = "/endpoint-control/fctems-override/" + str(ems_id)
        else:
            endpoint = "/endpoint-control/fctems-override"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        ems_id: int | None = None,
        status: str | None = None,
        name: str | None = None,
        dirty_reason: str | None = None,
        fortinetone_cloud_authentication: str | None = None,
        cloud_authentication_access_key: Any | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: str | None = None,
        pull_vulnerabilities: str | None = None,
        pull_tags: str | None = None,
        pull_malware_hash: str | None = None,
        capabilities: str | list | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: str | None = None,
        websocket_override: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        trust_ca_cn: str | None = None,
        verifying_ca: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing endpoint_control/fctems_override object.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            payload_dict: Object data as dict. Must include ems-id (primary key).
            ems_id: EMS ID in order (1 - 7).
            status: Enable or disable this EMS configuration.
            name: FortiClient Enterprise Management Server (EMS) name.
            dirty_reason: Dirty Reason for FortiClient EMS.
            fortinetone_cloud_authentication: Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If ems-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.put(
            ...     ems_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "ems-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ems_id=ems_id,
            status=status,
            name=name,
            dirty_reason=dirty_reason,
            fortinetone_cloud_authentication=fortinetone_cloud_authentication,
            cloud_authentication_access_key=cloud_authentication_access_key,
            server=server,
            https_port=https_port,
            serial_number=serial_number,
            tenant_id=tenant_id,
            source_ip=source_ip,
            pull_sysinfo=pull_sysinfo,
            pull_vulnerabilities=pull_vulnerabilities,
            pull_tags=pull_tags,
            pull_malware_hash=pull_malware_hash,
            capabilities=capabilities,
            call_timeout=call_timeout,
            out_of_sync_threshold=out_of_sync_threshold,
            send_tags_to_all_vdoms=send_tags_to_all_vdoms,
            websocket_override=websocket_override,
            interface_select_method=interface_select_method,
            interface=interface,
            trust_ca_cn=trust_ca_cn,
            verifying_ca=verifying_ca,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fctems_override import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/endpoint_control/fctems_override",
            )
        
        ems_id_value = payload_data.get("ems-id")
        if not ems_id_value:
            raise ValueError("ems-id is required for PUT")
        endpoint = "/endpoint-control/fctems-override/" + str(ems_id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        ems_id: int | None = None,
        status: str | None = None,
        name: str | None = None,
        dirty_reason: str | None = None,
        fortinetone_cloud_authentication: str | None = None,
        cloud_authentication_access_key: Any | None = None,
        server: str | None = None,
        https_port: int | None = None,
        serial_number: str | None = None,
        tenant_id: str | None = None,
        source_ip: str | None = None,
        pull_sysinfo: str | None = None,
        pull_vulnerabilities: str | None = None,
        pull_tags: str | None = None,
        pull_malware_hash: str | None = None,
        capabilities: str | list | None = None,
        call_timeout: int | None = None,
        out_of_sync_threshold: int | None = None,
        send_tags_to_all_vdoms: str | None = None,
        websocket_override: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        trust_ca_cn: str | None = None,
        verifying_ca: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new endpoint_control/fctems_override object.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            ems_id: EMS ID in order (1 - 7).
            status: Enable or disable this EMS configuration.
            name: FortiClient Enterprise Management Server (EMS) name.
            dirty_reason: Dirty Reason for FortiClient EMS.
            fortinetone_cloud_authentication: Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned ems-id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created ems-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = FctemsOverride.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(FctemsOverride.required_fields()) }}
            
            Use FctemsOverride.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            ems_id=ems_id,
            status=status,
            name=name,
            dirty_reason=dirty_reason,
            fortinetone_cloud_authentication=fortinetone_cloud_authentication,
            cloud_authentication_access_key=cloud_authentication_access_key,
            server=server,
            https_port=https_port,
            serial_number=serial_number,
            tenant_id=tenant_id,
            source_ip=source_ip,
            pull_sysinfo=pull_sysinfo,
            pull_vulnerabilities=pull_vulnerabilities,
            pull_tags=pull_tags,
            pull_malware_hash=pull_malware_hash,
            capabilities=capabilities,
            call_timeout=call_timeout,
            out_of_sync_threshold=out_of_sync_threshold,
            send_tags_to_all_vdoms=send_tags_to_all_vdoms,
            websocket_override=websocket_override,
            interface_select_method=interface_select_method,
            interface=interface,
            trust_ca_cn=trust_ca_cn,
            verifying_ca=verifying_ca,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.fctems_override import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/endpoint_control/fctems_override",
            )

        endpoint = "/endpoint-control/fctems-override"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        ems_id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete endpoint_control/fctems_override object.

        Configure FortiClient Enterprise Management Server (EMS) entries.

        Args:
            ems_id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If ems-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.delete(ems_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not ems_id:
            raise ValueError("ems-id is required for DELETE")
        endpoint = "/endpoint-control/fctems-override/" + str(ems_id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        ems_id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if endpoint_control/fctems_override object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            ems_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.endpoint_control_fctems_override.exists(ems_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.endpoint_control_fctems_override.exists(ems_id=1):
            ...     fgt.api.cmdb.endpoint_control_fctems_override.delete(ems_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(ems_id=ems_id, vdom=vdom, raw_json=True)
            
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
        Create or update endpoint_control/fctems_override object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (ems-id) in the payload.

        Args:
            payload_dict: Resource data including ems-id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If ems-id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "ems-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.endpoint_control_fctems_override.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.endpoint_control_fctems_override.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("ems-id")
        if not mkey_value:
            raise ValueError("ems-id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(ems_id=mkey_value, vdom=vdom):
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
            >>> print(FctemsOverride.help())
            
            >>> # Get field information
            >>> print(FctemsOverride.help("ems-id"))
        """
        from ._helpers.fctems_override import (
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
            >>> fields = FctemsOverride.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = FctemsOverride.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.fctems_override import get_all_fields, get_field_metadata

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
            >>> info = FctemsOverride.field_info("ems-id")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.fctems_override import get_field_metadata

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
            >>> is_valid, error = FctemsOverride.validate_field("ems-id", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.fctems_override import validate_field_value

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
            >>> required = FctemsOverride.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.fctems_override import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = FctemsOverride.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.fctems_override import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = FctemsOverride.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.fctems_override import get_schema_info

        return get_schema_info()
