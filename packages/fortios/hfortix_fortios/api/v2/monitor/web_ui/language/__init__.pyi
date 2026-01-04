"""Type stubs for LANGUAGE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import import_setting


class Language:
    """Type stub for Language."""

    import_setting: import_setting.ImportSetting

    def __init__(self, client: IHTTPClient) -> None: ...
