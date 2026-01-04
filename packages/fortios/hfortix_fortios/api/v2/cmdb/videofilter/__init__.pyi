"""Type stubs for VIDEOFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import keyword
    from . import profile
    from . import youtube_key


class Videofilter:
    """Type stub for Videofilter."""

    keyword: keyword.Keyword
    profile: profile.Profile
    youtube_key: youtube_key.YoutubeKey

    def __init__(self, client: IHTTPClient) -> None: ...
