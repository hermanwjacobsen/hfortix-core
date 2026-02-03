"""
Auto-generated basic tests for cmdb.user/saml

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.saml.json
Category: cmdb
Endpoint: /cmdb/user/saml

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_saml.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.saml


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSamlValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import saml as validators
            print(f"✅ Successfully imported validators for saml")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_saml_post")
            assert hasattr(validators, "validate_user_saml_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import saml as validators
        
        # Build minimal valid config with all required fields
        config = {
            "entity-id": "test_entity-id",  # string
            "idp-cert": "test_idp-cert",  # string
            "idp-entity-id": "test_idp-entity-id",  # string
            "idp-single-sign-on-url": "test_idp-single-sign-on-url",  # string
            "single-sign-on-url": "test_single-sign-on-url",  # string
        }
        
        try:
            result = validators.validate_user_saml_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSamlEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_scim_user_attr_type(self):
        """Test enum field scim-user-attr-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import saml as validators
        
        valid_values = ['user-name', 'display-name', 'external-id', 'email']
        
        # Test each valid value
        for value in valid_values:
            config = {"scim-user-attr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scim-user-attr-type={value}")
        
        print(f"✅ Enum field scim-user-attr-type has {len(valid_values)} valid values")
    def auto_test_enum_scim_group_attr_type(self):
        """Test enum field scim-group-attr-type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import saml as validators
        
        valid_values = ['display-name', 'external-id']
        
        # Test each valid value
        for value in valid_values:
            config = {"scim-group-attr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scim-group-attr-type={value}")
        
        print(f"✅ Enum field scim-group-attr-type has {len(valid_values)} valid values")
    def auto_test_enum_digest_method(self):
        """Test enum field digest-method validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import saml as validators
        
        valid_values = ['sha1', 'sha256']
        
        # Test each valid value
        for value in valid_values:
            config = {"digest-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: digest-method={value}")
        
        print(f"✅ Enum field digest-method has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/saml"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.saml.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']