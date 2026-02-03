import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_POLICYID = None
TEST_NAME = "testdospolicy6_1"


def cleanup():
    """Clean up test IPv6 DoS policies."""
    try:
        policies = fgt.api.cmdb.firewall.DoS_policy6.get()
        for policy in policies:
            if policy.name and str(policy.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.DoS_policy6.delete(policyid=policy.policyid)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_dos_policies6():
    """Test: Get all IPv6 DoS policies."""
    result = fgt.api.cmdb.firewall.DoS_policy6.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_dos_policy6():
    """Test: Create IPv6 DoS policy."""
    global TEST_POLICYID
    
    result = fgt.api.cmdb.firewall.DoS_policy6.post(
        name=TEST_NAME,
        interface="port3",
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        service=[{"name": "ALL"}],
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Get the created policy ID
    policies = fgt.api.cmdb.firewall.DoS_policy6.get()
    for policy in policies:
        if policy.name == TEST_NAME:
            TEST_POLICYID = policy.policyid
            break
    
    assert TEST_POLICYID is not None, "Could not find created IPv6 DoS policy"


def test_put_dos_policy6():
    """Test: Update IPv6 DoS policy."""
    global TEST_POLICYID
    
    # Get current policy ID if not set
    if TEST_POLICYID is None:
        policies = fgt.api.cmdb.firewall.DoS_policy6.get()
        for policy in policies:
            if policy.name == TEST_NAME:
                TEST_POLICYID = policy.policyid
                break
    
    assert TEST_POLICYID is not None, "No policy ID available"
    
    result = fgt.api.cmdb.firewall.DoS_policy6.put(
        policyid=TEST_POLICYID,
        comments="Updated IPv6 DoS Policy"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.DoS_policy6.get(policyid=TEST_POLICYID)
    assert verify is not None
    assert verify.comments == "Updated IPv6 DoS Policy"


def test_get_specific_dos_policy6():
    """Test: Get specific IPv6 DoS policy."""
    global TEST_POLICYID
    
    if TEST_POLICYID is None:
        policies = fgt.api.cmdb.firewall.DoS_policy6.get()
        for policy in policies:
            if policy.name == TEST_NAME:
                TEST_POLICYID = policy.policyid
                break
    
    assert TEST_POLICYID is not None, "No policy ID available"
    
    result = fgt.api.cmdb.firewall.DoS_policy6.get(policyid=TEST_POLICYID)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_dos_policy6():
    """Test: Delete IPv6 DoS policy."""
    global TEST_POLICYID
    
    if TEST_POLICYID is None:
        policies = fgt.api.cmdb.firewall.DoS_policy6.get()
        for policy in policies:
            if policy.name == TEST_NAME:
                TEST_POLICYID = policy.policyid
                break
    
    assert TEST_POLICYID is not None, "No policy ID available"
    
    result = fgt.api.cmdb.firewall.DoS_policy6.delete(policyid=TEST_POLICYID)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    policies = fgt.api.cmdb.firewall.DoS_policy6.get()
    policy_ids = [p.policyid for p in policies]
    assert TEST_POLICYID not in policy_ids, "IPv6 DoS policy should have been deleted"


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
        
    test_get_dos_policies6()
    print("✓ test_get_dos_policies6 passed")

    test_post_dos_policy6()
    print("✓ test_post_dos_policy6 passed")

    test_put_dos_policy6()
    print("✓ test_put_dos_policy6 passed")

    test_get_specific_dos_policy6()
    print("✓ test_get_specific_dos_policy6 passed")

    test_delete_dos_policy6()
    print("✓ test_delete_dos_policy6 passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
