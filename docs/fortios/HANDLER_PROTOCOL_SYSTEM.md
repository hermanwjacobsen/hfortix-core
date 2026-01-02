# Handler Protocol System

> **Extensibility Architecture**: Build custom handlers to extend HFortix functionality

## Overview

HFortix uses a **protocol-based handler system** that allows you to extend SDK functionality without modifying core code. This architecture enables:

- **Custom audit logging** to any destination
- **Real-time notifications** (Slack, Teams, email)
- **Data integration** (Kafka, databases, data lakes)
- **Custom workflows** (approval systems, rollback logic)
- **Compliance automation** (automatic ticket creation, approval checks)

### Why Protocol-Based?

Unlike traditional inheritance-based plugins, protocols are:

- ✅ **Zero coupling**: No dependency on HFortix base classes
- ✅ **Duck typing**: If it implements `log_operation()`, it works
- ✅ **Type safe**: Full IDE autocomplete and type checking
- ✅ **Simple**: Just implement one method
- ✅ **Testable**: Mock handlers easily

## Quick Start

### Your First Custom Handler

```python
from typing import Any
from hfortix import FortiOS

class SlackNotifier:
    """Send notifications to Slack when firewall rules change"""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Called after every API operation"""
        # Only notify on firewall policy changes
        if 'firewall.policy' in operation.get('object_type', ''):
            action = operation['action']
            user = operation.get('user_context', {}).get('username', 'Unknown')
            object_name = operation.get('object_name', 'N/A')
            
            message = f"🔥 Firewall changed by {user}: {action} {object_name}"
            self._send_to_slack(message)
    
    def _send_to_slack(self, message: str):
        import requests
        requests.post(self.webhook_url, json={"text": message})

# Use it
handler = SlackNotifier("https://hooks.slack.com/services/YOUR/WEBHOOK")
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

# Now all firewall policy changes trigger Slack notifications
fgt.api.cmdb.firewall.policy.create(
    name="Block-Malware",
    srcintf="internal",
    dstintf="wan1",
    action="deny"
)
# → Slack: "🔥 Firewall changed by admin: create Block-Malware"
```

## Handler Protocol Definition

### The AuditHandler Protocol

Every handler must implement this protocol:

```python
from typing import Any, Protocol, runtime_checkable

@runtime_checkable
class AuditHandler(Protocol):
    """
    Protocol for audit log handlers
    
    Any class implementing this protocol can be used as an audit handler.
    No inheritance required - just implement log_operation().
    """
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """
        Called after every API operation (success or failure)
        
        Args:
            operation: Dictionary with operation details
        
        Notes:
            - Should NOT raise exceptions (use try/except internally)
            - Failed handlers don't break API operations
            - Called in request thread - keep it fast or use async processing
        """
        ...
```

### Operation Data Structure

The `operation` dictionary contains:

```python
{
    # When & Who
    "timestamp": "2026-01-02T14:35:22.123456+00:00",  # ISO 8601 UTC
    "request_id": "a1b2c3d4-e5f6-7890",               # Unique ID
    "user_context": {                                  # Your custom metadata
        "username": "john.doe",
        "ticket": "CHG-12345",
        "service": "automation-bot"
    },
    
    # What & Where
    "method": "POST",                                  # GET, POST, PUT, DELETE
    "endpoint": "/api/v2/cmdb/firewall/policy",        # Full path
    "api_type": "cmdb",                                # cmdb, monitor, log
    "path": "firewall/policy",                         # Relative path
    "vdom": "root",                                    # Virtual domain
    
    # Action & Object
    "action": "create",                                # create, update, delete, read, list
    "object_type": "firewall.policy",                  # Resource type
    "object_name": "Allow-HTTPS",                      # Resource name (if available)
    
    # Request Data
    "data": {                                          # Request payload (sanitized)
        "name": "Allow-HTTPS",
        "srcintf": "internal",
        "action": "accept",
        # Note: passwords/tokens automatically redacted
    },
    "params": {                                        # Query parameters
        "vdom": "root"
    },
    
    # Result
    "status_code": 200,                                # HTTP status
    "success": True,                                   # True/False
    "duration_ms": 145,                                # Milliseconds
    "error": None,                                     # Error message if failed
    
    # Context
    "host": "192.168.1.99",                           # FortiGate IP
    "read_only_mode": False                           # True if simulated
}
```

