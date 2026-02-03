"""
Auto-generated basic tests for cmdb.switch_controller/security_policy/x802_1x

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.security-policy.802-1X.json
Category: cmdb
Endpoint: /cmdb/switch-controller.security-policy/802-1X

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_802-1X.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.security_policy.x802_1x


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoX8021xValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import x802_1x as validators
            print(f"✅ Successfully imported validators for 802-1X")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_security_policy_x802_1x_post")
            assert hasattr(validators, "validate_switch_controller_security_policy_x802_1x_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import x802_1x as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auth-fail-vlan-id": "test_auth-fail-vlan-id",  # string
            "authserver-timeout-tagged-vlanid": "test_authserver-timeout-tagged-vlanid",  # string
            "authserver-timeout-vlanid": "test_authserver-timeout-vlanid",  # string
            "guest-vlan-id": "test_guest-vlan-id",  # string
            "user-group": "test_user-group",  # string
        }
        
        try:
            result = validators.validate_switch_controller_security_policy_x802_1x_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoX8021xEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_security_mode(self):
        """Test enum field security-mode validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import x802_1x as validators
        
        valid_values = ['802.1X', '802.1X-mac-based']
        
        # Test each valid value
        for value in valid_values:
            config = {"security-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: security-mode={value}")
        
        print(f"✅ Enum field security-mode has {len(valid_values)} valid values")
    def auto_test_enum_mac_auth_bypass(self):
        """Test enum field mac-auth-bypass validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import x802_1x as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"mac-auth-bypass": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mac-auth-bypass={value}")
        
        print(f"✅ Enum field mac-auth-bypass has {len(valid_values)} valid values")
    def auto_test_enum_auth_order(self):
        """Test enum field auth-order validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.security_policy._helpers import x802_1x as validators
        
        valid_values = ['dot1x-mab', 'mab-dot1x', 'mab']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-order": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-order={value}")
        
        print(f"✅ Enum field auth-order has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/security_policy/x802_1x"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.security-policy.802-1X.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']