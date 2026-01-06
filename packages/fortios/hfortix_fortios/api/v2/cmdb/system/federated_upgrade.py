"""
FortiOS CMDB - System federated_upgrade

Configuration endpoint for managing cmdb system/federated_upgrade objects.

API Endpoints:
    GET    /cmdb/system/federated_upgrade
    POST   /cmdb/system/federated_upgrade
    PUT    /cmdb/system/federated_upgrade/{identifier}
    DELETE /cmdb/system/federated_upgrade/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_federated_upgrade.get()

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


class FederatedUpgrade(MetadataMixin):
    """FederatedUpgrade Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "federated_upgrade"

    def __init__(self, client: "IHTTPClient"):
        """Initialize FederatedUpgrade endpoint."""
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
        Retrieve system/federated_upgrade configuration.

        Coordinate federated upgrades within the Security Fabric.

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
            >>> # Get all system/federated_upgrade objects
            >>> result = fgt.api.cmdb.system_federated_upgrade.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_federated_upgrade.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_federated_upgrade.get(action="schema")

        See Also:
            - post(): Create new system/federated_upgrade object
            - put(): Update existing system/federated_upgrade object
            - delete(): Remove system/federated_upgrade object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/federated-upgrade/{name}"
        else:
            endpoint = "/system/federated-upgrade"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        status: str | None = None,
        source: str | None = None,
        failure_reason: str | None = None,
        failure_device: str | None = None,
        upgrade_id: int | None = None,
        next_path_index: int | None = None,
        ignore_signing_errors: str | None = None,
        ha_reboot_controller: str | None = None,
        known_ha_members: str | list | None = None,
        initial_version: str | None = None,
        starter_admin: str | None = None,
        node_list: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/federated_upgrade object.

        Coordinate federated upgrades within the Security Fabric.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            status: Current status of the upgrade.
            source: Source that set up the federated upgrade config.
            failure_reason: Reason for upgrade failure.
            failure_device: Serial number of the node to include.
            upgrade_id: Unique identifier for this upgrade.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_federated_upgrade.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_federated_upgrade.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            status=status,
            source=source,
            failure_reason=failure_reason,
            failure_device=failure_device,
            upgrade_id=upgrade_id,
            next_path_index=next_path_index,
            ignore_signing_errors=ignore_signing_errors,
            ha_reboot_controller=ha_reboot_controller,
            known_ha_members=known_ha_members,
            initial_version=initial_version,
            starter_admin=starter_admin,
            node_list=node_list,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.federated_upgrade import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/federated_upgrade",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/federated-upgrade/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





