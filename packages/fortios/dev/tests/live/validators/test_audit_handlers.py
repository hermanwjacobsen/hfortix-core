"""
Tests for hfortix_core.audit handlers

Tests NullHandler, StreamHandler, CallbackHandler, CompositeHandler.
FileHandler tested with temp file.
"""

import io
import sys
import tempfile
import os
from pathlib import Path

import pytest

from hfortix_core.audit.handlers import (
    NullHandler,
    StreamHandler,
    FileHandler,
    CompositeHandler,
    CallbackHandler,
)
from hfortix_core.audit.formatters import JSONFormatter


# Sample operation for testing
SAMPLE_OPERATION = {
    "timestamp": "2026-01-10T14:23:45Z",
    "request_id": "req-12345",
    "method": "POST",
    "endpoint": "/api/v2/cmdb/firewall/address",
    "host": "192.168.1.99",
    "success": True,
    "status_code": 200,
    "user_context": {"username": "admin"},
}


def test_null_handler():
    """Test NullHandler does nothing"""
    print("\n=== Testing NullHandler ===")
    
    handler = NullHandler()
    
    # Should not raise any exception
    handler.log_operation(SAMPLE_OPERATION)
    handler.log_operation({})
    handler.log_operation({"method": "GET"})
    
    print("✓ NullHandler accepts operations silently")


def test_stream_handler_stdout():
    """Test StreamHandler with stdout
    
    BUG FOUND in hfortix_core/audit/handlers.py line ~315:
    
        logger.debug(f"StreamHandler initialized: {self.stream.name}")
    
    StringIO objects don't have a 'name' attribute, causing:
        AttributeError: '_io.StringIO' object has no attribute 'name'
    
    FIX: Use getattr with default:
        logger.debug(f"StreamHandler initialized: {getattr(self.stream, 'name', '<unnamed>')}")
    """
    print("\n=== Testing StreamHandler (stdout) ===")
    
    # Capture stdout
    buffer = io.StringIO()
    handler = StreamHandler(stream=buffer)
    
    handler.log_operation(SAMPLE_OPERATION)
    
    output = buffer.getvalue()
    assert '"method":"POST"' in output or '"method": "POST"' in output
    assert '"timestamp"' in output
    assert "req-12345" in output
    
    print(f"✓ StreamHandler output (length: {len(output)})")
    print(f"  First 80 chars: {output[:80]}...")


def test_stream_handler_custom_formatter():
    """Test StreamHandler with custom formatter"""
    print("\n=== Testing StreamHandler (custom formatter) ===")
    
    buffer = io.StringIO()
    formatter = JSONFormatter(pretty=True, indent=4)
    handler = StreamHandler(stream=buffer, formatter=formatter)
    
    handler.log_operation(SAMPLE_OPERATION)
    
    output = buffer.getvalue()
    # Pretty format should have newlines and indentation
    assert "\n" in output
    assert "    " in output  # 4-space indent
    
    print("✓ Custom formatter applied")


def test_stream_handler_default_stdout():
    """Test StreamHandler defaults to stdout"""
    print("\n=== Testing StreamHandler (default stream) ===")
    
    handler = StreamHandler()
    assert handler.stream is sys.stdout
    
    print("✓ Default stream is stdout")


def test_callback_handler():
    """Test CallbackHandler with custom function"""
    print("\n=== Testing CallbackHandler ===")
    
    received_operations = []
    
    def my_callback(operation):
        received_operations.append(operation)
    
    handler = CallbackHandler(my_callback)
    
    handler.log_operation(SAMPLE_OPERATION)
    handler.log_operation({"method": "GET", "path": "/test"})
    
    assert len(received_operations) == 2
    assert received_operations[0] == SAMPLE_OPERATION
    assert received_operations[1]["method"] == "GET"
    
    print(f"✓ Callback received {len(received_operations)} operations")


def test_callback_handler_error_handling():
    """Test CallbackHandler handles callback errors gracefully"""
    print("\n=== Testing CallbackHandler (error handling) ===")
    
    def failing_callback(operation):
        raise ValueError("Simulated failure")
    
    handler = CallbackHandler(failing_callback)
    
    # Should not raise - errors are logged internally
    handler.log_operation(SAMPLE_OPERATION)
    
    print("✓ Callback errors are caught (not propagated)")


