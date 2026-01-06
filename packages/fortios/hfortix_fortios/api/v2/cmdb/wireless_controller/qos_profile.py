"""
FortiOS CMDB - Wireless_controller qos_profile

Configuration endpoint for managing cmdb wireless_controller/qos_profile objects.

API Endpoints:
    GET    /cmdb/wireless_controller/qos_profile
    POST   /cmdb/wireless_controller/qos_profile
    PUT    /cmdb/wireless_controller/qos_profile/{identifier}
    DELETE /cmdb/wireless_controller/qos_profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_qos_profile.get()

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


class QosProfile(MetadataMixin):
    """QosProfile Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "qos_profile"
    
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
        """Initialize QosProfile endpoint."""
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
        Retrieve wireless_controller/qos_profile configuration.

        Configure WiFi quality of service (QoS) profiles.

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
            >>> # Get all wireless_controller/qos_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/qos_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.wireless_controller_qos_profile.get(action="schema")

        See Also:
            - post(): Create new wireless_controller/qos_profile object
            - put(): Update existing wireless_controller/qos_profile object
            - delete(): Remove wireless_controller/qos_profile object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/wireless-controller/qos-profile/" + str(name)
        else:
            endpoint = "/wireless-controller/qos-profile"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: Literal["enable", "disable"] | None = None,
        wmm: Literal["enable", "disable"] | None = None,
        wmm_uapsd: Literal["enable", "disable"] | None = None,
        call_admission_control: Literal["enable", "disable"] | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: Literal["enable", "disable"] | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = None,
        dscp_wmm_vo: str | list | None = None,
        dscp_wmm_vi: str | list | None = None,
        dscp_wmm_be: str | list | None = None,
        dscp_wmm_bk: str | list | None = None,
        wmm_dscp_marking: Literal["enable", "disable"] | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing wireless_controller/qos_profile object.

        Configure WiFi quality of service (QoS) profiles.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: WiFi QoS profile name.
            comment: Comment.
            uplink: Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            downlink: Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            uplink_sta: Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            comment=comment,
            uplink=uplink,
            downlink=downlink,
            uplink_sta=uplink_sta,
            downlink_sta=downlink_sta,
            burst=burst,
            wmm=wmm,
            wmm_uapsd=wmm_uapsd,
            call_admission_control=call_admission_control,
            call_capacity=call_capacity,
            bandwidth_admission_control=bandwidth_admission_control,
            bandwidth_capacity=bandwidth_capacity,
            dscp_wmm_mapping=dscp_wmm_mapping,
            dscp_wmm_vo=dscp_wmm_vo,
            dscp_wmm_vi=dscp_wmm_vi,
            dscp_wmm_be=dscp_wmm_be,
            dscp_wmm_bk=dscp_wmm_bk,
            wmm_dscp_marking=wmm_dscp_marking,
            wmm_vo_dscp=wmm_vo_dscp,
            wmm_vi_dscp=wmm_vi_dscp,
            wmm_be_dscp=wmm_be_dscp,
            wmm_bk_dscp=wmm_bk_dscp,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.qos_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/qos_profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/qos-profile/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: Literal["enable", "disable"] | None = None,
        wmm: Literal["enable", "disable"] | None = None,
        wmm_uapsd: Literal["enable", "disable"] | None = None,
        call_admission_control: Literal["enable", "disable"] | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: Literal["enable", "disable"] | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = None,
        dscp_wmm_vo: str | list | None = None,
        dscp_wmm_vi: str | list | None = None,
        dscp_wmm_be: str | list | None = None,
        dscp_wmm_bk: str | list | None = None,
        wmm_dscp_marking: Literal["enable", "disable"] | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new wireless_controller/qos_profile object.

        Configure WiFi quality of service (QoS) profiles.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: WiFi QoS profile name.
            comment: Comment.
            uplink: Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            downlink: Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            uplink_sta: Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = QosProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(QosProfile.required_fields()) }}
            
            Use QosProfile.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            comment=comment,
            uplink=uplink,
            downlink=downlink,
            uplink_sta=uplink_sta,
            downlink_sta=downlink_sta,
            burst=burst,
            wmm=wmm,
            wmm_uapsd=wmm_uapsd,
            call_admission_control=call_admission_control,
            call_capacity=call_capacity,
            bandwidth_admission_control=bandwidth_admission_control,
            bandwidth_capacity=bandwidth_capacity,
            dscp_wmm_mapping=dscp_wmm_mapping,
            dscp_wmm_vo=dscp_wmm_vo,
            dscp_wmm_vi=dscp_wmm_vi,
            dscp_wmm_be=dscp_wmm_be,
            dscp_wmm_bk=dscp_wmm_bk,
            wmm_dscp_marking=wmm_dscp_marking,
            wmm_vo_dscp=wmm_vo_dscp,
            wmm_vi_dscp=wmm_vi_dscp,
            wmm_be_dscp=wmm_be_dscp,
            wmm_bk_dscp=wmm_bk_dscp,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.qos_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/qos_profile",
            )

        endpoint = "/wireless-controller/qos-profile"
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
        Delete wireless_controller/qos_profile object.

        Configure WiFi quality of service (QoS) profiles.

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
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/qos-profile/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/qos_profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_qos_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_qos_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_qos_profile.delete(name=1)

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
        Create or update wireless_controller/qos_profile object (intelligent operation).

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
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_qos_profile.set(payload_dict=obj_data)
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
        Move wireless_controller/qos_profile object to a new position.
        
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
            >>> fgt.api.cmdb.wireless_controller_qos_profile.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/qos-profile",
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
        Clone wireless_controller/qos_profile object.
        
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
            >>> fgt.api.cmdb.wireless_controller_qos_profile.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/qos-profile",
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
        Check if wireless_controller/qos_profile object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_qos_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_qos_profile.post(payload_dict=data)
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

