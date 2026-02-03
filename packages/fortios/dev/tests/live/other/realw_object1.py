import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fgtclient import fgt

def create_firewall_address():
    """Test: Create firewall address"""
    result = fgt.api.cmdb.firewall.address.post(
        name="test_address_lan1",
        subnet="192.168.1.0/24"
    )
    assert result is not None
    assert result.http_status == "success"   

    verify = fgt.api.cmdb.firewall.address.get(name="test_address_lan1")
    assert verify is not None
    assert verify.name == "test_address_lan1"
    assert verify.subnet == "192.168.1.0 255.255.255.0"   

def create_firewall_services():
    """Test: Create firewall services"""
    result1 = fgt.api.cmdb.firewall.service.custom.post(
        name="test_service1",
        protocol="TCP/UDP/UDP-Lite/SCTP",
        tcp_portrange="8080-8090",
        udp_portrange="8080-8090"
    )
    assert result1 is not None
    assert result1.http_status == "success"   
    
    verify1 = fgt.api.cmdb.firewall.service.custom.get(name="test_service1")
    assert verify1 is not None
   

    result2 = fgt.api.cmdb.firewall.service.custom.post(
        name="test_service2",
        protocol="ICMP",
        icmptype=8,
        icmpcode=0
    )
    assert result2 is not None
    assert result2.http_status == "success"
    verify2 = fgt.api.cmdb.firewall.service.custom.get(name="test_service2") 
    assert verify2 is not None


def create_firewall_service_group():
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
    verify = fgt.api.cmdb.firewall.service.group.get(name="test_service_group1")
    assert verify is not None


def create_firewall_ip_pool():
    """Test: Create firewall IP pool"""
    result = fgt.api.cmdb.firewall.ippool.post(
        name="test_ip_pool1",
        startip="192.168.55.1",
        endip="192.168.55.100"
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.ippool.get(name="test_ip_pool1")
    assert verify is not None
    

def create_firewall_address_group():
    """Test: Create firewall address group"""
    result = fgt.api.cmdb.firewall.addrgrp.post(
    name="test_address_group1",
    member=[
        {"name": "test_address_lan1"}
    ]
    )
    assert result is not None
    assert result.http_status == "success"
    verify = fgt.api.cmdb.firewall.addrgrp.get(name="test_address_group1")
    assert verify is not None
    

# def create_firewall_virtual_server():
#     """Test: Create firewall virtual server"""
#     result = fgt.api.cmdb.firewall.vip.post(
#         name="test_virtual_server1",
#         type="server-load-balance",
#         extport="443",
#         extip="192.168.55.10",
#         extintf="port3",                        # Should support [{"q_origin_key": "any"}]
#     )
#     assert result is not None
#     assert result.http_status == "success"
#     verify = fgt.api.cmdb.firewall.vip.get(name="test_virtual_server1")
#     assert verify is not None
    


def create_firewall_rule():
    """Test: Create firewall rule"""
    result = fgt.api.cmdb.firewall.policy.post(
        name="test_firewall_rule1",
        srcintf=[{"name": "port3"}],
        dstintf=[{"name": "port4"}],
        srcaddr=[{"name": "test_address_group1"}],
        dstaddr=[{"name": "all"}],
        action="accept",
        schedule="always",
        service=[{"name": "test_service_group1"}],
        logtraffic="all",
        nat="enable",
        ippool="enable",
        poolname=[{"name": "test_ip_pool1"}]
    )
    assert result is not None
    assert result.http_status == "success"

    

if __name__ == "__main__":  
    # Pre-cleanup - Delete all test objects (anything starting with "test_")
    try:
        for policy in fgt.api.cmdb.firewall.policy.get():
            if policy.name and policy.name.startswith("test_"):
                fgt.api.cmdb.firewall.policy.delete(policyid=policy.policyid)
    except:
        pass
    
    try:
        service_groups = fgt.api.cmdb.firewall.service.group.get()
        for sg in service_groups:
            if sg.name and sg.name.startswith("test_"):
                fgt.api.cmdb.firewall.service.group.delete(name=sg.name)
    except:
        pass
    
    try:
        addrgroups = fgt.api.cmdb.firewall.addrgrp.get()
        for ag in addrgroups:
            if ag.name and ag.name.startswith("test_"):
                fgt.api.cmdb.firewall.addrgrp.delete(name=ag.name)
    except:
        pass
    
    try:
        vips = fgt.api.cmdb.firewall.vip.get()
        for vip in vips:
            if vip.name and vip.name.startswith("test_"):
                fgt.api.cmdb.firewall.vip.delete(name=vip.name)
    except:
        pass
    
    try:
        ippools = fgt.api.cmdb.firewall.ippool.get()
        for pool in ippools:
            if pool.name and pool.name.startswith("test_"):
                fgt.api.cmdb.firewall.ippool.delete(name=pool.name)
    except:
        pass

    try:
        services = fgt.api.cmdb.firewall.service.custom.get()
        for svc in services:
            if svc.name and svc.name.startswith("test_"):
                fgt.api.cmdb.firewall.service.custom.delete(name=svc.name)
    except:
        pass

    try:
        addresses = fgt.api.cmdb.firewall.address.get()
        for addr in addresses:
            if addr.name and addr.name.startswith("test_"):
                fgt.api.cmdb.firewall.address.delete(name=addr.name)
    except:
        pass



    create_firewall_address()
    print("✓ create_firewall_address passed with object model")    
    create_firewall_services()
    print("✓ create_firewall_services passed with object model")
    create_firewall_service_group()
    print("✓ create_firewall_service_group passed with object model")
    create_firewall_address_group()
    print("✓ create_firewall_address_group passed with object model")
    create_firewall_ip_pool()
    print("✓ create_firewall_ip_pool passed with object model")
    # create_firewall_virtual_server()
    # print("✓ create_firewall_virtual_server passed with object model")
    create_firewall_rule()
    print("✓ create_firewall_rule passed with object model")

