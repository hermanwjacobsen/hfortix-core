"""
FortiOS CMDB - User radius

Configuration endpoint for managing cmdb user/radius objects.

API Endpoints:
    GET    /cmdb/user/radius
    POST   /cmdb/user/radius
    PUT    /cmdb/user/radius/{identifier}
    DELETE /cmdb/user/radius/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user_radius.get()

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


class Radius(MetadataMixin):
    """Radius Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "radius"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Radius endpoint."""
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
        Retrieve user/radius configuration.

        Configure RADIUS server entries.

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
            >>> # Get all user/radius objects
            >>> result = fgt.api.cmdb.user_radius.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific user/radius by name
            >>> result = fgt.api.cmdb.user_radius.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.user_radius.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.user_radius.get(action="schema")

        See Also:
            - post(): Create new user/radius object
            - put(): Update existing user/radius object
            - delete(): Remove user/radius object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/user/radius/" + str(name)
        else:
            endpoint = "/user/radius"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        server: str | None = None,
        secret: Any | None = None,
        secondary_server: str | None = None,
        secondary_secret: Any | None = None,
        tertiary_server: str | None = None,
        tertiary_secret: Any | None = None,
        timeout: int | None = None,
        status_ttl: int | None = None,
        all_usergroup: str | None = None,
        use_management_vdom: str | None = None,
        switch_controller_nas_ip_dynamic: str | None = None,
        nas_ip: str | None = None,
        nas_id_type: str | None = None,
        call_station_id_type: str | None = None,
        nas_id: str | None = None,
        acct_interim_interval: int | None = None,
        radius_coa: str | None = None,
        radius_port: int | None = None,
        h3c_compatibility: str | None = None,
        auth_type: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        username_case_sensitive: str | None = None,
        group_override_attr_type: str | None = None,
        password_renewal: str | None = None,
        require_message_authenticator: str | None = None,
        password_encoding: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_case: str | None = None,
        acct_all_servers: str | None = None,
        switch_controller_acct_fast_framedip_detect: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        switch_controller_service_type: str | list | None = None,
        transport_protocol: str | None = None,
        tls_min_proto_version: str | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        server_identity_check: str | None = None,
        account_key_processing: str | None = None,
        account_key_cert_field: str | None = None,
        rsso: str | None = None,
        rsso_radius_server_port: int | None = None,
        rsso_radius_response: str | None = None,
        rsso_validate_request_secret: str | None = None,
        rsso_secret: Any | None = None,
        rsso_endpoint_attribute: str | None = None,
        rsso_endpoint_block_attribute: str | None = None,
        sso_attribute: str | None = None,
        sso_attribute_key: str | None = None,
        sso_attribute_value_override: str | None = None,
        rsso_context_timeout: int | None = None,
        rsso_log_period: int | None = None,
        rsso_log_flags: str | list | None = None,
        rsso_flush_ip_session: str | None = None,
        rsso_ep_one_ip_only: str | None = None,
        delimiter: str | None = None,
        accounting_server: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing user/radius object.

        Configure RADIUS server entries.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: RADIUS server entry name.
            server: Primary RADIUS server CN domain name or IP address.
            secret: Pre-shared secret key used to access the primary RADIUS server.
            secondary_server: Secondary RADIUS CN domain name or IP address.
            secondary_secret: Secret key to access the secondary server.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.user_radius.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.user_radius.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            server=server,
            secret=secret,
            secondary_server=secondary_server,
            secondary_secret=secondary_secret,
            tertiary_server=tertiary_server,
            tertiary_secret=tertiary_secret,
            timeout=timeout,
            status_ttl=status_ttl,
            all_usergroup=all_usergroup,
            use_management_vdom=use_management_vdom,
            switch_controller_nas_ip_dynamic=switch_controller_nas_ip_dynamic,
            nas_ip=nas_ip,
            nas_id_type=nas_id_type,
            call_station_id_type=call_station_id_type,
            nas_id=nas_id,
            acct_interim_interval=acct_interim_interval,
            radius_coa=radius_coa,
            radius_port=radius_port,
            h3c_compatibility=h3c_compatibility,
            auth_type=auth_type,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            username_case_sensitive=username_case_sensitive,
            group_override_attr_type=group_override_attr_type,
            password_renewal=password_renewal,
            require_message_authenticator=require_message_authenticator,
            password_encoding=password_encoding,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_case=mac_case,
            acct_all_servers=acct_all_servers,
            switch_controller_acct_fast_framedip_detect=switch_controller_acct_fast_framedip_detect,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            switch_controller_service_type=switch_controller_service_type,
            transport_protocol=transport_protocol,
            tls_min_proto_version=tls_min_proto_version,
            ca_cert=ca_cert,
            client_cert=client_cert,
            server_identity_check=server_identity_check,
            account_key_processing=account_key_processing,
            account_key_cert_field=account_key_cert_field,
            rsso=rsso,
            rsso_radius_server_port=rsso_radius_server_port,
            rsso_radius_response=rsso_radius_response,
            rsso_validate_request_secret=rsso_validate_request_secret,
            rsso_secret=rsso_secret,
            rsso_endpoint_attribute=rsso_endpoint_attribute,
            rsso_endpoint_block_attribute=rsso_endpoint_block_attribute,
            sso_attribute=sso_attribute,
            sso_attribute_key=sso_attribute_key,
            sso_attribute_value_override=sso_attribute_value_override,
            rsso_context_timeout=rsso_context_timeout,
            rsso_log_period=rsso_log_period,
            rsso_log_flags=rsso_log_flags,
            rsso_flush_ip_session=rsso_flush_ip_session,
            rsso_ep_one_ip_only=rsso_ep_one_ip_only,
            delimiter=delimiter,
            accounting_server=accounting_server,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.radius import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/radius",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/user/radius/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        server: str | None = None,
        secret: Any | None = None,
        secondary_server: str | None = None,
        secondary_secret: Any | None = None,
        tertiary_server: str | None = None,
        tertiary_secret: Any | None = None,
        timeout: int | None = None,
        status_ttl: int | None = None,
        all_usergroup: str | None = None,
        use_management_vdom: str | None = None,
        switch_controller_nas_ip_dynamic: str | None = None,
        nas_ip: str | None = None,
        nas_id_type: str | None = None,
        call_station_id_type: str | None = None,
        nas_id: str | None = None,
        acct_interim_interval: int | None = None,
        radius_coa: str | None = None,
        radius_port: int | None = None,
        h3c_compatibility: str | None = None,
        auth_type: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        username_case_sensitive: str | None = None,
        group_override_attr_type: str | None = None,
        password_renewal: str | None = None,
        require_message_authenticator: str | None = None,
        password_encoding: str | None = None,
        mac_username_delimiter: str | None = None,
        mac_password_delimiter: str | None = None,
        mac_case: str | None = None,
        acct_all_servers: str | None = None,
        switch_controller_acct_fast_framedip_detect: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        switch_controller_service_type: str | list | None = None,
        transport_protocol: str | None = None,
        tls_min_proto_version: str | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        server_identity_check: str | None = None,
        account_key_processing: str | None = None,
        account_key_cert_field: str | None = None,
        rsso: str | None = None,
        rsso_radius_server_port: int | None = None,
        rsso_radius_response: str | None = None,
        rsso_validate_request_secret: str | None = None,
        rsso_secret: Any | None = None,
        rsso_endpoint_attribute: str | None = None,
        rsso_endpoint_block_attribute: str | None = None,
        sso_attribute: str | None = None,
        sso_attribute_key: str | None = None,
        sso_attribute_value_override: str | None = None,
        rsso_context_timeout: int | None = None,
        rsso_log_period: int | None = None,
        rsso_log_flags: str | list | None = None,
        rsso_flush_ip_session: str | None = None,
        rsso_ep_one_ip_only: str | None = None,
        delimiter: str | None = None,
        accounting_server: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new user/radius object.

        Configure RADIUS server entries.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: RADIUS server entry name.
            server: Primary RADIUS server CN domain name or IP address.
            secret: Pre-shared secret key used to access the primary RADIUS server.
            secondary_server: Secondary RADIUS CN domain name or IP address.
            secondary_secret: Secret key to access the secondary server.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.user_radius.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Radius.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.user_radius.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Radius.required_fields()) }}
            
            Use Radius.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            server=server,
            secret=secret,
            secondary_server=secondary_server,
            secondary_secret=secondary_secret,
            tertiary_server=tertiary_server,
            tertiary_secret=tertiary_secret,
            timeout=timeout,
            status_ttl=status_ttl,
            all_usergroup=all_usergroup,
            use_management_vdom=use_management_vdom,
            switch_controller_nas_ip_dynamic=switch_controller_nas_ip_dynamic,
            nas_ip=nas_ip,
            nas_id_type=nas_id_type,
            call_station_id_type=call_station_id_type,
            nas_id=nas_id,
            acct_interim_interval=acct_interim_interval,
            radius_coa=radius_coa,
            radius_port=radius_port,
            h3c_compatibility=h3c_compatibility,
            auth_type=auth_type,
            source_ip=source_ip,
            source_ip_interface=source_ip_interface,
            username_case_sensitive=username_case_sensitive,
            group_override_attr_type=group_override_attr_type,
            password_renewal=password_renewal,
            require_message_authenticator=require_message_authenticator,
            password_encoding=password_encoding,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_case=mac_case,
            acct_all_servers=acct_all_servers,
            switch_controller_acct_fast_framedip_detect=switch_controller_acct_fast_framedip_detect,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            switch_controller_service_type=switch_controller_service_type,
            transport_protocol=transport_protocol,
            tls_min_proto_version=tls_min_proto_version,
            ca_cert=ca_cert,
            client_cert=client_cert,
            server_identity_check=server_identity_check,
            account_key_processing=account_key_processing,
            account_key_cert_field=account_key_cert_field,
            rsso=rsso,
            rsso_radius_server_port=rsso_radius_server_port,
            rsso_radius_response=rsso_radius_response,
            rsso_validate_request_secret=rsso_validate_request_secret,
            rsso_secret=rsso_secret,
            rsso_endpoint_attribute=rsso_endpoint_attribute,
            rsso_endpoint_block_attribute=rsso_endpoint_block_attribute,
            sso_attribute=sso_attribute,
            sso_attribute_key=sso_attribute_key,
            sso_attribute_value_override=sso_attribute_value_override,
            rsso_context_timeout=rsso_context_timeout,
            rsso_log_period=rsso_log_period,
            rsso_log_flags=rsso_log_flags,
            rsso_flush_ip_session=rsso_flush_ip_session,
            rsso_ep_one_ip_only=rsso_ep_one_ip_only,
            delimiter=delimiter,
            accounting_server=accounting_server,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.radius import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/radius",
            )

        endpoint = "/user/radius"
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
        Delete user/radius object.

        Configure RADIUS server entries.

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
            >>> result = fgt.api.cmdb.user_radius.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/user/radius/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if user/radius object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.user_radius.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.user_radius.exists(name=1):
            ...     fgt.api.cmdb.user_radius.delete(name=1)

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
        Create or update user/radius object (intelligent operation).

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
            >>> result = fgt.api.cmdb.user_radius.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.user_radius.set(payload_dict=obj_data)
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


