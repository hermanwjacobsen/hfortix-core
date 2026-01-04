"""Type stubs for EXTENSION_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import dataplan
    from . import extender
    from . import extender_profile
    from . import extender_vap
    from . import fortigate
    from . import fortigate_profile


class ExtensionController:
    """Type stub for ExtensionController."""

    dataplan: dataplan.Dataplan
    extender: extender.Extender
    extender_profile: extender_profile.ExtenderProfile
    extender_vap: extender_vap.ExtenderVap
    fortigate: fortigate.Fortigate
    fortigate_profile: fortigate_profile.FortigateProfile

    def __init__(self, client: IHTTPClient) -> None: ...
