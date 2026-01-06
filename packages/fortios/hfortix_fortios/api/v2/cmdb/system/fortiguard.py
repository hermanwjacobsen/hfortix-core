"""
FortiOS CMDB - System fortiguard

Configuration endpoint for managing cmdb system/fortiguard objects.

API Endpoints:
    GET    /cmdb/system/fortiguard
    POST   /cmdb/system/fortiguard
    PUT    /cmdb/system/fortiguard/{identifier}
    DELETE /cmdb/system/fortiguard/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_fortiguard.get()

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


class Fortiguard(MetadataMixin):
    """Fortiguard Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "fortiguard"
    
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
        """Initialize Fortiguard endpoint."""
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
        Retrieve system/fortiguard configuration.

        Configure FortiGuard services.

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
            >>> # Get all system/fortiguard objects
            >>> result = fgt.api.cmdb.system_fortiguard.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_fortiguard.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_fortiguard.get(action="schema")

        See Also:
            - post(): Create new system/fortiguard object
            - put(): Update existing system/fortiguard object
            - delete(): Remove system/fortiguard object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/system/fortiguard/{name}"
        else:
            endpoint = "/system/fortiguard"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        fortiguard_anycast: Literal["enable", "disable"] | None = None,
        fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = None,
        protocol: Literal["udp", "http", "https"] | None = None,
        port: Literal["8888", "53", "80", "443"] | None = None,
        load_balance_servers: int | None = None,
        auto_join_forticloud: Literal["enable", "disable"] | None = None,
        update_server_location: Literal["automatic", "usa", "eu"] | None = None,
        sandbox_region: str | None = None,
        sandbox_inline_scan: Literal["enable", "disable"] | None = None,
        update_ffdb: Literal["enable", "disable"] | None = None,
        update_uwdb: Literal["enable", "disable"] | None = None,
        update_dldb: Literal["enable", "disable"] | None = None,
        update_extdb: Literal["enable", "disable"] | None = None,
        update_build_proxy: Literal["enable", "disable"] | None = None,
        persistent_connection: Literal["enable", "disable"] | None = None,
        auto_firmware_upgrade: Literal["enable", "disable"] | None = None,
        auto_firmware_upgrade_day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | list | None = None,
        auto_firmware_upgrade_delay: int | None = None,
        auto_firmware_upgrade_start_hour: int | None = None,
        auto_firmware_upgrade_end_hour: int | None = None,
        FDS_license_expiring_days: int | None = None,
        subscribe_update_notification: Literal["enable", "disable"] | None = None,
        antispam_force_off: Literal["enable", "disable"] | None = None,
        antispam_cache: Literal["enable", "disable"] | None = None,
        antispam_cache_ttl: int | None = None,
        antispam_cache_mpermille: int | None = None,
        antispam_license: int | None = None,
        antispam_expiration: int | None = None,
        antispam_timeout: int | None = None,
        outbreak_prevention_force_off: Literal["enable", "disable"] | None = None,
        outbreak_prevention_cache: Literal["enable", "disable"] | None = None,
        outbreak_prevention_cache_ttl: int | None = None,
        outbreak_prevention_cache_mpermille: int | None = None,
        outbreak_prevention_license: int | None = None,
        outbreak_prevention_expiration: int | None = None,
        outbreak_prevention_timeout: int | None = None,
        webfilter_force_off: Literal["enable", "disable"] | None = None,
        webfilter_cache: Literal["enable", "disable"] | None = None,
        webfilter_cache_ttl: int | None = None,
        webfilter_license: int | None = None,
        webfilter_expiration: int | None = None,
        webfilter_timeout: int | None = None,
        sdns_server_ip: str | list | None = None,
        sdns_server_port: int | None = None,
        anycast_sdns_server_ip: str | None = None,
        anycast_sdns_server_port: int | None = None,
        sdns_options: Literal["include-question-section"] | list | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        proxy_server_ip: str | None = None,
        proxy_server_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: Any | None = None,
        ddns_server_ip: str | None = None,
        ddns_server_ip6: str | None = None,
        ddns_server_port: int | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/fortiguard object.

        Configure FortiGuard services.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            fortiguard_anycast: Enable/disable use of FortiGuard's Anycast network.
            fortiguard_anycast_source: Configure which of Fortinet's servers to provide FortiGuard services in FortiGuard's anycast network. Default is Fortinet.
            protocol: Protocol used to communicate with the FortiGuard servers.
            port: Port used to communicate with the FortiGuard servers.
            load_balance_servers: Number of servers to alternate between as first FortiGuard option.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_fortiguard.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_fortiguard.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            fortiguard_anycast=fortiguard_anycast,
            fortiguard_anycast_source=fortiguard_anycast_source,
            protocol=protocol,
            port=port,
            load_balance_servers=load_balance_servers,
            auto_join_forticloud=auto_join_forticloud,
            update_server_location=update_server_location,
            sandbox_region=sandbox_region,
            sandbox_inline_scan=sandbox_inline_scan,
            update_ffdb=update_ffdb,
            update_uwdb=update_uwdb,
            update_dldb=update_dldb,
            update_extdb=update_extdb,
            update_build_proxy=update_build_proxy,
            persistent_connection=persistent_connection,
            auto_firmware_upgrade=auto_firmware_upgrade,
            auto_firmware_upgrade_day=auto_firmware_upgrade_day,
            auto_firmware_upgrade_delay=auto_firmware_upgrade_delay,
            auto_firmware_upgrade_start_hour=auto_firmware_upgrade_start_hour,
            auto_firmware_upgrade_end_hour=auto_firmware_upgrade_end_hour,
            FDS_license_expiring_days=FDS_license_expiring_days,
            subscribe_update_notification=subscribe_update_notification,
            antispam_force_off=antispam_force_off,
            antispam_cache=antispam_cache,
            antispam_cache_ttl=antispam_cache_ttl,
            antispam_cache_mpermille=antispam_cache_mpermille,
            antispam_license=antispam_license,
            antispam_expiration=antispam_expiration,
            antispam_timeout=antispam_timeout,
            outbreak_prevention_force_off=outbreak_prevention_force_off,
            outbreak_prevention_cache=outbreak_prevention_cache,
            outbreak_prevention_cache_ttl=outbreak_prevention_cache_ttl,
            outbreak_prevention_cache_mpermille=outbreak_prevention_cache_mpermille,
            outbreak_prevention_license=outbreak_prevention_license,
            outbreak_prevention_expiration=outbreak_prevention_expiration,
            outbreak_prevention_timeout=outbreak_prevention_timeout,
            webfilter_force_off=webfilter_force_off,
            webfilter_cache=webfilter_cache,
            webfilter_cache_ttl=webfilter_cache_ttl,
            webfilter_license=webfilter_license,
            webfilter_expiration=webfilter_expiration,
            webfilter_timeout=webfilter_timeout,
            sdns_server_ip=sdns_server_ip,
            sdns_server_port=sdns_server_port,
            anycast_sdns_server_ip=anycast_sdns_server_ip,
            anycast_sdns_server_port=anycast_sdns_server_port,
            sdns_options=sdns_options,
            source_ip=source_ip,
            source_ip6=source_ip6,
            proxy_server_ip=proxy_server_ip,
            proxy_server_port=proxy_server_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
            ddns_server_ip=ddns_server_ip,
            ddns_server_ip6=ddns_server_ip6,
            ddns_server_port=ddns_server_port,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.fortiguard import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/fortiguard",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/system/fortiguard/{name_value}"

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
        Move system/fortiguard object to a new position.
        
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
            >>> fgt.api.cmdb.system_fortiguard.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/fortiguard",
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
        Clone system/fortiguard object.
        
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
            >>> fgt.api.cmdb.system_fortiguard.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/fortiguard",
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
        Check if system/fortiguard object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_fortiguard.exists(name="myobj"):
            ...     fgt.api.cmdb.system_fortiguard.post(payload_dict=data)
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

