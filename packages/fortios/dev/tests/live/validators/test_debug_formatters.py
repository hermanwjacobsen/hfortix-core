"""
Tests for hfortix_core debug formatters

Tests format_connection_stats and format_request_info functions.
"""

from hfortix_core import format_connection_stats, format_request_info
import time


def test_format_connection_stats_full():
    """Test format_connection_stats with all fields"""
    print("\n=== Testing format_connection_stats (full) ===")
    
    stats = {
        "http2_enabled": True,
        "max_connections": 100,
        "max_keepalive_connections": 20,
        "active_requests": 5,
        "total_requests": 1000,
        "pool_exhaustion_count": 2,
        "circuit_breaker_state": "closed",
        "consecutive_failures": 0,
        "last_failure_time": None,
    }
    
    result = format_connection_stats(stats)
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Should contain key information
    assert "100" in result  # max_connections
    assert "1000" in result  # total_requests
    assert "Connection" in result
    
    print(f"✓ Formatted stats:\n{result}")


def test_format_connection_stats_minimal():
    """Test format_connection_stats with minimal fields"""
    print("\n=== Testing format_connection_stats (minimal) ===")
    
    stats = {
        "active_requests": 0,
        "total_requests": 0,
    }
    
    result = format_connection_stats(stats)
    assert isinstance(result, str)
    
    print(f"✓ Minimal stats:\n{result}")


def test_format_connection_stats_none():
    """Test format_connection_stats with None"""
    print("\n=== Testing format_connection_stats (None) ===")
    
    result = format_connection_stats(None)
    assert isinstance(result, str)
    
    print(f"✓ None stats: {result}")


def test_format_connection_stats_empty():
    """Test format_connection_stats with empty dict"""
    print("\n=== Testing format_connection_stats (empty) ===")
    
    result = format_connection_stats({})
    assert isinstance(result, str)
    
    print(f"✓ Empty stats: {result}")


def test_format_connection_stats_circuit_breaker_open():
    """Test format_connection_stats with open circuit breaker"""
    print("\n=== Testing format_connection_stats (circuit breaker open) ===")
    
    stats = {
        "circuit_breaker_state": "open",
        "consecutive_failures": 5,
        "last_failure_time": time.time() - 30,
    }
    
    result = format_connection_stats(stats)
    assert isinstance(result, str)
    
    print(f"✓ Circuit breaker open:\n{result}")


def test_format_connection_stats_circuit_breaker_half_open():
    """Test format_connection_stats with half-open circuit breaker"""
    print("\n=== Testing format_connection_stats (circuit breaker half-open) ===")
    
    stats = {
        "circuit_breaker_state": "half-open",
        "consecutive_failures": 3,
    }
    
    result = format_connection_stats(stats)
    assert isinstance(result, str)
    
    print(f"✓ Circuit breaker half-open:\n{result}")


def test_format_request_info_full():
    """Test format_request_info with all fields"""
    print("\n=== Testing format_request_info (full) ===")
    
    request_info = {
        "method": "GET",
        "endpoint": "/api/v2/cmdb/firewall/policy",
        "params": {"vdom": "root", "filter": "name==test"},
        "data": None,
        "response_time_ms": 125.5,
        "status_code": 200,
        "timestamp": time.time(),
        "error": "",
    }
    
    result = format_request_info(request_info)
    assert isinstance(result, str)
    assert "GET" in result
    assert "policy" in result.lower() or "firewall" in result.lower()
    
    print(f"✓ Formatted request:\n{result}")


def test_format_request_info_with_error():
    """Test format_request_info with error"""
    print("\n=== Testing format_request_info (with error) ===")
    
    request_info = {
        "method": "POST",
        "endpoint": "/api/v2/cmdb/firewall/address",
        "params": None,
        "data": {"name": "test", "subnet": "10.0.0.0/24"},
        "response_time_ms": 50.0,
        "status_code": 500,
        "timestamp": time.time(),
        "error": "Internal server error",
    }
    
    result = format_request_info(request_info)
    assert isinstance(result, str)
    assert "POST" in result
    
    print(f"✓ Request with error:\n{result}")


def test_format_request_info_none():
    """Test format_request_info with None"""
    print("\n=== Testing format_request_info (None) ===")
    
    result = format_request_info(None)
    assert isinstance(result, str)
    
    print(f"✓ None request: {result}")


def test_format_request_info_empty():
    """Test format_request_info with empty dict"""
    print("\n=== Testing format_request_info (empty) ===")
    
    result = format_request_info({})
    assert isinstance(result, str)
    
    print(f"✓ Empty request: {result}")


def test_format_request_info_minimal():
    """Test format_request_info with minimal fields"""
    print("\n=== Testing format_request_info (minimal) ===")
    
    request_info = {
        "method": "GET",
        "endpoint": "/api/v2/monitor/system/status",
    }
    
    result = format_request_info(request_info)
    assert isinstance(result, str)
    assert "GET" in result
    
    print(f"✓ Minimal request:\n{result}")


def test_format_request_info_all_methods():
    """Test format_request_info with all HTTP methods"""
    print("\n=== Testing format_request_info (all methods) ===")
    
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    
    for method in methods:
        request_info = {
            "method": method,
            "endpoint": "/api/test",
            "status_code": 200,
        }
        result = format_request_info(request_info)
        assert method in result
        print(f"  ✓ {method}")
    
    print("✓ All HTTP methods formatted correctly")


def test_format_request_info_large_response_time():
    """Test format_request_info with large response time"""
    print("\n=== Testing format_request_info (large response time) ===")
    
    request_info = {
        "method": "GET",
        "endpoint": "/api/v2/monitor/system/ha-statistics",
        "response_time_ms": 30000.0,  # 30 seconds
        "status_code": 200,
    }
    
    result = format_request_info(request_info)
    assert isinstance(result, str)
    
    print(f"✓ Large response time:\n{result}")


if __name__ == "__main__":
    test_format_connection_stats_full()
    test_format_connection_stats_minimal()
    test_format_connection_stats_none()
    test_format_connection_stats_empty()
    test_format_connection_stats_circuit_breaker_open()
    test_format_connection_stats_circuit_breaker_half_open()
    test_format_request_info_full()
    test_format_request_info_with_error()
    test_format_request_info_none()
    test_format_request_info_empty()
    test_format_request_info_minimal()
    test_format_request_info_all_methods()
    test_format_request_info_large_response_time()
    
    print("\n" + "=" * 60)
    print("✅ All debug formatter tests passed!")
    print("=" * 60)