## Built-in Handlers

HFortix includes production-ready handlers:

| Handler           | Use Case              | Destination                      |
| ----------------- | --------------------- | -------------------------------- |
| `FileHandler`     | Local audit trail     | JSON Lines file (auto-rotation)  |
| `SyslogHandler`   | SIEM integration      | Syslog server (RFC 5424)         |
| `StreamHandler`   | Container logs        | stdout/stderr                    |
| `CompositeHandler`| Multiple destinations | Routes to other handlers         |
| `NullHandler`     | Disable auditing      | No-op                            |

See [AUDIT_LOGGING.md](./AUDIT_LOGGING.md) for details.

## Custom Handler Examples

### Example 1: Database Logger

Store audit trail in PostgreSQL for long-term compliance:

```python
import psycopg2
from typing import Any

class DatabaseHandler:
    """Store audit logs in PostgreSQL"""
    
    def __init__(self, connection_string: str):
        self.conn_string = connection_string
        self._setup_table()
    
    def _setup_table(self):
        """Create audit_log table if doesn't exist"""
        with psycopg2.connect(self.conn_string) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS audit_log (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP WITH TIME ZONE,
                    request_id VARCHAR(50),
                    username VARCHAR(100),
                    action VARCHAR(20),
                    object_type VARCHAR(100),
                    object_name VARCHAR(255),
                    method VARCHAR(10),
                    endpoint TEXT,
                    status_code INTEGER,
                    success BOOLEAN,
                    duration_ms INTEGER,
                    data JSONB,
                    error TEXT
                )
            """)
            conn.commit()
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Insert operation into database"""
        try:
            user_context = operation.get('user_context', {})
            
            with psycopg2.connect(self.conn_string) as conn:
                conn.execute("""
                    INSERT INTO audit_log 
                    (timestamp, request_id, username, action, object_type, 
                     object_name, method, endpoint, status_code, success, 
                     duration_ms, data, error)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    operation['timestamp'],
                    operation['request_id'],
                    user_context.get('username'),
                    operation['action'],
                    operation['object_type'],
                    operation.get('object_name'),
                    operation['method'],
                    operation['endpoint'],
                    operation['status_code'],
                    operation['success'],
                    operation['duration_ms'],
                    psycopg2.extras.Json(operation.get('data')),
                    operation.get('error')
                ))
                conn.commit()
        except Exception as e:
            # Don't raise - just log the error
            import logging
            logging.error(f"Database audit failed: {e}")

# Usage
handler = DatabaseHandler("postgresql://user:pass@localhost/audit_db")
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

### Example 2: Kafka Publisher

Stream audit events to Kafka for real-time analytics:

```python
from kafka import KafkaProducer
import json
from typing import Any

