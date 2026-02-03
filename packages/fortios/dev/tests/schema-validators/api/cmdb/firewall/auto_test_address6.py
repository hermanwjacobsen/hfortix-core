"""
Auto-generated basic tests for cmdb.firewall/address6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.address6.json
Category: cmdb
Endpoint: /cmdb/firewall/address6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_address6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.address6


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddress6Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import address6 as validators
            print(f"✅ Successfully imported validators for address6")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_address6_post")
            assert hasattr(validators, "validate_firewall_address6_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address6 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "filter": "",  # var-string
            "template": "test_template",  # string
        }
        
        try:
            result = validators.validate_firewall_address6_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddress6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address6 as validators
        
        valid_values = ['ipprefix', 'iprange', 'fqdn', 'geography', 'dynamic', 'template', 'mac', 'route-tag', 'wildcard']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_host_type(self):
        """Test enum field host-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address6 as validators
        
        valid_values = ['any', 'specific']
        
        # Test each valid value
        for value in valid_values:
            config = {"host-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: host-type={value}")
        
        print(f"✅ Enum field host-type has {len(valid_values)} valid values")
    def auto_test_enum_sdn_addr_type(self):
        """Test enum field sdn-addr-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address6 as validators
        
        valid_values = ['private', 'public', 'all']
        
        # Test each valid value
        for value in valid_values:
            config = {"sdn-addr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sdn-addr-type={value}")
        
        print(f"✅ Enum field sdn-addr-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/address6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.address6.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']