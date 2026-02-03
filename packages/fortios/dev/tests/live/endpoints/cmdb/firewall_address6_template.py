import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_addr6_template1"


def cleanup():
    """Clean up test IPv6 address templates."""
    try:
        templates = fgt.api.cmdb.firewall.address6_template.get()
        for template in templates:
            if template.name and str(template.name).startswith("test"):
                try:
                    fgt.api.cmdb.firewall.address6_template.delete(name=template.name)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_address6_templates():
    """Test: Get all IPv6 address templates."""
    result = fgt.api.cmdb.firewall.address6_template.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_address6_template():
    """Test: Create IPv6 address template."""
    result = fgt.api.cmdb.firewall.address6_template.post(
        name=TEST_NAME,
        ip6="2001:db8::/32",
        subnet_segment_count=1,
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_address6_template():
    """Test: Update IPv6 address template."""
    result = fgt.api.cmdb.firewall.address6_template.put(
        name=TEST_NAME,
        subnet_segment_count=2,
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.address6_template.get(name=TEST_NAME)
    assert verify is not None
    assert verify.subnet_segment_count == 2


def test_get_specific_address6_template():
    """Test: Get specific IPv6 address template."""
    result = fgt.api.cmdb.firewall.address6_template.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME


def test_delete_address6_template():
    """Test: Delete IPv6 address template."""
    result = fgt.api.cmdb.firewall.address6_template.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    templates = fgt.api.cmdb.firewall.address6_template.get()
    template_names = [t.name for t in templates]
    assert TEST_NAME not in template_names, "IPv6 address template should have been deleted"


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
        
    test_get_address6_templates()
    print("✓ test_get_address6_templates passed")

    test_post_address6_template()
    print("✓ test_post_address6_template passed")

    test_put_address6_template()
    print("✓ test_put_address6_template passed")

    test_get_specific_address6_template()
    print("✓ test_get_specific_address6_template passed")

    test_delete_address6_template()
    print("✓ test_delete_address6_template passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
