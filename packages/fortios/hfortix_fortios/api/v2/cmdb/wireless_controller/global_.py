"""
FortiOS CMDB - Wireless_controller global_

Configuration endpoint for managing cmdb wireless_controller/global_ objects.

API Endpoints:
    GET    /cmdb/wireless_controller/global_
    POST   /cmdb/wireless_controller/global_
    PUT    /cmdb/wireless_controller/global_/{identifier}
    DELETE /cmdb/wireless_controller/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_global_.get()

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
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin


class Global(MetadataMixin):
    """Global Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "global_"

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
        Retrieve wireless_controller/global_ configuration.

        Configure wireless controller global settings.

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
            >>> # Get all wireless_controller/global_ objects
            >>> result = fgt.api.cmdb.wireless_controller_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_global_.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_global_.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/global_ object
            - put(): Update existing wireless_controller/global_ object
            - delete(): Remove wireless_controller/global_ object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/wireless-controller/global/{name}"
        else:
            endpoint = "/wireless-controller/global"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        location: str | None = None,
        acd_process_count: int | None = None,
        wpad_process_count: int | None = None,
        image_download: str | None = None,
        rolling_wtp_upgrade: str | None = None,
        rolling_wtp_upgrade_threshold: str | None = None,
        max_retransmit: int | None = None,
        control_message_offload: str | list | None = None,
        data_ethernet_II: str | None = None,
        link_aggregation: str | None = None,
        mesh_eth_type: int | None = None,
        fiapp_eth_type: int | None = None,
        discovery_mc_addr: Any | None = None,
        discovery_mc_addr6: str | None = None,
        max_clients: int | None = None,
        rogue_scan_mac_adjacency: int | None = None,
        ipsec_base_ip: str | None = None,
        wtp_share: str | None = None,
        tunnel_mode: str | None = None,
        nac_interval: int | None = None,
        ap_log_server: str | None = None,
        ap_log_server_ip: str | None = None,
        ap_log_server_port: int | None = None,
        max_sta_offline: int | None = None,
        max_sta_offline_ip2mac: int | None = None,
        max_sta_cap: int | None = None,
        max_sta_cap_wtp: int | None = None,
        max_rogue_ap: int | None = None,
        max_rogue_ap_wtp: int | None = None,
        max_rogue_sta: int | None = None,
        max_wids_entry: int | None = None,
        max_ble_device: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/global_ object.

        Configure wireless controller global settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name of the wireless controller.
            location: Description of the location of the wireless controller.
            acd_process_count: Configure the number cw_acd daemons for multi-core CPU support (default = 0).
            wpad_process_count: Wpad daemon process count for multi-core CPU support.
            image_download: Enable/disable WTP image download at join time.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            location=location,
            acd_process_count=acd_process_count,
            wpad_process_count=wpad_process_count,
            image_download=image_download,
            rolling_wtp_upgrade=rolling_wtp_upgrade,
            rolling_wtp_upgrade_threshold=rolling_wtp_upgrade_threshold,
            max_retransmit=max_retransmit,
            control_message_offload=control_message_offload,
            data_ethernet_II=data_ethernet_II,
            link_aggregation=link_aggregation,
            mesh_eth_type=mesh_eth_type,
            fiapp_eth_type=fiapp_eth_type,
            discovery_mc_addr=discovery_mc_addr,
            discovery_mc_addr6=discovery_mc_addr6,
            max_clients=max_clients,
            rogue_scan_mac_adjacency=rogue_scan_mac_adjacency,
            ipsec_base_ip=ipsec_base_ip,
            wtp_share=wtp_share,
            tunnel_mode=tunnel_mode,
            nac_interval=nac_interval,
            ap_log_server=ap_log_server,
            ap_log_server_ip=ap_log_server_ip,
            ap_log_server_port=ap_log_server_port,
            max_sta_offline=max_sta_offline,
            max_sta_offline_ip2mac=max_sta_offline_ip2mac,
            max_sta_cap=max_sta_cap,
            max_sta_cap_wtp=max_sta_cap_wtp,
            max_rogue_ap=max_rogue_ap,
            max_rogue_ap_wtp=max_rogue_ap_wtp,
            max_rogue_sta=max_rogue_sta,
            max_wids_entry=max_wids_entry,
            max_ble_device=max_ble_device,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/global_",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/wireless-controller/global/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





