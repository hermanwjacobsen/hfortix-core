"""Type stubs for CSF category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .pending_authorizations import PendingAuthorizations
    from .register_appliance import RegisterAppliance


class Csf:
    """Type stub for Csf."""

    pending_authorizations: PendingAuthorizations
    register_appliance: RegisterAppliance

    def __init__(self, client: IHTTPClient) -> None: ...
