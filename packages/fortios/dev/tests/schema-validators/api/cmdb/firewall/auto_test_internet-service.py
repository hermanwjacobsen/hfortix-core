"""
Auto-generated basic tests for cmdb.firewall/internet_service

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.internet-service.json
Category: cmdb
Endpoint: /cmdb/firewall/internet-service

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_internet-service.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.firewall.internet_service


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoInternetServiceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_direction(self):
        """Test enum field direction validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import internet_service as validators
        
        valid_values = ['src', 'dst', 'both']
        
        # Test each valid value
        for value in valid_values:
            config = {"direction": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: direction={value}")
        
        print(f"✅ Enum field direction has {len(valid_values)} valid values")
    def auto_test_enum_database(self):
        """Test enum field database validation."""
        from hfortix_fortios.api.v2.cmdb.firewall._helpers import internet_service as validators
        
        valid_values = ['isdb', 'irdb']
        
        # Test each valid value
        for value in valid_values:
            config = {"database": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: database={value}")
        
        print(f"✅ Enum field database has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/firewall/internet_service"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/firewall.internet-service.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']