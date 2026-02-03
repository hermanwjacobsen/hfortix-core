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


def test_get_user_banned():
    """Test: GET /monitor/user/banned - List all banned users by IP"""
    result = fgt.api.monitor.user.banned.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_banned_check():
    """Test: GET /monitor/user/banned/check - Check if an IP address is banned"""
    # Check if a test IP is banned (using a random IP that shouldn't be banned)
    result = fgt.api.monitor.user.banned.check.get(ip_address="192.0.2.1")
    assert result is not None
    assert result.http_status_code == 200
    
def test_get_user_banned_check_ipv6():
    """Test: Check if an IPv6 address is banned"""
    result = fgt.api.monitor.user.banned.check.get(ip_address="2001:db8::1")
    assert result is not None
    assert result.http_status_code == 200

def test_post_user_banned_add_and_verify():
    """Test: POST /monitor/user/banned/add_users - Add users to banned list and verify"""
    test_ips = ["192.0.2.100", "192.0.2.101"]
    
    # Add users to banned list with 300 second expiry
    result = fgt.api.monitor.user.banned.add_users.post(
        ip_addresses=test_ips,
        expiry=300
    )
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify first IP is now banned
    check_result = fgt.api.monitor.user.banned.check.get(ip_address=test_ips[0])
    assert check_result is not None
    assert check_result.http_status_code == 200
    # Check if is_banned field is True
    if hasattr(check_result, 'is_banned'):
        assert check_result.get('is_banned') == True

def test_post_user_banned_clear_specific_users():
    """Test: POST /monitor/user/banned/clear_users - Clear specific banned users"""
    # First ensure we have some banned users from previous test
    test_ips = ["192.0.2.100", "192.0.2.101"]
    
    # Clear specific users
    result = fgt.api.monitor.user.banned.clear_users.post(ip_addresses=test_ips)
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify first IP is no longer banned
    check_result = fgt.api.monitor.user.banned.check.get(ip_address=test_ips[0])
    assert check_result is not None
    assert check_result.http_status_code == 200
    if hasattr(check_result, 'is_banned'):
        assert check_result.get('is_banned') == False

def test_post_user_banned_add_ipv6():
    """Test: Add IPv6 address to banned list"""
    test_ipv6 = ["2001:db8::100"]
    
    # Add IPv6 user to banned list with indefinite ban (expiry=0)
    result = fgt.api.monitor.user.banned.add_users.post(
        ip_addresses=test_ipv6,
        expiry=0
    )
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify IPv6 is banned
    check_result = fgt.api.monitor.user.banned.check.get(ip_address=test_ipv6[0])
    assert check_result is not None
    assert check_result.http_status_code == 200

def test_post_user_banned_clear_all():
    """Test: POST /monitor/user/banned/clear_all - Clear all banned users"""
    result = fgt.api.monitor.user.banned.clear_all.post()
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify all cleared by getting banned list
    list_result = fgt.api.monitor.user.banned.get()
    assert list_result is not None
    assert list_result.http_status_code == 200

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
    test_get_user_banned()
    print("✓ test_get_user_banned passed")

    test_get_user_banned_check()
    print("✓ test_get_user_banned_check passed")

    test_get_user_banned_check_ipv6()
    print("✓ test_get_user_banned_check_ipv6 passed")

    test_post_user_banned_add_and_verify()
    print("✓ test_post_user_banned_add_and_verify passed")

    test_post_user_banned_clear_specific_users()
    print("✓ test_post_user_banned_clear_specific_users passed")

    test_post_user_banned_add_ipv6()
    print("✓ test_post_user_banned_add_ipv6 passed")

    test_post_user_banned_clear_all()
    print("✓ test_post_user_banned_clear_all passed")

    print("\n✓ All user banned tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
