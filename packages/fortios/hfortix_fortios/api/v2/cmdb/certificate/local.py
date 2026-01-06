"""
FortiOS CMDB - Certificate local

Configuration endpoint for managing cmdb certificate/local objects.

API Endpoints:
    GET    /cmdb/certificate/local
    POST   /cmdb/certificate/local
    PUT    /cmdb/certificate/local/{identifier}
    DELETE /cmdb/certificate/local/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.certificate_local.get()

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


class Local(MetadataMixin):
    """Local Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "local"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Local endpoint."""
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
        Retrieve certificate/local configuration.

        Local keys and certificates.

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
            >>> # Get all certificate/local objects
            >>> result = fgt.api.cmdb.certificate_local.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific certificate/local by name
            >>> result = fgt.api.cmdb.certificate_local.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.certificate_local.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.certificate_local.get(action="schema")

        See Also:
            - post(): Create new certificate/local object
            - put(): Update existing certificate/local object
            - delete(): Remove certificate/local object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/certificate/local/" + str(name)
        else:
            endpoint = "/certificate/local"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        password: Any | None = None,
        comments: str | None = None,
        private_key: str | None = None,
        certificate: str | None = None,
        csr: str | None = None,
        state: str | None = None,
        scep_url: str | None = None,
        range: str | None = None,
        source: str | None = None,
        auto_regenerate_days: int | None = None,
        auto_regenerate_days_warning: int | None = None,
        scep_password: Any | None = None,
        ca_identifier: str | None = None,
        name_encoding: str | None = None,
        source_ip: str | None = None,
        ike_localid: str | None = None,
        ike_localid_type: str | None = None,
        enroll_protocol: str | None = None,
        private_key_retain: str | None = None,
        cmp_server: str | None = None,
        cmp_path: str | None = None,
        cmp_server_cert: str | None = None,
        cmp_regeneration_method: str | None = None,
        acme_ca_url: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_eab_key_id: str | None = None,
        acme_eab_key_hmac: Any | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        est_server: str | None = None,
        est_ca_id: str | None = None,
        est_http_username: str | None = None,
        est_http_password: Any | None = None,
        est_client_cert: str | None = None,
        est_server_cert: str | None = None,
        est_srp_username: str | None = None,
        est_srp_password: Any | None = None,
        est_regeneration_method: str | None = None,
        details: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing certificate/local object.

        Local keys and certificates.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            password: Password as a PEM file.
            comments: Comment.
            private_key: PEM format key encrypted with a password.
            certificate: PEM format certificate.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.certificate_local.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.certificate_local.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            password=password,
            comments=comments,
            private_key=private_key,
            certificate=certificate,
            csr=csr,
            state=state,
            scep_url=scep_url,
            range=range,
            source=source,
            auto_regenerate_days=auto_regenerate_days,
            auto_regenerate_days_warning=auto_regenerate_days_warning,
            scep_password=scep_password,
            ca_identifier=ca_identifier,
            name_encoding=name_encoding,
            source_ip=source_ip,
            ike_localid=ike_localid,
            ike_localid_type=ike_localid_type,
            enroll_protocol=enroll_protocol,
            private_key_retain=private_key_retain,
            cmp_server=cmp_server,
            cmp_path=cmp_path,
            cmp_server_cert=cmp_server_cert,
            cmp_regeneration_method=cmp_regeneration_method,
            acme_ca_url=acme_ca_url,
            acme_domain=acme_domain,
            acme_email=acme_email,
            acme_eab_key_id=acme_eab_key_id,
            acme_eab_key_hmac=acme_eab_key_hmac,
            acme_rsa_key_size=acme_rsa_key_size,
            acme_renew_window=acme_renew_window,
            est_server=est_server,
            est_ca_id=est_ca_id,
            est_http_username=est_http_username,
            est_http_password=est_http_password,
            est_client_cert=est_client_cert,
            est_server_cert=est_server_cert,
            est_srp_username=est_srp_username,
            est_srp_password=est_srp_password,
            est_regeneration_method=est_regeneration_method,
            details=details,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.local import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/certificate/local",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/certificate/local/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        password: Any | None = None,
        comments: str | None = None,
        private_key: str | None = None,
        certificate: str | None = None,
        csr: str | None = None,
        state: str | None = None,
        scep_url: str | None = None,
        range: str | None = None,
        source: str | None = None,
        auto_regenerate_days: int | None = None,
        auto_regenerate_days_warning: int | None = None,
        scep_password: Any | None = None,
        ca_identifier: str | None = None,
        name_encoding: str | None = None,
        source_ip: str | None = None,
        ike_localid: str | None = None,
        ike_localid_type: str | None = None,
        enroll_protocol: str | None = None,
        private_key_retain: str | None = None,
        cmp_server: str | None = None,
        cmp_path: str | None = None,
        cmp_server_cert: str | None = None,
        cmp_regeneration_method: str | None = None,
        acme_ca_url: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_eab_key_id: str | None = None,
        acme_eab_key_hmac: Any | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        est_server: str | None = None,
        est_ca_id: str | None = None,
        est_http_username: str | None = None,
        est_http_password: Any | None = None,
        est_client_cert: str | None = None,
        est_server_cert: str | None = None,
        est_srp_username: str | None = None,
        est_srp_password: Any | None = None,
        est_regeneration_method: str | None = None,
        details: Any | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new certificate/local object.

        Local keys and certificates.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            password: Password as a PEM file.
            comments: Comment.
            private_key: PEM format key encrypted with a password.
            certificate: PEM format certificate.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.certificate_local.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Local.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.certificate_local.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Local.required_fields()) }}
            
            Use Local.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            password=password,
            comments=comments,
            private_key=private_key,
            certificate=certificate,
            csr=csr,
            state=state,
            scep_url=scep_url,
            range=range,
            source=source,
            auto_regenerate_days=auto_regenerate_days,
            auto_regenerate_days_warning=auto_regenerate_days_warning,
            scep_password=scep_password,
            ca_identifier=ca_identifier,
            name_encoding=name_encoding,
            source_ip=source_ip,
            ike_localid=ike_localid,
            ike_localid_type=ike_localid_type,
            enroll_protocol=enroll_protocol,
            private_key_retain=private_key_retain,
            cmp_server=cmp_server,
            cmp_path=cmp_path,
            cmp_server_cert=cmp_server_cert,
            cmp_regeneration_method=cmp_regeneration_method,
            acme_ca_url=acme_ca_url,
            acme_domain=acme_domain,
            acme_email=acme_email,
            acme_eab_key_id=acme_eab_key_id,
            acme_eab_key_hmac=acme_eab_key_hmac,
            acme_rsa_key_size=acme_rsa_key_size,
            acme_renew_window=acme_renew_window,
            est_server=est_server,
            est_ca_id=est_ca_id,
            est_http_username=est_http_username,
            est_http_password=est_http_password,
            est_client_cert=est_client_cert,
            est_server_cert=est_server_cert,
            est_srp_username=est_srp_username,
            est_srp_password=est_srp_password,
            est_regeneration_method=est_regeneration_method,
            details=details,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.local import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/certificate/local",
            )

        endpoint = "/certificate/local"
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
        Delete certificate/local object.

        Local keys and certificates.

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
            >>> result = fgt.api.cmdb.certificate_local.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/certificate/local/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if certificate/local object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.certificate_local.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.certificate_local.exists(name=1):
            ...     fgt.api.cmdb.certificate_local.delete(name=1)

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
        Create or update certificate/local object (intelligent operation).

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
            >>> result = fgt.api.cmdb.certificate_local.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.certificate_local.set(payload_dict=obj_data)
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


