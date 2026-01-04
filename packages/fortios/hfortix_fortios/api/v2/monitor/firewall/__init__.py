"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .address6_dynamic import Address6Dynamic
from .address_dynamic import AddressDynamic
from .address_fqdns import AddressFqdns
from .address_fqdns6 import AddressFqdns6
from .central_snat_map import CentralSnatMap
from .central_snat_map_base import CentralSnatMap
from .gtp import Gtp
from .gtp_base import Gtp
from .gtp_runtime_statistics import GtpRuntimeStatistics
from .gtp_statistics import GtpStatistics
from .health import Health
from .internet_service_basic import InternetServiceBasic
from .internet_service_fqdn import InternetServiceFqdn
from .internet_service_fqdn_icon_ids import InternetServiceFqdnIconIds
from .ippool import Ippool
from .local_in import LocalIn
from .local_in6 import LocalIn6
from .multicast_policy import MulticastPolicy
from .multicast_policy6 import MulticastPolicy6
from .multicast_policy6_base import MulticastPolicy6
from .multicast_policy_base import MulticastPolicy
from .per_ip_shaper import PerIpShaper
from .per_ip_shaper_base import PerIpShaper
from .policy import Policy
from .policy_base import Policy
from .proxy_policy import ProxyPolicy
from .proxy_policy_base import ProxyPolicy
from .saas_application import SaasApplication
from .security_policy import SecurityPolicy
from .security_policy_base import SecurityPolicy
from .shaper import Shaper
from .shaper_base import Shaper
from .uuid_list import UuidList
from .vip_overlap import VipOverlap

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Firewall:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.address6_dynamic = Address6Dynamic(client)
        self.address_dynamic = AddressDynamic(client)
        self.address_fqdns = AddressFqdns(client)
        self.address_fqdns6 = AddressFqdns6(client)
        self.central_snat_map = CentralSnatMap(client)
        self.central_snat_map = CentralSnatMap(client)
        self.gtp = Gtp(client)
        self.gtp = Gtp(client)
        self.gtp_runtime_statistics = GtpRuntimeStatistics(client)
        self.gtp_statistics = GtpStatistics(client)
        self.health = Health(client)
        self.internet_service_basic = InternetServiceBasic(client)
        self.internet_service_fqdn = InternetServiceFqdn(client)
        self.internet_service_fqdn_icon_ids = InternetServiceFqdnIconIds(client)
        self.ippool = Ippool(client)
        self.local_in = LocalIn(client)
        self.local_in6 = LocalIn6(client)
        self.multicast_policy = MulticastPolicy(client)
        self.multicast_policy6 = MulticastPolicy6(client)
        self.multicast_policy6 = MulticastPolicy6(client)
        self.multicast_policy = MulticastPolicy(client)
        self.per_ip_shaper = PerIpShaper(client)
        self.per_ip_shaper = PerIpShaper(client)
        self.policy = Policy(client)
        self.policy = Policy(client)
        self.proxy_policy = ProxyPolicy(client)
        self.proxy_policy = ProxyPolicy(client)
        self.saas_application = SaasApplication(client)
        self.security_policy = SecurityPolicy(client)
        self.security_policy = SecurityPolicy(client)
        self.shaper = Shaper(client)
        self.shaper = Shaper(client)
        self.uuid_list = UuidList(client)
        self.vip_overlap = VipOverlap(client)