class KafkaHandler:
    """Publish audit events to Kafka topic"""
    
    def __init__(self, bootstrap_servers: list[str], topic: str = "fortinet-audit"):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Publish operation to Kafka"""
        try:
            # Use request_id as partition key for ordering
            key = operation['request_id'].encode('utf-8')
            self.producer.send(self.topic, value=operation, key=key)
        except Exception as e:
            import logging
            logging.error(f"Kafka publish failed: {e}")
    
    def close(self):
        """Flush and close producer"""
        self.producer.flush()
        self.producer.close()

# Usage
handler = KafkaHandler(["kafka1:9092", "kafka2:9092"])
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

# Process events from Kafka
from kafka import KafkaConsumer
consumer = KafkaConsumer('fortinet-audit', bootstrap_servers=["kafka1:9092"])
for message in consumer:
    event = json.loads(message.value)
    print(f"Event: {event['action']} on {event['object_type']}")
```

### Example 3: Approval System

Block dangerous operations pending approval:

```python
from typing import Any

class ApprovalHandler:
    """Require approval for dangerous operations"""
    
    def __init__(self, approval_webhook: str):
        self.webhook = approval_webhook
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Check if operation needs post-approval"""
        # Flag dangerous operations for review
        is_delete = operation['action'] == 'delete'
        is_policy = 'policy' in operation.get('object_type', '')
        
        if is_delete and is_policy:
            self._request_approval(operation)
    
    def _request_approval(self, operation: dict[str, Any]):
        """Send approval request to workflow system"""
        import requests
        payload = {
            "type": "approval_required",
            "action": operation['action'],
            "object": operation.get('object_name'),
            "user": operation.get('user_context', {}).get('username'),
            "timestamp": operation['timestamp'],
            "rollback_data": operation.get('data')
        }
        requests.post(self.webhook, json=payload)

# Usage
handler = ApprovalHandler("https://workflow.company.com/approvals")
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

### Example 4: Multi-Destination Routing

Route different operations to different handlers:

```python
from typing import Any
from hfortix_core.audit import FileHandler, SyslogHandler

class SmartRouter:
    """Route operations based on type"""
    
    def __init__(self):
        self.compliance_handler = SyslogHandler("siem.company.com:514")
        self.debug_handler = FileHandler("/var/log/debug.jsonl")
        self.critical_handler = FileHandler("/var/log/critical.jsonl")
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Route to appropriate handler"""
        # All operations go to compliance SIEM
        self.compliance_handler.log_operation(operation)
        
        # Failed operations go to debug log
        if not operation['success']:
            self.debug_handler.log_operation(operation)
        
        # Critical operations (policy changes) get extra logging
        if 'policy' in operation.get('object_type', ''):
            self.critical_handler.log_operation(operation)

# Usage
handler = SmartRouter()
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

## Advanced Patterns

### Pattern 1: Async Processing

Don't block API operations with slow handlers:

```python
import queue
import threading
from typing import Any

class AsyncHandler:
    """Process operations asynchronously in background thread"""
    
    def __init__(self, target_handler):
        self.target = target_handler
        self.queue = queue.Queue()
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Queue operation for async processing"""
        self.queue.put(operation)
    
    def _process_queue(self):
        """Background worker thread"""
        while True:
            operation = self.queue.get()
            try:
                self.target.log_operation(operation)
            except Exception as e:
                import logging
                logging.error(f"Async handler error: {e}")
            finally:
                self.queue.task_done()

# Usage - wrap slow handler
slow_handler = DatabaseHandler("postgresql://...")
async_handler = AsyncHandler(slow_handler)
fgt = FortiOS("192.168.1.99", token="token", audit_handler=async_handler)
```

### Pattern 2: Error Aggregation

Batch errors for alert fatigue reduction:

```python
from typing import Any
from collections import defaultdict
import time

class ErrorAggregator:
    """Aggregate repeated errors before alerting"""
    
    def __init__(self, alert_handler, window_seconds=60, threshold=5):
        self.alert_handler = alert_handler
        self.window = window_seconds
        self.threshold = threshold
        self.errors = defaultdict(list)
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Track errors and alert on threshold"""
        if not operation['success']:
            error_key = (operation['endpoint'], operation.get('error'))
            now = time.time()
            
            # Add error with timestamp
            self.errors[error_key].append(now)
            
            # Clean old errors outside window
            self.errors[error_key] = [
                t for t in self.errors[error_key] 
                if now - t < self.window
            ]
            
            # Alert if threshold exceeded
            if len(self.errors[error_key]) >= self.threshold:
                self._send_alert(error_key, len(self.errors[error_key]))
                self.errors[error_key].clear()
    
    def _send_alert(self, error_key, count):
        endpoint, error = error_key
        alert = {
            "alert": f"{count} errors on {endpoint} in {self.window}s",
            "error": error
        }
        self.alert_handler.log_operation(alert)

