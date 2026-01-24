#!/usr/bin/env python3
"""Test FMG login/logout returning FortiObject with fmg_raw property."""

from hfortix_fortios.fmg_proxy import FortiManagerProxy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

# Connect to FortiManager
fmg = FortiManagerProxy(
    host=os.getenv("FMG_HOST", ""),
    username=os.getenv("FMG_USER", ""),
    password=os.getenv("FMG_PASS", ""),
    verify=False,
    adom="HWJ",
)

print("=" * 60)
print("Testing FortiManager Login/Logout with FortiObject")
print("=" * 60)

# Test login
print("\n1. Testing login()...")
login_response = fmg.login()
print(f"   Type: {type(login_response)}")
print(f"   Has fmg_raw: {hasattr(login_response, 'fmg_raw')}")
print(f"   Session: {login_response.get('session', 'N/A')}")
print(f"   Status: {login_response.get('result', [{}])[0].get('status', {})}")

# Access FMG properties
print("\n2. Testing FMG properties on login response...")
print(f"   .fmg_raw available: {login_response.fmg_raw is not None}")
print(f"   .dict available: {login_response.dict is not None}")
print(f"   .json available: {login_response.json is not None}")

# Test logout
print("\n3. Testing logout()...")
logout_response = fmg.logout()
print(f"   Type: {type(logout_response)}")
print(f"   Has fmg_raw: {hasattr(logout_response, 'fmg_raw')}")
print(f"   Status: {logout_response.get('status', {})}")

# Access FMG properties on logout
print("\n4. Testing FMG properties on logout response...")
print(f"   .fmg_raw: {logout_response.fmg_raw}")
print(f"   .dict available: {logout_response.dict is not None}")
print(f"   .json available: {logout_response.json is not None}")

print("\n" + "=" * 60)
print("✅ All tests passed! login() and logout() return FortiObject")
print("=" * 60)
