"""Type stubs for DLP category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import data_type
    from . import dictionary
    from . import exact_data_match
    from . import filepattern
    from . import label
    from . import profile
    from . import sensor
    from . import settings


class Dlp:
    """Type stub for Dlp."""

    data_type: data_type.DataType
    dictionary: dictionary.Dictionary
    exact_data_match: exact_data_match.ExactDataMatch
    filepattern: filepattern.Filepattern
    label: label.Label
    profile: profile.Profile
    sensor: sensor.Sensor
    settings: settings.Settings

    def __init__(self, client: IHTTPClient) -> None: ...
