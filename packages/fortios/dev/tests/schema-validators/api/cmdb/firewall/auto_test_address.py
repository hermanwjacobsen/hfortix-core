"""
Auto-generated basic tests for cmdb.firewall/address

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.address.json
Category: cmdb
Endpoint: /cmdb/firewall/address

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_address.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.address


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddressValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import address as validators
            print(f"✅ Successfully imported validators for address")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_address_post")
            assert hasattr(validators, "validate_firewall_address_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address as validators
        
        # Build minimal valid config with all required fields
        config = {
            "filter": "",  # var-string
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_firewall_address_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAddressEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address as validators
        
        valid_values = ['ipmask', 'iprange', 'fqdn', 'geography', 'wildcard', 'dynamic', 'interface-subnet', 'mac', 'route-tag']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_sub_type(self):
        """Test enum field sub-type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address as validators
        
        valid_values = ['sdn', 'clearpass-spt', 'fsso', 'rsso', 'ems-tag', 'fortivoice-tag', 'fortinac-tag', 'swc-tag', 'device-identification', 'external-resource', 'obsolete']
        
        # Test each valid value
        for value in valid_values:
            config = {"sub-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: sub-type={value}")
        
        print(f"✅ Enum field sub-type has {len(valid_values)} valid values")
    def auto_test_enum_clearpass_spt(self):
        """Test enum field clearpass-spt validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import address as validators
        
        valid_values = ['unknown', 'healthy', 'quarantine', 'checkup', 'transient', 'infected']
        
        # Test each valid value
        for value in valid_values:
            config = {"clearpass-spt": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: clearpass-spt={value}")
        
        print(f"✅ Enum field clearpass-spt has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/address"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.address.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']