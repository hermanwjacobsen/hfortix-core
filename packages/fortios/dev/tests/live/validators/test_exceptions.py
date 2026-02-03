"""
Tests for hfortix_core.exceptions module

Tests all exception classes, their hierarchy, and error message formatting.
"""

from hfortix_core.exceptions import (
    FortinetError,
    APIError,
    RetryableError,
    NonRetryableError,
    RateLimitError,
    TimeoutError,
    ServerError,
    ServiceUnavailableError,
    CircuitBreakerOpenError,
    BadRequestError,
    ResourceNotFoundError,
    AuthenticationError,
    AuthorizationError,
    DuplicateEntryError,
    InvalidValueError,
    PermissionDeniedError,
    MethodNotAllowedError,
    EntryInUseError,
    ConfigurationError,
    VDOMError,
    ValidationError,
    ReadOnlyModeError,
    OperationNotSupportedError,
)


def test_fortinet_error_basic():
    """Test base FortinetError"""
    print("\n=== Testing FortinetError (basic) ===")
    
    err = FortinetError("Basic error message")
    assert str(err) == "Basic error message"
    assert isinstance(err, Exception)
    
    print(f"✓ FortinetError created: {err}")


def test_api_error_full_attributes():
    """Test APIError with all attributes"""
    print("\n=== Testing APIError (full attributes) ===")
    
    err = APIError(
        message="Entry not found",
        http_status=404,
        error_code=-3,
        endpoint="/api/v2/cmdb/firewall/policy/999",
        method="GET",
        request_id="abc123",
        hint="Check if the entry exists"
    )
    
    assert err.http_status == 404
    assert err.error_code == -3
    assert err.endpoint == "/api/v2/cmdb/firewall/policy/999"
    assert err.method == "GET"
    assert err.request_id == "abc123"
    assert err.hint == "Check if the entry exists"
    
    err_str = str(err)
    assert "Entry not found" in err_str
    assert "404" in err_str
    assert "GET" in err_str
    
    print(f"✓ APIError created with all attributes")
    print(f"  {err}")


def test_api_error_minimal():
    """Test APIError with minimal attributes"""
    print("\n=== Testing APIError (minimal) ===")
    
    err = APIError("Simple error")
    assert str(err) == "Simple error"
    assert err.http_status is None
    assert err.error_code is None
    
    print(f"✓ Minimal APIError: {err}")


def test_exception_hierarchy():
    """Test exception inheritance hierarchy"""
    print("\n=== Testing Exception Hierarchy ===")
    
    assert issubclass(FortinetError, Exception)
    assert issubclass(APIError, FortinetError)
    assert issubclass(RetryableError, APIError)
    assert issubclass(NonRetryableError, APIError)
    
    retryable_errors = [
        RateLimitError,
        TimeoutError,
        ServerError,
        ServiceUnavailableError,
        CircuitBreakerOpenError,
    ]
    for err_class in retryable_errors:
        assert issubclass(err_class, RetryableError)
        print(f"  ✓ {err_class.__name__} → RetryableError")
    
    non_retryable_errors = [
        BadRequestError,
        ResourceNotFoundError,
        DuplicateEntryError,
        InvalidValueError,
        PermissionDeniedError,
        MethodNotAllowedError,
        EntryInUseError,
    ]
    for err_class in non_retryable_errors:
        assert issubclass(err_class, NonRetryableError)
        print(f"  ✓ {err_class.__name__} → NonRetryableError")
    
    assert issubclass(AuthenticationError, FortinetError)
    assert issubclass(AuthorizationError, FortinetError)
    print("  ✓ AuthenticationError → FortinetError")
    print("  ✓ AuthorizationError → FortinetError")
    
    print("✓ All exception hierarchies correct")


def test_catch_by_base_class():
    """Test exceptions can be caught by base class"""
    print("\n=== Testing Catch by Base Class ===")
    
    try:
        raise RateLimitError("Too many requests", http_status=429)
    except APIError as e:
        assert e.http_status == 429
        print("  ✓ RateLimitError caught as APIError")
    
    try:
        raise ResourceNotFoundError("Entry not found", http_status=404)
    except APIError as e:
        assert e.http_status == 404
        print("  ✓ ResourceNotFoundError caught as APIError")
    
    try:
        raise ConfigurationError("Invalid config")
    except FortinetError as e:
        assert "Invalid config" in str(e)
        print("  ✓ ConfigurationError caught as FortinetError")
    
    print("✓ Base class catching works correctly")


