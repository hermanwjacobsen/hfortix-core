import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def test_get_ssh_setting():
    """Test: Get SSH proxy settings."""
    result = fgt.api.cmdb.firewall.ssh.setting.get()
    assert result is not None
    assert result.http_status_code == 200


def test_put_ssh_setting():
    """Test: Update SSH proxy settings - toggle host trusted checking."""
    # Get current settings first
    current = fgt.api.cmdb.firewall.ssh.setting.get()
    original_value = current.host_trusted_checking
    
    # Toggle the value
    new_value = "disable" if original_value == "enable" else "enable"
    
    result = fgt.api.cmdb.firewall.ssh.setting.put(
        host_trusted_checking=new_value,
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.ssh.setting.get()
    assert verify is not None
    assert verify.host_trusted_checking == new_value


def test_revert_ssh_setting():
    """Test: Revert SSH settings to original value."""
    # Get current and toggle back
    current = fgt.api.cmdb.firewall.ssh.setting.get()
    original_value = current.host_trusted_checking
    new_value = "disable" if original_value == "enable" else "enable"
    
    result = fgt.api.cmdb.firewall.ssh.setting.put(
        host_trusted_checking=new_value,
    )
    assert result is not None
    assert result.http_status == "success"
    
    verify = fgt.api.cmdb.firewall.ssh.setting.get()
    assert verify.host_trusted_checking == new_value


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
    test_get_ssh_setting()
    print("✓ test_get_ssh_setting passed")

    test_put_ssh_setting()
    print("✓ test_put_ssh_setting passed")

    test_revert_ssh_setting()
    print("✓ test_revert_ssh_setting passed")

    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
