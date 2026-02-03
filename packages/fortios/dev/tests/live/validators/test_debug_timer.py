"""
Tests for hfortix_core.debug handlers

Tests debug_timer context manager and DebugSession helper class.
"""

import time
import io
import sys
from contextlib import redirect_stdout

from hfortix_core.debug import debug_timer


def test_debug_timer_basic():
    """Test debug_timer measures elapsed time"""
    print("\n=== Testing debug_timer (basic) ===")
    
    # Capture stdout
    buffer = io.StringIO()
    
    with redirect_stdout(buffer):
        with debug_timer("Test operation") as timing:
            time.sleep(0.05)  # 50ms
    
    # Check timing data
    assert "operation" in timing
    assert timing["operation"] == "Test operation"
    assert "duration_seconds" in timing
    assert "duration_ms" in timing
    assert timing["duration_seconds"] >= 0.05
    assert timing["duration_ms"] >= 50
    
    # Check printed output
    output = buffer.getvalue()
    assert "Test operation:" in output
    assert "ms" in output
    
    print(f"✓ Timing: {timing['duration_ms']:.1f}ms")
    print(f"✓ Output: {output.strip()}")


def test_debug_timer_default_name():
    """Test debug_timer with default operation name"""
    print("\n=== Testing debug_timer (default name) ===")
    
    buffer = io.StringIO()
    
    with redirect_stdout(buffer):
        with debug_timer() as timing:
            pass
    
    assert timing["operation"] == "Operation"
    assert "Operation:" in buffer.getvalue()
    
    print("✓ Default name 'Operation' used")


def test_debug_timer_timing_accuracy():
    """Test debug_timer timing accuracy"""
    print("\n=== Testing debug_timer (accuracy) ===")
    
    buffer = io.StringIO()
    
    with redirect_stdout(buffer):
        with debug_timer("Accuracy test") as timing:
            time.sleep(0.1)  # 100ms
    
    # Should be close to 100ms (allow some tolerance)
    assert 90 < timing["duration_ms"] < 200
    
    # duration_seconds should match duration_ms
    expected_ms = timing["duration_seconds"] * 1000
    assert abs(timing["duration_ms"] - expected_ms) < 0.01
    
    print(f"✓ Timing accurate: {timing['duration_ms']:.1f}ms (expected ~100ms)")


def test_debug_timer_no_sleep():
    """Test debug_timer with minimal operation"""
    print("\n=== Testing debug_timer (no sleep) ===")
    
    buffer = io.StringIO()
    
    with redirect_stdout(buffer):
        with debug_timer("Fast operation") as timing:
            x = 1 + 1  # Very fast operation
    
    # Should be very small but not negative
    assert timing["duration_ms"] >= 0
    assert timing["duration_seconds"] >= 0
    
    print(f"✓ Fast operation: {timing['duration_ms']:.3f}ms")


def test_debug_timer_exception_handling():
    """Test debug_timer still records time on exception"""
    print("\n=== Testing debug_timer (exception) ===")
    
    buffer = io.StringIO()
    timing_result = {}
    
    try:
        with redirect_stdout(buffer):
            with debug_timer("Exception test") as timing:
                timing_result = timing
                time.sleep(0.02)
                raise ValueError("Test exception")
    except ValueError:
        pass
    
    # Timing should still be recorded even though exception occurred
    assert "duration_ms" in timing_result
    assert timing_result["duration_ms"] >= 20
    
    # Output should still be printed
    assert "Exception test:" in buffer.getvalue()
    
    print(f"✓ Timing recorded despite exception: {timing_result['duration_ms']:.1f}ms")


def test_debug_timer_nested():
    """Test nested debug_timer calls"""
    print("\n=== Testing debug_timer (nested) ===")
    
    buffer = io.StringIO()
    
    with redirect_stdout(buffer):
        with debug_timer("Outer") as outer:
            time.sleep(0.02)
            with debug_timer("Inner") as inner:
                time.sleep(0.02)
    
    # Both should have timing
    assert outer["duration_ms"] >= 40  # ~40ms total
    assert inner["duration_ms"] >= 20  # ~20ms for inner
    
    # Inner should be less than outer
    assert inner["duration_ms"] < outer["duration_ms"]
    
    output = buffer.getvalue()
    assert "Inner:" in output
    assert "Outer:" in output
    
    print(f"✓ Outer: {outer['duration_ms']:.1f}ms, Inner: {inner['duration_ms']:.1f}ms")


def test_debug_timer_multiple_sequential():
    """Test multiple sequential debug_timer calls"""
    print("\n=== Testing debug_timer (sequential) ===")
    
    buffer = io.StringIO()
    
    with redirect_stdout(buffer):
        with debug_timer("First") as t1:
            time.sleep(0.01)
        
        with debug_timer("Second") as t2:
            time.sleep(0.02)
        
        with debug_timer("Third") as t3:
            time.sleep(0.03)
    
    # Each should be independent
    assert t1["duration_ms"] < t2["duration_ms"] < t3["duration_ms"]
    
    output = buffer.getvalue()
    assert "First:" in output
    assert "Second:" in output
    assert "Third:" in output
    
    print(f"✓ t1={t1['duration_ms']:.0f}ms, t2={t2['duration_ms']:.0f}ms, t3={t3['duration_ms']:.0f}ms")


def test_debug_timer_special_characters():
    """Test debug_timer with special characters in operation name"""
    print("\n=== Testing debug_timer (special chars) ===")
    
    buffer = io.StringIO()
    
    operations = [
        "GET /api/v2/cmdb/firewall/address",
        "Create 'test-host'",
        "Delete [old-data]",
        "Update {config}",
    ]
    
    for op in operations:
        with redirect_stdout(buffer):
            with debug_timer(op) as timing:
                pass
        assert timing["operation"] == op
    
    print("✓ Special characters handled correctly")


if __name__ == "__main__":
    test_debug_timer_basic()
    test_debug_timer_default_name()
    test_debug_timer_timing_accuracy()
    test_debug_timer_no_sleep()
    test_debug_timer_exception_handling()
    test_debug_timer_nested()
    test_debug_timer_multiple_sequential()
    test_debug_timer_special_characters()
    
    print("\n" + "=" * 60)
    print("✅ All debug_timer tests passed!")
    print("=" * 60)
