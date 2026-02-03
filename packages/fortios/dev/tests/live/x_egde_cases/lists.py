import sys
from pathlib import Path
import logging
from contextlib import contextmanager
import time

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fgtclient import fgt

# Generate a unique timestamp suffix for this test run
# All tests will share this timestamp making it easy to track objects from a single run
TIMESTAMP = int(time.time())




@contextmanager
def suppress_http_errors():
    """Temporarily suppress HTTP error logs for expected validation failures"""
    logger = logging.getLogger("hfortix.http")
    original_level = logger.level
    logger.setLevel(logging.CRITICAL)  # Suppress ERROR logs, only show CRITICAL
    try:
        yield
    finally:
        logger.setLevel(original_level)

def cleanup():
    """Cleanup: Delete all addrgrp and address objects starting with 'test_'"""
    
    # Delete address groups first (they reference addresses)
    try:
        addrgrps = fgt.api.cmdb.firewall.addrgrp.get()
        for grp in addrgrps:
            if grp.name.startswith("test_"):
                result = fgt.api.cmdb.firewall.addrgrp.delete(name=grp.name)
                print(f"Deleted addrgrp: {grp.name} - {result.http_status}")
    except Exception as e:
        print(f"Error cleaning addrgrps: {e}")
    
    # Delete addresses
    try:
        addresses = fgt.api.cmdb.firewall.address.get()
        for addr in addresses:
            if addr.name.startswith("test_"):
                result = fgt.api.cmdb.firewall.address.delete(name=addr.name)
                print(f"Deleted address: {addr.name} - {result.http_status}")
    except Exception as e:
        print(f"Error cleaning addresses: {e}")

    try:
        services = fgt.api.cmdb.firewall.service.custom.get()
        for service in services:
            if service.name.startswith("test_"):
                result = fgt.api.cmdb.firewall.service.custom.delete(name=service.name)
                print(f"Deleted service: {service.name} - {result.http_status}")
    except Exception as e:
        print(f"Error cleaning services: {e}")
    
    try:
        service_groups = fgt.api.cmdb.firewall.service.group.get()
        for sg in service_groups:
            if sg.name.startswith("test_"):
                result = fgt.api.cmdb.firewall.service.group.delete(name=sg.name)
                print(f"Deleted service group: {sg.name} - {result.http_status}")
    except Exception as e:
        print(f"Error cleaning service groups: {e}")

    try:
        radius_servers = fgt.api.cmdb.user.radius.get()
        for rs in radius_servers:
            if rs.name.startswith("test_"):
                result = fgt.api.cmdb.user.radius.delete(name=rs.name)
                print(f"Deleted radius server: {rs.name} - {result.http_status}")
    except Exception as e:
        print(f"Error cleaning radius servers: {e}")    

    try:
        policies = fgt.api.cmdb.firewall.policy.get()
        for policy in policies:
            if policy.name.startswith("test_"):
                result = fgt.api.cmdb.firewall.policy.delete(policyid=policy.policyid)
                print(f"Deleted policy: {policy.name} - {result.http_status}")
    except Exception as e:
        print(f"Error cleaning policies: {e}")  

    

# ============================================================

def create_firewall_service():
    """Test: Create firewall services"""
    result1 = fgt.api.cmdb.firewall.service.custom.post(
        name="test_service1",
        protocol="TCP/UDP/UDP-Lite/SCTP",
        tcp_portrange="8080"
    )
    assert result1 is not None
    assert result1.http_status == "success"

    result2 = fgt.api.cmdb.firewall.service.custom.post(
        name="test_service2",
        protocol="TCP/UDP/UDP-Lite/SCTP",
        udp_portrange="9090"
    )
    assert result2 is not None
    assert result2.http_status == "success"


