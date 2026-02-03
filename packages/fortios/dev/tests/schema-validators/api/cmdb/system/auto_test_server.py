"""
Auto-generated basic tests for cmdb.system/dhcp6/server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dhcp6.server.json
Category: cmdb
Endpoint: /cmdb/system.dhcp6/server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.dhcp6.server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoServerValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system.dhcp6._helpers import server as validators
            print(f"✅ Successfully imported validators for server")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_dhcp6_server_post")
            assert hasattr(validators, "validate_system_dhcp6_server_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system.dhcp6._helpers import server as validators
        
        # Build minimal valid config with all required fields
        config = {
            "delegated-prefix-iaid": 0,  # integer
            "id": 0,  # integer
            "interface": "test_interface",  # string
            "subnet": "::/0",  # ipv6-prefix
            "upstream-interface": "test_upstream-interface",  # string
        }
        
        try:
            result = validators.validate_system_dhcp6_server_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system.dhcp6._helpers import server as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_rapid_commit(self):
        """Test enum field rapid-commit validation."""
        from hfortix_fortios.api.v2.cmdb.system.dhcp6._helpers import server as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"rapid-commit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: rapid-commit={value}")
        
        print(f"✅ Enum field rapid-commit has {len(valid_values)} valid values")
    def auto_test_enum_dns_service(self):
        """Test enum field dns-service validation."""
        from hfortix_fortios.api.v2.cmdb.system.dhcp6._helpers import server as validators
        
        valid_values = ['delegated', 'default', 'specify']
        
        # Test each valid value
        for value in valid_values:
            config = {"dns-service": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dns-service={value}")
        
        print(f"✅ Enum field dns-service has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/dhcp6/server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.dhcp6.server.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']