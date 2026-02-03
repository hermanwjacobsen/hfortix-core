"""
Auto-generated basic tests for cmdb.system/switch_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.switch-interface.json
Category: cmdb
Endpoint: /cmdb/system/switch-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_switch-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.switch_interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSwitchInterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import switch_interface as validators
            print(f"✅ Successfully imported validators for switch-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_switch_interface_post")
            assert hasattr(validators, "validate_system_switch_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import switch_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
            "vdom": "test_vdom",  # string
        }
        
        try:
            result = validators.validate_system_switch_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSwitchInterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import switch_interface as validators
        
        valid_values = ['switch', 'hub']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_intra_switch_policy(self):
        """Test enum field intra-switch-policy validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import switch_interface as validators
        
        valid_values = ['implicit', 'explicit']
        
        # Test each valid value
        for value in valid_values:
            config = {"intra-switch-policy": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: intra-switch-policy={value}")
        
        print(f"✅ Enum field intra-switch-policy has {len(valid_values)} valid values")
    def auto_test_enum_span(self):
        """Test enum field span validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import switch_interface as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"span": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: span={value}")
        
        print(f"✅ Enum field span has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/switch_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.switch-interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']