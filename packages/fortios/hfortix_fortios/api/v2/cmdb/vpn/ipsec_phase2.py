"""
FortiOS CMDB - Vpn ipsec_phase2

Configuration endpoint for managing cmdb vpn/ipsec_phase2 objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec_phase2
    POST   /cmdb/vpn/ipsec_phase2
    PUT    /cmdb/vpn/ipsec_phase2/{identifier}
    DELETE /cmdb/vpn/ipsec_phase2/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_ipsec_phase2.get()

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


class IpsecPhase2:
    """IpsecPhase2 Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize IpsecPhase2 endpoint."""
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
        Retrieve vpn/ipsec_phase2 configuration.

        Configure VPN autokey tunnel.

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
            >>> # Get all vpn/ipsec_phase2 objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec_phase2 by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase2.get(action="schema")

        See Also:
            - post(): Create new vpn/ipsec_phase2 object
            - put(): Update existing vpn/ipsec_phase2 object
            - delete(): Remove vpn/ipsec_phase2 object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/vpn.ipsec/phase2/" + str(name)
        else:
            endpoint = "/vpn.ipsec/phase2"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        phase1name: str | None = None,
        dhcp_ipsec: str | None = None,
        use_natip: str | None = None,
        selector_match: str | None = None,
        proposal: str | None = None,
        pfs: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
        replay: str | None = None,
        keepalive: str | None = None,
        auto_negotiate: str | None = None,
        add_route: str | None = None,
        inbound_dscp_copy: str | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: str | None = None,
        single_source: str | None = None,
        route_overlap: str | None = None,
        encapsulation: str | None = None,
        l2tp: str | None = None,
        comments: str | None = None,
        initiator_ts_narrow: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: str | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: str | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing vpn/ipsec_phase2 object.

        Configure VPN autokey tunnel.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IPsec tunnel name.
            phase1name: Phase 1 determines the options required for phase 2.
            dhcp_ipsec: Enable/disable DHCP-IPsec.
            use_natip: Enable to use the FortiGate public IP as the source selector when outbound NAT is used.
            selector_match: Match type to use when comparing selectors.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            use_natip=use_natip,
            selector_match=selector_match,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ipsec_phase2 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec_phase2",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/vpn.ipsec/phase2/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        phase1name: str | None = None,
        dhcp_ipsec: str | None = None,
        use_natip: str | None = None,
        selector_match: str | None = None,
        proposal: str | None = None,
        pfs: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
        replay: str | None = None,
        keepalive: str | None = None,
        auto_negotiate: str | None = None,
        add_route: str | None = None,
        inbound_dscp_copy: str | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: str | None = None,
        single_source: str | None = None,
        route_overlap: str | None = None,
        encapsulation: str | None = None,
        l2tp: str | None = None,
        comments: str | None = None,
        initiator_ts_narrow: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: str | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: str | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new vpn/ipsec_phase2 object.

        Configure VPN autokey tunnel.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IPsec tunnel name.
            phase1name: Phase 1 determines the options required for phase 2.
            dhcp_ipsec: Enable/disable DHCP-IPsec.
            use_natip: Enable to use the FortiGate public IP as the source selector when outbound NAT is used.
            selector_match: Match type to use when comparing selectors.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = IpsecPhase2.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(IpsecPhase2.required_fields()) }}
            
            Use IpsecPhase2.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            use_natip=use_natip,
            selector_match=selector_match,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.ipsec_phase2 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec_phase2",
            )

        endpoint = "/vpn.ipsec/phase2"
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
        Delete vpn/ipsec_phase2 object.

        Configure VPN autokey tunnel.

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/vpn.ipsec/phase2/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if vpn/ipsec_phase2 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.vpn_ipsec_phase2.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.vpn_ipsec_phase2.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase2.delete(name=1)

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
        Create or update vpn/ipsec_phase2 object (intelligent operation).

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.vpn_ipsec_phase2.set(payload_dict=obj_data)
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
            >>> print(IpsecPhase2.help())
            
            >>> # Get field information
            >>> print(IpsecPhase2.help("name"))
        """
        from ._helpers.ipsec_phase2 import (
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
            >>> fields = IpsecPhase2.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = IpsecPhase2.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.ipsec_phase2 import get_all_fields, get_field_metadata

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
            >>> info = IpsecPhase2.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.ipsec_phase2 import get_field_metadata

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
            >>> is_valid, error = IpsecPhase2.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.ipsec_phase2 import validate_field_value

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
            >>> required = IpsecPhase2.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.ipsec_phase2 import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = IpsecPhase2.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.ipsec_phase2 import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = IpsecPhase2.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.ipsec_phase2 import get_schema_info

        return get_schema_info()
