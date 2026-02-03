"""
Auto-generated basic tests for cmdb.ips/global_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.global.json
Category: cmdb
Endpoint: /cmdb/ips/global

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_global.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.ips.global_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_fail_open(self):
        """Test enum field fail-open validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.ips._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fail-open": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fail-open={value}")
        
        print(f"✅ Enum field fail-open has {len(valid_values)} valid values")
    def auto_test_enum_database(self):
        """Test enum field database validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.ips._helpers.global_')
        
        valid_values = ['regular', 'extended']
        
        # Test each valid value
        for value in valid_values:
            config = {"database": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: database={value}")
        
        print(f"✅ Enum field database has {len(valid_values)} valid values")
    def auto_test_enum_traffic_submit(self):
        """Test enum field traffic-submit validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.ips._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"traffic-submit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: traffic-submit={value}")
        
        print(f"✅ Enum field traffic-submit has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/ips/global_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/ips.global.json"
TEST_HTTP_METHODS = ['GET', 'PUT']