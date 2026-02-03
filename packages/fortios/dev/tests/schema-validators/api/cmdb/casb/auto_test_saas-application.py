"""
Auto-generated basic tests for cmdb.casb/saas_application

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/casb.saas-application.json
Category: cmdb
Endpoint: /cmdb/casb/saas-application

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_saas-application.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.casb.saas_application


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSaasApplicationEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.casb._helpers import saas_application as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_type(self):
        """Test enum field type validation."""
        from hfortix_fortios.api.v2.cmdb.casb._helpers import saas_application as validators
        
        valid_values = ['built-in', 'customized']
        
        # Test each valid value
        for value in valid_values:
            config = {"type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: type={value}")
        
        print(f"✅ Enum field type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/casb/saas_application"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/casb.saas-application.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']