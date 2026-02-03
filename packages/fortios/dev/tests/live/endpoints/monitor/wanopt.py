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


def test_get_wanopt_history():
    """Test: GET /monitor/wanopt/history - Retrieve WAN optimization statistics history"""
    result = fgt.api.monitor.wanopt.history.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_history_10min():
    """Test: Get WAN opt history for 10-min period"""
    result = fgt.api.monitor.wanopt.history.get(vdom="root", period="10-min")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_history_hour():
    """Test: Get WAN opt history for hour period"""
    result = fgt.api.monitor.wanopt.history.get(vdom="root", period="hour")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_history_day():
    """Test: Get WAN opt history for day period"""
    result = fgt.api.monitor.wanopt.history.get(vdom="root", period="day")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_webcache():
    """Test: GET /monitor/wanopt/webcache - Retrieve webcache statistics history"""
    result = fgt.api.monitor.wanopt.webcache.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_webcache_10min():
    """Test: Get webcache stats for 10-min period"""
    result = fgt.api.monitor.wanopt.webcache.get(vdom="root", period="10-min")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_webcache_week():
    """Test: Get webcache stats for week period"""
    result = fgt.api.monitor.wanopt.webcache.get(vdom="root", period="week")
    assert result is not None
    assert result.http_status_code == 200

def test_get_wanopt_peer_stats():
    """Test: GET /monitor/wanopt/peer_stats - Retrieve WAN opt peer statistics"""
    result = fgt.api.monitor.wanopt.peer_stats.get(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_post_wanopt_history_reset():
    """Test: POST /monitor/wanopt/history/reset - Reset WAN opt statistics"""
    result = fgt.api.monitor.wanopt.history.reset.post(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_post_wanopt_webcache_reset():
    """Test: POST /monitor/wanopt/webcache/reset - Reset webcache statistics"""
    result = fgt.api.monitor.wanopt.webcache.reset.post(vdom="root")
    assert result is not None
    assert result.http_status_code == 200

def test_post_wanopt_peer_stats_reset():
    """Test: POST /monitor/wanopt/peer_stats/reset - Reset WAN opt peer statistics"""
    result = fgt.api.monitor.wanopt.peer_stats.reset.post(vdom="root")
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
    test_get_wanopt_history()
    print("✓ test_get_wanopt_history passed")

    test_get_wanopt_history_10min()
    print("✓ test_get_wanopt_history_10min passed")

    test_get_wanopt_history_hour()
    print("✓ test_get_wanopt_history_hour passed")

    test_get_wanopt_history_day()
    print("✓ test_get_wanopt_history_day passed")

    test_get_wanopt_webcache()
    print("✓ test_get_wanopt_webcache passed")

    test_get_wanopt_webcache_10min()
    print("✓ test_get_wanopt_webcache_10min passed")

    test_get_wanopt_webcache_week()
    print("✓ test_get_wanopt_webcache_week passed")

    test_get_wanopt_peer_stats()
    print("✓ test_get_wanopt_peer_stats passed")

    test_post_wanopt_history_reset()
    print("✓ test_post_wanopt_history_reset passed")

    test_post_wanopt_webcache_reset()
    print("✓ test_post_wanopt_webcache_reset passed")

    test_post_wanopt_peer_stats_reset()
    print("✓ test_post_wanopt_peer_stats_reset passed")

    print("\n✓ All wanopt tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
