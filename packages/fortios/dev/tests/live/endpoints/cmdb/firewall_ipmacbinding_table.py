import argparse
import sys
from pathlib import Path

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


TEST_NAME = "test_ipmac_binding1"

def cleanup():
    """Clean up test IP-MAC bindings."""
    try:
        bindings = fgt.api.cmdb.firewall.ipmacbinding.table.get()
        for binding in bindings:
            if binding.name and str(binding.name).startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.ipmacbinding.table.delete(seq_num=binding.seq_num)
                except Exception:
                    pass
    except Exception:
        pass


def test_get_ipmacbinding_table():
    """Test: Get all IP-MAC bindings."""
    result = fgt.api.cmdb.firewall.ipmacbinding.table.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_ipmacbinding_table():
    """Test: Create IP-MAC binding."""
    result = fgt.api.cmdb.firewall.ipmacbinding.table.post(
        name=TEST_NAME,
        ip="192.168.100.10",
        mac="00:11:22:33:44:55",
        status="enable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_ipmacbinding_table():
    """Test: Update IP-MAC binding."""
    # First get the seq_num of our test entry
    bindings = fgt.api.cmdb.firewall.ipmacbinding.table.get()
    test_binding = None
    for binding in bindings:
        if binding.name == TEST_NAME:
            test_binding = binding
            break
    
    assert test_binding is not None, f"Test binding '{TEST_NAME}' not found"
    
    result = fgt.api.cmdb.firewall.ipmacbinding.table.put(
        seq_num=test_binding.seq_num,
        status="disable"
    )
    assert result is not None
    assert result.http_status == "success"
    
    # Verify the update
    verify = fgt.api.cmdb.firewall.ipmacbinding.table.get(seq_num=test_binding.seq_num)
    assert verify.status == "disable"


def test_get_specific_ipmacbinding():
    """Test: Get specific IP-MAC binding."""
    # Get the seq_num of our test entry
    bindings = fgt.api.cmdb.firewall.ipmacbinding.table.get()
    test_binding = None
    for binding in bindings:
        if binding.name == TEST_NAME:
            test_binding = binding
            break
    
    assert test_binding is not None, f"Test binding '{TEST_NAME}' not found"
    
    result = fgt.api.cmdb.firewall.ipmacbinding.table.get(seq_num=test_binding.seq_num)
    assert result is not None
    assert result.name == TEST_NAME
    assert result.ip == "192.168.100.10"
    assert result.mac == "00:11:22:33:44:55"


def test_delete_ipmacbinding_table():
    """Test: Delete IP-MAC binding."""
    # Get the seq_num of our test entry
    bindings = fgt.api.cmdb.firewall.ipmacbinding.table.get()
    test_binding = None
    for binding in bindings:
        if binding.name == TEST_NAME:
            test_binding = binding
            break
    
    assert test_binding is not None, f"Test binding '{TEST_NAME}' not found"
    
    result = fgt.api.cmdb.firewall.ipmacbinding.table.delete(seq_num=test_binding.seq_num)
    assert result is not None
    assert result.http_status == "success"
    
    # Verify deletion
    bindings = fgt.api.cmdb.firewall.ipmacbinding.table.get()
    binding_names = [b.name for b in bindings]
    assert TEST_NAME not in binding_names, "Binding should have been deleted"



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
        
    test_get_ipmacbinding_table()
    print("✓ test_get_ipmacbinding_table passed")

    test_post_ipmacbinding_table()
    print("✓ test_post_ipmacbinding_table passed")

    test_put_ipmacbinding_table()
    print("✓ test_put_ipmacbinding_table passed")

    test_get_specific_ipmacbinding()
    print("✓ test_get_specific_ipmacbinding passed")

    test_delete_ipmacbinding_table()
    print("✓ test_delete_ipmacbinding_table passed")

    cleanup()
    print("✓ post-Cleanup passed")
    
    print("\n✓ All tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
