import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_SERVER_GROUP_NAME = "test_icap_group1"
TEST_SERVER_NAME = "test_icap_srv1"


def cleanup():
    """Clean up test ICAP server groups and servers."""
    try:
        # Clean up server groups first
        groups = fgt.api.cmdb.icap.server_group.get(vdom="test")
        for group in groups:
            if group.name and str(group.name).startswith("test"):
                try:
                    fgt.api.cmdb.icap.server_group.delete(name=group.name, vdom="test")
                except Exception:
                    pass
        
        # Clean up servers
        servers = fgt.api.cmdb.icap.server.get(vdom="test")
        for server in servers:
            if server.name and str(server.name).startswith("test"):
                try:
                    fgt.api.cmdb.icap.server.delete(name=server.name, vdom="test")
                except Exception:
                    pass
    except Exception:
        pass


def test_create_icap_server_for_group():
    """Test: Create ICAP server to use in server group."""
    result = fgt.api.cmdb.icap.server.post(
        name=TEST_SERVER_NAME,
        addr_type="ip4",
        ip_address="192.168.1.101",
        port=1344,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_icap_server_groups():
    """Test: Get all ICAP server groups."""
    result = fgt.api.cmdb.icap.server_group.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


def test_post_icap_server_group():
    """Test: Create ICAP server group."""
    result = fgt.api.cmdb.icap.server_group.post(
        name=TEST_SERVER_GROUP_NAME,
        server_list=TEST_SERVER_NAME,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_icap_server_group():
    """Test: Update ICAP server group."""
    result = fgt.api.cmdb.icap.server_group.put(
        name=TEST_SERVER_GROUP_NAME,
        server_list=TEST_SERVER_NAME,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.icap.server_group.get(name=TEST_SERVER_GROUP_NAME, vdom="test")
    assert verify is not None
    assert verify.name == TEST_SERVER_GROUP_NAME


def test_get_specific_icap_server_group():
    """Test: Get specific ICAP server group."""
    result = fgt.api.cmdb.icap.server_group.get(name=TEST_SERVER_GROUP_NAME, vdom="test")
    assert result is not None
    assert result.name == TEST_SERVER_GROUP_NAME


def test_delete_icap_server_group():
    """Test: Delete ICAP server group."""
    result = fgt.api.cmdb.icap.server_group.delete(name=TEST_SERVER_GROUP_NAME, vdom="test")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    groups = fgt.api.cmdb.icap.server_group.get(vdom="test")
    group_names = [g.name for g in groups]
    assert TEST_SERVER_GROUP_NAME not in group_names, "ICAP server group should have been deleted"


def test_cleanup_icap_server():
    """Test: Clean up test ICAP server."""
    result = fgt.api.cmdb.icap.server.delete(name=TEST_SERVER_NAME, vdom="test")
    assert result is not None
    assert result.http_status == "success"


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
    
    test_create_icap_server_for_group()
    print("✓ test_create_icap_server_for_group passed")
        
    test_get_icap_server_groups()
    print("✓ test_get_icap_server_groups passed")

    test_post_icap_server_group()
    print("✓ test_post_icap_server_group passed")

    test_put_icap_server_group()
    print("✓ test_put_icap_server_group passed")

    test_get_specific_icap_server_group()
    print("✓ test_get_specific_icap_server_group passed")

    test_delete_icap_server_group()
    print("✓ test_delete_icap_server_group passed")
    
    test_cleanup_icap_server()
    print("✓ test_cleanup_icap_server passed")

    cleanup()
    print("✓ Post-Cleanup passed")
    
    print("\n✓ All ICAP server group tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