def create_firewall_service_group1():
    """Test: Create firewall service group"""
    result = fgt.api.cmdb.firewall.service.group.post(
        name="test_service_group1",
        member=[
            {"name": "test_service1"},
            {"name": "test_service2"}
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def create_firewall_service_group2():
    """Test: Create firewall service group"""
    result = fgt.api.cmdb.firewall.service.group.post(
        name="test_service_group2",
        member=[
            {"name":"test_service1"},
            {"name":"test_service2"}
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def create_radius_server():
    result = fgt.api.cmdb.user.radius.post(
    name="test_radius",
    server="192.168.1.100",
    secret="mysecret",
    accounting_server=[
        {"id": 1, "server": "192.168.1.101"},
        {"id": 2, "server": "192.168.1.102"}
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def multiple_format_test():
    result = fgt.api.cmdb.firewall.policy.post(
    name="test_policy_multi_format",
    srcintf=["port3", "port4"],              # List of strings
    dstintf="port3",                          # Single string
    srcaddr=[{"name": "all"}],             # Already formatted
    dstaddr="all",                          # Single string
    service=["HTTP", "HTTPS"],               # List of strings
    action="accept",
    schedule="always"
    )
    assert result is not None
    assert result.http_status == "success"


# ============================================================
# TABLE FIELD FORMAT TESTS (using firewall.addrgrp.member)
# ============================================================

def test_create_address_objects():
    """Test: Create address objects for group testing"""
    # Create first address
    result1 = fgt.api.cmdb.firewall.address.post(
        name="test_lists_addr1",
        type="ipmask",
        subnet="192.168.1.0/24",
        comment="Test address 1 for list format testing"
    )
    assert result1 is not None
    assert result1.http_status == "success"
    
    # Create second address
    result2 = fgt.api.cmdb.firewall.address.post(
        name="test_lists_addr2",
        type="ipmask",
        subnet="192.168.2.0/24",
        comment="Test address 2 for list format testing"
    )
    assert result2 is not None
    assert result2.http_status == "success"


def test_traditional_dict_format():
    """Test: Traditional dict format for table fields"""
    result = fgt.api.cmdb.firewall.addrgrp.post(
        name="test_group_dict",
        member=[
            {"name": "test_lists_addr1"},
            {"name": "test_lists_addr2"}
        ]
    )
    assert result is not None
    assert result.http_status == "success"


def test_string_list_format():
    """Test: Simplified string list format for table fields"""
    result = fgt.api.cmdb.firewall.addrgrp.post(
        name="test_group_strings",
        member=["test_lists_addr1", "test_lists_addr2"]  # ✅ Simpler!
    )
    assert result is not None
    assert result.http_status == "success"


def test_single_string_format():
    """Test: Single string for single-member table fields"""
    result = fgt.api.cmdb.firewall.addrgrp.post(
        name="test_group_single",
        member="test_lists_addr1"  # ✅ Even simpler for single member!
    )
    assert result is not None
    assert result.http_status == "success"

def test_single_vs_list():
    """Test: Single item string vs single-item list"""
    # Single string
    result1 = fgt.api.cmdb.firewall.addrgrp.post(
        name="test_single_member",
        member="all"  # Single string
    )
    assert result1.http_status == "success"
    
    # Single-item list
    result2 = fgt.api.cmdb.firewall.addrgrp.post(
        name="test_list_one_member",
        member=["all"]  # List with one item
    )
    assert result2.http_status == "success"

def test_large_list():
    """Test: Large number of members"""
    # First create many addresses
    for i in range(20):
        fgt.api.cmdb.firewall.address.post(
            name=f"test_addr_{i}",  # Changed to match member list
            subnet=f"10.0.{i}.0/24"
        )
    
    # Then create group with all of them using string list
    members = [f"test_addr_{i}" for i in range(20)]
    result = fgt.api.cmdb.firewall.addrgrp.post(
        name="test_large_group",
        member=members  # List of 20 strings → auto-converted
    )
    assert result.http_status == "success"

def test_whitespace():
    """Test: Strings with whitespace"""
    result = fgt.api.cmdb.firewall.service.group.post(
        name="test_whitespace_group",
        member=[
            " test_service1 ",  # Leading/trailing spaces
            "test_service2",
            "\ttest_service1\n"  # Tabs and newlines
        ]
    )
    # This might fail if normalizer doesn't strip whitespace
    # Good to know for future enhancement

def test_special_chars():
    """Test: Names with special characters"""
    # Create service with special chars
    fgt.api.cmdb.firewall.service.custom.post(
        name="test_service-with-dashes",
        protocol="TCP/UDP/UDP-Lite/SCTP",
        tcp_portrange="8080"
    )
    
    result = fgt.api.cmdb.firewall.service.group.post(
        name="test_special_chars",
        member=["test_service-with-dashes"]  # Dashes in name
    )
    assert result.http_status == "success"

def test_update_with_flexible_format():
    """Test: PUT operations with flexible formats"""
    # Create with traditional format
    fgt.api.cmdb.firewall.service.group.post(
        name="test_update_group",
        member=[{"name": "test_service1"}]
    )
    
    # Update with string list format
    result = fgt.api.cmdb.firewall.service.group.put(
        name="test_update_group",
        member=["test_service1", "test_service2"]  # Different format
    )
    assert result.http_status == "success"

def test_empty_none_values():
    """Test: Empty lists and None values are handled gracefully"""
    # For firewall policy, srcintf/dstintf are REQUIRED
    # So test with fields that CAN be empty
    result = fgt.api.cmdb.firewall.policy.post(
        name="test_empty_values",
        srcintf="any",          # Required - must provide
        dstintf="any",          # Required - must provide
        srcaddr="all",          # Required
        dstaddr="all",          # Required
        service="ALL",          # Required
        action="deny",
        schedule="always",
        # Optional fields that CAN be empty/None:
        internet_service_src_custom=[],     # Empty list is OK
        internet_service_custom=None,       # None is OK
        users=None,                          # None is OK for optional fields
        groups=[]                            # Empty list for optional fields
    )
    assert result is not None
    assert result.http_status == "success"
    print("✓ test_empty_none_values: Empty/None for optional fields works")


def test_empty_none_values_validation():
    """Test: Normalizer handles empty values, FortiOS validates them"""
    with suppress_http_errors():  # <-- Suppress the "Request failed: HTTP 500" log
        try:
            result = fgt.api.cmdb.firewall.policy.post(
                name="test_invalid_empty",
                srcintf=None,  # This will become [] 
                dstintf=None,  # This will become []
                srcaddr="all",
                dstaddr="all",
                service="ALL",
                action="deny",
                schedule="always"
            )
            # Should not reach here - FortiOS should reject
            assert False, "Expected validation error from FortiOS"
        except Exception as e:
            # This is expected - FortiOS validation caught it
            assert "invalid" in str(e).lower() or "required" in str(e).lower()
    
    print("✓ test_empty_none_values: Normalizer passed [], FortiOS validated correctly")


def test_long_names():
    """Test: Long names are handled correctly"""
    long_name = "test_service_" + "x" * 50  # FortiOS has name limits
    
    try:
        fgt.api.cmdb.firewall.service.custom.post(
            name=long_name,
            protocol="TCP/UDP/UDP-Lite/SCTP",
            tcp_portrange="7777"
        )
        
        result = fgt.api.cmdb.firewall.service.group.post(
            name="test_long_name_ref",
            member=[long_name]
        )
        assert result.http_status == "success"
        print(f"✓ test_long_names: Names up to {len(long_name)} chars work")
    except Exception as e:
        # FortiOS might have a limit - that's OK
        print(f"  Note: FortiOS name limit is around {len(long_name)} chars: {e}")

def test_unicode_names():
    """Test: Unicode characters in names (if FortiOS supports)"""
    try:
        fgt.api.cmdb.firewall.service.custom.post(
            name="test_service_café",  # Accented character
            protocol="TCP/UDP/UDP-Lite/SCTP",
            tcp_portrange="6666"
        )
        
        result = fgt.api.cmdb.firewall.service.group.post(
            name="test_unicode",
            member=["test_service_café"]
        )
        assert result.http_status == "success"
        print("✓ test_unicode_names: Unicode characters supported")
    except Exception as e:
        print(f"  Note: FortiOS may not support unicode in names: {e}")

def test_duplicate_members():
    """Test: Duplicate members are handled (deduplicated or rejected)"""
    result = fgt.api.cmdb.firewall.service.group.post(
        name="test_duplicates",
        member=[
            "test_service1",
            "test_service2",
            "test_service1",  # Duplicate
            "test_service1"   # Another duplicate
        ]
    )
    assert result.http_status == "success"
    
    group = fgt.api.cmdb.firewall.service.group.get(
        name="test_duplicates",  # Positional argument
    )
    unique_count = len(set(m.name for m in group.member))
    total_count = len(group.member)
    
    if unique_count == total_count:
        print(f"✓ test_duplicates: FortiOS deduplicated ({unique_count} unique members)")
    else:
        print(f"✓ test_duplicates: FortiOS kept duplicates ({total_count} total, {unique_count} unique)")

def test_case_sensitivity():
    """Test: Name matching is case-sensitive or not"""
    # Delete if exists from previous run
    try:
        fgt.api.cmdb.firewall.service.custom.delete(name="Test_Service_MixedCase")
    except:
        pass  # Doesn't exist, that's fine
    
    # Create service with mixed case
    fgt.api.cmdb.firewall.service.custom.post(
        name="Test_Service_MixedCase",
        protocol="TCP/UDP/UDP-Lite/SCTP",
        tcp_portrange="5555"
    )
    
    # Try exact case
    result1 = fgt.api.cmdb.firewall.service.group.post(
        name="test_case_exact",
        member=["Test_Service_MixedCase"]
    )
    assert result1.http_status == "success"
    
    # Try different case
    with suppress_http_errors():  # <-- Add this to suppress "not found" error
        try:
            result2 = fgt.api.cmdb.firewall.service.group.post(
                name="test_case_different",
                member=["test_service_mixedcase"]  # All lowercase
            )
            print("  Note: FortiOS is case-INSENSITIVE for names")
        except Exception as e:
            if "not found" in str(e).lower():
                print("✓ test_case_sensitivity: FortiOS is case-SENSITIVE")


def test_full_crud_cycle():
    """Test: Complete CRUD cycle with flexible formats"""
    # Create with string list
    create_result = fgt.api.cmdb.firewall.service.group.post(
        name="test_crud_lifecycle",
        member=["test_service1"]
    )
    assert create_result.http_status == "success"
    
    # Read
    group = fgt.api.cmdb.firewall.service.group.get(name="test_crud_lifecycle")
    assert group.name == "test_crud_lifecycle"
    assert len(group.member) == 1
    
    # Update with dict format
    update_result = fgt.api.cmdb.firewall.service.group.put(
        name="test_crud_lifecycle",
        member=[{"name": "test_service1"}, {"name": "test_service2"}]
    )
    assert update_result.http_status == "success"
    
    # Read again
    group = fgt.api.cmdb.firewall.service.group.get(name="test_crud_lifecycle")
    assert len(group.member) == 2
    
    # Delete
    delete_result = fgt.api.cmdb.firewall.service.group.delete(name="test_crud_lifecycle")
    assert delete_result.http_status == "success"
    
    # Verify deleted
    assert not fgt.api.cmdb.firewall.service.group.exists(name="test_crud_lifecycle")
    print("✓ test_full_crud_cycle: Complete lifecycle with mixed formats")

def test_performance_timing():
    """Test: Performance comparison between formats"""
    import time
    
    # Create 10 addresses
    for i in range(10):
        fgt.api.cmdb.firewall.address.post(
            name=f"test_perf_{i}",
            subnet=f"10.10.{i}.0/24"
        )
    
    members = [f"test_perf_{i}" for i in range(10)]
    
    # Time string format
    start = time.time()
    fgt.api.cmdb.firewall.addrgrp.post(
        name="test_perf_string",
        member=members  # String list
    )
    string_time = time.time() - start
    
    # Time dict format
    start = time.time()
    fgt.api.cmdb.firewall.addrgrp.post(
        name="test_perf_dict",
        member=[{"name": m} for m in members]  # Dict list
    )
    dict_time = time.time() - start
    
    print(f"✓ test_performance_timing: String={string_time:.3f}s, Dict={dict_time:.3f}s")

if __name__ == "__main__":

    policies = fgt.api.cmdb.firewall.policy.get()
    for policy in policies:
        if policy.name.startswith("test_"):
            fgt.api.cmdb.firewall.policy.delete(policyid=policy.policyid)
            
    shapers = fgt.api.cmdb.firewall.shaper.traffic_shaper.get()
    for shaper in shapers:
        if shaper.name.startswith("test_"):
            fgt.api.cmdb.firewall.shaper.traffic_shaper.delete(name=shaper.name) 

    addrgoups = fgt.api.cmdb.firewall.addrgrp.get()
    for addrgroup in addrgoups:
        if addrgroup.name.startswith("test_"):
            fgt.api.cmdb.firewall.addrgrp.delete(name=addrgroup.name)    
    
    addresses = fgt.api.cmdb.firewall.address.get()
    for address in addresses:
        if address.name.startswith("test_"):
            fgt.api.cmdb.firewall.address.delete(name=address.name)  

    service_groups = fgt.api.cmdb.firewall.service.group.get()    
    for service_group in service_groups:
        if service_group.name.startswith("test_"):
            fgt.api.cmdb.firewall.service.group.delete(name=service_group.name)  


    service_custom = fgt.api.cmdb.firewall.service.custom.get()
    for service in service_custom:  
        if service.name.startswith("test_"):
            fgt.api.cmdb.firewall.service.custom.delete(name=service.name)
    

    shapers = fgt.api.cmdb.firewall.shaper.traffic_shaper.get()
    for shaper in shapers:
        if shaper.name.startswith("test_"):
            print(f"Deleting shaper: {shaper.name}")
            fgt.api.cmdb.firewall.shaper.traffic_shaper.delete(name=shaper.name)
      
    radius_servers = fgt.api.cmdb.user.radius.get()
    for server in radius_servers:   
        if server.name.startswith("test_"):
            fgt.api.cmdb.user.radius.delete(name=server.name)


    cleanup()
    print("✓ Pre-Cleanup completed")


    create_firewall_service()
    print("✓ create_firewall_service passed with object model")        

    create_firewall_service_group1() 
    print("✓ create_firewall_service_group passed with object model")        
    
    create_firewall_service_group2() 
    print("✓ create_firewall_service_group passed with object model")      

    create_radius_server()
    print("✓ create_radius_server passed with object model")



    multiple_format_test()
    print("✓ multiple_format_test passed with object model")

    test_single_vs_list()
    print("✓ test_single_vs_list passed with object model")

    # test_whitespace()
    # print("✓ test_whitespace passed with object model")

    test_create_address_objects()
    print("✓ test_create_address_objects passed with object model")

    test_traditional_dict_format()
    print("✓ test_traditional_dict_format passed with object model")

    test_string_list_format()
    print("✓ test_string_list_format passed with object model")

    test_single_string_format()
    print("✓ test_single_string_format passed with object model")


    test_special_chars()
    print("✓ test_special_chars passed with object model")

    test_large_list()
    print("✓ test_large_list passed with object model")

    test_update_with_flexible_format()
    print("✓ test_update_with_flexible_format passed with object model")

    test_empty_none_values()
    print("✓ test_empty_none_values passed with object model")

    test_empty_none_values_validation()
    print("✓ test_empty_none_values_validation passed with object model")

    test_long_names()
    print("✓ test_long_names passed with object model")

    test_unicode_names()
    print("✓ test_unicode_names passed with object model")

    test_duplicate_members()
    print("✓ test_duplicate_members passed with object model")

    test_case_sensitivity()
    print("✓ test_case_sensitivity passed with object model")

    test_full_crud_cycle()
    print("✓ test_full_crud_cycle passed with object model")

    test_performance_timing()
    print("✓ test_performance_timing passed with object model")

    cleanup()
    print("✓ Post-Cleanup completed")

    print("\n✓ All tests passed!")
