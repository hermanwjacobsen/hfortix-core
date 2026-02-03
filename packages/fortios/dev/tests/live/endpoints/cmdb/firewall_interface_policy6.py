import argparse
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_POLICYID = 90002


def cleanup():
    """Clean up test IPv6 interface policies."""
    try:
        policies = fgt.api.cmdb.firewall.interface_policy6.get()
        for pol in policies:
            if pol.policyid == TEST_POLICYID:
                try:
                    fgt.api.cmdb.firewall.interface_policy6.delete(policyid=pol.policyid)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_interface_policies6():
    """Test: Get all IPv6 interface policies."""
    result = fgt.api.cmdb.firewall.interface_policy6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_interface_policy6():
    """Test: Create IPv6 interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy6.post(
        policyid=TEST_POLICYID,
        interface="port3",
        status="enable",
        comments="Test IPv6 interface policy",
        srcaddr6=[{"name": "all"}],
        dstaddr6=[{"name": "all"}],
        service6=[{"name": "ALL"}],
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_interface_policy6():
    """Test: Update IPv6 interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy6.put(
        policyid=TEST_POLICYID,
        comments="Updated IPv6 interface policy",
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.interface_policy6.get(policyid=TEST_POLICYID)
    assert verify is not None
    assert verify.comments == "Updated IPv6 interface policy"


def test_get_specific_interface_policy6():
    """Test: Get specific IPv6 interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy6.get(policyid=TEST_POLICYID)
    assert result is not None
    assert result.policyid == TEST_POLICYID


def test_delete_interface_policy6():
    """Test: Delete IPv6 interface policy."""
    result = fgt.api.cmdb.firewall.interface_policy6.delete(policyid=TEST_POLICYID)
    assert result is not None
    assert result.http_status == "success"
    policies = fgt.api.cmdb.firewall.interface_policy6.get()
    ids = [p.policyid for p in policies]
    assert TEST_POLICYID not in ids, "IPv6 interface policy should have been deleted"


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
    test_get_interface_policies6()
    print("✓ test_get_interface_policies6 passed")
    test_post_interface_policy6()
    print("✓ test_post_interface_policy6 passed")
    test_put_interface_policy6()
    print("✓ test_put_interface_policy6 passed")
    test_get_specific_interface_policy6()
    print("✓ test_get_specific_interface_policy6 passed")
    test_delete_interface_policy6()
    print("✓ test_delete_interface_policy6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
