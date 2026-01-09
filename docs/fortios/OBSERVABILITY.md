# Logging & Observability

> **Enterprise Feature**: Structured logging, distributed tracing, and observability for production systems

## Overview

hfortix provides enterprise-grade logging and observability features designed for modern distributed systems. These features help you monitor, debug, and troubleshoot your FortiGate automation at scale.

### Key Features

- **Structured Logging**: Machine-readable JSON logs for log aggregation systems
- **Distributed Tracing**: `trace_id` parameter for request correlation across services
- **Easy Configuration**: One-line setup with `configure_logging()`
- **Multiple Formats**: Text (human-readable) or JSON (machine-readable)
- **Color Output**: Optional ANSI colors for terminal debugging
- **Integration**: Works seamlessly with ELK Stack, Splunk, CloudWatch, and other log aggregators

### Why This Matters

**Production Readiness**:
- Structured logs are essential for log aggregation and analysis
- Distributed tracing enables request correlation across microservices
- Proper logging reduces MTTR (Mean Time To Resolution)

**Observability Stack Integration**:
- JSON logs feed directly into Elasticsearch, Splunk, or CloudWatch
- `trace_id` enables end-to-end request tracking
- Structured data enables powerful log queries and analytics

## Quick Start

### Basic Configuration

```python
from hfortix_fortios import FortiOS, configure_logging

# Configure logging (one time, at application startup)
configure_logging(level="INFO", format="text")

# Create client - logs automatically configured
fgt = FortiOS("192.168.1.99", token="your-token")
```

### Production Configuration (JSON)

```python
from hfortix_fortios import configure_logging, FortiOS

# Configure JSON logging for production
configure_logging(level="INFO", format="json")

# All logs now in structured JSON format
fgt = FortiOS("192.168.1.99", token="your-token")
```

**Output Example**:
```json
{"timestamp":"2026-01-02T10:30:15.123456+00:00","level":"INFO","logger":"hfortix.http","message":"Request completed successfully","request_id":"a1b2c3d4","method":"GET","endpoint":"/api/v2/monitor/system/status","status_code":200,"duration_seconds":0.234,"attempts":1}
```

## configure_logging() Function

The `configure_logging()` function is your one-stop setup for all hfortix logging.

### Signature

```python
def configure_logging(
    level: str | int = "INFO",
    format: Literal["json", "text"] = "text",
    handler: logging.Handler | None = None,
    use_color: bool = False,
) -> None:
    """Configure logging for HFortix library"""
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `level` | str\|int | `"INFO"` | Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL |
| `format` | str | `"text"` | Output format: "text" or "json" |
| `handler` | Handler | None | Custom logging handler (optional) |
| `use_color` | bool | False | Use ANSI colors in text format |

### Examples

#### Development: Colored Text Logs

```python
configure_logging(level="DEBUG", format="text", use_color=True)
```

**Output**:
```
2026-01-02 10:30:15 [DEBUG] hfortix.http: Sending GET /api/v2/monitor/system/status
2026-01-02 10:30:15 [INFO] hfortix.http: Request completed successfully
```

#### Production: JSON to File

```python
import logging

# Create file handler
file_handler = logging.FileHandler("/var/log/hfortix.json")

# Configure JSON logging to file
configure_logging(
    level="INFO",
    format="json",
    handler=file_handler
)
```

#### Production: JSON to Stdout (Container)

```python
# In containers, log to stdout for log shipper to collect
configure_logging(level="INFO", format="json")

# Logs go to stdout in JSON format
# Your log shipper (Fluentd, Filebeat, etc.) collects them
```

#### Quiet Mode (Errors Only)

```python
configure_logging(level="ERROR", format="text")
```

## Distributed Tracing with trace_id

The `trace_id` parameter enables request correlation across your entire stack.

### Basic Usage

```python
from hfortix_fortios import FortiOS

# Pass trace_id to correlate this request
fgt = FortiOS(
    "192.168.1.99",
    token="your-token",
    trace_id="req-abc-123-xyz"
)

# All API calls include this trace_id in logs
fgt.api.monitor.system.status.get()
```

**Log Output**:
```json
{
  "timestamp": "2026-01-02T10:30:15Z",
  "level": "INFO",
  "logger": "hfortix.http",
  "message": "Request completed successfully",
  "trace_id": "req-abc-123-xyz",
  "request_id": "a1b2c3d4",
  "method": "GET",
  "endpoint": "/api/v2/monitor/system/status"
}
```

### Microservices Example

```python
from flask import Flask, request
from hfortix_fortios import FortiOS

