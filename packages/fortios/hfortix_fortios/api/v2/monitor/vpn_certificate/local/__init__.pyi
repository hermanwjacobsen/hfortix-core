"""Type stubs for LOCAL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import create
    from . import import_setting


class Local:
    """Type stub for Local."""

    create: create.Create
    import_setting: import_setting.ImportSetting

    def __init__(self, client: IHTTPClient) -> None: ...
