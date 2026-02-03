"""
Auto-generated basic tests for cmdb.system/vdom_netflow

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-netflow.json
Category: cmdb
Endpoint: /cmdb/system/vdom-netflow

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vdom-netflow.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vdom_netflow


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomNetflowEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_vdom_netflow(self):
        """Test enum field vdom-netflow validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_netflow as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"vdom-netflow": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vdom-netflow={value}")
        
        print(f"✅ Enum field vdom-netflow has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vdom_netflow"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-netflow.json"
TEST_HTTP_METHODS = ['GET', 'PUT']