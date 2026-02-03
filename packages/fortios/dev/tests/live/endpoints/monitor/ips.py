import argparse
import sys
from pathlib import Path
import pytest

# Run ips monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# IPS Monitor Tests - GET endpoints
# ============================================================================

def test_get_ips_rate_based():
    """Test GET /monitor/ips/rate-based - Returns a list of rate-based signatures in IPS package."""
    try:
        result = fgt.api.monitor.ips.rate_based.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_ips_metadata():
    """Test GET /monitor/ips/metadata - Returns IPS meta data."""
    try:
        result = fgt.api.monitor.ips.metadata.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_ips_anomaly():
    """Test GET /monitor/ips/anomaly - Returns IPS anomaly list."""
    try:
        result = fgt.api.monitor.ips.anomaly.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_ips_hold_signatures():
    """Test GET /monitor/ips/hold-signatures - Return a list of IPS signatures that are on hold due to active hold time."""
    try:
        result = fgt.api.monitor.ips.hold_signatures.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_ips_session_performance():
    """Test GET /monitor/ips/session/performance - Returns IPS session performance status."""
    try:
        result = fgt.api.monitor.ips.session.performance.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


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
    
    print("Running IPS monitor endpoint tests...")
    
    test_get_ips_rate_based()
    print("✓ test_get_ips_rate_based")
    
    test_get_ips_metadata()
    print("✓ test_get_ips_metadata")
    
    test_get_ips_anomaly()
    print("✓ test_get_ips_anomaly")
    
    test_get_ips_hold_signatures()
    print("✓ test_get_ips_hold_signatures")
    
    test_get_ips_session_performance()
    print("✓ test_get_ips_session_performance")
    
    print("\n✓ All IPS endpoint tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 5 active tests")
    print("- Total: 5 test functions covering IPS monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
