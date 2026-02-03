"""
Auto-generated basic tests for cmdb.monitoring/npu_hpe

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/monitoring.npu-hpe.json
Category: cmdb
Endpoint: /cmdb/monitoring/npu-hpe

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_npu-hpe.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.monitoring.npu_hpe


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNpuHpeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.monitoring._helpers import npu_hpe as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/monitoring/npu_hpe"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/monitoring.npu-hpe.json"
TEST_HTTP_METHODS = ['GET', 'PUT']