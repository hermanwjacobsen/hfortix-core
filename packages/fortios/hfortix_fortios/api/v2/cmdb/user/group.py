"""
FortiOS CMDB - User group

Configuration endpoint for managing cmdb user/group objects.

API Endpoints:
    GET    /cmdb/user/group
    POST   /cmdb/user/group
    PUT    /cmdb/user/group/{identifier}
    DELETE /cmdb/user/group/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.user_group.get()

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


class Group(MetadataMixin):
    """Group Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "group"
    
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
        """Initialize Group endpoint."""
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
        Retrieve user/group configuration.

        Configure user groups.

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
            >>> # Get all user/group objects
            >>> result = fgt.api.cmdb.user_group.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific user/group by name
            >>> result = fgt.api.cmdb.user_group.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.user_group.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.user_group.get(action="schema")

        See Also:
            - post(): Create new user/group object
            - put(): Update existing user/group object
            - delete(): Remove user/group object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/user/group/" + str(name)
        else:
            endpoint = "/user/group"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = None,
        authtimeout: int | None = None,
        auth_concurrent_override: Literal["enable", "disable"] | None = None,
        auth_concurrent_value: int | None = None,
        http_digest_realm: str | None = None,
        sso_attribute_value: str | None = None,
        member: str | list | None = None,
        match: str | list | None = None,
        user_id: Literal["email", "auto-generate", "specify"] | None = None,
        password: Literal["auto-generate", "specify", "disable"] | None = None,
        user_name: Literal["disable", "enable"] | None = None,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = None,
        company: Literal["optional", "mandatory", "disabled"] | None = None,
        email: Literal["disable", "enable"] | None = None,
        mobile_phone: Literal["disable", "enable"] | None = None,
        sms_server: Literal["fortiguard", "custom"] | None = None,
        sms_custom_server: str | None = None,
        expire_type: Literal["immediately", "first-successful-login"] | None = None,
        expire: int | None = None,
        max_accounts: int | None = None,
        multiple_guest_add: Literal["disable", "enable"] | None = None,
        guest: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing user/group object.

        Configure user groups.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Group name.
            id: Group ID.
            group_type: Set the group to be for firewall authentication, FSSO, RSSO, or guest users.
            authtimeout: Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.
            auth_concurrent_override: Enable/disable overriding the global number of concurrent authentication sessions for this user group.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.user_group.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.user_group.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            id=id,
            group_type=group_type,
            authtimeout=authtimeout,
            auth_concurrent_override=auth_concurrent_override,
            auth_concurrent_value=auth_concurrent_value,
            http_digest_realm=http_digest_realm,
            sso_attribute_value=sso_attribute_value,
            member=member,
            match=match,
            user_id=user_id,
            password=password,
            user_name=user_name,
            sponsor=sponsor,
            company=company,
            email=email,
            mobile_phone=mobile_phone,
            sms_server=sms_server,
            sms_custom_server=sms_custom_server,
            expire_type=expire_type,
            expire=expire,
            max_accounts=max_accounts,
            multiple_guest_add=multiple_guest_add,
            guest=guest,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.group import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/group",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/user/group/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        group_type: Literal["firewall", "fsso-service", "rsso", "guest"] | None = None,
        authtimeout: int | None = None,
        auth_concurrent_override: Literal["enable", "disable"] | None = None,
        auth_concurrent_value: int | None = None,
        http_digest_realm: str | None = None,
        sso_attribute_value: str | None = None,
        member: str | list | None = None,
        match: str | list | None = None,
        user_id: Literal["email", "auto-generate", "specify"] | None = None,
        password: Literal["auto-generate", "specify", "disable"] | None = None,
        user_name: Literal["disable", "enable"] | None = None,
        sponsor: Literal["optional", "mandatory", "disabled"] | None = None,
        company: Literal["optional", "mandatory", "disabled"] | None = None,
        email: Literal["disable", "enable"] | None = None,
        mobile_phone: Literal["disable", "enable"] | None = None,
        sms_server: Literal["fortiguard", "custom"] | None = None,
        sms_custom_server: str | None = None,
        expire_type: Literal["immediately", "first-successful-login"] | None = None,
        expire: int | None = None,
        max_accounts: int | None = None,
        multiple_guest_add: Literal["disable", "enable"] | None = None,
        guest: str | list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new user/group object.

        Configure user groups.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Group name.
            id: Group ID.
            group_type: Set the group to be for firewall authentication, FSSO, RSSO, or guest users.
            authtimeout: Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.
            auth_concurrent_override: Enable/disable overriding the global number of concurrent authentication sessions for this user group.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.user_group.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Group.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.user_group.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Group.required_fields()) }}
            
            Use Group.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            id=id,
            group_type=group_type,
            authtimeout=authtimeout,
            auth_concurrent_override=auth_concurrent_override,
            auth_concurrent_value=auth_concurrent_value,
            http_digest_realm=http_digest_realm,
            sso_attribute_value=sso_attribute_value,
            member=member,
            match=match,
            user_id=user_id,
            password=password,
            user_name=user_name,
            sponsor=sponsor,
            company=company,
            email=email,
            mobile_phone=mobile_phone,
            sms_server=sms_server,
            sms_custom_server=sms_custom_server,
            expire_type=expire_type,
            expire=expire,
            max_accounts=max_accounts,
            multiple_guest_add=multiple_guest_add,
            guest=guest,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.group import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/user/group",
            )

        endpoint = "/user/group"
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
        Delete user/group object.

        Configure user groups.

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
            >>> result = fgt.api.cmdb.user_group.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/user/group/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if user/group object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.user_group.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.user_group.exists(name=1):
            ...     fgt.api.cmdb.user_group.delete(name=1)

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
        Create or update user/group object (intelligent operation).

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
            >>> result = fgt.api.cmdb.user_group.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.user_group.set(payload_dict=obj_data)
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
        Move user/group object to a new position.
        
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
            >>> fgt.api.cmdb.user_group.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/user/group",
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
        Clone user/group object.
        
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
            >>> fgt.api.cmdb.user_group.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/user/group",
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
        Check if user/group object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.user_group.exists(name=1):
            ...     fgt.api.cmdb.user_group.post(payload_dict=data)
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

