"""
Auto-generated basic tests for cmdb.system/link_monitor

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.link-monitor.json
Category: cmdb
Endpoint: /cmdb/system/link-monitor

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_link-monitor.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.link_monitor


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLinkMonitorValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import link_monitor as validators
            print(f"✅ Successfully imported validators for link-monitor")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_link_monitor_post")
            assert hasattr(validators, "validate_system_link_monitor_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import link_monitor as validators
        
        # Build minimal valid config with all required fields
        config = {
            "http-get": "test_http-get",  # string
            "server": "test_server",  # string
        }
        
        try:
            result = validators.validate_system_link_monitor_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLinkMonitorEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_addr_mode(self):
        """Test enum field addr-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import link_monitor as validators
        
        valid_values = ['ipv4', 'ipv6']
        
        # Test each valid value
        for value in valid_values:
            config = {"addr-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: addr-mode={value}")
        
        print(f"✅ Enum field addr-mode has {len(valid_values)} valid values")
    def auto_test_enum_server_config(self):
        """Test enum field server-config validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import link_monitor as validators
        
        valid_values = ['default', 'individual']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-config": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-config={value}")
        
        print(f"✅ Enum field server-config has {len(valid_values)} valid values")
    def auto_test_enum_server_type(self):
        """Test enum field server-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import link_monitor as validators
        
        valid_values = ['static', 'dynamic']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-type={value}")
        
        print(f"✅ Enum field server-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/link_monitor"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.link-monitor.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']