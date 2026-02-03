from os import name
from time import sleep
from hfortix_fortios import FortiOS

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")

fgt: FortiOS = FortiOS(
    host="192.168.1.99", 
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1", 
    port=443, 
    verify=False, 
    error_mode="return", 
    vdom="root",  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1  # Short timeout if it does trigger
)


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
    test_get_system_config_revisions()
    print("✓ test_get_system_config_revisions passed")

    test_post_system_config_revisions_save()
    print("✓ test_post_system_config_revisions_save passed")

    test_post_config_revision_update_comments()
    print("✓ test_post_config_revision_update_comments passed")


    print("\n✓ All system config revision tests passed!")