app = Flask(__name__)

@app.route('/api/firewall/address')
def create_address():
    # Extract trace_id from incoming request
    trace_id = request.headers.get('X-Trace-ID')
    
    # Pass it to FortiOS client
    fgt = FortiOS(
        "192.168.1.99",
        token="token",
        trace_id=trace_id
    )
    
    # Now you can correlate:
    # - Incoming API request (Flask)
    # - FortiGate API call (hfortix)
    # - Database queries
    # - External service calls
    result = fgt.api.cmdb.firewall.address.post(
        name="test-host",
        subnet="10.0.0.1/32"
    )
    
    return {"status": "created", "trace_id": trace_id}
```

### Kubernetes/Cloud Native

```python
import uuid
from hfortix_fortios import FortiOS

def process_firewall_request(user_request):
    # Generate trace_id for this request
    trace_id = f"req-{uuid.uuid4().hex[:16]}"
    
    # All services use same trace_id
    fgt = FortiOS(
        "192.168.1.99",
        token="token",
        trace_id=trace_id,
        user_context={
            "pod": os.getenv("HOSTNAME"),
            "namespace": "firewall-automation",
            "deployment": "policy-manager"
        }
    )
    
    return fgt.api.cmdb.firewall.policy.get()
```

## User Context for Change Management

The `user_context` parameter adds custom metadata to every log entry and audit record.

### Basic Usage

```python
fgt = FortiOS(
    "192.168.1.99",
    token="your-token",
    user_context={
        "username": "john.doe",
        "ticket": "CHG-12345",
        "app": "firewall-manager",
        "environment": "production"
    }
)
```

**Log Output**:
```json
{
  "timestamp": "2026-01-02T10:30:15Z",
  "user_context": {
    "username": "john.doe",
    "ticket": "CHG-12345",
    "app": "firewall-manager",
    "environment": "production"
  },
  "method": "POST",
  "endpoint": "/api/v2/cmdb/firewall/address"
}
```

### Use Cases

#### Change Management

```python
fgt = FortiOS(
    "192.168.1.99",
    token="token",
    user_context={
        "username": "jane.smith",
        "ticket": "CHG-67890",
        "change_type": "firewall_policy",
        "approver": "security-team",
        "scheduled_time": "2026-01-02T22:00:00Z"
    }
)
```

#### Multi-Tenant Environments

```python
fgt = FortiOS(
    "192.168.1.99",
    token="token",
    user_context={
        "tenant_id": "acme-corp",
        "tenant_name": "Acme Corporation",
        "environment": "production",
        "region": "us-west-2"
    }
)
```

#### CI/CD Pipelines

```python
fgt = FortiOS(
    "192.168.1.99",
    token="token",
    user_context={
        "pipeline": os.getenv("CI_PIPELINE_ID"),
        "commit": os.getenv("CI_COMMIT_SHA"),
        "branch": os.getenv("CI_COMMIT_BRANCH"),
        "triggered_by": os.getenv("GITLAB_USER_LOGIN"),
        "build_url": os.getenv("CI_PIPELINE_URL")
    }
)
```

## Structured Logging Formatters

### TextFormatter

Human-readable format for development and debugging.

```python
from hfortix_core.logging import TextFormatter
import logging

# Create handler with text formatter
handler = logging.StreamHandler()
handler.setFormatter(TextFormatter(use_color=True))

# Configure logging
configure_logging(handler=handler)
```

**Output**:
```
2026-01-02 10:30:15 [INFO] hfortix.http: Request completed successfully
2026-01-02 10:30:16 [WARNING] hfortix.http: Retry attempt 1 of 3
2026-01-02 10:30:17 [ERROR] hfortix.http: Request failed
```

### StructuredFormatter (JSON)

Machine-readable format for log aggregation systems.

```python
from hfortix_core.logging import StructuredFormatter
import logging

# Create handler with structured formatter
handler = logging.FileHandler("/var/log/hfortix.json")
handler.setFormatter(StructuredFormatter(pretty=False))

