import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_SERVER_NAME = "test_icap_server1"


def cleanup():
    """Clean up test ICAP servers."""
    try:
        servers = fgt.api.cmdb.icap.server.get(vdom="test")
        for server in servers:
            if server.name and str(server.name).startswith("test"):
                try:
                    fgt.api.cmdb.icap.server.delete(name=server.name, vdom="test")
                except Exception:
                    pass
    except Exception:
        pass


def test_get_icap_servers():
    """Test: Get all ICAP servers."""
    result = fgt.api.cmdb.icap.server.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


def test_post_icap_server():
    """Test: Create ICAP server."""
    result = fgt.api.cmdb.icap.server.post(
        name=TEST_SERVER_NAME,
        addr_type="ip4",
        ip_address="192.168.1.100",
        port=1344,
        max_connections=100,
        secure="disable",
        healthcheck="enable",
        healthcheck_service="req",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_icap_server():
    """Test: Update ICAP server."""
    result = fgt.api.cmdb.icap.server.put(
        name=TEST_SERVER_NAME,
        port=1345,
        max_connections=200,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.icap.server.get(name=TEST_SERVER_NAME, vdom="test")
    assert verify is not None
    assert verify.port == 1345
    assert verify.max_connections == 200


def test_get_specific_icap_server():
    """Test: Get specific ICAP server."""
    result = fgt.api.cmdb.icap.server.get(name=TEST_SERVER_NAME, vdom="test")
    assert result is not None
    assert result.name == TEST_SERVER_NAME


def test_delete_icap_server():
    """Test: Delete ICAP server."""
    result = fgt.api.cmdb.icap.server.delete(name=TEST_SERVER_NAME, vdom="test")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    servers = fgt.api.cmdb.icap.server.get(vdom="test")
    server_names = [s.name for s in servers]
    assert TEST_SERVER_NAME not in server_names, "ICAP server should have been deleted"


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
        
    test_get_icap_servers()
    print("✓ test_get_icap_servers passed")

    test_post_icap_server()
    print("✓ test_post_icap_server passed")

    test_put_icap_server()
    print("✓ test_put_icap_server passed")

    test_get_specific_icap_server()
    print("✓ test_get_specific_icap_server passed")

    test_delete_icap_server()
    print("✓ test_delete_icap_server passed")

    cleanup()
    print("✓ Post-Cleanup passed")
    
    print("\n✓ All ICAP server tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
