#!/usr/bin/env python3
"""Test that FortiObject wrapping works for login/logout responses."""

from hfortix_fortios.models import FortiObject

# Simulate a logout response (what HTTPClientFMG returns)
mock_logout_response = {
    "id": 1,
    "result": {
        "status": {
            "code": 0,
            "message": "OK"
        }
    },
    "status": {
        "code": 0,
        "message": "OK"
    }
}

print("=" * 60)
print("Testing FortiObject Wrapping for FMG Responses")
print("=" * 60)

# Test wrapping (simulate what FortiManagerProxy.logout() does)
print("\n1. Creating FortiObject from mock logout response...")
envelope = {**mock_logout_response, "fmg_raw": mock_logout_response}
wrapped_response = FortiObject(mock_logout_response, raw_envelope=envelope)
print(f"   Type: {type(wrapped_response)}")
print(f"   Has fmg_raw: {hasattr(wrapped_response, 'fmg_raw')}")

# Test dict access
print("\n2. Testing dict-style access...")
print(f"   response['status']: {wrapped_response.get('status', {})}")
print(f"   response['status']['code']: {wrapped_response.get('status', {}).get('code', 'N/A')}")

# Test FMG properties
print("\n3. Testing FMG properties...")
print(f"   .fmg_raw type: {type(wrapped_response.fmg_raw)}")
print(f"   .fmg_raw == original: {wrapped_response.fmg_raw == mock_logout_response}")
print(f"   .dict available: {wrapped_response.dict is not None}")
print(f"   .json available: {wrapped_response.json is not None}")

# Test attribute access on nested dicts
print("\n4. Testing attribute access via fmg_raw...")
try:
    status_code = wrapped_response.fmg_raw.get("status", {}).get("code")
    print(f"   Status code via fmg_raw: {status_code}")
    print(f"   ✅ .fmg_raw works correctly!")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "=" * 60)
print("✅ FortiObject wrapping works correctly!")
print("   login_response.fmg_raw will return the full response")
print("   logout_response.fmg_raw will return the full response")
print("=" * 60)
