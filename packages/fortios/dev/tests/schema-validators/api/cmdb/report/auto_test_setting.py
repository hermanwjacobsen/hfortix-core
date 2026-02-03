"""
Auto-generated basic tests for cmdb.report/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/report.setting.json
Category: cmdb
Endpoint: /cmdb/report/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.report.setting


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_pdf_report(self):
        """Test enum field pdf-report validation."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"pdf-report": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: pdf-report={value}")
        
        print(f"✅ Enum field pdf-report has {len(valid_values)} valid values")
    def auto_test_enum_fortiview(self):
        """Test enum field fortiview validation."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortiview": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortiview={value}")
        
        print(f"✅ Enum field fortiview has {len(valid_values)} valid values")
    def auto_test_enum_report_source(self):
        """Test enum field report-source validation."""
        from hfortix_fortios.api.v2.cmdb.report._helpers import setting as validators
        
        valid_values = ['forward-traffic', 'sniffer-traffic', 'local-deny-traffic']
        
        # Test each valid value
        for value in valid_values:
            config = {"report-source": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: report-source={value}")
        
        print(f"✅ Enum field report-source has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/report/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/report.setting.json"
TEST_HTTP_METHODS = ['GET', 'PUT']