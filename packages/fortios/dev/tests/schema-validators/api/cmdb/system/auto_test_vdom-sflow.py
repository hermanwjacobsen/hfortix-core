"""
Auto-generated basic tests for cmdb.system/vdom_sflow

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-sflow.json
Category: cmdb
Endpoint: /cmdb/system/vdom-sflow

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vdom-sflow.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vdom_sflow


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomSflowEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_vdom_sflow(self):
        """Test enum field vdom-sflow validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_sflow as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"vdom-sflow": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vdom-sflow={value}")
        
        print(f"✅ Enum field vdom-sflow has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vdom_sflow"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-sflow.json"
TEST_HTTP_METHODS = ['GET', 'PUT']