def test_http_status_mapping():
    """Test HTTP status code descriptions"""
    print("\n=== Testing HTTP Status Mapping ===")
    
    for status in [400, 401, 403, 404, 429, 500]:
        err = APIError(f"Error {status}", http_status=status)
        err_str = str(err)
        assert str(status) in err_str
        print(f"  ✓ HTTP {status}")
    
    print("✓ HTTP status mapping works")


def test_fortios_error_code_mapping():
    """Test FortiOS error code descriptions"""
    print("\n=== Testing FortiOS Error Code Mapping ===")
    
    for code in [-3, -5, -6, 0]:
        err = APIError(f"Error {code}", error_code=code)
        err_str = str(err)
        assert str(code) in err_str
        print(f"  ✓ Error code {code}")
    
    print("✓ FortiOS error code mapping works")


def test_configuration_error():
    """Test ConfigurationError"""
    print("\n=== Testing ConfigurationError ===")
    
    err = ConfigurationError("Invalid host address")
    assert isinstance(err, FortinetError)
    assert "Invalid host address" in str(err)
    
    print(f"✓ ConfigurationError: {err}")


def test_vdom_error():
    """Test VDOMError"""
    print("\n=== Testing VDOMError ===")
    
    err = VDOMError("VDOM not found", vdom="test")
    assert isinstance(err, FortinetError)
    assert err.vdom == "test"
    
    print(f"✓ VDOMError: {err}")


def test_validation_error():
    """Test ValidationError"""
    print("\n=== Testing ValidationError ===")
    
    err = ValidationError("Field 'name' is required")
    assert isinstance(err, FortinetError)
    assert "required" in str(err)
    
    print(f"✓ ValidationError: {err}")


def test_exception_can_be_raised_and_caught():
    """Test all exceptions can be raised and caught"""
    print("\n=== Testing Raise/Catch All Exceptions ===")
    
    # Standard exceptions (message only)
    exception_classes = [
        FortinetError,
        APIError,
        RetryableError,
        NonRetryableError,
        RateLimitError,
        TimeoutError,
        ServerError,
        ServiceUnavailableError,
        CircuitBreakerOpenError,
        BadRequestError,
        ResourceNotFoundError,
        AuthenticationError,
        AuthorizationError,
        DuplicateEntryError,
        InvalidValueError,
        PermissionDeniedError,
        MethodNotAllowedError,
        EntryInUseError,
        ConfigurationError,
        ValidationError,
        ReadOnlyModeError,
    ]
    
    for exc_class in exception_classes:
        try:
            raise exc_class("Test message")
        except Exception as e:
            assert isinstance(e, exc_class)
            assert "Test message" in str(e)
            print(f"  ✓ {exc_class.__name__}")
    
    # VDOMError requires vdom argument
    try:
        raise VDOMError("Test message", vdom="root")
    except VDOMError as e:
        assert "Test message" in str(e)
        print(f"  ✓ VDOMError")
    
    # OperationNotSupportedError requires operation and endpoint
    try:
        raise OperationNotSupportedError("Test message", operation="DELETE", endpoint="/api/test")
    except OperationNotSupportedError as e:
        assert "Test message" in str(e)
        print(f"  ✓ OperationNotSupportedError")
    
    print("✓ All exceptions can be raised and caught")


if __name__ == "__main__":
    test_fortinet_error_basic()
    test_api_error_full_attributes()
    test_api_error_minimal()
    test_exception_hierarchy()
    test_catch_by_base_class()
    test_http_status_mapping()
    test_fortios_error_code_mapping()
    test_configuration_error()
    test_vdom_error()
    test_validation_error()
    test_exception_can_be_raised_and_caught()
    
    print("\n" + "=" * 60)
    print("✅ All exception tests passed!")
    print("=" * 60)
