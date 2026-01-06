"""
FortiOS CMDB - System automation_action

Configuration endpoint for managing cmdb system/automation_action objects.

API Endpoints:
    GET    /cmdb/system/automation_action
    POST   /cmdb/system/automation_action
    PUT    /cmdb/system/automation_action/{identifier}
    DELETE /cmdb/system/automation_action/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_automation_action.get()

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


class AutomationAction(MetadataMixin):
    """AutomationAction Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "automation_action"

    def __init__(self, client: "IHTTPClient"):
        """Initialize AutomationAction endpoint."""
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
        Retrieve system/automation_action configuration.

        Action for automation stitches.

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
            >>> # Get all system/automation_action objects
            >>> result = fgt.api.cmdb.system_automation_action.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/automation_action by name
            >>> result = fgt.api.cmdb.system_automation_action.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_automation_action.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.system_automation_action.get(action="schema")

        See Also:
            - post(): Create new system/automation_action object
            - put(): Update existing system/automation_action object
            - delete(): Remove system/automation_action object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/system/automation-action/" + str(name)
        else:
            endpoint = "/system/automation-action"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
        action_type: str | None = None,
        system_action: str | None = None,
        tls_certificate: str | None = None,
        forticare_email: str | None = None,
        email_to: str | list | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: Any | None = None,
        azure_function_authorization: str | None = None,
        azure_api_key: Any | None = None,
        alicloud_function_authorization: str | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: Any | None = None,
        message_type: str | None = None,
        message: str | None = None,
        replacement_message: str | None = None,
        replacemsg_group: str | None = None,
        protocol: str | None = None,
        method: str | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: str | list | None = None,
        form_data: str | list | None = None,
        verify_host_cert: str | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: str | None = None,
        execute_security_fabric: str | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: str | None = None,
        security_tag: str | None = None,
        sdn_connector: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing system/automation_action object.

        Action for automation stitches.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            description: Description.
            action_type: Action type.
            system_action: System action type.
            tls_certificate: Custom TLS certificate for API request.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_automation_action.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_automation_action.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            description=description,
            action_type=action_type,
            system_action=system_action,
            tls_certificate=tls_certificate,
            forticare_email=forticare_email,
            email_to=email_to,
            email_from=email_from,
            email_subject=email_subject,
            minimum_interval=minimum_interval,
            aws_api_key=aws_api_key,
            azure_function_authorization=azure_function_authorization,
            azure_api_key=azure_api_key,
            alicloud_function_authorization=alicloud_function_authorization,
            alicloud_access_key_id=alicloud_access_key_id,
            alicloud_access_key_secret=alicloud_access_key_secret,
            message_type=message_type,
            message=message,
            replacement_message=replacement_message,
            replacemsg_group=replacemsg_group,
            protocol=protocol,
            method=method,
            uri=uri,
            http_body=http_body,
            port=port,
            http_headers=http_headers,
            form_data=form_data,
            verify_host_cert=verify_host_cert,
            script=script,
            output_size=output_size,
            timeout=timeout,
            duration=duration,
            output_interval=output_interval,
            file_only=file_only,
            execute_security_fabric=execute_security_fabric,
            accprofile=accprofile,
            regular_expression=regular_expression,
            log_debug_print=log_debug_print,
            security_tag=security_tag,
            sdn_connector=sdn_connector,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.automation_action import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/automation_action",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/automation-action/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
        action_type: str | None = None,
        system_action: str | None = None,
        tls_certificate: str | None = None,
        forticare_email: str | None = None,
        email_to: str | list | None = None,
        email_from: str | None = None,
        email_subject: str | None = None,
        minimum_interval: int | None = None,
        aws_api_key: Any | None = None,
        azure_function_authorization: str | None = None,
        azure_api_key: Any | None = None,
        alicloud_function_authorization: str | None = None,
        alicloud_access_key_id: str | None = None,
        alicloud_access_key_secret: Any | None = None,
        message_type: str | None = None,
        message: str | None = None,
        replacement_message: str | None = None,
        replacemsg_group: str | None = None,
        protocol: str | None = None,
        method: str | None = None,
        uri: str | None = None,
        http_body: str | None = None,
        port: int | None = None,
        http_headers: str | list | None = None,
        form_data: str | list | None = None,
        verify_host_cert: str | None = None,
        script: str | None = None,
        output_size: int | None = None,
        timeout: int | None = None,
        duration: int | None = None,
        output_interval: int | None = None,
        file_only: str | None = None,
        execute_security_fabric: str | None = None,
        accprofile: str | None = None,
        regular_expression: str | None = None,
        log_debug_print: str | None = None,
        security_tag: str | None = None,
        sdn_connector: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new system/automation_action object.

        Action for automation stitches.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            description: Description.
            action_type: Action type.
            system_action: System action type.
            tls_certificate: Custom TLS certificate for API request.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_automation_action.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = AutomationAction.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_automation_action.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(AutomationAction.required_fields()) }}
            
            Use AutomationAction.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            description=description,
            action_type=action_type,
            system_action=system_action,
            tls_certificate=tls_certificate,
            forticare_email=forticare_email,
            email_to=email_to,
            email_from=email_from,
            email_subject=email_subject,
            minimum_interval=minimum_interval,
            aws_api_key=aws_api_key,
            azure_function_authorization=azure_function_authorization,
            azure_api_key=azure_api_key,
            alicloud_function_authorization=alicloud_function_authorization,
            alicloud_access_key_id=alicloud_access_key_id,
            alicloud_access_key_secret=alicloud_access_key_secret,
            message_type=message_type,
            message=message,
            replacement_message=replacement_message,
            replacemsg_group=replacemsg_group,
            protocol=protocol,
            method=method,
            uri=uri,
            http_body=http_body,
            port=port,
            http_headers=http_headers,
            form_data=form_data,
            verify_host_cert=verify_host_cert,
            script=script,
            output_size=output_size,
            timeout=timeout,
            duration=duration,
            output_interval=output_interval,
            file_only=file_only,
            execute_security_fabric=execute_security_fabric,
            accprofile=accprofile,
            regular_expression=regular_expression,
            log_debug_print=log_debug_print,
            security_tag=security_tag,
            sdn_connector=sdn_connector,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.automation_action import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/automation_action",
            )

        endpoint = "/system/automation-action"
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
        Delete system/automation_action object.

        Action for automation stitches.

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
            >>> result = fgt.api.cmdb.system_automation_action.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/automation-action/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/automation_action object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_automation_action.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_automation_action.exists(name=1):
            ...     fgt.api.cmdb.system_automation_action.delete(name=1)

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
        Create or update system/automation_action object (intelligent operation).

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
            >>> result = fgt.api.cmdb.system_automation_action.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_automation_action.set(payload_dict=obj_data)
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


