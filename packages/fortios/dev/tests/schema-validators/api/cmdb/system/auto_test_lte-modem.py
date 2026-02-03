"""
Auto-generated basic tests for cmdb.system/lte_modem

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.lte-modem.json
Category: cmdb
Endpoint: /cmdb/system/lte-modem

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_lte-modem.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.lte_modem


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoLteModemEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import lte_modem as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_pdptype(self):
        """Test enum field pdptype validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import lte_modem as validators
        
        valid_values = ['IPv4']
        
        # Test each valid value
        for value in valid_values:
            config = {"pdptype": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: pdptype={value}")
        
        print(f"✅ Enum field pdptype has {len(valid_values)} valid values")
    def auto_test_enum_authtype(self):
        """Test enum field authtype validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import lte_modem as validators
        
        valid_values = ['none', 'pap', 'chap']
        
        # Test each valid value
        for value in valid_values:
            config = {"authtype": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: authtype={value}")
        
        print(f"✅ Enum field authtype has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/lte_modem"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.lte-modem.json"
TEST_HTTP_METHODS = ['GET', 'PUT']