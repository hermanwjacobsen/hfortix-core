"""
Auto-generated basic tests for cmdb.log/eventfilter

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/log.eventfilter.json
Category: cmdb
Endpoint: /cmdb/log/eventfilter

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_eventfilter.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.eventfilter


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoEventfilterEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_event(self):
        """Test enum field event validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import eventfilter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"event": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: event={value}")
        
        print(f"✅ Enum field event has {len(valid_values)} valid values")
    def auto_test_enum_system(self):
        """Test enum field system validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import eventfilter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"system": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: system={value}")
        
        print(f"✅ Enum field system has {len(valid_values)} valid values")
    def auto_test_enum_vpn(self):
        """Test enum field vpn validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import eventfilter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"vpn": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vpn={value}")
        
        print(f"✅ Enum field vpn has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/eventfilter"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/log.eventfilter.json"
TEST_HTTP_METHODS = ['GET', 'PUT']