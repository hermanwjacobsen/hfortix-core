"""Type stubs for LICENSE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import database
    from . import fortianalyzer_status
    from . import forticare_org_list
    from . import forticare_resellers
    from . import status


class License:
    """Type stub for License."""

    database: database.Database
    fortianalyzer_status: fortianalyzer_status.FortianalyzerStatus
    forticare_org_list: forticare_org_list.ForticareOrgList
    forticare_resellers: forticare_resellers.ForticareResellers
    status: status.Status

    def __init__(self, client: IHTTPClient) -> None: ...
