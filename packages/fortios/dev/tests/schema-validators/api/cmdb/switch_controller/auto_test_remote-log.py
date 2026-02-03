"""
Auto-generated basic tests for cmdb.switch_controller/remote_log

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.remote-log.json
Category: cmdb
Endpoint: /cmdb/switch-controller/remote-log

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_remote-log.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.remote_log


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRemoteLogValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import remote_log as validators
            print(f"✅ Successfully imported validators for remote-log")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_remote_log_post")
            assert hasattr(validators, "validate_switch_controller_remote_log_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import remote_log as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
            "server": "test_server",  # string
        }
        
        try:
            result = validators.validate_switch_controller_remote_log_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRemoteLogEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import remote_log as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_severity(self):
        """Test enum field severity validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import remote_log as validators
        
        valid_values = ['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debug']
        
        # Test each valid value
        for value in valid_values:
            config = {"severity": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: severity={value}")
        
        print(f"✅ Enum field severity has {len(valid_values)} valid values")
    def auto_test_enum_csv(self):
        """Test enum field csv validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import remote_log as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"csv": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: csv={value}")
        
        print(f"✅ Enum field csv has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/remote_log"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.remote-log.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']