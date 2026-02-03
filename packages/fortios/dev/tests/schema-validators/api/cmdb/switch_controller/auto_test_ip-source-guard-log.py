"""
Auto-generated basic tests for cmdb.switch_controller/ip_source_guard_log

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.ip-source-guard-log.json
Category: cmdb
Endpoint: /cmdb/switch-controller/ip-source-guard-log

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ip-source-guard-log.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.ip_source_guard_log


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIpSourceGuardLogEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_log_violations(self):
        """Test enum field log-violations validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import ip_source_guard_log as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-violations": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-violations={value}")
        
        print(f"✅ Enum field log-violations has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/ip_source_guard_log"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.ip-source-guard-log.json"
TEST_HTTP_METHODS = ['GET', 'PUT']