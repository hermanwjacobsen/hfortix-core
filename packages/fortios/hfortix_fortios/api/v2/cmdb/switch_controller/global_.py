"""
FortiOS CMDB - Switch_controller global_

Configuration endpoint for managing cmdb switch_controller/global_ objects.

API Endpoints:
    GET    /cmdb/switch_controller/global_
    POST   /cmdb/switch_controller/global_
    PUT    /cmdb/switch_controller/global_/{identifier}
    DELETE /cmdb/switch_controller/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_global_.get()

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
        Retrieve switch_controller/global_ configuration.

        Configure FortiSwitch global settings.

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
            >>> # Get all switch_controller/global_ objects
            >>> result = fgt.api.cmdb.switch_controller_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_global_.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_global_.get(action="schema")

        See Also:
            - post(): Create new switch_controller/global_ object
            - put(): Update existing switch_controller/global_ object
            - delete(): Remove switch_controller/global_ object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller/global/{name}"
        else:
            endpoint = "/switch-controller/global"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        mac_aging_interval: int | None = None,
        https_image_push: str | None = None,
        vlan_all_mode: str | None = None,
        vlan_optimization: str | None = None,
        vlan_identity: str | None = None,
        disable_discovery: str | list | None = None,
        mac_retention_period: int | None = None,
        default_virtual_switch_vlan: str | None = None,
        dhcp_server_access_list: str | None = None,
        dhcp_option82_format: str | None = None,
        dhcp_option82_circuit_id: str | list | None = None,
        dhcp_option82_remote_id: str | list | None = None,
        dhcp_snoop_client_req: str | None = None,
        dhcp_snoop_client_db_exp: int | None = None,
        dhcp_snoop_db_per_port_learn_limit: int | None = None,
        log_mac_limit_violations: str | None = None,
        mac_violation_timer: int | None = None,
        sn_dns_resolution: str | None = None,
        mac_event_logging: str | None = None,
        bounce_quarantined_link: str | None = None,
        quarantine_mode: str | None = None,
        update_user_device: str | list | None = None,
        custom_command: str | list | None = None,
        fips_enforce: str | None = None,
        firmware_provision_on_authorization: str | None = None,
        switch_on_deauth: str | None = None,
        firewall_auth_user_hold_period: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/global_ object.

        Configure FortiSwitch global settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            mac_aging_interval: Time after which an inactive MAC is aged out (10 - 1000000 sec, default = 300, 0 = disable).
            https_image_push: Enable/disable image push to FortiSwitch using HTTPS.
            vlan_all_mode: VLAN configuration mode, user-defined-vlans or all-possible-vlans.
            vlan_optimization: FortiLink VLAN optimization.
            vlan_identity: Identity of the VLAN. Commonly used for RADIUS Tunnel-Private-Group-Id.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            mac_aging_interval=mac_aging_interval,
            https_image_push=https_image_push,
            vlan_all_mode=vlan_all_mode,
            vlan_optimization=vlan_optimization,
            vlan_identity=vlan_identity,
            disable_discovery=disable_discovery,
            mac_retention_period=mac_retention_period,
            default_virtual_switch_vlan=default_virtual_switch_vlan,
            dhcp_server_access_list=dhcp_server_access_list,
            dhcp_option82_format=dhcp_option82_format,
            dhcp_option82_circuit_id=dhcp_option82_circuit_id,
            dhcp_option82_remote_id=dhcp_option82_remote_id,
            dhcp_snoop_client_req=dhcp_snoop_client_req,
            dhcp_snoop_client_db_exp=dhcp_snoop_client_db_exp,
            dhcp_snoop_db_per_port_learn_limit=dhcp_snoop_db_per_port_learn_limit,
            log_mac_limit_violations=log_mac_limit_violations,
            mac_violation_timer=mac_violation_timer,
            sn_dns_resolution=sn_dns_resolution,
            mac_event_logging=mac_event_logging,
            bounce_quarantined_link=bounce_quarantined_link,
            quarantine_mode=quarantine_mode,
            update_user_device=update_user_device,
            custom_command=custom_command,
            fips_enforce=fips_enforce,
            firmware_provision_on_authorization=firmware_provision_on_authorization,
            switch_on_deauth=switch_on_deauth,
            firewall_auth_user_hold_period=firewall_auth_user_hold_period,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/global_",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller/global/{name_value}"

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
            >>> print(Global.help("mac-aging-interval"))
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
            >>> info = Global.field_info("mac-aging-interval")
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
            >>> is_valid, error = Global.validate_field("mac-aging-interval", "test")
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
