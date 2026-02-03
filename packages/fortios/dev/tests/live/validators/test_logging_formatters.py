"""
Tests for hfortix_core.logging formatters

Tests StructuredFormatter and TextFormatter for logging output.
"""

import logging
import json
from io import StringIO

from hfortix_core.logging import StructuredFormatter, TextFormatter


def test_structured_formatter_basic():
    """Test StructuredFormatter basic JSON output"""
    print("\n=== Testing StructuredFormatter (basic) ===")
    
    formatter = StructuredFormatter()
    
    # Create a log record
    record = logging.LogRecord(
        name="hfortix.test",
        level=logging.INFO,
        pathname="test.py",
        lineno=42,
        msg="Test message",
        args=(),
        exc_info=None,
    )
    
    result = formatter.format(record)
    data = json.loads(result)
    
    assert data["level"] == "INFO"
    assert data["logger"] == "hfortix.test"
    assert data["message"] == "Test message"
    assert "timestamp" in data
    
    print(f"✓ Basic JSON output: {result[:80]}...")


def test_structured_formatter_extra_fields():
    """Test StructuredFormatter with extra fields"""
    print("\n=== Testing StructuredFormatter (extra fields) ===")
    
    formatter = StructuredFormatter()
    
    record = logging.LogRecord(
        name="hfortix.http",
        level=logging.INFO,
        pathname="client.py",
        lineno=100,
        msg="API request completed",
        args=(),
        exc_info=None,
    )
    # Add extra fields
    record.endpoint = "/api/v2/cmdb/firewall/address"
    record.duration_seconds = 0.145
    record.status_code = 200
    record.request_id = "req-12345"
    
    result = formatter.format(record)
    data = json.loads(result)
    
    assert data["endpoint"] == "/api/v2/cmdb/firewall/address"
    assert data["duration_seconds"] == 0.145
    assert data["status_code"] == 200
    assert data["request_id"] == "req-12345"
    
    print(f"✓ Extra fields included: endpoint, duration, status_code, request_id")


def test_structured_formatter_include_fields():
    """Test StructuredFormatter with include_fields filter"""
    print("\n=== Testing StructuredFormatter (include_fields) ===")
    
    # Only include specific extra fields
    formatter = StructuredFormatter(include_fields=["endpoint", "status_code"])
    
    record = logging.LogRecord(
        name="hfortix",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="Test",
        args=(),
        exc_info=None,
    )
    record.endpoint = "/api/test"
    record.status_code = 200
    record.duration_seconds = 0.5  # Should be excluded
    record.secret_data = "should not appear"  # Should be excluded
    
    result = formatter.format(record)
    data = json.loads(result)
    
    assert "endpoint" in data
    assert "status_code" in data
    assert "duration_seconds" not in data
    assert "secret_data" not in data
    
    print("✓ Only include_fields are present")


def test_structured_formatter_exclude_fields():
    """Test StructuredFormatter with exclude_fields filter"""
    print("\n=== Testing StructuredFormatter (exclude_fields) ===")
    
    formatter = StructuredFormatter(exclude_fields=["password", "token"])
    
    record = logging.LogRecord(
        name="hfortix",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="Test",
        args=(),
        exc_info=None,
    )
    record.endpoint = "/api/test"
    record.password = "secret123"  # Should be excluded
    record.token = "abc123"  # Should be excluded
    
    result = formatter.format(record)
    data = json.loads(result)
    
    assert "endpoint" in data
    assert "password" not in data
    assert "token" not in data
    
    print("✓ exclude_fields are filtered out")


def test_structured_formatter_debug_source():
    """Test StructuredFormatter includes source for DEBUG level"""
    print("\n=== Testing StructuredFormatter (DEBUG source) ===")
    
    formatter = StructuredFormatter()
    
    # DEBUG record should include source location
    debug_record = logging.LogRecord(
        name="hfortix",
        level=logging.DEBUG,
        pathname="myfile.py",
        lineno=42,
        msg="Debug message",
        args=(),
        exc_info=None,
    )
    debug_record.funcName = "my_function"
    
    result = formatter.format(debug_record)
    data = json.loads(result)
    
    assert "source" in data
    assert data["source"]["file"] == "myfile.py"
    assert data["source"]["line"] == 42
    assert data["source"]["function"] == "my_function"
    
    # INFO record should NOT include source
    info_record = logging.LogRecord(
        name="hfortix",
        level=logging.INFO,
        pathname="myfile.py",
        lineno=42,
        msg="Info message",
        args=(),
        exc_info=None,
    )
    
    result = formatter.format(info_record)
    data = json.loads(result)
    assert "source" not in data
    
    print("✓ Source included for DEBUG, excluded for INFO")


def test_structured_formatter_exception():
    """Test StructuredFormatter with exception info"""
    print("\n=== Testing StructuredFormatter (exception) ===")
    
    formatter = StructuredFormatter()
    
    try:
        raise ValueError("Test error")
    except ValueError:
        import sys
        exc_info = sys.exc_info()
    
    record = logging.LogRecord(
        name="hfortix",
        level=logging.ERROR,
        pathname="test.py",
        lineno=1,
        msg="An error occurred",
        args=(),
        exc_info=exc_info,
    )
    
    result = formatter.format(record)
    data = json.loads(result)
    
    assert "exception" in data
    assert "ValueError" in data["exception"]
    assert "Test error" in data["exception"]
    
    print("✓ Exception info included")


