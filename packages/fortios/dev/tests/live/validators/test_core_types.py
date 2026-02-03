"""
Tests for hfortix_core.types TypedDicts.

Tests the response type structures:
- ConnectionStats
- RequestInfo
- APIResponse
- ListResponse
- ObjectResponse
- ErrorResponse
- MutationResponse
- MutationResponseFull
- RawAPIResponse
"""

from typing import cast, get_type_hints
from hfortix_core.types import (
    CircuitBreakerState,
    ConnectionStats,
    RequestInfo,
    APIResponse,
    ListResponse,
    ObjectResponse,
    ErrorResponse,
)


def test_connection_stats_is_typeddict():
    """Test ConnectionStats is a TypedDict."""
    print("\n=== Testing ConnectionStats TypedDict ===")
    
    # Should have __annotations__
    assert hasattr(ConnectionStats, '__annotations__')
    
    annotations = ConnectionStats.__annotations__
    assert 'http2_enabled' in annotations
    assert 'max_connections' in annotations
    assert 'total_requests' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ ConnectionStats - is TypedDict")


def test_connection_stats_can_be_created():
    """Test ConnectionStats dict can be created."""
    print("\n=== Testing ConnectionStats creation ===")
    
    stats: ConnectionStats = {
        'http2_enabled': True,
        'max_connections': 100,
        'max_keepalive_connections': 20,
        'active_requests': 5,
        'total_requests': 1000,
        'pool_exhaustion_count': 0,
        'circuit_breaker_state': 'closed',
        'consecutive_failures': 0,
        'last_failure_time': None,
    }
    
    assert stats['http2_enabled'] is True
    assert stats['max_connections'] == 100
    assert stats['circuit_breaker_state'] == 'closed'
    
    print("✅ ConnectionStats - can be created")


def test_connection_stats_circuit_breaker_states():
    """Test ConnectionStats circuit_breaker_state values."""
    print("\n=== Testing ConnectionStats circuit_breaker_state ===")
    
    valid_states = ['closed', 'open', 'half-open']
    
    for state in valid_states:
        stats: ConnectionStats = {
            'http2_enabled': True,
            'max_connections': 100,
            'max_keepalive_connections': 20,
            'active_requests': 0,
            'total_requests': 0,
            'pool_exhaustion_count': 0,
            'circuit_breaker_state': cast(CircuitBreakerState, state),
            'consecutive_failures': 0,
            'last_failure_time': None,
        }
        assert stats['circuit_breaker_state'] == state
    
    print("✅ ConnectionStats - circuit_breaker_state values")


def test_request_info_is_typeddict():
    """Test RequestInfo is a TypedDict."""
    print("\n=== Testing RequestInfo TypedDict ===")
    
    assert hasattr(RequestInfo, '__annotations__')
    
    annotations = RequestInfo.__annotations__
    assert 'method' in annotations
    assert 'endpoint' in annotations
    assert 'timestamp' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ RequestInfo - is TypedDict")


def test_request_info_can_be_created():
    """Test RequestInfo dict can be created."""
    print("\n=== Testing RequestInfo creation ===")
    
    import time
    
    info: RequestInfo = {
        'method': 'GET',
        'endpoint': '/api/v2/cmdb/firewall/address',
        'params': {'vdom': 'root'},
        'data': None,
        'response_time_ms': 125.5,
        'status_code': 200,
        'timestamp': time.time(),
        'error': '',
    }
    
    assert info['method'] == 'GET'
    assert info['endpoint'] == '/api/v2/cmdb/firewall/address'
    assert info['status_code'] == 200
    
    print("✅ RequestInfo - can be created")


def test_request_info_various_methods():
    """Test RequestInfo with various HTTP methods."""
    print("\n=== Testing RequestInfo various methods ===")
    
    import time
    
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
    
    for method in methods:
        info: RequestInfo = {
            'method': method,
            'endpoint': '/api/test',
            'params': None,
            'data': None,
            'response_time_ms': None,
            'status_code': None,
            'timestamp': time.time(),
            'error': '',
        }
        assert info['method'] == method
    
    print("✅ RequestInfo - various methods")


def test_api_response_is_typeddict():
    """Test APIResponse is a TypedDict."""
    print("\n=== Testing APIResponse TypedDict ===")
    
    assert hasattr(APIResponse, '__annotations__')
    
    annotations = APIResponse.__annotations__
    assert 'http_status' in annotations
    assert 'results' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ APIResponse - is TypedDict")


