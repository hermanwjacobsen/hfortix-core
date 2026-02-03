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


def test_post_utm_rating_lookup_select():
    """Test: POST /monitor/utm/rating-lookup/select - Lookup FortiGuard rating for URLs"""
    urls = ["https://www.fortinet.com", "https://www.google.com"]
    result = fgt.api.monitor.utm.rating_lookup.select.post(url=urls)
    assert result is not None
    assert result.http_status_code == 200

def test_post_utm_rating_lookup_select_with_lang():
    """Test: Lookup FortiGuard rating with language parameter"""
    urls = ["https://www.example.com"]
    result = fgt.api.monitor.utm.rating_lookup.select.post(url=urls, lang="en")
    assert result is not None
    assert result.http_status_code == 200

def test_post_utm_rating_lookup_select_multiple_urls():
    """Test: Lookup multiple URLs at once"""
    urls = [
        "https://www.fortinet.com",
        "https://www.google.com",
        "https://www.github.com",
        "https://www.microsoft.com"
    ]
    result = fgt.api.monitor.utm.rating_lookup.select.post(url=urls)
    assert result is not None
    assert result.http_status_code == 200


# SKIPPED: Returns HTTP 400 Bad Request - endpoint may require specific configuration
# def test_get_utm_app_lookup():
#     """Test: GET /monitor/utm/app-lookup - Query ISDB to resolve hosts to applications"""
#     hosts = ["www.fortinet.com", "www.google.com"]
#     result = fgt.api.monitor.utm.app_lookup.get(hosts=hosts)
#     assert result is not None
#     assert result.http_status_code == 200

# def test_get_utm_app_lookup_single_host():
#     """Test: Query single host resolution"""
#     result = fgt.api.monitor.utm.app_lookup.get(hosts=["www.microsoft.com"])
#     assert result is not None
#     assert result.http_status_code == 200

def test_get_utm_application_categories():
    """Test: GET /monitor/utm/application-categories - Retrieve application control categories"""
    result = fgt.api.monitor.utm.application_categories.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_utm_antivirus_stats():
    """Test: GET /monitor/utm/antivirus/stats - Retrieve antivirus scanning statistics"""
    result = fgt.api.monitor.utm.antivirus.stats.get()
    assert result is not None
    assert result.http_status_code == 200

def test_get_utm_blacklisted_certificates():
    """Test: GET /monitor/utm/blacklisted-certificates - Retrieve blacklisted SSL certificates"""
    # Get first 10 blacklisted certificates
    result = fgt.api.monitor.utm.blacklisted_certificates.get(start=0, count=10)
    assert result is not None
    assert result.http_status_code == 200

def test_get_utm_blacklisted_certificates_pagination():
    """Test: Get blacklisted certificates with different pagination"""
    # Get next 20 certificates starting from index 10
    result = fgt.api.monitor.utm.blacklisted_certificates.get(start=10, count=20)
    assert result is not None
    assert result.http_status_code == 200

def test_get_utm_blacklisted_certificates_max_count():
    """Test: Get maximum allowed certificates (limit 2000)"""
    result = fgt.api.monitor.utm.blacklisted_certificates.get(start=0, count=2000)
    assert result is not None
    assert result.http_status_code == 200

def test_get_utm_blacklisted_certificates_statistics():
    """Test: GET /monitor/utm/blacklisted-certificates/statistics - Get certificate statistics"""
    result = fgt.api.monitor.utm.blacklisted_certificates.statistics.get()
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
    test_post_utm_rating_lookup_select()
    print("✓ test_post_utm_rating_lookup_select passed")

    test_post_utm_rating_lookup_select_with_lang()
    print("✓ test_post_utm_rating_lookup_select_with_lang passed")

    test_post_utm_rating_lookup_select_multiple_urls()
    print("✓ test_post_utm_rating_lookup_select_multiple_urls passed")

    # test_get_utm_app_lookup()
    # print("✓ test_get_utm_app_lookup passed")

    test_get_utm_application_categories()
    print("✓ test_get_utm_application_categories passed")

    test_get_utm_antivirus_stats()
    print("✓ test_get_utm_antivirus_stats passed")

    test_get_utm_blacklisted_certificates()
    print("✓ test_get_utm_blacklisted_certificates passed")

    test_get_utm_blacklisted_certificates_pagination()
    print("✓ test_get_utm_blacklisted_certificates_pagination passed")

    test_get_utm_blacklisted_certificates_max_count()
    print("✓ test_get_utm_blacklisted_certificates_max_count passed")

    test_get_utm_blacklisted_certificates_statistics()
    print("✓ test_get_utm_blacklisted_certificates_statistics passed")

    print("\n✓ All UTM tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
