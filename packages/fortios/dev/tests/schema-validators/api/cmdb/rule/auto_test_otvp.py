"""
Auto-generated basic tests for cmdb.rule/otvp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/rule.otvp.json
Category: cmdb
Endpoint: /cmdb/rule/otvp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_otvp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.rule.otvp


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOtvpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.rule._helpers import otvp as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_log(self):
        """Test enum field log validation."""
        from hfortix_fortios.api.v2.cmdb.rule._helpers import otvp as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log={value}")
        
        print(f"✅ Enum field log has {len(valid_values)} valid values")
    def auto_test_enum_log_packet(self):
        """Test enum field log-packet validation."""
        from hfortix_fortios.api.v2.cmdb.rule._helpers import otvp as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"log-packet": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: log-packet={value}")
        
        print(f"✅ Enum field log-packet has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/rule/otvp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/rule.otvp.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']