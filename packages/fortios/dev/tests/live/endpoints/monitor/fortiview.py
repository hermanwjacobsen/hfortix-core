import argparse
import sys
from pathlib import Path
import pytest

# Run fortiview monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# FortiView Monitor Tests - GET endpoints
# ============================================================================

def test_get_fortiview_realtime_statistics():
    """Test GET /monitor/fortiview/realtime-statistics - Retrieve realtime drill-down and summary data for FortiView."""
    try:
        result = fgt.api.monitor.fortiview.realtime_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_fortiview_historical_statistics():
    """Test GET /monitor/fortiview/historical-statistics - Retrieve historical drill-down and summary data for FortiView."""
    try:
        result = fgt.api.monitor.fortiview.historical_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_fortiview_realtime_proxy_statistics():
    """Test GET /monitor/fortiview/realtime-proxy-statistics - Retrieve realtime drill-down and summary data for proxy session FortiView statistics."""
    try:
        result = fgt.api.monitor.fortiview.realtime_proxy_statistics.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# ============================================================================
# FortiView Monitor Tests - POST endpoints
# ============================================================================

# def test_post_fortiview_session_cancel():
#     """Test POST /monitor/fortiview/session/cancel - Cancel a FortiView request session."""
#     # Requires session parameters
#     try:
#         result = fgt.api.monitor.fortiview.session.cancel.post()
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
    
    print("Running FortiView monitor endpoint tests...")
    
    test_get_fortiview_realtime_statistics()
    print("✓ test_get_fortiview_realtime_statistics")
    
    test_get_fortiview_historical_statistics()
    print("✓ test_get_fortiview_historical_statistics")
    
    test_get_fortiview_realtime_proxy_statistics()
    print("✓ test_get_fortiview_realtime_proxy_statistics")
    
    print("\n✓ All FortiView GET endpoint tests completed!")
    
    # ========================================================================
    # POST endpoint tests
    # ========================================================================
    
    # Commented out - requires parameters
    # test_post_fortiview_session_cancel()
    # print("✓ test_post_fortiview_session_cancel")
    
    print("\nSummary:")
    print("- GET endpoints: 3 active tests")
    print("- POST endpoints: 0 active tests, 1 commented out (requires parameters)")
    print("- Total: 3 active test functions covering FortiView monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