configure_logging(handler=handler)
```

**Output**:
```json
{"timestamp":"2026-01-02T10:30:15.123456+00:00","level":"INFO","logger":"hfortix.http","message":"Request completed successfully","request_id":"a1b2c3d4","method":"GET","endpoint":"/api/v2/monitor/system/status","status_code":200,"duration_seconds":0.234}
```

### Standard Log Fields

All structured logs automatically include these fields:

| Field | Type | Description | Always Present |
|-------|------|-------------|----------------|
| `timestamp` | string | ISO 8601 UTC timestamp | ✅ Yes |
| `level` | string | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL) | ✅ Yes |
| `logger` | string | Logger name (e.g., "hfortix.http") | ✅ Yes |
| `message` | string | Human-readable message | ✅ Yes |
| `request_id` | string | Unique request identifier for correlation | When available |
| `method` | string | HTTP method (GET, POST, PUT, DELETE, PATCH) | For requests |
| `endpoint` | string | API endpoint path | For requests |
| `status_code` | int | HTTP status code | For responses |
| `duration_seconds` | float | Request duration in seconds | For completed requests |
| `vdom` | string | FortiOS Virtual Domain (multi-tenancy) | When configured |
| `adom` | string | FortiManager/FortiAnalyzer Admin Domain | When configured (future) |
| `error_type` | string | Exception class name | For errors |
| `attempt` | int | Current retry attempt number | For retries |
| `max_attempts` | int | Maximum retry attempts | For retries |

## Multi-Tenant Logging with VDOM/ADOM

> **Enterprise Feature**: Automatic inclusion of virtual domain context in all logs

### Overview

For multi-tenant environments, hfortix automatically includes `vdom` (FortiOS Virtual Domain) or `adom` (FortiManager/FortiAnalyzer Administrative Domain) in all structured logs. This enables per-tenant observability, filtering, and compliance reporting.

### FortiOS with VDOM

```python
from hfortix_fortios import FortiOS, configure_logging

# Configure structured logging
configure_logging(level="INFO", format="json")

# Create client with VDOM
fgt = FortiOS(
    host="192.168.1.99",
    token="token",
    vdom="customer_a"  # Virtual Domain for tenant isolation
)

# Make API calls - vdom automatically included in logs
fgt.api.cmdb.firewall.policy.get()
```

**Structured Log Output**:
```json
{
  "timestamp": "2026-01-02T10:30:15.123456+00:00",
  "level": "INFO",
  "logger": "hfortix.http",
  "message": "Request completed successfully",
  "request_id": "a1b2c3d4",
  "vdom": "customer_a",
  "method": "GET",
  "endpoint": "/api/v2/cmdb/firewall/policy",
  "status_code": 200,
  "duration_seconds": 0.145,
  "attempts": 1
}
```

### Benefits for Multi-Tenant Environments

**Log Filtering by Tenant**:
```bash
# Filter logs for specific customer
jq '.vdom == "customer_a"' /var/log/hfortix.json

# Find slow requests for a tenant
jq 'select(.vdom == "customer_a" and .duration_seconds > 2.0)' /var/log/hfortix.json

# Count requests by VDOM
jq -r '.vdom // "root"' /var/log/hfortix.json | sort | uniq -c
```

**ELK Stack Integration**:
```
# Elasticsearch query
GET /logs-hfortix-*/_search
{
  "query": {
    "bool": {
      "must": [
        {"term": {"vdom": "customer_a"}},
        {"range": {"duration_seconds": {"gte": 1.0}}}
      ]
    }
  }
}

# Kibana dashboard
- Group by: vdom
- Metric: Average duration_seconds
- Filter: status_code >= 400
```

**Splunk Integration**:
```
# Splunk search
source="hfortix" vdom="customer_a" status_code>=400
| stats count by endpoint, method
| sort -count

# Per-tenant metrics
index=hfortix
| stats avg(duration_seconds) as avg_duration, 
        count as total_requests by vdom
| sort -total_requests
```

**CloudWatch Logs Insights**:
```
# CloudWatch query
fields @timestamp, vdom, endpoint, duration_seconds, status_code
| filter vdom = "customer_a"
| filter status_code >= 400
| sort duration_seconds desc
```

### Future: FortiManager/FortiAnalyzer with ADOM

The infrastructure is ready for future FortiManager/FortiAnalyzer clients:

```python
# Future implementation
from hfortix_fortimanager import FortiManager

fmg = FortiManager(
    host="192.168.1.100",
    token="token",
    adom="root"  # Administrative Domain
)