def test_api_response_can_be_created():
    """Test APIResponse dict can be created."""
    print("\n=== Testing APIResponse creation ===")
    
    response: APIResponse = {
        'http_status': 200,
        'results': [{'name': 'test'}],
        'revision': '12345',
        'revision_changed': False,
        'old_revision': '12344',
        'vdom': 'root',
        'path': 'firewall',
        'name': 'address',
        'status': 'success',
        'http_method': 'GET',
        'serial': 'FGT123456789',
        'version': 'v7.2.0',
        'build': 1234,
        'mkey': 'test-address',
    }
    
    assert response['http_status'] == 200
    assert response['status'] == 'success'
    
    print("✅ APIResponse - can be created")


def test_list_response_is_typeddict():
    """Test ListResponse is a TypedDict."""
    print("\n=== Testing ListResponse TypedDict ===")
    
    assert hasattr(ListResponse, '__annotations__')
    
    annotations = ListResponse.__annotations__
    assert 'results' in annotations
    # Results should be list type
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ ListResponse - is TypedDict")


def test_list_response_can_be_created():
    """Test ListResponse dict can be created."""
    print("\n=== Testing ListResponse creation ===")
    
    response: ListResponse = {
        'http_status': 200,
        'results': [
            {'name': 'addr1', 'type': 'subnet'},
            {'name': 'addr2', 'type': 'fqdn'},
        ],
        'vdom': 'root',
        'path': 'firewall',
        'name': 'address',
        'status': 'success',
        'serial': 'FGT123456789',
        'version': 'v7.2.0',
        'build': 1234,
    }
    
    assert response['http_status'] == 200
    assert len(response['results']) == 2
    assert isinstance(response['results'], list)
    
    print("✅ ListResponse - can be created")


def test_object_response_is_typeddict():
    """Test ObjectResponse is a TypedDict."""
    print("\n=== Testing ObjectResponse TypedDict ===")
    
    assert hasattr(ObjectResponse, '__annotations__')
    
    annotations = ObjectResponse.__annotations__
    assert 'results' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ ObjectResponse - is TypedDict")


def test_object_response_can_be_created():
    """Test ObjectResponse dict can be created."""
    print("\n=== Testing ObjectResponse creation ===")
    
    response: ObjectResponse = {
        'http_status': 200,
        'results': {'name': 'test-address', 'type': 'subnet', 'subnet': '10.0.0.0/8'},
        'vdom': 'root',
        'path': 'firewall',
        'name': 'address',
        'status': 'success',
        'serial': 'FGT123456789',
        'version': 'v7.2.0',
        'build': 1234,
    }
    
    assert response['http_status'] == 200
    assert isinstance(response['results'], dict)
    assert response['results']['name'] == 'test-address'
    
    print("✅ ObjectResponse - can be created")


def test_error_response_is_typeddict():
    """Test ErrorResponse is a TypedDict."""
    print("\n=== Testing ErrorResponse TypedDict ===")
    
    assert hasattr(ErrorResponse, '__annotations__')
    
    annotations = ErrorResponse.__annotations__
    assert 'http_status' in annotations
    assert 'error' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ ErrorResponse - is TypedDict")


def test_error_response_can_be_created():
    """Test ErrorResponse dict can be created."""
    print("\n=== Testing ErrorResponse creation ===")
    
    response: ErrorResponse = {
        'http_status': 404,
        'error': -3,
        'errorcode': -3,
        'message': 'Entry not found',
        'vdom': 'root',
    }
    
    assert response['http_status'] == 404
    assert response['error'] == -3
    assert 'not found' in response['message'].lower()
    
    print("✅ ErrorResponse - can be created")


def test_error_response_common_codes():
    """Test ErrorResponse with common FortiOS error codes."""
    print("\n=== Testing ErrorResponse common codes ===")
    
    error_codes = {
        -3: 'Entry not found',
        -5: 'Duplicate entry',
        -6: 'Invalid value',
        -10: 'Object in use',
        -15: 'Permission denied',
    }
    
    for code, msg in error_codes.items():
        response: ErrorResponse = {
            'http_status': 400,
            'error': code,
            'errorcode': code,
            'message': msg,
            'vdom': 'root',
        }
        assert response['error'] == code
    
    print("✅ ErrorResponse - common codes")


def run_all_tests():
    """Run all type tests."""
    tests = [
        test_connection_stats_is_typeddict,
        test_connection_stats_can_be_created,
        test_connection_stats_circuit_breaker_states,
        test_request_info_is_typeddict,
        test_request_info_can_be_created,
        test_request_info_various_methods,
        test_api_response_is_typeddict,
        test_api_response_can_be_created,
        test_list_response_is_typeddict,
        test_list_response_can_be_created,
        test_object_response_is_typeddict,
        test_object_response_can_be_created,
        test_error_response_is_typeddict,
        test_error_response_can_be_created,
        test_error_response_common_codes,
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
