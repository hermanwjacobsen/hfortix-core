"""
FortiOS CMDB - Wireless_controller wids_profile

Configuration endpoint for managing cmdb wireless_controller/wids_profile objects.

API Endpoints:
    GET    /cmdb/wireless_controller/wids_profile
    POST   /cmdb/wireless_controller/wids_profile
    PUT    /cmdb/wireless_controller/wids_profile/{identifier}
    DELETE /cmdb/wireless_controller/wids_profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_wids_profile.get()

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


class WidsProfile:
    """WidsProfile Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize WidsProfile endpoint."""
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
        Retrieve wireless_controller/wids_profile configuration.

        Configure wireless intrusion detection system (WIDS) profiles.

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
            >>> # Get all wireless_controller/wids_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/wids_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_wids_profile.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/wids_profile object
            - put(): Update existing wireless_controller/wids_profile object
            - delete(): Remove wireless_controller/wids_profile object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/wireless-controller/wids-profile/" + str(name)
        else:
            endpoint = "/wireless-controller/wids-profile"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        sensor_mode: str | None = None,
        ap_scan: str | None = None,
        ap_scan_channel_list_2G_5G: str | list | None = None,
        ap_scan_channel_list_6G: str | list | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: str | list | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: str | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: str | None = None,
        wireless_bridge: str | None = None,
        deauth_broadcast: str | None = None,
        null_ssid_probe_resp: str | None = None,
        long_duration_attack: str | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: str | None = None,
        weak_wep_iv: str | None = None,
        auth_frame_flood: str | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: str | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: str | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: str | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: str | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: str | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: str | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: str | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: str | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: str | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: str | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: str | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: str | None = None,
        asleap_attack: str | None = None,
        eapol_start_flood: str | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: str | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: str | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: str | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: str | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: str | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: str | None = None,
        disassoc_broadcast: str | None = None,
        ap_spoofing: str | None = None,
        chan_based_mitm: str | None = None,
        adhoc_valid_ssid: str | None = None,
        adhoc_network: str | None = None,
        eapol_key_overflow: str | None = None,
        ap_impersonation: str | None = None,
        invalid_addr_combination: str | None = None,
        beacon_wrong_channel: str | None = None,
        ht_greenfield: str | None = None,
        overflow_ie: str | None = None,
        malformed_ht_ie: str | None = None,
        malformed_auth: str | None = None,
        malformed_association: str | None = None,
        ht_40mhz_intolerance: str | None = None,
        valid_ssid_misuse: str | None = None,
        valid_client_misassociation: str | None = None,
        hotspotter_attack: str | None = None,
        pwsave_dos_attack: str | None = None,
        omerta_attack: str | None = None,
        disconnect_station: str | None = None,
        unencrypted_valid: str | None = None,
        fata_jack: str | None = None,
        risky_encryption: str | None = None,
        fuzzed_beacon: str | None = None,
        fuzzed_probe_request: str | None = None,
        fuzzed_probe_response: str | None = None,
        air_jack: str | None = None,
        wpa_ft_attack: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/wids_profile object.

        Configure wireless intrusion detection system (WIDS) profiles.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: WIDS profile name.
            comment: Comment.
            sensor_mode: Scan nearby WiFi stations (default = disable).
            ap_scan: Enable/disable rogue AP detection.
            ap_scan_channel_list_2G_5G: Selected ap scan channel list for 2.4G and 5G bands.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            comment=comment,
            sensor_mode=sensor_mode,
            ap_scan=ap_scan,
            ap_scan_channel_list_2G_5G=ap_scan_channel_list_2G_5G,
            ap_scan_channel_list_6G=ap_scan_channel_list_6G,
            ap_bgscan_period=ap_bgscan_period,
            ap_bgscan_intv=ap_bgscan_intv,
            ap_bgscan_duration=ap_bgscan_duration,
            ap_bgscan_idle=ap_bgscan_idle,
            ap_bgscan_report_intv=ap_bgscan_report_intv,
            ap_bgscan_disable_schedules=ap_bgscan_disable_schedules,
            ap_fgscan_report_intv=ap_fgscan_report_intv,
            ap_scan_passive=ap_scan_passive,
            ap_scan_threshold=ap_scan_threshold,
            ap_auto_suppress=ap_auto_suppress,
            wireless_bridge=wireless_bridge,
            deauth_broadcast=deauth_broadcast,
            null_ssid_probe_resp=null_ssid_probe_resp,
            long_duration_attack=long_duration_attack,
            long_duration_thresh=long_duration_thresh,
            invalid_mac_oui=invalid_mac_oui,
            weak_wep_iv=weak_wep_iv,
            auth_frame_flood=auth_frame_flood,
            auth_flood_time=auth_flood_time,
            auth_flood_thresh=auth_flood_thresh,
            assoc_frame_flood=assoc_frame_flood,
            assoc_flood_time=assoc_flood_time,
            assoc_flood_thresh=assoc_flood_thresh,
            reassoc_flood=reassoc_flood,
            reassoc_flood_time=reassoc_flood_time,
            reassoc_flood_thresh=reassoc_flood_thresh,
            probe_flood=probe_flood,
            probe_flood_time=probe_flood_time,
            probe_flood_thresh=probe_flood_thresh,
            bcn_flood=bcn_flood,
            bcn_flood_time=bcn_flood_time,
            bcn_flood_thresh=bcn_flood_thresh,
            rts_flood=rts_flood,
            rts_flood_time=rts_flood_time,
            rts_flood_thresh=rts_flood_thresh,
            cts_flood=cts_flood,
            cts_flood_time=cts_flood_time,
            cts_flood_thresh=cts_flood_thresh,
            client_flood=client_flood,
            client_flood_time=client_flood_time,
            client_flood_thresh=client_flood_thresh,
            block_ack_flood=block_ack_flood,
            block_ack_flood_time=block_ack_flood_time,
            block_ack_flood_thresh=block_ack_flood_thresh,
            pspoll_flood=pspoll_flood,
            pspoll_flood_time=pspoll_flood_time,
            pspoll_flood_thresh=pspoll_flood_thresh,
            netstumbler=netstumbler,
            netstumbler_time=netstumbler_time,
            netstumbler_thresh=netstumbler_thresh,
            wellenreiter=wellenreiter,
            wellenreiter_time=wellenreiter_time,
            wellenreiter_thresh=wellenreiter_thresh,
            spoofed_deauth=spoofed_deauth,
            asleap_attack=asleap_attack,
            eapol_start_flood=eapol_start_flood,
            eapol_start_thresh=eapol_start_thresh,
            eapol_start_intv=eapol_start_intv,
            eapol_logoff_flood=eapol_logoff_flood,
            eapol_logoff_thresh=eapol_logoff_thresh,
            eapol_logoff_intv=eapol_logoff_intv,
            eapol_succ_flood=eapol_succ_flood,
            eapol_succ_thresh=eapol_succ_thresh,
            eapol_succ_intv=eapol_succ_intv,
            eapol_fail_flood=eapol_fail_flood,
            eapol_fail_thresh=eapol_fail_thresh,
            eapol_fail_intv=eapol_fail_intv,
            eapol_pre_succ_flood=eapol_pre_succ_flood,
            eapol_pre_succ_thresh=eapol_pre_succ_thresh,
            eapol_pre_succ_intv=eapol_pre_succ_intv,
            eapol_pre_fail_flood=eapol_pre_fail_flood,
            eapol_pre_fail_thresh=eapol_pre_fail_thresh,
            eapol_pre_fail_intv=eapol_pre_fail_intv,
            deauth_unknown_src_thresh=deauth_unknown_src_thresh,
            windows_bridge=windows_bridge,
            disassoc_broadcast=disassoc_broadcast,
            ap_spoofing=ap_spoofing,
            chan_based_mitm=chan_based_mitm,
            adhoc_valid_ssid=adhoc_valid_ssid,
            adhoc_network=adhoc_network,
            eapol_key_overflow=eapol_key_overflow,
            ap_impersonation=ap_impersonation,
            invalid_addr_combination=invalid_addr_combination,
            beacon_wrong_channel=beacon_wrong_channel,
            ht_greenfield=ht_greenfield,
            overflow_ie=overflow_ie,
            malformed_ht_ie=malformed_ht_ie,
            malformed_auth=malformed_auth,
            malformed_association=malformed_association,
            ht_40mhz_intolerance=ht_40mhz_intolerance,
            valid_ssid_misuse=valid_ssid_misuse,
            valid_client_misassociation=valid_client_misassociation,
            hotspotter_attack=hotspotter_attack,
            pwsave_dos_attack=pwsave_dos_attack,
            omerta_attack=omerta_attack,
            disconnect_station=disconnect_station,
            unencrypted_valid=unencrypted_valid,
            fata_jack=fata_jack,
            risky_encryption=risky_encryption,
            fuzzed_beacon=fuzzed_beacon,
            fuzzed_probe_request=fuzzed_probe_request,
            fuzzed_probe_response=fuzzed_probe_response,
            air_jack=air_jack,
            wpa_ft_attack=wpa_ft_attack,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wids_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wids_profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/wids-profile/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        sensor_mode: str | None = None,
        ap_scan: str | None = None,
        ap_scan_channel_list_2G_5G: str | list | None = None,
        ap_scan_channel_list_6G: str | list | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: str | list | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: str | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: str | None = None,
        wireless_bridge: str | None = None,
        deauth_broadcast: str | None = None,
        null_ssid_probe_resp: str | None = None,
        long_duration_attack: str | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: str | None = None,
        weak_wep_iv: str | None = None,
        auth_frame_flood: str | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: str | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: str | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: str | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: str | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: str | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: str | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: str | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: str | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: str | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: str | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: str | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: str | None = None,
        asleap_attack: str | None = None,
        eapol_start_flood: str | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: str | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: str | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: str | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: str | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: str | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: str | None = None,
        disassoc_broadcast: str | None = None,
        ap_spoofing: str | None = None,
        chan_based_mitm: str | None = None,
        adhoc_valid_ssid: str | None = None,
        adhoc_network: str | None = None,
        eapol_key_overflow: str | None = None,
        ap_impersonation: str | None = None,
        invalid_addr_combination: str | None = None,
        beacon_wrong_channel: str | None = None,
        ht_greenfield: str | None = None,
        overflow_ie: str | None = None,
        malformed_ht_ie: str | None = None,
        malformed_auth: str | None = None,
        malformed_association: str | None = None,
        ht_40mhz_intolerance: str | None = None,
        valid_ssid_misuse: str | None = None,
        valid_client_misassociation: str | None = None,
        hotspotter_attack: str | None = None,
        pwsave_dos_attack: str | None = None,
        omerta_attack: str | None = None,
        disconnect_station: str | None = None,
        unencrypted_valid: str | None = None,
        fata_jack: str | None = None,
        risky_encryption: str | None = None,
        fuzzed_beacon: str | None = None,
        fuzzed_probe_request: str | None = None,
        fuzzed_probe_response: str | None = None,
        air_jack: str | None = None,
        wpa_ft_attack: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/wids_profile object.

        Configure wireless intrusion detection system (WIDS) profiles.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: WIDS profile name.
            comment: Comment.
            sensor_mode: Scan nearby WiFi stations (default = disable).
            ap_scan: Enable/disable rogue AP detection.
            ap_scan_channel_list_2G_5G: Selected ap scan channel list for 2.4G and 5G bands.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = WidsProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(WidsProfile.required_fields()) }}
            
            Use WidsProfile.help('field_name') to get field details.

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
            sensor_mode=sensor_mode,
            ap_scan=ap_scan,
            ap_scan_channel_list_2G_5G=ap_scan_channel_list_2G_5G,
            ap_scan_channel_list_6G=ap_scan_channel_list_6G,
            ap_bgscan_period=ap_bgscan_period,
            ap_bgscan_intv=ap_bgscan_intv,
            ap_bgscan_duration=ap_bgscan_duration,
            ap_bgscan_idle=ap_bgscan_idle,
            ap_bgscan_report_intv=ap_bgscan_report_intv,
            ap_bgscan_disable_schedules=ap_bgscan_disable_schedules,
            ap_fgscan_report_intv=ap_fgscan_report_intv,
            ap_scan_passive=ap_scan_passive,
            ap_scan_threshold=ap_scan_threshold,
            ap_auto_suppress=ap_auto_suppress,
            wireless_bridge=wireless_bridge,
            deauth_broadcast=deauth_broadcast,
            null_ssid_probe_resp=null_ssid_probe_resp,
            long_duration_attack=long_duration_attack,
            long_duration_thresh=long_duration_thresh,
            invalid_mac_oui=invalid_mac_oui,
            weak_wep_iv=weak_wep_iv,
            auth_frame_flood=auth_frame_flood,
            auth_flood_time=auth_flood_time,
            auth_flood_thresh=auth_flood_thresh,
            assoc_frame_flood=assoc_frame_flood,
            assoc_flood_time=assoc_flood_time,
            assoc_flood_thresh=assoc_flood_thresh,
            reassoc_flood=reassoc_flood,
            reassoc_flood_time=reassoc_flood_time,
            reassoc_flood_thresh=reassoc_flood_thresh,
            probe_flood=probe_flood,
            probe_flood_time=probe_flood_time,
            probe_flood_thresh=probe_flood_thresh,
            bcn_flood=bcn_flood,
            bcn_flood_time=bcn_flood_time,
            bcn_flood_thresh=bcn_flood_thresh,
            rts_flood=rts_flood,
            rts_flood_time=rts_flood_time,
            rts_flood_thresh=rts_flood_thresh,
            cts_flood=cts_flood,
            cts_flood_time=cts_flood_time,
            cts_flood_thresh=cts_flood_thresh,
            client_flood=client_flood,
            client_flood_time=client_flood_time,
            client_flood_thresh=client_flood_thresh,
            block_ack_flood=block_ack_flood,
            block_ack_flood_time=block_ack_flood_time,
            block_ack_flood_thresh=block_ack_flood_thresh,
            pspoll_flood=pspoll_flood,
            pspoll_flood_time=pspoll_flood_time,
            pspoll_flood_thresh=pspoll_flood_thresh,
            netstumbler=netstumbler,
            netstumbler_time=netstumbler_time,
            netstumbler_thresh=netstumbler_thresh,
            wellenreiter=wellenreiter,
            wellenreiter_time=wellenreiter_time,
            wellenreiter_thresh=wellenreiter_thresh,
            spoofed_deauth=spoofed_deauth,
            asleap_attack=asleap_attack,
            eapol_start_flood=eapol_start_flood,
            eapol_start_thresh=eapol_start_thresh,
            eapol_start_intv=eapol_start_intv,
            eapol_logoff_flood=eapol_logoff_flood,
            eapol_logoff_thresh=eapol_logoff_thresh,
            eapol_logoff_intv=eapol_logoff_intv,
            eapol_succ_flood=eapol_succ_flood,
            eapol_succ_thresh=eapol_succ_thresh,
            eapol_succ_intv=eapol_succ_intv,
            eapol_fail_flood=eapol_fail_flood,
            eapol_fail_thresh=eapol_fail_thresh,
            eapol_fail_intv=eapol_fail_intv,
            eapol_pre_succ_flood=eapol_pre_succ_flood,
            eapol_pre_succ_thresh=eapol_pre_succ_thresh,
            eapol_pre_succ_intv=eapol_pre_succ_intv,
            eapol_pre_fail_flood=eapol_pre_fail_flood,
            eapol_pre_fail_thresh=eapol_pre_fail_thresh,
            eapol_pre_fail_intv=eapol_pre_fail_intv,
            deauth_unknown_src_thresh=deauth_unknown_src_thresh,
            windows_bridge=windows_bridge,
            disassoc_broadcast=disassoc_broadcast,
            ap_spoofing=ap_spoofing,
            chan_based_mitm=chan_based_mitm,
            adhoc_valid_ssid=adhoc_valid_ssid,
            adhoc_network=adhoc_network,
            eapol_key_overflow=eapol_key_overflow,
            ap_impersonation=ap_impersonation,
            invalid_addr_combination=invalid_addr_combination,
            beacon_wrong_channel=beacon_wrong_channel,
            ht_greenfield=ht_greenfield,
            overflow_ie=overflow_ie,
            malformed_ht_ie=malformed_ht_ie,
            malformed_auth=malformed_auth,
            malformed_association=malformed_association,
            ht_40mhz_intolerance=ht_40mhz_intolerance,
            valid_ssid_misuse=valid_ssid_misuse,
            valid_client_misassociation=valid_client_misassociation,
            hotspotter_attack=hotspotter_attack,
            pwsave_dos_attack=pwsave_dos_attack,
            omerta_attack=omerta_attack,
            disconnect_station=disconnect_station,
            unencrypted_valid=unencrypted_valid,
            fata_jack=fata_jack,
            risky_encryption=risky_encryption,
            fuzzed_beacon=fuzzed_beacon,
            fuzzed_probe_request=fuzzed_probe_request,
            fuzzed_probe_response=fuzzed_probe_response,
            air_jack=air_jack,
            wpa_ft_attack=wpa_ft_attack,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wids_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wids_profile",
            )

        endpoint = "/wireless-controller/wids-profile"
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
        Delete wireless_controller/wids_profile object.

        Configure wireless intrusion detection system (WIDS) profiles.

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
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/wids-profile/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/wids_profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_wids_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_wids_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_wids_profile.delete(name=1)

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
        Create or update wireless_controller/wids_profile object (intelligent operation).

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
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_wids_profile.set(payload_dict=obj_data)
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
            >>> print(WidsProfile.help())
            
            >>> # Get field information
            >>> print(WidsProfile.help("name"))
        """
        from ._helpers.wids_profile import (
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
            >>> fields = WidsProfile.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = WidsProfile.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.wids_profile import get_all_fields, get_field_metadata

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
            >>> info = WidsProfile.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.wids_profile import get_field_metadata

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
            >>> is_valid, error = WidsProfile.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.wids_profile import validate_field_value

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
            >>> required = WidsProfile.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.wids_profile import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = WidsProfile.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.wids_profile import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = WidsProfile.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.wids_profile import get_schema_info

        return get_schema_info()
