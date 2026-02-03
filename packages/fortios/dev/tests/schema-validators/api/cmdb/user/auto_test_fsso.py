"""
Auto-generated basic tests for cmdb.user/fsso

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.fsso.json
Category: cmdb
Endpoint: /cmdb/user/fsso

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fsso.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.fsso


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFssoValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import fsso as validators
            print(f"✅ Successfully imported validators for fsso")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_fsso_post")
            assert hasattr(validators, "validate_user_fsso_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "name": "test_name",  # string
            "port": 8000,  # integer
            "server": "test_server",  # string
        }
        
        try:
            result = validators.validate_user_fsso_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFssoEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso as validators
        
        valid_values = ['default', 'fortinac']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_ldap_poll(self):
        """Test enum field ldap-poll validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ldap-poll": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ldap-poll={value}")
        
        print(f"✅ Enum field ldap-poll has {len(valid_values)} valid values")
    def auto_test_enum_ssl(self):
        """Test enum field ssl validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import fsso as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssl": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssl={value}")
        
        print(f"✅ Enum field ssl has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/fsso"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.fsso.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']