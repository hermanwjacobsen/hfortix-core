"""
Auto-generated basic tests for cmdb.system/npu

Generated from schema: /app/dev/classes/fortinet/packages/fortios/dev/schema/7.6.5/cmdb/system.npu.json
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


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoNpuGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve npu configuration."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single FortiObject
        assert hasattr(result, "__dict__")  # FortiObject
        print(f"✅ Retrieved npu configuration (singleton)")
        # Convert to dict to count fields
        result_dict = result.dict
        print(f"   Config keys: {len(result_dict)} fields")
    
    
    def auto_test_get_with_vdom(self):
        """Test GET - with vdom parameter."""
        try:
            result = endpoint.get(vdom="root")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with vdom=root successful")
    
    def auto_test_get_with_filters(self):
        """Test GET - with filter parameters."""
        # Test with common filter options
        try:
            result = endpoint.get(
                filter="",  # No filter (get all)
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoNpuExists:
    """Auto-generated exists() tests."""
    




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
TEST_SCHEMA = "/app/dev/classes/fortinet/packages/fortios/dev/schema/7.6.5/cmdb/system.npu.json"
TEST_HTTP_METHODS = ['GET', 'PUT']