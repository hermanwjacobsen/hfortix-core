"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .installer import Installer
from .record_list import RecordList
from .summary import Summary

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class EndpointControl:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.installer = Installer(client)
        self.record_list = RecordList(client)
        self.summary = Summary(client)