# Logs will automatically include adom field
fmg.api.dvmdb.device.get()
```

**Expected Output**:
```json
{
  "timestamp": "2026-01-02T10:30:15.123456+00:00",
  "level": "INFO",
  "logger": "hfortix.http",
  "message": "Request completed successfully",
  "request_id": "xyz123",
  "adom": "root",
  "method": "GET",
  "endpoint": "/api/v2/dvmdb/device",
  "status_code": 200
}
```

### Use Cases

**1. Multi-Customer MSP (Managed Service Provider)**:
```python
# Different VDOM per customer
customers = {
    "acme": FortiOS(host="...", token="...", vdom="acme-corp"),
    "contoso": FortiOS(host="...", token="...", vdom="contoso-ltd"),
    "fabrikam": FortiOS(host="...", token="...", vdom="fabrikam-inc")
}

# Each customer's logs are isolated by vdom
for name, client in customers.items():
    policies = client.api.cmdb.firewall.policy.get()
    # Logs include vdom for each customer
```

**2. Compliance Reporting per Tenant**:
```python
# Export audit logs filtered by VDOM
fgt = FortiOS(host="...", token="...", vdom="customer_a", track_operations=True)

# ... perform operations ...

# Export audit trail for this tenant only
audit_logs = fgt.export_audit_logs(format="json")
# All operations tagged with vdom="customer_a"
```

**3. Performance Monitoring per Tenant**:
```python
# Monitor health metrics by VDOM
fgt = FortiOS(host="...", token="...", vdom="customer_b")

metrics = fgt.get_health_metrics()
# Analyze which tenants have slow requests or high retry rates
# Logs include vdom for correlation
```

### Best Practices

1. **Always specify VDOM** in multi-tenant environments:
   ```python
   fgt = FortiOS(host="...", token="...", vdom="customer_a")
   ```

2. **Use structured logging** for multi-tenant deployments:
   ```python
   configure_logging(format="json")  # Enable structured logs
   ```

3. **Index by VDOM** in log aggregation systems:
   - Elasticsearch: Create separate indices per VDOM
   - Splunk: Use VDOM as a source type or indexed field
   - CloudWatch: Add VDOM as a dimension

4. **Monitor per-tenant metrics**:
   - Track request counts by VDOM
   - Alert on per-tenant error rates
   - Dashboard showing per-customer performance

**Pretty-Printed** (development):
```python
handler.setFormatter(StructuredFormatter(pretty=True, indent=2))
```

```json
{
  "timestamp": "2026-01-02T10:30:15.123456+00:00",
  "level": "INFO",
  "logger": "hfortix.http",
  "message": "Request completed successfully",
  "request_id": "a1b2c3d4",
  "method": "GET",
  "endpoint": "/api/v2/monitor/system/status"
}
```

## Integration Examples

### ELK Stack (Elasticsearch, Logstash, Kibana)

```python
from hfortix_fortios import configure_logging, FortiOS
import logging

# Configure JSON logging
configure_logging(level="INFO", format="json")

# Create client with context
fgt = FortiOS(
    "192.168.1.99",
    token="token",
    trace_id="req-abc-123",
    user_context={
        "service": "firewall-automation",
        "version": "1.2.3",
        "environment": "production"
    }
)

# Logs automatically flow to Filebeat → Logstash → Elasticsearch
# Query in Kibana: trace_id:"req-abc-123"
```

**Filebeat Configuration**:
```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/hfortix.json
  json.keys_under_root: true
  json.add_error_key: true

output.logstash:
  hosts: ["logstash:5044"]
```

### Splunk

```python
from hfortix_fortios import configure_logging, FortiOS
import logging

# Configure JSON logging to file
file_handler = logging.FileHandler("/var/log/hfortix/app.json")
configure_logging(format="json", handler=file_handler)

# Splunk Universal Forwarder monitors /var/log/hfortix/
fgt = FortiOS(
    "192.168.1.99",
    token="token",
    user_context={"splunk_index": "firewall"}
)
```

**Splunk Query**:
```
index=firewall sourcetype=hfortix trace_id="req-abc-123"
```

### AWS CloudWatch Logs

```python
from hfortix_fortios import configure_logging, FortiOS
import watchtower
import logging

# Configure CloudWatch handler
cloudwatch_handler = watchtower.CloudWatchLogHandler(
    log_group="/aws/ecs/firewall-automation",
    stream_name="hfortix"
)

configure_logging(
    level="INFO",
    format="json",
    handler=cloudwatch_handler
)

fgt = FortiOS(
    "192.168.1.99",
    token="token",
    trace_id="req-abc-123",
    user_context={
        "task_arn": os.getenv("ECS_TASK_ARN"),
        "cluster": os.getenv("ECS_CLUSTER")
    }
)
```

### Google Cloud Logging (Stackdriver)

```python
from hfortix_fortios import configure_logging, FortiOS
import google.cloud.logging

