"""Type stubs for CASB category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import attribute_match
    from . import profile
    from . import saas_application
    from . import user_activity


class Casb:
    """Type stub for Casb."""

    attribute_match: attribute_match.AttributeMatch
    profile: profile.Profile
    saas_application: saas_application.SaasApplication
    user_activity: user_activity.UserActivity

    def __init__(self, client: IHTTPClient) -> None: ...
