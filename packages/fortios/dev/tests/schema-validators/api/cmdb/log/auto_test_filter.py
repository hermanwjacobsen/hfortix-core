"""
Auto-generated basic tests for cmdb.log/syslogd/filter

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/log.syslogd.filter.json
Category: cmdb
Endpoint: /cmdb/log.syslogd/filter

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_filter.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.syslogd.filter


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFilterEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_severity(self):
        """Test enum field severity validation."""
        from hfortix_fortios.api.v2.cmdb.log.syslogd._helpers import filter as validators
        
        valid_values = ['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debug']
        
        # Test each valid value
        for value in valid_values:
            config = {"severity": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: severity={value}")
        
        print(f"✅ Enum field severity has {len(valid_values)} valid values")
    def auto_test_enum_forward_traffic(self):
        """Test enum field forward-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.log.syslogd._helpers import filter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"forward-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: forward-traffic={value}")
        
        print(f"✅ Enum field forward-traffic has {len(valid_values)} valid values")
    def auto_test_enum_local_traffic(self):
        """Test enum field local-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.log.syslogd._helpers import filter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"local-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: local-traffic={value}")
        
        print(f"✅ Enum field local-traffic has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/syslogd/filter"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/log.syslogd.filter.json"
TEST_HTTP_METHODS = ['GET', 'PUT']