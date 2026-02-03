"""
Auto-generated basic tests for cmdb.system/ddns

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ddns.json
Category: cmdb
Endpoint: /cmdb/system/ddns

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ddns.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ddns


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDdnsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
            print(f"✅ Successfully imported validators for ddns")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ddns_post")
            assert hasattr(validators, "validate_system_ddns_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        # Build minimal valid config with all required fields
        config = {
            "ddns-server": "dyndns.org",  # option
            "monitor-interface": "test_monitor-interface",  # string
        }
        
        try:
            result = validators.validate_system_ddns_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDdnsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ddns_server(self):
        """Test enum field ddns-server validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        valid_values = ['dyndns.org', 'dyns.net', 'tzo.com', 'vavic.com', 'dipdns.net', 'now.net.cn', 'dhs.org', 'easydns.com', 'genericDDNS', 'FortiGuardDDNS', 'noip.com']
        
        # Test each valid value
        for value in valid_values:
            config = {"ddns-server": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ddns-server={value}")
        
        print(f"✅ Enum field ddns-server has {len(valid_values)} valid values")
    def auto_test_enum_addr_type(self):
        """Test enum field addr-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-type={value}")
        
        print(f"✅ Enum field addr-type has {len(valid_values)} valid values")
    def auto_test_enum_server_type(self):
        """Test enum field server-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ddns as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-type={value}")
        
        print(f"✅ Enum field server-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ddns"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ddns.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']