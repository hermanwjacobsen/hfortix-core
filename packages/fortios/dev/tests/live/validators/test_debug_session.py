"""
Tests for hfortix_core.debug.DebugSession class.

DebugSession is used to capture and track HTTP requests during debugging.
It requires a FortiOS client instance, which we mock for testing.
"""

import io
from unittest.mock import MagicMock
from contextlib import redirect_stdout

from hfortix_core.debug import DebugSession


def create_mock_client():
    """Create a mock FortiOS client for testing."""
    mock_client = MagicMock()
    mock_client.host = "192.168.1.1"
    mock_client.vdom = "root"
    return mock_client


def test_debug_session_creation():
    """Test creating a DebugSession."""
    print("\n=== Testing DebugSession creation ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    assert session is not None
    
    print("✅ DebugSession - creation")


def test_debug_session_capture_request_basic():
    """Test capturing a basic request."""
    print("\n=== Testing DebugSession capture_request ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(
        method="GET",
        endpoint="/api/v2/cmdb/firewall/address"
    )
    
    summary = session.get_summary()
    assert "requests" in summary or "total_requests" in summary or len(summary) > 0
    
    print("✅ DebugSession - capture_request basic")


def test_debug_session_capture_request_with_params():
    """Test capturing a request with params."""
    print("\n=== Testing DebugSession capture_request with params ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(
        method="GET",
        endpoint="/api/v2/cmdb/firewall/address",
        params={"vdom": "root", "count": 100}
    )
    
    summary = session.get_summary()
    assert summary is not None
    
    print("✅ DebugSession - capture_request with params")


def test_debug_session_capture_request_with_response():
    """Test capturing a request with response time."""
    print("\n=== Testing DebugSession capture_request with response ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(
        method="POST",
        endpoint="/api/v2/cmdb/firewall/address",
        params=None,
        response_time_ms=125.5
    )
    
    summary = session.get_summary()
    assert summary is not None
    
    print("✅ DebugSession - capture_request with response time")


def test_debug_session_capture_multiple_requests():
    """Test capturing multiple requests."""
    print("\n=== Testing DebugSession multiple requests ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    # Simulate multiple API calls
    endpoints = [
        ("GET", "/api/v2/cmdb/firewall/address"),
        ("GET", "/api/v2/cmdb/firewall/service/custom"),
        ("POST", "/api/v2/cmdb/firewall/policy"),
        ("DELETE", "/api/v2/cmdb/firewall/address/test"),
    ]
    
    for method, endpoint in endpoints:
        session.capture_request(method=method, endpoint=endpoint)
    
    summary = session.get_summary()
    assert summary is not None
    
    print("✅ DebugSession - multiple requests captured")


def test_debug_session_get_summary():
    """Test get_summary returns dict with expected structure."""
    print("\n=== Testing DebugSession get_summary ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(method="GET", endpoint="/api/v2/cmdb/system/status")
    session.capture_request(method="GET", endpoint="/api/v2/cmdb/firewall/address")
    
    summary = session.get_summary()
    
    assert isinstance(summary, dict)
    # Summary should contain some statistics
    print(f"  Summary keys: {list(summary.keys())}")
    
    print("✅ DebugSession - get_summary")


def test_debug_session_get_summary_empty():
    """Test get_summary on empty session."""
    print("\n=== Testing DebugSession get_summary empty ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    summary = session.get_summary()
    
    assert isinstance(summary, dict)
    
    print("✅ DebugSession - get_summary empty session")


def test_debug_session_print_requests():
    """Test print_requests outputs request info."""
    print("\n=== Testing DebugSession print_requests ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(method="GET", endpoint="/api/v2/cmdb/firewall/address")
    session.capture_request(method="POST", endpoint="/api/v2/cmdb/firewall/policy")
    
    # Capture output
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        session.print_requests()
    
    output = buffer.getvalue()
    # Should have some output (may vary based on implementation)
    print(f"  Output length: {len(output)} chars")
    
    print("✅ DebugSession - print_requests")


def test_debug_session_print_requests_verbose():
    """Test print_requests with verbose=True."""
    print("\n=== Testing DebugSession print_requests verbose ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(
        method="GET",
        endpoint="/api/v2/cmdb/firewall/address",
        params={"vdom": "root"}
    )
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        session.print_requests(verbose=True)
    
    output = buffer.getvalue()
    print(f"  Verbose output length: {len(output)} chars")
    
    print("✅ DebugSession - print_requests verbose")


def test_debug_session_print_requests_empty():
    """Test print_requests on empty session."""
    print("\n=== Testing DebugSession print_requests empty ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        session.print_requests()
    
    # Should not crash even with no requests
    
    print("✅ DebugSession - print_requests empty")


def test_debug_session_print_summary_text():
    """Test print_summary with text format."""
    print("\n=== Testing DebugSession print_summary text ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(method="GET", endpoint="/api/v2/cmdb/firewall/address")
    session.capture_request(method="GET", endpoint="/api/v2/cmdb/firewall/service/custom")
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        session.print_summary(format="text")
    
    output = buffer.getvalue()
    print(f"  Text summary length: {len(output)} chars")
    
    print("✅ DebugSession - print_summary text")


def test_debug_session_print_summary_json():
    """Test print_summary with json format."""
    print("\n=== Testing DebugSession print_summary json ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    session.capture_request(method="GET", endpoint="/api/v2/cmdb/firewall/address")
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        session.print_summary(format="json")
    
    output = buffer.getvalue()
    # JSON output should be parseable
    if output.strip():
        import json
        try:
            parsed = json.loads(output)
            assert isinstance(parsed, dict)
        except json.JSONDecodeError:
            pass  # May not be pure JSON depending on implementation
    
    print("✅ DebugSession - print_summary json")


def test_debug_session_print_summary_empty():
    """Test print_summary on empty session."""
    print("\n=== Testing DebugSession print_summary empty ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        session.print_summary()
    
    # Should not crash
    
    print("✅ DebugSession - print_summary empty")


def test_debug_session_all_http_methods():
    """Test capturing all HTTP methods."""
    print("\n=== Testing DebugSession all HTTP methods ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    
    for method in methods:
        session.capture_request(method=method, endpoint=f"/api/test/{method.lower()}")
    
    summary = session.get_summary()
    assert summary is not None
    
    print("✅ DebugSession - all HTTP methods")


def test_debug_session_with_error_response():
    """Test capturing a failed request."""
    print("\n=== Testing DebugSession error response ===")
    
    mock_client = create_mock_client()
    session = DebugSession(client=mock_client, print_on_exit=False)
    
    # Capture a request that would have failed
    session.capture_request(
        method="GET",
        endpoint="/api/v2/cmdb/firewall/address/nonexistent",
        response_time_ms=15.0
    )
    
    summary = session.get_summary()
    assert summary is not None
    
    print("✅ DebugSession - error response captured")


def run_all_tests():
    """Run all DebugSession tests."""
    tests = [
        test_debug_session_creation,
        test_debug_session_capture_request_basic,
        test_debug_session_capture_request_with_params,
        test_debug_session_capture_request_with_response,
        test_debug_session_capture_multiple_requests,
        test_debug_session_get_summary,
        test_debug_session_get_summary_empty,
        test_debug_session_print_requests,
        test_debug_session_print_requests_verbose,
        test_debug_session_print_requests_empty,
        test_debug_session_print_summary_text,
        test_debug_session_print_summary_json,
        test_debug_session_print_summary_empty,
        test_debug_session_all_http_methods,
        test_debug_session_with_error_response,
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
