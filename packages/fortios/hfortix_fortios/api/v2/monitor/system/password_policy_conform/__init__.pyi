"""Type stubs for PASSWORD_POLICY_CONFORM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import select


class PasswordPolicyConform:
    """Type stub for PasswordPolicyConform."""

    select: select.Select

    def __init__(self, client: IHTTPClient) -> None: ...
