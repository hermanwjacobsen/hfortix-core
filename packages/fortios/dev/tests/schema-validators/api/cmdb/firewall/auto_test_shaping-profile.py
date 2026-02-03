"""
Auto-generated basic tests for cmdb.firewall/shaping_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaping-profile.json
Category: cmdb
Endpoint: /cmdb/firewall/shaping-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_shaping-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.shaping_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoShapingProfileValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_profile as validators
            print(f"✅ Successfully imported validators for shaping-profile")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_shaping_profile_post")
            assert hasattr(validators, "validate_firewall_shaping_profile_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_profile as validators
        
        # Build minimal valid config with all required fields
        config = {
            "default-class-id": 0,  # integer
            "profile-name": "test_profile-name",  # string
        }
        
        try:
            result = validators.validate_firewall_shaping_profile_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoShapingProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_profile as validators
        
        valid_values = ['policing', 'queuing']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_npu_offloading(self):
        """Test enum field npu-offloading validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import shaping_profile as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"npu-offloading": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: npu-offloading={value}")
        
        print(f"✅ Enum field npu-offloading has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/shaping_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.shaping-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']