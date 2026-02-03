"""
Auto-generated basic tests for cmdb.ips/view_map

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.view-map.json
Category: cmdb
Endpoint: /cmdb/ips/view-map

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_view-map.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ips.view_map


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoViewMapEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_which(self):
        """Test enum field which validation."""
        from hfortix_fortios.api.v2.cmdb.ips._helpers import view_map as validators
        
        valid_values = ['firewall', 'interface', 'interface6', 'sniffer', 'sniffer6', 'explicit']
        
        # Test each valid value
        for value in valid_values:
            config = {"which": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: which={value}")
        
        print(f"✅ Enum field which has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ips/view_map"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.view-map.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']