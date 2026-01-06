"""
FortiOS CMDB - Router isis

Configuration endpoint for managing cmdb router/isis objects.

API Endpoints:
    GET    /cmdb/router/isis
    POST   /cmdb/router/isis
    PUT    /cmdb/router/isis/{identifier}
    DELETE /cmdb/router/isis/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_isis.get()

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


class Isis(MetadataMixin):
    """Isis Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "isis"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Isis endpoint."""
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
        Retrieve router/isis configuration.

        Configure IS-IS.

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
            >>> # Get all router/isis objects
            >>> result = fgt.api.cmdb.router_isis.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_isis.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.router_isis.get(action="schema")

        See Also:
            - post(): Create new router/isis object
            - put(): Update existing router/isis object
            - delete(): Remove router/isis object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/router/isis/{name}"
        else:
            endpoint = "/router/isis"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        is_type: str | None = None,
        adv_passive_only: str | None = None,
        adv_passive_only6: str | None = None,
        auth_mode_l1: str | None = None,
        auth_mode_l2: str | None = None,
        auth_password_l1: Any | None = None,
        auth_password_l2: Any | None = None,
        auth_keychain_l1: str | None = None,
        auth_keychain_l2: str | None = None,
        auth_sendonly_l1: str | None = None,
        auth_sendonly_l2: str | None = None,
        ignore_lsp_errors: str | None = None,
        lsp_gen_interval_l1: int | None = None,
        lsp_gen_interval_l2: int | None = None,
        lsp_refresh_interval: int | None = None,
        max_lsp_lifetime: int | None = None,
        spf_interval_exp_l1: str | None = None,
        spf_interval_exp_l2: str | None = None,
        dynamic_hostname: str | None = None,
        adjacency_check: str | None = None,
        adjacency_check6: str | None = None,
        overload_bit: str | None = None,
        overload_bit_suppress: str | list | None = None,
        overload_bit_on_startup: int | None = None,
        default_originate: str | None = None,
        default_originate6: str | None = None,
        metric_style: str | None = None,
        redistribute_l1: str | None = None,
        redistribute_l1_list: str | None = None,
        redistribute_l2: str | None = None,
        redistribute_l2_list: str | None = None,
        redistribute6_l1: str | None = None,
        redistribute6_l1_list: str | None = None,
        redistribute6_l2: str | None = None,
        redistribute6_l2_list: str | None = None,
        isis_net: str | list | None = None,
        isis_interface: str | list | None = None,
        summary_address: str | list | None = None,
        summary_address6: str | list | None = None,
        redistribute: str | list | None = None,
        redistribute6: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing router/isis object.

        Configure IS-IS.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            is_type: IS type.
            adv_passive_only: Enable/disable IS-IS advertisement of passive interfaces only.
            adv_passive_only6: Enable/disable IPv6 IS-IS advertisement of passive interfaces only.
            auth_mode_l1: Level 1 authentication mode.
            auth_mode_l2: Level 2 authentication mode.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_isis.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_isis.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            is_type=is_type,
            adv_passive_only=adv_passive_only,
            adv_passive_only6=adv_passive_only6,
            auth_mode_l1=auth_mode_l1,
            auth_mode_l2=auth_mode_l2,
            auth_password_l1=auth_password_l1,
            auth_password_l2=auth_password_l2,
            auth_keychain_l1=auth_keychain_l1,
            auth_keychain_l2=auth_keychain_l2,
            auth_sendonly_l1=auth_sendonly_l1,
            auth_sendonly_l2=auth_sendonly_l2,
            ignore_lsp_errors=ignore_lsp_errors,
            lsp_gen_interval_l1=lsp_gen_interval_l1,
            lsp_gen_interval_l2=lsp_gen_interval_l2,
            lsp_refresh_interval=lsp_refresh_interval,
            max_lsp_lifetime=max_lsp_lifetime,
            spf_interval_exp_l1=spf_interval_exp_l1,
            spf_interval_exp_l2=spf_interval_exp_l2,
            dynamic_hostname=dynamic_hostname,
            adjacency_check=adjacency_check,
            adjacency_check6=adjacency_check6,
            overload_bit=overload_bit,
            overload_bit_suppress=overload_bit_suppress,
            overload_bit_on_startup=overload_bit_on_startup,
            default_originate=default_originate,
            default_originate6=default_originate6,
            metric_style=metric_style,
            redistribute_l1=redistribute_l1,
            redistribute_l1_list=redistribute_l1_list,
            redistribute_l2=redistribute_l2,
            redistribute_l2_list=redistribute_l2_list,
            redistribute6_l1=redistribute6_l1,
            redistribute6_l1_list=redistribute6_l1_list,
            redistribute6_l2=redistribute6_l2,
            redistribute6_l2_list=redistribute6_l2_list,
            isis_net=isis_net,
            isis_interface=isis_interface,
            summary_address=summary_address,
            summary_address6=summary_address6,
            redistribute=redistribute,
            redistribute6=redistribute6,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.isis import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/isis",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/router/isis/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





