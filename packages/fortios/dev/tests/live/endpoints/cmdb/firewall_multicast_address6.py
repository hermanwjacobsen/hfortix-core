import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_multicast_addr6_1"
TEST_IP6 = "ff00::/8"


def cleanup():
    try:
        addresses = fgt.api.cmdb.firewall.multicast_address6.get()
        for addr in addresses:
            if getattr(addr, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.multicast_address6.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_multicast_address6():
    result = fgt.api.cmdb.firewall.multicast_address6.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_multicast_address6():
    result = fgt.api.cmdb.firewall.multicast_address6.post(
        name=TEST_NAME,
        ip6=TEST_IP6
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_multicast_address6():
    result = fgt.api.cmdb.firewall.multicast_address6.put(
        name=TEST_NAME,
        ip6="ff02::/16",
        comment="Updated multicast address6"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.multicast_address6.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.ip6 == "ff02::/16"

def test_get_specific_multicast_address6():
    result = fgt.api.cmdb.firewall.multicast_address6.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_multicast_address6():
    result = fgt.api.cmdb.firewall.multicast_address6.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    addresses = fgt.api.cmdb.firewall.multicast_address6.get()
    names = [getattr(a, "name", None) for a in addresses]
    assert TEST_NAME not in names, "Multicast address6 should have been deleted"

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
    test_get_multicast_address6()
    print("✓ test_get_multicast_address6 passed")
    test_post_multicast_address6()
    print("✓ test_post_multicast_address6 passed")
    test_put_multicast_address6()
    print("✓ test_put_multicast_address6 passed")
    test_get_specific_multicast_address6()
    print("✓ test_get_specific_multicast_address6 passed")
    test_delete_multicast_address6()
    print("✓ test_delete_multicast_address6 passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
