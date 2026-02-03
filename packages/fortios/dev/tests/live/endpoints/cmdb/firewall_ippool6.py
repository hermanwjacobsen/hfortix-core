import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_ippool6_1"
TEST_TYPE = "overload"
TEST_STARTIP = "2001:db8:1::1"
TEST_ENDIP = "2001:db8:1::ff"


def cleanup():
    try:
        pools = fgt.api.cmdb.firewall.ippool6.get()
        for pool in pools:
            if getattr(pool, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.ippool6.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_ippool6():
    result = fgt.api.cmdb.firewall.ippool6.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_ippool6():
    result = fgt.api.cmdb.firewall.ippool6.post(
        name=TEST_NAME,
        type=TEST_TYPE,
        startip=TEST_STARTIP,
        endip=TEST_ENDIP
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_ippool6():
    result = fgt.api.cmdb.firewall.ippool6.put(
        name=TEST_NAME,
        type=TEST_TYPE,
        startip="2001:db8:2::1",
        endip="2001:db8:2::ff"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ippool6.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.startip == "2001:db8:2::1"
    assert verify.endip == "2001:db8:2::ff"

def test_get_specific_ippool6():
    result = fgt.api.cmdb.firewall.ippool6.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_ippool6():
    result = fgt.api.cmdb.firewall.ippool6.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    pools = fgt.api.cmdb.firewall.ippool6.get()
    names = [getattr(p, "name", None) for p in pools]
    assert TEST_NAME not in names, "IPv6 pool should have been deleted"

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
    test_get_ippool6()
    print("✓ test_get_ippool6 passed")
    test_post_ippool6()
    print("✓ test_post_ippool6 passed")
    test_put_ippool6()
    print("✓ test_put_ippool6 passed")
    test_get_specific_ippool6()
    print("✓ test_get_specific_ippool6 passed")
    test_delete_ippool6()
    print("✓ test_delete_ippool6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
