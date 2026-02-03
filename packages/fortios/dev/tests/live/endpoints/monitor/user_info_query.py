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


def test_get_user_info_query():
    """Test: GET /monitor/user/info/query - Query user info (no filters)"""
    result = fgt.api.monitor.user.info.query.get()
    assert result is not None
    assert result.http_status_code == 200


def test_get_user_info_query_key_only():
    """Test: Get user info with primary key fields only"""
    result = fgt.api.monitor.user.info.query.get(key_only=True)
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_info_query_total_only():
    """Test: Get total count of user info entries only"""
    result = fgt.api.monitor.user.info.query.get(total_only=True)
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_info_query_latest():
    """Test: Get user info with latest query type"""
    result = fgt.api.monitor.user.info.query.get(query_type="latest")
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_info_query_with_filters():
    """Test: Get user info with username filter"""
    # Filter for users with a specific username pattern (will test the filter mechanism)
    filters = [
        '{"type": "username", "value": "admin", "op": "contains"}'
    ]
    result = fgt.api.monitor.user.info.query.get(filters=filters)
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_info_query_filter_logic_or():
    """Test: Get user info with OR filter logic"""
    filters = [
        '{"type": "username", "value": "admin", "op": "contains"}',
        '{"type": "username", "value": "user", "op": "contains"}'
    ]
    result = fgt.api.monitor.user.info.query.get(filters=filters, filter_logic="or")
    assert result is not None
    assert result.http_status_code == 200

def test_get_user_info_query_filter_logic_and():
    """Test: Get user info with AND filter logic (default)"""
    filters = [
        '{"type": "username", "value": "admin", "op": "exact"}'
    ]
    result = fgt.api.monitor.user.info.query.get(filters=filters, filter_logic="and")
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
    test_get_user_info_query()
    print("✓ test_get_user_info_query passed")

    test_get_user_info_query_key_only()
    print("✓ test_get_user_info_query_key_only passed")

    test_get_user_info_query_total_only()
    print("✓ test_get_user_info_query_total_only passed")

    test_get_user_info_query_latest()
    print("✓ test_get_user_info_query_latest passed")

    test_get_user_info_query_with_filters()
    print("✓ test_get_user_info_query_with_filters passed")

    test_get_user_info_query_filter_logic_or()
    print("✓ test_get_user_info_query_filter_logic_or passed")

    test_get_user_info_query_filter_logic_and()
    print("✓ test_get_user_info_query_filter_logic_and passed")

    print("\n✓ All user info query tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
