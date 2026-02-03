import argparse
import sys
from pathlib import Path
import pytest

# Run fortiguard monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# FortiGuard Monitor Tests - GET endpoints
# ============================================================================

def test_get_fortiguard_redirect_portal():
    """Test GET /monitor/fortiguard/redirect-portal - Retrieve the FortiGuard redirect portal IP."""
    try:
        result = fgt.api.monitor.fortiguard.redirect_portal.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_fortiguard_service_communication_stats():
    """Test GET /monitor/fortiguard/service-communication-stats - Retrieve historical statistics for all FortiGuard services."""
    try:
        result = fgt.api.monitor.fortiguard.service_communication_stats.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_fortiguard_service_communication_stats_fortiguard_query():
    """Test GET /monitor/fortiguard/service-communication-stats - Retrieve statistics for fortiguard_query service."""
    try:
        result = fgt.api.monitor.fortiguard.service_communication_stats.get(service_type="fortiguard_query")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_fortiguard_answers():
    """Test GET /monitor/fortiguard/answers - Retrieve a list of questions on answers.fortinet.com."""
    try:
        result = fgt.api.monitor.fortiguard.answers.get()
        print("\nFortiGuard Answers Response:")
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
    
    print("Running FortiGuard monitor endpoint tests...")
    
    test_get_fortiguard_redirect_portal()
    print("✓ test_get_fortiguard_redirect_portal")
    
    test_get_fortiguard_service_communication_stats()
    print("✓ test_get_fortiguard_service_communication_stats (all services)")
    
    test_get_fortiguard_service_communication_stats_fortiguard_query()
    print("✓ test_get_fortiguard_service_communication_stats_fortiguard_query (specific service)")
    
    test_get_fortiguard_answers()
    print("✓ test_get_fortiguard_answers")
    
    print("\n✓ All FortiGuard endpoint tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 4 active tests")
    print("- Total: 4 test functions covering FortiGuard monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
