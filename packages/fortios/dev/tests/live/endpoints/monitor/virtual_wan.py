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


def test_get_virtual_wan_sladb():
    """Test: GET /monitor/virtual-wan/sladb - Retrieve SLA Database from FortiGuard"""
    result = fgt.api.monitor.virtual_wan.sladb.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_interface_log():
    """Test: GET /monitor/virtual-wan/interface-log - Retrieve SD-WAN interface quality log"""
    result = fgt.api.monitor.virtual_wan.interface_log.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_interface_log_with_seconds():
    """Test: Get interface log for last 300 seconds"""
    result = fgt.api.monitor.virtual_wan.interface_log.get(vdom="root", seconds=300)
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_health_check():
    """Test: GET /monitor/virtual-wan/health-check - Retrieve health-check statistics (deprecated)"""
    result = fgt.api.monitor.virtual_wan.health_check.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_sla_log():
    """Test: GET /monitor/virtual-wan/sla-log - Retrieve SLA probe results logs"""
    result = fgt.api.monitor.virtual_wan.sla_log.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_sla_log_latest():
    """Test: Get latest SLA log only"""
    result = fgt.api.monitor.virtual_wan.sla_log.get(vdom="root", latest=True)
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_sla_log_with_seconds():
    """Test: Get SLA logs from last 600 seconds"""
    result = fgt.api.monitor.virtual_wan.sla_log.get(vdom="root", seconds=600)
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_sla_log_skip_vpn_child():
    """Test: Get SLA logs skipping VPN child interfaces"""
    result = fgt.api.monitor.virtual_wan.sla_log.get(vdom="root", skip_vpn_child=True)
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_members():
    """Test: GET /monitor/virtual-wan/members - Retrieve interface statistics for SD-WAN links"""
    result = fgt.api.monitor.virtual_wan.members.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_virtual_wan_members_skip_vpn_child():
    """Test: Get SD-WAN members skipping VPN child interfaces"""
    result = fgt.api.monitor.virtual_wan.members.get(vdom="root", skip_vpn_child=True)
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
    test_get_virtual_wan_sladb()
    print("✓ test_get_virtual_wan_sladb passed")

    test_get_virtual_wan_interface_log()
    print("✓ test_get_virtual_wan_interface_log passed")

    test_get_virtual_wan_interface_log_with_seconds()
    print("✓ test_get_virtual_wan_interface_log_with_seconds passed")

    test_get_virtual_wan_health_check()
    print("✓ test_get_virtual_wan_health_check passed")

    test_get_virtual_wan_sla_log()
    print("✓ test_get_virtual_wan_sla_log passed")

    test_get_virtual_wan_sla_log_latest()
    print("✓ test_get_virtual_wan_sla_log_latest passed")

    test_get_virtual_wan_sla_log_with_seconds()
    print("✓ test_get_virtual_wan_sla_log_with_seconds passed")

    test_get_virtual_wan_sla_log_skip_vpn_child()
    print("✓ test_get_virtual_wan_sla_log_skip_vpn_child passed")

    test_get_virtual_wan_members()
    print("✓ test_get_virtual_wan_members passed")

    test_get_virtual_wan_members_skip_vpn_child()
    print("✓ test_get_virtual_wan_members_skip_vpn_child passed")

    print("\n✓ All virtual-wan tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
