import argparse
import sys
from pathlib import Path

import pytest

# Run DLP tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group("emailfilter")

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def cleanup():
    try:
        fgt.api.cmdb.endpoint_control.settings.put(
            override="disable"
        )
    except Exception:
        pass

    try:
        fgt.api.cmdb.endpoint_control.fctems.put(
            ems_id=3,
            name="",
            server="",
            status="disable"
        )
    except Exception:
        pass

    try:
        fgt.api.cmdb.endpoint_control.fctems_override.put(
            ems_id=4,
            name="",
            server="",
            status="disable"
        )
    except Exception:
        pass

def test_get_endpoint_control():
    """Test: Get endpoint control settings"""
    result = fgt.api.cmdb.endpoint_control.settings.get()
    assert result is not None
    assert result.http_status_code == 200

def test_put_endpoint_control():
    """Test: Update endpoint control settings"""
    result = fgt.api.cmdb.endpoint_control.settings.put(
        override="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.endpoint_control.settings.get()
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.override == "enable"

def test_restore_endpoint_control():    
    """Test: Restore endpoint control settings to default"""
    result = fgt.api.cmdb.endpoint_control.settings.put(
        override="disable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.endpoint_control.settings.get()
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.override == "disable"
 
def test_get_endpoint_control_ftcems():
    """Test: Get endpoint control ftcms settings"""
    result = fgt.api.cmdb.endpoint_control.fctems.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_endpoint_control_ftcems():
    """Test: Update endpoint control ftcms settings
    
    Note: fctems table has pre-defined entries (ems_id 3-7).
    POST always fails with HTTP 500 - cannot create new entries via API.
    Once deleted, entries cannot be recreated via API.
    When enabling EMS, both 'name' and 'server' are required.
    """
    result = fgt.api.cmdb.endpoint_control.fctems.put(
        ems_id=3,
        status="enable",
        name="test-ems",
        server="ems.example.com",
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.endpoint_control.fctems.get(ems_id=3)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == "test-ems"
    assert verify.server == "ems.example.com"



def test_get_specific_endpoint_control_ftcems():
    """Test: Get specific endpoint control ftcms settings"""
    result = fgt.api.cmdb.endpoint_control.fctems.get(ems_id=3)
    assert result is not None
    assert result.http_status_code == 200
    assert result.ems_id == 3


def test_restore_endpoint_control_ftcems():
    """Test: Restore fctems entry to default state"""
    result = fgt.api.cmdb.endpoint_control.fctems.put(
        ems_id=3,
        name="",
        server="",
        status="disable"
    )
    assert result is not None
    assert result.http_status == "success"


# =============================================================================
# fctems-override Tests (Static Table - No POST/DELETE)
# =============================================================================

def test_get_endpoint_control_fctems_override():
    """Test: Get all endpoint control fctems-override entries
    
    Note: fctems-override is a static table with pre-defined entries (ems_id 1-7).
    POST and DELETE operations fail - entries can only be modified via PUT.
    """
    result = fgt.api.cmdb.endpoint_control.fctems_override.get()
    assert result is not None
    assert result.http_status_code == 200


def test_get_specific_endpoint_control_fctems_override():
    """Test: Get specific fctems-override entry"""
    result = fgt.api.cmdb.endpoint_control.fctems_override.get(ems_id=4)
    assert result is not None
    assert result.http_status_code == 200
    assert result.ems_id == 4


def test_put_endpoint_control_fctems_override():
    """Test: Update fctems-override entry
    
    Note: Like fctems, requires 'name' and 'server' when enabling.
    This is a vdom-override table - modifications apply to the current vdom.
    """
    result = fgt.api.cmdb.endpoint_control.fctems_override.put(
        ems_id=4,
        status="enable",
        name="override-ems-test",
        server="ems-override.example.com",
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.endpoint_control.fctems_override.get(ems_id=4)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == "override-ems-test"
    assert verify.server == "ems-override.example.com"


def test_restore_endpoint_control_fctems_override():
    """Test: Restore fctems-override entry to default state"""
    result = fgt.api.cmdb.endpoint_control.fctems_override.put(
        ems_id=4,
        name="",
        server="",
        status="disable"
    )
    assert result is not None
    assert result.http_status == "success"



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
    test_get_endpoint_control()
    print("✓ test_get_endpoint_control passed")

    test_put_endpoint_control()
    print("✓ test_put_endpoint_control passed")

    test_restore_endpoint_control()
    print("✓ test_restore_endpoint_control passed")

    test_get_endpoint_control_ftcems()
    print("✓ test_get_endpoint_control_ftcems passed")

    test_put_endpoint_control_ftcems()
    print("✓ test_put_endpoint_control_ftcems passed")
    
    test_get_specific_endpoint_control_ftcems()
    print("✓ test_get_specific_endpoint_control_ftcems passed")

    test_restore_endpoint_control_ftcems()
    print("✓ test_restore_endpoint_control_ftcems passed")

    # fctems-override tests
    test_get_endpoint_control_fctems_override()
    print("✓ test_get_endpoint_control_fctems_override passed")

    test_get_specific_endpoint_control_fctems_override()
    print("✓ test_get_specific_endpoint_control_fctems_override passed")

    test_put_endpoint_control_fctems_override()
    print("✓ test_put_endpoint_control_fctems_override passed")

    test_restore_endpoint_control_fctems_override()
    print("✓ test_restore_endpoint_control_fctems_override passed")

    cleanup()   
    print("✓ Post-Cleanup passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
