#!/usr/bin/env python3
"""
Automatic cleanup script for pytest test objects.

This script is automatically run by run_tests.py before executing tests
to ensure a clean state on the FortiGate device.
"""

import sys
from pathlib import Path

# Ensure fgtclient can be imported
sys.path.insert(0, str(Path(__file__).parent))

from fgtclient import fgt  # type: ignore


def cleanup_test_objects():
    """
    Clean up all objects with names starting with 'test_' from FortiGate.
    
    Deletes in reverse dependency order to avoid reference errors.
    Returns the total number of objects deleted.
    """
    total_deleted = 0
    
    # 1. Delete firewall policies first (they reference other objects)
    try:
        policies = fgt.api.cmdb.firewall.policy.get()
        for policy in policies:
            if policy.name and policy.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.policy.delete(policyid=policy.policyid)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 2. Delete router policies
    try:
        router_policies = fgt.api.cmdb.router.policy.get()
        for policy in router_policies:
            # Delete router policies with test in comments
            should_delete = False
            if hasattr(policy, 'comments') and policy.comments and 'test' in policy.comments.lower():
                should_delete = True
            
            if should_delete:
                try:
                    fgt.api.cmdb.router.policy.delete(seq_num=policy.seq_num)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 2b. Delete router policy6 (IPv6 policies)
    try:
        router_policy6 = fgt.api.cmdb.router.policy6.get()
        for policy in router_policy6:
            # Delete router policy6 with test in comments or low seq_num (test range)
            should_delete = False
            if hasattr(policy, 'comments') and policy.comments and 'test' in policy.comments.lower():
                should_delete = True
            # Also check if seq_num is in test range (< 1000, since tests use 10, 20, 30, etc.)
            if hasattr(policy, 'seq_num') and policy.seq_num < 1000:
                should_delete = True
            
            if should_delete:
                try:
                    fgt.api.cmdb.router.policy6.delete(seq_num=policy.seq_num)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 3. Delete firewall address groups
    try:
        addr_groups = fgt.api.cmdb.firewall.addrgrp.get()
        for group in addr_groups:
            if group.name and group.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.addrgrp.delete(name=group.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 4. Delete firewall service groups
    try:
        svc_groups = fgt.api.cmdb.firewall.service.group.get()
        for group in svc_groups:
            if group.name and group.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.service.group.delete(name=group.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 5. Delete firewall addresses
    try:
        addresses = fgt.api.cmdb.firewall.address.get()
        for addr in addresses:
            if addr.name and addr.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.address.delete(name=addr.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 6. Delete firewall services
    try:
        services = fgt.api.cmdb.firewall.service.custom.get()
        for svc in services:
            if svc.name and svc.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.service.custom.delete(name=svc.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 7. Delete firewall VIPs
    try:
        vips = fgt.api.cmdb.firewall.vip.get()
        for vip in vips:
            if vip.name and vip.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.vip.delete(name=vip.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 8. Delete firewall IP pools
    try:
        ippools = fgt.api.cmdb.firewall.ippool.get()
        for pool in ippools:
            if pool.name and pool.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.ippool.delete(name=pool.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 9. Delete firewall shapers
    try:
        shapers = fgt.api.cmdb.firewall.shaper.traffic_shaper.get()
        for shaper in shapers:
            if shaper.name and shaper.name.startswith("test_"):
                try:
                    fgt.api.cmdb.firewall.shaper.traffic_shaper.delete(name=shaper.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 10. Delete authentication schemes
    try:
        schemes = fgt.api.cmdb.authentication.scheme.get()
        for scheme in schemes:
            if scheme.name and scheme.name.startswith("test_"):
                try:
                    fgt.api.cmdb.authentication.scheme.delete(name=scheme.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 11. Delete authentication rules
    try:
        rules = fgt.api.cmdb.authentication.rule.get()
        for rule in rules:
            if rule.name and rule.name.startswith("test_"):
                try:
                    fgt.api.cmdb.authentication.rule.delete(name=rule.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 12. Delete antivirus profiles
    try:
        profiles = fgt.api.cmdb.antivirus.profile.get()
        for profile in profiles:
            if profile.name and profile.name.startswith("test_"):
                try:
                    fgt.api.cmdb.antivirus.profile.delete(name=profile.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 13. Delete application lists
    try:
        lists = fgt.api.cmdb.application.list.get()
        for lst in lists:
            if lst.name and lst.name.startswith("test_"):
                try:
                    fgt.api.cmdb.application.list.delete(name=lst.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 14. Delete application custom
    try:
        customs = fgt.api.cmdb.application.custom.get()
        for custom in customs:
            if custom.tag and custom.tag.startswith("test_"):
                try:
                    fgt.api.cmdb.application.custom.delete(tag=custom.tag)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 15. Delete application groups
    try:
        groups = fgt.api.cmdb.application.group.get()
        for group in groups:
            if group.name and group.name.startswith("test_"):
                try:
                    fgt.api.cmdb.application.group.delete(name=group.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 16. Delete static routes
    try:
        static_routes = fgt.api.cmdb.router.static.get()
        for route in static_routes:
            # Delete static routes with test in comment
            should_delete = False
            if hasattr(route, 'comment') and route.comment and 'test' in route.comment.lower():
                should_delete = True
            
            if should_delete:
                try:
                    fgt.api.cmdb.router.static.delete(seq_num=route.seq_num)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 17. Delete route maps
    try:
        route_maps = fgt.api.cmdb.router.route_map.get()
        for route_map in route_maps:
            if hasattr(route_map, 'name') and route_map.name and route_map.name.startswith("test_"):
                try:
                    fgt.api.cmdb.router.route_map.delete(name=route_map.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 18. Delete prefix lists
    try:
        prefix_lists = fgt.api.cmdb.router.prefix_list.get()
        for prefix_list in prefix_lists:
            if hasattr(prefix_list, 'name') and prefix_list.name and prefix_list.name.startswith("test_"):
                try:
                    fgt.api.cmdb.router.prefix_list.delete(name=prefix_list.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 19. Delete access lists
    try:
        access_lists = fgt.api.cmdb.router.access_list.get()
        for access_list in access_lists:
            if hasattr(access_list, 'name') and access_list.name and access_list.name.startswith("test_"):
                try:
                    fgt.api.cmdb.router.access_list.delete(name=access_list.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 20. Delete community lists
    try:
        community_lists = fgt.api.cmdb.router.community_list.get()
        for community_list in community_lists:
            if hasattr(community_list, 'name') and community_list.name and community_list.name.startswith("test_"):
                try:
                    fgt.api.cmdb.router.community_list.delete(name=community_list.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    # 21. Delete AS path lists
    try:
        aspath_lists = fgt.api.cmdb.router.aspath_list.get()
        for aspath_list in aspath_lists:
            if hasattr(aspath_list, 'name') and aspath_list.name and aspath_list.name.startswith("test_"):
                try:
                    fgt.api.cmdb.router.aspath_list.delete(name=aspath_list.name)
                    total_deleted += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    return total_deleted


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧹 CLEANING UP TEST OBJECTS FROM FORTIGATE")
    print("="*70 + "\n")
    
    deleted = cleanup_test_objects()
    
    print("\n" + "="*70)
    print(f"✅ Cleanup complete! Deleted {deleted} test objects.")
    print("="*70 + "\n")
