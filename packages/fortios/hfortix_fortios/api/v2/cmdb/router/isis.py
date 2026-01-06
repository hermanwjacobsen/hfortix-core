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


class Isis(MetadataMixin):
    """Isis Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "isis"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

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
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = None,
        adv_passive_only: Literal["enable", "disable"] | None = None,
        adv_passive_only6: Literal["enable", "disable"] | None = None,
        auth_mode_l1: Literal["password", "md5"] | None = None,
        auth_mode_l2: Literal["password", "md5"] | None = None,
        auth_password_l1: Any | None = None,
        auth_password_l2: Any | None = None,
        auth_keychain_l1: str | None = None,
        auth_keychain_l2: str | None = None,
        auth_sendonly_l1: Literal["enable", "disable"] | None = None,
        auth_sendonly_l2: Literal["enable", "disable"] | None = None,
        ignore_lsp_errors: Literal["enable", "disable"] | None = None,
        lsp_gen_interval_l1: int | None = None,
        lsp_gen_interval_l2: int | None = None,
        lsp_refresh_interval: int | None = None,
        max_lsp_lifetime: int | None = None,
        spf_interval_exp_l1: str | None = None,
        spf_interval_exp_l2: str | None = None,
        dynamic_hostname: Literal["enable", "disable"] | None = None,
        adjacency_check: Literal["enable", "disable"] | None = None,
        adjacency_check6: Literal["enable", "disable"] | None = None,
        overload_bit: Literal["enable", "disable"] | None = None,
        overload_bit_suppress: Literal["external", "interlevel"] | list | None = None,
        overload_bit_on_startup: int | None = None,
        default_originate: Literal["enable", "disable"] | None = None,
        default_originate6: Literal["enable", "disable"] | None = None,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = None,
        redistribute_l1: Literal["enable", "disable"] | None = None,
        redistribute_l1_list: str | None = None,
        redistribute_l2: Literal["enable", "disable"] | None = None,
        redistribute_l2_list: str | None = None,
        redistribute6_l1: Literal["enable", "disable"] | None = None,
        redistribute6_l1_list: str | None = None,
        redistribute6_l2: Literal["enable", "disable"] | None = None,
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
        Move router/isis object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.router_isis.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/isis",
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
        Clone router/isis object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.router_isis.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/isis",
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
        Check if router/isis object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.router_isis.exists(name="myobj"):
            ...     fgt.api.cmdb.router_isis.post(payload_dict=data)
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

