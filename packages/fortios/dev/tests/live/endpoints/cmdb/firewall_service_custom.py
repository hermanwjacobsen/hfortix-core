import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_service_custom1"


def cleanup():
    """Clean up test custom services."""
    try:
        services = fgt.api.cmdb.firewall.service.custom.get()
        for service in services:
            if service.name and str(service.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.service.custom.delete(name=service.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_custom_services():
    """Test: Get all custom services."""
    result = fgt.api.cmdb.firewall.service.custom.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_custom_service():
    """Test: Create custom service (TCP port 8080)."""
    result = fgt.api.cmdb.firewall.service.custom.post(
        name=TEST_NAME,
        protocol="TCP/UDP/UDP-Lite/SCTP",
        tcp_portrange="8080",
        comment="Test Custom Service"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_custom_service():
    """Test: Update custom service (change to port 9090)."""
    result = fgt.api.cmdb.firewall.service.custom.put(
        name=TEST_NAME,
        tcp_portrange="9090",
        comment="Updated Test Custom Service"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.service.custom.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated Test Custom Service"
    assert "9090" in verify.tcp_portrange


def test_get_specific_custom_service():
    """Test: Get specific custom service."""
    result = fgt.api.cmdb.firewall.service.custom.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_custom_service():
    """Test: Delete custom service."""
    result = fgt.api.cmdb.firewall.service.custom.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    services = fgt.api.cmdb.firewall.service.custom.get()
    service_names = [s.name for s in services]
    assert TEST_NAME not in service_names, "Service should have been deleted"


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
        
    test_get_custom_services()
    print("✓ test_get_custom_services passed")

    test_post_custom_service()
    print("✓ test_post_custom_service passed")

    test_put_custom_service()
    print("✓ test_put_custom_service passed")

    test_get_specific_custom_service()
    print("✓ test_get_specific_custom_service passed")

    test_delete_custom_service()
    print("✓ test_delete_custom_service passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
