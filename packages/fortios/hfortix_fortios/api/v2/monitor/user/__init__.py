"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .banned import Banned
from .banned_base import Banned
from .collected_email import CollectedEmail
from .firewall import Firewall
from .firewall_base import Firewall
from .fortitoken import Fortitoken
from .fortitoken_base import Fortitoken
from .fsso import Fsso
from .fsso_base import Fsso
from .proxy import Proxy
from .proxy_base import Proxy

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class User:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.banned = Banned(client)
        self.banned = Banned(client)
        self.collected_email = CollectedEmail(client)
        self.firewall = Firewall(client)
        self.firewall = Firewall(client)
        self.fortitoken = Fortitoken(client)
        self.fortitoken = Fortitoken(client)
        self.fsso = Fsso(client)
        self.fsso = Fsso(client)
        self.proxy = Proxy(client)
        self.proxy = Proxy(client)
