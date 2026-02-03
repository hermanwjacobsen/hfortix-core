import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_service_category1"


def cleanup():
    """Clean up test service categories."""
    try:
        categories = fgt.api.cmdb.firewall.service.category.get()
        for category in categories:
            if category.name and str(category.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.service.category.delete(name=category.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_service_categories():
    """Test: Get all service categories."""
    result = fgt.api.cmdb.firewall.service.category.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_service_category():
    """Test: Create service category."""
    result = fgt.api.cmdb.firewall.service.category.post(
        name=TEST_NAME,
        comment="Test Service Category"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_service_category():
    """Test: Update service category."""
    result = fgt.api.cmdb.firewall.service.category.put(
        name=TEST_NAME,
        comment="Updated Test Service Category"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.service.category.get(name=TEST_NAME)
    assert verify is not None
    assert verify.comment == "Updated Test Service Category"


def test_get_specific_service_category():
    """Test: Get specific service category."""
    result = fgt.api.cmdb.firewall.service.category.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_service_category():
    """Test: Delete service category."""
    result = fgt.api.cmdb.firewall.service.category.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    categories = fgt.api.cmdb.firewall.service.category.get()
    category_names = [c.name for c in categories]
    assert TEST_NAME not in category_names, "Category should have been deleted"


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
        
    test_get_service_categories()
    print("✓ test_get_service_categories passed")

    test_post_service_category()
    print("✓ test_post_service_category passed")

    test_put_service_category()
    print("✓ test_put_service_category passed")

    test_get_specific_service_category()
    print("✓ test_get_specific_service_category passed")

    test_delete_service_category()
    print("✓ test_delete_service_category passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
