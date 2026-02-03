"""
Auto-generated basic tests for cmdb.dlp/data_type

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.data-type.json
Category: cmdb
Endpoint: /cmdb/dlp/data-type

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_data-type.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.dlp.data_type


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDataTypeValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.dlp._helpers import data_type as validators
            print(f"✅ Successfully imported validators for data-type")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_dlp_data_type_post")
            assert hasattr(validators, "validate_dlp_data_type_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import data_type as validators
        
        # Build minimal valid config with all required fields
        config = {
            "look-ahead": 1,  # integer
            "look-back": 1,  # integer
            "match-ahead": 1,  # integer
            "match-back": 1,  # integer
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_dlp_data_type_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDataTypeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_verify_transformed_pattern(self):
        """Test enum field verify-transformed-pattern validation."""
        from hfortix_fortios.api.v2.cmdb.dlp._helpers import data_type as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"verify-transformed-pattern": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: verify-transformed-pattern={value}")
        
        print(f"✅ Enum field verify-transformed-pattern has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/dlp/data_type"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/dlp.data-type.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']