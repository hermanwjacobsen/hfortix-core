"""Type stubs for FORTIMANAGER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import backup_action
    from . import backup_details
    from . import backup_summary


class Fortimanager:
    """Type stub for Fortimanager."""

    backup_action: backup_action.BackupAction
    backup_details: backup_details.BackupDetails
    backup_summary: backup_summary.BackupSummary

    def __init__(self, client: IHTTPClient) -> None: ...
