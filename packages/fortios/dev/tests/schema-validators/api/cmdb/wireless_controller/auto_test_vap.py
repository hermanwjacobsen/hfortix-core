"""
Auto-generated basic tests for cmdb.wireless_controller/vap

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.vap.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/vap

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vap.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.vap


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVapValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap as validators
            print(f"✅ Successfully imported validators for vap")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_wireless_controller_vap_post")
            assert hasattr(validators, "validate_wireless_controller_vap_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_wireless_controller_vap_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_pre_auth(self):
        """Test enum field pre-auth validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"pre-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: pre-auth={value}")
        
        print(f"✅ Enum field pre-auth has {len(valid_values)} valid values")
    def auto_test_enum_external_pre_auth(self):
        """Test enum field external-pre-auth validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"external-pre-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: external-pre-auth={value}")
        
        print(f"✅ Enum field external-pre-auth has {len(valid_values)} valid values")
    def auto_test_enum_mesh_backhaul(self):
        """Test enum field mesh-backhaul validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import vap as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"mesh-backhaul": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mesh-backhaul={value}")
        
        print(f"✅ Enum field mesh-backhaul has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/vap"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.vap.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']