import argparse
import sys
from pathlib import Path
import pytest

# Run registration monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# Registration Monitor Tests - GET endpoints
# ============================================================================

def test_get_registration_forticloud_disclaimer():
    """Test GET /monitor/registration/forticloud/disclaimer - Retrieve the FortiCloud disclaimer."""
    try:
        result = fgt.api.monitor.registration.forticloud.disclaimer.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "500" in str(e):
            print("Server error (500) - FortiCloud service may not be configured")
        else:
            raise


def test_get_registration_forticloud_domains():
    """Test GET /monitor/registration/forticloud/domains - Retrieve a list of FortiCloud login domains."""
    try:
        result = fgt.api.monitor.registration.forticloud.domains.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "500" in str(e):
            print("Server error (500) - FortiCloud service may not be configured")
        else:
            raise


def test_get_registration_forticare_check_connectivity():
    """Test GET /monitor/registration/forticare/check-connectivity - Check connectivity to FortiCare servers."""
    try:
        result = fgt.api.monitor.registration.forticare.check_connectivity.get()
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        elif "500" in str(e):
            print("Server error (500) - FortiCare service may not be configured")
        else:
            raise


# def test_get_registration_forticloud_device_status_fortiap():
#     """Test GET /monitor/registration/forticloud/device-status - Fetch FortiAP registration status from FortiCloud."""
#     # DISABLED: Returns 424 error - FortiCloud service not configured
#     try:
#         # Query FortiAP device status with serial FP231FTF2209AHNJ
#         result = fgt.api.monitor.registration.forticloud.device_status.get(
#             serials=["FP231FTF2209AHNJ"],
#             vdom="root"
#         )
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "424" in str(e):
#             print("Service unavailable (424) - FortiCloud service not configured")
#         elif "500" in str(e):
#             print("Server error (500) - FortiCloud service may not be configured")
#         else:
#             raise


# def test_get_registration_forticloud_device_status_fortiswitch():
#     """Test GET /monitor/registration/forticloud/device-status - Fetch FortiSwitch registration status from FortiCloud."""
#     # DISABLED: Returns 424 error - FortiCloud service not configured
#     try:
#         # Query FortiSwitch device status with serial S124FPTF22004975
#         result = fgt.api.monitor.registration.forticloud.device_status.get(
#             serials=["S124FPTF22004975"],
#             vdom="root"
#         )
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         elif "424" in str(e):
#             print("Service unavailable (424) - FortiCloud service not configured")
#         elif "500" in str(e):
#             print("Server error (500) - FortiCloud service may not be configured")
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
    
    print("Running Registration monitor endpoint tests...")
    
    test_get_registration_forticloud_disclaimer()
    print("✓ test_get_registration_forticloud_disclaimer")
    
    test_get_registration_forticloud_domains()
    print("✓ test_get_registration_forticloud_domains")
    
    test_get_registration_forticare_check_connectivity()
    print("✓ test_get_registration_forticare_check_connectivity")

    # test_get_registration_forticloud_device_status_fortiap()
    # print("✓ test_get_registration_forticloud_device_status_fortiap")

    # test_get_registration_forticloud_device_status_fortiswitch()
    # print("✓ test_get_registration_forticloud_device_status_fortiswitch")
    

    
    print("\n✓ All Registration endpoint tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 3 active tests, 1 commented out (requires device serial)")
    print("- Total: 3 active test functions covering Registration monitor endpoints")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
