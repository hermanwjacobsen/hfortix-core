# Comprehensive Stress Test - Quick Reference

## 🎯 What is RECOMMENDED?

**RECOMMENDED = 80% of MAX**

This provides a **20% safety margin** for production environments to handle:
- Firmware upgrades that may change performance characteristics
- Other users/applications accessing the FortiGate simultaneously  
- Burst traffic scenarios
- Configuration changes that affect performance
- CPU/memory fluctuations on the FortiGate

## 📊 Example Output

### Detailed Per-Test Metrics

Each test now shows:

```
Testing max_connections=150...
  ✓ Success: 50/50 (100.0%)
  ⏱ Duration: 11.45s
  📊 Throughput: 4.37 req/s
  📈 Response Times: Avg=229.0ms, Median=225.6ms, Min=195.2ms, Max=287.1ms
  📉 Std Dev: 19.8ms, P95=265.3ms
```

**Metrics explained:**
- **Success rate** - Must be ≥95% to continue
- **Throughput** - Requests per second (higher = better)
- **Avg/Median** - Central tendency of response times
- **Min/Max** - Range of response times
- **Std Dev** - Consistency (lower = more predictable)
- **P95** - 95th percentile (95% of requests faster than this)

### Phase Results

```
================================================================================
SYNC MODE - max_connections Results:
  MAX: 150
  RECOMMENDED: 120 (80% of MAX)
  Peak Throughput: 4.37 req/s
================================================================================
```

### Final Summary

```
================================================================================
FINAL RECOMMENDATIONS - Optimal Connection Parameters
================================================================================

For PRODUCTION use, configure FortiOS client with:

  mode: 'async'
  max_connections: 160 (80% of MAX: 200)
  max_keepalive_connections: 16 (80% of MAX: 20)
  max_retries: 3
  adaptive_retry: True
  connect_timeout: 10.0
  read_timeout: 30.0

================================================================================
MAXIMUM TESTED VALUES (not recommended for production)
================================================================================

  max_connections (sync): 150 @ 4.37 req/s
  max_connections (async): 200 @ 8.12 req/s
  max_keepalive_connections: 20

================================================================================
TEST SUMMARY
================================================================================

  Total test phases: 6
  Total tests run: 23
  Best performing mode: ASYNC
  Async vs Sync improvement: +85.8% faster
  Recommendation confidence: HIGH (80% safety margin)
================================================================================
```

## 🔧 Quick Usage

```python
from hfortix.FortiOS.performance_test import comprehensive_stress_test

results = comprehensive_stress_test(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    recovery_sleep=60  # Sleep 60s between phases
)

# Copy the RECOMMENDED values to your code
```

Or use the example script:

```bash
python examples/stress_test_example.py
```

## 📈 Understanding Throughput

The difference between MAX and RECOMMENDED:

| Metric | MAX | RECOMMENDED | Notes |
|--------|-----|-------------|-------|
| **max_connections** | 200 | 160 (80%) | 40 connections reserved for headroom |
| **max_keepalive_connections** | 20 | 16 (80%) | 4 connections reserved for headroom |
| **Risk Level** | ⚠️ HIGH | ✅ LOW | MAX may cause errors under load |
| **Production Use** | ❌ Not recommended | ✅ Recommended | Safety margin included |

## 🚀 When to Use MAX vs RECOMMENDED

### Use RECOMMENDED (80% of MAX) when:
- ✅ Production environments
- ✅ Multiple users accessing FortiGate
- ✅ Long-running operations
- ✅ You need stability over peak performance
- ✅ You can't afford occasional errors

### Use MAX only when:
- ⚠️ You accept occasional errors (>5% failure rate possible)
- ⚠️ You're the only user of the API
- ⚠️ You need absolute maximum throughput
- ⚠️ You monitor and can handle failures
- ⚠️ Short-lived scripts with retry logic

## 💡 Why 80%?

Industry standard safety margin for production systems:
- **Telecom**: 80% link utilization recommended (RFC 3272)
- **Web servers**: 80% CPU/memory threshold for scaling
- **Storage**: 80% capacity before expansion
- **Networks**: 80% bandwidth before congestion

**80% provides the sweet spot** between performance and reliability!

## 📝 Test Results Data Structure

```python
results = {
    "max_values": {
        "max_connections_sync": 150,
        "max_connections_async": 200,
        "max_connections_sync_throughput": 4.37,
        "max_connections_async_throughput": 8.12,
        "max_keepalive_connections_sync": 20,
        "max_retries": 3,
    },
    "recommended_values": {
        "max_connections_sync": 120,      # 80% of 150
        "max_connections_async": 160,     # 80% of 200
        "max_keepalive_connections_sync": 16,  # 80% of 20
        "max_retries": 3,
        "adaptive_retry": True,
    },
    "test_results": {
        "max_connections_150_sync": {
            "success_rate": 100.0,
            "throughput": 4.37,
            "duration": 11.45,
            "errors": 0,
            "avg_response_ms": 229.0,
            "median_response_ms": 225.6,
            "min_response_ms": 195.2,
            "max_response_ms": 287.1,
            "stdev_ms": 19.8,
            "p95_ms": 265.3,
        },
        # ... more test results
    },
    "best_mode": "async"
}
```

## 🎓 Summary

- **RECOMMENDED = 80% of MAX** (always)
- **Detailed response time statistics** included in output
- **Peak throughput tracked** for each test
- **Error samples shown** (first 3 per test)
- **Production-ready configuration** displayed at end
- **Performance comparison** shows async vs sync improvement percentage

Use RECOMMENDED values in production for **stability and reliability** with a 20% safety margin! 🛡️
