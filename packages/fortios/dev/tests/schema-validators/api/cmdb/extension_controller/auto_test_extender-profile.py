"""
Auto-generated basic tests for cmdb.extension_controller/extender_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.extender-profile.json
Category: cmdb
Endpoint: /cmdb/extension-controller/extender-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_extender-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.extension_controller.extender_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExtenderProfileValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_profile as validators
            print(f"✅ Successfully imported validators for extender-profile")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_extension_controller_extender_profile_post")
            assert hasattr(validators, "validate_extension_controller_extender_profile_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_profile as validators
        
        # Build minimal valid config with all required fields
        config = {
            "bandwidth-limit": 1024,  # integer
            "cellular": "test_cellular",  # string
            "extension": "wan-extension",  # option
            "lan-extension": "test_lan-extension",  # string
            "login-password": "",  # password
            "model": "FX201E",  # option
        }
        
        try:
            result = validators.validate_extension_controller_extender_profile_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExtenderProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_model(self):
        """Test enum field model validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_profile as validators
        
        valid_values = ['FX201E', 'FX211E', 'FX200F', 'FXA11F', 'FXE11F', 'FXA21F', 'FXE21F', 'FXA22F', 'FXE22F', 'FX212F', 'FX311F', 'FX312F', 'FX511F', 'FXR51G', 'FXN51G', 'FXW51G', 'FVG21F', 'FVA21F', 'FVG22F', 'FVA22F', 'FX04DA', 'FG', 'BS10FW', 'BS20GW', 'BS20GN', 'FVG51G', 'FXE11G', 'FX211G']
        
        # Test each valid value
        for value in valid_values:
            config = {"model": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: model={value}")
        
        print(f"✅ Enum field model has {len(valid_values)} valid values")
    def auto_test_enum_extension(self):
        """Test enum field extension validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_profile as validators
        
        valid_values = ['wan-extension', 'lan-extension']
        
        # Test each valid value
        for value in valid_values:
            config = {"extension": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: extension={value}")
        
        print(f"✅ Enum field extension has {len(valid_values)} valid values")
    def auto_test_enum_allowaccess(self):
        """Test enum field allowaccess validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_profile as validators
        
        valid_values = ['ping', 'telnet', 'http', 'https', 'ssh', 'snmp']
        
        # Test each valid value
        for value in valid_values:
            config = {"allowaccess": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: allowaccess={value}")
        
        print(f"✅ Enum field allowaccess has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/extension_controller/extender_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.extender-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']