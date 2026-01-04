"""Type stubs for FORTIANALYZER3 category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import filter
    from . import override_filter
    from . import override_setting
    from . import setting


class Fortianalyzer3:
    """Type stub for Fortianalyzer3."""

    filter: filter.Filter
    override_filter: override_filter.OverrideFilter
    override_setting: override_setting.OverrideSetting
    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
