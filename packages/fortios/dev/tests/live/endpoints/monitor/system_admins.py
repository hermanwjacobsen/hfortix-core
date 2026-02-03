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


def test_get_system_current_admins():
    """Test: Get current logged-in administrators"""
    result = fgt.api.monitor.system.current_admins.get()
    assert result is not None
    
    # Result is a list of admin sessions
    admin_count = len(result) if isinstance(result, list) else 0
    print(f"✓ Retrieved {admin_count} current administrator session(s)")
    
    # Show details if admins are logged in
    if admin_count > 0:
        for admin in result:
            print(f"  - {admin.get('admin')} via {admin.get('method')} from {admin.get('srcaddr')}")

def test_system_interface_connected_admins_info():
    """Test: Get detailed info for each current logged-in administrator"""
    result = fgt.api.monitor.system.interface_connected_admins_info.get(interface="port3")
    assert result is not None
    assert 'current_admin_connected' in result
    
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
    test_get_system_current_admins()
    print("✓ test_get_system_current_admins passed")

    test_system_interface_connected_admins_info()
    print("✓ test_system_interface_connected_admins_info passed")

    print("\n✓ All system current admins tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
