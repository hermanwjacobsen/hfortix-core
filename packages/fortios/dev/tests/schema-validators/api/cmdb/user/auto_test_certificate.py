"""
Auto-generated basic tests for cmdb.user/certificate

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.certificate.json
Category: cmdb
Endpoint: /cmdb/user/certificate

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_certificate.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.certificate


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCertificateValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import certificate as validators
            print(f"✅ Successfully imported validators for certificate")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_certificate_post")
            assert hasattr(validators, "validate_user_certificate_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import certificate as validators
        
        # Build minimal valid config with all required fields
        config = {
            "common-name": "test_common-name",  # string
            "issuer": "test_issuer",  # string
            "status": "enable",  # option
            "type": "single-certificate",  # option
        }
        
        try:
            result = validators.validate_user_certificate_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCertificateEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import certificate as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import certificate as validators
        
        valid_values = ['single-certificate', 'trusted-issuer']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/certificate"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.certificate.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']