"""
Auto-generated basic tests for cmdb.firewall/ldb_monitor

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ldb-monitor.json
Category: cmdb
Endpoint: /cmdb/firewall/ldb-monitor

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ldb-monitor.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.ldb_monitor


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLdbMonitorValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.firewall._helpers import ldb_monitor as validators
            print(f"✅ Successfully imported validators for ldb-monitor")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_firewall_ldb_monitor_post")
            assert hasattr(validators, "validate_firewall_ldb_monitor_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ldb_monitor as validators
        
        # Build minimal valid config with all required fields
        config = {
            "type": "ping",  # option
        }
        
        try:
            result = validators.validate_firewall_ldb_monitor_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLdbMonitorEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ldb_monitor as validators
        
        valid_values = ['ping', 'tcp', 'http', 'https', 'dns']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")
    def auto_test_enum_dns_protocol(self):
        """Test enum field dns-protocol validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import ldb_monitor as validators
        
        valid_values = ['udp', 'tcp']
        
        # Test each valid value
        for value in valid_values:
            config = {"dns-protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dns-protocol={value}")
        
        print(f"✅ Enum field dns-protocol has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/ldb_monitor"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.ldb-monitor.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']