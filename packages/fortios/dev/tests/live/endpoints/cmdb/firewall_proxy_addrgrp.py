import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_proxy_addrgrp_9999975"
TEST_TYPE = "dst"
TEST_MEMBER1 = "test_proxy_addr_member1_9999975"
TEST_MEMBER2 = "test_proxy_addr_member2_9999975"
TEST_COMMENT = "Test proxy address group"


def cleanup():
    try:
        # Cleanup group first
        groups = fgt.api.cmdb.firewall.proxy_addrgrp.get()
        for group in groups:
            if getattr(group, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.proxy_addrgrp.delete(name=TEST_NAME)
                break
        
        # Cleanup member addresses
        addresses = fgt.api.cmdb.firewall.proxy_address.get()
        for addr in addresses:
            addr_name = getattr(addr, "name", None)
            if addr_name in [TEST_MEMBER1, TEST_MEMBER2]:
                fgt.api.cmdb.firewall.proxy_address.delete(name=addr_name)
    except Exception:
        pass


@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    """Setup and teardown for all tests."""
    cleanup()  # Pre-cleanup
    yield
    cleanup()  # Post-cleanup


def test_get_proxy_addrgrp():
    result = fgt.api.cmdb.firewall.proxy_addrgrp.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_proxy_addrgrp():
    """Create proxy address group with member addresses."""
    # Create member addresses first
    try:
        fgt.api.cmdb.firewall.proxy_address.post(
            name=TEST_MEMBER1,
            type="host-regex",
            host_regex=".*\\.example1\\.com"
        )
    except Exception:
        pass  # May already exist
    
    try:
        fgt.api.cmdb.firewall.proxy_address.post(
            name=TEST_MEMBER2,
            type="host-regex",
            host_regex=".*\\.example2\\.com"
        )
    except Exception:
        pass  # May already exist
    
    # Create group
    result = fgt.api.cmdb.firewall.proxy_addrgrp.post(
        name=TEST_NAME,
        type=TEST_TYPE,
        member=[{"name": TEST_MEMBER1}, {"name": TEST_MEMBER2}],
        comment=TEST_COMMENT
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_proxy_addrgrp():
    updated_comment = "Updated proxy address group"
    result = fgt.api.cmdb.firewall.proxy_addrgrp.put(
        name=TEST_NAME,
        type=TEST_TYPE,
        member=[{"name": TEST_MEMBER1}],
        comment=updated_comment
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.proxy_addrgrp.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.name == TEST_NAME
    assert verify.comment == updated_comment

def test_get_specific_proxy_addrgrp():
    result = fgt.api.cmdb.firewall.proxy_addrgrp.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_proxy_addrgrp():
    """Delete the proxy address group."""
    result = fgt.api.cmdb.firewall.proxy_addrgrp.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    groups = fgt.api.cmdb.firewall.proxy_addrgrp.get()
    names = [getattr(g, "name", None) for g in groups]
    assert TEST_NAME not in names, "Proxy address group should have been deleted"
    
    # Clean up member addresses after deleting group
    try:
        fgt.api.cmdb.firewall.proxy_address.delete(name=TEST_MEMBER1)
    except Exception:
        pass
    try:
        fgt.api.cmdb.firewall.proxy_address.delete(name=TEST_MEMBER2)
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
    test_get_proxy_addrgrp()
    print("✓ test_get_proxy_addrgrp passed")
    test_post_proxy_addrgrp()
    print("✓ test_post_proxy_addrgrp passed")
    test_put_proxy_addrgrp()
    print("✓ test_put_proxy_addrgrp passed")
    test_get_specific_proxy_addrgrp()
    print("✓ test_get_specific_proxy_addrgrp passed")
    test_delete_proxy_addrgrp()
    print("✓ test_delete_proxy_addrgrp passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