def test_structured_formatter_all_levels():
    """Test StructuredFormatter with all log levels"""
    print("\n=== Testing StructuredFormatter (all levels) ===")
    
    formatter = StructuredFormatter()
    
    levels = [
        (logging.DEBUG, "DEBUG"),
        (logging.INFO, "INFO"),
        (logging.WARNING, "WARNING"),
        (logging.ERROR, "ERROR"),
        (logging.CRITICAL, "CRITICAL"),
    ]
    
    for level, level_name in levels:
        record = logging.LogRecord(
            name="test",
            level=level,
            pathname="test.py",
            lineno=1,
            msg="Test",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        data = json.loads(result)
        assert data["level"] == level_name
        print(f"  ✓ {level_name}")
    
    print("✓ All log levels formatted correctly")


def test_text_formatter_basic():
    """Test TextFormatter basic output"""
    print("\n=== Testing TextFormatter (basic) ===")
    
    formatter = TextFormatter(use_color=False)
    
    record = logging.LogRecord(
        name="hfortix.client",
        level=logging.INFO,
        pathname="client.py",
        lineno=100,
        msg="Connected to FortiGate",
        args=(),
        exc_info=None,
    )
    
    result = formatter.format(record)
    
    # Should contain: timestamp [LEVEL] logger: message
    assert "[INFO]" in result
    assert "hfortix.client" in result
    assert "Connected to FortiGate" in result
    
    print(f"✓ Text output: {result}")


def test_text_formatter_with_color():
    """Test TextFormatter with ANSI colors"""
    print("\n=== Testing TextFormatter (with color) ===")
    
    formatter = TextFormatter(use_color=True)
    
    levels = [
        (logging.DEBUG, "\033[36m"),    # Cyan
        (logging.INFO, "\033[32m"),     # Green
        (logging.WARNING, "\033[33m"),  # Yellow
        (logging.ERROR, "\033[31m"),    # Red
        (logging.CRITICAL, "\033[35m"), # Magenta
    ]
    
    for level, color_code in levels:
        record = logging.LogRecord(
            name="test",
            level=level,
            pathname="test.py",
            lineno=1,
            msg="Test message",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        assert color_code in result, f"Missing color code for {logging.getLevelName(level)}"
        assert "\033[0m" in result  # Reset code
        print(f"  ✓ {logging.getLevelName(level)} has color")
    
    print("✓ All levels have correct colors")


def test_text_formatter_without_color():
    """Test TextFormatter without ANSI colors"""
    print("\n=== Testing TextFormatter (no color) ===")
    
    formatter = TextFormatter(use_color=False)
    
    record = logging.LogRecord(
        name="test",
        level=logging.ERROR,
        pathname="test.py",
        lineno=1,
        msg="Error message",
        args=(),
        exc_info=None,
    )
    
    result = formatter.format(record)
    
    # Should not contain ANSI codes
    assert "\033[" not in result
    assert "[ERROR]" in result
    
    print(f"✓ No color codes: {result}")


def test_text_formatter_exception():
    """Test TextFormatter with exception info"""
    print("\n=== Testing TextFormatter (exception) ===")
    
    formatter = TextFormatter(use_color=False)
    
    try:
        raise RuntimeError("Something went wrong")
    except RuntimeError:
        import sys
        exc_info = sys.exc_info()
    
    record = logging.LogRecord(
        name="test",
        level=logging.ERROR,
        pathname="test.py",
        lineno=1,
        msg="An error occurred",
        args=(),
        exc_info=exc_info,
    )
    
    result = formatter.format(record)
    
    assert "RuntimeError" in result
    assert "Something went wrong" in result
    
    print("✓ Exception info included in text output")


def test_text_formatter_message_formatting():
    """Test TextFormatter with message args"""
    print("\n=== Testing TextFormatter (message formatting) ===")
    
    formatter = TextFormatter(use_color=False)
    
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="Request to %s completed in %.2fms",
        args=("/api/test", 125.5),
        exc_info=None,
    )
    
    result = formatter.format(record)
    
    assert "Request to /api/test completed in 125.50ms" in result
    
    print(f"✓ Message args formatted: {result}")


def test_formatter_integration_with_logger():
    """Test formatters work with actual logging"""
    print("\n=== Testing Integration with Logger ===")
    
    # Create handler with buffer
    buffer = StringIO()
    handler = logging.StreamHandler(buffer)
    
    # Test StructuredFormatter
    handler.setFormatter(StructuredFormatter())
    
    logger = logging.getLogger("test.integration")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    logger.info("Test message", extra={"custom_field": "value"})
    
    output = buffer.getvalue()
    data = json.loads(output.strip())
    
    assert data["message"] == "Test message"
    assert data["custom_field"] == "value"
    
    # Cleanup
    logger.removeHandler(handler)
    
    print("✓ Formatter integrates correctly with logging module")


if __name__ == "__main__":
    test_structured_formatter_basic()
    test_structured_formatter_extra_fields()
    test_structured_formatter_include_fields()
    test_structured_formatter_exclude_fields()
    test_structured_formatter_debug_source()
    test_structured_formatter_exception()
    test_structured_formatter_all_levels()
    test_text_formatter_basic()
    test_text_formatter_with_color()
    test_text_formatter_without_color()
    test_text_formatter_exception()
    test_text_formatter_message_formatting()
    test_formatter_integration_with_logger()
    
    print("\n" + "=" * 60)
    print("✅ All logging formatter tests passed!")
    print("=" * 60)
