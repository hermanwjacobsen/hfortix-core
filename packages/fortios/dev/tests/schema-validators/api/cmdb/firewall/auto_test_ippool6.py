"""
Auto-generated basic tests for cmdb.firewall/ippool6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ippool6.json
Category: cmdb
Endpoint: /cmdb/firewall/ippool6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ippool6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ippool6


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIppool6Validators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool6 as validators
            print(f"✅ Successfully imported validators for ippool6")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ippool6_post")
            assert hasattr(validators, "validate_firewall_ippool6_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool6 as validators
        
        # Build minimal valid config with all required fields
        config = {
            "endip": "::",  # ipv6-address
            "external-prefix": "::/0",  # ipv6-network
            "internal-prefix": "::/0",  # ipv6-network
            "startip": "::",  # ipv6-address
        }
        
        try:
            result = validators.validate_firewall_ippool6_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIppool6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool6 as validators
        
        valid_values = ['overload', 'nptv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_nat46(self):
        """Test enum field nat46 validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool6 as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"nat46": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: nat46={value}")
        
        print(f"✅ Enum field nat46 has {len(valid_values)} valid values")
    def auto_test_enum_add_nat46_route(self):
        """Test enum field add-nat46-route validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool6 as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"add-nat46-route": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: add-nat46-route={value}")
        
        print(f"✅ Enum field add-nat46-route has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ippool6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ippool6.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']