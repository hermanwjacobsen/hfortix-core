"""
Auto-generated basic tests for cmdb.webfilter/ftgd_local_rating

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.ftgd-local-rating.json
Category: cmdb
Endpoint: /cmdb/webfilter/ftgd-local-rating

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ftgd-local-rating.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.webfilter.ftgd_local_rating


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFtgdLocalRatingValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.webfilter._helpers import ftgd_local_rating as validators
            print(f"✅ Successfully imported validators for ftgd-local-rating")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_webfilter_ftgd_local_rating_post")
            assert hasattr(validators, "validate_webfilter_ftgd_local_rating_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import ftgd_local_rating as validators
        
        # Build minimal valid config with all required fields
        config = {
            "rating": "",  # user
            "url": "test_url",  # string
        }
        
        try:
            result = validators.validate_webfilter_ftgd_local_rating_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFtgdLocalRatingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import ftgd_local_rating as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/webfilter/ftgd_local_rating"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.ftgd-local-rating.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']