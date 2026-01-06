"""
FortiOS CMDB - Log fortianalyzer_cloud override_filter

Configuration endpoint for managing cmdb log/fortianalyzer_cloud/override_filter objects.

API Endpoints:
    GET    /cmdb/log/fortianalyzer_cloud/override_filter
    POST   /cmdb/log/fortianalyzer_cloud/override_filter
    PUT    /cmdb/log/fortianalyzer_cloud/override_filter/{identifier}
    DELETE /cmdb/log/fortianalyzer_cloud/override_filter/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_fortianalyzer_cloud_override_filter.get()

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


class OverrideFilter(MetadataMixin):
    """OverrideFilter Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "override_filter"

    def __init__(self, client: "IHTTPClient"):
        """Initialize OverrideFilter endpoint."""
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
        Retrieve log/fortianalyzer_cloud/override_filter configuration.

        Override filters for FortiAnalyzer Cloud.

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
            >>> # Get all log/fortianalyzer_cloud/override_filter objects
            >>> result = fgt.api.cmdb.log_fortianalyzer_cloud_override_filter.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_fortianalyzer_cloud_override_filter.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.log_fortianalyzer_cloud_override_filter.get(action="schema")

        See Also:
            - post(): Create new log/fortianalyzer_cloud/override_filter object
            - put(): Update existing log/fortianalyzer_cloud/override_filter object
            - delete(): Remove log/fortianalyzer_cloud/override_filter object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/log.fortianalyzer-cloud/override-filter/{name}"
        else:
            endpoint = "/log.fortianalyzer-cloud/override-filter"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        severity: str | None = None,
        forward_traffic: str | None = None,
        local_traffic: str | None = None,
        multicast_traffic: str | None = None,
        sniffer_traffic: str | None = None,
        ztna_traffic: str | None = None,
        http_transaction: str | None = None,
        anomaly: str | None = None,
        voip: str | None = None,
        dlp_archive: str | None = None,
        gtp: str | None = None,
        forti_switch: str | None = None,
        free_style: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing log/fortianalyzer_cloud/override_filter object.

        Override filters for FortiAnalyzer Cloud.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            severity: Lowest severity level to log.
            forward_traffic: Enable/disable forward traffic logging.
            local_traffic: Enable/disable local in or out traffic logging.
            multicast_traffic: Enable/disable multicast traffic logging.
            sniffer_traffic: Enable/disable sniffer traffic logging.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_fortianalyzer_cloud_override_filter.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_fortianalyzer_cloud_override_filter.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            severity=severity,
            forward_traffic=forward_traffic,
            local_traffic=local_traffic,
            multicast_traffic=multicast_traffic,
            sniffer_traffic=sniffer_traffic,
            ztna_traffic=ztna_traffic,
            http_transaction=http_transaction,
            anomaly=anomaly,
            voip=voip,
            dlp_archive=dlp_archive,
            gtp=gtp,
            forti_switch=forti_switch,
            free_style=free_style,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.override_filter import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/fortianalyzer_cloud/override_filter",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/log.fortianalyzer-cloud/override-filter/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





