"""Type stubs for FORTIGUARD category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import answers
    from . import redirect_portal
    from . import service_communication_stats


class Fortiguard:
    """Type stub for Fortiguard."""

    answers: answers.Answers
    redirect_portal: redirect_portal.RedirectPortal
    service_communication_stats: service_communication_stats.ServiceCommunicationStats

    def __init__(self, client: IHTTPClient) -> None: ...
