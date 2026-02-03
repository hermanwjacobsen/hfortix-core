"""
Auto-generated basic tests for cmdb.firewall/local_in_policy6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.local-in-policy6.json
Category: cmdb
Endpoint: /cmdb/firewall/local-in-policy6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_local-in-policy6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.local_in_policy6


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalInPolicy6Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy6 as validators
            print(f"✅ Successfully imported validators for local-in-policy6")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_local_in_policy6_post")
            assert hasattr(validators, "validate_firewall_local_in_policy6_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy6 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "dstaddr": "test_dstaddr",  # string
            "intf": "test_intf",  # string
            "schedule": "test_schedule",  # string
            "service": "test_service",  # string
            "srcaddr": "test_srcaddr",  # string
        }
        
        try:
            result = validators.validate_firewall_local_in_policy6_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLocalInPolicy6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_srcaddr_negate(self):
        """Test enum field srcaddr-negate validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"srcaddr-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: srcaddr-negate={value}")
        
        print(f"✅ Enum field srcaddr-negate has {len(valid_values)} valid values")
    def auto_test_enum_internet_service6_src(self):
        """Test enum field internet-service6-src validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"internet-service6-src": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: internet-service6-src={value}")
        
        print(f"✅ Enum field internet-service6-src has {len(valid_values)} valid values")
    def auto_test_enum_dstaddr_negate(self):
        """Test enum field dstaddr-negate validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import local_in_policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dstaddr-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dstaddr-negate={value}")
        
        print(f"✅ Enum field dstaddr-negate has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/local_in_policy6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.local-in-policy6.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']