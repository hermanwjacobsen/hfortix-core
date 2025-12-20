"""
FortiOS Service API - System service operations
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .....http_client_interface import IHTTPClient

from .system import System

__all__ = ["System"]
