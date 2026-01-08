from typing import TypedDict, Literal, NotRequired, Any, Coroutine, Union, overload, Generator, final
from hfortix_fortios.models import FortiObject

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional)
class SecurityPolicyPayload(TypedDict, total=False):
    """
    Type hints for firewall/security_policy payload fields.
    
    Configure NGFW IPv4/IPv6 application policies.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: av-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.casb.profile.ProfileEndpoint` (via: casb-profile)
        - :class:`~.diameter-filter.profile.ProfileEndpoint` (via: diameter-filter-profile)
        - :class:`~.dlp.profile.ProfileEndpoint` (via: dlp-profile)
        - :class:`~.dnsfilter.profile.ProfileEndpoint` (via: dnsfilter-profile)
        - :class:`~.emailfilter.profile.ProfileEndpoint` (via: emailfilter-profile)
        - :class:`~.file-filter.profile.ProfileEndpoint` (via: file-filter-profile)
        - :class:`~.firewall.profile-group.ProfileGroupEndpoint` (via: profile-group)
        - :class:`~.firewall.profile-protocol-options.ProfileProtocolOptionsEndpoint` (via: profile-protocol-options)
        - ... and 12 more dependencies

    **Usage:**
        payload: SecurityPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    uuid: NotRequired[str]  # Universally Unique Identifier
    policyid: NotRequired[int]  # Policy ID.
    name: NotRequired[str]  # Policy name.
    comments: NotRequired[str]  # Comment.
    srcintf: list[dict[str, Any]]  # Incoming (ingress) interface.
    dstintf: list[dict[str, Any]]  # Outgoing (egress) interface.
    srcaddr: NotRequired[list[dict[str, Any]]]  # Source IPv4 address name and address group names.
    srcaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr specifies what the source address must
    dstaddr: NotRequired[list[dict[str, Any]]]  # Destination IPv4 address name and address group names.
    dstaddr_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr specifies what the destination address
    srcaddr6: NotRequired[list[dict[str, Any]]]  # Source IPv6 address name and address group names.
    srcaddr6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled srcaddr6 specifies what the source address must
    dstaddr6: NotRequired[list[dict[str, Any]]]  # Destination IPv6 address name and address group names.
    dstaddr6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled dstaddr6 specifies what the destination address
    internet_service: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services for this policy. If
    internet_service_name: NotRequired[list[dict[str, Any]]]  # Internet Service name.
    internet_service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service specifies what the service mus
    internet_service_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service name.
    internet_service_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service group name.
    internet_service_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service name.
    internet_service_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of Internet Services in source for this p
    internet_service_src_name: NotRequired[list[dict[str, Any]]]  # Internet Service source name.
    internet_service_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service-src specifies what the service
    internet_service_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service source group name.
    internet_service_src_custom: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source name.
    internet_service_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service source group name.
    internet_service_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard Internet Service source name.
    internet_service6: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services for this policy
    internet_service6_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service name.
    internet_service6_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6 specifies what the service mu
    internet_service6_group: NotRequired[list[dict[str, Any]]]  # Internet Service group name.
    internet_service6_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service name.
    internet_service6_custom_group: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service group name.
    internet_service6_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard IPv6 Internet Service name.
    internet_service6_src: NotRequired[Literal["enable", "disable"]]  # Enable/disable use of IPv6 Internet Services in source for t
    internet_service6_src_name: NotRequired[list[dict[str, Any]]]  # IPv6 Internet Service source name.
    internet_service6_src_negate: NotRequired[Literal["enable", "disable"]]  # When enabled internet-service6-src specifies what the servic
    internet_service6_src_group: NotRequired[list[dict[str, Any]]]  # Internet Service6 source group name.
    internet_service6_src_custom: NotRequired[list[dict[str, Any]]]  # Custom IPv6 Internet Service source name.
    internet_service6_src_custom_group: NotRequired[list[dict[str, Any]]]  # Custom Internet Service6 source group name.
    internet_service6_src_fortiguard: NotRequired[list[dict[str, Any]]]  # FortiGuard IPv6 Internet Service source name.
    enforce_default_app_port: NotRequired[Literal["enable", "disable"]]  # Enable/disable default application port enforcement for allo
    service: NotRequired[list[dict[str, Any]]]  # Service and service group names.
    service_negate: NotRequired[Literal["enable", "disable"]]  # When enabled service specifies what the service must NOT be.
    action: NotRequired[Literal["accept", "deny"]]  # Policy action (accept/deny).
    send_deny_packet: NotRequired[Literal["disable", "enable"]]  # Enable to send a reply when a session is denied or blocked b
    schedule: str  # Schedule name.
    status: NotRequired[Literal["enable", "disable"]]  # Enable or disable this policy.
    logtraffic: NotRequired[Literal["all", "utm", "disable"]]  # Enable or disable logging. Log all sessions or security prof
    learning_mode: NotRequired[Literal["enable", "disable"]]  # Enable to allow everything, but log all of the meaningful da
    nat46: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT46.
    nat64: NotRequired[Literal["enable", "disable"]]  # Enable/disable NAT64.
    profile_type: NotRequired[Literal["single", "group"]]  # Determine whether the firewall policy allows security profil
    profile_group: NotRequired[str]  # Name of profile group.
    profile_protocol_options: NotRequired[str]  # Name of an existing Protocol options profile.
    ssl_ssh_profile: NotRequired[str]  # Name of an existing SSL SSH profile.
    av_profile: NotRequired[str]  # Name of an existing Antivirus profile.
    webfilter_profile: NotRequired[str]  # Name of an existing Web filter profile.
    dnsfilter_profile: NotRequired[str]  # Name of an existing DNS filter profile.
    emailfilter_profile: NotRequired[str]  # Name of an existing email filter profile.
    dlp_profile: NotRequired[str]  # Name of an existing DLP profile.
    file_filter_profile: NotRequired[str]  # Name of an existing file-filter profile.
    ips_sensor: NotRequired[str]  # Name of an existing IPS sensor.
    application_list: NotRequired[str]  # Name of an existing Application list.
    voip_profile: NotRequired[str]  # Name of an existing VoIP (voipd) profile.
    ips_voip_filter: NotRequired[str]  # Name of an existing VoIP (ips) profile.
    sctp_filter_profile: NotRequired[str]  # Name of an existing SCTP filter profile.
    diameter_filter_profile: NotRequired[str]  # Name of an existing Diameter filter profile.
    virtual_patch_profile: NotRequired[str]  # Name of an existing virtual-patch profile.
    icap_profile: NotRequired[str]  # Name of an existing ICAP profile.
    videofilter_profile: NotRequired[str]  # Name of an existing VideoFilter profile.
    ssh_filter_profile: NotRequired[str]  # Name of an existing SSH filter profile.
    casb_profile: NotRequired[str]  # Name of an existing CASB profile.
    application: NotRequired[list[dict[str, Any]]]  # Application ID list.
    app_category: NotRequired[list[dict[str, Any]]]  # Application category ID list.
    url_category: NotRequired[list[dict[str, Any]]]  # URL categories or groups.
    app_group: NotRequired[list[dict[str, Any]]]  # Application group names.
    groups: NotRequired[list[dict[str, Any]]]  # Names of user groups that can authenticate with this policy.
    users: NotRequired[list[dict[str, Any]]]  # Names of individual users that can authenticate with this po
    fsso_groups: NotRequired[list[dict[str, Any]]]  # Names of FSSO groups.

# Nested classes for table field children

@final
class SecurityPolicySrcintfObject:
    """Typed object for srcintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
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
class SecurityPolicyDstintfObject:
    """Typed object for dstintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name.
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
class SecurityPolicySrcaddrObject:
    """Typed object for srcaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class SecurityPolicyDstaddrObject:
    """Typed object for dstaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class SecurityPolicySrcaddr6Object:
    """Typed object for srcaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class SecurityPolicyDstaddr6Object:
    """Typed object for dstaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name.
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
class SecurityPolicyInternetservicenameObject:
    """Typed object for internet-service-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name.
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
class SecurityPolicyInternetservicegroupObject:
    """Typed object for internet-service-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name.
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
class SecurityPolicyInternetservicecustomObject:
    """Typed object for internet-service-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name.
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
class SecurityPolicyInternetservicecustomgroupObject:
    """Typed object for internet-service-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service group name.
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
class SecurityPolicyInternetservicefortiguardObject:
    """Typed object for internet-service-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name.
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
class SecurityPolicyInternetservicesrcnameObject:
    """Typed object for internet-service-src-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name.
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
class SecurityPolicyInternetservicesrcgroupObject:
    """Typed object for internet-service-src-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name.
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
class SecurityPolicyInternetservicesrccustomObject:
    """Typed object for internet-service-src-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name.
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
class SecurityPolicyInternetservicesrccustomgroupObject:
    """Typed object for internet-service-src-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service group name.
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
class SecurityPolicyInternetservicesrcfortiguardObject:
    """Typed object for internet-service-src-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name.
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
class SecurityPolicyInternetservice6nameObject:
    """Typed object for internet-service6-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 Internet Service name.
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
class SecurityPolicyInternetservice6groupObject:
    """Typed object for internet-service6-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name.
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
class SecurityPolicyInternetservice6customObject:
    """Typed object for internet-service6-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom IPv6 Internet Service name.
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
class SecurityPolicyInternetservice6customgroupObject:
    """Typed object for internet-service6-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom IPv6 Internet Service group name.
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
class SecurityPolicyInternetservice6fortiguardObject:
    """Typed object for internet-service6-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name.
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
class SecurityPolicyInternetservice6srcnameObject:
    """Typed object for internet-service6-src-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service name.
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
class SecurityPolicyInternetservice6srcgroupObject:
    """Typed object for internet-service6-src-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service group name.
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
class SecurityPolicyInternetservice6srccustomObject:
    """Typed object for internet-service6-src-custom table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service name.
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
class SecurityPolicyInternetservice6srccustomgroupObject:
    """Typed object for internet-service6-src-custom-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom Internet Service6 group name.
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
class SecurityPolicyInternetservice6srcfortiguardObject:
    """Typed object for internet-service6-src-fortiguard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard Internet Service name.
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
class SecurityPolicyServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Service name.
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
class SecurityPolicyApplicationObject:
    """Typed object for application table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Application IDs.
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SecurityPolicyAppcategoryObject:
    """Typed object for app-category table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Category IDs.
    id: int
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


@final
class SecurityPolicyAppgroupObject:
    """Typed object for app-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Application group names.
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
class SecurityPolicyGroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User group name.
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
class SecurityPolicyUsersObject:
    """Typed object for users table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User name.
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
class SecurityPolicyFssogroupsObject:
    """Typed object for fsso-groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Names of FSSO groups.
    name: str
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> dict[str, Any]: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class SecurityPolicyResponse(TypedDict):
    """
    Type hints for firewall/security_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    uuid: str
    policyid: int
    name: str
    comments: str
    srcintf: list[dict[str, Any]]
    dstintf: list[dict[str, Any]]
    srcaddr: list[dict[str, Any]]
    srcaddr_negate: Literal["enable", "disable"]
    dstaddr: list[dict[str, Any]]
    dstaddr_negate: Literal["enable", "disable"]
    srcaddr6: list[dict[str, Any]]
    srcaddr6_negate: Literal["enable", "disable"]
    dstaddr6: list[dict[str, Any]]
    dstaddr6_negate: Literal["enable", "disable"]
    internet_service: Literal["enable", "disable"]
    internet_service_name: list[dict[str, Any]]
    internet_service_negate: Literal["enable", "disable"]
    internet_service_group: list[dict[str, Any]]
    internet_service_custom: list[dict[str, Any]]
    internet_service_custom_group: list[dict[str, Any]]
    internet_service_fortiguard: list[dict[str, Any]]
    internet_service_src: Literal["enable", "disable"]
    internet_service_src_name: list[dict[str, Any]]
    internet_service_src_negate: Literal["enable", "disable"]
    internet_service_src_group: list[dict[str, Any]]
    internet_service_src_custom: list[dict[str, Any]]
    internet_service_src_custom_group: list[dict[str, Any]]
    internet_service_src_fortiguard: list[dict[str, Any]]
    internet_service6: Literal["enable", "disable"]
    internet_service6_name: list[dict[str, Any]]
    internet_service6_negate: Literal["enable", "disable"]
    internet_service6_group: list[dict[str, Any]]
    internet_service6_custom: list[dict[str, Any]]
    internet_service6_custom_group: list[dict[str, Any]]
    internet_service6_fortiguard: list[dict[str, Any]]
    internet_service6_src: Literal["enable", "disable"]
    internet_service6_src_name: list[dict[str, Any]]
    internet_service6_src_negate: Literal["enable", "disable"]
    internet_service6_src_group: list[dict[str, Any]]
    internet_service6_src_custom: list[dict[str, Any]]
    internet_service6_src_custom_group: list[dict[str, Any]]
    internet_service6_src_fortiguard: list[dict[str, Any]]
    enforce_default_app_port: Literal["enable", "disable"]
    service: list[dict[str, Any]]
    service_negate: Literal["enable", "disable"]
    action: Literal["accept", "deny"]
    send_deny_packet: Literal["disable", "enable"]
    schedule: str
    status: Literal["enable", "disable"]
    logtraffic: Literal["all", "utm", "disable"]
    learning_mode: Literal["enable", "disable"]
    nat46: Literal["enable", "disable"]
    nat64: Literal["enable", "disable"]
    profile_type: Literal["single", "group"]
    profile_group: str
    profile_protocol_options: str
    ssl_ssh_profile: str
    av_profile: str
    webfilter_profile: str
    dnsfilter_profile: str
    emailfilter_profile: str
    dlp_profile: str
    file_filter_profile: str
    ips_sensor: str
    application_list: str
    voip_profile: str
    ips_voip_filter: str
    sctp_filter_profile: str
    diameter_filter_profile: str
    virtual_patch_profile: str
    icap_profile: str
    videofilter_profile: str
    ssh_filter_profile: str
    casb_profile: str
    application: list[dict[str, Any]]
    app_category: list[dict[str, Any]]
    url_category: list[dict[str, Any]]
    app_group: list[dict[str, Any]]
    groups: list[dict[str, Any]]
    users: list[dict[str, Any]]
    fsso_groups: list[dict[str, Any]]


@final
class SecurityPolicyObject:
    """Typed FortiObject for firewall/security_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Universally Unique Identifier
    uuid: str
    # Policy ID.
    policyid: int
    # Policy name.
    name: str
    # Comment.
    comments: str
    # Incoming (ingress) interface.
    srcintf: list[SecurityPolicySrcintfObject]  # Table field - list of typed objects
    # Outgoing (egress) interface.
    dstintf: list[SecurityPolicyDstintfObject]  # Table field - list of typed objects
    # Source IPv4 address name and address group names.
    srcaddr: list[SecurityPolicySrcaddrObject]  # Table field - list of typed objects
    # When enabled srcaddr specifies what the source address must NOT be.
    srcaddr_negate: Literal["enable", "disable"]
    # Destination IPv4 address name and address group names.
    dstaddr: list[SecurityPolicyDstaddrObject]  # Table field - list of typed objects
    # When enabled dstaddr specifies what the destination address must NOT be.
    dstaddr_negate: Literal["enable", "disable"]
    # Source IPv6 address name and address group names.
    srcaddr6: list[SecurityPolicySrcaddr6Object]  # Table field - list of typed objects
    # When enabled srcaddr6 specifies what the source address must NOT be.
    srcaddr6_negate: Literal["enable", "disable"]
    # Destination IPv6 address name and address group names.
    dstaddr6: list[SecurityPolicyDstaddr6Object]  # Table field - list of typed objects
    # When enabled dstaddr6 specifies what the destination address must NOT be.
    dstaddr6_negate: Literal["enable", "disable"]
    # Enable/disable use of Internet Services for this policy. If enabled, destination
    internet_service: Literal["enable", "disable"]
    # Internet Service name.
    internet_service_name: list[SecurityPolicyInternetservicenameObject]  # Table field - list of typed objects
    # When enabled internet-service specifies what the service must NOT be.
    internet_service_negate: Literal["enable", "disable"]
    # Internet Service group name.
    internet_service_group: list[SecurityPolicyInternetservicegroupObject]  # Table field - list of typed objects
    # Custom Internet Service name.
    internet_service_custom: list[SecurityPolicyInternetservicecustomObject]  # Table field - list of typed objects
    # Custom Internet Service group name.
    internet_service_custom_group: list[SecurityPolicyInternetservicecustomgroupObject]  # Table field - list of typed objects
    # FortiGuard Internet Service name.
    internet_service_fortiguard: list[SecurityPolicyInternetservicefortiguardObject]  # Table field - list of typed objects
    # Enable/disable use of Internet Services in source for this policy. If enabled, s
    internet_service_src: Literal["enable", "disable"]
    # Internet Service source name.
    internet_service_src_name: list[SecurityPolicyInternetservicesrcnameObject]  # Table field - list of typed objects
    # When enabled internet-service-src specifies what the service must NOT be.
    internet_service_src_negate: Literal["enable", "disable"]
    # Internet Service source group name.
    internet_service_src_group: list[SecurityPolicyInternetservicesrcgroupObject]  # Table field - list of typed objects
    # Custom Internet Service source name.
    internet_service_src_custom: list[SecurityPolicyInternetservicesrccustomObject]  # Table field - list of typed objects
    # Custom Internet Service source group name.
    internet_service_src_custom_group: list[SecurityPolicyInternetservicesrccustomgroupObject]  # Table field - list of typed objects
    # FortiGuard Internet Service source name.
    internet_service_src_fortiguard: list[SecurityPolicyInternetservicesrcfortiguardObject]  # Table field - list of typed objects
    # Enable/disable use of IPv6 Internet Services for this policy. If enabled, destin
    internet_service6: Literal["enable", "disable"]
    # IPv6 Internet Service name.
    internet_service6_name: list[SecurityPolicyInternetservice6nameObject]  # Table field - list of typed objects
    # When enabled internet-service6 specifies what the service must NOT be.
    internet_service6_negate: Literal["enable", "disable"]
    # Internet Service group name.
    internet_service6_group: list[SecurityPolicyInternetservice6groupObject]  # Table field - list of typed objects
    # Custom IPv6 Internet Service name.
    internet_service6_custom: list[SecurityPolicyInternetservice6customObject]  # Table field - list of typed objects
    # Custom IPv6 Internet Service group name.
    internet_service6_custom_group: list[SecurityPolicyInternetservice6customgroupObject]  # Table field - list of typed objects
    # FortiGuard IPv6 Internet Service name.
    internet_service6_fortiguard: list[SecurityPolicyInternetservice6fortiguardObject]  # Table field - list of typed objects
    # Enable/disable use of IPv6 Internet Services in source for this policy. If enabl
    internet_service6_src: Literal["enable", "disable"]
    # IPv6 Internet Service source name.
    internet_service6_src_name: list[SecurityPolicyInternetservice6srcnameObject]  # Table field - list of typed objects
    # When enabled internet-service6-src specifies what the service must NOT be.
    internet_service6_src_negate: Literal["enable", "disable"]
    # Internet Service6 source group name.
    internet_service6_src_group: list[SecurityPolicyInternetservice6srcgroupObject]  # Table field - list of typed objects
    # Custom IPv6 Internet Service source name.
    internet_service6_src_custom: list[SecurityPolicyInternetservice6srccustomObject]  # Table field - list of typed objects
    # Custom Internet Service6 source group name.
    internet_service6_src_custom_group: list[SecurityPolicyInternetservice6srccustomgroupObject]  # Table field - list of typed objects
    # FortiGuard IPv6 Internet Service source name.
    internet_service6_src_fortiguard: list[SecurityPolicyInternetservice6srcfortiguardObject]  # Table field - list of typed objects
    # Enable/disable default application port enforcement for allowed applications.
    enforce_default_app_port: Literal["enable", "disable"]
    # Service and service group names.
    service: list[SecurityPolicyServiceObject]  # Table field - list of typed objects
    # When enabled service specifies what the service must NOT be.
    service_negate: Literal["enable", "disable"]
    # Policy action (accept/deny).
    action: Literal["accept", "deny"]
    # Enable to send a reply when a session is denied or blocked by a firewall policy.
    send_deny_packet: Literal["disable", "enable"]
    # Schedule name.
    schedule: str
    # Enable or disable this policy.
    status: Literal["enable", "disable"]
    # Enable or disable logging. Log all sessions or security profile sessions.
    logtraffic: Literal["all", "utm", "disable"]
    # Enable to allow everything, but log all of the meaningful data for security info
    learning_mode: Literal["enable", "disable"]
    # Enable/disable NAT46.
    nat46: Literal["enable", "disable"]
    # Enable/disable NAT64.
    nat64: Literal["enable", "disable"]
    # Determine whether the firewall policy allows security profile groups or single p
    profile_type: Literal["single", "group"]
    # Name of profile group.
    profile_group: str
    # Name of an existing Protocol options profile.
    profile_protocol_options: str
    # Name of an existing SSL SSH profile.
    ssl_ssh_profile: str
    # Name of an existing Antivirus profile.
    av_profile: str
    # Name of an existing Web filter profile.
    webfilter_profile: str
    # Name of an existing DNS filter profile.
    dnsfilter_profile: str
    # Name of an existing email filter profile.
    emailfilter_profile: str
    # Name of an existing DLP profile.
    dlp_profile: str
    # Name of an existing file-filter profile.
    file_filter_profile: str
    # Name of an existing IPS sensor.
    ips_sensor: str
    # Name of an existing Application list.
    application_list: str
    # Name of an existing VoIP (voipd) profile.
    voip_profile: str
    # Name of an existing VoIP (ips) profile.
    ips_voip_filter: str
    # Name of an existing SCTP filter profile.
    sctp_filter_profile: str
    # Name of an existing Diameter filter profile.
    diameter_filter_profile: str
    # Name of an existing virtual-patch profile.
    virtual_patch_profile: str
    # Name of an existing ICAP profile.
    icap_profile: str
    # Name of an existing VideoFilter profile.
    videofilter_profile: str
    # Name of an existing SSH filter profile.
    ssh_filter_profile: str
    # Name of an existing CASB profile.
    casb_profile: str
    # Application ID list.
    application: list[SecurityPolicyApplicationObject]  # Table field - list of typed objects
    # Application category ID list.
    app_category: list[SecurityPolicyAppcategoryObject]  # Table field - list of typed objects
    # URL categories or groups.
    url_category: list[dict[str, Any]]  # Multi-value field
    # Application group names.
    app_group: list[SecurityPolicyAppgroupObject]  # Table field - list of typed objects
    # Names of user groups that can authenticate with this policy.
    groups: list[SecurityPolicyGroupsObject]  # Table field - list of typed objects
    # Names of individual users that can authenticate with this policy.
    users: list[SecurityPolicyUsersObject]  # Table field - list of typed objects
    # Names of FSSO groups.
    fsso_groups: list[SecurityPolicyFssogroupsObject]  # Table field - list of typed objects
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SecurityPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...


