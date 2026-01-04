from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union

# Payload TypedDict for IDE autocomplete
class IpsecPhase1Payload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec_phase1 payload fields.
    
    Use this for IDE autocomplete when building payload dicts:
        payload: IpsecPhase1Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: NotRequired[str]  # IPsec remote gateway name.
    type: NotRequired[Literal["static", "dynamic", "ddns"]]  # Remote gateway type.
    interface: str  # Local physical, aggregate, or VLAN outgoing interface.
    ike_version: NotRequired[Literal["1", "2"]]  # IKE protocol version.
    remote_gw: str  # Remote VPN gateway.
    local_gw: NotRequired[str]  # Local VPN gateway.
    remotegw_ddns: str  # Domain name of remote gateway. For example, name.ddns.com.
    keylife: NotRequired[int]  # Time to wait in seconds before phase 1 encryption key expire
    certificate: list[dict[str, Any]]  # Names of up to 4 signed personal certificates.
    authmethod: NotRequired[Literal["psk", "signature"]]  # Authentication method.
    authmethod_remote: NotRequired[Literal["psk", "signature"]]  # Authentication method (remote side).
    mode: NotRequired[Literal["aggressive", "main"]]  # ID protection mode used to establish a secure channel.
    peertype: NotRequired[Literal["any", "one", "dialup", "peer", "peergrp"]]  # Accept this peer type.
    peerid: str  # Accept this peer identity.
    usrgrp: str  # User group name for dialup peers.
    peer: str  # Accept this peer certificate.
    peergrp: str  # Accept this peer certificate group.
    mode_cfg: NotRequired[Literal["disable", "enable"]]  # Enable/disable configuration method.
    mode_cfg_allow_client_selector: NotRequired[Literal["disable", "enable"]]  # Enable/disable mode-cfg client to use custom phase2 selector
    assign_ip: NotRequired[Literal["disable", "enable"]]  # Enable/disable assignment of IP to IPsec interface via confi
    assign_ip_from: NotRequired[Literal["range", "usrgrp", "dhcp", "name"]]  # Method by which the IP address will be assigned.
    ipv4_start_ip: str  # Start of IPv4 range.
    ipv4_end_ip: str  # End of IPv4 range.
    ipv4_netmask: NotRequired[str]  # IPv4 Netmask.
    dhcp_ra_giaddr: NotRequired[str]  # Relay agent gateway IP address to use in the giaddr field of
    dhcp6_ra_linkaddr: NotRequired[str]  # Relay agent IPv6 link address to use in DHCP6 requests.
    dns_mode: NotRequired[Literal["manual", "auto"]]  # DNS server mode.
    ipv4_dns_server1: NotRequired[str]  # IPv4 DNS server 1.
    ipv4_dns_server2: NotRequired[str]  # IPv4 DNS server 2.
    ipv4_dns_server3: NotRequired[str]  # IPv4 DNS server 3.
    internal_domain_list: NotRequired[list[dict[str, Any]]]  # One or more internal domain names in quotes separated by spa
    dns_suffix_search: NotRequired[list[dict[str, Any]]]  # One or more DNS domain name suffixes in quotes separated by 
    ipv4_wins_server1: NotRequired[str]  # WINS server 1.
    ipv4_wins_server2: NotRequired[str]  # WINS server 2.
    ipv4_exclude_range: NotRequired[list[dict[str, Any]]]  # Configuration Method IPv4 exclude ranges.
    ipv4_split_include: NotRequired[str]  # IPv4 split-include subnets.
    split_include_service: NotRequired[str]  # Split-include services.
    ipv4_name: NotRequired[str]  # IPv4 address name.
    ipv6_start_ip: str  # Start of IPv6 range.
    ipv6_end_ip: str  # End of IPv6 range.
    ipv6_prefix: NotRequired[int]  # IPv6 prefix.
    ipv6_dns_server1: NotRequired[str]  # IPv6 DNS server 1.
    ipv6_dns_server2: NotRequired[str]  # IPv6 DNS server 2.
    ipv6_dns_server3: NotRequired[str]  # IPv6 DNS server 3.
    ipv6_exclude_range: NotRequired[list[dict[str, Any]]]  # Configuration method IPv6 exclude ranges.
    ipv6_split_include: NotRequired[str]  # IPv6 split-include subnets.
    ipv6_name: NotRequired[str]  # IPv6 address name.
    ip_delay_interval: NotRequired[int]  # IP address reuse delay interval in seconds (0 - 28800).
    unity_support: NotRequired[Literal["disable", "enable"]]  # Enable/disable support for Cisco UNITY Configuration Method 
    domain: NotRequired[str]  # Instruct unity clients about the single default DNS domain.
    banner: NotRequired[str]  # Message that unity client should display after connecting.
    include_local_lan: NotRequired[Literal["disable", "enable"]]  # Enable/disable allow local LAN access on unity clients.
    ipv4_split_exclude: NotRequired[str]  # IPv4 subnets that should not be sent over the IPsec tunnel.
    ipv6_split_exclude: NotRequired[str]  # IPv6 subnets that should not be sent over the IPsec tunnel.
    save_password: NotRequired[Literal["disable", "enable"]]  # Enable/disable saving XAuth username and password on VPN cli
    client_auto_negotiate: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowing the VPN client to bring up the tunne
    client_keep_alive: NotRequired[Literal["disable", "enable"]]  # Enable/disable allowing the VPN client to keep the tunnel up
    backup_gateway: NotRequired[list[dict[str, Any]]]  # Instruct unity clients about the backup gateway address(es).
    proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]  # Phase1 proposal.
    add_route: NotRequired[Literal["disable", "enable"]]  # Enable/disable control addition of a route to peer destinati
    add_gw_route: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatically add a route to the remote gatew
    psksecret: str  # Pre-shared secret for PSK authentication (ASCII string or he
    psksecret_remote: str  # Pre-shared secret for remote side PSK authentication (ASCII 
    keepalive: NotRequired[int]  # NAT-T keep alive interval.
    distance: NotRequired[int]  # Distance for routes added by IKE (1 - 255).
    priority: NotRequired[int]  # Priority for routes added by IKE (1 - 65535).
    localid: NotRequired[str]  # Local ID.
    localid_type: NotRequired[Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"]]  # Local ID type.
    auto_negotiate: NotRequired[Literal["enable", "disable"]]  # Enable/disable automatic initiation of IKE SA negotiation.
    negotiate_timeout: NotRequired[int]  # IKE SA negotiation timeout in seconds (1 - 300).
    fragmentation: NotRequired[Literal["enable", "disable"]]  # Enable/disable fragment IKE message on re-transmission.
    dpd: NotRequired[Literal["disable", "on-idle", "on-demand"]]  # Dead Peer Detection mode.
    dpd_retrycount: NotRequired[int]  # Number of DPD retry attempts.
    dpd_retryinterval: NotRequired[str]  # DPD retry interval.
    comments: NotRequired[str]  # Comment.
    npu_offload: NotRequired[Literal["enable", "disable"]]  # Enable/disable offloading NPU.
    send_cert_chain: NotRequired[Literal["enable", "disable"]]  # Enable/disable sending certificate chain.
    dhgrp: NotRequired[Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]]  # DH group.
    addke1: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE1 group.
    addke2: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE2 group.
    addke3: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE3 group.
    addke4: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE4 group.
    addke5: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE5 group.
    addke6: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE6 group.
    addke7: NotRequired[Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]]  # ADDKE7 group.
    suite_b: NotRequired[Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"]]  # Use Suite-B.
    eap: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKEv2 EAP authentication.
    eap_identity: NotRequired[Literal["use-id-payload", "send-request"]]  # IKEv2 EAP peer identity type.
    eap_exclude_peergrp: NotRequired[str]  # Peer group excluded from EAP authentication.
    eap_cert_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable peer certificate authentication in addition t
    acct_verify: NotRequired[Literal["enable", "disable"]]  # Enable/disable verification of RADIUS accounting record.
    ppk: NotRequired[Literal["disable", "allow", "require"]]  # Enable/disable IKEv2 Postquantum Preshared Key (PPK).
    ppk_secret: str  # IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal
    ppk_identity: NotRequired[str]  # IKEv2 Postquantum Preshared Key Identity.
    wizard_type: NotRequired[Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"]]  # GUI VPN Wizard Type.
    xauthtype: NotRequired[Literal["disable", "client", "pap", "chap", "auto"]]  # XAuth type.
    reauth: NotRequired[Literal["disable", "enable"]]  # Enable/disable re-authentication upon IKE SA lifetime expira
    authusr: str  # XAuth user name.
    authpasswd: str  # XAuth password (max 35 characters).
    group_authentication: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKEv2 IDi group authentication.
    group_authentication_secret: str  # Password for IKEv2 ID group authentication. ASCII string or 
    authusrgrp: NotRequired[str]  # Authentication user group.
    mesh_selector_type: NotRequired[Literal["disable", "subnet", "host"]]  # Add selectors containing subsets of the configuration depend
    idle_timeout: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPsec tunnel idle timeout.
    shared_idle_timeout: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPsec tunnel shared idle timeout.
    idle_timeoutinterval: NotRequired[int]  # IPsec tunnel idle timeout in minutes (5 - 43200).
    ha_sync_esp_seqno: NotRequired[Literal["enable", "disable"]]  # Enable/disable sequence number jump ahead for IPsec HA.
    fgsp_sync: NotRequired[Literal["enable", "disable"]]  # Enable/disable IPsec syncing of tunnels for FGSP IPsec.
    inbound_dscp_copy: NotRequired[Literal["enable", "disable"]]  # Enable/disable copy the dscp in the ESP header to the inner 
    nattraversal: NotRequired[Literal["enable", "disable", "forced"]]  # Enable/disable NAT traversal.
    esn: NotRequired[Literal["require", "allow", "disable"]]  # Extended sequence number (ESN) negotiation.
    fragmentation_mtu: NotRequired[int]  # IKE fragmentation MTU (500 - 16000).
    childless_ike: NotRequired[Literal["enable", "disable"]]  # Enable/disable childless IKEv2 initiation (RFC 6023).
    azure_ad_autoconnect: NotRequired[Literal["enable", "disable"]]  # Enable/disable Azure AD Auto-Connect for FortiClient.
    client_resume: NotRequired[Literal["enable", "disable"]]  # Enable/disable resumption of offline FortiClient sessions.  
    client_resume_interval: NotRequired[int]  # Maximum time in seconds during which a VPN client may resume
    rekey: NotRequired[Literal["enable", "disable"]]  # Enable/disable phase1 rekey.
    digital_signature_auth: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKEv2 Digital Signature Authentication (RFC 7
    signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"]  # Digital Signature Authentication hash algorithms.
    rsa_signature_format: NotRequired[Literal["pkcs1", "pss"]]  # Digital Signature Authentication RSA signature format.
    rsa_signature_hash_override: NotRequired[Literal["enable", "disable"]]  # Enable/disable IKEv2 RSA signature hash algorithm override.
    enforce_unique_id: NotRequired[Literal["disable", "keep-new", "keep-old"]]  # Enable/disable peer ID uniqueness check.
    cert_id_validation: NotRequired[Literal["enable", "disable"]]  # Enable/disable cross validation of peer ID and the identity 
    fec_egress: NotRequired[Literal["enable", "disable"]]  # Enable/disable Forward Error Correction for egress IPsec tra
    fec_send_timeout: NotRequired[int]  # Timeout in milliseconds before sending Forward Error Correct
    fec_base: NotRequired[int]  # Number of base Forward Error Correction packets (1 - 20).
    fec_codec: NotRequired[Literal["rs", "xor"]]  # Forward Error Correction encoding/decoding algorithm.
    fec_redundant: NotRequired[int]  # Number of redundant Forward Error Correction packets (1 - 5 
    fec_ingress: NotRequired[Literal["enable", "disable"]]  # Enable/disable Forward Error Correction for ingress IPsec tr
    fec_receive_timeout: NotRequired[int]  # Timeout in milliseconds before dropping Forward Error Correc
    fec_health_check: NotRequired[str]  # SD-WAN health check.
    fec_mapping_profile: NotRequired[str]  # Forward Error Correction (FEC) mapping profile.
    network_overlay: NotRequired[Literal["disable", "enable"]]  # Enable/disable network overlays.
    network_id: int  # VPN gateway network ID.
    dev_id_notification: NotRequired[Literal["disable", "enable"]]  # Enable/disable device ID notification.
    dev_id: str  # Device ID carried by the device ID notification.
    loopback_asymroute: NotRequired[Literal["enable", "disable"]]  # Enable/disable asymmetric routing for IKE traffic on loopbac
    link_cost: NotRequired[int]  # VPN tunnel underlay link cost.
    kms: NotRequired[str]  # Key Management Services server.
    exchange_fgt_device_id: NotRequired[Literal["enable", "disable"]]  # Enable/disable device identifier exchange with peer FortiGat
    ipv6_auto_linklocal: NotRequired[Literal["enable", "disable"]]  # Enable/disable auto generation of IPv6 link-local address us
    ems_sn_check: NotRequired[Literal["enable", "disable"]]  # Enable/disable verification of EMS serial number.
    cert_trust_store: NotRequired[Literal["local", "ems"]]  # CA certificate trust store.
    qkd: NotRequired[Literal["disable", "allow", "require"]]  # Enable/disable use of Quantum Key Distribution (QKD) server.
    qkd_hybrid: NotRequired[Literal["disable", "allow", "require"]]  # Enable/disable use of Quantum Key Distribution (QKD) hybrid 
    qkd_profile: NotRequired[str]  # Quantum Key Distribution (QKD) server profile.
    transport: NotRequired[Literal["udp", "auto", "tcp"]]  # Set IKE transport protocol.
    fortinet_esp: NotRequired[Literal["enable", "disable"]]  # Enable/disable Fortinet ESP encapsulaton.
    auto_transport_threshold: NotRequired[int]  # Timeout in seconds before falling back to next transport pro
    remote_gw_match: NotRequired[Literal["any", "ipmask", "iprange", "geography", "ztna"]]  # Set type of IPv4 remote gateway address matching.
    remote_gw_subnet: NotRequired[str]  # IPv4 address and subnet mask.
    remote_gw_start_ip: NotRequired[str]  # First IPv4 address in the range.
    remote_gw_end_ip: NotRequired[str]  # Last IPv4 address in the range.
    remote_gw_country: NotRequired[str]  # IPv4 addresses associated to a specific country.
    remote_gw_ztna_tags: list[dict[str, Any]]  # IPv4 ZTNA posture tags.
    remote_gw6_match: NotRequired[Literal["any", "ipprefix", "iprange", "geography"]]  # Set type of IPv6 remote gateway address matching.
    remote_gw6_subnet: NotRequired[str]  # IPv6 address and prefix.
    remote_gw6_start_ip: NotRequired[str]  # First IPv6 address in the range.
    remote_gw6_end_ip: NotRequired[str]  # Last IPv6 address in the range.
    remote_gw6_country: NotRequired[str]  # IPv6 addresses associated to a specific country.
    cert_peer_username_validation: NotRequired[Literal["none", "othername", "rfc822name", "cn"]]  # Enable/disable cross validation of peer username and the ide
    cert_peer_username_strip: NotRequired[Literal["disable", "enable"]]  # Enable/disable domain stripping on certificate identity.


class IpsecPhase1:
    """
    Configure VPN remote gateway.
    
    Path: vpn/ipsec_phase1
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
        payload_dict: IpsecPhase1Payload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]: ...
    
    def put(
        self,
        payload_dict: IpsecPhase1Payload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        remote_gw: str | None = ...,
        local_gw: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
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
        payload_dict: IpsecPhase1Payload | None = ...,
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