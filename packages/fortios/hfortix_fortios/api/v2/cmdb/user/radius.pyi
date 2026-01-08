from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class RadiusPayload(TypedDict, total=False):
    """
    Type hints for user/radius payload fields.
    
    Configure RADIUS server entries.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: ca-cert)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: client-cert)

    **Usage:**
        payload: RadiusPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # RADIUS server entry name.
    server: str  # Primary RADIUS server CN domain name or IP address.
    secret: str  # Pre-shared secret key used to access the primary RADIUS serv
    secondary_server: NotRequired[str]  # Secondary RADIUS CN domain name or IP address.
    secondary_secret: NotRequired[str]  # Secret key to access the secondary server.
    tertiary_server: NotRequired[str]  # Tertiary RADIUS CN domain name or IP address.
    tertiary_secret: NotRequired[str]  # Secret key to access the tertiary server.
    timeout: NotRequired[int]  # Time in seconds to retry connecting server.
    status_ttl: NotRequired[int]  # Time for which server reachability is cached so that when a
    all_usergroup: NotRequired[Literal["disable", "enable"]]  # Enable/disable automatically including this RADIUS server in
    use_management_vdom: NotRequired[Literal["enable", "disable"]]  # Enable/disable using management VDOM to send requests.
    switch_controller_nas_ip_dynamic: NotRequired[Literal["enable", "disable"]]  # Enable/Disable switch-controller nas-ip dynamic to dynamical
    nas_ip: NotRequired[str]  # IP address used to communicate with the RADIUS server and us
    nas_id_type: NotRequired[Literal["legacy", "custom", "hostname"]]  # NAS identifier type configuration (default = legacy).
    call_station_id_type: NotRequired[Literal["legacy", "IP", "MAC"]]  # Calling & Called station identifier type configuration
    nas_id: NotRequired[str]  # Custom NAS identifier.
    acct_interim_interval: NotRequired[int]  # Time in seconds between each accounting interim update messa
    radius_coa: NotRequired[Literal["enable", "disable"]]  # Enable to allow a mechanism to change the attributes of an a
    radius_port: NotRequired[int]  # RADIUS service port number.
    h3c_compatibility: NotRequired[Literal["enable", "disable"]]  # Enable/disable compatibility with the H3C, a mechanism that
    auth_type: NotRequired[Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]]  # Authentication methods/protocols permitted for this RADIUS s
    source_ip: NotRequired[str]  # Source IP address for communications to the RADIUS server.
    source_ip_interface: NotRequired[str]  # Source interface for communication with the RADIUS server.
    username_case_sensitive: NotRequired[Literal["enable", "disable"]]  # Enable/disable case sensitive user names.
    group_override_attr_type: NotRequired[Literal["filter-Id", "class"]]  # RADIUS attribute type to override user group information.
    password_renewal: NotRequired[Literal["enable", "disable"]]  # Enable/disable password renewal.
    require_message_authenticator: NotRequired[Literal["enable", "disable"]]  # Require message authenticator in authentication response.
    password_encoding: NotRequired[Literal["auto", "ISO-8859-1"]]  # Password encoding.
    mac_username_delimiter: NotRequired[Literal["hyphen", "single-hyphen", "colon", "none"]]  # MAC authentication username delimiter (default = hyphen).
    mac_password_delimiter: NotRequired[Literal["hyphen", "single-hyphen", "colon", "none"]]  # MAC authentication password delimiter (default = hyphen).
    mac_case: NotRequired[Literal["uppercase", "lowercase"]]  # MAC authentication case (default = lowercase).
    acct_all_servers: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending of accounting messages to all configu
    switch_controller_acct_fast_framedip_detect: NotRequired[int]  # Switch controller accounting message Framed-IP detection fro
    interface_select_method: NotRequired[Literal["auto", "sdwan", "specify"]]  # Specify how to select outgoing interface to reach server.
    interface: str  # Specify outgoing interface to reach server.
    vrf_select: NotRequired[int]  # VRF ID used for connection to server.
    switch_controller_service_type: NotRequired[Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"]]  # RADIUS service type.
    transport_protocol: NotRequired[Literal["udp", "tcp", "tls"]]  # Transport protocol to be used (default = udp).
    tls_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for TLS connections
    ca_cert: NotRequired[str]  # CA of server to trust under TLS.
    client_cert: NotRequired[str]  # Client certificate to use under TLS.
    server_identity_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable RADIUS server identity check
    account_key_processing: NotRequired[Literal["same", "strip"]]  # Account key processing operation. The FortiGate will keep ei
    account_key_cert_field: NotRequired[Literal["othername", "rfc822name", "dnsname", "cn"]]  # Define subject identity field in certificate for user access
    rsso: Literal["enable", "disable"]  # Enable/disable RADIUS based single sign on feature.
    rsso_radius_server_port: int  # UDP port to listen on for RADIUS Start and Stop records.
    rsso_radius_response: Literal["enable", "disable"]  # Enable/disable sending RADIUS response packets after receivi
    rsso_validate_request_secret: Literal["enable", "disable"]  # Enable/disable validating the RADIUS request shared secret i
    rsso_secret: str  # RADIUS secret used by the RADIUS accounting server.
    rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attributes used to extract the user end point identif
    rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attributes used to block a user.
    sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]  # RADIUS attribute that contains the profile group name to be
    sso_attribute_key: NotRequired[str]  # Key prefix for SSO group value in the SSO attribute.
    sso_attribute_value_override: Literal["enable", "disable"]  # Enable/disable override old attribute value with new value f
    rsso_context_timeout: int  # Time in seconds before the logged out user is removed from t
    rsso_log_period: int  # Time interval in seconds that group event log messages will
    rsso_log_flags: NotRequired[Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"]]  # Events to log.
    rsso_flush_ip_session: NotRequired[Literal["enable", "disable"]]  # Enable/disable flushing user IP sessions on RADIUS accountin
    rsso_ep_one_ip_only: NotRequired[Literal["enable", "disable"]]  # Enable/disable the replacement of old IP addresses with new
    delimiter: NotRequired[Literal["plus", "comma"]]  # Configure delimiter to be used for separating profile group
    accounting_server: NotRequired[list[dict[str, Any]]]  # Additional accounting servers.

# Nested classes for table field children

@final
class RadiusClassObject:
    """Typed object for class table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Class name.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class RadiusAccountingserverObject:
    """Typed object for accounting-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID (0 - 4294967295).
    id: int
    # Status.
    status: Literal["enable", "disable"]
    # Server CN domain name or IP address.
    server: str
    # Secret key.
    secret: str
    # RADIUS accounting port number.
    port: int
    # Source IP address for communications to the RADIUS server.
    source_ip: str
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class RadiusResponse(TypedDict):
    """
    Type hints for user/radius API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str
    server: str
    secret: str
    secondary_server: str
    secondary_secret: str
    tertiary_server: str
    tertiary_secret: str
    timeout: int
    status_ttl: int
    all_usergroup: Literal["disable", "enable"]
    use_management_vdom: Literal["enable", "disable"]
    switch_controller_nas_ip_dynamic: Literal["enable", "disable"]
    nas_ip: str
    nas_id_type: Literal["legacy", "custom", "hostname"]
    call_station_id_type: Literal["legacy", "IP", "MAC"]
    nas_id: str
    acct_interim_interval: int
    radius_coa: Literal["enable", "disable"]
    radius_port: int
    h3c_compatibility: Literal["enable", "disable"]
    auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]
    source_ip: str
    source_ip_interface: str
    username_case_sensitive: Literal["enable", "disable"]
    group_override_attr_type: Literal["filter-Id", "class"]
    password_renewal: Literal["enable", "disable"]
    require_message_authenticator: Literal["enable", "disable"]
    password_encoding: Literal["auto", "ISO-8859-1"]
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    mac_case: Literal["uppercase", "lowercase"]
    acct_all_servers: Literal["enable", "disable"]
    switch_controller_acct_fast_framedip_detect: int
    interface_select_method: Literal["auto", "sdwan", "specify"]
    interface: str
    vrf_select: int
    switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"]
    transport_protocol: Literal["udp", "tcp", "tls"]
    tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    ca_cert: str
    client_cert: str
    server_identity_check: Literal["enable", "disable"]
    account_key_processing: Literal["same", "strip"]
    account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"]
    rsso: Literal["enable", "disable"]
    rsso_radius_server_port: int
    rsso_radius_response: Literal["enable", "disable"]
    rsso_validate_request_secret: Literal["enable", "disable"]
    rsso_secret: str
    rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    sso_attribute_key: str
    sso_attribute_value_override: Literal["enable", "disable"]
    rsso_context_timeout: int
    rsso_log_period: int
    rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"]
    rsso_flush_ip_session: Literal["enable", "disable"]
    rsso_ep_one_ip_only: Literal["enable", "disable"]
    delimiter: Literal["plus", "comma"]
    accounting_server: list[dict[str, Any]]