class SecurityPolicy:
    """
    Configure NGFW IPv4/IPv6 application policies.
    
    Path: firewall/security_policy
    Category: cmdb
    Primary Key: policyid
    """
    
    # Overloads for get() with response_mode="object" - MOST SPECIFIC FIRST
    # Single object (mkey/name provided as positional arg)
    @overload
    def get(
        self,
        policyid: int,
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
    ) -> SecurityPolicyObject: ...
    
    # Single object (mkey/name provided as keyword arg)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> SecurityPolicyObject: ...
    
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
    ) -> list[SecurityPolicyObject]: ...
    
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int,
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
    ) -> SecurityPolicyResponse: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        policyid: int,
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
    ) -> SecurityPolicyResponse: ...
    
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
    ) -> list[SecurityPolicyResponse]: ...
    
    # Default overload for dict mode
    @overload
    def get(
        self,
        policyid: int | None = ...,
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
        policyid: int | None = ...,
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
    ) -> SecurityPolicyObject | list[SecurityPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> dict[str, Any]: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SecurityPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SecurityPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        response_mode: Literal["dict", "object"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["object"] = ...,
        **kwargs: Any,
    ) -> SecurityPolicyObject: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        response_mode: Literal["dict"] | None = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    @overload
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        policyid: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    
    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SecurityPolicyPayload | None = ...,
        uuid: str | None = ...,
        policyid: int | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        dstintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr_negate: Literal["enable", "disable"] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr_negate: Literal["enable", "disable"] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6_negate: Literal["enable", "disable"] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6_negate: Literal["enable", "disable"] | None = ...,
        internet_service: Literal["enable", "disable"] | None = ...,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_negate: Literal["enable", "disable"] | None = ...,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src: Literal["enable", "disable"] | None = ...,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6: Literal["enable", "disable"] | None = ...,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src: Literal["enable", "disable"] | None = ...,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_negate: Literal["enable", "disable"] | None = ...,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = ...,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = ...,
        enforce_default_app_port: Literal["enable", "disable"] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        service_negate: Literal["enable", "disable"] | None = ...,
        action: Literal["accept", "deny"] | None = ...,
        send_deny_packet: Literal["disable", "enable"] | None = ...,
        schedule: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        logtraffic: Literal["all", "utm", "disable"] | None = ...,
        learning_mode: Literal["enable", "disable"] | None = ...,
        nat46: Literal["enable", "disable"] | None = ...,
        nat64: Literal["enable", "disable"] | None = ...,
        profile_type: Literal["single", "group"] | None = ...,
        profile_group: str | None = ...,
        profile_protocol_options: str | None = ...,
        ssl_ssh_profile: str | None = ...,
        av_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        dnsfilter_profile: str | None = ...,
        emailfilter_profile: str | None = ...,
        dlp_profile: str | None = ...,
        file_filter_profile: str | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        voip_profile: str | None = ...,
        ips_voip_filter: str | None = ...,
        sctp_filter_profile: str | None = ...,
        diameter_filter_profile: str | None = ...,
        virtual_patch_profile: str | None = ...,
        icap_profile: str | None = ...,
        videofilter_profile: str | None = ...,
        ssh_filter_profile: str | None = ...,
        casb_profile: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        url_category: str | list[str] | None = ...,
        app_group: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "SecurityPolicy",
    "SecurityPolicyPayload",
    "SecurityPolicyObject",
]