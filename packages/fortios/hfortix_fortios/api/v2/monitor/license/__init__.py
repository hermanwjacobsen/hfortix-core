"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .fortianalyzer_status import FortianalyzerStatus
from .forticare_org_list import ForticareOrgList
from .forticare_resellers import ForticareResellers
from .status import Status

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class License:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.fortianalyzer_status = FortianalyzerStatus(client)
        self.forticare_org_list = ForticareOrgList(client)
        self.forticare_resellers = ForticareResellers(client)
        self.status = Status(client)
