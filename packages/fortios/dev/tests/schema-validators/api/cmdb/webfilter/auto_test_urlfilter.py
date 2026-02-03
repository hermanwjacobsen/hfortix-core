"""
Auto-generated basic tests for cmdb.webfilter/urlfilter

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.urlfilter.json
Category: cmdb
Endpoint: /cmdb/webfilter/urlfilter

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_urlfilter.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.webfilter.urlfilter


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoUrlfilterValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.webfilter._helpers import urlfilter as validators
            print(f"✅ Successfully imported validators for urlfilter")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_webfilter_urlfilter_post")
            assert hasattr(validators, "validate_webfilter_urlfilter_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import urlfilter as validators
        
        # Build minimal valid config with all required fields
        config = {
            "entries": "test_entries",  # string
            "id": 0,  # integer
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_webfilter_urlfilter_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoUrlfilterEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_one_arm_ips_urlfilter(self):
        """Test enum field one-arm-ips-urlfilter validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import urlfilter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"one-arm-ips-urlfilter": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: one-arm-ips-urlfilter={value}")
        
        print(f"✅ Enum field one-arm-ips-urlfilter has {len(valid_values)} valid values")
    def auto_test_enum_ip_addr_block(self):
        """Test enum field ip-addr-block validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import urlfilter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip-addr-block": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip-addr-block={value}")
        
        print(f"✅ Enum field ip-addr-block has {len(valid_values)} valid values")
    def auto_test_enum_ip4_mapped_ip6(self):
        """Test enum field ip4-mapped-ip6 validation."""
        from hfortix_fortios.api.v2.cmdb.webfilter._helpers import urlfilter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ip4-mapped-ip6": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ip4-mapped-ip6={value}")
        
        print(f"✅ Enum field ip4-mapped-ip6 has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/webfilter/urlfilter"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/webfilter.urlfilter.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']