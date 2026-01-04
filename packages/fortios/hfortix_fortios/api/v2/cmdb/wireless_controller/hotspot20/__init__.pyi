"""Type stubs for HOTSPOT20 category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import anqp_3gpp_cellular
    from . import anqp_ip_address_type
    from . import anqp_nai_realm
    from . import anqp_network_auth_type
    from . import anqp_roaming_consortium
    from . import anqp_venue_name
    from . import anqp_venue_url
    from . import h2qp_advice_of_charge
    from . import h2qp_conn_capability
    from . import h2qp_operator_name
    from . import h2qp_osu_provider
    from . import h2qp_osu_provider_nai
    from . import h2qp_terms_and_conditions
    from . import h2qp_wan_metric
    from . import hs_profile
    from . import icon
    from . import qos_map


class Hotspot20:
    """Type stub for Hotspot20."""

    anqp_3gpp_cellular: anqp_3gpp_cellular.Anqp3gppCellular
    anqp_ip_address_type: anqp_ip_address_type.AnqpIpAddressType
    anqp_nai_realm: anqp_nai_realm.AnqpNaiRealm
    anqp_network_auth_type: anqp_network_auth_type.AnqpNetworkAuthType
    anqp_roaming_consortium: anqp_roaming_consortium.AnqpRoamingConsortium
    anqp_venue_name: anqp_venue_name.AnqpVenueName
    anqp_venue_url: anqp_venue_url.AnqpVenueUrl
    h2qp_advice_of_charge: h2qp_advice_of_charge.H2qpAdviceOfCharge
    h2qp_conn_capability: h2qp_conn_capability.H2qpConnCapability
    h2qp_operator_name: h2qp_operator_name.H2qpOperatorName
    h2qp_osu_provider: h2qp_osu_provider.H2qpOsuProvider
    h2qp_osu_provider_nai: h2qp_osu_provider_nai.H2qpOsuProviderNai
    h2qp_terms_and_conditions: h2qp_terms_and_conditions.H2qpTermsAndConditions
    h2qp_wan_metric: h2qp_wan_metric.H2qpWanMetric
    hs_profile: hs_profile.HsProfile
    icon: icon.Icon
    qos_map: qos_map.QosMap

    def __init__(self, client: IHTTPClient) -> None: ...
