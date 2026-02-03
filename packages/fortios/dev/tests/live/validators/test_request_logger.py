"""
Tests for hfortix_core.logging.RequestLogger class.

RequestLogger provides structured logging for HTTP requests.
Requires method and endpoint parameters for initialization.
"""

import io
import logging
from contextlib import redirect_stdout

from hfortix_core.logging import RequestLogger


def test_request_logger_creation():
    """Test creating a RequestLogger."""
    print("\n=== Testing RequestLogger creation ===")
    
    logger = RequestLogger(method="GET", endpoint="/api/v2/cmdb/firewall/address")
    assert logger is not None
    
    print("✅ RequestLogger - creation")


def test_request_logger_with_extra():
    """Test creating a RequestLogger with extra data."""
    print("\n=== Testing RequestLogger with extra ===")
    
    logger = RequestLogger(
        method="POST",
        endpoint="/api/v2/cmdb/firewall/policy",
        extra={"vdom": "root", "params": {"count": 100}}
    )
    assert logger is not None
    
    print("✅ RequestLogger - with extra")


def test_request_logger_all_methods():
    """Test RequestLogger with all HTTP methods."""
    print("\n=== Testing RequestLogger all methods ===")
    
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    
    for method in methods:
        logger = RequestLogger(method=method, endpoint="/api/test")
        assert logger is not None
    
    print("✅ RequestLogger - all HTTP methods")


def test_request_logger_various_endpoints():
    """Test RequestLogger with various endpoints."""
    print("\n=== Testing RequestLogger various endpoints ===")
    
    endpoints = [
        "/api/v2/cmdb/firewall/address",
        "/api/v2/cmdb/firewall/policy/1",
        "/api/v2/monitor/system/status",
        "/api/v2/cmdb/system/interface",
    ]
    
    for endpoint in endpoints:
        logger = RequestLogger(method="GET", endpoint=endpoint)
        assert logger is not None
    
    print("✅ RequestLogger - various endpoints")


def test_request_logger_class_exists():
    """Test that RequestLogger class has expected interface."""
    print("\n=== Testing RequestLogger interface ===")
    
    # Check class exists
    assert RequestLogger is not None
    
    # Check it's a class
    assert isinstance(RequestLogger, type)
    
    print("✅ RequestLogger - class exists")


def test_request_logger_import():
    """Test RequestLogger can be imported from multiple paths."""
    print("\n=== Testing RequestLogger import ===")
    
    from hfortix_core.logging import RequestLogger as RL1
    from hfortix_core import RequestLogger as RL2
    
    assert RL1 is not None
    assert RL2 is not None
    
    print("✅ RequestLogger - import from multiple paths")


def test_request_logger_empty_extra():
    """Test RequestLogger with empty extra dict."""
    print("\n=== Testing RequestLogger empty extra ===")
    
    logger = RequestLogger(
        method="GET",
        endpoint="/api/test",
        extra={}
    )
    assert logger is not None
    
    print("✅ RequestLogger - empty extra")


def test_request_logger_none_extra():
    """Test RequestLogger with None extra."""
    print("\n=== Testing RequestLogger None extra ===")
    
    logger = RequestLogger(
        method="GET",
        endpoint="/api/test",
        extra=None
    )
    assert logger is not None
    
    print("✅ RequestLogger - None extra")


def run_all_tests():
    """Run all RequestLogger tests."""
    tests = [
        test_request_logger_creation,
        test_request_logger_with_extra,
        test_request_logger_all_methods,
        test_request_logger_various_endpoints,
        test_request_logger_class_exists,
        test_request_logger_import,
        test_request_logger_empty_extra,
        test_request_logger_none_extra,
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
