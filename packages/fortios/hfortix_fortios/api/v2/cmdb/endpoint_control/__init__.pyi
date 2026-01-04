"""Type stubs for ENDPOINT_CONTROL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import fctems
    from . import fctems_override
    from . import settings


class EndpointControl:
    """Type stub for EndpointControl."""

    fctems: fctems.Fctems
    fctems_override: fctems_override.FctemsOverride
    settings: settings.Settings

    def __init__(self, client: IHTTPClient) -> None: ...