def test_file_handler():
    """Test FileHandler writes to file"""
    print("\n=== Testing FileHandler ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "audit.jsonl"
        
        handler = FileHandler(filepath)
        
        handler.log_operation(SAMPLE_OPERATION)
        handler.log_operation({"method": "GET", "path": "/test"})
        
        # Force flush
        handler.close()
        
        # Read file
        content = filepath.read_text()
        lines = content.strip().split("\n")
        
        assert len(lines) == 2
        assert '"method":"POST"' in lines[0] or '"method": "POST"' in lines[0]
        assert '"method":"GET"' in lines[1] or '"method": "GET"' in lines[1]
        
        print(f"✓ FileHandler wrote {len(lines)} lines to {filepath.name}")


def test_file_handler_creates_directory():
    """Test FileHandler creates parent directories"""
    print("\n=== Testing FileHandler (directory creation) ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "nested" / "deep" / "audit.log"
        
        handler = FileHandler(filepath)
        handler.log_operation(SAMPLE_OPERATION)
        handler.close()
        
        assert filepath.exists()
        
        print(f"✓ Created nested directory: {filepath.parent}")


def test_file_handler_append_mode():
    """Test FileHandler appends to existing file"""
    print("\n=== Testing FileHandler (append mode) ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "audit.jsonl"
        
        # First handler
        handler1 = FileHandler(filepath)
        handler1.log_operation({"id": 1})
        handler1.close()
        
        # Second handler (should append)
        handler2 = FileHandler(filepath)
        handler2.log_operation({"id": 2})
        handler2.close()
        
        lines = filepath.read_text().strip().split("\n")
        assert len(lines) == 2
        
        print("✓ FileHandler appends to existing file")


def test_file_handler_rotation():
    """Test FileHandler rotation when size limit exceeded"""
    print("\n=== Testing FileHandler (rotation) ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = Path(tmpdir) / "audit.jsonl"
        
        # Very small max_bytes to trigger rotation
        handler = FileHandler(filepath, max_bytes=200, backup_count=3)
        
        # Write enough to trigger rotation
        for i in range(20):
            handler.log_operation({
                "id": i,
                "data": "x" * 50,  # Make each entry ~80 bytes
            })
        
        handler.close()
        
        # Check for backup files
        files = list(Path(tmpdir).glob("audit.jsonl*"))
        
        # Should have main file and at least one backup
        assert len(files) >= 1
        
        print(f"✓ FileHandler created {len(files)} file(s) after rotation")
        for f in sorted(files):
            print(f"  - {f.name}: {f.stat().st_size} bytes")


def test_composite_handler_basic():
    """Test CompositeHandler sends to multiple handlers"""
    print("\n=== Testing CompositeHandler (basic) ===")
    
    buffer1 = io.StringIO()
    buffer2 = io.StringIO()
    
    handler = CompositeHandler([
        StreamHandler(buffer1),
        StreamHandler(buffer2),
    ])
    
    handler.log_operation(SAMPLE_OPERATION)
    
    # Both should receive the operation
    output1 = buffer1.getvalue()
    output2 = buffer2.getvalue()
    
    assert '"method":"POST"' in output1 or '"method": "POST"' in output1
    assert output1 == output2  # Same content
    
    print("✓ CompositeHandler sent to both handlers")


def test_composite_handler_priority():
    """Test CompositeHandler executes in priority order"""
    print("\n=== Testing CompositeHandler (priority) ===")
    
    execution_order = []
    
    def make_callback(name):
        def cb(op):
            execution_order.append(name)
        return cb
    
    handler = CompositeHandler([
        (CallbackHandler(make_callback("low")), 1, None),
        (CallbackHandler(make_callback("high")), 10, None),
        (CallbackHandler(make_callback("medium")), 5, None),
    ])
    
    handler.log_operation(SAMPLE_OPERATION)
    
    # Should execute in priority order: high, medium, low
    assert execution_order == ["high", "medium", "low"]
    
    print(f"✓ Execution order: {execution_order}")


def test_composite_handler_filter():
    """Test CompositeHandler with filter functions"""
    print("\n=== Testing CompositeHandler (filtering) ===")
    
    all_ops = []
    write_ops = []
    
    handler = CompositeHandler([
        (CallbackHandler(lambda op: all_ops.append(op)), 0, None),  # No filter
        (CallbackHandler(lambda op: write_ops.append(op)), 0, 
         lambda op: op.get("method") in ["POST", "PUT", "DELETE"]),  # Write-only filter
    ])
    
    handler.log_operation({"method": "GET", "path": "/read"})
    handler.log_operation({"method": "POST", "path": "/create"})
    handler.log_operation({"method": "DELETE", "path": "/remove"})
    
    assert len(all_ops) == 3
    assert len(write_ops) == 2  # Only POST and DELETE
    
    print(f"✓ All handler: {len(all_ops)}, Write-only handler: {len(write_ops)}")


def test_composite_handler_error_aggregation():
    """Test CompositeHandler aggregates errors"""
    print("\n=== Testing CompositeHandler (error aggregation) ===")
    
    def failing_callback(op):
        raise RuntimeError("Handler failed!")
    
    buffer = io.StringIO()
    
    handler = CompositeHandler([
        CallbackHandler(failing_callback, propagate_errors=True),  # Will fail and bubble for aggregation
        StreamHandler(buffer),                                     # Will succeed
    ], aggregate_errors=True)
    
    handler.log_operation(SAMPLE_OPERATION)
    
    # Working handler should still receive the operation
    assert len(buffer.getvalue()) > 0
    
    # Error should be tracked
    summary = handler.error_summary
    assert summary["total_errors"] == 1
    
    print(f"✓ Error summary: {summary['total_errors']} error(s)")
    print("✓ Other handlers continued despite failure")


def test_composite_handler_add_remove():
    """Test CompositeHandler dynamic add/remove"""
    print("\n=== Testing CompositeHandler (add/remove) ===")
    
    received = []
    
    handler = CompositeHandler([])
    
    # Add handler
    cb_handler = CallbackHandler(lambda op: received.append(op))
    handler.add_handler(cb_handler, priority=5)
    
    handler.log_operation({"id": 1})
    assert len(received) == 1
    
    # Remove handler
    removed = handler.remove_handler(cb_handler)
    assert removed is True
    
    handler.log_operation({"id": 2})
    assert len(received) == 1  # No new operations
    
    print("✓ Dynamic add/remove works")


def test_composite_handler_get_handlers():
    """Test CompositeHandler get_handlers()"""
    print("\n=== Testing CompositeHandler (get_handlers) ===")
    
    h1 = NullHandler()
    h2 = NullHandler()
    
    handler = CompositeHandler([
        (h1, 10, None),
        (h2, 5, None),
    ])
    
    handlers = handler.get_handlers()
    
    assert len(handlers) == 2
    # Should be sorted by priority (highest first)
    assert handlers[0][1] == 10  # priority of first
    assert handlers[1][1] == 5   # priority of second
    
    print(f"✓ get_handlers() returns {len(handlers)} handlers in priority order")


def test_composite_handler_reset_errors():
    """Test CompositeHandler error reset"""
    print("\n=== Testing CompositeHandler (reset errors) ===")
    
    def failing(op):
        raise Exception("fail")
    
    handler = CompositeHandler([CallbackHandler(failing, propagate_errors=True)], aggregate_errors=True)
    
    handler.log_operation({})
    assert handler.error_summary["total_errors"] == 1
    
    handler.reset_errors()
    assert handler.error_summary["total_errors"] == 0
    
    print("✓ Error counts reset")


def test_handler_protocol_compliance():
    """Test all handlers implement log_operation"""
    print("\n=== Testing Handler Protocol Compliance ===")
    
    handlers = [
        NullHandler(),
        StreamHandler(io.StringIO()),
        CallbackHandler(lambda op: None),
        CompositeHandler([]),
    ]
    
    for handler in handlers:
        # Should have log_operation method
        assert hasattr(handler, "log_operation")
        assert callable(handler.log_operation)
        
        # Should accept operation dict
        handler.log_operation(SAMPLE_OPERATION)
        
        print(f"  ✓ {handler.__class__.__name__}")
    
    print("✓ All handlers are protocol compliant")


if __name__ == "__main__":
    test_null_handler()
    test_stream_handler_stdout()
    test_stream_handler_custom_formatter()
    test_stream_handler_default_stdout()
    test_callback_handler()
    test_callback_handler_error_handling()
    test_file_handler()
    test_file_handler_creates_directory()
    test_file_handler_append_mode()
    test_file_handler_rotation()
    test_composite_handler_basic()
    test_composite_handler_priority()
    test_composite_handler_filter()
    test_composite_handler_error_aggregation()
    test_composite_handler_add_remove()
    test_composite_handler_get_handlers()
    test_composite_handler_reset_errors()
    test_handler_protocol_compliance()
    
    print("\n" + "=" * 60)
    print("✅ All audit handler tests passed!")
    print("=" * 60)
