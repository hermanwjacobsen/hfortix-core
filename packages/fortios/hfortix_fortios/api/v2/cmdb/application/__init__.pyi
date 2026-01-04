"""Type stubs for APPLICATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom
    from . import group
    from . import list
    from . import name
    from . import rule_settings


class Application:
    """Type stub for Application."""

    custom: custom.Custom
    group: group.Group
    list: list.List
    name: name.Name
    rule_settings: rule_settings.RuleSettings

    def __init__(self, client: IHTTPClient) -> None: ...
