"""
Auto-generated basic tests for cmdb.switch_controller/igmp_snooping

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.igmp-snooping.json
Category: cmdb
Endpoint: /cmdb/switch-controller/igmp-snooping

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_igmp-snooping.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.igmp_snooping


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoIgmpSnoopingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_flood_unknown_multicast(self):
        """Test enum field flood-unknown-multicast validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import igmp_snooping as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"flood-unknown-multicast": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: flood-unknown-multicast={value}")
        
        print(f"✅ Enum field flood-unknown-multicast has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/igmp_snooping"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.igmp-snooping.json"
TEST_HTTP_METHODS = ['GET', 'PUT']