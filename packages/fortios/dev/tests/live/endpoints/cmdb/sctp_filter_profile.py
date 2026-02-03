"""
Tests for sctp-filter/profile endpoint - SCTP filter profiles
This endpoint configures SCTP (Stream Control Transmission Protocol) filter profiles.

Key features tested:
- GET all SCTP filter profiles
- POST to create SCTP filter profiles
- GET specific SCTP filter profile
- PUT to update SCTP filter profiles
- DELETE SCTP filter profiles
- PPID (Payload Protocol Identifier) filters with actions: pass, reset, replace
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

# NOTE: SCTP filter profile endpoint structure:
# - GET /sctp-filter/profile - Get all SCTP filter profiles
# - GET /sctp-filter/profile/{name} - Get specific SCTP filter profile
# - POST /sctp-filter/profile - Create new SCTP filter profile
# - PUT /sctp-filter/profile/{name} - Update SCTP filter profile
# - DELETE /sctp-filter/profile/{name} - Delete SCTP filter profile

def cleanup():
    """Cleanup all test SCTP filter profiles."""
    profiles = fgt.api.cmdb.sctp_filter.profile.get()
    for profile in profiles:
        if profile.name.startswith("TEST_SCTP_"):
            fgt.api.cmdb.sctp_filter.profile.delete(name=profile.name)


def test_get_sctp_filter_profile():
    """Test: Get all SCTP filter profiles"""
    result = fgt.api.cmdb.sctp_filter.profile.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_sctp_filter_profile_basic():
    """Test: Create basic SCTP filter profile"""
    result = fgt.api.cmdb.sctp_filter.profile.post(
        name="TEST_SCTP_1",
        comment="Basic SCTP filter profile"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_sctp_filter_profile_specific():
    """Test: Get specific SCTP filter profile"""
    result = fgt.api.cmdb.sctp_filter.profile.get(name="TEST_SCTP_1")
    assert result is not None
    assert result.http_status_code == 200
    assert result.name == "TEST_SCTP_1"


def test_post_sctp_filter_profile_with_ppid_pass():
    """Test: Create SCTP filter profile with PPID filter (pass action)"""
    result = fgt.api.cmdb.sctp_filter.profile.post(
        name="TEST_SCTP_2",
        comment="SCTP profile with PPID pass filter",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 0,
                "action": "pass",
                "comment": "Pass PPID 0"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_sctp_filter_profile_with_ppid_reset():
    """Test: Create SCTP filter profile with PPID filter (reset action)"""
    result = fgt.api.cmdb.sctp_filter.profile.post(
        name="TEST_SCTP_3",
        comment="SCTP profile with PPID reset filter",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 1,
                "action": "reset",
                "comment": "Reset on PPID 1"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_sctp_filter_profile_with_ppid_replace():
    """Test: Create SCTP filter profile with PPID filter (replace action)"""
    result = fgt.api.cmdb.sctp_filter.profile.post(
        name="TEST_SCTP_4",
        comment="SCTP profile with PPID replace filter",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 2,
                "action": "replace",
                "comment": "Replace PPID 2"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_sctp_filter_profile_multiple_ppid_filters():
    """Test: Create SCTP filter profile with multiple PPID filters"""
    result = fgt.api.cmdb.sctp_filter.profile.post(
        name="TEST_SCTP_5",
        comment="SCTP profile with multiple PPID filters",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 0,
                "action": "pass",
                "comment": "Pass PPID 0"
            },
            {
                "id": 2,
                "ppid": 3,
                "action": "reset",
                "comment": "Reset PPID 3"
            },
            {
                "id": 3,
                "ppid": 46,
                "action": "replace",
                "comment": "Replace M3UA (PPID 46)"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_post_sctp_filter_profile_common_ppids():
    """Test: Create SCTP filter profile with common SCTP PPIDs"""
    result = fgt.api.cmdb.sctp_filter.profile.post(
        name="TEST_SCTP_6",
        comment="SCTP profile for common protocol PPIDs",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 46,
                "action": "pass",
                "comment": "M3UA - MTP3 User Adaptation"
            },
            {
                "id": 2,
                "ppid": 3,
                "action": "pass",
                "comment": "IUA - ISDN User Adaptation"
            },
            {
                "id": 3,
                "ppid": 51,
                "action": "pass",
                "comment": "S1AP - S1 Application Protocol"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_sctp_filter_profile():
    """Test: Update SCTP filter profile"""
    result = fgt.api.cmdb.sctp_filter.profile.put(
        name="TEST_SCTP_1",
        comment="Updated SCTP filter profile",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 10,
                "action": "reset",
                "comment": "Added PPID filter"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_put_sctp_filter_profile_add_ppid_filters():
    """Test: Add more PPID filters to existing profile"""
    result = fgt.api.cmdb.sctp_filter.profile.put(
        name="TEST_SCTP_2",
        comment="SCTP profile with additional PPID filters",
        ppid_filters=[
            {
                "id": 1,
                "ppid": 0,
                "action": "pass",
                "comment": "Pass PPID 0"
            },
            {
                "id": 2,
                "ppid": 5,
                "action": "reset",
                "comment": "Reset PPID 5"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_delete_sctp_filter_profile():
    """Test: Delete specific SCTP filter profile"""
    result = fgt.api.cmdb.sctp_filter.profile.delete(name="TEST_SCTP_4")
    assert result is not None
    assert result.http_status == "success"


def test_get_sctp_filter_profile_verify():
    """Test: Verify SCTP filter profiles exist"""
    result = fgt.api.cmdb.sctp_filter.profile.get()
    assert result is not None
    assert result.http_status_code == 200


def test_zz_cleanup_after():
    """Test: Cleanup after all tests"""
    cleanup()


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

    test_get_sctp_filter_profile()
    print("✓ test_get_sctp_filter_profile passed")
    
    test_post_sctp_filter_profile_basic()
    print("✓ test_post_sctp_filter_profile_basic passed")
    
    test_get_sctp_filter_profile_specific()
    print("✓ test_get_sctp_filter_profile_specific passed")
    
    test_post_sctp_filter_profile_with_ppid_pass()
    print("✓ test_post_sctp_filter_profile_with_ppid_pass passed")
    
    test_post_sctp_filter_profile_with_ppid_reset()
    print("✓ test_post_sctp_filter_profile_with_ppid_reset passed")
    
    test_post_sctp_filter_profile_with_ppid_replace()
    print("✓ test_post_sctp_filter_profile_with_ppid_replace passed")
    
    test_post_sctp_filter_profile_multiple_ppid_filters()
    print("✓ test_post_sctp_filter_profile_multiple_ppid_filters passed")
    
    test_post_sctp_filter_profile_common_ppids()
    print("✓ test_post_sctp_filter_profile_common_ppids passed")
    
    test_put_sctp_filter_profile()
    print("✓ test_put_sctp_filter_profile passed")
    
    test_put_sctp_filter_profile_add_ppid_filters()
    print("✓ test_put_sctp_filter_profile_add_ppid_filters passed")
    
    test_delete_sctp_filter_profile()
    print("✓ test_delete_sctp_filter_profile passed")
    
    test_get_sctp_filter_profile_verify()
    print("✓ test_get_sctp_filter_profile_verify passed")

    cleanup()
    print("✓ All sctp-filter/profile tests passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
