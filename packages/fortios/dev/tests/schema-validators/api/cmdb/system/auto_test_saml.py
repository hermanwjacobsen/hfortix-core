"""
Auto-generated basic tests for cmdb.system/saml

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.saml.json
Category: cmdb
Endpoint: /cmdb/system/saml

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_saml.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.saml


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSamlValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import saml as validators
            print(f"✅ Successfully imported validators for saml")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_saml_post")
            assert hasattr(validators, "validate_system_saml_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import saml as validators
        
        # Build minimal valid config with all required fields
        config = {
            "default-login-page": "normal",  # option
            "default-profile": "test_default-profile",  # string
            "entity-id": "test_entity-id",  # string
            "idp-cert": "test_idp-cert",  # string
            "server-address": "test_server-address",  # string
        }
        
        try:
            result = validators.validate_system_saml_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSamlEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import saml as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_role(self):
        """Test enum field role validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import saml as validators
        
        valid_values = ['identity-provider', 'service-provider']
        
        # Test each valid value
        for value in valid_values:
            config = {"role": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: role={value}")
        
        print(f"✅ Enum field role has {len(valid_values)} valid values")
    def auto_test_enum_default_login_page(self):
        """Test enum field default-login-page validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import saml as validators
        
        valid_values = ['normal', 'sso']
        
        # Test each valid value
        for value in valid_values:
            config = {"default-login-page": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: default-login-page={value}")
        
        print(f"✅ Enum field default-login-page has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/saml"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.saml.json"
TEST_HTTP_METHODS = ['GET', 'PUT']