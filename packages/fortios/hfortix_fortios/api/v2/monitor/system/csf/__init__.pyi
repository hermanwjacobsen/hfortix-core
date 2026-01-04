"""Type stubs for CSF category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import register_appliance


class Csf:
    """Type stub for Csf."""

    register_appliance: register_appliance.RegisterAppliance

    def __init__(self, client: IHTTPClient) -> None: ...
