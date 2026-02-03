import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_SENSOR_NAME = "test_ips_sensor1"


def cleanup():
    """Clean up test IPS sensors."""
    try:
        sensors = fgt.api.cmdb.ips.sensor.get(vdom="test")
        for sensor in sensors:
            if sensor.name and str(sensor.name).startswith("test"):
                try:
                    fgt.api.cmdb.ips.sensor.delete(name=sensor.name, vdom="test")
                except Exception:
                    pass
    except Exception:
        pass


def test_get_ips_sensors():
    """Test: Get all IPS sensors."""
    result = fgt.api.cmdb.ips.sensor.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


def test_post_ips_sensor():
    """Test: Create IPS sensor."""
    result = fgt.api.cmdb.ips.sensor.post(
        name=TEST_SENSOR_NAME,
        comment="Test IPS sensor",
        block_malicious_url="enable",
        scan_botnet_connections="block",
        extended_log="enable",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_ips_sensor():
    """Test: Update IPS sensor."""
    result = fgt.api.cmdb.ips.sensor.put(
        name=TEST_SENSOR_NAME,
        comment="Updated IPS sensor",
        extended_log="disable",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.sensor.get(name=TEST_SENSOR_NAME, vdom="test")
    assert verify is not None
    assert verify.comment == "Updated IPS sensor"
    assert verify.extended_log == "disable"


def test_get_specific_ips_sensor():
    """Test: Get specific IPS sensor."""
    result = fgt.api.cmdb.ips.sensor.get(name=TEST_SENSOR_NAME, vdom="test")
    assert result is not None
    assert result.name == TEST_SENSOR_NAME


def test_delete_ips_sensor():
    """Test: Delete IPS sensor."""
    result = fgt.api.cmdb.ips.sensor.delete(name=TEST_SENSOR_NAME, vdom="test")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    sensors = fgt.api.cmdb.ips.sensor.get(vdom="test")
    sensor_names = [s.name for s in sensors]
    assert TEST_SENSOR_NAME not in sensor_names, "IPS sensor should have been deleted"


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
    cleanup()
    print("✓ Pre-Cleanup passed")
        
    test_get_ips_sensors()
    print("✓ test_get_ips_sensors passed")

    test_post_ips_sensor()
    print("✓ test_post_ips_sensor passed")

    test_put_ips_sensor()
    print("✓ test_put_ips_sensor passed")

    test_get_specific_ips_sensor()
    print("✓ test_get_specific_ips_sensor passed")

    test_delete_ips_sensor()
    print("✓ test_delete_ips_sensor passed")

    cleanup()
    print("✓ Post-Cleanup passed")
    
    print("\n✓ All IPS sensor tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
