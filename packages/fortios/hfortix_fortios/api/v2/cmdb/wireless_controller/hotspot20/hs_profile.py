"""
FortiOS CMDB - Wireless_controller hotspot20 hs_profile

Configuration endpoint for managing cmdb wireless_controller/hotspot20/hs_profile objects.

API Endpoints:
    GET    /cmdb/wireless_controller/hotspot20/hs_profile
    POST   /cmdb/wireless_controller/hotspot20/hs_profile
    PUT    /cmdb/wireless_controller/hotspot20/hs_profile/{identifier}
    DELETE /cmdb/wireless_controller/hotspot20/hs_profile/{identifier}

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


class HsProfile(MetadataMixin):
    """HsProfile Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "hs_profile"
    
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
        """Initialize HsProfile endpoint."""
        self._client = client

    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve wireless_controller/hotspot20/hs_profile configuration.

        Configure hotspot profile.

        Args:
            name: String identifier to retrieve specific object.
                If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional query parameters passed directly to API.

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
            >>> # Get all wireless_controller/hotspot20/hs_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/hotspot20/hs_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get_schema()

        See Also:
            - post(): Create new wireless_controller/hotspot20/hs_profile object
            - put(): Update existing wireless_controller/hotspot20/hs_profile object
            - delete(): Remove wireless_controller/hotspot20/hs_profile object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        
        if name:
            endpoint = "/wireless-controller.hotspot20/hs-profile/" + str(name)
        else:
            endpoint = "/wireless-controller.hotspot20/hs-profile"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        release: int | None = None,
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = None,
        access_network_internet: Literal["enable", "disable"] | None = None,
        access_network_asra: Literal["enable", "disable"] | None = None,
        access_network_esr: Literal["enable", "disable"] | None = None,
        access_network_uesa: Literal["enable", "disable"] | None = None,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = None,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = None,
        hessid: str | None = None,
        proxy_arp: Literal["enable", "disable"] | None = None,
        l2tif: Literal["enable", "disable"] | None = None,
        pame_bi: Literal["disable", "enable"] | None = None,
        anqp_domain_id: int | None = None,
        domain_name: str | None = None,
        osu_ssid: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        dgaf: Literal["enable", "disable"] | None = None,
        deauth_request_timeout: int | None = None,
        wnm_sleep_mode: Literal["enable", "disable"] | None = None,
        bss_transition: Literal["enable", "disable"] | None = None,
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
        wba_open_roaming: Literal["disable", "enable"] | None = None,
        wba_financial_clearing_provider: str | None = None,
        wba_data_clearing_provider: str | None = None,
        wba_charging_currency: str | None = None,
        wba_charging_rate: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/hotspot20/hs_profile object.

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
        from ._helpers.hs_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/hotspot20/hs_profile",
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
        access_network_type: Literal["private-network", "private-network-with-guest-access", "chargeable-public-network", "free-public-network", "personal-device-network", "emergency-services-only-network", "test-or-experimental", "wildcard"] | None = None,
        access_network_internet: Literal["enable", "disable"] | None = None,
        access_network_asra: Literal["enable", "disable"] | None = None,
        access_network_esr: Literal["enable", "disable"] | None = None,
        access_network_uesa: Literal["enable", "disable"] | None = None,
        venue_group: Literal["unspecified", "assembly", "business", "educational", "factory", "institutional", "mercantile", "residential", "storage", "utility", "vehicular", "outdoor"] | None = None,
        venue_type: Literal["unspecified", "arena", "stadium", "passenger-terminal", "amphitheater", "amusement-park", "place-of-worship", "convention-center", "library", "museum", "restaurant", "theater", "bar", "coffee-shop", "zoo-or-aquarium", "emergency-center", "doctor-office", "bank", "fire-station", "police-station", "post-office", "professional-office", "research-facility", "attorney-office", "primary-school", "secondary-school", "university-or-college", "factory", "hospital", "long-term-care-facility", "rehab-center", "group-home", "prison-or-jail", "retail-store", "grocery-market", "auto-service-station", "shopping-mall", "gas-station", "private", "hotel-or-motel", "dormitory", "boarding-house", "automobile", "airplane", "bus", "ferry", "ship-or-boat", "train", "motor-bike", "muni-mesh-network", "city-park", "rest-area", "traffic-control", "bus-stop", "kiosk"] | None = None,
        hessid: str | None = None,
        proxy_arp: Literal["enable", "disable"] | None = None,
        l2tif: Literal["enable", "disable"] | None = None,
        pame_bi: Literal["disable", "enable"] | None = None,
        anqp_domain_id: int | None = None,
        domain_name: str | None = None,
        osu_ssid: str | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        dgaf: Literal["enable", "disable"] | None = None,
        deauth_request_timeout: int | None = None,
        wnm_sleep_mode: Literal["enable", "disable"] | None = None,
        bss_transition: Literal["enable", "disable"] | None = None,
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
        wba_open_roaming: Literal["disable", "enable"] | None = None,
        wba_financial_clearing_provider: str | None = None,
        wba_data_clearing_provider: str | None = None,
        wba_charging_currency: str | None = None,
        wba_charging_rate: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/hotspot20/hs_profile object.

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
            >>> payload = HsProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(HsProfile.required_fields()) }}
            
            Use HsProfile.help('field_name') to get field details.

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
        from ._helpers.hs_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/hotspot20/hs_profile",
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
        Delete wireless_controller/hotspot20/hs_profile object.

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
        Check if wireless_controller/hotspot20/hs_profile object exists.

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
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
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
        Create or update wireless_controller/hotspot20/hs_profile object (intelligent operation).

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
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move wireless_controller/hotspot20/hs_profile object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller.hotspot20/hs-profile",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone wireless_controller/hotspot20/hs_profile object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller.hotspot20/hs-profile",
            params={
                "name": name,
                "new_name": new_name,
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
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if wireless_controller/hotspot20/hs_profile object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_hotspot20_hs_profile.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
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

