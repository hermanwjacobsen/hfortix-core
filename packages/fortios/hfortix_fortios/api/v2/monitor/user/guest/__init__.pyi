"""Type stubs for GUEST category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import email
    from . import sms


class Guest:
    """Type stub for Guest."""

    email: email.Email
    sms: sms.Sms

    def __init__(self, client: IHTTPClient) -> None: ...
