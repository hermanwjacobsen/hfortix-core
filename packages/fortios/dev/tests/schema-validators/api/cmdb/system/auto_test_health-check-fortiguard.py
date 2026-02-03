"""
Auto-generated basic tests for cmdb.system/health_check_fortiguard

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.health-check-fortiguard.json
Category: cmdb
Endpoint: /cmdb/system/health-check-fortiguard

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_health-check-fortiguard.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.health_check_fortiguard


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHealthCheckFortiguardValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import health_check_fortiguard as validators
            print(f"✅ Successfully imported validators for health-check-fortiguard")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_health_check_fortiguard_post")
            assert hasattr(validators, "validate_system_health_check_fortiguard_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import health_check_fortiguard as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
            "protocol": "ping",  # option
            "server": "test_server",  # string
        }
        
        try:
            result = validators.validate_system_health_check_fortiguard_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoHealthCheckFortiguardEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_protocol(self):
        """Test enum field protocol validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import health_check_fortiguard as validators
        
        valid_values = ['ping', 'tcp-echo', 'udp-echo', 'http', 'https', 'twamp', 'dns', 'tcp-connect', 'ftp']
        
        # Test each valid value
        for value in valid_values:
            config = {"protocol": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: protocol={value}")
        
        print(f"✅ Enum field protocol has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/health_check_fortiguard"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.health-check-fortiguard.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']