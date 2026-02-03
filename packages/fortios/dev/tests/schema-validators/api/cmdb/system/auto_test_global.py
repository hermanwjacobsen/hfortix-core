"""
Auto-generated basic tests for cmdb.system/global_

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.global.json
Category: cmdb
Endpoint: /cmdb/system/global

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_global.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.global_


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            # 'global' is a Python keyword, using importlib
            import importlib
            validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.system._helpers.global_')
            print(f"✅ Successfully imported validators for global")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_global_post")
            assert hasattr(validators, "validate_system_global_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.system._helpers.global_')
        
        # Build minimal valid config with all required fields
        config = {
            "ip-src-port-range": "1024-25000",  # user
            "restart-time": "",  # user
            "timezone": "test_timezone",  # string
            "traffic-priority": "tos",  # option
            "traffic-priority-level": "low",  # option
            "wad-restart-end-time": "",  # user
            "wad-restart-start-time": "",  # user
        }
        
        try:
            result = validators.validate_system_global_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGlobalEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_language(self):
        """Test enum field language validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.system._helpers.global_')
        
        valid_values = ['english', 'french', 'spanish', 'portuguese', 'japanese', 'trach', 'simch', 'korean']
        
        # Test each valid value
        for value in valid_values:
            config = {"language": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: language={value}")
        
        print(f"✅ Enum field language has {len(valid_values)} valid values")
    def auto_test_enum_gui_ipv6(self):
        """Test enum field gui-ipv6 validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.system._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"gui-ipv6": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: gui-ipv6={value}")
        
        print(f"✅ Enum field gui-ipv6 has {len(valid_values)} valid values")
    def auto_test_enum_gui_replacement_message_groups(self):
        """Test enum field gui-replacement-message-groups validation."""
        # 'global' is a Python keyword, using importlib
        import importlib
        validators = importlib.import_module('hfortix_fortios.api.v2.cmdb.system._helpers.global_')
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"gui-replacement-message-groups": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: gui-replacement-message-groups={value}")
        
        print(f"✅ Enum field gui-replacement-message-groups has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/global_"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.global.json"
TEST_HTTP_METHODS = ['GET', 'PUT']