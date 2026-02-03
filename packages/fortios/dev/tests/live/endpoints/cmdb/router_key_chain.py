import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))
from fgtclient import fgt

import pytest

# Run tests on a single worker to preserve state (group by filename)
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# NOTE: Key-chain key configuration limitation
# FortiOS API returns error -56 "Empty values are not allowed" when trying to
# configure keys via POST/PUT operations. This appears to be a FortiOS API limitation
# where the 'key' sub-table must be configured via CLI rather than REST API.
# These tests verify the key-chain container CRUD operations work correctly.
# Actual key configuration would need to be done via CLI commands like:
#   config router key-chain
#       edit "keychain_name"
#           config key
#               edit 1
#                   set key-string "secret"
#               next
#           end
#       next
#   end

def cleanup():
    """Remove all test key-chains"""
    key_chains = fgt.api.cmdb.router.key_chain.get()
    for kc in key_chains:
        if kc.name.startswith("test_"):
            fgt.api.cmdb.router.key_chain.delete(name=kc.name)


def test_get_router_key_chain():
    """Test: Get all router key-chains"""
    result = fgt.api.cmdb.router.key_chain.get()
    assert result is not None


def test_post_router_key_chain():
    """Test: Create a basic key-chain with one key"""
    result = fgt.api.cmdb.router.key_chain.post(
        name="test_keychain1",
        key=[
                {
                "id": "1",
                "accept_lifetime": "00:00:00 01 01 2026 00:00:00 01 01 2030",
                "send_lifetime": "00:00:00 01 01 2026 00:00:00 01 01 2030",
                "key_string": "MySuperSecretKey123",
                "algorithm": "hmac-sha256"
                }
            ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.router.key_chain.get(name="test_keychain1")
    assert len(verify.key) == 1
    assert verify.key[0].id == "1"
    assert verify.key[0].key_string is not None
    assert verify.key[0].algorithm == "hmac-sha256"




def test_get_specific_router_key_chain():
    """Test: Get specific key-chain"""
    result = fgt.api.cmdb.router.key_chain.get(name="test_keychain1")
    assert result is not None
    assert result.name == "test_keychain1"


def test_delete_router_key_chain():
    """Test: Delete key-chains"""
    # Delete all test key-chains
    result = fgt.api.cmdb.router.key_chain.delete(name="test_keychain1")
    assert result is not None
    assert result.http_status == "success"
    

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

    test_get_router_key_chain()
    print("✓ test_get_router_key_chain passed")
    
    test_post_router_key_chain()
    print("✓ test_post_router_key_chain_basic passed")
    
   
    test_get_specific_router_key_chain()
    print("✓ test_get_specific_router_key_chain passed")
    
    test_delete_router_key_chain()
    print("✓ test_delete_router_key_chain passed")

    cleanup()
    print("✓ All router/key-chain tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
