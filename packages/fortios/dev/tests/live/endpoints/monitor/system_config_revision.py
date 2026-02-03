import argparse
import sys
from pathlib import Path
import pytest
import base64
import requests
import os
from dotenv import load_dotenv
import urllib3

# Disable SSL warnings for test environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Run registration monitor tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group(Path(__file__).stem)

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def test_get_system_config_revisions():
    """Test: Get system configuration revisions"""
    result = fgt.api.monitor.system.config_revision.get()
    assert result is not None
    assert 'revisions' in result
    print(f"✓ Retrieved {len(result['revisions'])} configuration revisions")

def test_post_system_config_revisions_save():
    """Test: Save current configuration as a new revision"""
    result = fgt.api.monitor.system.config_revision.save.post(comments="test_save_config_revision")
    assert result is not None
    assert result.http_status == "success"
    print(f"✓ Saved new configuration revision")
    verify = fgt.api.monitor.system.config_revision.info.get(config_id=result['id'])
    assert verify is not None

def test_post_config_revision_update_comments():
    """Test: Update comments for a specific configuration revision"""
    # First, save a new revision to update
    save_result = fgt.api.monitor.system.config_revision.save.post(comments="test_initial_comment")
    assert save_result is not None
    config_id = save_result['id']
    
    # Now, update the comments
    update_result = fgt.api.monitor.system.config_revision.update_comments.post(
        config_id=config_id,
        comments="test_updated_comment"
    )
    assert update_result is not None
    assert update_result.http_status == "success"
    print(f"✓ Updated comments for configuration revision ID: {config_id}")
    
    # Verify the update
    verify = fgt.api.monitor.system.config_revision.get()
    for rev in verify['revisions']:
        if rev['id'] == config_id:
            assert rev['comment'] == "test_updated_comment"
            print(f"✓ Verified updated comments for configuration revision ID: {config_id}")
            break
    else:
        pytest.fail(f"Configuration revision ID {config_id} not found in revisions")

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
    test_get_system_config_revisions()
    print("✓ test_get_system_config_revisions passed")

    test_post_system_config_revisions_save()
    print("✓ test_post_system_config_revisions_save passed")

    test_post_config_revision_update_comments()
    print("✓ test_post_config_revision_update_comments passed")


    print("\n✓ All system config revision tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
