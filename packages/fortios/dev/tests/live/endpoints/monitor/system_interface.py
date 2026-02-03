import argparse
import sys
from pathlib import Path
import pytest
import base64
import requests
import os
from dotenv import load_dotenv
import urllib3
import time

# Disable SSL warnings for test environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Run registration monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def test_get_system_interface():
    """Test: Get system interface information"""
    result = fgt.api.monitor.system.interface.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_system_interface_dhcp_status():
    """Test: Get system interface DHCP status information"""
    result = fgt.api.monitor.system.interface.dhcp_status.get(mkey='port3')
    assert result is not None
    assert result.http_status_code == 200

def test_get_system_interface_kernel_interfaces():
    """Test: Get system interface kernel interfaces information"""
    result = fgt.api.monitor.system.interface.kernel_interfaces.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_system_avilable_interfaces():
    """Test: Get system available interfaces information"""
    result = fgt.api.monitor.system.available_interfaces.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_system_interface_speed_test_status():
    """Test: Post system interface speed test status information"""
    result = fgt.api.monitor.system.interface.speed_test_trigger.post(mkey='port3') 
    assert result is not None
    assert result.http_status_code == 200
    speedtest_info = fgt.api.monitor.system.interface.speed_test_status.get(id=result['id'])
    assert speedtest_info is not None
    assert speedtest_info.http_status_code == 200
    print(speedtest_info.json)
    

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
    test_get_system_interface()
    print("✓ test_get_system_interface passed")

    test_get_system_interface_dhcp_status()
    print("✓ test_get_system_interface_dhcp_status passed")

    test_get_system_interface_kernel_interfaces()
    print("✓ test_get_system_interface_kernel_interfaces passed")

    test_get_system_avilable_interfaces()
    print("✓ test_get_system_avilable_interfaces passed")

    test_post_system_interface_speed_test_status()
    print("✓ test_post_system_interface_speed_test_status passed")

    print("\n✓ All system interface tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
