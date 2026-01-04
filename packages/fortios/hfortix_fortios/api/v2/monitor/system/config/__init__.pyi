"""Type stubs for CONFIG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import backup
    from . import restore
    from . import restore_status


class Config:
    """Type stub for Config."""

    backup: backup.Backup
    restore: restore.Restore
    restore_status: restore_status.RestoreStatus

    def __init__(self, client: IHTTPClient) -> None: ...
