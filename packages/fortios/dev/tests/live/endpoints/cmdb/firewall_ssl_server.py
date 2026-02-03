import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_ssl_server_9999966"
TEST_IP = "192.168.100.100"
TEST_PORT = 443
TEST_SSL_MODE = "half"
TEST_MAPPED_PORT = 80


def cleanup():
    try:
        servers = fgt.api.cmdb.firewall.ssl_server.get()
        for server in servers:
            if getattr(server, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.ssl_server.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_ssl_server():
    """Test GET all SSL servers."""
    result = fgt.api.cmdb.firewall.ssl_server.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_ssl_server():
    result = fgt.api.cmdb.firewall.ssl_server.post(
        name=TEST_NAME,
        ip=TEST_IP,
        port=TEST_PORT,
        ssl_mode=TEST_SSL_MODE,
        mapped_port=TEST_MAPPED_PORT,
        add_header_x_forwarded_proto="enable",
        ssl_min_version="tls-1.2",
        ssl_max_version="tls-1.3"
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_ssl_server():
    updated_port = 8443
    result = fgt.api.cmdb.firewall.ssl_server.put(
        name=TEST_NAME,
        port=updated_port,
        ssl_mode="full"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ssl_server.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.port == updated_port
    assert verify.ssl_mode == "full"

def test_get_specific_ssl_server():
    result = fgt.api.cmdb.firewall.ssl_server.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_ssl_server():
    result = fgt.api.cmdb.firewall.ssl_server.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    servers = fgt.api.cmdb.firewall.ssl_server.get()
    names = [getattr(s, "name", None) for s in servers]
    assert TEST_NAME not in names, "SSL server should have been deleted"

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
    test_get_ssl_server()
    print("✓ test_get_ssl_server passed")
    test_post_ssl_server()
    print("✓ test_post_ssl_server passed")
    test_put_ssl_server()
    print("✓ test_put_ssl_server passed")
    test_get_specific_ssl_server()
    print("✓ test_get_specific_ssl_server passed")
    test_delete_ssl_server()
    print("✓ test_delete_ssl_server passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
