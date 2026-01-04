"""Type stubs for CONFIG_SCRIPT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import delete
    from . import run
    from . import upload


class ConfigScript:
    """Type stub for ConfigScript."""

    delete: delete.Delete
    run: run.Run
    upload: upload.Upload

    def __init__(self, client: IHTTPClient) -> None: ...
