"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .fortiguard_categories import FortiguardCategories

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Videofilter:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.fortiguard_categories = FortiguardCategories(client)
