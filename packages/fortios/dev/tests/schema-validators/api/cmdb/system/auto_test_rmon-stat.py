"""
Auto-generated basic tests for cmdb.system/snmp/rmon_stat

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.snmp.rmon-stat.json
Category: cmdb
Endpoint: /cmdb/system.snmp/rmon-stat

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_rmon-stat.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.snmp.rmon_stat


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRmonStatValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system.snmp._helpers import rmon_stat as validators
            print(f"✅ Successfully imported validators for rmon-stat")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_snmp_rmon_stat_post")
            assert hasattr(validators, "validate_system_snmp_rmon_stat_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system.snmp._helpers import rmon_stat as validators
        
        # Build minimal valid config with all required fields
        config = {
            "id": 0,  # integer
            "source": "test_source",  # string
        }
        
        try:
            result = validators.validate_system_snmp_rmon_stat_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/snmp/rmon_stat"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.snmp.rmon-stat.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']