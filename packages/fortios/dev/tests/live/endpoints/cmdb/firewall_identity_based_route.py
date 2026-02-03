import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_idroute1"


def cleanup():
    """Clean up test identity-based routes."""
    try:
        routes = fgt.api.cmdb.firewall.identity_based_route.get()
        for route in routes:
            if route.name and str(route.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.identity_based_route.delete(name=route.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_identity_based_routes():
    """Test: Get all identity-based routes."""
    result = fgt.api.cmdb.firewall.identity_based_route.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_identity_based_route():
    """Test: Create identity-based route."""
    result = fgt.api.cmdb.firewall.identity_based_route.post(
        name=TEST_NAME,
        comments="Test identity-based route",
        rule=[],
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_identity_based_route():
    """Test: Update identity-based route."""
    result = fgt.api.cmdb.firewall.identity_based_route.put(
        name=TEST_NAME,
        comments="Updated identity-based route",
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.identity_based_route.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comments == "Updated identity-based route"


def test_get_specific_identity_based_route():
    """Test: Get specific identity-based route."""
    result = fgt.api.cmdb.firewall.identity_based_route.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_identity_based_route():
    """Test: Delete identity-based route."""
    result = fgt.api.cmdb.firewall.identity_based_route.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    routes = fgt.api.cmdb.firewall.identity_based_route.get()
    route_names = [r.name for r in routes]
    assert TEST_NAME not in route_names, "Identity-based route should have been deleted"


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
        
    test_get_identity_based_routes()
    print("✓ test_get_identity_based_routes passed")

    test_post_identity_based_route()
    print("✓ test_post_identity_based_route passed")

    test_put_identity_based_route()
    print("✓ test_put_identity_based_route passed")

    test_get_specific_identity_based_route()
    print("✓ test_get_specific_identity_based_route passed")

    test_delete_identity_based_route()
    print("✓ test_delete_identity_based_route passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
