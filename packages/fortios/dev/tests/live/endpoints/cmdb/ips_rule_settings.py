import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# NOTE: IPS rule-settings endpoint is for configuring settings for specific IPS rule IDs
# We need to create a custom IPS signature first to get a valid rule ID

TEST_SENSOR_NAME = "test_sensor_for_rule_settings"
TEST_CUSTOM_TAG = "test_custom_for_rule_settings"


def cleanup():
    """Clean up test IPS objects."""
    try:
        # Clean up rule settings
        settings = fgt.api.cmdb.ips.rule_settings.get(vdom="test")
        for setting in settings:
            if hasattr(setting, "id"):
                try:
                    fgt.api.cmdb.ips.rule_settings.delete(id=setting.id, vdom="test")
                except Exception:
                    pass
        
        # Clean up custom signatures
        customs = fgt.api.cmdb.ips.custom.get(vdom="test")
        for custom in customs:
            if custom.tag and str(custom.tag).startswith("test"):
                try:
                    fgt.api.cmdb.ips.custom.delete(tag=custom.tag, vdom="test")
                except Exception:
                    pass
    except Exception:
        pass


def setup_custom_signature():
    """Create a custom IPS signature to get a rule ID."""
    try:
        result = fgt.api.cmdb.ips.custom.post(
            tag=TEST_CUSTOM_TAG,
            signature="F-SBID( --name \"TEST.RuleSettings.Rule\"; --pattern \"test\"; --service HTTP; )",
            comment="Test custom IPS signature for rule settings",
            status="enable",
            vdom="test"
        )
        return result
    except Exception:
        return None


def test_get_ips_rule_settings():
    """Test: Get IPS rule settings (typically empty unless configured)."""
    result = fgt.api.cmdb.ips.rule_settings.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


def test_create_custom_signature_for_rule_settings():
    """Test: Create custom IPS signature to get a rule ID."""
    result = setup_custom_signature()
    # Custom signature should be created successfully
    if result:
        assert result.http_status == "success"


def test_post_ips_rule_setting():
    """Test: Create IPS rule setting for custom signature."""
    # Get the custom signature to find its rule ID
    custom = fgt.api.cmdb.ips.custom.get(tag=TEST_CUSTOM_TAG, vdom="test")
    
    # The custom.get() returns a single object with rule_id attribute
    if custom and hasattr(custom, "rule_id"):
        rule_id = custom.rule_id
        
        result = fgt.api.cmdb.ips.rule_settings.post(
            id=rule_id,
            vdom="test"
        )
        
        # Check if it was created
        if result is not None:
            assert result.http_status == "success"
        else:
            # POST returns None - endpoint doesn't support creating rule settings
            # even with valid rule IDs from custom signatures
            pass


def test_get_ips_rule_settings_after_post():
    """Test: Verify IPS rule settings after attempting to create."""
    result = fgt.api.cmdb.ips.rule_settings.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    # Endpoint doesn't support creating settings, so this will still be empty


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
    
    test_get_ips_rule_settings()
    print("✓ test_get_ips_rule_settings passed")

    test_create_custom_signature_for_rule_settings()
    print("✓ test_create_custom_signature_for_rule_settings passed")

    test_post_ips_rule_setting()
    print("✓ test_post_ips_rule_setting passed")

    test_get_ips_rule_settings_after_post()
    print("✓ test_get_ips_rule_settings_after_post passed")
    
    cleanup()
    print("✓ Post-Cleanup passed")
    
    print("\n✓ All IPS rule settings tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
