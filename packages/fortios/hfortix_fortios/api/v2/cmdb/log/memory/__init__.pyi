"""Type stubs for MEMORY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import filter
    from . import global_setting
    from . import setting


class Memory:
    """Type stub for Memory."""

    filter: filter.Filter
    global_setting: global_setting.GlobalSetting
    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
