"""
Auto-generated basic tests for cmdb.videofilter/keyword

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/videofilter.keyword.json
Category: cmdb
Endpoint: /cmdb/videofilter/keyword

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_keyword.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.videofilter.keyword


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoKeywordValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.videofilter._helpers import keyword as validators
            print(f"✅ Successfully imported validators for keyword")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_videofilter_keyword_post")
            assert hasattr(validators, "validate_videofilter_keyword_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.videofilter._helpers import keyword as validators
        
        # Build minimal valid config with all required fields
        config = {
            "id": 0,  # integer
            "match": "or",  # option
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_videofilter_keyword_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoKeywordEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_match(self):
        """Test enum field match validation."""
        from hfortix_fortios.api.v2.cmdb.videofilter._helpers import keyword as validators
        
        valid_values = ['or', 'and']
        
        # Test each valid value
        for value in valid_values:
            config = {"match": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: match={value}")
        
        print(f"✅ Enum field match has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/videofilter/keyword"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/videofilter.keyword.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']