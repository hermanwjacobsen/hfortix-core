"""
Tests for hfortix_fortios.configure_logging function.

configure_logging sets up logging for the FortiOS client.
"""

import io
import logging
import tempfile
import os
from contextlib import redirect_stdout, redirect_stderr

from hfortix_fortios import configure_logging


def test_configure_logging_default():
    """Test configure_logging with default options."""
    print("\n=== Testing configure_logging default ===")
    
    # Should not raise
    configure_logging()
    
    print("✅ configure_logging - default")


def test_configure_logging_level_info():
    """Test configure_logging with INFO level."""
    print("\n=== Testing configure_logging INFO level ===")
    
    configure_logging(level="INFO")
    
    print("✅ configure_logging - INFO level")


def test_configure_logging_level_debug():
    """Test configure_logging with DEBUG level."""
    print("\n=== Testing configure_logging DEBUG level ===")
    
    configure_logging(level="DEBUG")
    
    print("✅ configure_logging - DEBUG level")


def test_configure_logging_level_warning():
    """Test configure_logging with WARNING level."""
    print("\n=== Testing configure_logging WARNING level ===")
    
    configure_logging(level="WARNING")
    
    print("✅ configure_logging - WARNING level")


def test_configure_logging_level_error():
    """Test configure_logging with ERROR level."""
    print("\n=== Testing configure_logging ERROR level ===")
    
    configure_logging(level="ERROR")
    
    print("✅ configure_logging - ERROR level")


def test_configure_logging_level_int():
    """Test configure_logging with integer level."""
    print("\n=== Testing configure_logging int level ===")
    
    configure_logging(level=logging.DEBUG)
    configure_logging(level=logging.INFO)
    configure_logging(level=logging.WARNING)
    
    print("✅ configure_logging - integer level")


def test_configure_logging_format_json():
    """Test configure_logging with JSON format."""
    print("\n=== Testing configure_logging JSON format ===")
    
    configure_logging(format="json")
    
    print("✅ configure_logging - JSON format")


def test_configure_logging_format_text():
    """Test configure_logging with text format."""
    print("\n=== Testing configure_logging text format ===")
    
    configure_logging(format="text")
    
    print("✅ configure_logging - text format")


def test_configure_logging_with_color():
    """Test configure_logging with color enabled."""
    print("\n=== Testing configure_logging with color ===")
    
    configure_logging(use_color=True)
    
    print("✅ configure_logging - with color")


def test_configure_logging_without_color():
    """Test configure_logging with color disabled."""
    print("\n=== Testing configure_logging without color ===")
    
    configure_logging(use_color=False)
    
    print("✅ configure_logging - without color")


def test_configure_logging_include_trace():
    """Test configure_logging with trace enabled."""
    print("\n=== Testing configure_logging include_trace ===")
    
    configure_logging(include_trace=True)
    
    print("✅ configure_logging - include_trace=True")


def test_configure_logging_no_trace():
    """Test configure_logging with trace disabled."""
    print("\n=== Testing configure_logging no trace ===")
    
    configure_logging(include_trace=False)
    
    print("✅ configure_logging - include_trace=False")


def test_configure_logging_structured():
    """Test configure_logging with structured output."""
    print("\n=== Testing configure_logging structured ===")
    
    configure_logging(structured=True)
    
    print("✅ configure_logging - structured=True")


def test_configure_logging_output_file():
    """Test configure_logging with output file."""
    print("\n=== Testing configure_logging output_file ===")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False) as f:
        filepath = f.name
    
    try:
        configure_logging(output_file=filepath)
        
        # File should exist (may or may not have content depending on implementation)
        assert os.path.exists(filepath)
        
    finally:
        # Cleanup
        if os.path.exists(filepath):
            os.remove(filepath)
    
    print("✅ configure_logging - output_file")


def test_configure_logging_custom_handler():
    """Test configure_logging with custom handler."""
    print("\n=== Testing configure_logging custom handler ===")
    
    buffer = io.StringIO()
    handler = logging.StreamHandler(buffer)
    handler.setLevel(logging.DEBUG)
    
    configure_logging(handler=handler)
    
    print("✅ configure_logging - custom handler")


def test_configure_logging_all_options():
    """Test configure_logging with all options."""
    print("\n=== Testing configure_logging all options ===")
    
    configure_logging(
        level="DEBUG",
        format="text",
        use_color=False,
        include_trace=True,
        structured=False
    )
    
    print("✅ configure_logging - all options")


def test_configure_logging_json_structured():
    """Test configure_logging with JSON and structured."""
    print("\n=== Testing configure_logging JSON structured ===")
    
    configure_logging(
        format="json",
        structured=True,
        level="DEBUG"
    )
    
    print("✅ configure_logging - JSON structured")


def test_configure_logging_multiple_calls():
    """Test calling configure_logging multiple times."""
    print("\n=== Testing configure_logging multiple calls ===")
    
    # Should be safe to call multiple times
    configure_logging(level="INFO")
    configure_logging(level="DEBUG")
    configure_logging(level="WARNING")
    configure_logging(level="INFO", format="json")
    configure_logging(level="INFO", format="text")
    
    print("✅ configure_logging - multiple calls")


def run_all_tests():
    """Run all configure_logging tests."""
    tests = [
        test_configure_logging_default,
        test_configure_logging_level_info,
        test_configure_logging_level_debug,
        test_configure_logging_level_warning,
        test_configure_logging_level_error,
        test_configure_logging_level_int,
        test_configure_logging_format_json,
        test_configure_logging_format_text,
        test_configure_logging_with_color,
        test_configure_logging_without_color,
        test_configure_logging_include_trace,
        test_configure_logging_no_trace,
        test_configure_logging_structured,
        test_configure_logging_output_file,
        test_configure_logging_custom_handler,
        test_configure_logging_all_options,
        test_configure_logging_json_structured,
        test_configure_logging_multiple_calls,
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
