"""
Rate limit tracking for FortiCloud services.

Provides simple counters to track API calls and errors for rate limit monitoring.
No enforcement - just visibility for future use.
"""

from __future__ import annotations

import time
from collections import deque
from typing import Any


class RateLimitStats:
    """
    Simple rate limit tracking (no enforcement).
    
    Tracks API calls and errors over multiple time windows:
    - Last minute (60 seconds)
    - Last 5 minutes (300 seconds)
    - Last hour (3600 seconds)
    
    Does NOT enforce limits - just provides visibility.
    
    Usage:
        >>> stats = RateLimitStats(
        ...     calls_per_min=100,
        ...     calls_per_5min=500,
        ...     calls_per_hour=1000,
        ...     errors_per_hour=10
        ... )
        >>> 
        >>> # Record calls
        >>> stats.record_call()
        >>> stats.record_error()
        >>> 
        >>> # Check status
        >>> status = stats.get_status()
        >>> print(f"Calls last min: {status['calls_last_min']}")
        >>> print(f"Calls last 5min: {status['calls_last_5min']}")
        >>> print(f"Calls last hour: {status['calls_last_hour']}")
    """
    
    def __init__(
        self,
        calls_per_min: int | None = None,
        calls_per_5min: int | None = None,
        calls_per_hour: int | None = None,
        errors_per_min: int | None = None,
        errors_per_5min: int | None = None,
        errors_per_hour: int | None = None,
    ):
        """
        Initialize rate limit stats.
        
        Args:
            calls_per_min: Maximum calls allowed per minute (None = no limit)
            calls_per_5min: Maximum calls allowed per 5 minutes (None = no limit)
            calls_per_hour: Maximum calls allowed per hour (None = no limit)
            errors_per_min: Maximum errors allowed per minute (None = no limit)
            errors_per_5min: Maximum errors allowed per 5 minutes (None = no limit)
            errors_per_hour: Maximum errors allowed per hour (None = no limit)
        """
        self.limits = {
            "calls_per_min": calls_per_min,
            "calls_per_5min": calls_per_5min,
            "calls_per_hour": calls_per_hour,
            "errors_per_min": errors_per_min,
            "errors_per_5min": errors_per_5min,
            "errors_per_hour": errors_per_hour,
        }
        
        # Track timestamps with deque (efficient for sliding window)
        # maxlen prevents unbounded growth
        max_calls_limit = max(
            (limit for limit in [calls_per_min, calls_per_5min, calls_per_hour] if limit is not None),
            default=1000
        )
        max_errors_limit = max(
            (limit for limit in [errors_per_min, errors_per_5min, errors_per_hour] if limit is not None),
            default=100
        )
        
        self._calls: deque[float] = deque(maxlen=max(max_calls_limit * 2, 1000))  # Keep extra for accuracy
        self._errors: deque[float] = deque(maxlen=max(max_errors_limit * 2, 100))
        
        # Total counters (never reset)
        self._total_calls = 0
        self._total_errors = 0
    
    def record_call(self) -> None:
        """Record an API call."""
        now = time.time()
        self._calls.append(now)
        self._total_calls += 1
    
    def record_error(self) -> None:
        """Record an API error."""
        now = time.time()
        self._errors.append(now)
        self._total_errors += 1
    
    def get_status(self) -> dict[str, Any]:
        """
        Get current rate limit status.
        
        Returns:
            Dict with:
            - calls_last_min: Call count in last 60 seconds
            - calls_last_5min: Call count in last 300 seconds
            - calls_last_hour: Call count in last 3600 seconds
            - errors_last_min: Error count in last 60 seconds
            - errors_last_5min: Error count in last 300 seconds
            - errors_last_hour: Error count in last 3600 seconds
            - total_calls: Total calls since creation
            - total_errors: Total errors since creation
            - limits: Configured limits
            - within_limits: True if all limits are respected (if set)
        """
        now = time.time()
        
        # Count calls in time windows
        calls_last_min = sum(1 for t in self._calls if now - t < 60)
        calls_last_5min = sum(1 for t in self._calls if now - t < 300)
        calls_last_hour = sum(1 for t in self._calls if now - t < 3600)
        
        # Count errors in time windows
        errors_last_min = sum(1 for t in self._errors if now - t < 60)
        errors_last_5min = sum(1 for t in self._errors if now - t < 300)
        errors_last_hour = sum(1 for t in self._errors if now - t < 3600)
        
        # Check if within limits (only check limits that are set)
        within_limits = True
        
        if self.limits["calls_per_min"] is not None:
            within_limits = within_limits and (calls_last_min <= self.limits["calls_per_min"])
        
        if self.limits["calls_per_5min"] is not None:
            within_limits = within_limits and (calls_last_5min <= self.limits["calls_per_5min"])
        
        if self.limits["calls_per_hour"] is not None:
            within_limits = within_limits and (calls_last_hour <= self.limits["calls_per_hour"])
        
        if self.limits["errors_per_min"] is not None:
            within_limits = within_limits and (errors_last_min <= self.limits["errors_per_min"])
        
        if self.limits["errors_per_5min"] is not None:
            within_limits = within_limits and (errors_last_5min <= self.limits["errors_per_5min"])
        
        if self.limits["errors_per_hour"] is not None:
            within_limits = within_limits and (errors_last_hour <= self.limits["errors_per_hour"])
        
        return {
            "calls_last_min": calls_last_min,
            "calls_last_5min": calls_last_5min,
            "calls_last_hour": calls_last_hour,
            "errors_last_min": errors_last_min,
            "errors_last_5min": errors_last_5min,
            "errors_last_hour": errors_last_hour,
            "total_calls": self._total_calls,
            "total_errors": self._total_errors,
            "limits": self.limits,
            "within_limits": within_limits,
        }
    
    def reset(self) -> None:
        """Reset all counters (use with caution)."""
        self._calls.clear()
        self._errors.clear()
        self._total_calls = 0
        self._total_errors = 0
    
    def __repr__(self) -> str:
        """String representation."""
        status = self.get_status()
        return (
            f"RateLimitStats("
            f"calls_1m={status['calls_last_min']}/{self.limits['calls_per_min']}, "
            f"calls_5m={status['calls_last_5min']}/{self.limits['calls_per_5min']}, "
            f"calls_1h={status['calls_last_hour']}/{self.limits['calls_per_hour']}, "
            f"within_limits={status['within_limits']})"
        )
