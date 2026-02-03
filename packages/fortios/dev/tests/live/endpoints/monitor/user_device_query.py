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


def test_get_user_device_query():
    """Test: GET /monitor/user/device/query - Retrieve user devices (no filters)"""
    result = fgt.api.monitor.user.device.query.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_device_query_key_only():
    """Test: Get user devices with primary key fields only"""
    result = fgt.api.monitor.user.device.query.get(key_only=True)
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_device_query_total_only():
    """Test: Get total count of user devices only"""
    result = fgt.api.monitor.user.device.query.get(total_only=True)
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_device_query_latest():
    """Test: Get user devices with latest query type"""
    result = fgt.api.monitor.user.device.query.get(query_type="latest")
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_device_query_fortiswitch_client_view():
    """Test: Get user devices with FortiSwitch client view"""
    result = fgt.api.monitor.user.device.query.get(view_type="fortiswitch_client")
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_device_query_forticlient_view():
    """Test: Get user devices with FortiClient view"""
    result = fgt.api.monitor.user.device.query.get(view_type="forticlient")
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_device_query_with_filters():
    """Test: Get user devices with MAC address filter"""
    # Filter for devices with a specific MAC pattern (will likely return empty, but tests the filter mechanism)
    filters = [
        '{"type": "mac", "value": "00:00:00:00:00:00", "op": "exact"}'
    ]
    result = fgt.api.monitor.user.device.query.get(filters=filters)
    assert result is not None
    assert result.http_status_code == 200

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
    test_get_user_device_query()
    print("✓ test_get_user_device_query passed")

    test_get_user_device_query_key_only()
    print("✓ test_get_user_device_query_key_only passed")

    test_get_user_device_query_total_only()
    print("✓ test_get_user_device_query_total_only passed")

    test_get_user_device_query_latest()
    print("✓ test_get_user_device_query_latest passed")

    test_get_user_device_query_fortiswitch_client_view()
    print("✓ test_get_user_device_query_fortiswitch_client_view passed")

    test_get_user_device_query_forticlient_view()
    print("✓ test_get_user_device_query_forticlient_view passed")

    test_get_user_device_query_with_filters()
    print("✓ test_get_user_device_query_with_filters passed")

    print("\n✓ All user device query tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
