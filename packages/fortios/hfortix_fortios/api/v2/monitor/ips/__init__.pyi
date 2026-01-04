"""Type stubs for IPS category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import anomaly
    from . import hold_signatures
    from . import metadata
    from . import rate_based
    from . import session


class Ips:
    """Type stub for Ips."""

    anomaly: anomaly.Anomaly
    hold_signatures: hold_signatures.HoldSignatures
    metadata: metadata.Metadata
    rate_based: rate_based.RateBased
    session: session.Session

    def __init__(self, client: IHTTPClient) -> None: ...
