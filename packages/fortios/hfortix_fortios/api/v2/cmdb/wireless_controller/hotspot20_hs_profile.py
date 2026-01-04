"""
FortiOS CMDB - Wireless Controller hotspot20_hs_profile

Configuration endpoint for managing cmdb wireless-controller/hotspot20_hs_profile objects.

API Endpoints:
    GET    /cmdb/wireless-controller/hotspot20_hs_profile
    POST   /cmdb/wireless-controller/hotspot20_hs_profile
    PUT    /cmdb/wireless-controller/hotspot20_hs_profile/{identifier}
    DELETE /cmdb/wireless-controller/hotspot20_hs_profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get()

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


class Hotspot20HsProfile:
    """Hotspot20HsProfile Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Hotspot20HsProfile endpoint."""
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
        Retrieve wireless-controller/hotspot20_hs_profile configuration.

        Configure hotspot profile.

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
            >>> # Get all wireless-controller/hotspot20_hs_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless-controller/hotspot20_hs_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get(action="schema")

        See Also:
            - post(): Create new wireless-controller/hotspot20_hs_profile object
            - put(): Update existing wireless-controller/hotspot20_hs_profile object
            - delete(): Remove wireless-controller/hotspot20_hs_profile object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/wireless-controller.hotspot20/hs-profile/" + str(name)
        else:
            endpoint = "/wireless-controller.hotspot20/hs-profile"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        release: int | None = None,
        access_network_type: str | None = None,
        access_network_internet: str | None = None,
        access_network_asra: str | None = None,
        access_network_esr: str | None = None,
        access_network_uesa: str | None = None,
        venue_group: str | None = None,
        venue_type: str | None = None,
        hessid: str | None = None,
        proxy_arp: str | None = None,
        l2tif: str | None = None,
        pame_bi: str | None = None,
        anqp_domain_id: int | None = None,
        domain_name: str | None = None,
        osu_ssid: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        dgaf: str | None = None,
        deauth_request_timeout: int | None = None,
        wnm_sleep_mode: str | None = None,
        bss_transition: str | None = None,
        venue_name: str | None = None,
        venue_url: str | None = None,
        roaming_consortium: str | None = None,
        nai_realm: str | None = None,
        oper_friendly_name: str | None = None,
        oper_icon: str | None = None,
        advice_of_charge: str | None = None,
        osu_provider_nai: str | None = None,
        terms_and_conditions: str | None = None,
        osu_provider: str | list | None = None,
        wan_metrics: str | None = None,
        network_auth: str | None = None,
        x3gpp_plmn: str | None = None,
        conn_cap: str | None = None,
        qos_map: str | None = None,
        ip_addr_type: str | None = None,
        wba_open_roaming: str | None = None,
        wba_financial_clearing_provider: str | None = None,
        wba_data_clearing_provider: str | None = None,
        wba_charging_currency: str | None = None,
        wba_charging_rate: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless-controller/hotspot20_hs_profile object.

        Configure hotspot profile.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Hotspot profile name.
            release: Hotspot 2.0 Release number (1, 2, 3, default = 2).
            access_network_type: Access network type.
            access_network_internet: Enable/disable connectivity to the Internet.
            access_network_asra: Enable/disable additional step required for access (ASRA).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            release=release,
            access_network_type=access_network_type,
            access_network_internet=access_network_internet,
            access_network_asra=access_network_asra,
            access_network_esr=access_network_esr,
            access_network_uesa=access_network_uesa,
            venue_group=venue_group,
            venue_type=venue_type,
            hessid=hessid,
            proxy_arp=proxy_arp,
            l2tif=l2tif,
            pame_bi=pame_bi,
            anqp_domain_id=anqp_domain_id,
            domain_name=domain_name,
            osu_ssid=osu_ssid,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            dgaf=dgaf,
            deauth_request_timeout=deauth_request_timeout,
            wnm_sleep_mode=wnm_sleep_mode,
            bss_transition=bss_transition,
            venue_name=venue_name,
            venue_url=venue_url,
            roaming_consortium=roaming_consortium,
            nai_realm=nai_realm,
            oper_friendly_name=oper_friendly_name,
            oper_icon=oper_icon,
            advice_of_charge=advice_of_charge,
            osu_provider_nai=osu_provider_nai,
            terms_and_conditions=terms_and_conditions,
            osu_provider=osu_provider,
            wan_metrics=wan_metrics,
            network_auth=network_auth,
            x3gpp_plmn=x3gpp_plmn,
            conn_cap=conn_cap,
            qos_map=qos_map,
            ip_addr_type=ip_addr_type,
            wba_open_roaming=wba_open_roaming,
            wba_financial_clearing_provider=wba_financial_clearing_provider,
            wba_data_clearing_provider=wba_data_clearing_provider,
            wba_charging_currency=wba_charging_currency,
            wba_charging_rate=wba_charging_rate,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.hotspot20_hs_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless-controller/hotspot20_hs_profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller.hotspot20/hs-profile/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        release: int | None = None,
        access_network_type: str | None = None,
        access_network_internet: str | None = None,
        access_network_asra: str | None = None,
        access_network_esr: str | None = None,
        access_network_uesa: str | None = None,
        venue_group: str | None = None,
        venue_type: str | None = None,
        hessid: str | None = None,
        proxy_arp: str | None = None,
        l2tif: str | None = None,
        pame_bi: str | None = None,
        anqp_domain_id: int | None = None,
        domain_name: str | None = None,
        osu_ssid: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        dgaf: str | None = None,
        deauth_request_timeout: int | None = None,
        wnm_sleep_mode: str | None = None,
        bss_transition: str | None = None,
        venue_name: str | None = None,
        venue_url: str | None = None,
        roaming_consortium: str | None = None,
        nai_realm: str | None = None,
        oper_friendly_name: str | None = None,
        oper_icon: str | None = None,
        advice_of_charge: str | None = None,
        osu_provider_nai: str | None = None,
        terms_and_conditions: str | None = None,
        osu_provider: str | list | None = None,
        wan_metrics: str | None = None,
        network_auth: str | None = None,
        x3gpp_plmn: str | None = None,
        conn_cap: str | None = None,
        qos_map: str | None = None,
        ip_addr_type: str | None = None,
        wba_open_roaming: str | None = None,
        wba_financial_clearing_provider: str | None = None,
        wba_data_clearing_provider: str | None = None,
        wba_charging_currency: str | None = None,
        wba_charging_rate: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless-controller/hotspot20_hs_profile object.

        Configure hotspot profile.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Hotspot profile name.
            release: Hotspot 2.0 Release number (1, 2, 3, default = 2).
            access_network_type: Access network type.
            access_network_internet: Enable/disable connectivity to the Internet.
            access_network_asra: Enable/disable additional step required for access (ASRA).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Hotspot20HsProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Hotspot20HsProfile.required_fields()) }}
            
            Use Hotspot20HsProfile.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            release=release,
            access_network_type=access_network_type,
            access_network_internet=access_network_internet,
            access_network_asra=access_network_asra,
            access_network_esr=access_network_esr,
            access_network_uesa=access_network_uesa,
            venue_group=venue_group,
            venue_type=venue_type,
            hessid=hessid,
            proxy_arp=proxy_arp,
            l2tif=l2tif,
            pame_bi=pame_bi,
            anqp_domain_id=anqp_domain_id,
            domain_name=domain_name,
            osu_ssid=osu_ssid,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            dgaf=dgaf,
            deauth_request_timeout=deauth_request_timeout,
            wnm_sleep_mode=wnm_sleep_mode,
            bss_transition=bss_transition,
            venue_name=venue_name,
            venue_url=venue_url,
            roaming_consortium=roaming_consortium,
            nai_realm=nai_realm,
            oper_friendly_name=oper_friendly_name,
            oper_icon=oper_icon,
            advice_of_charge=advice_of_charge,
            osu_provider_nai=osu_provider_nai,
            terms_and_conditions=terms_and_conditions,
            osu_provider=osu_provider,
            wan_metrics=wan_metrics,
            network_auth=network_auth,
            x3gpp_plmn=x3gpp_plmn,
            conn_cap=conn_cap,
            qos_map=qos_map,
            ip_addr_type=ip_addr_type,
            wba_open_roaming=wba_open_roaming,
            wba_financial_clearing_provider=wba_financial_clearing_provider,
            wba_data_clearing_provider=wba_data_clearing_provider,
            wba_charging_currency=wba_charging_currency,
            wba_charging_rate=wba_charging_rate,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.hotspot20_hs_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless-controller/hotspot20_hs_profile",
            )

        endpoint = "/wireless-controller.hotspot20/hs-profile"
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
        Delete wireless-controller/hotspot20_hs_profile object.

        Configure hotspot profile.

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
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller.hotspot20/hs-profile/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless-controller/hotspot20_hs_profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.delete(name=1)

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
        Create or update wireless-controller/hotspot20_hs_profile object (intelligent operation).

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
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.set(payload_dict=obj_data)
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
            >>> print(Hotspot20HsProfile.help())
            
            >>> # Get field information
            >>> print(Hotspot20HsProfile.help("name"))
        """
        from ._helpers.hotspot20_hs_profile import (
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
            >>> fields = Hotspot20HsProfile.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Hotspot20HsProfile.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.hotspot20_hs_profile import get_all_fields, get_field_metadata

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
            >>> info = Hotspot20HsProfile.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.hotspot20_hs_profile import get_field_metadata

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
            >>> is_valid, error = Hotspot20HsProfile.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.hotspot20_hs_profile import validate_field_value

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
            >>> required = Hotspot20HsProfile.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.hotspot20_hs_profile import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Hotspot20HsProfile.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.hotspot20_hs_profile import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Hotspot20HsProfile.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.hotspot20_hs_profile import get_schema_info

        return get_schema_info()
