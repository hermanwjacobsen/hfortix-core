#!/usr/bin/env python3
"""
Test script to verify http_api_request and fmg_api_request properties work correctly.

This test validates that request information is properly tracked and exposed through
both http_api_request and fmg_api_request properties on all response types:
- FortiObject
- FortiObjectList
- ContentResponse
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from packages.fortios.hfortix_fortios.models import (
    FortiObject,
    FortiObjectList,
    ContentResponse,
    process_response
)


def test_fortiobject_http_api_request():
    """Test FortiObject with http_api_request property."""
    print("=" * 70)
    print("Test 1: FortiObject with http_api_request")
    print("=" * 70)

    request_info = {
        "method": "GET",
        "url": "https://192.168.1.99/api/v2/cmdb/firewall/address/test",
        "endpoint": "/api/v2/cmdb/firewall/address/test",
        "params": {"vdom": "root"},
        "data": None,
        "timestamp": 1706889600.123
    }

    data = {"name": "test", "subnet": "10.0.0.1 255.255.255.255"}
    obj = FortiObject(data, request_info=request_info)

    print(f"Object name: {obj.name}")
    print(f"Object subnet: {obj.subnet}")
    print(f"\nHTTP API Request Info:")
    print(f"  {obj.http_api_request}")
    
    assert obj.http_api_request == request_info
    assert obj.http_api_request['method'] == 'GET'
    assert obj.http_api_request['url'] == "https://192.168.1.99/api/v2/cmdb/firewall/address/test"
    print("✅ Test 1 passed!")


def test_fortiobject_fmg_api_request():
    """Test FortiObject with fmg_api_request property (alias for http_api_request)."""
    print("\n" + "=" * 70)
    print("Test 2: FortiObject with fmg_api_request")
    print("=" * 70)

    request_info = {
        "method": "GET",
        "url": "https://fmg.example.com/jsonrpc",
        "endpoint": "/api/v2/cmdb/firewall/address/test",
        "params": {"vdom": "root"},
        "data": {"method": "get", "params": [{"url": "/pm/config/device/FGT-01/..."}]},
        "timestamp": 1706889600.123
    }

    data = {"name": "test", "subnet": "10.0.0.1 255.255.255.255"}
    obj = FortiObject(data, request_info=request_info)

    print(f"Object name: {obj.name}")
    print(f"Object subnet: {obj.subnet}")
    print(f"\nFMG API Request Info:")
    print(f"  {obj.fmg_api_request}")
    
    assert obj.fmg_api_request == request_info
    assert obj.fmg_api_request == obj.http_api_request  # They should be the same
    assert obj.fmg_api_request['method'] == 'GET'
    assert obj.fmg_api_request['url'] == "https://fmg.example.com/jsonrpc"
    print("✅ Test 2 passed!")


def test_fortiobjectlist_http_api_request():
    """Test FortiObjectList with http_api_request property."""
    print("\n" + "=" * 70)
    print("Test 3: FortiObjectList with http_api_request")
    print("=" * 70)

    request_info = {
        "method": "GET",
        "url": "https://192.168.1.99/api/v2/cmdb/firewall/policy",
        "endpoint": "/api/v2/cmdb/firewall/policy",
        "params": {"filter": "srcaddr==internal", "vdom": "root"},
        "data": None,
        "timestamp": 1706889601.456
    }

    policies_data = [
        {"policyid": 1, "name": "policy1"},
        {"policyid": 2, "name": "policy2"}
    ]

    policies = FortiObjectList(
        [FortiObject(p, request_info=request_info) for p in policies_data],
        request_info=request_info
    )

    print(f"Number of policies: {len(policies)}")
    print(f"First policy name: {policies[0].name}")
    print(f"\nHTTP API Request Info (from list):")
    print(f"  {policies.http_api_request}")
    print(f"\nHTTP API Request Info (from first item):")
    print(f"  {policies[0].http_api_request}")
    
    assert policies.http_api_request == request_info
    assert policies[0].http_api_request == request_info
    assert policies.http_api_request['params']['filter'] == "srcaddr==internal"
    print("✅ Test 3 passed!")


def test_fortiobjectlist_fmg_api_request():
    """Test FortiObjectList with fmg_api_request property."""
    print("\n" + "=" * 70)
    print("Test 4: FortiObjectList with fmg_api_request")
    print("=" * 70)

    request_info = {
        "method": "GET",
        "url": "https://fmg.example.com/jsonrpc",
        "endpoint": "/api/v2/cmdb/firewall/policy",
        "params": {"vdom": "root"},
        "data": {"method": "get", "params": [{"url": "/pm/config/device/FGT-01/..."}]},
        "timestamp": 1706889601.456
    }

    policies_data = [
        {"policyid": 1, "name": "policy1"},
        {"policyid": 2, "name": "policy2"}
    ]

    policies = FortiObjectList(
        [FortiObject(p, request_info=request_info) for p in policies_data],
        request_info=request_info
    )

    print(f"Number of policies: {len(policies)}")
    print(f"First policy name: {policies[0].name}")
    print(f"\nFMG API Request Info (from list):")
    print(f"  {policies.fmg_api_request}")
    print(f"\nFMG API Request Info (from first item):")
    print(f"  {policies[0].fmg_api_request}")
    
    assert policies.fmg_api_request == request_info
    assert policies.fmg_api_request == policies.http_api_request  # Alias
    assert policies[0].fmg_api_request == request_info
    print("✅ Test 4 passed!")


def test_process_response_http_api_request():
    """Test process_response with http_api_request."""
    print("\n" + "=" * 70)
    print("Test 5: process_response with http_api_request")
    print("=" * 70)

    request_info = {
        "method": "POST",
        "url": "https://192.168.1.99/api/v2/cmdb/firewall/address",
        "endpoint": "/api/v2/cmdb/firewall/address",
        "params": {"vdom": "root"},
        "data": {"name": "webserver", "subnet": "10.0.1.100/32"},
        "timestamp": 1706889602.789
    }

    result = {
        "http_status": 200,
        "status": "success",
        "results": [
            {"name": "webserver", "subnet": "10.0.1.100 255.255.255.255"}
        ]
    }

    processed = process_response(
        result,
        raw_envelope=result,
        response_time=0.045,
        request_info=request_info
    )

    print(f"Processed type: {type(processed)}")
    if hasattr(processed, 'http_api_request'):
        print(f"HTTP API Request Info:")
        print(f"  Method: {processed.http_api_request.get('method')}")
        print(f"  URL: {processed.http_api_request.get('url')}")
        print(f"  Data: {processed.http_api_request.get('data')}")
    
    assert hasattr(processed, 'http_api_request')
    assert processed.http_api_request == request_info
    assert processed.http_api_request['method'] == 'POST'
    assert processed.http_api_request['data']['name'] == 'webserver'
    print("✅ Test 5 passed!")


def test_process_response_fmg_api_request():
    """Test process_response with fmg_api_request."""
    print("\n" + "=" * 70)
    print("Test 6: process_response with fmg_api_request")
    print("=" * 70)

    request_info = {
        "method": "POST",
        "url": "https://fmg.example.com/jsonrpc",
        "endpoint": "/api/v2/cmdb/firewall/address",
        "params": {"vdom": "root"},
        "data": {"method": "set", "params": [{"url": "/pm/config/device/FGT-01/..."}]},
        "timestamp": 1706889602.789
    }

    result = {
        "http_status": 200,
        "status": "success",
        "results": [
            {"name": "webserver", "subnet": "10.0.1.100 255.255.255.255"}
        ]
    }

    processed = process_response(
        result,
        raw_envelope=result,
        response_time=0.045,
        request_info=request_info
    )

    print(f"Processed type: {type(processed)}")
    if hasattr(processed, 'fmg_api_request'):
        print(f"FMG API Request Info:")
        print(f"  Method: {processed.fmg_api_request.get('method')}")
        print(f"  URL: {processed.fmg_api_request.get('url')}")
        print(f"  Data method: {processed.fmg_api_request.get('data', {}).get('method')}")
    
    assert hasattr(processed, 'fmg_api_request')
    assert processed.fmg_api_request == request_info
    assert processed.fmg_api_request == processed.http_api_request  # Alias
    assert processed.fmg_api_request['url'] == 'https://fmg.example.com/jsonrpc'
    print("✅ Test 6 passed!")


def test_unwrapped_response():
    """Test unwrapped single response with request_info."""
    print("\n" + "=" * 70)
    print("Test 7: Unwrapped single response with request_info")
    print("=" * 70)

    request_info = {
        "method": "POST",
        "url": "https://192.168.1.99/api/v2/cmdb/firewall/address",
        "endpoint": "/api/v2/cmdb/firewall/address",
        "params": {"vdom": "root"},
        "data": {"name": "webserver", "subnet": "10.0.1.100/32"},
        "timestamp": 1706889602.789
    }

    result = {
        "http_status": 200,
        "status": "success",
        "results": [
            {"name": "webserver", "subnet": "10.0.1.100 255.255.255.255"}
        ]
    }

    unwrapped = process_response(
        result,
        unwrap_single=True,
        raw_envelope=result,
        response_time=0.032,
        request_info=request_info
    )

    print(f"Unwrapped type: {type(unwrapped)}")
    print(f"Name: {unwrapped.name}")
    print(f"HTTP API Request Info:")
    print(f"  {unwrapped.http_api_request}")
    print(f"FMG API Request Info:")
    print(f"  {unwrapped.fmg_api_request}")
    
    assert unwrapped.http_api_request == request_info
    assert unwrapped.fmg_api_request == request_info
    assert unwrapped.http_api_request == unwrapped.fmg_api_request
    print("✅ Test 7 passed!")


def test_contentresponse_with_request_info():
    """Test ContentResponse with request_info."""
    print("\n" + "=" * 70)
    print("Test 8: ContentResponse with request_info")
    print("=" * 70)

    request_info = {
        "method": "GET",
        "url": "https://192.168.1.99/api/v2/monitor/system/config/revision/file",
        "endpoint": "/api/v2/monitor/system/config/revision/file",
        "params": {"config_id": 45, "vdom": "root"},
        "data": None,
        "timestamp": 1706889603.123
    }

    result = {
        "http_status": 200,
        "status": "success",
        "results": "...config file content..."
    }

    # Simulate what happens for non-list results (like monitor endpoints)
    # ContentResponse expects data dict with 'content' and 'content_type'
    data = {
        "content": b"...config file content...",
        "content_type": "text/plain"
    }
    content = ContentResponse(
        data=data,
        raw_envelope=result,
        response_time=0.056,
        request_info=request_info
    )

    print(f"Content type: {type(content)}")
    print(f"Content length: {len(content.content)}")
    print(f"\nHTTP API Request Info:")
    print(f"  {content.http_api_request}")
    print(f"\nFMG API Request Info:")
    print(f"  {content.fmg_api_request}")
    
    assert content.http_api_request == request_info
    assert content.fmg_api_request == request_info
    assert content.http_api_request['params']['config_id'] == 45
    print("✅ Test 8 passed!")


def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("API Request Properties Test Suite")
    print("Testing http_api_request and fmg_api_request properties")
    print("=" * 70 + "\n")

    try:
        test_fortiobject_http_api_request()
        test_fortiobject_fmg_api_request()
        test_fortiobjectlist_http_api_request()
        test_fortiobjectlist_fmg_api_request()
        test_process_response_http_api_request()
        test_process_response_fmg_api_request()
        test_unwrapped_response()
        test_contentresponse_with_request_info()

        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED!")
        print("=" * 70)
        return 0
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