# Usage
slack = SlackNotifier("https://hooks.slack.com/...")
aggregator = ErrorAggregator(slack, window_seconds=60, threshold=5)
fgt = FortiOS("192.168.1.99", token="token", audit_handler=aggregator)
```

### Pattern 3: Conditional Filtering

Only log what matters:

```python
from typing import Any, Callable

class FilteredHandler:
    """Only log operations matching filter criteria"""
    
    def __init__(self, target_handler, filter_fn: Callable[[dict], bool]):
        self.target = target_handler
        self.filter = filter_fn
    
    def log_operation(self, operation: dict[str, Any]) -> None:
        """Apply filter before logging"""
        if self.filter(operation):
            self.target.log_operation(operation)

# Usage examples
from hfortix_core.audit import FileHandler

# Only log write operations
writes_only = FilteredHandler(
    FileHandler("/var/log/writes.jsonl"),
    filter_fn=lambda op: op['method'] in ['POST', 'PUT', 'DELETE']
)

# Only log failures
failures_only = FilteredHandler(
    FileHandler("/var/log/failures.jsonl"),
    filter_fn=lambda op: not op['success']
)

# Only log specific VDOMs
vdom_filter = FilteredHandler(
    FileHandler("/var/log/production.jsonl"),
    filter_fn=lambda op: op.get('vdom') == 'production'
)

# Use CompositeHandler to combine
from hfortix_core.audit import CompositeHandler
handler = CompositeHandler([writes_only, failures_only, vdom_filter])
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

## Testing Custom Handlers

### Unit Testing

```python
import unittest
from unittest.mock import Mock, patch

class TestSlackNotifier(unittest.TestCase):
    
    def setUp(self):
        self.handler = SlackNotifier("https://test.webhook")
    
    @patch('requests.post')
    def test_firewall_policy_change_notifies(self, mock_post):
        """Should send Slack message on policy change"""
        operation = {
            'action': 'create',
            'object_type': 'firewall.policy',
            'object_name': 'Test-Policy',
            'user_context': {'username': 'admin'}
        }
        
        self.handler.log_operation(operation)
        
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        self.assertIn('Test-Policy', call_args[1]['json']['text'])
    
    @patch('requests.post')
    def test_non_policy_change_ignores(self, mock_post):
        """Should not notify on non-policy changes"""
        operation = {
            'action': 'create',
            'object_type': 'firewall.address',
            'object_name': 'Test-Address'
        }
        
        self.handler.log_operation(operation)
        
        mock_post.assert_not_called()
```

### Integration Testing

```python
from hfortix import FortiOS
from hfortix_core.audit import NullHandler

def test_handler_with_real_api():
    """Test handler receives actual operations"""
    operations_received = []
    
    class TestHandler:
        def log_operation(self, operation):
            operations_received.append(operation)
    
    handler = TestHandler()
    fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
    
    # Make API call
    fgt.api.cmdb.firewall.address.get()
    
    # Verify handler was called
    assert len(operations_received) == 1
    assert operations_received[0]['method'] == 'GET'
    assert operations_received[0]['object_type'] == 'firewall.address'
```

## Best Practices

### ✅ DO

1. **Handle errors gracefully** - Don't raise exceptions from `log_operation()`
2. **Keep it fast** - Use async processing for slow operations
3. **Sanitize sensitive data** - HFortix sanitizes, but double-check
4. **Use type hints** - Helps with IDE autocomplete
5. **Log handler errors** - Use Python logging to debug handler issues
6. **Test thoroughly** - Unit test your handlers

