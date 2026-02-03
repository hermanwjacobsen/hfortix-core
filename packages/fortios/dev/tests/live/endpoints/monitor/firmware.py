import argparse
import sys
from pathlib import Path
import pytest

# Run firmware monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# Firmware Monitor Tests - GET endpoints
# ============================================================================

def test_get_firmware_extension_device_fortiswitch():
    """Test GET /monitor/firmware/extension-device - Retrieve recommended firmwares for FortiSwitch."""
    try:
        result = fgt.api.monitor.firmware.extension_device.get(type="fortiswitch")
        print(result.json)
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firmware_extension_device_fortiap():
    """Test GET /monitor/firmware/extension-device - Retrieve recommended firmwares for FortiAP."""
    try:
        result = fgt.api.monitor.firmware.extension_device.get(type="fortiap")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


def test_get_firmware_extension_device_fortiextender():
    """Test GET /monitor/firmware/extension-device - Retrieve recommended firmwares for FortiExtender."""
    try:
        result = fgt.api.monitor.firmware.extension_device.get(type="fortiextender")
        assert result is not None
        assert result.http_status_code == 200
    except Exception as e:
        if "404" in str(e):
            print("Resource not found")
        else:
            raise


# def test_get_firmware_extension_device_with_timeout():
#     """Test GET /monitor/firmware/extension-device - Retrieve recommended firmwares with custom timeout."""
#     # Requires type parameter, optional timeout parameter
#     try:
#         result = fgt.api.monitor.firmware.extension_device.get(type="fortiswitch", timeout=30)
#         assert result is not None
#         assert result.http_status_code == 200
#     except Exception as e:
#         if "404" in str(e):
#             print("Resource not found")
#         else:
#             raise


# def test_get_firmware_extension_device_with_version():
#     """Test GET /monitor/firmware/extension-device - Retrieve recommended firmwares for specific FortiGate version."""
#     # Requires type parameter, optional version parameter
#     try:
#         result = fgt.api.monitor.firmware.extension_device.get(type="fortiswitch", version="7.6.0")
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
    
    print("Running firmware monitor endpoint tests...")
    
    test_get_firmware_extension_device_fortiswitch()
    print("✓ test_get_firmware_extension_device_fortiswitch")
    
    test_get_firmware_extension_device_fortiap()
    print("✓ test_get_firmware_extension_device_fortiap")
    
    test_get_firmware_extension_device_fortiextender()
    print("✓ test_get_firmware_extension_device_fortiextender")
    
    print("\n✓ All firmware endpoint tests completed!")
    print("\nSummary:")
    print("- GET endpoints: 3 active tests")
    print("- Total: 3 test functions covering firmware monitor endpoint")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
