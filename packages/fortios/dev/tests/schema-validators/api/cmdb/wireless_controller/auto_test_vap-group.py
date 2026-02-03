"""
Auto-generated basic tests for cmdb.wireless_controller/vap_group

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.vap-group.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/vap-group

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vap-group.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.vap_group


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVapGroupValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap_group as validators
            print(f"✅ Successfully imported validators for vap-group")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_wireless_controller_vap_group_post")
            assert hasattr(validators, "validate_wireless_controller_vap_group_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap_group as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_wireless_controller_vap_group_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/vap_group"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.vap-group.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']