"""
Async Rate Limiter with Token Bucket Algorithm

Provides asyncio-safe rate limiting with queue support for asynchronous operations.
"""

from __future__ import annotations

import asyncio
import logging
import time
from typing import Literal

logger = logging.getLogger("hfortix.async_rate_limiter")

__all__ = ["AsyncRateLimiter"]


class AsyncRateLimiter:
    """
    Async token bucket rate limiter with FIFO queue support
    
    Implements token bucket algorithm for smooth rate limiting with burst support.
    asyncio-safe for use in asynchronous HTTP clients.
    
    Features:
    - Token bucket algorithm (allows controlled bursts)
    - FIFO queue for overflow handling
    - Comprehensive metrics tracking
    - Three strategies: queue, drop, raise
    - asyncio-safe with asyncio.Lock
    
    Args:
        max_requests: Maximum requests allowed per window (token capacity)
        window_seconds: Time window in seconds for rate limiting
        strategy: How to handle requests when limit exceeded:
            - "queue": Queue requests (wait for tokens)
            - "drop": Drop requests silently (return False)
            - "raise": Raise RateLimitExceededError
        queue_size: Maximum queued requests (default: 100)
        queue_timeout: Maximum wait time in queue seconds (default: 30.0)
        queue_overflow: What to do when queue is full:
            - "block": Wait for space in queue (with timeout)
            - "drop": Drop request silently (return False)
            - "raise": Raise RateLimitQueueFullError
            
    Example:
        >>> limiter = AsyncRateLimiter(
        ...     max_requests=100,
        ...     window_seconds=60.0,
        ...     strategy="queue",
        ...     queue_size=50
        ... )
        >>> 
        >>> if await limiter.acquire():
        ...     try:
        ...         # Make HTTP request
        ...         response = await client.get(...)
        ...     finally:
        ...         await limiter.release()
    """
    
    def __init__(
        self,
        max_requests: int,
        window_seconds: float,
        strategy: Literal["queue", "drop", "raise"] = "queue",
        queue_size: int = 100,
        queue_timeout: float = 30.0,
        queue_overflow: Literal["block", "drop", "raise"] = "block",
    ) -> None:
        # Validate parameters
        if max_requests <= 0:
            raise ValueError("max_requests must be > 0")
        if window_seconds <= 0:
            raise ValueError("window_seconds must be > 0")
        if queue_size < 0:
            raise ValueError("queue_size must be >= 0")
        if queue_timeout <= 0:
            raise ValueError("queue_timeout must be > 0")
        if strategy not in ("queue", "drop", "raise"):
            raise ValueError("strategy must be 'queue', 'drop', or 'raise'")
        if queue_overflow not in ("block", "drop", "raise"):
            raise ValueError("queue_overflow must be 'block', 'drop', or 'raise'")
            
        # Configuration
        self._max_requests = max_requests
        self._window_seconds = window_seconds
        self._strategy = strategy
        self._queue_size = queue_size
        self._queue_timeout = queue_timeout
        self._queue_overflow = queue_overflow
        
        # Token bucket state
        self._tokens = float(max_requests)  # Start with full bucket
        self._refill_rate = max_requests / window_seconds  # Tokens per second
        self._last_refill = time.time()
        
        # Queue for overflow requests
        self._request_queue: asyncio.Queue = asyncio.Queue(maxsize=queue_size)
        
        # Asyncio safety
        self._lock = asyncio.Lock()
        
        # Metrics
        self._total_requests = 0
        self._allowed_requests = 0
        self._queued_requests = 0
        self._dropped_requests = 0
        self._queue_wait_times: list[float] = []
        self._max_queue_wait = 0.0
        self._start_time = time.time()
        
        logger.debug(
            f"AsyncRateLimiter initialized: {max_requests} req/{window_seconds}s, "
            f"strategy={strategy}, queue_size={queue_size}"
        )
    
    def _refill_tokens(self) -> None:
        """Refill tokens based on elapsed time (token bucket algorithm)"""
        now = time.time()
        elapsed = now - self._last_refill
        
        # Add tokens based on time elapsed
        tokens_to_add = elapsed * self._refill_rate
        self._tokens = min(self._max_requests, self._tokens + tokens_to_add)
        self._last_refill = now
        
        logger.debug(f"Refilled tokens: {self._tokens:.2f}/{self._max_requests}")
    
    async def acquire(self) -> bool:
        """
        Acquire permission to make a request
        
        Returns:
            bool: True if request is allowed, False if dropped
            
        Raises:
            RateLimitExceededError: If strategy="raise" and limit exceeded
            RateLimitQueueFullError: If queue_overflow="raise" and queue is full
            RateLimitQueueTimeoutError: If request times out in queue
        """
        self._total_requests += 1
        
        async with self._lock:
            self._refill_tokens()
            
            # Fast path: tokens available
            if self._tokens >= 1.0:
                self._tokens -= 1.0
                self._allowed_requests += 1
                logger.debug(
                    f"Request allowed immediately ({self._tokens:.2f} tokens remaining)"
                )
                return True
            
            # Rate limit exceeded - handle based on strategy
            logger.info(
                f"Rate limit exceeded ({self._total_requests} total, "
                f"{self._allowed_requests} allowed, {self._tokens:.2f} tokens)"
            )
            
            if self._strategy == "drop":
                self._dropped_requests += 1
                logger.info(f"Request dropped (strategy=drop)")
                return False
                
            elif self._strategy == "raise":
                self._dropped_requests += 1
                from hfortix_core.exceptions import RateLimitExceededError
                raise RateLimitExceededError(
                    f"Rate limit exceeded: {self._max_requests} requests per "
                    f"{self._window_seconds}s (tokens: {self._tokens:.2f})"
                )
            
            # strategy == "queue"
            # Special case: if queue_size is 0, behave like "drop" strategy
            if self._queue_size == 0:
                self._dropped_requests += 1
                if self._queue_overflow == "raise":
                    from hfortix_core.exceptions import RateLimitQueueFullError
                    raise RateLimitQueueFullError(
                        f"Rate limit queue full (queue_size=0, no queuing available)"
                    )
                logger.warning(f"Request dropped - queue_size=0, no queuing available")
                return False
            
            # Try to add to queue
            queue_start = time.time()
            
            try:
                if self._queue_overflow == "block":
                    # Block until space available (with timeout)
                    await asyncio.wait_for(
                        self._request_queue.put(True),
                        timeout=self._queue_timeout
                    )
                elif self._queue_overflow == "drop":
                    # Try to add, drop if full
                    self._request_queue.put_nowait(True)
                else:  # "raise"
                    # Try to add, raise if full
                    self._request_queue.put_nowait(True)
                    
                self._queued_requests += 1
                logger.info(
                    f"Request queued ({self._request_queue.qsize()}/{self._queue_size})"
                )
                
            except asyncio.QueueFull:
                self._dropped_requests += 1
                if self._queue_overflow == "raise":
                    from hfortix_core.exceptions import RateLimitQueueFullError
                    raise RateLimitQueueFullError(
                        f"Rate limit queue full ({self._queue_size} max)"
                    )
                logger.warning(f"Request dropped - queue full")
                return False
            except asyncio.TimeoutError:
                self._dropped_requests += 1
                logger.warning(f"Request dropped - queue put timeout")
                return False
        
        # Wait for token to become available (outside lock)
        while True:
            await asyncio.sleep(0.1)  # Check every 100ms
            
            async with self._lock:
                self._refill_tokens()
                
                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    self._allowed_requests += 1
                    
                    # Remove from queue
                    try:
                        self._request_queue.get_nowait()
                        self._request_queue.task_done()
                    except asyncio.QueueEmpty:
                        pass
                    
                    # Track wait time
                    wait_time = time.time() - queue_start
                    self._queue_wait_times.append(wait_time)
                    self._max_queue_wait = max(self._max_queue_wait, wait_time)
                    
                    logger.debug(f"Queued request allowed after {wait_time:.2f}s wait")
                    return True
            
            # Check timeout
            if time.time() - queue_start > self._queue_timeout:
                async with self._lock:
                    # Remove from queue
                    try:
                        self._request_queue.get_nowait()
                        self._request_queue.task_done()
                    except asyncio.QueueEmpty:
                        pass
                    
                    self._dropped_requests += 1
                
                from hfortix_core.exceptions import RateLimitQueueTimeoutError
                raise RateLimitQueueTimeoutError(
                    f"Request timed out in queue after {self._queue_timeout}s"
                )
    
    async def release(self) -> None:
        """
        Release after request completes
        
        Note: Current implementation doesn't require explicit release,
        but included for API consistency and future extensions.
        """
        pass
    
    async def get_stats(self) -> dict:
        """
        Get comprehensive rate limiter statistics
        
        Returns:
            dict: Statistics including:
                - total_requests: Total requests attempted
                - allowed_requests: Requests allowed through
                - queued_requests: Requests that were queued
                - dropped_requests: Requests that were dropped
                - current_queue_size: Current queue size
                - max_queue_size: Maximum queue capacity
                - queue_utilization: Queue usage percentage (0.0-1.0)
                - avg_queue_wait_ms: Average queue wait time in milliseconds
                - max_queue_wait_ms: Maximum queue wait time in milliseconds
                - rate_limit_efficiency: Percentage of capacity used
                - tokens_available: Current tokens available
                - tokens_capacity: Maximum token capacity
                - refill_rate_per_sec: Token refill rate
                - window_seconds: Rate limit window
                - uptime_seconds: Uptime since creation
                - strategy: Rate limit strategy
                - queue_overflow: Queue overflow behavior
        """
        async with self._lock:
            self._refill_tokens()
            
            uptime = time.time() - self._start_time
            
            # Calculate efficiency (what % of capacity is being used)
            if uptime > 0:
                requests_per_sec = self._allowed_requests / uptime
                capacity_per_sec = self._refill_rate
                efficiency = min(1.0, requests_per_sec / capacity_per_sec) if capacity_per_sec > 0 else 0.0
            else:
                efficiency = 0.0
            
            # Calculate queue metrics
            avg_wait = (
                sum(self._queue_wait_times) / len(self._queue_wait_times)
                if self._queue_wait_times else 0.0
            )
            
            return {
                # Request counts
                "total_requests": self._total_requests,
                "allowed_requests": self._allowed_requests,
                "queued_requests": self._queued_requests,
                "dropped_requests": self._dropped_requests,
                
                # Queue metrics
                "current_queue_size": self._request_queue.qsize(),
                "max_queue_size": self._queue_size,
                "queue_utilization": (
                    self._request_queue.qsize() / self._queue_size
                    if self._queue_size > 0 else 0.0
                ),
                "avg_queue_wait_ms": avg_wait * 1000,
                "max_queue_wait_ms": self._max_queue_wait * 1000,
                
                # Efficiency
                "rate_limit_efficiency": efficiency,
                "tokens_available": self._tokens,
                "tokens_capacity": self._max_requests,
                "refill_rate_per_sec": self._refill_rate,
                
                # Configuration
                "window_seconds": self._window_seconds,
                "uptime_seconds": uptime,
                "strategy": self._strategy,
                "queue_overflow": self._queue_overflow,
            }
