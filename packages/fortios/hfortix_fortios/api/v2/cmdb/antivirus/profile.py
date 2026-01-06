"""
FortiOS CMDB - Antivirus profile

Configuration endpoint for managing cmdb antivirus/profile objects.

API Endpoints:
    GET    /cmdb/antivirus/profile
    POST   /cmdb/antivirus/profile
    PUT    /cmdb/antivirus/profile/{identifier}
    DELETE /cmdb/antivirus/profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.antivirus_profile.get()

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


class Profile:
    """Profile Operations."""

    def __init__(self, client: "IHTTPClient"):
        """Initialize Profile endpoint."""
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
        Retrieve antivirus/profile configuration.

        Configure AntiVirus profiles.

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
            >>> # Get all antivirus/profile objects
            >>> result = fgt.api.cmdb.antivirus_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific antivirus/profile by name
            >>> result = fgt.api.cmdb.antivirus_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.antivirus_profile.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.antivirus_profile.get(action="schema")

        See Also:
            - post(): Create new antivirus/profile object
            - put(): Update existing antivirus/profile object
            - delete(): Remove antivirus/profile object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = "/antivirus/profile/" + str(name)
        else:
            endpoint = "/antivirus/profile"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        replacemsg_group: str | None = None,
        feature_set: str | None = None,
        fortisandbox_mode: str | None = None,
        fortisandbox_max_upload: int | None = None,
        analytics_ignore_filetype: int | None = None,
        analytics_accept_filetype: int | None = None,
        analytics_db: str | None = None,
        mobile_malware_db: str | None = None,
        http: str | None = None,
        ftp: str | None = None,
        imap: str | None = None,
        pop3: str | None = None,
        smtp: str | None = None,
        mapi: str | None = None,
        nntp: str | None = None,
        cifs: str | None = None,
        ssh: str | None = None,
        nac_quar: str | None = None,
        content_disarm: str | None = None,
        outbreak_prevention_archive_scan: str | None = None,
        external_blocklist_enable_all: str | None = None,
        external_blocklist: str | list | None = None,
        ems_threat_feed: str | None = None,
        fortindr_error_action: str | None = None,
        fortindr_timeout_action: str | None = None,
        fortisandbox_scan_timeout: int | None = None,
        fortisandbox_error_action: str | None = None,
        fortisandbox_timeout_action: str | None = None,
        av_virus_log: str | None = None,
        extended_log: str | None = None,
        scan_mode: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing antivirus/profile object.

        Configure AntiVirus profiles.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Profile name.
            comment: Comment.
            replacemsg_group: Replacement message group customized for this profile.
            feature_set: Flow/proxy feature set.
            fortisandbox_mode: FortiSandbox scan modes.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.antivirus_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.antivirus_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            name=name,
            comment=comment,
            replacemsg_group=replacemsg_group,
            feature_set=feature_set,
            fortisandbox_mode=fortisandbox_mode,
            fortisandbox_max_upload=fortisandbox_max_upload,
            analytics_ignore_filetype=analytics_ignore_filetype,
            analytics_accept_filetype=analytics_accept_filetype,
            analytics_db=analytics_db,
            mobile_malware_db=mobile_malware_db,
            http=http,
            ftp=ftp,
            imap=imap,
            pop3=pop3,
            smtp=smtp,
            mapi=mapi,
            nntp=nntp,
            cifs=cifs,
            ssh=ssh,
            nac_quar=nac_quar,
            content_disarm=content_disarm,
            outbreak_prevention_archive_scan=outbreak_prevention_archive_scan,
            external_blocklist_enable_all=external_blocklist_enable_all,
            external_blocklist=external_blocklist,
            ems_threat_feed=ems_threat_feed,
            fortindr_error_action=fortindr_error_action,
            fortindr_timeout_action=fortindr_timeout_action,
            fortisandbox_scan_timeout=fortisandbox_scan_timeout,
            fortisandbox_error_action=fortisandbox_error_action,
            fortisandbox_timeout_action=fortisandbox_timeout_action,
            av_virus_log=av_virus_log,
            extended_log=extended_log,
            scan_mode=scan_mode,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/antivirus/profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/antivirus/profile/" + str(name_value)

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        comment: str | None = None,
        replacemsg_group: str | None = None,
        feature_set: str | None = None,
        fortisandbox_mode: str | None = None,
        fortisandbox_max_upload: int | None = None,
        analytics_ignore_filetype: int | None = None,
        analytics_accept_filetype: int | None = None,
        analytics_db: str | None = None,
        mobile_malware_db: str | None = None,
        http: str | None = None,
        ftp: str | None = None,
        imap: str | None = None,
        pop3: str | None = None,
        smtp: str | None = None,
        mapi: str | None = None,
        nntp: str | None = None,
        cifs: str | None = None,
        ssh: str | None = None,
        nac_quar: str | None = None,
        content_disarm: str | None = None,
        outbreak_prevention_archive_scan: str | None = None,
        external_blocklist_enable_all: str | None = None,
        external_blocklist: str | list | None = None,
        ems_threat_feed: str | None = None,
        fortindr_error_action: str | None = None,
        fortindr_timeout_action: str | None = None,
        fortisandbox_scan_timeout: int | None = None,
        fortisandbox_error_action: str | None = None,
        fortisandbox_timeout_action: str | None = None,
        av_virus_log: str | None = None,
        extended_log: str | None = None,
        scan_mode: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create new antivirus/profile object.

        Configure AntiVirus profiles.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Profile name.
            comment: Comment.
            replacemsg_group: Replacement message group customized for this profile.
            feature_set: Flow/proxy feature set.
            fortisandbox_mode: FortiSandbox scan modes.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            raw_json: If True, return raw API response without processing.
            **kwargs: Additional parameters

        Returns:
            API response dict containing created object with assigned name.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.antivirus_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Profile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.antivirus_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Profile.required_fields()) }}
            
            Use Profile.help('field_name') to get field details.

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
            replacemsg_group=replacemsg_group,
            feature_set=feature_set,
            fortisandbox_mode=fortisandbox_mode,
            fortisandbox_max_upload=fortisandbox_max_upload,
            analytics_ignore_filetype=analytics_ignore_filetype,
            analytics_accept_filetype=analytics_accept_filetype,
            analytics_db=analytics_db,
            mobile_malware_db=mobile_malware_db,
            http=http,
            ftp=ftp,
            imap=imap,
            pop3=pop3,
            smtp=smtp,
            mapi=mapi,
            nntp=nntp,
            cifs=cifs,
            ssh=ssh,
            nac_quar=nac_quar,
            content_disarm=content_disarm,
            outbreak_prevention_archive_scan=outbreak_prevention_archive_scan,
            external_blocklist_enable_all=external_blocklist_enable_all,
            external_blocklist=external_blocklist,
            ems_threat_feed=ems_threat_feed,
            fortindr_error_action=fortindr_error_action,
            fortindr_timeout_action=fortindr_timeout_action,
            fortisandbox_scan_timeout=fortisandbox_scan_timeout,
            fortisandbox_error_action=fortisandbox_error_action,
            fortisandbox_timeout_action=fortisandbox_timeout_action,
            av_virus_log=av_virus_log,
            extended_log=extended_log,
            scan_mode=scan_mode,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/antivirus/profile",
            )

        endpoint = "/antivirus/profile"
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
        Delete antivirus/profile object.

        Configure AntiVirus profiles.

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
            >>> result = fgt.api.cmdb.antivirus_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/antivirus/profile/" + str(name)

        return self._client.delete(
            "cmdb", endpoint, params=kwargs, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if antivirus/profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.antivirus_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.antivirus_profile.exists(name=1):
            ...     fgt.api.cmdb.antivirus_profile.delete(name=1)

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
        Create or update antivirus/profile object (intelligent operation).

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
            >>> result = fgt.api.cmdb.antivirus_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.antivirus_profile.set(payload_dict=obj_data)
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
    # Metadata Helper Methods
    # Provide easy access to schema metadata without separate imports
    # ========================================================================

    @staticmethod
    def help(field_name: str | None = None) -> str:
        """
        Get help text for endpoint or specific field.

        Args:
            field_name: Optional field name to get help for. If None, shows endpoint help.

        Returns:
            Formatted help text

        Examples:
            >>> # Get endpoint information
            >>> print(Profile.help())
            
            >>> # Get field information
            >>> print(Profile.help("name"))
        """
        from ._helpers.profile import (
            get_schema_info,
            get_field_metadata,
        )

        if field_name is None:
            # Endpoint help
            info = get_schema_info()
            lines = [
                f"Endpoint: {info['endpoint']}",
                f"Category: {info['category']}",
                f"Help: {info.get('help', 'N/A')}",
                "",
                f"Total Fields: {info['total_fields']}",
                f"Required Fields: {info['required_fields_count']}",
                f"Fields with Defaults: {info['fields_with_defaults_count']}",
            ]
            if 'mkey' in info:
                lines.append(f"\nPrimary Key: {info['mkey']} ({info['mkey_type']})")
            return "\n".join(lines)
        
        # Field help
        meta = get_field_metadata(field_name)
        if meta is None:
            return f"Unknown field: {field_name}"

        lines = [
            f"Field: {meta['name']}",
            f"Type: {meta['type']}",
        ]
        if 'description' in meta:
            lines.append(f"Description: {meta['description']}")
        lines.append(f"Required: {'Yes' if meta.get('required', False) else 'No'}")
        if 'default' in meta:
            lines.append(f"Default: {meta['default']}")
        if 'options' in meta:
            lines.append(f"Options: {', '.join(meta['options'])}")
        if 'constraints' in meta:
            constraints = meta['constraints']
            if 'min' in constraints or 'max' in constraints:
                min_val = constraints.get('min', '?')
                max_val = constraints.get('max', '?')
                lines.append(f"Range: {min_val} - {max_val}")
            if 'max_length' in constraints:
                lines.append(f"Max Length: {constraints['max_length']}")

        return "\n".join(lines)

    @staticmethod
    def fields(detailed: bool = False) -> Union[list[str], dict[str, dict]]:
        """
        Get list of all field names or detailed field information.

        Args:
            detailed: If True, return dict with field metadata

        Returns:
            List of field names or dict of field metadata

        Examples:
            >>> # Simple list
            >>> fields = Profile.fields()
            >>> print(f"Available fields: {len(fields)}")
            
            >>> # Detailed info
            >>> fields = Profile.fields(detailed=True)
            >>> for name, meta in fields.items():
            ...     print(f"{name}: {meta['type']}")
        """
        from ._helpers.profile import get_all_fields, get_field_metadata

        field_names = get_all_fields()

        if not detailed:
            return field_names

        # Build detailed dict
        detailed_fields = {}
        for fname in field_names:
            meta = get_field_metadata(fname)
            if meta:
                detailed_fields[fname] = meta

        return detailed_fields

    @staticmethod
    def field_info(field_name: str) -> dict[str, Any] | None:
        """
        Get complete metadata for a specific field.

        Args:
            field_name: Name of the field

        Returns:
            Field metadata dict or None if field doesn't exist

        Examples:
            >>> info = Profile.field_info("name")
            >>> print(f"Type: {info['type']}")
            >>> if 'options' in info:
            ...     print(f"Options: {info['options']}")
        """
        from ._helpers.profile import get_field_metadata

        return get_field_metadata(field_name)

    @staticmethod
    def validate_field(field_name: str, value: Any) -> tuple[bool, str | None]:
        """
        Validate a field value against its constraints.

        Args:
            field_name: Name of the field
            value: Value to validate

        Returns:
            Tuple of (is_valid, error_message)

        Examples:
            >>> is_valid, error = Profile.validate_field("name", "test")
            >>> if not is_valid:
            ...     print(f"Validation error: {error}")
        """
        from ._helpers.profile import validate_field_value

        return validate_field_value(field_name, value)

    @staticmethod
    def required_fields() -> list[str]:
        """
        Get list of required field names.

        Note: Due to FortiOS schema quirks, some fields may be conditionally required.
        Always test with the actual API for authoritative requirements.

        Returns:
            List of required field names

        Examples:
            >>> required = Profile.required_fields()
            >>> print(f"Required fields: {', '.join(required)}")
        """
        from ._helpers.profile import REQUIRED_FIELDS

        return REQUIRED_FIELDS.copy()

    @staticmethod
    def defaults() -> dict[str, Any]:
        """
        Get all fields with default values.

        Returns:
            Dict mapping field names to default values

        Examples:
            >>> defaults = Profile.defaults()
            >>> print(f"Fields with defaults: {len(defaults)}")
            >>> # Use as starting point for payload
            >>> payload = defaults.copy()
            >>> payload['name'] = 'my-custom-name'
        """
        from ._helpers.profile import FIELDS_WITH_DEFAULTS

        return FIELDS_WITH_DEFAULTS.copy()

    @staticmethod
    def schema() -> dict[str, Any]:
        """
        Get complete schema information for this endpoint.

        Returns:
            Schema metadata dict containing endpoint info, field counts, and primary key

        Examples:
            >>> schema = Profile.schema()
            >>> print(f"Endpoint: {schema['endpoint']}")
            >>> print(f"Total fields: {schema['total_fields']}")
            >>> print(f"Primary key: {schema.get('mkey', 'N/A')}")
        """
        from ._helpers.profile import get_schema_info

        return get_schema_info()
