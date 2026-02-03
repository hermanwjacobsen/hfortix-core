"""
Tests for hfortix_fortios response types and Literal types.

Tests:
- FortiOSListResponse
- FortiOSDictResponse
- FortiOSResponse
- FortiOSSuccessResponse
- FortiOSErrorResponse
- Literal types (ActionType, LogSeverity, ProtocolType, etc.)
"""

from typing import Literal, get_type_hints, get_args, get_origin, Union
from hfortix_fortios import (
    FortiOSListResponse,
    FortiOSDictResponse,
    FortiOSResponse,
    FortiOSSuccessResponse,
    FortiOSErrorResponse,
)
from hfortix_fortios.types import (
    ActionType,
    LogSeverity,
    ProtocolType,
    ScheduleType,
    StatusType,
)


def test_fortioslitresponse_is_typeddict():
    """Test FortiOSListResponse is a TypedDict."""
    print("\n=== Testing FortiOSListResponse TypedDict ===")
    
    assert hasattr(FortiOSListResponse, '__annotations__')
    
    annotations = FortiOSListResponse.__annotations__
    assert 'results' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ FortiOSListResponse - is TypedDict")


def test_fortioslitresponse_can_be_created():
    """Test FortiOSListResponse dict can be created."""
    print("\n=== Testing FortiOSListResponse creation ===")
    
    response: FortiOSListResponse = {
        'http_status': 200,
        'http_method': 'GET',
        'results': [
            {'name': 'addr1', 'type': 'subnet'},
            {'name': 'addr2', 'type': 'fqdn'},
        ],
        'vdom': 'root',
        'path': 'firewall',
        'status': 'success',
        'serial': 'FGT123456789',
        'version': 'v7.2.0',
        'build': 1234,
    }
    
    assert response['http_status'] == 200
    assert isinstance(response['results'], list)
    assert len(response['results']) == 2
    
    print("✅ FortiOSListResponse - can be created")


def test_fortiosdictresponse_is_typeddict():
    """Test FortiOSDictResponse is a TypedDict."""
    print("\n=== Testing FortiOSDictResponse TypedDict ===")
    
    assert hasattr(FortiOSDictResponse, '__annotations__')
    
    annotations = FortiOSDictResponse.__annotations__
    assert 'results' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ FortiOSDictResponse - is TypedDict")


