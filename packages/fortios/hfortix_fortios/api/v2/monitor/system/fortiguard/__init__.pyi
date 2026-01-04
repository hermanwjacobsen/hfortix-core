"""Type stubs for FORTIGUARD category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import clear_statistics
    from . import manual_update
    from . import test_availability
    from . import update


class Fortiguard:
    """Type stub for Fortiguard."""

    clear_statistics: clear_statistics.ClearStatistics
    manual_update: manual_update.ManualUpdate
    test_availability: test_availability.TestAvailability
    update: update.Update

    def __init__(self, client: IHTTPClient) -> None: ...
