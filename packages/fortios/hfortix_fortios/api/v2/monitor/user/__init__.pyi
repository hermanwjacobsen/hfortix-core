"""Type stubs for USER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .collected_email import CollectedEmail, CollectedEmailDictMode, CollectedEmailObjectMode
    from .banned import Banned
    from .device import Device, DeviceDictMode, DeviceObjectMode
    from .firewall import Firewall
    from .fortitoken import Fortitoken
    from .fortitoken_cloud import FortitokenCloud, FortitokenCloudDictMode, FortitokenCloudObjectMode
    from .fsso import Fsso
    from .guest import Guest, GuestDictMode, GuestObjectMode
    from .info import Info, InfoDictMode, InfoObjectMode
    from .local import Local, LocalDictMode, LocalObjectMode
    from .password_policy_conform import PasswordPolicyConform, PasswordPolicyConformDictMode, PasswordPolicyConformObjectMode
    from .proxy import Proxy
    from .query import Query, QueryDictMode, QueryObjectMode
    from .radius import Radius, RadiusDictMode, RadiusObjectMode
    from .scim import Scim, ScimDictMode, ScimObjectMode
    from .tacacs_plus import TacacsPlus, TacacsPlusDictMode, TacacsPlusObjectMode

__all__ = [
    "CollectedEmail",
    "UserDictMode",
    "UserObjectMode",
]

class UserDictMode:
    """USER API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    banned: Banned
    device: DeviceDictMode
    firewall: Firewall
    fortitoken: Fortitoken
    fortitoken_cloud: FortitokenCloudDictMode
    fsso: Fsso
    guest: GuestDictMode
    info: InfoDictMode
    local: LocalDictMode
    password_policy_conform: PasswordPolicyConformDictMode
    proxy: Proxy
    query: QueryDictMode
    radius: RadiusDictMode
    scim: ScimDictMode
    tacacs_plus: TacacsPlusDictMode
    collected_email: CollectedEmailDictMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize user category with HTTP client."""
        ...


class UserObjectMode:
    """USER API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    banned: Banned
    device: DeviceObjectMode
    firewall: Firewall
    fortitoken: Fortitoken
    fortitoken_cloud: FortitokenCloudObjectMode
    fsso: Fsso
    guest: GuestObjectMode
    info: InfoObjectMode
    local: LocalObjectMode
    password_policy_conform: PasswordPolicyConformObjectMode
    proxy: Proxy
    query: QueryObjectMode
    radius: RadiusObjectMode
    scim: ScimObjectMode
    tacacs_plus: TacacsPlusObjectMode
    collected_email: CollectedEmailObjectMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize user category with HTTP client."""
        ...


# Base class for backwards compatibility
class User:
    """USER API category."""
    
    banned: Banned
    device: Device
    firewall: Firewall
    fortitoken: Fortitoken
    fortitoken_cloud: FortitokenCloud
    fsso: Fsso
    guest: Guest
    info: Info
    local: Local
    password_policy_conform: PasswordPolicyConform
    proxy: Proxy
    query: Query
    radius: Radius
    scim: Scim
    tacacs_plus: TacacsPlus
    collected_email: CollectedEmail

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize user category with HTTP client."""
        ...
