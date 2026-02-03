import argparse
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_POLICYID = 90001


def cleanup():
    """Clean up test interface policies."""
    try:
        policies = fgt.api.cmdb.firewall.interface_policy.get()
        for pol in policies:
            if pol.policyid == TEST_POLICYID:
                try:
                    fgt.api.cmdb.firewall.interface_policy.delete(policyid=pol.policyid)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_interface_policies():
    """Test: Get all interface policies."""
    result = fgt.api.cmdb.firewall.interface_policy.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_interface_policy():
    """Test: Create interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy.post(
        policyid=TEST_POLICYID,
        interface="port3",
        status="enable",
        comments="Test interface policy",
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        service=[{"name": "ALL"}],
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_interface_policy():
    """Test: Update interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy.put(
        policyid=TEST_POLICYID,
        comments="Updated interface policy",
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.interface_policy.get(policyid=TEST_POLICYID)
    assert verify is not None
    assert verify.comments == "Updated interface policy"


def test_get_specific_interface_policy():
    """Test: Get specific interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy.get(policyid=TEST_POLICYID)
    assert result is not None
    assert result.policyid == TEST_POLICYID


def test_delete_interface_policy():
    """Test: Delete interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy.delete(policyid=TEST_POLICYID)
    assert result is not None
    assert result.http_status == "success"
    policies = fgt.api.cmdb.firewall.interface_policy.get()
    ids = [p.policyid for p in policies]
    assert TEST_POLICYID not in ids, "Interface policy should have been deleted"


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
    test_get_interface_policies()
    print("✓ test_get_interface_policies passed")
    test_post_interface_policy()
    print("✓ test_post_interface_policy passed")
    test_put_interface_policy()
    print("✓ test_put_interface_policy passed")
    test_get_specific_interface_policy()
    print("✓ test_get_specific_interface_policy passed")
    test_delete_interface_policy()
    print("✓ test_delete_interface_policy passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
