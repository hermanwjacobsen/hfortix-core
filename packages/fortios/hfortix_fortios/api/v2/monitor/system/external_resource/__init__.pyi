"""Type stubs for EXTERNAL_RESOURCE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import dynamic
    from . import entry_list
    from . import generic_address
    from . import refresh
    from . import validate_jsonpath


class ExternalResource:
    """Type stub for ExternalResource."""

    dynamic: dynamic.Dynamic
    entry_list: entry_list.EntryList
    generic_address: generic_address.GenericAddress
    refresh: refresh.Refresh
    validate_jsonpath: validate_jsonpath.ValidateJsonpath

    def __init__(self, client: IHTTPClient) -> None: ...
