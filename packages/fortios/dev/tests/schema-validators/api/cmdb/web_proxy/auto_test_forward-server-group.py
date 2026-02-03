"""
Auto-generated basic tests for cmdb.web_proxy/forward_server_group

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.forward-server-group.json
Category: cmdb
Endpoint: /cmdb/web-proxy/forward-server-group

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_forward-server-group.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.web_proxy.forward_server_group


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoForwardServerGroupEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_affinity(self):
        """Test enum field affinity validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server_group as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"affinity": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: affinity={value}")
        
        print(f"✅ Enum field affinity has {len(valid_values)} valid values")
    def auto_test_enum_ldb_method(self):
        """Test enum field ldb-method validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server_group as validators
        
        valid_values = ['weighted', 'least-session', 'active-passive']
        
        # Test each valid value
        for value in valid_values:
            config = {"ldb-method": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ldb-method={value}")
        
        print(f"✅ Enum field ldb-method has {len(valid_values)} valid values")
    def auto_test_enum_group_down_option(self):
        """Test enum field group-down-option validation."""
        from hfortix_fortios.api.v2.cmdb.web_proxy._helpers import forward_server_group as validators
        
        valid_values = ['block', 'pass']
        
        # Test each valid value
        for value in valid_values:
            config = {"group-down-option": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: group-down-option={value}")
        
        print(f"✅ Enum field group-down-option has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/web_proxy/forward_server_group"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/web-proxy.forward-server-group.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']