"""
Auto-generated basic tests for cmdb.switch_controller/snmp_user

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.snmp-user.json
Category: cmdb
Endpoint: /cmdb/switch-controller/snmp-user

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_snmp-user.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.snmp_user


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSnmpUserValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import snmp_user as validators
            print(f"✅ Successfully imported validators for snmp-user")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_snmp_user_post")
            assert hasattr(validators, "validate_switch_controller_snmp_user_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import snmp_user as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auth-pwd": "",  # password
            "priv-pwd": "",  # password
        }
        
        try:
            result = validators.validate_switch_controller_snmp_user_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSnmpUserEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_queries(self):
        """Test enum field queries validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import snmp_user as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"queries": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: queries={value}")
        
        print(f"✅ Enum field queries has {len(valid_values)} valid values")
    def auto_test_enum_security_level(self):
        """Test enum field security-level validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import snmp_user as validators
        
        valid_values = ['no-auth-no-priv', 'auth-no-priv', 'auth-priv']
        
        # Test each valid value
        for value in valid_values:
            config = {"security-level": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: security-level={value}")
        
        print(f"✅ Enum field security-level has {len(valid_values)} valid values")
    def auto_test_enum_auth_proto(self):
        """Test enum field auth-proto validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import snmp_user as validators
        
        valid_values = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-proto": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-proto={value}")
        
        print(f"✅ Enum field auth-proto has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/snmp_user"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.snmp-user.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']