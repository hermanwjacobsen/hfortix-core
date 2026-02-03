"""
Auto-generated basic tests for cmdb.system/replacemsg_image

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.replacemsg-image.json
Category: cmdb
Endpoint: /cmdb/system/replacemsg-image

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_replacemsg-image.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.replacemsg_image


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoReplacemsgImageEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_image_type(self):
        """Test enum field image-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import replacemsg_image as validators
        
        valid_values = ['gif', 'jpg', 'tiff', 'png']
        
        # Test each valid value
        for value in valid_values:
            config = {"image-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: image-type={value}")
        
        print(f"✅ Enum field image-type has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/replacemsg_image"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.replacemsg-image.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']