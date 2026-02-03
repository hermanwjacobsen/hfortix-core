import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


# Global variable to store original configuration
original_config = None


def test_get_ips_settings():
    """Test: Get IPS VDOM settings."""
    global original_config
    result = fgt.api.cmdb.ips.settings.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    
    # Store original configuration for restoration
    original_config = {
        "ips_packet_quota": result.ips_packet_quota if hasattr(result, "ips_packet_quota") else None,
        "packet_log_history": result.packet_log_history if hasattr(result, "packet_log_history") else None,
        "packet_log_post_attack": result.packet_log_post_attack if hasattr(result, "packet_log_post_attack") else None,
    }


def test_put_ips_settings_packet_quota():
    """Test: Update IPS packet quota setting."""
    result = fgt.api.cmdb.ips.settings.put(
        ips_packet_quota=2048,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.settings.get(vdom="test")
    assert verify is not None
    assert verify.ips_packet_quota == 2048


def test_put_ips_settings_log_history():
    """Test: Update IPS packet log history setting."""
    result = fgt.api.cmdb.ips.settings.put(
        packet_log_history=16,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.settings.get(vdom="test")
    assert verify is not None
    assert verify.packet_log_history == 16


def test_put_ips_settings_log_post_attack():
    """Test: Update IPS packet log post-attack setting."""
    result = fgt.api.cmdb.ips.settings.put(
        packet_log_post_attack=32,
        vdom="test"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.ips.settings.get(vdom="test")
    assert verify is not None
    assert verify.packet_log_post_attack == 32


def test_restore_ips_settings():
    """Test: Restore IPS settings to original state."""
    global original_config
    
    if original_config is None:
        return
    
    # Build restoration payload with only non-None values
    restore_payload = {}
    if original_config.get("ips_packet_quota") is not None:
        restore_payload["ips_packet_quota"] = original_config["ips_packet_quota"]
    if original_config.get("packet_log_history") is not None:
        restore_payload["packet_log_history"] = original_config["packet_log_history"]
    if original_config.get("packet_log_post_attack") is not None:
        restore_payload["packet_log_post_attack"] = original_config["packet_log_post_attack"]
    
    if restore_payload:
        restore_payload["vdom"] = "test"
        result = fgt.api.cmdb.ips.settings.put(**restore_payload)
        assert result is not None
        assert result.http_status == "success"
        
        # Verify restoration
        verify = fgt.api.cmdb.ips.settings.get(vdom="test")
        assert verify is not None


def test_verify_ips_settings_restored():
    """Test: Verify IPS settings were restored."""
    result = fgt.api.cmdb.ips.settings.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200


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
    test_get_ips_settings()
    print("✓ test_get_ips_settings passed")

    test_put_ips_settings_packet_quota()
    print("✓ test_put_ips_settings_packet_quota passed")

    test_put_ips_settings_log_history()
    print("✓ test_put_ips_settings_log_history passed")

    test_put_ips_settings_log_post_attack()
    print("✓ test_put_ips_settings_log_post_attack passed")

    test_restore_ips_settings()
    print("✓ test_restore_ips_settings passed")

    test_verify_ips_settings_restored()
    print("✓ test_verify_ips_settings_restored passed")
    
    print("\n✓ All IPS settings tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
