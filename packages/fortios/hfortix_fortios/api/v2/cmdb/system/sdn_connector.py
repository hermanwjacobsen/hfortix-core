"""
FortiOS CMDB - System sdn_connector

Configuration endpoint for managing cmdb system/sdn_connector objects.

API Endpoints:
    GET    /cmdb/system/sdn_connector
    POST   /cmdb/system/sdn_connector
    PUT    /cmdb/system/sdn_connector/{identifier}
    DELETE /cmdb/system/sdn_connector/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_sdn_connector.get()

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


class SdnConnector(MetadataMixin):
    """SdnConnector Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "sdn_connector"
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize SdnConnector endpoint."""
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
        Retrieve system/sdn_connector configuration.

        Configure connection to SDN Connector.

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
            >>> # Get all system/sdn_connector objects
            >>> result = fgt.api.cmdb.system_sdn_connector.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/sdn_connector by name
            >>> result = fgt.api.cmdb.system_sdn_connector.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_sdn_connector.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_sdn_connector.get(action="schema")

        See Also:
            - post(): Create new system/sdn_connector object
            - put(): Update existing system/sdn_connector object
            - delete(): Remove system/sdn_connector object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/system/sdn-connector/" + str(name)
        else:
            endpoint = "/system/sdn-connector"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = None,
        proxy: str | None = None,
        use_metadata_iam: Literal["disable", "enable"] | None = None,
        microsoft_365: Literal["disable", "enable"] | None = None,
        ha_status: Literal["disable", "enable"] | None = None,
        verify_certificate: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        server_list: str | list | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: Any | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: Any | None = None,
        access_key: str | None = None,
        secret_key: Any | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: Literal["disable", "enable"] | None = None,
        external_account_list: str | list | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: Any | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = None,
        nic: str | list | None = None,
        route_table: str | list | None = None,
        user_id: str | None = None,
        compartment_list: str | list | None = None,
        oci_region_list: str | list | None = None,
        oci_region_type: Literal["commercial", "government"] | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: str | list | None = None,
        route: str | list | None = None,
        gcp_project_list: str | list | None = None,
        forwarding_rule: str | list | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: Any | None = None,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/sdn_connector object.

        Configure connection to SDN Connector.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: SDN connector name.
            status: Enable/disable connection to the remote SDN connector.
            type: Type of SDN connector.
            proxy: SDN proxy.
            use_metadata_iam: Enable/disable use of IAM role from metadata to call API.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_sdn_connector.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_sdn_connector.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            status=status,
            type=type,
            proxy=proxy,
            use_metadata_iam=use_metadata_iam,
            microsoft_365=microsoft_365,
            ha_status=ha_status,
            verify_certificate=verify_certificate,
            server=server,
            server_list=server_list,
            server_port=server_port,
            message_server_port=message_server_port,
            username=username,
            password=password,
            vcenter_server=vcenter_server,
            vcenter_username=vcenter_username,
            vcenter_password=vcenter_password,
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            vpc_id=vpc_id,
            alt_resource_ip=alt_resource_ip,
            external_account_list=external_account_list,
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            resource_group=resource_group,
            login_endpoint=login_endpoint,
            resource_url=resource_url,
            azure_region=azure_region,
            nic=nic,
            route_table=route_table,
            user_id=user_id,
            compartment_list=compartment_list,
            oci_region_list=oci_region_list,
            oci_region_type=oci_region_type,
            oci_cert=oci_cert,
            oci_fingerprint=oci_fingerprint,
            external_ip=external_ip,
            route=route,
            gcp_project_list=gcp_project_list,
            forwarding_rule=forwarding_rule,
            service_account=service_account,
            private_key=private_key,
            secret_token=secret_token,
            domain=domain,
            group_name=group_name,
            server_cert=server_cert,
            server_ca_cert=server_ca_cert,
            api_key=api_key,
            ibm_region=ibm_region,
            par_id=par_id,
            update_interval=update_interval,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.sdn_connector import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdn_connector",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/sdn-connector/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["aci", "alicloud", "aws", "azure", "gcp", "nsx", "nuage", "oci", "openstack", "kubernetes", "vmware", "sepm", "aci-direct", "ibm", "nutanix", "sap"] | None = None,
        proxy: str | None = None,
        use_metadata_iam: Literal["disable", "enable"] | None = None,
        microsoft_365: Literal["disable", "enable"] | None = None,
        ha_status: Literal["disable", "enable"] | None = None,
        verify_certificate: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        server_list: str | list | None = None,
        server_port: int | None = None,
        message_server_port: int | None = None,
        username: str | None = None,
        password: Any | None = None,
        vcenter_server: str | None = None,
        vcenter_username: str | None = None,
        vcenter_password: Any | None = None,
        access_key: str | None = None,
        secret_key: Any | None = None,
        region: str | None = None,
        vpc_id: str | None = None,
        alt_resource_ip: Literal["disable", "enable"] | None = None,
        external_account_list: str | list | None = None,
        tenant_id: str | None = None,
        client_id: str | None = None,
        client_secret: Any | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
        login_endpoint: str | None = None,
        resource_url: str | None = None,
        azure_region: Literal["global", "china", "germany", "usgov", "local"] | None = None,
        nic: str | list | None = None,
        route_table: str | list | None = None,
        user_id: str | None = None,
        compartment_list: str | list | None = None,
        oci_region_list: str | list | None = None,
        oci_region_type: Literal["commercial", "government"] | None = None,
        oci_cert: str | None = None,
        oci_fingerprint: str | None = None,
        external_ip: str | list | None = None,
        route: str | list | None = None,
        gcp_project_list: str | list | None = None,
        forwarding_rule: str | list | None = None,
        service_account: str | None = None,
        private_key: str | None = None,
        secret_token: str | None = None,
        domain: str | None = None,
        group_name: str | None = None,
        server_cert: str | None = None,
        server_ca_cert: str | None = None,
        api_key: Any | None = None,
        ibm_region: Literal["dallas", "washington-dc", "london", "frankfurt", "sydney", "tokyo", "osaka", "toronto", "sao-paulo", "madrid"] | None = None,
        par_id: str | None = None,
        update_interval: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/sdn_connector object.

        Configure connection to SDN Connector.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: SDN connector name.
            status: Enable/disable connection to the remote SDN connector.
            type: Type of SDN connector.
            proxy: SDN proxy.
            use_metadata_iam: Enable/disable use of IAM role from metadata to call API.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_sdn_connector.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SdnConnector.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_sdn_connector.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SdnConnector.required_fields()) }}
            
            Use SdnConnector.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            status=status,
            type=type,
            proxy=proxy,
            use_metadata_iam=use_metadata_iam,
            microsoft_365=microsoft_365,
            ha_status=ha_status,
            verify_certificate=verify_certificate,
            server=server,
            server_list=server_list,
            server_port=server_port,
            message_server_port=message_server_port,
            username=username,
            password=password,
            vcenter_server=vcenter_server,
            vcenter_username=vcenter_username,
            vcenter_password=vcenter_password,
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            vpc_id=vpc_id,
            alt_resource_ip=alt_resource_ip,
            external_account_list=external_account_list,
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            resource_group=resource_group,
            login_endpoint=login_endpoint,
            resource_url=resource_url,
            azure_region=azure_region,
            nic=nic,
            route_table=route_table,
            user_id=user_id,
            compartment_list=compartment_list,
            oci_region_list=oci_region_list,
            oci_region_type=oci_region_type,
            oci_cert=oci_cert,
            oci_fingerprint=oci_fingerprint,
            external_ip=external_ip,
            route=route,
            gcp_project_list=gcp_project_list,
            forwarding_rule=forwarding_rule,
            service_account=service_account,
            private_key=private_key,
            secret_token=secret_token,
            domain=domain,
            group_name=group_name,
            server_cert=server_cert,
            server_ca_cert=server_ca_cert,
            api_key=api_key,
            ibm_region=ibm_region,
            par_id=par_id,
            update_interval=update_interval,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.sdn_connector import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/sdn_connector",
            )

        endpoint = "/system/sdn-connector"
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
        Delete system/sdn_connector object.

        Configure connection to SDN Connector.

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
            >>> result = fgt.api.cmdb.system_sdn_connector.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/sdn-connector/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/sdn_connector object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_sdn_connector.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_sdn_connector.exists(name=1):
            ...     fgt.api.cmdb.system_sdn_connector.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            response = self.get(
                name=name,
                vdom=vdom,
                raw_json=True
            )
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/sdn_connector object (intelligent operation).

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
            >>> result = fgt.api.cmdb.system_sdn_connector.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_sdn_connector.set(payload_dict=obj_data)
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
        Move system/sdn_connector object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_sdn_connector.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/sdn-connector",
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
        Clone system/sdn_connector object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_sdn_connector.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/sdn-connector",
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
        Check if system/sdn_connector object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_sdn_connector.exists(name=1):
            ...     fgt.api.cmdb.system_sdn_connector.post(payload_dict=data)
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

