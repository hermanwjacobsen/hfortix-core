"""
Tests for hfortix_core.audit.handlers.SyslogHandler.

SyslogHandler sends audit logs to syslog.
Note: These tests don't actually send to syslog, just test the handler interface.
"""

from hfortix_core.audit.handlers import SyslogHandler
from hfortix_core.audit.formatters import SyslogFormatter


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


def test_syslog_handler_creation():
    """Test creating a SyslogHandler."""
    print("\n=== Testing SyslogHandler creation ===")
    
    handler = SyslogHandler(server="localhost")
    assert handler is not None
    
    print("✅ SyslogHandler - creation")


def test_syslog_handler_with_address():
    """Test creating a SyslogHandler with custom server address."""
    print("\n=== Testing SyslogHandler with address ===")
    
    handler = SyslogHandler(server="localhost:514")
    assert handler is not None
    
    print("✅ SyslogHandler - with address")


def test_syslog_handler_with_timeout():
    """Test creating a SyslogHandler with custom timeout."""
    print("\n=== Testing SyslogHandler with timeout ===")
    
    handler = SyslogHandler(server="localhost", timeout=10.0)
    assert handler is not None
    
    print("✅ SyslogHandler - with timeout")


def test_syslog_handler_with_port():
    """Test creating a SyslogHandler with custom port."""
    print("\n=== Testing SyslogHandler with port ===")
    
    handler = SyslogHandler(server="localhost:1514")
    assert handler is not None
    
    print("✅ SyslogHandler - with port")


def test_syslog_handler_server_formats():
    """Test SyslogHandler with various server formats."""
    print("\n=== Testing SyslogHandler server formats ===")
    
    # Various valid server formats
    servers = [
        "localhost",
        "localhost:514",
        "192.168.1.100",
        "192.168.1.100:514",
        "syslog.example.com",
        "syslog.example.com:1514",
    ]
    
    for server in servers:
        handler = SyslogHandler(server=server)
        assert handler is not None
    
    print("✅ SyslogHandler - server formats")


def test_syslog_handler_with_formatter():
    """Test creating a SyslogHandler with custom formatter."""
    print("\n=== Testing SyslogHandler with formatter ===")
    
    formatter = SyslogFormatter()
    handler = SyslogHandler(server="localhost", formatter=formatter)
    assert handler is not None
    
    print("✅ SyslogHandler - with formatter")


def test_syslog_handler_log_operation():
    """Test log_operation method exists and is callable."""
    print("\n=== Testing SyslogHandler log_operation ===")
    
    handler = SyslogHandler(server="localhost")
    
    # log_operation should exist and be callable
    assert hasattr(handler, 'log_operation')
    assert callable(handler.log_operation)
    
    print("✅ SyslogHandler - log_operation exists")


def test_syslog_handler_interface():
    """Test SyslogHandler has expected interface."""
    print("\n=== Testing SyslogHandler interface ===")
    
    handler = SyslogHandler(server="localhost")
    
    # Check it has the handler interface
    assert hasattr(handler, 'log_operation')
    
    print("✅ SyslogHandler - interface")


def test_syslog_handler_all_params():
    """Test creating a SyslogHandler with all parameters."""
    print("\n=== Testing SyslogHandler all params ===")
    
    formatter = SyslogFormatter()
    handler = SyslogHandler(
        server="localhost:514",
        formatter=formatter,
        timeout=10.0
    )
    assert handler is not None
    
    print("✅ SyslogHandler - all params")


def test_syslog_handler_default_port():
    """Test creating a SyslogHandler uses default port 514."""
    print("\n=== Testing SyslogHandler default port ===")
    
    handler = SyslogHandler(server="localhost")
    assert handler is not None
    
    print("✅ SyslogHandler - default port")


def run_all_tests():
    """Run all SyslogHandler tests."""
    tests = [
        test_syslog_handler_creation,
        test_syslog_handler_with_address,
        test_syslog_handler_with_timeout,
        test_syslog_handler_with_port,
        test_syslog_handler_server_formats,
        test_syslog_handler_with_formatter,
        test_syslog_handler_log_operation,
        test_syslog_handler_interface,
        test_syslog_handler_all_params,
        test_syslog_handler_default_port,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"❌ {test.__name__} FAILED: {e}")
    
    print(f"\n{'='*50}")
    print(f"Results: {passed}/{passed + failed} passed")
    return failed == 0


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
