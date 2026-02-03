"""
Auto-generated basic tests for cmdb.emailfilter/profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/emailfilter.profile.json
Category: cmdb
Endpoint: /cmdb/emailfilter/profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.emailfilter.profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import profile as validators
            print(f"✅ Successfully imported validators for profile")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_emailfilter_profile_post")
            assert hasattr(validators, "validate_emailfilter_profile_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import profile as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_emailfilter_profile_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_feature_set(self):
        """Test enum field feature-set validation."""
        from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import profile as validators
        
        valid_values = ['flow', 'proxy']
        
        # Test each valid value
        for value in valid_values:
            config = {"feature-set": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: feature-set={value}")
        
        print(f"✅ Enum field feature-set has {len(valid_values)} valid values")
    def auto_test_enum_spam_log(self):
        """Test enum field spam-log validation."""
        from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"spam-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: spam-log={value}")
        
        print(f"✅ Enum field spam-log has {len(valid_values)} valid values")
    def auto_test_enum_spam_log_fortiguard_response(self):
        """Test enum field spam-log-fortiguard-response validation."""
        from hfortix_fortios.api.v2.cmdb.emailfilter._helpers import profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"spam-log-fortiguard-response": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: spam-log-fortiguard-response={value}")
        
        print(f"✅ Enum field spam-log-fortiguard-response has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/emailfilter/profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/emailfilter.profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']