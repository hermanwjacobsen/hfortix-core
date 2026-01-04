from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class RadiusPayload(TypedDict, total=False):
    """
    Type hints for user/radius payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
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
    call_station_id_type: NotRequired[Literal["legacy", "IP", "MAC"]]  # Calling & Called station identifier type configuration (defa
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
    tls_min_proto_version: NotRequired[Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]]  # Minimum supported protocol version for TLS connections (defa
    ca_cert: NotRequired[str]  # CA of server to trust under TLS.
    client_cert: NotRequired[str]  # Client certificate to use under TLS.
    server_identity_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable RADIUS server identity check (verify server d
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


class Radius:
    """
    Configure RADIUS server entries.
    
    Path: user/radius
    Category: cmdb
    Primary Key: name
    """
    
    def get(
        self,
        name: str | None = ...,
        filter: str | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> Union[bool, Coroutine[Any, Any, bool]]: ...
    
    def set(
        self,
        payload_dict: RadiusPayload | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
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