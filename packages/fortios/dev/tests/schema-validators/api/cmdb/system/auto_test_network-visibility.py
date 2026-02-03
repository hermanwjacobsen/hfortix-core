"""
Auto-generated basic tests for cmdb.system/network_visibility

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.network-visibility.json
Category: cmdb
Endpoint: /cmdb/system/network-visibility

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_network-visibility.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.network_visibility


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoNetworkVisibilityEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_destination_visibility(self):
        """Test enum field destination-visibility validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import network_visibility as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"destination-visibility": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: destination-visibility={value}")
        
        print(f"✅ Enum field destination-visibility has {len(valid_values)} valid values")
    def auto_test_enum_source_location(self):
        """Test enum field source-location validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import network_visibility as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"source-location": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: source-location={value}")
        
        print(f"✅ Enum field source-location has {len(valid_values)} valid values")
    def auto_test_enum_destination_hostname_visibility(self):
        """Test enum field destination-hostname-visibility validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import network_visibility as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"destination-hostname-visibility": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: destination-hostname-visibility={value}")
        
        print(f"✅ Enum field destination-hostname-visibility has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/network_visibility"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.network-visibility.json"
TEST_HTTP_METHODS = ['GET', 'PUT']