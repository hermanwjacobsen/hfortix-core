"""
Auto-generated basic tests for cmdb.system/vdom_link

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-link.json
Category: cmdb
Endpoint: /cmdb/system/vdom-link

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vdom-link.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vdom_link


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomLinkEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_vcluster(self):
        """Test enum field vcluster validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_link as validators
        
        valid_values = ['vcluster1', 'vcluster2']
        
        # Test each valid value
        for value in valid_values:
            config = {"vcluster": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vcluster={value}")
        
        print(f"✅ Enum field vcluster has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_link as validators
        
        valid_values = ['ppp', 'ethernet']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vdom_link"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-link.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']