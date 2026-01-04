"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .category_quota import CategoryQuota
from .category_quota_base import CategoryQuota
from .fortiguard_categories import FortiguardCategories
from .malicious_urls import MaliciousUrls
from .malicious_urls_base import MaliciousUrls
from .override import Override
from .override_base import Override
from .trusted_urls import TrustedUrls

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Webfilter:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.category_quota = CategoryQuota(client)
        self.category_quota = CategoryQuota(client)
        self.fortiguard_categories = FortiguardCategories(client)
        self.malicious_urls = MaliciousUrls(client)
        self.malicious_urls = MaliciousUrls(client)
        self.override = Override(client)
        self.override = Override(client)
        self.trusted_urls = TrustedUrls(client)
