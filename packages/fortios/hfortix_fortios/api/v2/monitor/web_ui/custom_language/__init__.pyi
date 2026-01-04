"""Type stubs for CUSTOM_LANGUAGE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import create
    from . import download
    from . import update


class CustomLanguage:
    """Type stub for CustomLanguage."""

    create: create.Create
    download: download.Download
    update: update.Update

    def __init__(self, client: IHTTPClient) -> None: ...
