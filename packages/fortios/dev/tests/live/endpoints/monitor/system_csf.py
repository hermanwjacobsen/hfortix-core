import argparse
import sys
from pathlib import Path
import pytest
import base64
import requests
import os
from dotenv import load_dotenv
import urllib3

# Disable SSL warnings for test environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Run registration monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def test_get_system_csf():
    """Test: GET /system/csf - Retrieve Security Fabric topology"""
    result = fgt.api.monitor.system.csf.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # Check if Security Fabric is enabled
    protocol_enabled = result.get('protocol_enabled', False)
    print(f"✓ Security Fabric protocol enabled: {protocol_enabled}")
    
    if protocol_enabled:
        csf_name = result.get('csf_group_name', 'N/A')
        print(f"  Security Fabric name: {csf_name}")
        
        # Show device types in the fabric
        devices = result.get('devices', {})
        if devices:
            print(f"  Device types in fabric:")
            for device_type, device_list in devices.items():
                count = len(device_list) if isinstance(device_list, list) else 0
                print(f"    - {device_type}: {count} device(s)")
        
        # Show pending devices
        pending = result.get('pending', [])
        if pending and len(pending) > 0:
            print(f"  Pending authorizations: {len(pending)} device(s)")
    else:
        print("  Security Fabric is not enabled on this device")

def test_get_system_csf_pending_authorizations():
    """Test: GET /system/csf/pending-authorizations - Retrieve pending device authorizations"""
    result = fgt.api.monitor.system.csf.pending_authorizations.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # Check for pending authorizations
    pending_count = len(result) if isinstance(result, list) else 0
    print(f"✓ Retrieved {pending_count} pending authorization(s)")
    
    if pending_count > 0:
        print("  Pending devices:")
        for device in result:
            serial = device.get('serial', 'unknown')
            device_type = device.get('device_type', 'unknown')
            mgmt_ip = device.get('mgmt_ip_str', 'N/A')
            auth_type = device.get('authorization_type', 'N/A')
            print(f"    - {serial} ({device_type}) - IP: {mgmt_ip}, Auth: {auth_type}")
    else:
        print("  No pending device authorizations")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests")
    parser.add_argument("--client", choices=["direct", "fmg_proxy"], default="direct",
                        help="Client to use: direct (default) or fmg_proxy")
    args = parser.parse_args()
    
    if args.client == "fmg_proxy":
        from fmgclient import fgt, fmg
        client_name = "FMG proxy"
    else:
        from fgtclient import fgt
        fmg = None
        client_name = "direct"
    
    print(f"Running tests with {client_name} client...")
    test_get_system_csf()
    print("✓ test_get_system_csf passed")
    
    test_get_system_csf_pending_authorizations()
    print("✓ test_get_system_csf_pending_authorizations passed")
    
    print("\n✓ All Security Fabric tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
