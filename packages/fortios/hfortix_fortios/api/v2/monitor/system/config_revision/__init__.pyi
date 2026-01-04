"""Type stubs for CONFIG_REVISION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import delete
    from . import file
    from . import info
    from . import save
    from . import update_comments


class ConfigRevision:
    """Type stub for ConfigRevision."""

    delete: delete.Delete
    file: file.File
    info: info.Info
    save: save.Save
    update_comments: update_comments.UpdateComments

    def __init__(self, client: IHTTPClient) -> None: ...
