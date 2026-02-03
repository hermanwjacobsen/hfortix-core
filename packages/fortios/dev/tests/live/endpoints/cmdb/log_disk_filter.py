import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# NOTE: IPS view-map endpoint appears to be read-only or requires specific conditions
# POST returns None even with valid parameters

def cleanup():
    try:
        fgt.api.cmdb.log.disk.filter.put(
            severity="information",
        )
    except Exception:
        pass


def test_get_log_disk_filter():
    """Test: Get all log disk filters."""
    result = fgt.api.cmdb.log.disk.filter.get(vdom="test")
    print(result.raw)
    assert result is not None
    assert result.http_status_code == 200

def test_put_log_disk_filter():
    """Test: Create a log disk filter entry."""
    result = fgt.api.cmdb.log.disk.filter.put(
        severity="critical",
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.log.disk.filter.get(vdom="test")
    assert verify is not None
    assert verify.severity == "critical"

def test_restore_log_disk_filter():
    """Test: Restore log disk filter to default state."""
    result = fgt.api.cmdb.log.disk.filter.put(
        severity="information",
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.log.disk.filter.get(vdom="test")
    assert verify is not None
    assert verify.severity == "information"



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
    test_get_log_disk_filter()
    print("✓ test_get_log_disk_filter passed")

    test_put_log_disk_filter()
    print("✓ test_put_log_disk_filter passed")

    test_restore_log_disk_filter()  
    print("✓ test_restore_log_disk_filter passed")
    
    print("\n✓ All log disk filter tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
