"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .delete import Delete
from .download import Download
from .list import List
from .meta import Meta
from .start import Start
from .start_base import Start
from .stop import Stop

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Sniffer:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.delete = Delete(client)
        self.download = Download(client)
        self.list = List(client)
        self.meta = Meta(client)
        self.start = Start(client)
        self.start = Start(client)
        self.stop = Stop(client)
