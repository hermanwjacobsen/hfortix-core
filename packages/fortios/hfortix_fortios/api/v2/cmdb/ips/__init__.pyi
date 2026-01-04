"""Type stubs for IPS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom
    from . import decoder
    from . import global_setting
    from . import rule
    from . import rule_settings
    from . import sensor
    from . import settings
    from . import view_map


class Ips:
    """Type stub for Ips."""

    custom: custom.Custom
    decoder: decoder.Decoder
    global_setting: global_setting.GlobalSetting
    rule: rule.Rule
    rule_settings: rule_settings.RuleSettings
    sensor: sensor.Sensor
    settings: settings.Settings
    view_map: view_map.ViewMap

    def __init__(self, client: IHTTPClient) -> None: ...
