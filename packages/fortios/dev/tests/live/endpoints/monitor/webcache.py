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


def test_get_webcache_stats():
    """Test: GET /monitor/webcache/stats - Retrieve webcache statistics (default period)"""
    result = fgt.api.monitor.webcache.stats.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_webcache_stats_10min():
    """Test: Get webcache stats for 10min period"""
    result = fgt.api.monitor.webcache.stats.get(period="10min")
    assert result is not None
    assert result.http_status_code == 200

def test_get_webcache_stats_hour():
    """Test: Get webcache stats for hour period"""
    result = fgt.api.monitor.webcache.stats.get(period="hour")
    assert result is not None
    assert result.http_status_code == 200

def test_get_webcache_stats_day():
    """Test: Get webcache stats for day period"""
    result = fgt.api.monitor.webcache.stats.get(period="day")
    assert result is not None
    assert result.http_status_code == 200

def test_get_webcache_stats_month():
    """Test: Get webcache stats for month period"""
    result = fgt.api.monitor.webcache.stats.get(period="month")
    assert result is not None
    assert result.http_status_code == 200

def test_post_webcache_stats_reset():
    """Test: POST /monitor/webcache/stats/reset - Reset all webcache statistics"""
    result = fgt.api.monitor.webcache.stats.reset.post()
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
    test_get_webcache_stats()
    print("✓ test_get_webcache_stats passed")

    test_get_webcache_stats_10min()
    print("✓ test_get_webcache_stats_10min passed")

    test_get_webcache_stats_hour()
    print("✓ test_get_webcache_stats_hour passed")

    test_get_webcache_stats_day()
    print("✓ test_get_webcache_stats_day passed")

    test_get_webcache_stats_month()
    print("✓ test_get_webcache_stats_month passed")

    test_post_webcache_stats_reset()
    print("✓ test_post_webcache_stats_reset passed")

    print("\n✓ All webcache tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
