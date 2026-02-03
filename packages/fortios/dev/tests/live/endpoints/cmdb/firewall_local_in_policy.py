import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_POLICYID = 9999996
TEST_ACTION = "accept"
TEST_INTF = "port3"


def cleanup():
    try:
        policies = fgt.api.cmdb.firewall.local_in_policy.get()
        for policy in policies:
            if getattr(policy, "policyid", None) == TEST_POLICYID:
                fgt.api.cmdb.firewall.local_in_policy.delete(policyid=TEST_POLICYID)
                break
    except Exception:
        pass

def test_get_local_in_policy():
    result = fgt.api.cmdb.firewall.local_in_policy.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_local_in_policy():
    result = fgt.api.cmdb.firewall.local_in_policy.post(
        policyid=TEST_POLICYID,
        intf=[{"name": TEST_INTF}],
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        action=TEST_ACTION,
        service=[{"name": "ALL"}],
        schedule="always",
        status="enable"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_local_in_policy():
    result = fgt.api.cmdb.firewall.local_in_policy.put(
        policyid=TEST_POLICYID,
        intf=[{"name": "port4"}],
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        action="deny",
        service=[{"name": "ALL"}],
        schedule="always",
        status="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.local_in_policy.get(policyid=TEST_POLICYID)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.action == "deny"

def test_get_specific_local_in_policy():
    result = fgt.api.cmdb.firewall.local_in_policy.get(policyid=TEST_POLICYID)
    assert result is not None
    assert result.policyid == TEST_POLICYID

def test_delete_local_in_policy():
    result = fgt.api.cmdb.firewall.local_in_policy.delete(policyid=TEST_POLICYID)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    policies = fgt.api.cmdb.firewall.local_in_policy.get()
    ids = [getattr(p, "policyid", None) for p in policies]
    assert TEST_POLICYID not in ids, "Local-in policy should have been deleted"

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
    test_get_local_in_policy()
    print("✓ test_get_local_in_policy passed")
    test_post_local_in_policy()
    print("✓ test_post_local_in_policy passed")
    test_put_local_in_policy()
    print("✓ test_put_local_in_policy passed")
    test_get_specific_local_in_policy()
    print("✓ test_get_specific_local_in_policy passed")
    test_delete_local_in_policy()
    print("✓ test_delete_local_in_policy passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
