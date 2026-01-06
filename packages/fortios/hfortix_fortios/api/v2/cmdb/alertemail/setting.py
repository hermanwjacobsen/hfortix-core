"""
FortiOS CMDB - Alertemail setting

Configuration endpoint for managing cmdb alertemail/setting objects.

API Endpoints:
    GET    /cmdb/alertemail/setting
    POST   /cmdb/alertemail/setting
    PUT    /cmdb/alertemail/setting/{identifier}
    DELETE /cmdb/alertemail/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.alertemail_setting.get()

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


class Setting(MetadataMixin):
    """Setting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "setting"

    def __init__(self, client: "IHTTPClient"):
        """Initialize Setting endpoint."""
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
        Retrieve alertemail/setting configuration.

        Configure alert email settings.

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
            >>> # Get all alertemail/setting objects
            >>> result = fgt.api.cmdb.alertemail_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.alertemail_setting.get(
            ...     payload_dict={"filter": ["name==test"]}
            ... )
            
            >>> # Get schema information
            >>> schema = fgt.api.cmdb.alertemail_setting.get(action="schema")

        See Also:
            - post(): Create new alertemail/setting object
            - put(): Update existing alertemail/setting object
            - delete(): Remove alertemail/setting object
            - exists(): Check if object exists
        """
        params = payload_dict.copy() if payload_dict else {}
        
        if name:
            endpoint = f"/alertemail/setting/{name}"
        else:
            endpoint = "/alertemail/setting"
        
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )


    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        username: str | None = None,
        mailto1: str | None = None,
        mailto2: str | None = None,
        mailto3: str | None = None,
        filter_mode: str | None = None,
        email_interval: int | None = None,
        IPS_logs: str | None = None,
        firewall_authentication_failure_logs: str | None = None,
        HA_logs: str | None = None,
        IPsec_errors_logs: str | None = None,
        FDS_update_logs: str | None = None,
        PPP_errors_logs: str | None = None,
        sslvpn_authentication_errors_logs: str | None = None,
        antivirus_logs: str | None = None,
        webfilter_logs: str | None = None,
        configuration_changes_logs: str | None = None,
        violation_traffic_logs: str | None = None,
        admin_login_logs: str | None = None,
        FDS_license_expiring_warning: str | None = None,
        log_disk_usage_warning: str | None = None,
        fortiguard_log_quota_warning: str | None = None,
        amc_interface_bypass_mode: str | None = None,
        FIPS_CC_errors: str | None = None,
        FSSO_disconnect_logs: str | None = None,
        ssh_logs: str | None = None,
        local_disk_usage: int | None = None,
        emergency_interval: int | None = None,
        alert_interval: int | None = None,
        critical_interval: int | None = None,
        error_interval: int | None = None,
        warning_interval: int | None = None,
        notification_interval: int | None = None,
        information_interval: int | None = None,
        debug_interval: int | None = None,
        severity: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update existing alertemail/setting object.

        Configure alert email settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            username: Name that appears in the From: field of alert emails (max. 63 characters).
            mailto1: Email address to send alert email to (usually a system administrator) (max. 63 characters).
            mailto2: Optional second email address to send alert email to (max. 63 characters).
            mailto3: Optional third email address to send alert email to (max. 63 characters).
            filter_mode: How to filter log messages that are sent to alert emails.
            vdom: Virtual domain name.
            raw_json: If True, return raw API response.
            **kwargs: Additional parameters

        Returns:
            API response dict

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.alertemail_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.alertemail_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function
        # Note: Skip reserved parameters (data, vdom, raw_json, kwargs) and Python keywords from field list
        payload_data = build_cmdb_payload(
            username=username,
            mailto1=mailto1,
            mailto2=mailto2,
            mailto3=mailto3,
            filter_mode=filter_mode,
            email_interval=email_interval,
            IPS_logs=IPS_logs,
            firewall_authentication_failure_logs=firewall_authentication_failure_logs,
            HA_logs=HA_logs,
            IPsec_errors_logs=IPsec_errors_logs,
            FDS_update_logs=FDS_update_logs,
            PPP_errors_logs=PPP_errors_logs,
            sslvpn_authentication_errors_logs=sslvpn_authentication_errors_logs,
            antivirus_logs=antivirus_logs,
            webfilter_logs=webfilter_logs,
            configuration_changes_logs=configuration_changes_logs,
            violation_traffic_logs=violation_traffic_logs,
            admin_login_logs=admin_login_logs,
            FDS_license_expiring_warning=FDS_license_expiring_warning,
            log_disk_usage_warning=log_disk_usage_warning,
            fortiguard_log_quota_warning=fortiguard_log_quota_warning,
            amc_interface_bypass_mode=amc_interface_bypass_mode,
            FIPS_CC_errors=FIPS_CC_errors,
            FSSO_disconnect_logs=FSSO_disconnect_logs,
            ssh_logs=ssh_logs,
            local_disk_usage=local_disk_usage,
            emergency_interval=emergency_interval,
            alert_interval=alert_interval,
            critical_interval=critical_interval,
            error_interval=error_interval,
            warning_interval=warning_interval,
            notification_interval=notification_interval,
            information_interval=information_interval,
            debug_interval=debug_interval,
            severity=severity,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/alertemail/setting",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = f"/alertemail/setting/{name_value}"

        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=kwargs, vdom=vdom, raw_json=raw_json
        )





