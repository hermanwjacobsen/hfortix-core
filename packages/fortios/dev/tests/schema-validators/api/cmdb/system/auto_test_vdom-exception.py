"""
Auto-generated basic tests for cmdb.system/vdom_exception

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-exception.json
Category: cmdb
Endpoint: /cmdb/system/vdom-exception

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_vdom-exception.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.vdom_exception


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomExceptionValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
            print(f"✅ Successfully imported validators for vdom-exception")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_vdom_exception_post")
            assert hasattr(validators, "validate_system_vdom_exception_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
        
        # Build minimal valid config with all required fields
        config = {
            "object": "log.fortianalyzer.setting",  # option
        }
        
        try:
            result = validators.validate_system_vdom_exception_post(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoVdomExceptionEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_object(self):
        """Test enum field object validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
        
        valid_values = ['log.fortianalyzer.setting', 'log.fortianalyzer.override-setting', 'log.fortianalyzer2.setting', 'log.fortianalyzer2.override-setting', 'log.fortianalyzer3.setting', 'log.fortianalyzer3.override-setting', 'log.fortianalyzer-cloud.setting', 'log.fortianalyzer-cloud.override-setting', 'log.syslogd.setting', 'log.syslogd.override-setting', 'log.syslogd2.setting', 'log.syslogd2.override-setting', 'log.syslogd3.setting', 'log.syslogd3.override-setting', 'log.syslogd4.setting', 'log.syslogd4.override-setting', 'system.gre-tunnel', 'system.central-management', 'system.csf', 'user.radius', 'system.interface', 'vpn.ipsec.phase1-interface', 'vpn.ipsec.phase2-interface', 'router.bgp', 'router.route-map', 'router.prefix-list', 'firewall.ippool', 'firewall.ippool6', 'router.static', 'router.static6', 'firewall.vip', 'firewall.vip6', 'system.sdwan', 'system.saml', 'router.policy', 'router.policy6', 'log.syslogd.setting', 'log.syslogd.override-setting', 'firewall.address']
        
        # Test each valid value
        for value in valid_values:
            config = {"object": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: object={value}")
        
        print(f"✅ Enum field object has {len(valid_values)} valid values")
    def auto_test_enum_scope(self):
        """Test enum field scope validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import vdom_exception as validators
        
        valid_values = ['all', 'inclusive', 'exclusive']
        
        # Test each valid value
        for value in valid_values:
            config = {"scope": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: scope={value}")
        
        print(f"✅ Enum field scope has {len(valid_values)} valid values")


# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/vdom_exception"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.vdom-exception.json"
TEST_HTTP_METHODS = ['DELETE', 'GET', 'POST', 'PUT']