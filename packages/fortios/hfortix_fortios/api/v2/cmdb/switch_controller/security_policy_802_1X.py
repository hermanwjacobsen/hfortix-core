"""
FortiOS CMDB - Switch Controller security_policy_802_1x

Configuration endpoint for managing cmdb switch-controller/security_policy_802_1X objects.

API Endpoints:
    GET    /cmdb/switch-controller/security_policy_802_1X
    POST   /cmdb/switch-controller/security_policy_802_1X
    PUT    /cmdb/switch-controller/security_policy_802_1X/{identifier}
    DELETE /cmdb/switch-controller/security_policy_802_1X/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_security_policy_802_1X.get()

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


class SecurityPolicy8021x:
    """SecurityPolicy8021x Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize SecurityPolicy8021x endpoint."""
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
        Retrieve switch-controller/security_policy_802_1X configuration.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

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
            >>> # Get all switch-controller/security_policy_802_1X objects
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific switch-controller/security_policy_802_1X by name
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_security_policy_802_1X.get(action="schema")

        See Also:
            - post(): Create new switch-controller/security_policy_802_1X object
            - put(): Update existing switch-controller/security_policy_802_1X object
            - delete(): Remove switch-controller/security_policy_802_1X object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/switch-controller.security-policy/802-1X/" + str(name)
        else:
            endpoint = "/switch-controller.security-policy/802-1X"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        security_mode: str | None = None,
        user_group: str | list | None = None,
        mac_auth_bypass: str | None = None,
        auth_order: str | None = None,
        auth_priority: str | None = None,
        open_auth: str | None = None,
        eap_passthru: str | None = None,
        eap_auto_untagged_vlans: str | None = None,
        guest_vlan: str | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: str | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: str | None = None,
        radius_timeout_overwrite: str | None = None,
        policy_type: str | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: str | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: str | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch-controller/security_policy_802_1X object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Policy name.
            security_mode: Port or MAC based 802.1X security mode.
            user_group: Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
            mac_auth_bypass: Enable/disable MAB for this policy.
            auth_order: Configure authentication order.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.security_policy_802_1X import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch-controller/security_policy_802_1X",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/switch-controller.security-policy/802-1X/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        security_mode: str | None = None,
        user_group: str | list | None = None,
        mac_auth_bypass: str | None = None,
        auth_order: str | None = None,
        auth_priority: str | None = None,
        open_auth: str | None = None,
        eap_passthru: str | None = None,
        eap_auto_untagged_vlans: str | None = None,
        guest_vlan: str | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: str | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: str | None = None,
        radius_timeout_overwrite: str | None = None,
        policy_type: str | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: str | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: str | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new switch-controller/security_policy_802_1X object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Policy name.
            security_mode: Port or MAC based 802.1X security mode.
            user_group: Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
            mac_auth_bypass: Enable/disable MAB for this policy.
            auth_order: Configure authentication order.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SecurityPolicy8021x.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SecurityPolicy8021x.required_fields()) }}
            
            Use SecurityPolicy8021x.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.security_policy_802_1X import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch-controller/security_policy_802_1X",
            )

        endpoint = "/switch-controller.security-policy/802-1X"
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
        Delete switch-controller/security_policy_802_1X object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

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
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/switch-controller.security-policy/802-1X/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if switch-controller/security_policy_802_1X object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.switch_controller_security_policy_802_1X.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.switch_controller_security_policy_802_1X.exists(name=1):
            ...     fgt.api.cmdb.switch_controller_security_policy_802_1X.delete(name=1)

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
        Create or update switch-controller/security_policy_802_1X object (intelligent operation).

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
            >>> result = fgt.api.cmdb.switch_controller_security_policy_802_1X.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.switch_controller_security_policy_802_1X.set(payload_dict=obj_data)
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
            >>> print(SecurityPolicy8021x.help())
            
            >>> # Get field information
            >>> print(SecurityPolicy8021x.help("name"))
        """
        from ._helpers.security_policy_802_1X import (
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
            >>> fields = SecurityPolicy8021x.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = SecurityPolicy8021x.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.security_policy_802_1X import get_all_fields, get_field_metadata

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
            >>> info = SecurityPolicy8021x.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.security_policy_802_1X import get_field_metadata

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
            >>> is_valid, error = SecurityPolicy8021x.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.security_policy_802_1X import validate_field_value

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
            >>> required = SecurityPolicy8021x.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.security_policy_802_1X import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = SecurityPolicy8021x.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.security_policy_802_1X import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = SecurityPolicy8021x.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.security_policy_802_1X import get_schema_info

        return get_schema_info()
