import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_GROUP_NAME = "test_vipgrp_9999961"
TEST_VIP1_NAME = "test_vip_member1_9999961"
TEST_VIP2_NAME = "test_vip_member2_9999961"
TEST_EXTIP1 = "203.0.113.20"
TEST_EXTIP2 = "203.0.113.21"
TEST_MAPPEDIP1 = "192.168.100.20"
TEST_MAPPEDIP2 = "192.168.100.21"
TEST_EXTINTF = "port3"


def cleanup():
    try:
        # Clean up VIP group
        vipgrps = fgt.api.cmdb.firewall.vipgrp.get()
        for vipgrp in vipgrps:
            if getattr(vipgrp, "name", None) == TEST_GROUP_NAME:
                fgt.api.cmdb.firewall.vipgrp.delete(name=TEST_GROUP_NAME)
                break
        
        # Clean up member VIPs
        vips = fgt.api.cmdb.firewall.vip.get()
        for vip in vips:
            vip_name = getattr(vip, "name", None)
            if vip_name in [TEST_VIP1_NAME, TEST_VIP2_NAME]:
                fgt.api.cmdb.firewall.vip.delete(name=vip_name)
    except Exception:
        pass

def test_get_vipgrp():
    """Test GET all VIP groups."""
    result = fgt.api.cmdb.firewall.vipgrp.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_vipgrp():
    # First create member VIPs
    fgt.api.cmdb.firewall.vip.post(
        name=TEST_VIP1_NAME,
        type="static-nat",
        extip=TEST_EXTIP1,
        mappedip=[{"range": f"{TEST_MAPPEDIP1}-{TEST_MAPPEDIP1}"}],
        extintf=TEST_EXTINTF
    )
    fgt.api.cmdb.firewall.vip.post(
        name=TEST_VIP2_NAME,
        type="static-nat",
        extip=TEST_EXTIP2,
        mappedip=[{"range": f"{TEST_MAPPEDIP2}-{TEST_MAPPEDIP2}"}],
        extintf=TEST_EXTINTF
    )
    
    # Create VIP group
    result = fgt.api.cmdb.firewall.vipgrp.post(
        name=TEST_GROUP_NAME,
        interface=TEST_EXTINTF,
        member=[
            {"name": TEST_VIP1_NAME},
            {"name": TEST_VIP2_NAME}
        ],
        comments="Test VIP group"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_vipgrp():
    updated_comments = "Updated VIP group"
    result = fgt.api.cmdb.firewall.vipgrp.put(
        name=TEST_GROUP_NAME,
        comments=updated_comments,
        color=5
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.vipgrp.get(name=TEST_GROUP_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comments == updated_comments
    assert verify.color == 5

def test_get_specific_vipgrp():
    result = fgt.api.cmdb.firewall.vipgrp.get(name=TEST_GROUP_NAME)
    assert result is not None
    assert result.name == TEST_GROUP_NAME

def test_delete_vipgrp():
    result = fgt.api.cmdb.firewall.vipgrp.delete(name=TEST_GROUP_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    vipgrps = fgt.api.cmdb.firewall.vipgrp.get()
    names = [getattr(v, "name", None) for v in vipgrps]
    assert TEST_GROUP_NAME not in names, "VIP group should have been deleted"

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
    test_get_vipgrp()
    print("✓ test_get_vipgrp passed")
    test_post_vipgrp()
    print("✓ test_post_vipgrp passed")
    test_put_vipgrp()
    print("✓ test_put_vipgrp passed")
    test_get_specific_vipgrp()
    print("✓ test_get_specific_vipgrp passed")
    test_delete_vipgrp()
    print("✓ test_delete_vipgrp passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
