import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_vip_9999963"
TEST_EXTIP = "203.0.113.10"
TEST_MAPPEDIP_START = "192.168.100.10"
TEST_MAPPEDIP_END = "192.168.100.10"
TEST_EXTINTF = "port3"


def cleanup():
    try:
        vips = fgt.api.cmdb.firewall.vip.get()
        for vip in vips:
            if getattr(vip, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.vip.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_vip():
    """Test GET all virtual IPs."""
    result = fgt.api.cmdb.firewall.vip.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_vip():
    result = fgt.api.cmdb.firewall.vip.post(
        name=TEST_NAME,
        type="static-nat",
        extip=TEST_EXTIP,
        mappedip=[{"range": f"{TEST_MAPPEDIP_START}-{TEST_MAPPEDIP_END}"}],
        extintf=TEST_EXTINTF,
        comment="Test virtual IP for IPv4"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_vip():
    updated_comment = "Updated virtual IP for IPv4"
    result = fgt.api.cmdb.firewall.vip.put(
        name=TEST_NAME,
        comment=updated_comment,
        arp_reply="enable"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.vip.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comment == updated_comment

def test_get_specific_vip():
    result = fgt.api.cmdb.firewall.vip.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_vip():
    result = fgt.api.cmdb.firewall.vip.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    vips = fgt.api.cmdb.firewall.vip.get()
    names = [getattr(v, "name", None) for v in vips]
    assert TEST_NAME not in names, "VIP should have been deleted"

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
    test_get_vip()
    print("✓ test_get_vip passed")
    test_post_vip()
    print("✓ test_post_vip passed")
    test_put_vip()
    print("✓ test_put_vip passed")
    test_get_specific_vip()
    print("✓ test_get_specific_vip passed")
    test_delete_vip()
    print("✓ test_delete_vip passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
