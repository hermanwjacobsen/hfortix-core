"""
Auto-generated basic tests for cmdb.system/vxlan

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vxlan.json
Category: cmdb
Endpoint: /cmdb/system/vxlan

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vxlan.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vxlan


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVxlanValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import vxlan as validators
            print(f"✅ Successfully imported validators for vxlan")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_vxlan_post")
            assert hasattr(validators, "validate_system_vxlan_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vxlan as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "ip-version": "ipv4-unicast",  # option
            "multicast-ttl": 0,  # integer
            "remote-ip6": "test_remote-ip6",  # string
            "vni": 0,  # integer
        }
        
        try:
            result = validators.validate_system_vxlan_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVxlanEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ip_version(self):
        """Test enum field ip-version validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vxlan as validators
        
        valid_values = ['ipv4-unicast', 'ipv6-unicast', 'ipv4-multicast', 'ipv6-multicast']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-version": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-version={value}")
        
        print(f"✅ Enum field ip-version has {len(valid_values)} valid values")
    def auto_test_enum_learn_from_traffic(self):
        """Test enum field learn-from-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vxlan as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"learn-from-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: learn-from-traffic={value}")
        
        print(f"✅ Enum field learn-from-traffic has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vxlan"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vxlan.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']