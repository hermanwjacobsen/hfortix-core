"""Session management for FortiCloud services."""

from .cloud_session import CloudSession, TokenInfo
from .token_storage import TokenStorage, InMemoryTokenStorage, TokenData
from .lifecycle_hooks import (
    TokenLifecycleHooks,
    TokenEvent,
    SimpleLifecycleHooks,
    TokenAcquiredCallback,
    TokenRefreshedCallback,
    TokenExpiredCallback,
    TokenFailedCallback,
)

__all__ = [
    # Core session
    "CloudSession",
    "TokenInfo",
    # Token storage
    "TokenStorage",
    "InMemoryTokenStorage",
    "TokenData",
    # Lifecycle hooks
    "TokenLifecycleHooks",
    "TokenEvent",
    "SimpleLifecycleHooks",
    "TokenAcquiredCallback",
    "TokenRefreshedCallback",
    "TokenExpiredCallback",
    "TokenFailedCallback",
]
