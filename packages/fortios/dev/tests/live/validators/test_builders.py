"""
Tests for hfortix_fortios builders.

Tests build_cmdb_payload, build_cmdb_payload_normalized, and build_api_payload functions.
"""

from hfortix_fortios._helpers.builders import (
    build_cmdb_payload,
    build_cmdb_payload_normalized,
    build_api_payload,
)


# ============================================================================
# build_cmdb_payload tests
# ============================================================================

def test_build_cmdb_payload_basic():
    """Test basic payload building."""
    result = build_cmdb_payload(name="test", status="enable")
    assert result == {"name": "test", "status": "enable"}
    print("✅ build_cmdb_payload - basic")


def test_build_cmdb_payload_snake_to_kebab():
    """Test snake_case to kebab-case conversion."""
    result = build_cmdb_payload(
        interface_name="port1",
        allow_access="ping https",
        vdom_name="root"
    )
    assert result == {
        "interface-name": "port1",
        "allow-access": "ping https",
        "vdom-name": "root"
    }
    print("✅ build_cmdb_payload - snake_case to kebab-case")


def test_build_cmdb_payload_filters_none():
    """Test that None values are filtered out."""
    result = build_cmdb_payload(
        name="test",
        comment=None,
        status="enable",
        description=None
    )
    assert result == {"name": "test", "status": "enable"}
    print("✅ build_cmdb_payload - filters None values")


def test_build_cmdb_payload_keeps_zero():
    """Test that zero values are kept."""
    result = build_cmdb_payload(name="test", priority=0, count=0)
    assert result == {"name": "test", "priority": 0, "count": 0}
    print("✅ build_cmdb_payload - keeps zero")


def test_build_cmdb_payload_keeps_empty_string():
    """Test that empty strings are kept."""
    result = build_cmdb_payload(name="test", comment="")
    assert result == {"name": "test", "comment": ""}
    print("✅ build_cmdb_payload - keeps empty string")


def test_build_cmdb_payload_keeps_false():
    """Test that False values are kept."""
    result = build_cmdb_payload(name="test", enabled=False)
    assert result == {"name": "test", "enabled": False}
    print("✅ build_cmdb_payload - keeps False")


def test_build_cmdb_payload_data_dict_merge():
    """Test that 'data' dict is merged into payload."""
    result = build_cmdb_payload(
        name="test",
        data={"extra-field": "value", "name": "override"}
    )
    # data should be merged and override existing keys
    assert result == {"name": "override", "extra-field": "value"}
    print("✅ build_cmdb_payload - data dict merge")


def test_build_cmdb_payload_empty():
    """Test empty payload."""
    result = build_cmdb_payload()
    assert result == {}
    print("✅ build_cmdb_payload - empty")


def test_build_cmdb_payload_all_none():
    """Test all None values."""
    result = build_cmdb_payload(a=None, b=None, c=None)
    assert result == {}
    print("✅ build_cmdb_payload - all None")


# ============================================================================
# build_cmdb_payload_normalized tests
# ============================================================================

def test_build_cmdb_payload_normalized_basic():
    """Test basic normalized payload building."""
    result = build_cmdb_payload_normalized(name="test", status="enable")
    assert result == {"name": "test", "status": "enable"}
    print("✅ build_cmdb_payload_normalized - basic")


def test_build_cmdb_payload_normalized_member_string():
    """Test normalizing member field from string."""
    result = build_cmdb_payload_normalized(name="group1", member="addr1")
    assert result == {"name": "group1", "member": [{"name": "addr1"}]}
    print("✅ build_cmdb_payload_normalized - member string")


def test_build_cmdb_payload_normalized_member_list():
    """Test normalizing member field from list."""
    result = build_cmdb_payload_normalized(name="group1", member=["addr1", "addr2"])
    assert result == {
        "name": "group1",
        "member": [{"name": "addr1"}, {"name": "addr2"}]
    }
    print("✅ build_cmdb_payload_normalized - member list")


def test_build_cmdb_payload_normalized_srcintf():
    """Test normalizing srcintf field."""
    result = build_cmdb_payload_normalized(srcintf="port1", dstintf="port2")
    assert result == {
        "srcintf": [{"name": "port1"}],
        "dstintf": [{"name": "port2"}]
    }
    print("✅ build_cmdb_payload_normalized - srcintf/dstintf")


def test_build_cmdb_payload_normalized_interface():
    """Test normalizing interface field."""
    result = build_cmdb_payload_normalized(name="test", interface=["eth0", "eth1"])
    assert result == {
        "name": "test",
        "interface": [{"name": "eth0"}, {"name": "eth1"}]
    }
    print("✅ build_cmdb_payload_normalized - interface list")


def test_build_cmdb_payload_normalized_non_normalized_field():
    """Test that non-normalized fields pass through."""
    result = build_cmdb_payload_normalized(
        name="test",
        comment="my comment",
        member="addr1"
    )
    assert result == {
        "name": "test",
        "comment": "my comment",
        "member": [{"name": "addr1"}]
    }
    print("✅ build_cmdb_payload_normalized - non-normalized fields passthrough")


