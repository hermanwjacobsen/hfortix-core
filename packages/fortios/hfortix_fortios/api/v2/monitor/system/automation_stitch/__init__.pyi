"""Type stubs for AUTOMATION_STITCH category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import test
    from . import webhook


class AutomationStitch:
    """Type stub for AutomationStitch."""

    test: test.Test
    webhook: webhook.Webhook

    def __init__(self, client: IHTTPClient) -> None: ...
