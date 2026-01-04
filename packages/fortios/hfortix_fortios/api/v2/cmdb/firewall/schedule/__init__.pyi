"""Type stubs for SCHEDULE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import group
    from . import onetime
    from . import recurring


class Schedule:
    """Type stub for Schedule."""

    group: group.Group
    onetime: onetime.Onetime
    recurring: recurring.Recurring

    def __init__(self, client: IHTTPClient) -> None: ...
