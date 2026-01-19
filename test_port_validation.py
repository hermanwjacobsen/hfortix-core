"""Test port parameter validation with invalid string values."""
import os
from hfortix_fortios import FortiOS

# Test 1: Invalid port string passed directly
print("Test 1: Passing port='aa' directly")
try:
    fgt = FortiOS(
        host="192.168.1.1",
        token="test-token",
        port="aa",  # Invalid - not a numeric string
    )
    print("  ❌ No error raised - THIS IS UNEXPECTED!")
except ValueError as e:
    print(f"  ✅ ValueError raised as expected: {e}")
except Exception as e:
    print(f"  ⚠️ Different error: {type(e).__name__}: {e}")

# Test 2: Invalid port from environment variable
print("\nTest 2: Using FORTIOS_PORT='aa' from environment")
os.environ["FORTIOS_PORT"] = "aa"
try:
    fgt = FortiOS(
        host="192.168.1.1",
        token="test-token",
    )
    print("  ❌ No error raised - THIS IS UNEXPECTED!")
except ValueError as e:
    print(f"  ✅ ValueError raised as expected: {e}")
except Exception as e:
    print(f"  ⚠️ Different error: {type(e).__name__}: {e}")

# Test 3: Valid numeric string
print("\nTest 3: Passing port='8443' (valid numeric string)")
try:
    fgt = FortiOS(
        host="192.168.1.1",
        token="test-token",
        port="8443",
    )
    print("  ✅ No error - valid port string accepted")
except Exception as e:
    print(f"  ❌ Unexpected error: {type(e).__name__}: {e}")

# Test 4: Valid integer
print("\nTest 4: Passing port=8443 (integer)")
try:
    fgt = FortiOS(
        host="192.168.1.1",
        token="test-token",
        port=8443,
    )
    print("  ✅ No error - valid integer port accepted")
except Exception as e:
    print(f"  ❌ Unexpected error: {type(e).__name__}: {e}")

# Cleanup
del os.environ["FORTIOS_PORT"]
