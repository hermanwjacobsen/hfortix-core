"""
Auto-generated basic tests for cmdb.vpn/certificate/ocsp_server

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.certificate.ocsp-server.json
Category: cmdb
Endpoint: /cmdb/vpn.certificate/ocsp-server

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ocsp-server.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.vpn.certificate.ocsp_server


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoOcspServerEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_unavail_action(self):
        """Test enum field unavail-action validation."""
        from hfortix_fortios.api.v2.cmdb.vpn.certificate._helpers import ocsp_server as validators
        
        valid_values = ['revoke', 'ignore']
        
        # Test each valid value
        for value in valid_values:
            config = {"unavail-action": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: unavail-action={value}")
        
        print(f"✅ Enum field unavail-action has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/vpn/certificate/ocsp_server"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/vpn.certificate.ocsp-server.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']