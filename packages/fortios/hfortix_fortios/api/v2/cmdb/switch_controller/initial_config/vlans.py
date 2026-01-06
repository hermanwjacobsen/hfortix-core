"""
FortiOS CMDB - Switch_controller initial_config vlans

Configuration endpoint for managing cmdb switch_controller/initial_config/vlans objects.

API Endpoints:
    GET    /cmdb/switch_controller/initial_config/vlans
    POST   /cmdb/switch_controller/initial_config/vlans
    PUT    /cmdb/switch_controller/initial_config/vlans/{identifier}
    DELETE /cmdb/switch_controller/initial_config/vlans/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_initial_config_vlans.get()

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


class Vlans(MetadataMixin):
    """Vlans Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vlans"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vlans endpoint."""
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
        Retrieve switch_controller/initial_config/vlans configuration.

        Configure initial template for auto-generated VLAN interfaces.

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
            >>> # Get all switch_controller/initial_config/vlans objects
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.switch_controller_initial_config_vlans.get(action="schema")

        See Also:
            - post(): Create new switch_controller/initial_config/vlans object
            - put(): Update existing switch_controller/initial_config/vlans object
            - delete(): Remove switch_controller/initial_config/vlans object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/switch-controller.initial-config/vlans/{name}"
        else:
            endpoint = "/switch-controller.initial-config/vlans"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        optional_vlans: str | None = None,
        default_vlan: str | None = None,
        quarantine: str | None = None,
        rspan: str | None = None,
        voice: str | None = None,
        video: str | None = None,
        nac: str | None = None,
        nac_segment: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing switch_controller/initial_config/vlans object.

        Configure initial template for auto-generated VLAN interfaces.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            optional_vlans: Auto-generate pre-configured VLANs upon switch discovery.
            default_vlan: Default VLAN (native) assigned to all switch ports upon discovery.
            quarantine: VLAN for quarantined traffic.
            rspan: VLAN for RSPAN/ERSPAN mirrored traffic.
            voice: VLAN dedicated for voice devices.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_initial_config_vlans.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            optional_vlans=optional_vlans,
            default_vlan=default_vlan,
            quarantine=quarantine,
            rspan=rspan,
            voice=voice,
            video=video,
            nac=nac,
            nac_segment=nac_segment,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vlans import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/initial_config/vlans",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/switch-controller.initial-config/vlans/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





