"""Type stubs for AUTHENTICATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import rule
    from . import scheme
    from . import setting


class Authentication:
    """Type stub for Authentication."""

    rule: rule.Rule
    scheme: scheme.Scheme
    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
