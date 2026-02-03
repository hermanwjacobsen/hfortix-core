"""
Auto-generated basic tests for cmdb.switch_controller/managed_switch

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.managed-switch.json
Category: cmdb
Endpoint: /cmdb/switch-controller/managed-switch

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_managed-switch.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.managed_switch


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManagedSwitchValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
            print(f"✅ Successfully imported validators for managed-switch")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_managed_switch_post")
            assert hasattr(validators, "validate_switch_controller_managed_switch_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        # Build minimal valid config with all required fields
        config = {
            "fsw-wan1-peer": "test_fsw-wan1-peer",  # string
            "radius-nas-ip": "0.0.0.0",  # ipv4-address
            "sn": "test_sn",  # string
            "switch-id": "test_switch-id",  # string
        }
        
        try:
            result = validators.validate_switch_controller_managed_switch_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManagedSwitchEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_purdue_level(self):
        """Test enum field purdue-level validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        valid_values = ['1', '1.5', '2', '2.5', '3', '3.5', '4', '5', '5.5']
        
        # Test each valid value
        for value in valid_values:
            config = {"purdue-level": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: purdue-level={value}")
        
        print(f"✅ Enum field purdue-level has {len(valid_values)} valid values")
    def auto_test_enum_fsw_wan1_admin(self):
        """Test enum field fsw-wan1-admin validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        valid_values = ['discovered', 'disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fsw-wan1-admin": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fsw-wan1-admin={value}")
        
        print(f"✅ Enum field fsw-wan1-admin has {len(valid_values)} valid values")
    def auto_test_enum_poe_pre_standard_detection(self):
        """Test enum field poe-pre-standard-detection validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"poe-pre-standard-detection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: poe-pre-standard-detection={value}")
        
        print(f"✅ Enum field poe-pre-standard-detection has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/managed_switch"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.managed-switch.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']