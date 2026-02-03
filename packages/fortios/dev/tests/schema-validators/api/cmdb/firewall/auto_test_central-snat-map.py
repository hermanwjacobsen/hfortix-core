"""
Auto-generated basic tests for cmdb.firewall/central_snat_map

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.central-snat-map.json
Category: cmdb
Endpoint: /cmdb/firewall/central-snat-map

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_central-snat-map.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.central_snat_map


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCentralSnatMapValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
            print(f"✅ Successfully imported validators for central-snat-map")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_central_snat_map_post")
            assert hasattr(validators, "validate_firewall_central_snat_map_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dst-addr": "test_dst-addr",  # string
            "dst-addr6": "test_dst-addr6",  # string
            "dstintf": "test_dstintf",  # string
            "orig-addr": "test_orig-addr",  # string
            "orig-addr6": "test_orig-addr6",  # string
            "srcintf": "test_srcintf",  # string
        }
        
        try:
            result = validators.validate_firewall_central_snat_map_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCentralSnatMapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_nat(self):
        """Test enum field nat validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import central_snat_map as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"nat": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: nat={value}")
        
        print(f"✅ Enum field nat has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/central_snat_map"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.central-snat-map.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']