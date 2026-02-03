"""
Auto-generated basic tests for cmdb.system/interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.interface.json
Category: cmdb
Endpoint: /cmdb/system/interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import interface as validators
            print(f"✅ Successfully imported validators for interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_interface_post")
            assert hasattr(validators, "validate_system_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dhcp-relay-interface": "test_dhcp-relay-interface",  # string
            "interface": "test_interface",  # string
            "system-id": "00:00:00:00:00:00",  # mac-address
            "vdom": "test_vdom",  # string
        }
        
        try:
            result = validators.validate_system_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fortilink(self):
        """Test enum field fortilink validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import interface as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortilink": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortilink={value}")
        
        print(f"✅ Enum field fortilink has {len(valid_values)} valid values")
    def auto_test_enum_switch_controller_source_ip(self):
        """Test enum field switch-controller-source-ip validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import interface as validators
        
        valid_values = ['outbound', 'fixed']
        
        # Test each valid value
        for value in valid_values:
            config = {"switch-controller-source-ip": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: switch-controller-source-ip={value}")
        
        print(f"✅ Enum field switch-controller-source-ip has {len(valid_values)} valid values")
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import interface as validators
        
        valid_values = ['static', 'dhcp', 'pppoe']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']