import argparse
import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

TEST_NAME = "test_ssl_ssh_profile_9999965"


def cleanup():
    try:
        profiles = fgt.api.cmdb.firewall.ssl_ssh_profile.get()
        for profile in profiles:
            if getattr(profile, "name", None) == TEST_NAME:
                fgt.api.cmdb.firewall.ssl_ssh_profile.delete(name=TEST_NAME)
                break
    except Exception:
        pass

def test_get_ssl_ssh_profile():
    """Test GET all SSL/SSH profiles."""
    result = fgt.api.cmdb.firewall.ssl_ssh_profile.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_ssl_ssh_profile():
    result = fgt.api.cmdb.firewall.ssl_ssh_profile.post(
        name=TEST_NAME,
        comment="Test SSL/SSH inspection profile",
        server_cert_mode="re-sign",
        ssl_anomaly_log="enable",
        ssl_exemption_log="enable",
        https={
            "ports": [443],
            "status": "deep-inspection"
        },
        ftps={
            "ports": [990],
            "status": "deep-inspection"
        },
        imaps={
            "ports": [993],
            "status": "deep-inspection"
        },
        pop3s={
            "ports": [995],
            "status": "deep-inspection"
        },
        smtps={
            "ports": [465],
            "status": "deep-inspection"
        },
        ssh={
            "ports": [22],
            "status": "deep-inspection"
        }
    )
    assert result is not None
    assert result.http_status == "success"

def test_put_ssl_ssh_profile():
    updated_comment = "Updated SSL/SSH inspection profile"
    result = fgt.api.cmdb.firewall.ssl_ssh_profile.put(
        name=TEST_NAME,
        comment=updated_comment,
        ssl_negotiation_log="enable",
        ssl_handshake_log="enable",
        supported_alpn="http2"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ssl_ssh_profile.get(name=TEST_NAME)
    assert verify is not None
    assert verify.http_status_code == 200
    assert verify.comment == updated_comment
    assert verify.supported_alpn == "http2"

def test_get_specific_ssl_ssh_profile():
    result = fgt.api.cmdb.firewall.ssl_ssh_profile.get(name=TEST_NAME)
    assert result is not None
    assert result.name == TEST_NAME

def test_delete_ssl_ssh_profile():
    result = fgt.api.cmdb.firewall.ssl_ssh_profile.delete(name=TEST_NAME)
    assert result is not None
    assert result.http_status == "success"
    # Verify deletion
    profiles = fgt.api.cmdb.firewall.ssl_ssh_profile.get()
    names = [getattr(p, "name", None) for p in profiles]
    assert TEST_NAME not in names, "SSL/SSH profile should have been deleted"

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
    test_get_ssl_ssh_profile()
    print("✓ test_get_ssl_ssh_profile passed")
    test_post_ssl_ssh_profile()
    print("✓ test_post_ssl_ssh_profile passed")
    test_put_ssl_ssh_profile()
    print("✓ test_put_ssl_ssh_profile passed")
    test_get_specific_ssl_ssh_profile()
    print("✓ test_get_specific_ssl_ssh_profile passed")
    test_delete_ssl_ssh_profile()
    print("✓ test_delete_ssl_ssh_profile passed")
    cleanup()
    print("✓ post-Cleanup passed")
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
