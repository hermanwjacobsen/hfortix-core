"""
FortiOS CMDB - Wireless_controller wtp_profile

Configuration endpoint for managing cmdb wireless_controller/wtp_profile objects.

API Endpoints:
    GET    /cmdb/wireless_controller/wtp_profile
    POST   /cmdb/wireless_controller/wtp_profile
    PUT    /cmdb/wireless_controller/wtp_profile/{identifier}
    DELETE /cmdb/wireless_controller/wtp_profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_wtp_profile.get()

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


class WtpProfile:
    """WtpProfile Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize WtpProfile endpoint."""
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
        Retrieve wireless_controller/wtp_profile configuration.

        Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

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
            >>> # Get all wireless_controller/wtp_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/wtp_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_wtp_profile.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/wtp_profile object
            - put(): Update existing wireless_controller/wtp_profile object
            - delete(): Remove wireless_controller/wtp_profile object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/wireless-controller/wtp-profile/" + str(name)
        else:
            endpoint = "/wireless-controller/wtp-profile"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        platform: str | None = None,
        control_message_offload: str | None = None,
        bonjour_profile: str | None = None,
        apcfg_profile: str | None = None,
        apcfg_mesh: str | None = None,
        apcfg_mesh_ap_type: str | None = None,
        apcfg_mesh_ssid: str | None = None,
        apcfg_mesh_eth_bridge: str | None = None,
        ble_profile: str | None = None,
        syslog_profile: str | None = None,
        wan_port_mode: str | None = None,
        lan: str | None = None,
        energy_efficient_ethernet: str | None = None,
        led_state: str | None = None,
        led_schedules: str | list | None = None,
        dtls_policy: str | None = None,
        dtls_in_kernel: str | None = None,
        max_clients: int | None = None,
        handoff_rssi: int | None = None,
        handoff_sta_thresh: int | None = None,
        handoff_roaming: str | None = None,
        deny_mac_list: str | list | None = None,
        ap_country: str | None = None,
        ip_fragment_preventing: str | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        split_tunneling_acl_path: str | None = None,
        split_tunneling_acl_local_ap_subnet: str | None = None,
        split_tunneling_acl: str | list | None = None,
        allowaccess: str | None = None,
        login_passwd_change: str | None = None,
        login_passwd: Any | None = None,
        lldp: str | None = None,
        poe_mode: str | None = None,
        usb_port: str | None = None,
        frequency_handoff: str | None = None,
        ap_handoff: str | None = None,
        default_mesh_root: str | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        lbs: str | None = None,
        ext_info_enable: str | None = None,
        indoor_outdoor_deployment: str | None = None,
        esl_ses_dongle: str | None = None,
        console_login: str | None = None,
        wan_port_auth: str | None = None,
        wan_port_auth_usrname: str | None = None,
        wan_port_auth_password: Any | None = None,
        wan_port_auth_methods: str | None = None,
        wan_port_auth_macsec: str | None = None,
        unii_4_5ghz_band: str | None = None,
        admin_auth_tacacs_plus: str | None = None,
        admin_restrict_local: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/wtp_profile object.

        Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: WTP (or FortiAP or AP) profile name.
            comment: Comment.
            platform: WTP, FortiAP, or AP platform.
            control_message_offload: Enable/disable CAPWAP control message data channel offload.
            bonjour_profile: Bonjour profile name.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            comment=comment,
            platform=platform,
            control_message_offload=control_message_offload,
            bonjour_profile=bonjour_profile,
            apcfg_profile=apcfg_profile,
            apcfg_mesh=apcfg_mesh,
            apcfg_mesh_ap_type=apcfg_mesh_ap_type,
            apcfg_mesh_ssid=apcfg_mesh_ssid,
            apcfg_mesh_eth_bridge=apcfg_mesh_eth_bridge,
            ble_profile=ble_profile,
            syslog_profile=syslog_profile,
            wan_port_mode=wan_port_mode,
            lan=lan,
            energy_efficient_ethernet=energy_efficient_ethernet,
            led_state=led_state,
            led_schedules=led_schedules,
            dtls_policy=dtls_policy,
            dtls_in_kernel=dtls_in_kernel,
            max_clients=max_clients,
            handoff_rssi=handoff_rssi,
            handoff_sta_thresh=handoff_sta_thresh,
            handoff_roaming=handoff_roaming,
            deny_mac_list=deny_mac_list,
            ap_country=ap_country,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            allowaccess=allowaccess,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            lldp=lldp,
            poe_mode=poe_mode,
            usb_port=usb_port,
            frequency_handoff=frequency_handoff,
            ap_handoff=ap_handoff,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            lbs=lbs,
            ext_info_enable=ext_info_enable,
            indoor_outdoor_deployment=indoor_outdoor_deployment,
            esl_ses_dongle=esl_ses_dongle,
            console_login=console_login,
            wan_port_auth=wan_port_auth,
            wan_port_auth_usrname=wan_port_auth_usrname,
            wan_port_auth_password=wan_port_auth_password,
            wan_port_auth_methods=wan_port_auth_methods,
            wan_port_auth_macsec=wan_port_auth_macsec,
            unii_4_5ghz_band=unii_4_5ghz_band,
            admin_auth_tacacs_plus=admin_auth_tacacs_plus,
            admin_restrict_local=admin_restrict_local,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wtp_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wtp_profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/wtp-profile/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        platform: str | None = None,
        control_message_offload: str | None = None,
        bonjour_profile: str | None = None,
        apcfg_profile: str | None = None,
        apcfg_mesh: str | None = None,
        apcfg_mesh_ap_type: str | None = None,
        apcfg_mesh_ssid: str | None = None,
        apcfg_mesh_eth_bridge: str | None = None,
        ble_profile: str | None = None,
        syslog_profile: str | None = None,
        wan_port_mode: str | None = None,
        lan: str | None = None,
        energy_efficient_ethernet: str | None = None,
        led_state: str | None = None,
        led_schedules: str | list | None = None,
        dtls_policy: str | None = None,
        dtls_in_kernel: str | None = None,
        max_clients: int | None = None,
        handoff_rssi: int | None = None,
        handoff_sta_thresh: int | None = None,
        handoff_roaming: str | None = None,
        deny_mac_list: str | list | None = None,
        ap_country: str | None = None,
        ip_fragment_preventing: str | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        split_tunneling_acl_path: str | None = None,
        split_tunneling_acl_local_ap_subnet: str | None = None,
        split_tunneling_acl: str | list | None = None,
        allowaccess: str | None = None,
        login_passwd_change: str | None = None,
        login_passwd: Any | None = None,
        lldp: str | None = None,
        poe_mode: str | None = None,
        usb_port: str | None = None,
        frequency_handoff: str | None = None,
        ap_handoff: str | None = None,
        default_mesh_root: str | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        lbs: str | None = None,
        ext_info_enable: str | None = None,
        indoor_outdoor_deployment: str | None = None,
        esl_ses_dongle: str | None = None,
        console_login: str | None = None,
        wan_port_auth: str | None = None,
        wan_port_auth_usrname: str | None = None,
        wan_port_auth_password: Any | None = None,
        wan_port_auth_methods: str | None = None,
        wan_port_auth_macsec: str | None = None,
        unii_4_5ghz_band: str | None = None,
        admin_auth_tacacs_plus: str | None = None,
        admin_restrict_local: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/wtp_profile object.

        Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: WTP (or FortiAP or AP) profile name.
            comment: Comment.
            platform: WTP, FortiAP, or AP platform.
            control_message_offload: Enable/disable CAPWAP control message data channel offload.
            bonjour_profile: Bonjour profile name.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = WtpProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(WtpProfile.required_fields()) }}
            
            Use WtpProfile.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            comment=comment,
            platform=platform,
            control_message_offload=control_message_offload,
            bonjour_profile=bonjour_profile,
            apcfg_profile=apcfg_profile,
            apcfg_mesh=apcfg_mesh,
            apcfg_mesh_ap_type=apcfg_mesh_ap_type,
            apcfg_mesh_ssid=apcfg_mesh_ssid,
            apcfg_mesh_eth_bridge=apcfg_mesh_eth_bridge,
            ble_profile=ble_profile,
            syslog_profile=syslog_profile,
            wan_port_mode=wan_port_mode,
            lan=lan,
            energy_efficient_ethernet=energy_efficient_ethernet,
            led_state=led_state,
            led_schedules=led_schedules,
            dtls_policy=dtls_policy,
            dtls_in_kernel=dtls_in_kernel,
            max_clients=max_clients,
            handoff_rssi=handoff_rssi,
            handoff_sta_thresh=handoff_sta_thresh,
            handoff_roaming=handoff_roaming,
            deny_mac_list=deny_mac_list,
            ap_country=ap_country,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            allowaccess=allowaccess,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            lldp=lldp,
            poe_mode=poe_mode,
            usb_port=usb_port,
            frequency_handoff=frequency_handoff,
            ap_handoff=ap_handoff,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            lbs=lbs,
            ext_info_enable=ext_info_enable,
            indoor_outdoor_deployment=indoor_outdoor_deployment,
            esl_ses_dongle=esl_ses_dongle,
            console_login=console_login,
            wan_port_auth=wan_port_auth,
            wan_port_auth_usrname=wan_port_auth_usrname,
            wan_port_auth_password=wan_port_auth_password,
            wan_port_auth_methods=wan_port_auth_methods,
            wan_port_auth_macsec=wan_port_auth_macsec,
            unii_4_5ghz_band=unii_4_5ghz_band,
            admin_auth_tacacs_plus=admin_auth_tacacs_plus,
            admin_restrict_local=admin_restrict_local,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wtp_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wtp_profile",
            )

        endpoint = "/wireless-controller/wtp-profile"
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
        Delete wireless_controller/wtp_profile object.

        Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

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
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/wtp-profile/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/wtp_profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_wtp_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_wtp_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_wtp_profile.delete(name=1)

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
        Create or update wireless_controller/wtp_profile object (intelligent operation).

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
            >>> result = fgt.api.cmdb.wireless_controller_wtp_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_wtp_profile.set(payload_dict=obj_data)
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
            >>> print(WtpProfile.help())
            
            >>> # Get field information
            >>> print(WtpProfile.help("name"))
        """
        from ._helpers.wtp_profile import (
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
            >>> fields = WtpProfile.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = WtpProfile.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.wtp_profile import get_all_fields, get_field_metadata

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
            >>> info = WtpProfile.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.wtp_profile import get_field_metadata

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
            >>> is_valid, error = WtpProfile.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.wtp_profile import validate_field_value

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
            >>> required = WtpProfile.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.wtp_profile import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = WtpProfile.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.wtp_profile import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = WtpProfile.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.wtp_profile import get_schema_info

        return get_schema_info()
