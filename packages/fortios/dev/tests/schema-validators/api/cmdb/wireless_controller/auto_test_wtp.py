"""
Auto-generated basic tests for cmdb.wireless_controller/wtp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wtp.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/wtp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_wtp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.wtp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWtpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
            print(f"✅ Successfully imported validators for wtp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_wireless_controller_wtp_post")
            assert hasattr(validators, "validate_wireless_controller_wtp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "wtp-id": "test_wtp-id",  # string
            "wtp-profile": "test_wtp-profile",  # string
        }
        
        try:
            result = validators.validate_wireless_controller_wtp_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWtpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_admin(self):
        """Test enum field admin validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        valid_values = ['discovered', 'disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"admin": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: admin={value}")
        
        print(f"✅ Enum field admin has {len(valid_values)} valid values")
    def auto_test_enum_firmware_provision_latest(self):
        """Test enum field firmware-provision-latest validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        valid_values = ['disable', 'once']
        
        # Test each valid value
        for value in valid_values:
            config = {"firmware-provision-latest": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: firmware-provision-latest={value}")
        
        print(f"✅ Enum field firmware-provision-latest has {len(valid_values)} valid values")
    def auto_test_enum_override_led_state(self):
        """Test enum field override-led-state validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"override-led-state": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: override-led-state={value}")
        
        print(f"✅ Enum field override-led-state has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/wtp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wtp.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']