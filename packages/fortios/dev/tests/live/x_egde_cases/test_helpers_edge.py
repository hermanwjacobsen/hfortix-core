"""
Helper utilities for FortiGate API tests.

Provides functions for generating unique test object names and common test patterns.
"""

import time
from datetime import datetime


# Global timestamp for this test run - all tests in one run share the same timestamp
# This makes it easy to identify which objects belong to which test run
TEST_RUN_TIMESTAMP = int(time.time())


def get_test_name(base_name: str, use_timestamp: bool = True) -> str:
    """
    Generate a unique test object name.
    
    Args:
        base_name: The base name for the test object (e.g., "service", "address")
        use_timestamp: Whether to append timestamp (default: True)
    
    Returns:
        A unique test name like "test_service_1704844800" or just "test_service"
    
    Examples:
        >>> get_test_name("service")
        'test_service_1704844800'
        
        >>> get_test_name("address_group", use_timestamp=False)
        'test_address_group'
    """
    if use_timestamp:
        return f"test_{base_name}_{TEST_RUN_TIMESTAMP}"
    else:
        return f"test_{base_name}"


def get_unique_test_name(base_name: str) -> str:
    """
    Generate a unique test object name with microsecond precision.
    
    Use this when you need to create multiple objects within the same test
    and need guaranteed uniqueness.
    
    Args:
        base_name: The base name for the test object
    
    Returns:
        A unique test name like "test_service_1704844800_123456"
    
    Examples:
        >>> get_unique_test_name("temp_service")
        'test_temp_service_1704844800_123456'
    """
    current_time = time.time()
    timestamp = int(current_time)
    microseconds = int((current_time - timestamp) * 1_000_000)
    return f"test_{base_name}_{timestamp}_{microseconds}"


def get_test_run_id() -> str:
    """
    Get a human-readable ID for this test run.
    
    Returns:
        A timestamp string like "20260109_143045" (YYYYMMDD_HHMMSS)
    """
    return datetime.fromtimestamp(TEST_RUN_TIMESTAMP).strftime("%Y%m%d_%H%M%S")


def print_test_header(test_name: str, description: str = ""):
    """
    Print a formatted test header for better readability.
    
    Args:
        test_name: Name of the test
        description: Optional description of what the test does
    """
    print(f"\n{'='*70}")
    print(f"TEST: {test_name}")
    if description:
        print(f"DESC: {description}")
    print(f"RUN:  {get_test_run_id()}")
    print(f"{'='*70}")


def print_test_result(test_name: str, passed: bool = True, message: str = ""):
    """
    Print a formatted test result.
    
    Args:
        test_name: Name of the test
        passed: Whether the test passed (default: True)
        message: Optional additional message
    """
    status = "✓ PASS" if passed else "✗ FAIL"
    if message:
        print(f"{status}: {test_name} - {message}")
    else:
        print(f"{status}: {test_name}")


# Example usage in tests:
if __name__ == "__main__":
    print("Test Run ID:", get_test_run_id())
    print("Test Name:", get_test_name("service"))
    print("Unique Name 1:", get_unique_test_name("temp"))
    time.sleep(0.001)  # Wait a bit
    print("Unique Name 2:", get_unique_test_name("temp"))
    
    print_test_header("example_test", "This demonstrates the test header")
    print_test_result("example_test", passed=True, message="All checks passed")
