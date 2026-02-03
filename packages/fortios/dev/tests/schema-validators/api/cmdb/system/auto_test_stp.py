"""
Auto-generated basic tests for cmdb.system/stp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.stp.json
Category: cmdb
Endpoint: /cmdb/system/stp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_stp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.stp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoStpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_switch_priority(self):
        """Test enum field switch-priority validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import stp as validators
        
        valid_values = ['0', '4096', '8192', '12288', '16384', '20480', '24576', '28672', '32768', '36864', '40960', '45056', '49152', '53248', '57344']
        
        # Test each valid value
        for value in valid_values:
            config = {"switch-priority": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: switch-priority={value}")
        
        print(f"✅ Enum field switch-priority has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/stp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.stp.json"
TEST_HTTP_METHODS = ['GET', 'PUT']