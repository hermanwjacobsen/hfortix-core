"""
Tests for rule/fmwp endpoint - FMWP (FortiGate Mobile Web Protection) signatures
This endpoint displays FMWP signature rules from FortiGuard.

NOTE: This endpoint appears to be READ-ONLY, similar to IPS signatures.
FMWP signatures are provided by FortiGuard and cannot be created/modified via API.

Key features tested:
- GET all FMWP signatures
- GET specific FMWP signature (if any exist)
"""

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

# NOTE: FMWP endpoint structure:
# - GET /rule/fmwp - Get all FMWP signatures
# - GET /rule/fmwp/{name} - Get specific FMWP signature
# POST/PUT/DELETE operations appear to be unsupported (read-only endpoint)


def test_get_rule_fmwp():
    """Test: Get all FMWP signatures"""
    result = fgt.api.cmdb.rule.fmwp.get()
    assert result is not None
    assert result.http_status_code == 200
    
    # FMWP signatures are provided by FortiGuard
    # The list may be empty if FortiGuard service is not configured
    print(f"✓ Retrieved {len(result)} FMWP signatures")


def test_get_rule_fmwp_verify_structure():
    """Test: Verify FMWP signature structure"""
    result = fgt.api.cmdb.rule.fmwp.get()
    assert result is not None
    
    # If signatures exist, verify their structure
    if len(result) > 0:
        sig = result[0] # type: ignore
        # Verify expected fields exist
        assert hasattr(sig, 'name'), "Signature should have 'name' field"
        print(f"✓ First signature name: {sig.name}")
    else:
        print("✓ No FMWP signatures available (FortiGuard service may not be configured)")


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
    test_get_rule_fmwp()
    print("✓ test_get_rule_fmwp passed")
    
    test_get_rule_fmwp_verify_structure()
    print("✓ test_get_rule_fmwp_verify_structure passed")

    print("✓ All rule/fmwp tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
