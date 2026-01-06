"""
FortiOS CMDB - Wireless_controller wtp

Configuration endpoint for managing cmdb wireless_controller/wtp objects.

API Endpoints:
    GET    /cmdb/wireless_controller/wtp
    POST   /cmdb/wireless_controller/wtp
    PUT    /cmdb/wireless_controller/wtp/{identifier}
    DELETE /cmdb/wireless_controller/wtp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_wtp.get()

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, Literal
if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_cmdb_payload,
    is_success,
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin


class Wtp(MetadataMixin):
    """Wtp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "wtp"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Wtp endpoint."""
        self._client = client

    def get(
        self,
        wtp_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve wireless_controller/wtp configuration.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            wtp_id: String identifier to retrieve specific object.
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
            >>> # Get all wireless_controller/wtp objects
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/wtp by wtp-id
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get(wtp_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_wtp.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/wtp object
            - put(): Update existing wireless_controller/wtp object
            - delete(): Remove wireless_controller/wtp object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if wtp_id:
            endpoint = "/wireless-controller/wtp/" + str(wtp_id)
        else:
            endpoint = "/wireless-controller/wtp"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        wtp_id: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: Literal["discovered", "disable", "enable"] | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: Literal["enable", "disable"] | None = None,
        led_state: Literal["enable", "disable"] | None = None,
        override_wan_port_mode: Literal["enable", "disable"] | None = None,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = None,
        override_ip_fragment: Literal["enable", "disable"] | None = None,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: Literal["enable", "disable"] | None = None,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = None,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = None,
        split_tunneling_acl: str | list | None = None,
        override_lan: Literal["enable", "disable"] | None = None,
        lan: str | None = None,
        override_allowaccess: Literal["enable", "disable"] | None = None,
        allowaccess: Literal["https", "ssh", "snmp"] | list | None = None,
        override_login_passwd_change: Literal["enable", "disable"] | None = None,
        login_passwd_change: Literal["yes", "default", "no"] | None = None,
        login_passwd: Any | None = None,
        override_default_mesh_root: Literal["enable", "disable"] | None = None,
        default_mesh_root: Literal["enable", "disable"] | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        image_download: Literal["enable", "disable"] | None = None,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/wtp object.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            payload_dict: Object data as dict. Must include wtp-id (primary key).
            wtp_id: WTP ID.
            index: Index (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            admin: Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP.
            name: WTP, AP or FortiAP configuration name.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If wtp-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_wtp.put(
            ...     wtp_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "wtp-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wtp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            wtp_id=wtp_id,
            index=index,
            uuid=uuid,
            admin=admin,
            name=name,
            location=location,
            comment=comment,
            region=region,
            region_x=region_x,
            region_y=region_y,
            firmware_provision=firmware_provision,
            firmware_provision_latest=firmware_provision_latest,
            wtp_profile=wtp_profile,
            apcfg_profile=apcfg_profile,
            bonjour_profile=bonjour_profile,
            ble_major_id=ble_major_id,
            ble_minor_id=ble_minor_id,
            override_led_state=override_led_state,
            led_state=led_state,
            override_wan_port_mode=override_wan_port_mode,
            wan_port_mode=wan_port_mode,
            override_ip_fragment=override_ip_fragment,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            override_split_tunnel=override_split_tunnel,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            override_lan=override_lan,
            lan=lan,
            override_allowaccess=override_allowaccess,
            allowaccess=allowaccess,
            override_login_passwd_change=override_login_passwd_change,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            override_default_mesh_root=override_default_mesh_root,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            image_download=image_download,
            mesh_bridge_enable=mesh_bridge_enable,
            purdue_level=purdue_level,
            coordinate_latitude=coordinate_latitude,
            coordinate_longitude=coordinate_longitude,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wtp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wtp",
            )
        
        wtp_id_value = payload_data.get("wtp-id")
        if not wtp_id_value:
            raise ValueError("wtp-id is required for PUT")
        endpoint = "/wireless-controller/wtp/" + str(wtp_id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        wtp_id: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: Literal["discovered", "disable", "enable"] | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: Literal["enable", "disable"] | None = None,
        led_state: Literal["enable", "disable"] | None = None,
        override_wan_port_mode: Literal["enable", "disable"] | None = None,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = None,
        override_ip_fragment: Literal["enable", "disable"] | None = None,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: Literal["enable", "disable"] | None = None,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = None,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = None,
        split_tunneling_acl: str | list | None = None,
        override_lan: Literal["enable", "disable"] | None = None,
        lan: str | None = None,
        override_allowaccess: Literal["enable", "disable"] | None = None,
        allowaccess: Literal["https", "ssh", "snmp"] | list | None = None,
        override_login_passwd_change: Literal["enable", "disable"] | None = None,
        login_passwd_change: Literal["yes", "default", "no"] | None = None,
        login_passwd: Any | None = None,
        override_default_mesh_root: Literal["enable", "disable"] | None = None,
        default_mesh_root: Literal["enable", "disable"] | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        image_download: Literal["enable", "disable"] | None = None,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/wtp object.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            wtp_id: WTP ID.
            index: Index (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            admin: Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP.
            name: WTP, AP or FortiAP configuration name.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned wtp-id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_wtp.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created wtp-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Wtp.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_wtp.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Wtp.required_fields()) }}
            
            Use Wtp.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            wtp_id=wtp_id,
            index=index,
            uuid=uuid,
            admin=admin,
            name=name,
            location=location,
            comment=comment,
            region=region,
            region_x=region_x,
            region_y=region_y,
            firmware_provision=firmware_provision,
            firmware_provision_latest=firmware_provision_latest,
            wtp_profile=wtp_profile,
            apcfg_profile=apcfg_profile,
            bonjour_profile=bonjour_profile,
            ble_major_id=ble_major_id,
            ble_minor_id=ble_minor_id,
            override_led_state=override_led_state,
            led_state=led_state,
            override_wan_port_mode=override_wan_port_mode,
            wan_port_mode=wan_port_mode,
            override_ip_fragment=override_ip_fragment,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            override_split_tunnel=override_split_tunnel,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            override_lan=override_lan,
            lan=lan,
            override_allowaccess=override_allowaccess,
            allowaccess=allowaccess,
            override_login_passwd_change=override_login_passwd_change,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            override_default_mesh_root=override_default_mesh_root,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            image_download=image_download,
            mesh_bridge_enable=mesh_bridge_enable,
            purdue_level=purdue_level,
            coordinate_latitude=coordinate_latitude,
            coordinate_longitude=coordinate_longitude,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wtp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wtp",
            )

        endpoint = "/wireless-controller/wtp"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        wtp_id: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete wireless_controller/wtp object.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            wtp_id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If wtp-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.wireless_controller_wtp.delete(wtp_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not wtp_id:
            raise ValueError("wtp-id is required for DELETE")
        endpoint = "/wireless-controller/wtp/" + str(wtp_id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/wtp object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            wtp_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_wtp.exists(wtp_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_wtp.exists(wtp_id=1):
            ...     fgt.api.cmdb.wireless_controller_wtp.delete(wtp_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                wtp_id=wtp_id,
                vdom=vdom,
                raw_json=True
            )
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update wireless_controller/wtp object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (wtp-id) in the payload.

        Args:
            payload_dict: Resource data including wtp-id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If wtp-id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "wtp-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wtp.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_wtp.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("wtp-id")
        if not mkey_value:
            raise ValueError("wtp-id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(wtp_id=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        wtp_id: str,
        action: Literal["before", "after"],
        reference_wtp_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move wireless_controller/wtp object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            wtp_id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_wtp_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.wireless_controller_wtp.move(
            ...     wtp_id=100,
            ...     action="before",
            ...     reference_wtp_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/wtp",
            params={
                "wtp-id": wtp_id,
                "action": "move",
                action: reference_wtp_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        wtp_id: str,
        new_wtp_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone wireless_controller/wtp object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            wtp_id: Identifier of object to clone
            new_wtp_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.wireless_controller_wtp.clone(
            ...     wtp_id=1,
            ...     new_wtp_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/wtp",
            params={
                "wtp-id": wtp_id,
                "new_wtp-id": new_wtp_id,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if wireless_controller/wtp object exists.
        
        Args:
            wtp_id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_wtp.exists(wtp_id=1):
            ...     fgt.api.cmdb.wireless_controller_wtp.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                wtp_id=wtp_id,
                vdom=vdom,
                raw_json=True
            )
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

