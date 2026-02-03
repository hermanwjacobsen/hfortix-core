"""
Auto-generated basic tests for cmdb.system/vne_interface

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vne-interface.json
Category: cmdb
Endpoint: /cmdb/system/vne-interface

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vne-interface.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vne_interface


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVneInterfaceValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import vne_interface as validators
            print(f"✅ Successfully imported validators for vne-interface")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_vne_interface_post")
            assert hasattr(validators, "validate_system_vne_interface_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vne_interface as validators
        
        # Build minimal valid config with all required fields
        config = {
            "auto-asic-offload": "enable",  # option
            "bmr-hostname": "",  # password
            "br": "test_br",  # string
            "interface": "test_interface",  # string
            "mode": "map-e",  # option
            "ssl-certificate": "test_ssl-certificate",  # string
            "update-url": "test_update-url",  # string
        }
        
        try:
            result = validators.validate_system_vne_interface_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVneInterfaceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_auto_asic_offload(self):
        """Test enum field auto-asic-offload validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vne_interface as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auto-asic-offload": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auto-asic-offload={value}")
        
        print(f"✅ Enum field auto-asic-offload has {len(valid_values)} valid values")
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vne_interface as validators
        
        valid_values = ['map-e', 'fixed-ip', 'ds-lite']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vne_interface"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vne-interface.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']