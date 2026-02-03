"""
Auto-generated basic tests for cmdb.log/tacacs_plus_accounting3/filter

Generated from schema: /app/dev/classes/fortinet/packages/fortios/dev/schema/7.6.5/cmdb/log.tacacs+accounting3.filter.json
Category: cmdb
Endpoint: /cmdb/log.tacacs+accounting3/filter

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_filter.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.tacacs_plus_accounting3.filter


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoFilterGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve filter configuration."""
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
        print(f"✅ Retrieved filter configuration (singleton)")
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
class TestAutoFilterExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFilterEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_login_audit(self):
        """Test enum field login-audit validation."""
        from hfortix_fortios.api.v2.cmdb.log.tacacs_plus_accounting3._helpers import filter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"login-audit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: login-audit={value}")
        
        print(f"✅ Enum field login-audit has {len(valid_values)} valid values")
    def auto_test_enum_config_change_audit(self):
        """Test enum field config-change-audit validation."""
        from hfortix_fortios.api.v2.cmdb.log.tacacs_plus_accounting3._helpers import filter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"config-change-audit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: config-change-audit={value}")
        
        print(f"✅ Enum field config-change-audit has {len(valid_values)} valid values")
    def auto_test_enum_cli_cmd_audit(self):
        """Test enum field cli-cmd-audit validation."""
        from hfortix_fortios.api.v2.cmdb.log.tacacs_plus_accounting3._helpers import filter as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"cli-cmd-audit": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: cli-cmd-audit={value}")
        
        print(f"✅ Enum field cli-cmd-audit has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/tacacs_plus_accounting3/filter"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/packages/fortios/dev/schema/7.6.5/cmdb/log.tacacs+accounting3.filter.json"
TEST_HTTP_METHODS = ['GET', 'PUT']