"""Type stubs for ANTIVIRUS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import exempt_list
    from . import profile
    from . import quarantine
    from . import settings


class Antivirus:
    """Type stub for Antivirus."""

    exempt_list: exempt_list.ExemptList
    profile: profile.Profile
    quarantine: quarantine.Quarantine
    settings: settings.Settings

    def __init__(self, client: IHTTPClient) -> None: ...
