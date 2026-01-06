"""
FortiOS CMDB - Firewall shaping_policy

Configuration endpoint for managing cmdb firewall/shaping_policy objects.

API Endpoints:
    GET    /cmdb/firewall/shaping_policy
    POST   /cmdb/firewall/shaping_policy
    PUT    /cmdb/firewall/shaping_policy/{identifier}
    DELETE /cmdb/firewall/shaping_policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_shaping_policy.get()

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


class ShapingPolicy(MetadataMixin):
    """ShapingPolicy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "shaping_policy"

    def __init__(self, client: "IHTTPClient"):
        """Initialize ShapingPolicy endpoint."""
        self._client = client

    def get(
        self,
        id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve firewall/shaping_policy configuration.

        Configure shaping policies.

        Args:
            id: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/shaping_policy objects
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/shaping_policy by id
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get(id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.firewall_shaping_policy.get(action="schema")

        See Also:
            - post(): Create new firewall/shaping_policy object
            - put(): Update existing firewall/shaping_policy object
            - delete(): Remove firewall/shaping_policy object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if id:
            endpoint = "/firewall/shaping-policy/" + str(id)
        else:
            endpoint = "/firewall/shaping-policy"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: str | None = None,
        ip_version: str | None = None,
        traffic_type: str | None = None,
        srcaddr: str | list | None = None,
        dstaddr: str | list | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        internet_service: str | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: str | list | None = None,
        internet_service_src_group: str | list | None = None,
        internet_service_src_custom: str | list | None = None,
        internet_service_src_custom_group: str | list | None = None,
        internet_service_src_fortiguard: str | list | None = None,
        service: str | list | None = None,
        schedule: str | None = None,
        users: str | list | None = None,
        groups: str | list | None = None,
        application: str | list | None = None,
        app_category: str | list | None = None,
        app_group: str | list | None = None,
        url_category: str | list | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing firewall/shaping_policy object.

        Configure shaping policies.

        Args:
            payload_dict: Object data as dict. Must include id (primary key).
            id: Shaping policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            name: Shaping policy name.
            comment: Comments.
            status: Enable/disable this traffic shaping policy.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_shaping_policy.put(
            ...     id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_shaping_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            uuid=uuid,
            name=name,
            comment=comment,
            status=status,
            ip_version=ip_version,
            traffic_type=traffic_type,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            service=service,
            schedule=schedule,
            users=users,
            groups=groups,
            application=application,
            app_category=app_category,
            app_group=app_group,
            url_category=url_category,
            srcintf=srcintf,
            dstintf=dstintf,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            class_id=class_id,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            cos_mask=cos_mask,
            cos=cos,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.shaping_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/shaping_policy",
            )
        
        id_value = payload_data.get("id")
        if not id_value:
            raise ValueError("id is required for PUT")
        endpoint = "/firewall/shaping-policy/" + str(id_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: str | None = None,
        ip_version: str | None = None,
        traffic_type: str | None = None,
        srcaddr: str | list | None = None,
        dstaddr: str | list | None = None,
        srcaddr6: str | list | None = None,
        dstaddr6: str | list | None = None,
        internet_service: str | None = None,
        internet_service_name: str | list | None = None,
        internet_service_group: str | list | None = None,
        internet_service_custom: str | list | None = None,
        internet_service_custom_group: str | list | None = None,
        internet_service_fortiguard: str | list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: str | list | None = None,
        internet_service_src_group: str | list | None = None,
        internet_service_src_custom: str | list | None = None,
        internet_service_src_custom_group: str | list | None = None,
        internet_service_src_fortiguard: str | list | None = None,
        service: str | list | None = None,
        schedule: str | None = None,
        users: str | list | None = None,
        groups: str | list | None = None,
        application: str | list | None = None,
        app_category: str | list | None = None,
        app_group: str | list | None = None,
        url_category: str | list | None = None,
        srcintf: str | list | None = None,
        dstintf: str | list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new firewall/shaping_policy object.

        Configure shaping policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            id: Shaping policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            name: Shaping policy name.
            comment: Comments.
            status: Enable/disable this traffic shaping policy.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned id.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_shaping_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ShapingPolicy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_shaping_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ShapingPolicy.required_fields()) }}
            
            Use ShapingPolicy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            id=id,
            uuid=uuid,
            name=name,
            comment=comment,
            status=status,
            ip_version=ip_version,
            traffic_type=traffic_type,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            service=service,
            schedule=schedule,
            users=users,
            groups=groups,
            application=application,
            app_category=app_category,
            app_group=app_group,
            url_category=url_category,
            srcintf=srcintf,
            dstintf=dstintf,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            class_id=class_id,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            cos_mask=cos_mask,
            cos=cos,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.shaping_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/shaping_policy",
            )

        endpoint = "/firewall/shaping-policy"
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete firewall/shaping_policy object.

        Configure shaping policies.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name
            raw_json: If True, return raw API response
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_shaping_policy.delete(id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not id:
            raise ValueError("id is required for DELETE")
        endpoint = "/firewall/shaping-policy/" + str(id)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/shaping_policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_shaping_policy.exists(id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_shaping_policy.exists(id=1):
            ...     fgt.api.cmdb.firewall_shaping_policy.delete(id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        try:
            response = self.get(id=id, vdom=vdom, raw_json=True)
            
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
        Create or update firewall/shaping_policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (id) in the payload.

        Args:
            payload_dict: Resource data including id (primary key)
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            API response dictionary

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Intelligent create or update - no need to check exists()
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_shaping_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_shaping_policy.set(payload_dict=obj_data)
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
        
        mkey_value = payload_dict.get("id")
        if not mkey_value:
            raise ValueError("id is required in payload_dict for set()")
        
        # Check if resource exists
        if self.exists(id=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_dict, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_dict, vdom=vdom, **kwargs)


