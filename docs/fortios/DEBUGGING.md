# Debugging Guide

This guide covers HFortix's comprehensive debugging and observability features for troubleshooting API interactions and performance issues.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Debug Mode](#debug-mode)
- [Connection Statistics](#connection-statistics)
- [Request Inspection](#request-inspection)
- [Debug Session](#debug-session)
- [Logging Configuration](#logging-configuration)
- [Performance Profiling](#performance-profiling)
- [Common Debugging Scenarios](#common-debugging-scenarios)

## Overview

HFortix provides multiple debugging tools:

- **Debug Mode**: Automatic detailed logging
- **Connection Stats**: Real-time pool metrics
- **Request Inspection**: Last request details
- **Debug Session**: Comprehensive session monitoring
- **Structured Logging**: JSON logs for aggregation
- **Performance Profiling**: Timing and metrics

## Quick Start

### Enable Debug Logging

```python
from hfortix_fortios import FortiOS

# Quick debug mode - boolean
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    debug=True,  # Enables DEBUG level logging
)

# Or specify log level as string
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    debug="INFO",  # INFO, DEBUG, WARNING, ERROR
)
```

### Check Last Request

```python
# Make some API calls
fgt.api.cmdb.firewall.address.get()

# Inspect last request
info = fgt.last_request
print(f"Method: {info['method']}")
print(f"Endpoint: {info['endpoint']}")
print(f"Response time: {info['response_time_ms']:.1f}ms")
print(f"Status: {info['status_code']}")
```

### Monitor Connection Pool

```python
# Get connection statistics
stats = fgt.connection_stats
print(f"Active: {stats['active_requests']}")
print(f"Total: {stats['total_requests']}")
print(f"Pool exhaustion: {stats['pool_exhaustion_count']}")
```

## Debug Mode

### Boolean Debug Mode

Enable debug logging with a simple boolean:

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    debug=True,  # Automatically sets level to DEBUG
)
```

**Output:**
```
DEBUG:hfortix.http:→ GET /api/v2/cmdb/firewall/address
DEBUG:hfortix.http:← 200 OK (123.4ms)
```

### String Debug Level

Specify exact log level:

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    debug="INFO",  # INFO, DEBUG, WARNING, ERROR, OFF
)
```

### Debug Options

Pass additional debug configuration:

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    debug=True,
    debug_options={
        "include_headers": True,
        "include_body": True,
        "max_body_size": 1000,
    },
)
```

## Connection Statistics

### Real-Time Metrics

Monitor connection pool health:

```python
stats = fgt.connection_stats

print(f"Max Connections: {stats['max_connections']}")
print(f"Max Keepalive: {stats['max_keepalive_connections']}")
print(f"Active Requests: {stats['active_requests']}")
print(f"Total Requests: {stats['total_requests']}")
print(f"Pool Exhaustion Count: {stats['pool_exhaustion_count']}")

# Check exhaustion timestamps
if stats['pool_exhaustion_timestamps']:
    print(f"Last exhaustion: {stats['pool_exhaustion_timestamps'][-1]}")
```

### Formatted Output

Use helper functions for pretty printing:

```python
from hfortix_fortios import format_connection_stats

# Pretty print connection stats
print(format_connection_stats(fgt.connection_stats))
```

**Output:**
```
Connection Pool Statistics
==================================================
Max Connections: 100
Max Keepalive: 20
Active Requests: 2
Total Requests: 1543
Pool Exhaustion Events: 0
```

### Detecting Pool Issues

```python
stats = fgt.connection_stats

# Check if pool is saturated
utilization = stats['active_requests'] / stats['max_connections']
if utilization > 0.8:
    print(f"WARNING: Pool at {utilization:.1%} capacity")

# Check for frequent exhaustion
if stats['pool_exhaustion_count'] > 10:
    print("WARNING: Consider increasing max_connections")
```

## Request Inspection

### Last Request Details

Get detailed information about the most recent API call:

```python
# Make API call
result = fgt.api.cmdb.firewall.address.get()

# Inspect last request
info = fgt.last_request

if info:
    print(f"Method: {info['method']}")  # GET, POST, PUT, DELETE
    print(f"Endpoint: {info['endpoint']}")  # /api/v2/cmdb/firewall/address
    print(f"Params: {info['params']}")  # Query parameters
    print(f"Response Time: {info['response_time_ms']:.1f}ms")
    print(f"Status Code: {info['status_code']}")  # 200, 404, etc.
```

### Formatted Request Info

```python
from hfortix_fortios import format_request_info

# Pretty print last request
print(format_request_info(fgt.last_request))
```

**Output:**
```
GET /api/v2/cmdb/firewall/address
Params: {"vdom": "root"}
Response Time: 123.4ms
Status Code: 200
```

### Tracking Request Performance

```python
# Make multiple requests and track performance
requests = []

for i in range(10):
    fgt.api.cmdb.firewall.address.get(filter=f"name=@NET_{i}")
    requests.append(fgt.last_request.copy())

# Analyze performance
avg_time = sum(r['response_time_ms'] for r in requests) / len(requests)
max_time = max(r['response_time_ms'] for r in requests)
min_time = min(r['response_time_ms'] for r in requests)

print(f"Average: {avg_time:.1f}ms")
print(f"Max: {max_time:.1f}ms")
print(f"Min: {min_time:.1f}ms")
```

## Debug Session

### Comprehensive Session Monitoring

Use `DebugSession` context manager for detailed session analysis:

```python
from hfortix_fortios import FortiOS, DebugSession

fgt = FortiOS(host="192.168.1.99", token="your-token")

# Monitor entire session
with DebugSession(fgt) as session:
    # Make API calls
    fgt.api.cmdb.firewall.address.get()
    fgt.api.cmdb.firewall.policy.get()
    
    # Auto-prints summary on exit
```

**Output:**
```
Debug Session Summary
============================================================
Duration: 1.234s
Total Requests: 2
Successful: 2
Failed: 0
Average Response Time: 617.0ms
Max Response Time: 743.2ms
Min Response Time: 490.8ms

Connection Pool Delta:
  Requests Made: 2
  Pool Exhaustions: 0
  Active Requests Change: 0

Final Connection Stats:
  Active Requests: 0
  Total Requests: 2
  Pool Exhaustion Count: 0
```

### Capture Response Data

Capture full API responses for analysis:

```python
with DebugSession(fgt, capture_response_data=True) as session:
    result = fgt.api.cmdb.firewall.address.get()
    
    # Don't auto-print
    session.print_on_exit = False

# Access captured data
session.print_requests(verbose=True)
```

### Manual Session Control

```python
# Don't auto-print summary
with DebugSession(fgt, print_on_exit=False) as session:
    fgt.api.cmdb.firewall.address.get()
    fgt.api.cmdb.firewall.policy.get()
    
    # Print custom summary
    summary = session.get_summary()
    print(f"Completed {summary['total_requests']} requests")
    print(f"Average time: {summary['avg_response_time_ms']:.1f}ms")
    
    # Print JSON format
    session.print_summary(format="json")
```

### Performance Analysis

```python
with DebugSession(fgt) as session:
    # Run operations
    for i in range(100):
        fgt.api.cmdb.firewall.address.get(filter=f"name=@NET_{i}")
    
    summary = session.get_summary()
    
    # Identify performance issues
    if summary['avg_response_time_ms'] > 500:
        print("WARNING: Slow responses detected")
    
    if summary['stats_delta']['pool_exhaustions'] > 0:
        print("WARNING: Pool exhaustion occurred")
```

## Logging Configuration

### Global Logging Setup

Configure logging for the entire library:

```python
from hfortix_fortios import configure_logging

# Text logging with colors
configure_logging(
    level="DEBUG",
    format="text",
    use_color=True,
)

# JSON logging for log aggregation
configure_logging(
    level="INFO",
    format="json",
)

# Log to file
configure_logging(
    level="DEBUG",
    format="json",
    output_file="/var/log/hfortix.log",
)

# Structured logging with request tracing
configure_logging(
    level="INFO",
    format="json",
    include_trace=True,  # Add request_id to all logs
    structured=True,  # Include extra metadata
)
```

### Per-Instance Logging

Override logging for specific client:

```python
# Global config
configure_logging(level="INFO")

# This instance has DEBUG logging
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    debug="DEBUG",  # Override global level
)
```

### Custom Log Handler

```python
import logging
from hfortix_fortios import configure_logging

# Create custom handler
handler = logging.FileHandler("/var/log/fortios-api.log")

configure_logging(
    level="INFO",
    handler=handler,
)
```

### Structured Logging Example

```python
configure_logging(
    level="INFO",
    format="json",
    include_trace=True,
)

# Logs will include:
# {"timestamp": "...", "level": "INFO", "message": "...", "request_id": "..."}
```

## Performance Profiling

### Debug Timer

Time individual operations:

```python
from hfortix_fortios import debug_timer

with debug_timer("Get firewall addresses") as timing:
    result = fgt.api.cmdb.firewall.address.get()

print(f"Took {timing['duration_ms']:.1f}ms")
```

**Output:**
```
Get firewall addresses: 123.4ms
```

### Batch Operation Profiling

```python
from hfortix_fortios import debug_timer, DebugSession

with DebugSession(fgt) as session:
    with debug_timer("Create 100 addresses"):
        for i in range(100):
            fgt.api.cmdb.firewall.address.post(data={
                "name": f"NET_{i}",
                "subnet": f"10.0.{i}.0/24",
            })
    
    # Session summary includes detailed metrics
```

### Comparing Performance

```python
# Test different configurations
configs = [
    {"max_connections": 10, "label": "Low"},
    {"max_connections": 50, "label": "Medium"},
    {"max_connections": 100, "label": "High"},
]

for config in configs:
    fgt = FortiOS(
        host="192.168.1.99",
        token="your-token",
        max_connections=config['max_connections'],
    )
    
    with debug_timer(f"Config: {config['label']}"):
        for i in range(50):
            fgt.api.cmdb.firewall.address.get()
```

## Common Debugging Scenarios

### Scenario 1: Slow API Responses

```python
# Enable detailed logging
fgt = FortiOS(host="192.168.1.99", token="your-token", debug=True)

# Monitor request performance
result = fgt.api.cmdb.firewall.address.get()
info = fgt.last_request

if info['response_time_ms'] > 1000:
    print(f"Slow request: {info['response_time_ms']:.1f}ms")
    print(f"Endpoint: {info['endpoint']}")
    
    # Check connection stats
    stats = fgt.connection_stats
    if stats['active_requests'] > stats['max_connections'] * 0.8:
        print("Pool saturation may be causing slowdown")
```

### Scenario 2: Connection Pool Exhaustion

```python
from hfortix_fortios import FortiOS, print_debug_info

fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_connections=10,  # Intentionally low
)

# Make many concurrent requests
for i in range(20):
    fgt.api.cmdb.firewall.address.get()

# Check for exhaustion
print_debug_info(fgt)

# Output will show pool_exhaustion_count > 0
```

**Solution:**
```python
# Increase pool size
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_connections=50,  # Increased
)
```

### Scenario 3: Debugging Failed Requests

```python
from hfortix_fortios import FortiOS, format_request_info
from hfortix_core import APIError

fgt = FortiOS(host="192.168.1.99", token="your-token", debug=True)

try:
    fgt.api.cmdb.firewall.address.post(data={"invalid": "data"})
except APIError as e:
    print(f"API Error: {e}")
    
    # Inspect failed request
    print(format_request_info(fgt.last_request))
    
    # Check logs for detailed error
```

### Scenario 4: Performance Regression

```python
from hfortix_fortios import FortiOS, DebugSession

# Baseline measurement
fgt = FortiOS(host="192.168.1.99", token="your-token")

with DebugSession(fgt) as session:
    for i in range(100):
        fgt.api.cmdb.firewall.address.get()
    
    baseline = session.get_summary()

# After code changes, compare
with DebugSession(fgt) as session:
    for i in range(100):
        fgt.api.cmdb.firewall.address.get()
    
    current = session.get_summary()

# Compare
print(f"Baseline avg: {baseline['avg_response_time_ms']:.1f}ms")
print(f"Current avg: {current['avg_response_time_ms']:.1f}ms")

if current['avg_response_time_ms'] > baseline['avg_response_time_ms'] * 1.2:
    print("WARNING: 20%+ performance regression")
```

### Scenario 5: Rate Limiting Investigation

```python
from hfortix_fortios import FortiOS, DebugSession
from hfortix_core import RateLimitError

fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
    max_retries=0,  # Disable auto-retry to see rate limits
)

