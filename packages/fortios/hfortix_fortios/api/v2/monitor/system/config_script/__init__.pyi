"""Type stubs for CONFIG_SCRIPT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .delete import Delete
    from .run import Run
    from .upload import Upload


class ConfigScript:
    """Type stub for ConfigScript."""

    delete: Delete
    run: Run
    upload: Upload

    def __init__(self, client: IHTTPClient) -> None: ...
