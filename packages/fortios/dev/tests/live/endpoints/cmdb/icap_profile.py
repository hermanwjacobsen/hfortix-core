import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_PROFILE_NAME = "test_icap_profile1"
TEST_SERVER_NAME = "test_icap_srv2"


def cleanup():
    """Clean up test ICAP profiles and servers."""
    try:
        # Clean up profiles first
        profiles = fgt.api.cmdb.icap.profile.get(vdom="test")
        for profile in profiles:
            if profile.name and str(profile.name).startswith("test"):
                try:
                    fgt.api.cmdb.icap.profile.delete(name=profile.name, vdom="test")
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


def test_create_icap_server_for_profile():
    """Test: Create ICAP server to use in profile."""
    result = fgt.api.cmdb.icap.server.post(
        name=TEST_SERVER_NAME,
        addr_type="ip4",
        ip_address="192.168.1.102",
        port=1344,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_icap_profiles():
    """Test: Get all ICAP profiles."""
    result = fgt.api.cmdb.icap.profile.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


def test_post_icap_profile():
    """Test: Create ICAP profile."""
    result = fgt.api.cmdb.icap.profile.post(
        name=TEST_PROFILE_NAME,
        request="enable",
        response="enable",
        request_server=TEST_SERVER_NAME,
        response_server=TEST_SERVER_NAME,
        request_path="/reqmod",
        response_path="/respmod",
        request_failure="bypass",
        response_failure="bypass",
        preview="enable",
        preview_data_length=1024,
        timeout=60,
        comment="Test ICAP profile",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_icap_profile():
    """Test: Update ICAP profile."""
    result = fgt.api.cmdb.icap.profile.put(
        name=TEST_PROFILE_NAME,
        timeout=120,
        preview_data_length=2048,
        comment="Updated ICAP profile",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.icap.profile.get(name=TEST_PROFILE_NAME, vdom="test")
    assert verify is not None
    assert verify.timeout == 120
    assert verify.preview_data_length == 2048
    assert verify.comment == "Updated ICAP profile"


def test_get_specific_icap_profile():
    """Test: Get specific ICAP profile."""
    result = fgt.api.cmdb.icap.profile.get(name=TEST_PROFILE_NAME, vdom="test")
    assert result is not None
    assert result.name == TEST_PROFILE_NAME


def test_delete_icap_profile():
    """Test: Delete ICAP profile."""
    result = fgt.api.cmdb.icap.profile.delete(name=TEST_PROFILE_NAME, vdom="test")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    profiles = fgt.api.cmdb.icap.profile.get(vdom="test")
    profile_names = [p.name for p in profiles]
    assert TEST_PROFILE_NAME not in profile_names, "ICAP profile should have been deleted"


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
    
    test_create_icap_server_for_profile()
    print("✓ test_create_icap_server_for_profile passed")
        
    test_get_icap_profiles()
    print("✓ test_get_icap_profiles passed")

    test_post_icap_profile()
    print("✓ test_post_icap_profile passed")

    test_put_icap_profile()
    print("✓ test_put_icap_profile passed")

    test_get_specific_icap_profile()
    print("✓ test_get_specific_icap_profile passed")

    test_delete_icap_profile()
    print("✓ test_delete_icap_profile passed")
    
    test_cleanup_icap_server()
    print("✓ test_cleanup_icap_server passed")

    cleanup()
    print("✓ Post-Cleanup passed")
    
    print("\n✓ All ICAP profile tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