@final
class RadiusObject:
    """Typed FortiObject for user/radius with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # RADIUS server entry name.
    name: str
    # Primary RADIUS server CN domain name or IP address.
    server: str
    # Pre-shared secret key used to access the primary RADIUS server.
    secret: str
    # Secondary RADIUS CN domain name or IP address.
    secondary_server: str
    # Secret key to access the secondary server.
    secondary_secret: str
    # Tertiary RADIUS CN domain name or IP address.
    tertiary_server: str
    # Secret key to access the tertiary server.
    tertiary_secret: str
    # Time in seconds to retry connecting server.
    timeout: int
    # Time for which server reachability is cached so that when a server is unreachabl
    status_ttl: int
    # Enable/disable automatically including this RADIUS server in all user groups.
    all_usergroup: Literal["disable", "enable"]
    # Enable/disable using management VDOM to send requests.
    use_management_vdom: Literal["enable", "disable"]
    # Enable/Disable switch-controller nas-ip dynamic to dynamically set nas-ip.
    switch_controller_nas_ip_dynamic: Literal["enable", "disable"]
    # IP address used to communicate with the RADIUS server and used as NAS-IP-Address
    nas_ip: str
    # NAS identifier type configuration (default = legacy).
    nas_id_type: Literal["legacy", "custom", "hostname"]
    # Calling & Called station identifier type configuration (default = legacy), this
    call_station_id_type: Literal["legacy", "IP", "MAC"]
    # Custom NAS identifier.
    nas_id: str
    # Time in seconds between each accounting interim update message.
    acct_interim_interval: int
    # Enable to allow a mechanism to change the attributes of an authentication, autho
    radius_coa: Literal["enable", "disable"]
    # RADIUS service port number.
    radius_port: int
    # Enable/disable compatibility with the H3C, a mechanism that performs security ch
    h3c_compatibility: Literal["enable", "disable"]
    # Authentication methods/protocols permitted for this RADIUS server.
    auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"]
    # Source IP address for communications to the RADIUS server.
    source_ip: str
    # Source interface for communication with the RADIUS server.
    source_ip_interface: str
    # Enable/disable case sensitive user names.
    username_case_sensitive: Literal["enable", "disable"]
    # RADIUS attribute type to override user group information.
    group_override_attr_type: Literal["filter-Id", "class"]
    # Enable/disable password renewal.
    password_renewal: Literal["enable", "disable"]
    # Require message authenticator in authentication response.
    require_message_authenticator: Literal["enable", "disable"]
    # Password encoding.
    password_encoding: Literal["auto", "ISO-8859-1"]
    # MAC authentication username delimiter (default = hyphen).
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC authentication password delimiter (default = hyphen).
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC authentication case (default = lowercase).
    mac_case: Literal["uppercase", "lowercase"]
    # Enable/disable sending of accounting messages to all configured servers
    acct_all_servers: Literal["enable", "disable"]
    # Switch controller accounting message Framed-IP detection from DHCP snooping
    switch_controller_acct_fast_framedip_detect: int
    # Specify how to select outgoing interface to reach server.
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server.
    interface: str
    # VRF ID used for connection to server.
    vrf_select: int
    # RADIUS service type.
    switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"]
    # Transport protocol to be used (default = udp).
    transport_protocol: Literal["udp", "tcp", "tls"]
    # Minimum supported protocol version for TLS connections
    tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # CA of server to trust under TLS.
    ca_cert: str
    # Client certificate to use under TLS.
    client_cert: str
    # Enable/disable RADIUS server identity check
    server_identity_check: Literal["enable", "disable"]
    # Account key processing operation. The FortiGate will keep either the whole domai
    account_key_processing: Literal["same", "strip"]
    # Define subject identity field in certificate for user access right checking.
    account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"]
    # Enable/disable RADIUS based single sign on feature.
    rsso: Literal["enable", "disable"]
    # UDP port to listen on for RADIUS Start and Stop records.
    rsso_radius_server_port: int
    # Enable/disable sending RADIUS response packets after receiving Start and Stop re
    rsso_radius_response: Literal["enable", "disable"]
    # Enable/disable validating the RADIUS request shared secret in the Start or End r
    rsso_validate_request_secret: Literal["enable", "disable"]
    # RADIUS secret used by the RADIUS accounting server.
    rsso_secret: str
    # RADIUS attributes used to extract the user end point identifier from the RADIUS
    rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    # RADIUS attributes used to block a user.
    rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    # RADIUS attribute that contains the profile group name to be extracted from the R
    sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"]
    # Key prefix for SSO group value in the SSO attribute.
    sso_attribute_key: str
    # Enable/disable override old attribute value with new value for the same endpoint
    sso_attribute_value_override: Literal["enable", "disable"]
    # Time in seconds before the logged out user is removed from the "user context lis
    rsso_context_timeout: int
    # Time interval in seconds that group event log messages will be generated for dyn
    rsso_log_period: int
    # Events to log.
    rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"]
    # Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.
    rsso_flush_ip_session: Literal["enable", "disable"]
    # Enable/disable the replacement of old IP addresses with new ones for the same en
    rsso_ep_one_ip_only: Literal["enable", "disable"]
    # Configure delimiter to be used for separating profile group names in the SSO att
    delimiter: Literal["plus", "comma"]
    # Additional accounting servers.
    accounting_server: list[RadiusAccountingserverObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> RadiusPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class Radius:
    """
    Configure RADIUS server entries.
    
    Path: user/radius
    Category: cmdb
    Primary Key: name
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RadiusObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RadiusObject: ...
    
    # List of objects (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> list[RadiusObject]: ...
    
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> RadiusResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> RadiusResponse: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] = ...,
        **kwargs: Any,
    ) -> list[RadiusResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], list[dict[str, Any]]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: str | None = ...,
        **kwargs: Any,
    ) -> RadiusObject | list[RadiusObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RadiusObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RadiusObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> RadiusObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: RadiusPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        secret: str | None = ...,
        secondary_server: str | None = ...,
        secondary_secret: str | None = ...,
        tertiary_server: str | None = ...,
        tertiary_secret: str | None = ...,
        timeout: int | None = ...,
        status_ttl: int | None = ...,
        all_usergroup: Literal["disable", "enable"] | None = ...,
        use_management_vdom: Literal["enable", "disable"] | None = ...,
        switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = ...,
        nas_ip: str | None = ...,
        nas_id_type: Literal["legacy", "custom", "hostname"] | None = ...,
        call_station_id_type: Literal["legacy", "IP", "MAC"] | None = ...,
        nas_id: str | None = ...,
        acct_interim_interval: int | None = ...,
        radius_coa: Literal["enable", "disable"] | None = ...,
        radius_port: int | None = ...,
        h3c_compatibility: Literal["enable", "disable"] | None = ...,
        auth_type: Literal["auto", "ms_chap_v2", "ms_chap", "chap", "pap"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        username_case_sensitive: Literal["enable", "disable"] | None = ...,
        group_override_attr_type: Literal["filter-Id", "class"] | None = ...,
        password_renewal: Literal["enable", "disable"] | None = ...,
        require_message_authenticator: Literal["enable", "disable"] | None = ...,
        password_encoding: Literal["auto", "ISO-8859-1"] | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        acct_all_servers: Literal["enable", "disable"] | None = ...,
        switch_controller_acct_fast_framedip_detect: int | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        switch_controller_service_type: Literal["login", "framed", "callback-login", "callback-framed", "outbound", "administrative", "nas-prompt", "authenticate-only", "callback-nas-prompt", "call-check", "callback-administrative"] | list[str] | None = ...,
        transport_protocol: Literal["udp", "tcp", "tls"] | None = ...,
        tls_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        ca_cert: str | None = ...,
        client_cert: str | None = ...,
        server_identity_check: Literal["enable", "disable"] | None = ...,
        account_key_processing: Literal["same", "strip"] | None = ...,
        account_key_cert_field: Literal["othername", "rfc822name", "dnsname", "cn"] | None = ...,
        rsso: Literal["enable", "disable"] | None = ...,
        rsso_radius_server_port: int | None = ...,
        rsso_radius_response: Literal["enable", "disable"] | None = ...,
        rsso_validate_request_secret: Literal["enable", "disable"] | None = ...,
        rsso_secret: str | None = ...,
        rsso_endpoint_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        rsso_endpoint_block_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute: Literal["User-Name", "NAS-IP-Address", "Framed-IP-Address", "Framed-IP-Netmask", "Filter-Id", "Login-IP-Host", "Reply-Message", "Callback-Number", "Callback-Id", "Framed-Route", "Framed-IPX-Network", "Class", "Called-Station-Id", "Calling-Station-Id", "NAS-Identifier", "Proxy-State", "Login-LAT-Service", "Login-LAT-Node", "Login-LAT-Group", "Framed-AppleTalk-Zone", "Acct-Session-Id", "Acct-Multi-Session-Id"] | None = ...,
        sso_attribute_key: str | None = ...,
        sso_attribute_value_override: Literal["enable", "disable"] | None = ...,
        rsso_context_timeout: int | None = ...,
        rsso_log_period: int | None = ...,
        rsso_log_flags: Literal["protocol-error", "profile-missing", "accounting-stop-missed", "accounting-event", "endpoint-block", "radiusd-other", "none"] | list[str] | None = ...,
        rsso_flush_ip_session: Literal["enable", "disable"] | None = ...,
        rsso_ep_one_ip_only: Literal["enable", "disable"] | None = ...,
        delimiter: Literal["plus", "comma"] | None = ...,
        accounting_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> dict[str, Any]: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> dict[str, Any]: ...
    
    @staticmethod
    def schema() -> dict[str, Any]: ...


__all__ = [
    "Radius",
    "RadiusPayload",
    "RadiusObject",
]