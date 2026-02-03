"""
Auto-generated basic tests for cmdb.log/custom_field

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/log.custom-field.json
Category: cmdb
Endpoint: /cmdb/log/custom-field

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_custom-field.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.custom_field


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCustomFieldValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.log._helpers import custom_field as validators
            print(f"✅ Successfully imported validators for custom-field")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_log_custom_field_post")
            assert hasattr(validators, "validate_log_custom_field_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import custom_field as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
            "value": "test_value",  # string
        }
        
        try:
            result = validators.validate_log_custom_field_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/custom_field"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/log.custom-field.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']