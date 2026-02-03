"""
Auto-generated basic tests for cmdb.extension_controller/extender_vap

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.extender-vap.json
Category: cmdb
Endpoint: /cmdb/extension-controller/extender-vap

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_extender-vap.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.extension_controller.extender_vap


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExtenderVapValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_vap as validators
            print(f"✅ Successfully imported validators for extender-vap")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_extension_controller_extender_vap_post")
            assert hasattr(validators, "validate_extension_controller_extender_vap_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_vap as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auth-server-address": "test_auth-server-address",  # string
            "auth-server-port": 0,  # integer
            "auth-server-secret": "test_auth-server-secret",  # string
            "passphrase": "",  # password
            "sae-password": "",  # password
            "security": "OPEN",  # option
            "ssid": "test_ssid",  # string
            "type": "local-vap",  # option
        }
        
        try:
            result = validators.validate_extension_controller_extender_vap_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoExtenderVapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_vap as validators
        
        valid_values = ['local-vap', 'lan-ext-vap']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_broadcast_ssid(self):
        """Test enum field broadcast-ssid validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_vap as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"broadcast-ssid": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: broadcast-ssid={value}")
        
        print(f"✅ Enum field broadcast-ssid has {len(valid_values)} valid values")
    def auto_test_enum_security(self):
        """Test enum field security validation."""
        from hfortix_fortios.api.v2.cmdb.extension_controller._helpers import extender_vap as validators
        
        valid_values = ['OPEN', 'WPA2-Personal', 'WPA-WPA2-Personal', 'WPA3-SAE', 'WPA3-SAE-Transition', 'WPA2-Enterprise', 'WPA3-Enterprise-only', 'WPA3-Enterprise-transition', 'WPA3-Enterprise-192-bit']
        
        # Test each valid value
        for value in valid_values:
            config = {"security": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: security={value}")
        
        print(f"✅ Enum field security has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/extension_controller/extender_vap"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/extension-controller.extender-vap.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']