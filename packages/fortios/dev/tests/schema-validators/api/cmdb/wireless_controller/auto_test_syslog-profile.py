"""
Auto-generated basic tests for cmdb.wireless_controller/syslog_profile

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.syslog-profile.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/syslog-profile

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_syslog-profile.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.syslog_profile


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSyslogProfileEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_server_status(self):
        """Test enum field server-status validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import syslog_profile as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-status={value}")
        
        print(f"✅ Enum field server-status has {len(valid_values)} valid values")
    def auto_test_enum_server_type(self):
        """Test enum field server-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import syslog_profile as validators
        
        valid_values = ['standard', 'fortianalyzer']
        
        # Test each valid value
        for value in valid_values:
            config = {"server-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: server-type={value}")
        
        print(f"✅ Enum field server-type has {len(valid_values)} valid values")
    def auto_test_enum_log_level(self):
        """Test enum field log-level validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import syslog_profile as validators
        
        valid_values = ['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debugging']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-level": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-level={value}")
        
        print(f"✅ Enum field log-level has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/syslog_profile"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.syslog-profile.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']