import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_CUSTOM_NAME = "test_ips_custom1"


def cleanup():
    """Clean up test IPS custom signatures."""
    try:
        customs = fgt.api.cmdb.ips.custom.get(vdom="test")
        for custom in customs:
            if custom.tag and str(custom.tag).startswith("test"):
                try:
                    fgt.api.cmdb.ips.custom.delete(tag=custom.tag, vdom="test")
                except Exception:
                    pass
    except Exception:
        pass


def test_get_ips_custom_signatures():
    """Test: Get all IPS custom signatures."""
    result = fgt.api.cmdb.ips.custom.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


def test_post_ips_custom_signature():
    """Test: Create IPS custom signature."""
    result = fgt.api.cmdb.ips.custom.post(
        tag=TEST_CUSTOM_NAME,
        signature="F-SBID( --name \"TEST.Custom.Rule\"; --pattern \"test\"; --service HTTP; )",
        comment="Test custom IPS signature",
        status="enable",
        log="enable",
        log_packet="enable",
        action="block",
        severity="critical",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_ips_custom_signature():
    """Test: Update IPS custom signature."""
    result = fgt.api.cmdb.ips.custom.put(
        tag=TEST_CUSTOM_NAME,
        comment="Updated custom IPS signature",
        action="pass",
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.custom.get(tag=TEST_CUSTOM_NAME, vdom="test")
    assert verify is not None
    assert verify.comment == "Updated custom IPS signature"
    assert verify.action == "pass"


def test_get_specific_ips_custom_signature():
    """Test: Get specific IPS custom signature."""
    result = fgt.api.cmdb.ips.custom.get(tag=TEST_CUSTOM_NAME, vdom="test")
    assert result is not None
    assert result.tag == TEST_CUSTOM_NAME


def test_delete_ips_custom_signature():
    """Test: Delete IPS custom signature."""
    result = fgt.api.cmdb.ips.custom.delete(tag=TEST_CUSTOM_NAME, vdom="test")
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    customs = fgt.api.cmdb.ips.custom.get(vdom="test")
    custom_tags = [c.tag for c in customs]
    assert TEST_CUSTOM_NAME not in custom_tags, "IPS custom signature should have been deleted"


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
        
    test_get_ips_custom_signatures()
    print("✓ test_get_ips_custom_signatures passed")

    test_post_ips_custom_signature()
    print("✓ test_post_ips_custom_signature passed")

    test_put_ips_custom_signature()
    print("✓ test_put_ips_custom_signature passed")

    test_get_specific_ips_custom_signature()
    print("✓ test_get_specific_ips_custom_signature passed")

    test_delete_ips_custom_signature()
    print("✓ test_delete_ips_custom_signature passed")

    cleanup()
    print("✓ Post-Cleanup passed")
    
    print("\n✓ All IPS custom signature tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
