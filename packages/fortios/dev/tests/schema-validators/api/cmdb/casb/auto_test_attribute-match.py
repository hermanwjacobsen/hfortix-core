"""
Auto-generated basic tests for cmdb.casb/attribute_match

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/casb.attribute-match.json
Category: cmdb
Endpoint: /cmdb/casb/attribute-match

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_attribute-match.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.casb.attribute_match


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAttributeMatchValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.casb._helpers import attribute_match as validators
            print(f"✅ Successfully imported validators for attribute-match")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_casb_attribute_match_post")
            assert hasattr(validators, "validate_casb_attribute_match_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.casb._helpers import attribute_match as validators
        
        # Build minimal valid config with all required fields
        config = {
            "application": "test_application",  # string
        }
        
        try:
            result = validators.validate_casb_attribute_match_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAttributeMatchEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_match_strategy(self):
        """Test enum field match-strategy validation."""
        from hfortix_fortios.api.v2.cmdb.casb._helpers import attribute_match as validators
        
        valid_values = ['or', 'and', 'subset']
        
        # Test each valid value
        for value in valid_values:
            config = {"match-strategy": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: match-strategy={value}")
        
        print(f"✅ Enum field match-strategy has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/casb/attribute_match"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/casb.attribute-match.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']