### ❌ DON'T

1. **Don't block** - Long operations should be async
2. **Don't raise** - Exceptions break API operations
3. **Don't assume** - Check for optional fields in operation dict
4. **Don't log passwords** - Already sanitized, but verify
5. **Don't modify operation** - It's passed to multiple handlers

## Performance Considerations

### Handler Performance Impact

| Handler Type | Latency Impact | Notes              |
| ------------ | -------------- | ------------------ |
| In-memory    | < 1ms          | Negligible         |
| File I/O     | 1-5ms          | Buffered, minimal  |
| Syslog (UDP) | < 5ms          | Fire-and-forget    |
| Database     | 10-50ms        | Use async wrapper  |
| HTTP webhook | 50-500ms       | Definitely async   |
| Kafka        | 5-20ms         | Async recommended  |

### Optimization Tips

```python
# ✅ Good - Async for slow handlers
handler = AsyncHandler(DatabaseHandler("postgresql://..."))

# ❌ Bad - Blocks every API call
handler = DatabaseHandler("postgresql://...")

# ✅ Good - Batch operations
class BatchingHandler:
    def __init__(self, batch_size=100):
        self.batch = []
        self.batch_size = batch_size
    
    def log_operation(self, operation):
        self.batch.append(operation)
        if len(self.batch) >= self.batch_size:
            self._flush_batch()

# ✅ Good - Filter early
handler = FilteredHandler(
    SlowHandler(),
    filter_fn=lambda op: op['action'] == 'delete'  # Only 1% of ops
)
```

## Troubleshooting

### Handler Not Being Called

```python
# Check if handler is set
fgt = FortiOS("192.168.1.99", token="token", audit_handler=my_handler)
print(fgt._client._audit_handler)  # Should show your handler

# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Handler Errors Silent

```python
# Handler errors are logged but don't raise
# Check logs:
import logging
logging.basicConfig(level=logging.ERROR)

# Add error tracking to your handler
class MyHandler:
    def __init__(self):
        self.errors = []
    
    def log_operation(self, operation):
        try:
            # Your logic
            pass
        except Exception as e:
            self.errors.append(e)
            raise  # Re-raise to see in logs
```

## Migration Guide

### From fortiosapi (Official Library)

The official library has no audit logging. To migrate:

```python
# Before (fortiosapi)
from fortiosapi import FortiOSAPI
fgt = FortiOSAPI()
fgt.tokenlogin("192.168.1.99", "token")

# After (hfortix)
from hfortix import FortiOS
from hfortix_core.audit import FileHandler

handler = FileHandler("/var/log/audit.jsonl")
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

# Now all operations are automatically logged!
```

### From Custom Logging

If you built custom logging:

```python
# Before - Manual logging
import logging
logger = logging.getLogger(__name__)

def create_policy(fgt, data):
    logger.info(f"Creating policy: {data}")
    result = fgt.api.cmdb.firewall.policy.create(**data)
    logger.info(f"Policy created: {result}")
    return result

# After - Automatic via handler
from hfortix import FortiOS
from hfortix_core.audit import FileHandler

fgt = FortiOS("192.168.1.99", token="token", 
              audit_handler=FileHandler("/var/log/audit.jsonl"))

# Just call the API - logging happens automatically
result = fgt.api.cmdb.firewall.policy.create(**data)
```

## See Also

- [Audit Logging Guide](./AUDIT_LOGGING.md) - Built-in handlers and compliance
- [Observability Guide](./OBSERVABILITY.md) - Metrics and monitoring
- [API Reference](../source/core/api-reference/http-client.rst) - HTTP client docs
- [Examples](../../examples/) - Sample implementations

## Support

- **GitHub Issues**: [hermanwjacobsen/hfortix](https://github.com/hermanwjacobsen/hfortix/issues)
- **Documentation**: [docs/](../)
- **Examples**: [examples/](../../examples/)
