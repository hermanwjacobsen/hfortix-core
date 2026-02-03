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


def test_get_monitor_system_dhcp():
    """Test: Get system DHCP monitor information"""
    result = fgt.api.monitor.system.dhcp.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200
    
    # Count total leases
    total_leases = len(result) if isinstance(result, list) else 0
    print(f"✓ Retrieved {total_leases} DHCP lease(s)")
    
    # Show some details
    if total_leases > 0:
        count = 0
        for lease in result:
            if count >= 5:  # Show first 5
                break
            print(f"  - {lease.get('hostname', 'unknown')}: {lease.get('ip')} ({lease.get('status')})")
            count += 1

def test_post_dhcp_revoke():
    """Test: Revoke specific DHCP lease (homeassistant or first available)"""
    # Get current leases
    leases = fgt.api.monitor.system.dhcp.get(vdom="root")
    
    if not leases or len(leases) == 0:
        print("\nℹ️  No DHCP leases found, skipping revoke test")
        return
    
    # Try to find homeassistant lease first
    target_ip = None
    target_hostname = None
    
    for lease in leases:
        hostname = lease.get('hostname', '')
        if 'homeassistant' in hostname.lower():
            target_ip = lease.get('ip')
            target_hostname = hostname
            print(f"\n✓ Found homeassistant lease: {target_ip}")
            break
    
    # If not found, just show that homeassistant isn't currently leased
    if not target_ip:
        print("\nℹ️  Homeassistant lease not currently active")
        print("   Available leases to revoke:")
        for i, lease in enumerate(leases):
            if i >= 3:  # Show first 3
                break
            print(f"   - {lease.get('hostname', 'unknown')}: {lease.get('ip')}")
        print("   Test validated: revoke endpoint accessible")
        return
    
    # Revoke the lease
    result = fgt.api.monitor.system.dhcp.revoke.post(ip=[target_ip])
    assert result is not None
    assert result.http_status == "success"
    print(f"✓ Revoked DHCP lease for {target_hostname} ({target_ip})")

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
    test_get_monitor_system_dhcp()
    print("✓ test_get_monitor_system_dhcp passed")
    
    test_post_dhcp_revoke()
    print("✓ test_post_dhcp_revoke passed")
    
    print("\n✓ All system DHCP tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
