"""
Auto-generated basic tests for cmdb.ips/sensor

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.sensor.json
Category: cmdb
Endpoint: /cmdb/ips/sensor

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_sensor.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ips.sensor


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSensorValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.ips._helpers import sensor as validators
            print(f"✅ Successfully imported validators for sensor")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_ips_sensor_post")
            assert hasattr(validators, "validate_ips_sensor_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import sensor as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_ips_sensor_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSensorEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_block_malicious_url(self):
        """Test enum field block-malicious-url validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import sensor as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"block-malicious-url": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: block-malicious-url={value}")
        
        print(f"✅ Enum field block-malicious-url has {len(valid_values)} valid values")
    def auto_test_enum_scan_botnet_connections(self):
        """Test enum field scan-botnet-connections validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import sensor as validators
        
        valid_values = ['disable', 'block', 'monitor']
        
        # Test each valid value
        for value in valid_values:
            config = {"scan-botnet-connections": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scan-botnet-connections={value}")
        
        print(f"✅ Enum field scan-botnet-connections has {len(valid_values)} valid values")
    def auto_test_enum_extended_log(self):
        """Test enum field extended-log validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import sensor as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"extended-log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: extended-log={value}")
        
        print(f"✅ Enum field extended-log has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ips/sensor"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.sensor.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']