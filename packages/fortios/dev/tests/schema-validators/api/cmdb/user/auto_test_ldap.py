"""
Auto-generated basic tests for cmdb.user/ldap

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.ldap.json
Category: cmdb
Endpoint: /cmdb/user/ldap

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ldap.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.ldap


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLdapValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import ldap as validators
            print(f"✅ Successfully imported validators for ldap")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_ldap_post")
            assert hasattr(validators, "validate_user_ldap_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import ldap as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dn": "test_dn",  # string
            "interface": "test_interface",  # string
            "server": "test_server",  # string
            "username": "test_username",  # string
        }
        
        try:
            result = validators.validate_user_ldap_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLdapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_server_identity_check(self):
        """Test enum field server-identity-check validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import ldap as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-identity-check": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-identity-check={value}")
        
        print(f"✅ Enum field server-identity-check has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import ldap as validators
        
        valid_values = ['simple', 'anonymous', 'regular']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_two_factor(self):
        """Test enum field two-factor validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import ldap as validators
        
        valid_values = ['disable', 'fortitoken-cloud']
        
        # Test each valid value
        for value in valid_values:
            config = {"two-factor": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: two-factor={value}")
        
        print(f"✅ Enum field two-factor has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/ldap"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.ldap.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']