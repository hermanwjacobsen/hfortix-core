"""Type stubs for MCLAG_ICL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import eligible_peer
    from . import set_tier1
    from . import set_tier_plus
    from . import tier_plus_candidates


class MclagIcl:
    """Type stub for MclagIcl."""

    eligible_peer: eligible_peer.EligiblePeer
    set_tier1: set_tier1.SetTier1
    set_tier_plus: set_tier_plus.SetTierPlus
    tier_plus_candidates: tier_plus_candidates.TierPlusCandidates

    def __init__(self, client: IHTTPClient) -> None: ...
