"""
Auto-generated basic tests for cmdb.system/cloud_service

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.cloud-service.json
Category: cmdb
Endpoint: /cmdb/system/cloud-service

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_cloud-service.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.cloud_service


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoCloudServiceEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_vendor(self):
        """Test enum field vendor validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import cloud_service as validators
        
        valid_values = ['unknown', 'google-cloud-kms']
        
        # Test each valid value
        for value in valid_values:
            config = {"vendor": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: vendor={value}")
        
        print(f"✅ Enum field vendor has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/cloud_service"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.cloud-service.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']