def test_build_cmdb_payload_normalized_custom_fields():
    """Test custom normalize_fields parameter."""
    result = build_cmdb_payload_normalized(
        normalize_fields={"custom_field"},
        name="test",
        custom_field="value1"
    )
    assert result == {
        "name": "test",
        "custom-field": [{"name": "value1"}]
    }
    print("✅ build_cmdb_payload_normalized - custom normalize fields")


def test_build_cmdb_payload_normalized_empty_normalization_result():
    """Test that empty normalization results are not added."""
    result = build_cmdb_payload_normalized(name="test", member=None)
    assert result == {"name": "test"}
    print("✅ build_cmdb_payload_normalized - empty normalization skipped")


# ============================================================================
# build_api_payload tests
# ============================================================================

def test_build_api_payload_basic():
    """Test basic API payload building."""
    result = build_api_payload(name="test", status="enable")
    assert result == {"name": "test", "status": "enable"}
    print("✅ build_api_payload - basic")


def test_build_api_payload_auto_normalize():
    """Test auto-normalization of common fields."""
    result = build_api_payload(
        srcaddr="addr1",
        dstaddr="addr2",
        service="HTTP"
    )
    assert result == {
        "srcaddr": [{"name": "addr1"}],
        "dstaddr": [{"name": "addr2"}],
        "service": [{"name": "HTTP"}]
    }
    print("✅ build_api_payload - auto normalize common fields")


def test_build_api_payload_disable_auto_normalize():
    """Test disabling auto-normalization."""
    result = build_api_payload(
        auto_normalize=False,
        srcaddr="addr1",
        dstaddr="addr2"
    )
    assert result == {
        "srcaddr": "addr1",
        "dstaddr": "addr2"
    }
    print("✅ build_api_payload - auto normalize disabled")


def test_build_api_payload_explicit_normalize_fields():
    """Test explicit normalize_fields parameter."""
    result = build_api_payload(
        normalize_fields={"my_field"},
        my_field="value1",
        srcaddr="addr1"  # Not in normalize_fields
    )
    assert result == {
        "my-field": [{"name": "value1"}],
        "srcaddr": "addr1"
    }
    print("✅ build_api_payload - explicit normalize fields")


def test_build_api_payload_firewall_policy_fields():
    """Test all firewall policy list fields."""
    result = build_api_payload(
        srcintf="port1",
        dstintf="port2",
        srcaddr="all",
        dstaddr="all",
        service="ALL",
        poolname="pool1",
        groups="admin-group",
        users="admin"
    )
    assert "srcintf" in result
    assert "dstintf" in result
    assert "srcaddr" in result
    assert "dstaddr" in result
    assert "service" in result
    assert "poolname" in result
    assert "groups" in result
    assert "users" in result
    # All should be lists of dicts
    for key in ["srcintf", "dstintf", "srcaddr", "dstaddr", "service", "poolname", "groups", "users"]:
        assert isinstance(result[key], list)
        assert isinstance(result[key][0], dict)
    print("✅ build_api_payload - firewall policy fields")


def test_build_api_payload_data_merge():
    """Test data dict merge."""
    result = build_api_payload(
        name="test",
        data={"extra": "value"}
    )
    assert result == {"name": "test", "extra": "value"}
    print("✅ build_api_payload - data merge")


def test_build_api_payload_snake_to_kebab():
    """Test snake_case to kebab-case conversion."""
    result = build_api_payload(
        auto_normalize=False,
        internet_service_name="test",
        custom_log_fields="field1"
    )
    assert result == {
        "internet-service-name": "test",
        "custom-log-fields": "field1"
    }
    print("✅ build_api_payload - snake to kebab conversion")


def run_all_tests():
    """Run all builder tests."""
    print("\n" + "=" * 60)
    print("BUILDER TESTS")
    print("=" * 60 + "\n")

    # build_cmdb_payload tests
    test_build_cmdb_payload_basic()
    test_build_cmdb_payload_snake_to_kebab()
    test_build_cmdb_payload_filters_none()
    test_build_cmdb_payload_keeps_zero()
    test_build_cmdb_payload_keeps_empty_string()
    test_build_cmdb_payload_keeps_false()
    test_build_cmdb_payload_data_dict_merge()
    test_build_cmdb_payload_empty()
    test_build_cmdb_payload_all_none()

    # build_cmdb_payload_normalized tests
    test_build_cmdb_payload_normalized_basic()
    test_build_cmdb_payload_normalized_member_string()
    test_build_cmdb_payload_normalized_member_list()
    test_build_cmdb_payload_normalized_srcintf()
    test_build_cmdb_payload_normalized_interface()
    test_build_cmdb_payload_normalized_non_normalized_field()
    test_build_cmdb_payload_normalized_custom_fields()
    test_build_cmdb_payload_normalized_empty_normalization_result()

    # build_api_payload tests
    test_build_api_payload_basic()
    test_build_api_payload_auto_normalize()
    test_build_api_payload_disable_auto_normalize()
    test_build_api_payload_explicit_normalize_fields()
    test_build_api_payload_firewall_policy_fields()
    test_build_api_payload_data_merge()
    test_build_api_payload_snake_to_kebab()

    print("\n" + "=" * 60)
    print("ALL BUILDER TESTS PASSED!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
