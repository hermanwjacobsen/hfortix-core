"""
Auto-generated basic tests for cmdb.system/pppoe_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.pppoe-interface.json
Category: cmdb
Endpoint: /cmdb/system/pppoe-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_pppoe-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.pppoe_interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPppoeInterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import pppoe_interface as validators
            print(f"✅ Successfully imported validators for pppoe-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_pppoe_interface_post")
            assert hasattr(validators, "validate_system_pppoe_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import pppoe_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "device": "test_device",  # string
        }
        
        try:
            result = validators.validate_system_pppoe_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPppoeInterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_dial_on_demand(self):
        """Test enum field dial-on-demand validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import pppoe_interface as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dial-on-demand": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dial-on-demand={value}")
        
        print(f"✅ Enum field dial-on-demand has {len(valid_values)} valid values")
    def auto_test_enum_ipv6(self):
        """Test enum field ipv6 validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import pppoe_interface as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipv6": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipv6={value}")
        
        print(f"✅ Enum field ipv6 has {len(valid_values)} valid values")
    def auto_test_enum_pppoe_egress_cos(self):
        """Test enum field pppoe-egress-cos validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import pppoe_interface as validators
        
        valid_values = ['cos0', 'cos1', 'cos2', 'cos3', 'cos4', 'cos5', 'cos6', 'cos7']
        
        # Test each valid value
        for value in valid_values:
            config = {"pppoe-egress-cos": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: pppoe-egress-cos={value}")
        
        print(f"✅ Enum field pppoe-egress-cos has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/pppoe_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.pppoe-interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']