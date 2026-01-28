# Rate Limiting and Resilience

This guide covers HFortix's built-in resilience features for handling API rate limits, transient failures, and high-load scenarios.

## Table of Contents

- [Overview](#overview)
- [HTTP 429 Rate Limiting](#http-429-rate-limiting)
- [Circuit Breaker Pattern](#circuit-breaker-pattern)
- [Retry Strategies](#retry-strategies)
- [Connection Pool Management](#connection-pool-management)
- [Async Patterns for High Throughput](#async-patterns-for-high-throughput)
- [Best Practices](#best-practices)

## Overview

FortiGate devices enforce API rate limits to prevent resource exhaustion. HFortix provides multiple resilience mechanisms:

- **Automatic Retry**: Exponential backoff for transient failures
- **Circuit Breaker**: Fast-fail when service is degraded
- **Connection Pooling**: Efficient connection reuse with HTTP/2
- **Async Support**: High-throughput operations with asyncio

## HTTP 429 Rate Limiting

### Understanding FortiOS Rate Limits

FortiGate enforces rate limits on API requests:
- **Default**: ~10 requests/second per session
- **Burst**: ~50 requests in short bursts
- **Response**: HTTP 429 (Too Many Requests) with `Retry-After` header

### Automatic Handling

HFortix automatically retries 429 responses:

```python
from hfortix_fortios import FortiOS

# Automatic retry with exponential backoff
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_retries=5,  # Retry up to 5 times (default: 3)
    retry_strategy="exponential",  # or "linear"
    retry_jitter=True,  # Add randomness to prevent thundering herd
)

# This will automatically retry if rate limited
result = fgt.api.cmdb.firewall.address.get()
```

### Retry Strategies

#### Exponential Backoff (Default)

Doubles wait time after each retry:
- Attempt 1: Wait 1s
- Attempt 2: Wait 2s
- Attempt 3: Wait 4s
- Attempt 4: Wait 8s

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    retry_strategy="exponential",
    max_retries=5,
)
```

#### Linear Backoff

Fixed incremental delay:
- Attempt 1: Wait 1s
- Attempt 2: Wait 2s
- Attempt 3: Wait 3s

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    retry_strategy="linear",
    max_retries=3,
)
```

#### Adaptive Retry

Dynamically adjusts based on server load signals:

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    adaptive_retry=True,  # Use server hints (Retry-After header)
)
```

### Retry with Jitter

Add randomness to prevent synchronized retries (thundering herd):

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    retry_jitter=True,  # Add ±25% randomness to delays
)
```

## Circuit Breaker Pattern

### Overview

Circuit breaker prevents cascading failures by failing fast when service is unhealthy.

**States:**
- **CLOSED**: Normal operation, requests flow through
- **OPEN**: Service unhealthy, fail immediately without calling API
- **HALF_OPEN**: Testing if service recovered

### Configuration

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    circuit_breaker_threshold=10,  # Open after 10 consecutive failures
    circuit_breaker_timeout=30.0,  # Try recovery after 30 seconds
    circuit_breaker_auto_retry=True,  # Automatically retry when circuit opens
    circuit_breaker_max_retries=3,  # Max auto-retries
    circuit_breaker_retry_delay=5.0,  # Wait 5s between retries
)
```

### Manual Circuit Breaker Control

```python
# Check circuit state
state = fgt._client.circuit_breaker.state
print(f"Circuit state: {state}")  # CLOSED, OPEN, or HALF_OPEN

# Manually reset circuit
fgt._client.circuit_breaker.reset()
```

### Exception Handling

```python
from hfortix_core import CircuitBreakerOpenError, RateLimitError

try:
    result = fgt.api.cmdb.firewall.address.get()
except CircuitBreakerOpenError:
    print("Circuit breaker open - service unavailable")
    # Wait and retry later
except RateLimitError as e:
    print(f"Rate limited: {e}")
    # Retry after delay
```

## Connection Pool Management

### HTTP/2 Connection Pooling

HFortix uses `httpx` with HTTP/2 for efficient connection reuse:

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_connections=100,  # Maximum total connections
    max_keepalive_connections=20,  # Connections to keep alive
    session_idle_timeout=300,  # Close idle connections after 5 min
)
```

### Monitoring Connection Pool

```python
# Get real-time connection statistics
stats = fgt.connection_stats
print(f"Active requests: {stats['active_requests']}")
print(f"Total requests: {stats['total_requests']}")
print(f"Pool exhaustion events: {stats['pool_exhaustion_count']}")

# Inspect last request
info = fgt.last_request
if info:
    print(f"Last request: {info['method']} {info['endpoint']}")
    print(f"Response time: {info['response_time_ms']:.1f}ms")
    print(f"Status code: {info['status_code']}")
```

### Connection Pool Exhaustion

When pool is exhausted, requests wait for available connections:

```python
# Monitor pool exhaustion
stats = fgt.connection_stats
if stats['pool_exhaustion_count'] > 0:
    print(f"Pool exhausted {stats['pool_exhaustion_count']} times")
    
    # Increase pool size if needed
    # (requires creating new client instance)
```

## Async Patterns for High Throughput

### Basic Async Usage

```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    fgt = FortiOS(
        host="192.168.1.99",
        token="your-token",
        mode="async",  # Enable async mode
        max_connections=50,  # Higher limit for concurrent requests
    )
    
    async with fgt:
        # Async API calls
        result = await fgt.api.cmdb.firewall.address.get()
        print(result)

asyncio.run(main())
```

### Concurrent Requests

Process multiple requests in parallel:

```python
import asyncio
from hfortix_fortios import FortiOS

async def get_all_addresses(fgt):
    """Get all firewall addresses concurrently."""
    result = await fgt.api.cmdb.firewall.address.get()
    return result.get('results', [])

async def create_address(fgt, name, subnet):
    """Create a single firewall address."""
    data = {
        "name": name,
        "subnet": subnet,
        "type": "ipmask",
    }
    return await fgt.api.cmdb.firewall.address.post(data=data)

async def main():
    fgt = FortiOS(
        host="192.168.1.99",
        token="your-token",
        mode="async",
        max_connections=20,  # Allow 20 concurrent connections
    )
    
    async with fgt:
        # Create multiple addresses concurrently
        addresses = [
            ("NET_10.0.1.0", "10.0.1.0/24"),
            ("NET_10.0.2.0", "10.0.2.0/24"),
            ("NET_10.0.3.0", "10.0.3.0/24"),
        ]
        
        # Run all creates concurrently
        results = await asyncio.gather(
            *[create_address(fgt, name, subnet) for name, subnet in addresses]
        )
        
        print(f"Created {len(results)} addresses")

asyncio.run(main())
```

### Rate Limiting with Async

Use semaphore to control concurrency:

```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    fgt = FortiOS(
        host="192.168.1.99",
        token="your-token",
        mode="async",
        max_connections=10,
    )
    
    # Limit to 5 concurrent requests
    semaphore = asyncio.Semaphore(5)
    
    async def create_with_limit(name, subnet):
        async with semaphore:
            data = {
                "name": name,
                "subnet": subnet,
                "type": "ipmask",
            }
            return await fgt.api.cmdb.firewall.address.post(data=data)
    
    async with fgt:
        addresses = [(f"NET_{i}", f"10.0.{i}.0/24") for i in range(100)]
        
        # Only 5 concurrent requests at a time
        results = await asyncio.gather(
            *[create_with_limit(name, subnet) for name, subnet in addresses]
        )

asyncio.run(main())
```

### Async with Retry

Combine async with automatic retry:

```python
import asyncio
from hfortix_fortios import FortiOS
from hfortix_core import RateLimitError

async def main():
    fgt = FortiOS(
        host="192.168.1.99",
        token="your-token",
        mode="async",
        max_retries=5,  # Auto-retry works with async too
        retry_strategy="exponential",
        retry_jitter=True,
    )
    
    async with fgt:
        try:
            # This will auto-retry if rate limited
            result = await fgt.api.cmdb.firewall.address.get()
        except RateLimitError as e:
            print(f"Still rate limited after retries: {e}")

asyncio.run(main())
```

## Best Practices

### 1. Choose Appropriate Retry Strategy

```python
# For production - exponential with jitter
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    retry_strategy="exponential",
    retry_jitter=True,  # Prevent thundering herd
    max_retries=5,
)
```

### 2. Enable Circuit Breaker for Critical Services

```python
# Fail fast when service is unhealthy
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    circuit_breaker_threshold=10,
    circuit_breaker_timeout=30.0,
    circuit_breaker_auto_retry=True,
)
```

### 3. Use Async for Bulk Operations

```python
# Process large batches efficiently
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    mode="async",
    max_connections=20,
)
```

### 4. Monitor Connection Pool

```python
# Check for pool exhaustion
stats = fgt.connection_stats
if stats['pool_exhaustion_count'] > 10:
    print("WARNING: Increase max_connections")
```

### 5. Handle Exceptions Gracefully

```python
from hfortix_core import (
    CircuitBreakerOpenError,
    RateLimitError,
    ServiceUnavailableError,
)

try:
    result = fgt.api.cmdb.firewall.address.get()
except RateLimitError:
    # Implement custom backoff
    time.sleep(5)
except CircuitBreakerOpenError:
    # Service degraded - wait longer
    time.sleep(30)
except ServiceUnavailableError:
    # FortiGate overloaded
    time.sleep(60)
```

### 6. Use Read-Only Mode for Auditing

```python
# Prevent accidental writes
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    read_only=True,  # All writes will raise ReadOnlyModeError
)
```

### 7. Track Operations for Compliance

```python
# Track all write operations
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    track_operations=True,
)

# Get operation history
operations = fgt.get_write_operations()
for op in operations:
    print(f"{op['timestamp']}: {op['method']} {op['endpoint']}")
```

## Configuration Examples

### Conservative (Low Load)

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_retries=3,
    retry_strategy="exponential",
    max_connections=10,
    max_keepalive_connections=5,
)
```

### Aggressive (High Load)

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    mode="async",
    max_retries=7,
    retry_strategy="exponential",
    retry_jitter=True,
    max_connections=100,
    max_keepalive_connections=20,
    circuit_breaker_threshold=20,
    circuit_breaker_auto_retry=True,
)
```

### Production Recommended

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_retries=5,
    retry_strategy="exponential",
    retry_jitter=True,
    adaptive_retry=True,
    max_connections=50,
    max_keepalive_connections=10,
    circuit_breaker_threshold=15,
    circuit_breaker_timeout=30.0,
    circuit_breaker_auto_retry=True,
    track_operations=True,
)
```

## See Also

- [Error Handling Guide](ERROR_HANDLING_CONFIG.md)
- [Debugging Guide](DEBUGGING.md)
- [Performance Testing](PERFORMANCE_TESTING.md)
- [Async Guide](ASYNC_GUIDE.md)
