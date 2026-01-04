"""Type stubs for INFO category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import query
    from . import thumbnail
    from . import thumbnail_file


class Info:
    """Type stub for Info."""

    query: query.Query
    thumbnail: thumbnail.Thumbnail
    thumbnail_file: thumbnail_file.ThumbnailFile

    def __init__(self, client: IHTTPClient) -> None: ...
