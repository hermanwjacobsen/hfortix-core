"""
FortiOS CMDB - System standalone_cluster

Configuration endpoint for managing cmdb system/standalone_cluster objects.

API Endpoints:
    GET    /cmdb/system/standalone_cluster
    POST   /cmdb/system/standalone_cluster
    PUT    /cmdb/system/standalone_cluster/{identifier}
    DELETE /cmdb/system/standalone_cluster/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_standalone_cluster.get()

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


class StandaloneCluster(MetadataMixin):
    """StandaloneCluster Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "standalone_cluster"

    def __init__(self, client: "IHTTPClient"):
        """Initialize StandaloneCluster endpoint."""
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
        Retrieve system/standalone_cluster configuration.

        Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.

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
            >>> # Get all system/standalone_cluster objects
            >>> result = fgt.api.cmdb.system_standalone_cluster.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_standalone_cluster.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_standalone_cluster.get(action="schema")

        See Also:
            - post(): Create new system/standalone_cluster object
            - put(): Update existing system/standalone_cluster object
            - delete(): Remove system/standalone_cluster object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/standalone-cluster/{name}"
        else:
            endpoint = "/system/standalone-cluster"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        standalone_group_id: int | None = None,
        group_member_id: int | None = None,
        layer2_connection: str | None = None,
        session_sync_dev: str | list | None = None,
        encryption: str | None = None,
        psksecret: Any | None = None,
        asymmetric_traffic_control: str | None = None,
        cluster_peer: str | list | None = None,
        monitor_interface: str | list | None = None,
        pingsvr_monitor_interface: str | list | None = None,
        monitor_prefix: str | list | None = None,
        helper_traffic_bounce: str | None = None,
        utm_traffic_bounce: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/standalone_cluster object.

        Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            standalone_group_id: Cluster group ID (0 - 255). Must be the same for all members.
            group_member_id: Cluster member ID (0 - 15).
            layer2_connection: Indicate whether layer 2 connections are present among FGSP members.
            session_sync_dev: Offload session-sync process to kernel and sync sessions using connected interface(s) directly.
            encryption: Enable/disable encryption when synchronizing sessions.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_standalone_cluster.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_standalone_cluster.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            standalone_group_id=standalone_group_id,
            group_member_id=group_member_id,
            layer2_connection=layer2_connection,
            session_sync_dev=session_sync_dev,
            encryption=encryption,
            psksecret=psksecret,
            asymmetric_traffic_control=asymmetric_traffic_control,
            cluster_peer=cluster_peer,
            monitor_interface=monitor_interface,
            pingsvr_monitor_interface=pingsvr_monitor_interface,
            monitor_prefix=monitor_prefix,
            helper_traffic_bounce=helper_traffic_bounce,
            utm_traffic_bounce=utm_traffic_bounce,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.standalone_cluster import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/standalone_cluster",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/standalone-cluster/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





