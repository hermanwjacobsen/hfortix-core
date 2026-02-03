import argparse
import sys
from pathlib import Path
import pytest

# Run FTP proxy explicit tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# FTP Proxy Explicit Configuration Tests
# ============================================================================

# Store original configuration
original_config = None


def test_get_ftp_proxy_explicit():
    """Test GET /cmdb/ftp-proxy/explicit - Retrieve explicit FTP proxy configuration."""
    global original_config
    result = fgt.api.cmdb.ftp_proxy.explicit.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    original_config = result.dict  # Store original config for restoration
    print(f"Current FTP proxy explicit config: {result.dict}")


def test_update_ftp_proxy_explicit_enable():
    """Test PUT /cmdb/ftp-proxy/explicit - Enable explicit FTP proxy with configuration."""
    result = fgt.api.cmdb.ftp_proxy.explicit.put(
        status="enable",
        incoming_port="2121",
        incoming_ip="0.0.0.0",
        outgoing_ip="0.0.0.0",
        sec_default_action="deny",
        server_data_mode="passive",
        ssl="disable",
        vdom="test"
    )
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify the configuration was applied
    verify = fgt.api.cmdb.ftp_proxy.explicit.get(vdom="test")
    assert verify.dict.get("status") == "enable"
    assert verify.dict.get("incoming_port") == "2121"
    assert verify.dict.get("sec_default_action") == "deny"
    assert verify.dict.get("server_data_mode") == "passive"
    assert verify.dict.get("ssl") == "disable"
    print("FTP proxy explicit enabled with passive mode - VERIFIED")


def test_update_ftp_proxy_explicit_ssl():
    """Test PUT /cmdb/ftp-proxy/explicit - Enable FTPS proxy with SSL configuration."""
    result = fgt.api.cmdb.ftp_proxy.explicit.put(
        status="enable",
        incoming_port="2121",
        incoming_ip="0.0.0.0",
        outgoing_ip="0.0.0.0",
        ssl="enable",
        ssl_dh_bits="2048",
        ssl_algorithm="high",
        vdom="test"
    )
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify SSL configuration was applied
    verify = fgt.api.cmdb.ftp_proxy.explicit.get(vdom="test")
    assert verify.dict.get("ssl") == "enable"
    assert verify.dict.get("ssl_dh_bits") == "2048"
    assert verify.dict.get("ssl_algorithm") == "high"
    print("FTPS proxy enabled with SSL configuration - VERIFIED")


def test_update_ftp_proxy_explicit_client_mode():
    """Test PUT /cmdb/ftp-proxy/explicit - Configure with client data mode."""
    result = fgt.api.cmdb.ftp_proxy.explicit.put(
        status="enable",
        server_data_mode="client",
        sec_default_action="accept",
        vdom="test"
    )
    assert result is not None
    assert result.http_status_code == 200
    
    # Verify client mode and accept action were applied
    verify = fgt.api.cmdb.ftp_proxy.explicit.get(vdom="test")
    assert verify.dict.get("server_data_mode") == "client"
    assert verify.dict.get("sec_default_action") == "accept"
    print("FTP proxy configured with client data mode - VERIFIED")


def test_restore_ftp_proxy_explicit():
    """Test PUT /cmdb/ftp-proxy/explicit - Restore original FTP proxy configuration."""
    global original_config
    if original_config:
        # Restore original configuration
        result = fgt.api.cmdb.ftp_proxy.explicit.put(**original_config, vdom="test")
        assert result is not None
        assert result.http_status_code == 200
        print(f"FTP proxy explicit configuration restored to original state")
    else:
        print("No original config to restore")


def test_verify_ftp_proxy_explicit_restored():
    """Test GET /cmdb/ftp-proxy/explicit - Verify FTP proxy configuration is restored."""
    global original_config
    result = fgt.api.cmdb.ftp_proxy.explicit.get(vdom="test")
    assert result is not None
    assert result.http_status_code == 200
    if original_config:
        assert result.dict.get("status") == original_config.get("status")
        print(f"Verified FTP proxy is restored to: {result.dict.get('status')}")
    else:
        print(f"Current FTP proxy status: {result.dict.get('status')}")


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
    # ========================================================================
    # FTP Proxy Explicit Configuration Tests
    # ========================================================================
    
    print("Running FTP Proxy Explicit configuration tests...")
    
    test_get_ftp_proxy_explicit()
    print("✓ test_get_ftp_proxy_explicit")
    
    test_update_ftp_proxy_explicit_enable()
    print("✓ test_update_ftp_proxy_explicit_enable")
    
    test_update_ftp_proxy_explicit_ssl()
    print("✓ test_update_ftp_proxy_explicit_ssl")
    
    test_update_ftp_proxy_explicit_client_mode()
    print("✓ test_update_ftp_proxy_explicit_client_mode")
    
    test_restore_ftp_proxy_explicit()
    print("✓ test_restore_ftp_proxy_explicit")
    
    test_verify_ftp_proxy_explicit_restored()
    print("✓ test_verify_ftp_proxy_explicit_restored")
    
    print("\n✓ All FTP Proxy Explicit tests completed!")
    print("\nSummary:")
    print("- GET: 2 tests (retrieve config, verify restored)")
    print("- PUT: 4 tests (enable, SSL config, client mode, restore)")
    print("- Total: 6 test functions covering FTP proxy explicit configuration")
    print("\nConfiguration tested:")
    print("  - Enable/disable FTP proxy")
    print("  - Incoming/outgoing IP and port configuration")
    print("  - Security default action (accept/deny)")
    print("  - Server data mode (passive/client)")
    print("  - SSL/FTPS configuration")
    print("  - SSL DH bits and algorithm settings")
    print("  - Configuration backup and restore")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
