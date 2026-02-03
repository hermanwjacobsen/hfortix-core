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


def test_get_webfilter_override():
    """Test: GET /monitor/webfilter/override - List all webfilter overrides"""
    result = fgt.api.monitor.webfilter.override.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_webfilter_malicious_urls():
    """Test: GET /monitor/webfilter/malicious-urls - List all malicious URLs"""
    result = fgt.api.monitor.webfilter.malicious_urls.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_webfilter_malicious_urls_stat():
    """Test: GET /monitor/webfilter/malicious-urls/stat - Get malicious URL statistics"""
    result = fgt.api.monitor.webfilter.malicious_urls.stat.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_webfilter_category_quota():
    """Test: GET /monitor/webfilter/category-quota - Get category quota usage (no filters)"""
    result = fgt.api.monitor.webfilter.category_quota.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_webfilter_fortiguard_categories():
    """Test: GET /monitor/webfilter/fortiguard-categories - Get FortiGuard webfilter categories"""
    result = fgt.api.monitor.webfilter.fortiguard_categories.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_webfilter_trusted_urls():
    """Test: GET /monitor/webfilter/trusted-urls - List all trusted URLs"""
    result = fgt.api.monitor.webfilter.trusted_urls.get()
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
    test_get_webfilter_override()
    print("✓ test_get_webfilter_override passed")

    test_get_webfilter_malicious_urls()
    print("✓ test_get_webfilter_malicious_urls passed")

    test_get_webfilter_malicious_urls_stat()
    print("✓ test_get_webfilter_malicious_urls_stat passed")

    test_get_webfilter_category_quota()
    print("✓ test_get_webfilter_category_quota passed")

    test_get_webfilter_fortiguard_categories()
    print("✓ test_get_webfilter_fortiguard_categories passed")

    test_get_webfilter_trusted_urls()
    print("✓ test_get_webfilter_trusted_urls passed")

    print("\n✓ All webfilter tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