rate_limited = 0

with DebugSession(fgt) as session:
    for i in range(100):
        try:
            fgt.api.cmdb.firewall.address.get()
        except RateLimitError:
            rate_limited += 1

print(f"Rate limited: {rate_limited}/100 requests")
print(f"Adjust request rate or enable retries")
```

## Integration with Observability Tools

### ELK Stack

```python
from hfortix_fortios import configure_logging
import logging

# Configure for Elasticsearch
configure_logging(
    level="INFO",
    format="json",
    include_trace=True,
    output_file="/var/log/hfortix/api.log",
)

# Use filebeat to ship logs to Elasticsearch
```

### Splunk

```python
# Splunk HEC (HTTP Event Collector)
import logging
from hfortix_fortios import configure_logging

# Create Splunk handler (requires splunk-handler package)
from splunk_handler import SplunkHandler

splunk = SplunkHandler(
    host='splunk.example.com',
    port=8088,
    token='your-hec-token',
)

configure_logging(
    level="INFO",
    format="json",
    handler=splunk,
)
```

### CloudWatch

```python
# AWS CloudWatch Logs
import boto3
import logging
from hfortix_fortios import configure_logging

# Use watchtower for CloudWatch integration
from watchtower import CloudWatchLogHandler

cloudwatch = CloudWatchLogHandler(
    log_group='/aws/hfortix',
    stream_name='fortios-api',
)

configure_logging(
    level="INFO",
    format="json",
    handler=cloudwatch,
)
```

## Best Practices

1. **Enable Debug Mode During Development**
   ```python
   fgt = FortiOS(host="...", token="...", debug=True)
   ```

2. **Use JSON Logging in Production**
   ```python
   configure_logging(level="INFO", format="json", include_trace=True)
   ```

3. **Monitor Connection Pool Health**
   ```python
   stats = fgt.connection_stats
   if stats['pool_exhaustion_count'] > 0:
       # Investigate and increase max_connections
   ```

4. **Use DebugSession for Performance Testing**
   ```python
   with DebugSession(fgt) as session:
       # Run operations
       session.print_summary()
   ```

5. **Inspect Failed Requests**
   ```python
   try:
       fgt.api.cmdb.firewall.address.post(data=...)
   except APIError:
       print(format_request_info(fgt.last_request))
   ```

## See Also

- [Rate Limiting Guide](RATE_LIMITING.md)
- [Error Handling Guide](ERROR_HANDLING_CONFIG.md)
- [Performance Testing](PERFORMANCE_TESTING.md)
- [Observability Guide](OBSERVABILITY.md)
