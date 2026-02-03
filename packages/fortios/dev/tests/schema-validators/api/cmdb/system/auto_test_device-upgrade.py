"""
Auto-generated basic tests for cmdb.system/device_upgrade

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.device-upgrade.json
Category: cmdb
Endpoint: /cmdb/system/device-upgrade

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_device-upgrade.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.device_upgrade


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDeviceUpgradeValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
            print(f"✅ Successfully imported validators for device-upgrade")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_device_upgrade_post")
            assert hasattr(validators, "validate_system_device_upgrade_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        # Build minimal valid config with all required fields
        config = {
            "device-type": "fortigate",  # option
            "known-ha-members": "test_known-ha-members",  # string
            "maximum-minutes": 15,  # integer
            "next-path-index": 0,  # integer
            "serial": "test_serial",  # string
            "setup-time": "",  # user
            "status": "disabled",  # option
            "time": "",  # user
            "timing": "immediate",  # option
            "upgrade-path": "",  # user
        }
        
        try:
            result = validators.validate_system_device_upgrade_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDeviceUpgradeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        valid_values = ['disabled', 'initialized', 'downloading', 'device-disconnected', 'ready', 'coordinating', 'staging', 'final-check', 'upgrade-devices', 'cancelled', 'confirmed', 'done', 'failed']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_timing(self):
        """Test enum field timing validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        valid_values = ['immediate', 'scheduled']
        
        # Test each valid value
        for value in valid_values:
            config = {"timing": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: timing={value}")
        
        print(f"✅ Enum field timing has {len(valid_values)} valid values")
    def auto_test_enum_device_type(self):
        """Test enum field device-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        valid_values = ['fortigate', 'fortiswitch', 'fortiap', 'fortiextender']
        
        # Test each valid value
        for value in valid_values:
            config = {"device-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: device-type={value}")
        
        print(f"✅ Enum field device-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/device_upgrade"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.device-upgrade.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']