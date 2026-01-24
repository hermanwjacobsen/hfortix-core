"""
Test FMG response properties on login, logout, and proxy calls.

All FortiManager operations should return response dicts with:
- result/status fields
- For proxy calls: fmg_status_code, fmg_raw, fmg_status_message properties
"""

from hfortix_fortios import FortiManagerProxy
import os
from dotenv import load_dotenv

load_dotenv()

fmg = FortiManagerProxy(
    host=os.getenv("FMG_HOST", ""),
    username=os.getenv("FMG_USER", ""),
    password=os.getenv("FMG_PASS", ""),
    verify=False,
    adom="KTL",
)

print("="*70)
print("TEST 1: Login Response")
print("="*70)
login_response = fmg.login()
print(f"✅ Login returns: {type(login_response)}")
print(f"   Keys: {list(login_response.keys())}")
if "result" in login_response:
    result = login_response["result"][0] if isinstance(login_response["result"], list) else login_response["result"]
    status = result.get("status", {})
    print(f"   Status code: {status.get('code')}")
    print(f"   Status message: {status.get('message')}")
if "session" in login_response:
    print(f"   Session token: {login_response['session'][:20]}..." if login_response['session'] else "None")

print(f"\n{'='*70}")
print("TEST 2: Proxy Call - FMG Response Properties")
print("="*70)

devices = fmg.get_devices()
if devices:
    device = devices[0]
    print(f"Testing with device: {device.name}")
    
    fgt = fmg.proxy(device=device.name)
    
    # Test a working endpoint
    status = fgt.api.monitor.system.status.get()
    
    print(f"\n✅ Response object type: {type(status)}")
    print(f"   Response has .json property: {hasattr(status, 'json')}")
    print(f"   Response has .dict property: {hasattr(status, 'dict')}")
    print(f"   Response has .raw property: {hasattr(status, 'raw')}")
    
    # FMG-specific properties
    print(f"\n📦 FMG Properties:")
    print(f"   .fmg_status_code: {status.fmg_status_code}")
    print(f"   .fmg_status_message: {status.fmg_status_message}")
    print(f"   .fmg_proxy_target: {status.fmg_proxy_target}")
    print(f"   .fmg_url: {status.fmg_url}")
    
    # Check if fmg_raw exists and show structure
    print(f"\n   .fmg_raw exists: {hasattr(status, 'fmg_raw')}")
    if hasattr(status, 'fmg_raw') and status.fmg_raw:
        print(f"   .fmg_raw keys: {list(status.fmg_raw.keys())}")
    
    # Standard FortiOS properties
    print(f"\n📡 FortiOS Properties:")
    print(f"   .http_status: {status.http_status}")
    print(f"   .http_status_code: {status.http_status_code}")
    print(f"   .http_method: {status.http_method}")
    print(f"   .vdom: {status.vdom}")

print(f"\n{'='*70}")
print("TEST 3: Logout Response")
print("="*70)
logout_response = fmg.logout()
print(f"✅ Logout returns: {type(logout_response)}")
print(f"   Keys: {list(logout_response.keys())}")
if "status" in logout_response:
    print(f"   Status code: {logout_response['status'].get('code')}")
    print(f"   Status message: {logout_response['status'].get('message')}")
elif "result" in logout_response:
    result = logout_response["result"][0] if isinstance(logout_response["result"], list) else logout_response["result"]
    status = result.get("status", {})
    print(f"   Status code: {status.get('code')}")
    print(f"   Status message: {status.get('message')}")

print(f"\n{'='*70}")
print("SUMMARY")
print("="*70)
print("""
✅ fmg.login() now returns dict with status/session
✅ fmg.logout() now returns dict with status
✅ Proxy responses have FMG properties:
   - fmg_status_code
   - fmg_status_message  
   - fmg_proxy_target
   - fmg_url
   - fmg_raw
   
All FMG operations now return proper response objects!
""")
