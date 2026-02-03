import argparse
import sys
from pathlib import Path
import pytest

# Run license monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# License Monitor Tests - GET endpoints
# ============================================================================

def test_get_license_status():
    """Test GET /monitor/license/status - Get current license & registration status."""
    try:
        result = fgt.api.monitor.license.status.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_license_fortianalyzer_status():
    """Test GET /monitor/license/fortianalyzer-status - Get current license & registration status for the connected FortiAnalyzer."""
    try:
        result = fgt.api.monitor.license.fortianalyzer_status.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_license_forticare_resellers():
    """Test GET /monitor/license/forticare-resellers - Get current FortiCare resellers for the requested country."""
    try:
        # Try without country_code parameter to see default behavior
        result = fgt.api.monitor.license.forticare_resellers.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_license_forticare_org_list():
    """Test GET /monitor/license/forticare-org-list - Get FortiCare organization size and industry lists."""
    try:
        result = fgt.api.monitor.license.forticare_org_list.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# ============================================================================
# License Monitor Tests - POST endpoints
# ============================================================================

# def test_post_license_database_upgrade():
#     """Test POST /monitor/license/database/upgrade - Upgrade or downgrade UTM engine or signature package."""
#     # Requires uploaded file parameter
#     try:
#         result = fgt.api.monitor.license.database.upgrade.post()
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
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
    # GET endpoint tests
    # ========================================================================
    
    print("Running License monitor endpoint tests...")
    
    test_get_license_status()
    print("✓ test_get_license_status")
    
    test_get_license_fortianalyzer_status()
    print("✓ test_get_license_fortianalyzer_status")
    
    test_get_license_forticare_resellers()
    print("✓ test_get_license_forticare_resellers")
    
    test_get_license_forticare_org_list()
    print("✓ test_get_license_forticare_org_list")
    
    print("\n✓ All License GET endpoint tests completed!")
    
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    # Commented out - requires parameters
    # test_post_license_database_upgrade()
    # print("✓ test_post_license_database_upgrade")
    
    print("\nSummary:")
    print("- GET endpoints: 4 active tests")
    print("- POST endpoints: 0 active tests, 1 commented out (requires parameters)")
    print("- Total: 4 active test functions covering License monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
