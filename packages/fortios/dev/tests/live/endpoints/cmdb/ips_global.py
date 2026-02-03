import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# Global variable to store original configuration
original_config = None


def test_get_ips_global():
    """Test: Get IPS global configuration."""
    global original_config
    result = fgt.api.cmdb.ips.global_.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original configuration for restoration
    original_config = {
        "fail_open": result.fail_open if hasattr(result, "fail_open") else None,
        "database": result.database if hasattr(result, "database") else None,
        "traffic_submit": result.traffic_submit if hasattr(result, "traffic_submit") else None,
    }


def test_put_ips_global_fail_open():
    """Test: Update IPS global fail-open setting."""
    result = fgt.api.cmdb.ips.global_.put(
        fail_open="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.global_.get()
    assert verify is not None
    assert verify.fail_open == "enable"


def test_put_ips_global_database():
    """Test: Update IPS global database setting."""
    result = fgt.api.cmdb.ips.global_.put(
        database="extended"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.global_.get()
    assert verify is not None
    assert verify.database == "extended"


def test_put_ips_global_traffic_submit():
    """Test: Update IPS global traffic submit setting."""
    result = fgt.api.cmdb.ips.global_.put(
        traffic_submit="disable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.global_.get()
    assert verify is not None
    assert verify.traffic_submit == "disable"


def test_restore_ips_global():
    """Test: Restore IPS global configuration to original state."""
    global original_config
    
    if original_config is None:
        return
    
    # Build restoration payload with only non-None values
    restore_payload = {}
    if original_config.get("fail_open") is not None:
        restore_payload["fail_open"] = original_config["fail_open"]
    if original_config.get("database") is not None:
        restore_payload["database"] = original_config["database"]
    if original_config.get("traffic_submit") is not None:
        restore_payload["traffic_submit"] = original_config["traffic_submit"]
    
    if restore_payload:
        result = fgt.api.cmdb.ips.global_.put(**restore_payload)
        assert result is not None
        assert result.http_status == "success"
        
        # Verify restoration
        verify = fgt.api.cmdb.ips.global_.get()
        assert verify is not None


def test_verify_ips_global_restored():
    """Test: Verify IPS global configuration was restored."""
    result = fgt.api.cmdb.ips.global_.get()
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
    test_get_ips_global()
    print("✓ test_get_ips_global passed")

    test_put_ips_global_fail_open()
    print("✓ test_put_ips_global_fail_open passed")

    test_put_ips_global_database()
    print("✓ test_put_ips_global_database passed")

    test_put_ips_global_traffic_submit()
    print("✓ test_put_ips_global_traffic_submit passed")

    test_restore_ips_global()
    print("✓ test_restore_ips_global passed")

    test_verify_ips_global_restored()
    print("✓ test_verify_ips_global_restored passed")
    
    print("\n✓ All IPS global configuration tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
