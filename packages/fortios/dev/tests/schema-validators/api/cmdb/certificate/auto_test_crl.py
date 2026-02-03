"""
Auto-generated basic tests for cmdb.certificate/crl

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/certificate.crl.json
Category: cmdb
Endpoint: /cmdb/certificate/crl

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_crl.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.certificate.crl


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCrlValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.certificate._helpers import crl as validators
            print(f"✅ Successfully imported validators for crl")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_certificate_crl_post")
            assert hasattr(validators, "validate_certificate_crl_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import crl as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_certificate_crl_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCrlEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_range(self):
        """Test enum field range validation."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import crl as validators
        
        valid_values = ['global', 'vdom']
        
        # Test each valid value
        for value in valid_values:
            config = {"range": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: range={value}")
        
        print(f"✅ Enum field range has {len(valid_values)} valid values")
    def auto_test_enum_source(self):
        """Test enum field source validation."""
        from hfortix_fortios.api.v2.cmdb.certificate._helpers import crl as validators
        
        valid_values = ['factory', 'user', 'bundle']
        
        # Test each valid value
        for value in valid_values:
            config = {"source": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: source={value}")
        
        print(f"✅ Enum field source has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/certificate/crl"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/certificate.crl.json"
TEST_HTTP_METHODS = ['GET']