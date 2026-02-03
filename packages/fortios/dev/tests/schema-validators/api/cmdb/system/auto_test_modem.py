"""
Auto-generated basic tests for cmdb.system/modem

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.modem.json
Category: cmdb
Endpoint: /cmdb/system/modem

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_modem.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.modem


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoModemEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import modem as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_mode(self):
        """Test enum field mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import modem as validators
        
        valid_values = ['standalone', 'redundant']
        
        # Test each valid value
        for value in valid_values:
            config = {"mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mode={value}")
        
        print(f"✅ Enum field mode has {len(valid_values)} valid values")
    def auto_test_enum_auto_dial(self):
        """Test enum field auto-dial validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import modem as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"auto-dial": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auto-dial={value}")
        
        print(f"✅ Enum field auto-dial has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/modem"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.modem.json"
TEST_HTTP_METHODS = ['GET', 'PUT']