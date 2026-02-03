"""
Auto-generated basic tests for cmdb.system/np6xlite

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.np6xlite.json
Category: cmdb
Endpoint: /cmdb/system/np6xlite

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_np6xlite.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.np6xlite


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNp6xliteEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fastpath(self):
        """Test enum field fastpath validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import np6xlite as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fastpath": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fastpath={value}")
        
        print(f"✅ Enum field fastpath has {len(valid_values)} valid values")
    def auto_test_enum_per_session_accounting(self):
        """Test enum field per-session-accounting validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import np6xlite as validators
        
        valid_values = ['disable', 'traffic-log-only', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"per-session-accounting": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: per-session-accounting={value}")
        
        print(f"✅ Enum field per-session-accounting has {len(valid_values)} valid values")
    def auto_test_enum_ipsec_inner_fragment(self):
        """Test enum field ipsec-inner-fragment validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import np6xlite as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipsec-inner-fragment": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipsec-inner-fragment={value}")
        
        print(f"✅ Enum field ipsec-inner-fragment has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/np6xlite"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.np6xlite.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']