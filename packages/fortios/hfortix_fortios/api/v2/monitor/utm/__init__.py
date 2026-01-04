"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .application_categories import ApplicationCategories

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Utm:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.application_categories = ApplicationCategories(client)
