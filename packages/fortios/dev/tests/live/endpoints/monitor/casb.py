#!/usr/bin/env python
"""Tests for monitor/casb API endpoints.

Tests CASB (Cloud Access Security Broker) monitoring endpoints
for SaaS application visibility.
"""

import argparse
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



# ============================================================================
# CASB MONITOR TESTS
# ============================================================================

def test_casb_saas_application_details():
    """Test: Get CASB SaaS application details."""
    result = fgt.api.monitor.casb.saas_application.details.get()
    assert result.http_status == "success"


# ============================================================================
# MAIN - Direct execution
# ============================================================================

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
    print("Testing monitor/casb API endpoints...")
    print("=" * 60)
    print()
    
    test_casb_saas_application_details()
    print("✓ test_casb_saas_application_details passed")
    
    print()
    print("=" * 60)
    print("✓ All 1 test passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