# Configure Cloud Logging
client = google.cloud.logging.Client()
handler = client.get_default_handler()

configure_logging(
    level="INFO",
    format="json",
    handler=handler
)

fgt = FortiOS(
    "192.168.1.99",
    token="token",
    trace_id="req-abc-123",
    user_context={
        "project_id": "my-gcp-project",
        "service": "firewall-automation"
    }
)
```

### Datadog

```python
from hfortix_fortios import configure_logging, FortiOS
from ddtrace import tracer
import logging

# Configure JSON logging
configure_logging(level="INFO", format="json")

# Get Datadog trace context
trace_id = tracer.current_span().trace_id if tracer.current_span() else None

fgt = FortiOS(
    "192.168.1.99",
    token="token",
    trace_id=f"dd-{trace_id}",
    user_context={
        "dd_service": "firewall-automation",
        "dd_env": "production"
    }
)
```

## Complete Production Example

```python
"""
Production-ready FortiGate automation with full observability
"""
from hfortix_fortios import configure_logging, FortiOS
from hfortix_core.audit import FileHandler
import logging
import uuid
import os

# ============================================================================
# 1. Configure Logging (Application Startup)
# ============================================================================

# JSON logging to file for log shipper
log_file = "/var/log/hfortix/app.json"
file_handler = logging.FileHandler(log_file)

configure_logging(
    level="INFO",
    format="json",
    handler=file_handler
)

# ============================================================================
# 2. Configure Audit Logging
# ============================================================================

audit_handler = FileHandler("/var/log/hfortix/audit.jsonl")

# ============================================================================
# 3. Create FortiGate Client with Full Context
# ============================================================================

def create_fortios_client(request_context: dict):
    """Create FortiOS client with full observability context"""
    
    # Generate or extract trace_id
    trace_id = request_context.get('trace_id') or f"req-{uuid.uuid4().hex[:16]}"
    
    # Build user context
    user_context = {
        "username": request_context.get("username", "unknown"),
        "ticket": request_context.get("ticket"),
        "environment": os.getenv("ENVIRONMENT", "production"),
        "service": "firewall-automation",
        "version": "1.0.0",
        "pod_name": os.getenv("HOSTNAME"),
        "namespace": os.getenv("K8S_NAMESPACE", "default"),
    }
    
    # Remove None values
    user_context = {k: v for k, v in user_context.items() if v is not None}
    
    # Create client
    return FortiOS(
        host=os.getenv("FORTIGATE_HOST"),
        token=os.getenv("FORTIGATE_TOKEN"),
        verify=True,  # Always verify in production
        audit_handler=audit_handler,
        trace_id=trace_id,
        user_context=user_context
    )

# ============================================================================
# 4. Use in Application
# ============================================================================

def create_firewall_address(name: str, subnet: str, username: str, ticket: str):
    """Create firewall address with full observability"""
    
    # Create client with context
    fgt = create_fortios_client({
        "username": username,
        "ticket": ticket
    })
    
    # Execute operation - automatically logged with full context
    result = fgt.api.cmdb.firewall.address.post(
        name=name,
        subnet=subnet,
        comment=f"Created via ticket {ticket}"
    )
    
    return result

# Example usage
if __name__ == "__main__":
    create_firewall_address(
        name="test-server",
        subnet="10.0.0.100/32",
        username="john.doe",
        ticket="CHG-12345"
    )
```

**Resulting Logs**:

Application Log (`/var/log/hfortix/app.json`):
```json
{"timestamp":"2026-01-02T10:30:15.123456+00:00","level":"INFO","logger":"hfortix.http","message":"Request completed successfully","trace_id":"req-abc123def456","request_id":"a1b2c3d4","method":"POST","endpoint":"/api/v2/cmdb/firewall/address","status_code":200,"duration_seconds":0.234,"user_context":{"username":"john.doe","ticket":"CHG-12345","environment":"production","service":"firewall-automation"}}
```

Audit Log (`/var/log/hfortix/audit.jsonl`):
```json
{"timestamp":"2026-01-02T10:30:15.123456+00:00","trace_id":"req-abc123def456","request_id":"a1b2c3d4","method":"POST","api_type":"cmdb","path":"/api/v2/cmdb/firewall/address","action":"create","object_type":"firewall.address","object_name":"test-server","data":{"name":"test-server","subnet":"10.0.0.100/32","comment":"Created via ticket CHG-12345"},"status_code":200,"success":true,"duration_ms":234,"host":"192.168.1.99","vdom":"root","user_context":{"username":"john.doe","ticket":"CHG-12345","environment":"production","service":"firewall-automation"}}
```

## Best Practices

### 1. Configure Once at Startup

```python
# ✅ Good: Configure at application startup
if __name__ == "__main__":
    configure_logging(level="INFO", format="json")
    main()

