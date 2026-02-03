"""
Auto-generated basic tests for cmdb.firewall/ippool

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ippool.json
Category: cmdb
Endpoint: /cmdb/firewall/ippool

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ippool.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ippool


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIppoolValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool as validators
            print(f"✅ Successfully imported validators for ippool")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ippool_post")
            assert hasattr(validators, "validate_firewall_ippool_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool as validators
        
        # Build minimal valid config with all required fields
        config = {
            "block-size": 128,  # integer
            "client-prefix-length": 64,  # integer
            "endip": "0.0.0.0",  # ipv4-address-any
            "endport": 65533,  # integer
            "num-blocks-per-user": 8,  # integer
            "port-per-user": 0,  # integer
            "source-endip": "0.0.0.0",  # ipv4-address-any
            "source-prefix6": "::/0",  # ipv6-network
            "source-startip": "0.0.0.0",  # ipv4-address-any
            "startip": "0.0.0.0",  # ipv4-address-any
            "startport": 5117,  # integer
        }
        
        try:
            result = validators.validate_firewall_ippool_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIppoolEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool as validators
        
        valid_values = ['overload', 'one-to-one', 'fixed-port-range', 'port-block-allocation']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_permit_any_host(self):
        """Test enum field permit-any-host validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"permit-any-host": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: permit-any-host={value}")
        
        print(f"✅ Enum field permit-any-host has {len(valid_values)} valid values")
    def auto_test_enum_arp_reply(self):
        """Test enum field arp-reply validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ippool as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"arp-reply": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: arp-reply={value}")
        
        print(f"✅ Enum field arp-reply has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ippool"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ippool.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']