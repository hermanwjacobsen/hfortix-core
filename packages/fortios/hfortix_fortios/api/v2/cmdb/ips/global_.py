"""
FortiOS CMDB - Ips global_

Configuration endpoint for managing cmdb ips/global_ objects.

API Endpoints:
    GET    /cmdb/ips/global_
    POST   /cmdb/ips/global_
    PUT    /cmdb/ips/global_/{identifier}
    DELETE /cmdb/ips/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.ips_global_.get()

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
        Retrieve ips/global_ configuration.

        Configure IPS global parameter.

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
            >>> # Get all ips/global_ objects
            >>> result = fgt.api.cmdb.ips_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.ips_global_.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.ips_global_.get(action="schema")

        See Also:
            - post(): Create new ips/global_ object
            - put(): Update existing ips/global_ object
            - delete(): Remove ips/global_ object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/ips/global/{name}"
        else:
            endpoint = "/ips/global"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        fail_open: str | None = None,
        database: str | None = None,
        traffic_submit: str | None = None,
        anomaly_mode: str | None = None,
        session_limit_mode: str | None = None,
        socket_size: int | None = None,
        engine_count: int | None = None,
        sync_session_ttl: str | None = None,
        deep_app_insp_timeout: int | None = None,
        deep_app_insp_db_limit: int | None = None,
        exclude_signatures: str | None = None,
        packet_log_queue_depth: int | None = None,
        ngfw_max_scan_range: int | None = None,
        av_mem_limit: int | None = None,
        machine_learning_detection: str | None = None,
        tls_active_probe: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing ips/global_ object.

        Configure IPS global parameter.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            fail_open: Enable to allow traffic if the IPS buffer is full. Default is disable and IPS traffic is blocked when the IPS buffer is full.
            database: Regular or extended IPS database. Regular protects against the latest common and in-the-wild attacks. Extended includes protection from legacy attacks.
            traffic_submit: Enable/disable submitting attack data found by this FortiGate to FortiGuard.
            anomaly_mode: Global blocking mode for rate-based anomalies.
            session_limit_mode: Method of counting concurrent sessions used by session limit anomalies. Choose between greater accuracy (accurate) or improved performance (heuristics).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.ips_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.ips_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            fail_open=fail_open,
            database=database,
            traffic_submit=traffic_submit,
            anomaly_mode=anomaly_mode,
            session_limit_mode=session_limit_mode,
            socket_size=socket_size,
            engine_count=engine_count,
            sync_session_ttl=sync_session_ttl,
            deep_app_insp_timeout=deep_app_insp_timeout,
            deep_app_insp_db_limit=deep_app_insp_db_limit,
            exclude_signatures=exclude_signatures,
            packet_log_queue_depth=packet_log_queue_depth,
            ngfw_max_scan_range=ngfw_max_scan_range,
            av_mem_limit=av_mem_limit,
            machine_learning_detection=machine_learning_detection,
            tls_active_probe=tls_active_probe,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/ips/global_",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/ips/global/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