# ❌ Bad: Configuring in every function
def process_request():
    configure_logging(...)  # Don't do this
```

### 2. Use JSON in Production

```python
# ✅ Production: JSON format
configure_logging(level="INFO", format="json")

# ✅ Development: Text with colors
configure_logging(level="DEBUG", format="text", use_color=True)
```

### 3. Always Include trace_id in Distributed Systems

```python
# ✅ Good: Propagate trace_id
def handle_request(request):
    trace_id = request.headers.get('X-Trace-ID') or generate_trace_id()
    fgt = FortiOS("host", token="token", trace_id=trace_id)
    
# ❌ Bad: No trace_id
def handle_request(request):
    fgt = FortiOS("host", token="token")  # Can't correlate across services
```

### 4. Include Meaningful User Context

```python
# ✅ Good: Rich context
user_context = {
    "username": "john.doe",
    "ticket": "CHG-12345",
    "app": "firewall-manager",
    "environment": "production",
    "region": "us-west-2"
}

# ❌ Bad: Minimal context
user_context = {"user": "john"}
```

### 5. Use Different Log Levels Appropriately

```python
# DEBUG: Detailed debugging info
configure_logging(level="DEBUG")  # Development only

# INFO: General operational events
configure_logging(level="INFO")  # Production default

# WARNING: Important but non-critical issues
configure_logging(level="WARNING")  # Production (quiet mode)

# ERROR: Error events
configure_logging(level="ERROR")  # Production (minimal logging)
```

## Troubleshooting

### No Logs Appearing

**Problem**: Configured logging but seeing no output.

**Solution**:
```python
# Verify logging is configured
import logging
logging.getLogger("hfortix").setLevel(logging.DEBUG)

# Check handlers
logger = logging.getLogger("hfortix")
print(logger.handlers)  # Should not be empty
```

### Logs Not in JSON Format

**Problem**: Using `format="json"` but logs are still text.

**Solution**:
```python
# Ensure you're using configure_logging from hfortix_fortios
from hfortix_fortios import configure_logging  # ✅ Correct

# Not from Python's logging module
import logging
logging.basicConfig(...)  # ❌ Wrong - won't use our formatters
```

### trace_id Not Appearing in Logs

**Problem**: Set `trace_id` but it's not in log output.

**Solution**:
```python
# trace_id only appears in structured (JSON) logs
configure_logging(format="json")  # Required for trace_id

# Text format doesn't include trace_id by default
configure_logging(format="text")  # Won't show trace_id
```

### Duplicate Log Entries

**Problem**: Seeing duplicate log messages.

**Solution**:
```python
# Don't call configure_logging multiple times
# Call once at application startup

# If you need to change config, remove existing handlers first
logger = logging.getLogger("hfortix")
logger.handlers.clear()
configure_logging(...)
```

## See Also

- [Audit Logging Guide](AUDIT_LOGGING.md) - Enterprise audit logging for compliance
- [Error Handling Configuration](ERROR_HANDLING_CONFIG.md) - Error handling modes
- [API Reference](../docs/source/fortios/api-reference/index.rst) - Complete API documentation
- [Examples](../../examples/) - Working code examples

## Summary

✅ **You now know how to**:
- Configure structured logging with `configure_logging()`
- Use `trace_id` for distributed tracing
- Add `user_context` for change management
- Integrate with ELK, Splunk, CloudWatch, and other log aggregators
- Build production-ready observability into your FortiGate automation

🎯 **Next Steps**:
1. Configure logging in your application startup
2. Add `trace_id` to your API requests
3. Set up log aggregation (ELK, Splunk, etc.)
4. Add `user_context` for compliance tracking
5. Monitor your logs in production

📊 **Production Checklist**:
- [ ] JSON logging configured (`format="json"`)
- [ ] Log level set appropriately (`INFO` or `WARNING`)
- [ ] `trace_id` propagated from incoming requests
- [ ] `user_context` includes username, ticket, environment
- [ ] Logs flowing to aggregation system (ELK/Splunk/CloudWatch)
- [ ] Audit logging configured (see [AUDIT_LOGGING.md](AUDIT_LOGGING.md))
- [ ] Alerts configured for ERROR level logs
