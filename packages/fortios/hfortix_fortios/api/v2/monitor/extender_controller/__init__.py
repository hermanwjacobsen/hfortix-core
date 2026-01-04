"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .extender import Extender
from .extender_base import Extender

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class ExtenderController:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.extender = Extender(client)
        self.extender = Extender(client)
