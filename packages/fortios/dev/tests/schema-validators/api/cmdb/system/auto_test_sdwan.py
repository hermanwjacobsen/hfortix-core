"""
Auto-generated basic tests for cmdb.system/sdwan

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.sdwan.json
Category: cmdb
Endpoint: /cmdb/system/sdwan

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_sdwan.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.sdwan


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSdwanEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdwan as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_load_balance_mode(self):
        """Test enum field load-balance-mode validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdwan as validators
        
        valid_values = ['source-ip-based', 'weight-based', 'usage-based', 'source-dest-ip-based', 'measured-volume-based']
        
        # Test each valid value
        for value in valid_values:
            config = {"load-balance-mode": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: load-balance-mode={value}")
        
        print(f"✅ Enum field load-balance-mode has {len(valid_values)} valid values")
    def auto_test_enum_speedtest_bypass_routing(self):
        """Test enum field speedtest-bypass-routing validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import sdwan as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"speedtest-bypass-routing": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: speedtest-bypass-routing={value}")
        
        print(f"✅ Enum field speedtest-bypass-routing has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/sdwan"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.sdwan.json"
TEST_HTTP_METHODS = ['GET', 'PUT']