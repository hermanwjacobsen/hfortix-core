import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_GROUP_NAME = "test_vipgrp6_9999960"
TEST_VIP1_NAME = "test_vip6_member1_9999960"
TEST_VIP2_NAME = "test_vip6_member2_9999960"
TEST_EXTIP1 = "2001:db8:1::20"
TEST_EXTIP2 = "2001:db8:1::21"
TEST_MAPPEDIP1 = "2001:db8:2::20-2001:db8:2::20"
TEST_MAPPEDIP2 = "2001:db8:2::21-2001:db8:2::21"


def cleanup():
    try:
        # Clean up VIP6 group first
        vipgrps = fgt.api.cmdb.firewall.vipgrp6.get()
        for vipgrp in vipgrps:
            if getattr(vipgrp, "name", None) == TEST_GROUP_NAME:
                fgt.api.cmdb.firewall.vipgrp6.delete(name=TEST_GROUP_NAME)
                break
        
        # Clean up member VIP6s
        vips = fgt.api.cmdb.firewall.vip6.get()
        for vip in vips:
            vip_name = getattr(vip, "name", None)
            if vip_name in [TEST_VIP1_NAME, TEST_VIP2_NAME]:
                fgt.api.cmdb.firewall.vip6.delete(name=vip_name)
    except Exception:
        pass


@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    """Setup and teardown for all tests."""
    cleanup()  # Pre-cleanup
    yield
    cleanup()  # Post-cleanup


def test_get_vipgrp6():
    """Test GET all IPv6 VIP groups."""
    result = fgt.api.cmdb.firewall.vipgrp6.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_vipgrp6():
    """Create IPv6 VIP group with member VIPs."""
    # First create member VIP6s
    try:
        fgt.api.cmdb.firewall.vip6.post(
            name=TEST_VIP1_NAME,
            type="static-nat",
            extip=TEST_EXTIP1,
            mappedip=TEST_MAPPEDIP1
        )
    except Exception:
        pass  # May already exist
    
    try:
        fgt.api.cmdb.firewall.vip6.post(
            name=TEST_VIP2_NAME,
            type="static-nat",
            extip=TEST_EXTIP2,
            mappedip=TEST_MAPPEDIP2
        )
    except Exception:
        pass  # May already exist
    
    # Create VIP6 group
    result = fgt.api.cmdb.firewall.vipgrp6.post(
        name=TEST_GROUP_NAME,
        member=[
            {"name": TEST_VIP1_NAME},
            {"name": TEST_VIP2_NAME}
        ],
        comments="Test IPv6 VIP group"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_vipgrp6():
    updated_comments = "Updated IPv6 VIP group"
    result = fgt.api.cmdb.firewall.vipgrp6.put(
        name=TEST_GROUP_NAME,
        comments=updated_comments,
        color=10
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.vipgrp6.get(name=TEST_GROUP_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comments == updated_comments
    assert verify.color == 10

def test_get_specific_vipgrp6():
    result = fgt.api.cmdb.firewall.vipgrp6.get(name=TEST_GROUP_NAME)
    assert result is not None
    assert result.name == TEST_GROUP_NAME

def test_delete_vipgrp6():
    """Delete the IPv6 VIP group."""
    result = fgt.api.cmdb.firewall.vipgrp6.delete(name=TEST_GROUP_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    vipgrps = fgt.api.cmdb.firewall.vipgrp6.get()
    names = [getattr(v, "name", None) for v in vipgrps]
    assert TEST_GROUP_NAME not in names, "VIP6 group should have been deleted"
    
    # Clean up member VIP6s after deleting group
    try:
        fgt.api.cmdb.firewall.vip6.delete(name=TEST_VIP1_NAME)
    except Exception:
        pass
    try:
        fgt.api.cmdb.firewall.vip6.delete(name=TEST_VIP2_NAME)
    except Exception:
        pass

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
    test_get_vipgrp6()
    print("✓ test_get_vipgrp6 passed")
    test_post_vipgrp6()
    print("✓ test_post_vipgrp6 passed")
    test_put_vipgrp6()
    print("✓ test_put_vipgrp6 passed")
    test_get_specific_vipgrp6()
    print("✓ test_get_specific_vipgrp6 passed")
    test_delete_vipgrp6()
    print("✓ test_delete_vipgrp6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
