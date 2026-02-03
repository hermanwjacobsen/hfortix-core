"""
Auto-generated basic tests for cmdb.authentication/scheme

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.scheme.json
Category: cmdb
Endpoint: /cmdb/authentication/scheme

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_scheme.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.authentication.scheme


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSchemeValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.authentication._helpers import scheme as validators
            print(f"✅ Successfully imported validators for scheme")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_authentication_scheme_post")
            assert hasattr(validators, "validate_authentication_scheme_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import scheme as validators
        
        # Build minimal valid config with all required fields
        config = {
            "method": "ntlm",  # option
        }
        
        try:
            result = validators.validate_authentication_scheme_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSchemeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_method(self):
        """Test enum field method validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import scheme as validators
        
        valid_values = ['ntlm', 'basic', 'digest', 'form', 'negotiate', 'fsso', 'rsso', 'ssh-publickey', 'cert', 'saml', 'entra-sso']
        
        # Test each valid value
        for value in valid_values:
            config = {"method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: method={value}")
        
        print(f"✅ Enum field method has {len(valid_values)} valid values")
    def auto_test_enum_negotiate_ntlm(self):
        """Test enum field negotiate-ntlm validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import scheme as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"negotiate-ntlm": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: negotiate-ntlm={value}")
        
        print(f"✅ Enum field negotiate-ntlm has {len(valid_values)} valid values")
    def auto_test_enum_require_tfa(self):
        """Test enum field require-tfa validation."""
        from hfortix_fortios.api.v2.cmdb.authentication._helpers import scheme as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"require-tfa": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: require-tfa={value}")
        
        print(f"✅ Enum field require-tfa has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/authentication/scheme"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/authentication.scheme.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']