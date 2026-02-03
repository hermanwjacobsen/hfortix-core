import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_ID = 9999993
TEST_NAME = "test_mcast_policy6_1"
TEST_SRCINTF = "port3"
TEST_DSTINTF = "port4"
TEST_ACTION = "accept"


def cleanup():
    try:
        policies = fgt.api.cmdb.firewall.multicast_policy6.get()
        for policy in policies:
            if getattr(policy, "id", None) == TEST_ID:
                fgt.api.cmdb.firewall.multicast_policy6.delete(id=TEST_ID)
                break
    except Exception:
        pass

def test_get_multicast_policy6():
    result = fgt.api.cmdb.firewall.multicast_policy6.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_multicast_policy6():
    result = fgt.api.cmdb.firewall.multicast_policy6.post(
        id=TEST_ID,
        name=TEST_NAME,
        srcintf=TEST_SRCINTF,
        dstintf=TEST_DSTINTF,
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        action=TEST_ACTION,
        status="enable"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_multicast_policy6():
    result = fgt.api.cmdb.firewall.multicast_policy6.put(
        id=TEST_ID,
        name="test_mcast_policy6_1_updated",
        srcintf=TEST_SRCINTF,
        dstintf=TEST_DSTINTF,
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        action="deny",
        status="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.multicast_policy6.get(id=TEST_ID)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.action == "deny"

def test_get_specific_multicast_policy6():
    result = fgt.api.cmdb.firewall.multicast_policy6.get(id=TEST_ID)
    assert result is not None
    assert result.id == TEST_ID

def test_delete_multicast_policy6():
    result = fgt.api.cmdb.firewall.multicast_policy6.delete(id=TEST_ID)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    policies = fgt.api.cmdb.firewall.multicast_policy6.get()
    ids = [getattr(p, "id", None) for p in policies]
    assert TEST_ID not in ids, "Multicast policy6 should have been deleted"

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
    test_get_multicast_policy6()
    print("✓ test_get_multicast_policy6 passed")
    test_post_multicast_policy6()
    print("✓ test_post_multicast_policy6 passed")
    test_put_multicast_policy6()
    print("✓ test_put_multicast_policy6 passed")
    test_get_specific_multicast_policy6()
    print("✓ test_get_specific_multicast_policy6 passed")
    test_delete_multicast_policy6()
    print("✓ test_delete_multicast_policy6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
