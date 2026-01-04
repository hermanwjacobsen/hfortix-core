"""Type stubs for AUTO_CONFIG category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import custom
    from . import default
    from . import policy


class AutoConfig:
    """Type stub for AutoConfig."""

    custom: custom.Custom
    default: default.Default
    policy: policy.Policy

    def __init__(self, client: IHTTPClient) -> None: ...
