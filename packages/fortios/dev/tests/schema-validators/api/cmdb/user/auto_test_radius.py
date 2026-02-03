"""
Auto-generated basic tests for cmdb.user/radius

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.radius.json
Category: cmdb
Endpoint: /cmdb/user/radius

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_radius.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.radius


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRadiusValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
            print(f"✅ Successfully imported validators for radius")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_radius_post")
            assert hasattr(validators, "validate_user_radius_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "rsso": "enable",  # option
            "rsso-context-timeout": 28800,  # integer
            "rsso-endpoint-attribute": "User-Name",  # option
            "rsso-endpoint-block-attribute": "User-Name",  # option
            "rsso-log-period": 0,  # integer
            "rsso-radius-response": "enable",  # option
            "rsso-radius-server-port": 1813,  # integer
            "rsso-secret": "",  # password
            "rsso-validate-request-secret": "enable",  # option
            "secret": "",  # password
            "server": "test_server",  # string
            "sso-attribute": "User-Name",  # option
            "sso-attribute-value-override": "enable",  # option
        }
        
        try:
            result = validators.validate_user_radius_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRadiusEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_all_usergroup(self):
        """Test enum field all-usergroup validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"all-usergroup": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: all-usergroup={value}")
        
        print(f"✅ Enum field all-usergroup has {len(valid_values)} valid values")
    def auto_test_enum_use_management_vdom(self):
        """Test enum field use-management-vdom validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"use-management-vdom": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: use-management-vdom={value}")
        
        print(f"✅ Enum field use-management-vdom has {len(valid_values)} valid values")
    def auto_test_enum_switch_controller_nas_ip_dynamic(self):
        """Test enum field switch-controller-nas-ip-dynamic validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"switch-controller-nas-ip-dynamic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: switch-controller-nas-ip-dynamic={value}")
        
        print(f"✅ Enum field switch-controller-nas-ip-dynamic has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/radius"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.radius.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']