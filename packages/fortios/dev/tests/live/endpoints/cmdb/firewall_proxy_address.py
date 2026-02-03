import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_proxy_addr_9999979"
TEST_TYPE = "host-regex"
TEST_HOST_REGEX = ".*\\.example\\.com"
TEST_PATH = "/api/.*"
TEST_COMMENT = "Test proxy address"


def cleanup():
    try:
        addresses = fgt.api.cmdb.firewall.proxy_address.get()
        for address in addresses:
            if getattr(address, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.proxy_address.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_proxy_address():
    result = fgt.api.cmdb.firewall.proxy_address.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_proxy_address():
    result = fgt.api.cmdb.firewall.proxy_address.post(
        name=TEST_NAME,
        type=TEST_TYPE,
        host_regex=TEST_HOST_REGEX,
        path=TEST_PATH,
        referrer="enable",
        case_sensitivity="enable",
        comment=TEST_COMMENT
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_proxy_address():
    updated_comment = "Updated proxy address"
    updated_path = "/api/v2/.*"
    result = fgt.api.cmdb.firewall.proxy_address.put(
        name=TEST_NAME,
        type=TEST_TYPE,
        host_regex=TEST_HOST_REGEX,
        path=updated_path,
        referrer="disable",
        case_sensitivity="disable",
        comment=updated_comment
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.proxy_address.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == TEST_NAME
    assert verify.comment == updated_comment
    assert verify.referrer == "disable"
    assert verify.case_sensitivity == "disable"

def test_get_specific_proxy_address():
    result = fgt.api.cmdb.firewall.proxy_address.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_proxy_address():
    result = fgt.api.cmdb.firewall.proxy_address.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    addresses = fgt.api.cmdb.firewall.proxy_address.get()
    names = [getattr(a, "name", None) for a in addresses]
    assert TEST_NAME not in names, "Proxy address should have been deleted"

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
    test_get_proxy_address()
    print("✓ test_get_proxy_address passed")
    test_post_proxy_address()
    print("✓ test_post_proxy_address passed")
    test_put_proxy_address()
    print("✓ test_put_proxy_address passed")
    test_get_specific_proxy_address()
    print("✓ test_get_specific_proxy_address passed")
    test_delete_proxy_address()
    print("✓ test_delete_proxy_address passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
