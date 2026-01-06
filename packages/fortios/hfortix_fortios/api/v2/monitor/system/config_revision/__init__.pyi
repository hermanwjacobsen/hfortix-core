"""Type stubs for CONFIG_REVISION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .delete import Delete
    from .file import File
    from .info import Info
    from .save import Save
    from .update_comments import UpdateComments


class ConfigRevision:
    """Type stub for ConfigRevision."""

    delete: Delete
    file: File
    info: Info
    save: Save
    update_comments: UpdateComments

    def __init__(self, client: IHTTPClient) -> None: ...
