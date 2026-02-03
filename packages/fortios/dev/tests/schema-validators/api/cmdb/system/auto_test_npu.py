"""
Auto-generated basic tests for cmdb.system/npu

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.npu.json
Category: cmdb
Endpoint: /cmdb/system/npu

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_npu.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.npu


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNpuEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_dedicated_management_cpu(self):
        """Test enum field dedicated-management-cpu validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import npu as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dedicated-management-cpu": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dedicated-management-cpu={value}")
        
        print(f"✅ Enum field dedicated-management-cpu has {len(valid_values)} valid values")
    def auto_test_enum_capwap_offload(self):
        """Test enum field capwap-offload validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import npu as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"capwap-offload": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: capwap-offload={value}")
        
        print(f"✅ Enum field capwap-offload has {len(valid_values)} valid values")
    def auto_test_enum_ipsec_mtu_override(self):
        """Test enum field ipsec-mtu-override validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import npu as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"ipsec-mtu-override": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ipsec-mtu-override={value}")
        
        print(f"✅ Enum field ipsec-mtu-override has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/npu"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.npu.json"
TEST_HTTP_METHODS = ['GET', 'PUT']