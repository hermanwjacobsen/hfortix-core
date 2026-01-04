"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .answers import Answers
from .redirect_portal import RedirectPortal
from .service_communication_stats import ServiceCommunicationStats

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Fortiguard:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.answers = Answers(client)
        self.redirect_portal = RedirectPortal(client)
        self.service_communication_stats = ServiceCommunicationStats(client)
