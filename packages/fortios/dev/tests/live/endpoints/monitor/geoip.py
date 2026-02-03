import argparse
import sys
from pathlib import Path
import pytest

# Run geoip monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# GeoIP Monitor Tests - POST endpoints
# ============================================================================

# def test_post_geoip_query_select():
#     """Test POST /monitor/geoip/geoip-query/select - Retrieve location details for IPs queried against FortiGuard's geoip service."""
#     # Returns 424 - GeoIP service unavailable
#     try:
#         # Query location for Google DNS (8.8.8.8)
#         result = fgt.api.monitor.geoip.geoip_query.select.post(ip_addresses="8.8.8.8")
#         print("\nGeoIP Query Response for 8.8.8.8:")
#         print(result.raw)
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "424" in str(e):
#             print("GeoIP service unavailable (424) - FortiGuard GeoIP service may not be configured or enabled")
#         else:
#             raise


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
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    print("Running GeoIP monitor endpoint tests...")
    
    # Commented out - returns 424 (GeoIP service unavailable)
    # test_post_geoip_query_select()
    # print("✓ test_post_geoip_query_select")
    
    print("\n✓ GeoIP endpoint tests documented!")
    print("\nSummary:")
    print("- POST endpoints: 0 active tests, 1 commented out (returns 424 - service unavailable)")
    print("- Total: 1 test function covering GeoIP monitor endpoint")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
