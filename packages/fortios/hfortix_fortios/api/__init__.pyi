"""Type stubs for hfortix_fortios.api module."""

from __future__ import annotations

from hfortix_core.http.interface import IHTTPClient

from .utils import Utils
from .v2.cmdb import CMDB, CMDBDictMode, CMDBObjectMode
from .v2.log import Log
from .v2.monitor import Monitor, MonitorDictMode, MonitorObjectMode
from .v2.service import Service, ServiceDictMode, ServiceObjectMode

__all__ = ["API", "APIDictMode", "APIObjectMode", "CMDB", "Log", "Monitor", "Service"]


class APIDictMode:
    """API interface for dict response mode."""
    
    cmdb: CMDBDictMode
    monitor: MonitorDictMode
    log: Log
    service: ServiceDictMode
    utils: Utils
    
    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None: ...


class APIObjectMode:
    """API interface for object response mode."""
    
    cmdb: CMDBObjectMode
    monitor: MonitorObjectMode
    log: Log
    service: ServiceObjectMode
    utils: Utils
    
    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None: ...


class API:
    """FortiOS REST API v2 Interface."""
    
    cmdb: CMDB
    monitor: Monitor
    log: Log
    service: Service
    utils: Utils
    
    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None: ...
