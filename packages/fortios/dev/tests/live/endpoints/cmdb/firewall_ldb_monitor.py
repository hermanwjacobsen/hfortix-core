import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_ldb_monitor1"
TEST_TYPE = "ping"
TEST_INTERVAL = 10
TEST_TIMEOUT = 2
TEST_RETRY = 3


def cleanup():
    try:
        monitors = fgt.api.cmdb.firewall.ldb_monitor.get()
        for monitor in monitors:
            if getattr(monitor, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.ldb_monitor.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_ldb_monitor():
    result = fgt.api.cmdb.firewall.ldb_monitor.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_ldb_monitor():
    result = fgt.api.cmdb.firewall.ldb_monitor.post(
        name=TEST_NAME,
        type=TEST_TYPE,
        interval=TEST_INTERVAL,
        timeout=TEST_TIMEOUT,
        retry=TEST_RETRY
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_ldb_monitor():
    result = fgt.api.cmdb.firewall.ldb_monitor.put(
        name=TEST_NAME,
        type=TEST_TYPE,
        interval=15,
        timeout=3,
        retry=5
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ldb_monitor.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.interval == 15
    assert verify.timeout == 3
    assert verify.retry == 5

def test_get_specific_ldb_monitor():
    result = fgt.api.cmdb.firewall.ldb_monitor.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_ldb_monitor():
    result = fgt.api.cmdb.firewall.ldb_monitor.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    monitors = fgt.api.cmdb.firewall.ldb_monitor.get()
    names = [getattr(m, "name", None) for m in monitors]
    assert TEST_NAME not in names, "LDB monitor should have been deleted"

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
    test_get_ldb_monitor()
    print("✓ test_get_ldb_monitor passed")
    test_post_ldb_monitor()
    print("✓ test_post_ldb_monitor passed")
    test_put_ldb_monitor()
    print("✓ test_put_ldb_monitor passed")
    test_get_specific_ldb_monitor()
    print("✓ test_get_specific_ldb_monitor passed")
    test_delete_ldb_monitor()
    print("✓ test_delete_ldb_monitor passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
