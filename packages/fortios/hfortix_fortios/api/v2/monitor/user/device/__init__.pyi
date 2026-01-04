"""Type stubs for DEVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import iot_query
    from . import purdue_level
    from . import query
    from . import stats


class Device:
    """Type stub for Device."""

    iot_query: iot_query.IotQuery
    purdue_level: purdue_level.PurdueLevel
    query: query.Query
    stats: stats.Stats

    def __init__(self, client: IHTTPClient) -> None: ...
