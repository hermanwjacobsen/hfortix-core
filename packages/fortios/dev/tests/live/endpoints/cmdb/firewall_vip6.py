import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_vip6_9999962"
TEST_EXTIP = "2001:db8:1::10"
TEST_MAPPEDIP = "2001:db8:2::10-2001:db8:2::10"


def cleanup():
    try:
        vips = fgt.api.cmdb.firewall.vip6.get()
        for vip in vips:
            if getattr(vip, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.vip6.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_vip6():
    """Test GET all IPv6 virtual IPs."""
    result = fgt.api.cmdb.firewall.vip6.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_vip6():
    result = fgt.api.cmdb.firewall.vip6.post(
        name=TEST_NAME,
        type="static-nat",
        extip=TEST_EXTIP,
        mappedip=TEST_MAPPEDIP,
        comment="Test virtual IP for IPv6"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_vip6():
    updated_comment = "Updated virtual IP for IPv6"
    result = fgt.api.cmdb.firewall.vip6.put(
        name=TEST_NAME,
        comment=updated_comment,
        ndp_reply="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.vip6.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comment == updated_comment

def test_get_specific_vip6():
    result = fgt.api.cmdb.firewall.vip6.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_vip6():
    result = fgt.api.cmdb.firewall.vip6.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    vips = fgt.api.cmdb.firewall.vip6.get()
    names = [getattr(v, "name", None) for v in vips]
    assert TEST_NAME not in names, "VIP6 should have been deleted"

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
    test_get_vip6()
    print("✓ test_get_vip6 passed")
    test_post_vip6()
    print("✓ test_post_vip6 passed")
    test_put_vip6()
    print("✓ test_put_vip6 passed")
    test_get_specific_vip6()
    print("✓ test_get_specific_vip6 passed")
    test_delete_vip6()
    print("✓ test_delete_vip6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
