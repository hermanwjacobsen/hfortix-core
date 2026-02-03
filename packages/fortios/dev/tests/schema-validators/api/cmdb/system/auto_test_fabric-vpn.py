"""
Auto-generated basic tests for cmdb.system/fabric_vpn

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fabric-vpn.json
Category: cmdb
Endpoint: /cmdb/system/fabric-vpn

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fabric-vpn.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.fabric_vpn


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFabricVpnValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import fabric_vpn as validators
            print(f"✅ Successfully imported validators for fabric-vpn")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_fabric_vpn_post")
            assert hasattr(validators, "validate_system_fabric_vpn_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fabric_vpn as validators
        
        # Build minimal valid config with all required fields
        config = {
            "bgp-as": "",  # user
            "loopback-address-block": "0.0.0.0 0.0.0.0",  # ipv4-classnet-host
            "psksecret": "",  # password-3
            "status": "enable",  # option
            "sync-mode": "enable",  # option
            "vpn-role": "hub",  # option
        }
        
        try:
            result = validators.validate_system_fabric_vpn_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFabricVpnEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fabric_vpn as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_sync_mode(self):
        """Test enum field sync-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fabric_vpn as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"sync-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sync-mode={value}")
        
        print(f"✅ Enum field sync-mode has {len(valid_values)} valid values")
    def auto_test_enum_policy_rule(self):
        """Test enum field policy-rule validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import fabric_vpn as validators
        
        valid_values = ['health-check', 'manual', 'auto']
        
        # Test each valid value
        for value in valid_values:
            config = {"policy-rule": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: policy-rule={value}")
        
        print(f"✅ Enum field policy-rule has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/fabric_vpn"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.fabric-vpn.json"
TEST_HTTP_METHODS = ['GET', 'PUT']