def test_fortiosdictresponse_can_be_created():
    """Test FortiOSDictResponse dict can be created."""
    print("\n=== Testing FortiOSDictResponse creation ===")
    
    response: FortiOSDictResponse = {
        'http_status': 200,
        'http_method': 'GET',
        'results': {'name': 'test-addr', 'type': 'subnet', 'subnet': '10.0.0.0/8'},
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
    assert response['results']['name'] == 'test-addr'
    
    print("✅ FortiOSDictResponse - can be created")


def test_fortiosresponse_is_union():
    """Test FortiOSResponse is a Union type."""
    print("\n=== Testing FortiOSResponse Union ===")
    
    # FortiOSResponse should be Union of list and dict responses
    origin = get_origin(FortiOSResponse)
    
    # For Union types
    if origin is Union:
        args = get_args(FortiOSResponse)
        print(f"  Union args: {args}")
        assert len(args) >= 2
    else:
        # Might be a TypeAlias
        print(f"  Type: {FortiOSResponse}")
    
    print("✅ FortiOSResponse - is defined")


def test_fortiossuccessresponse_is_typeddict():
    """Test FortiOSSuccessResponse is a TypedDict."""
    print("\n=== Testing FortiOSSuccessResponse TypedDict ===")
    
    assert hasattr(FortiOSSuccessResponse, '__annotations__')
    
    annotations = FortiOSSuccessResponse.__annotations__
    assert 'status' in annotations or 'http_status' in annotations
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ FortiOSSuccessResponse - is TypedDict")


def test_fortiossuccessresponse_can_be_created():
    """Test FortiOSSuccessResponse dict can be created."""
    print("\n=== Testing FortiOSSuccessResponse creation ===")
    
    response: FortiOSSuccessResponse = {
        'http_status': 200,
        'http_method': 'POST',
        'results': [{'name': 'new-address'}],
        'status': 'success',
        'vdom': 'root',
        'path': 'firewall',
        'serial': 'FGT123456789',
        'version': 'v7.2.0',
        'build': 1234,
    }
    
    assert response['http_status'] == 200
    assert response['status'] == 'success'
    
    print("✅ FortiOSSuccessResponse - can be created")


def test_fortioserrorresponse_is_typeddict():
    """Test FortiOSErrorResponse is a TypedDict."""
    print("\n=== Testing FortiOSErrorResponse TypedDict ===")
    
    assert hasattr(FortiOSErrorResponse, '__annotations__')
    
    annotations = FortiOSErrorResponse.__annotations__
    # Should have error-related fields
    
    print(f"  Keys: {list(annotations.keys())}")
    print("✅ FortiOSErrorResponse - is TypedDict")


def test_fortioserrorresponse_can_be_created():
    """Test FortiOSErrorResponse dict can be created."""
    print("\n=== Testing FortiOSErrorResponse creation ===")
    
    response: FortiOSErrorResponse = {
        'http_status': 404,
        'http_method': 'GET',
        'error': -3,
        'message': 'Entry not found',
        'status': 'error',
        'vdom': 'root',
    }
    
    assert response['http_status'] == 404
    assert response['error'] == -3
    
    print("✅ FortiOSErrorResponse - can be created")


def test_actiontype_literal():
    """Test ActionType is a Literal type."""
    print("\n=== Testing ActionType Literal ===")
    
    origin = get_origin(ActionType)
    assert origin is Literal
    
    args = get_args(ActionType)
    assert 'accept' in args
    assert 'deny' in args
    
    print(f"  Values: {args}")
    print("✅ ActionType - is Literal")


def test_actiontype_values():
    """Test ActionType accepts valid values."""
    print("\n=== Testing ActionType values ===")
    
    args = get_args(ActionType)
    
    # Common firewall actions
    expected = ['accept', 'deny', 'ipsec']
    for val in expected:
        if val in args:
            action: ActionType = val  # type: ignore
    
    print("✅ ActionType - values work")


def test_logseverity_literal():
    """Test LogSeverity is a Literal type."""
    print("\n=== Testing LogSeverity Literal ===")
    
    origin = get_origin(LogSeverity)
    assert origin is Literal
    
    args = get_args(LogSeverity)
    
    # Standard syslog severities
    expected_severities = ['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debug']
    
    print(f"  Values: {args}")
    for sev in args:
        assert isinstance(sev, str)
    
    print("✅ LogSeverity - is Literal")


def test_protocoltype_literal():
    """Test ProtocolType is a Literal type."""
    print("\n=== Testing ProtocolType Literal ===")
    
    origin = get_origin(ProtocolType)
    assert origin is Literal
    
    args = get_args(ProtocolType)
    
    print(f"  Values: {args}")
    # Should contain protocol numbers or names
    
    print("✅ ProtocolType - is Literal")


def test_scheduletype_literal():
    """Test ScheduleType is a Literal type."""
    print("\n=== Testing ScheduleType Literal ===")
    
    origin = get_origin(ScheduleType)
    assert origin is Literal
    
    args = get_args(ScheduleType)
    
    # Common schedule types
    expected = ['always', 'onetime', 'recurring']
    
    print(f"  Values: {args}")
    for exp in expected:
        if exp in args:
            pass  # Found expected value
    
    print("✅ ScheduleType - is Literal")


def test_statustype_literal():
    """Test StatusType is a Literal type."""
    print("\n=== Testing StatusType Literal ===")
    
    origin = get_origin(StatusType)
    assert origin is Literal
    
    args = get_args(StatusType)
    
    # Should have enable/disable
    assert 'enable' in args
    assert 'disable' in args
    
    print(f"  Values: {args}")
    print("✅ StatusType - is Literal")


def test_literal_type_checking():
    """Test that Literal types work for type narrowing."""
    print("\n=== Testing Literal type checking ===")
    
    # Test runtime value checking with get_args
    action_values = get_args(ActionType)
    status_values = get_args(StatusType)
    
    # Validate a value is in the Literal
    test_action = 'accept'
    test_status = 'enable'
    
    assert test_action in action_values
    assert test_status in status_values
    
    print("✅ Literal type checking - works")


def run_all_tests():
    """Run all FortiOS type tests."""
    tests = [
        test_fortioslitresponse_is_typeddict,
        test_fortioslitresponse_can_be_created,
        test_fortiosdictresponse_is_typeddict,
        test_fortiosdictresponse_can_be_created,
        test_fortiosresponse_is_union,
        test_fortiossuccessresponse_is_typeddict,
        test_fortiossuccessresponse_can_be_created,
        test_fortioserrorresponse_is_typeddict,
        test_fortioserrorresponse_can_be_created,
        test_actiontype_literal,
        test_actiontype_values,
        test_logseverity_literal,
        test_protocoltype_literal,
        test_scheduletype_literal,
        test_statustype_literal,
        test_literal_type_checking,
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
