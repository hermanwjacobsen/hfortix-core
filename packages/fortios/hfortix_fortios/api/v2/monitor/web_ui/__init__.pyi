"""Type stubs for WEB_UI category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom_language
    from . import language


class WebUi:
    """Type stub for WebUi."""

    custom_language: custom_language.CustomLanguage
    language: language.Language

    def __init__(self, client: IHTTPClient) -> None: ...
