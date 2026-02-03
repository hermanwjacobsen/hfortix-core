import argparse
import sys
from pathlib import Path

import pytest

# Run DLP tests on a single worker to preserve state
pytestmark = pytest.mark.xdist_group("emailfilter")

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt


def cleanup(): 
    try:
        email_filters = fgt.api.cmdb.emailfilter.block_allow_list.get()
        for ef in email_filters:
            name = ef.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.emailfilter.block_allow_list.delete(ef.id)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        bwords = fgt.api.cmdb.emailfilter.bword.get()
        for bw in bwords:
            name = bw.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.emailfilter.bword.delete(bw.id)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        dnsbls = fgt.api.cmdb.emailfilter.dnsbl.get()
        for db in dnsbls:
            name = db.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.emailfilter.dnsbl.delete(db.id)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        fortishield = fgt.api.cmdb.emailfilter.fortishield.get()
        if fortishield:
            fgt.api.cmdb.emailfilter.fortishield.put(
                spam_submit_force="enable"
            )
    except Exception:
        pass

    try:
        iptrusts = fgt.api.cmdb.emailfilter.iptrust.get()
        for it in iptrusts:
            name = it.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.emailfilter.iptrust.delete(it.id)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        mheaders = fgt.api.cmdb.emailfilter.mheader.get()
        for mh in mheaders:
            name = mh.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.emailfilter.mheader.delete(mh.id)
                except Exception:
                    pass
    except Exception:
        pass

    
    try: 
        fgt.api.cmdb.emailfilter.options.put(
            dns_timeout=7
        )
    except Exception:
        pass

    try:
        profiles = fgt.api.cmdb.emailfilter.profile.get()
        for profile in profiles:
            name = profile.name
            if name and str(name).startswith("test_"):
                try:
                    fgt.api.cmdb.emailfilter.profile.delete(profile.name)
                except Exception:
                    pass
    except Exception:
        pass

def test_get_emailfilter_block_allow_list():
    """Test: Get email filter block/allow list"""
    result = fgt.api.cmdb.emailfilter.block_allow_list.get()
    assert result is not None
    assert result.http_status_code == 200


def test_post_emailfilter_block_allow_list():
    """Test: Create email filter block/allow list entry"""
    result = fgt.api.cmdb.emailfilter.block_allow_list.post(
        name="test_emailfilter1",
        comment="Test Email Filter",
    )

def test_get_specific_emailfilter_block_allow_list():
    """Test: Get specific email filter block/allow list entry"""
    result = fgt.api.cmdb.emailfilter.block_allow_list.get()
    for ef in result:
        if ef.name == "test_emailfilter1":
            specific = fgt.api.cmdb.emailfilter.block_allow_list.get(id=ef.id)
            assert specific is not None
            assert specific.name == "test_emailfilter1"
            return
    pytest.fail("test_emailfilter1 not found")


def test_put_emailfilter_block_allow_list():
    """Test: Update email filter block/allow list entry"""
    result = fgt.api.cmdb.emailfilter.block_allow_list.get()
    for ef in result:
        if ef.name == "test_emailfilter1":
            updated = fgt.api.cmdb.emailfilter.block_allow_list.put(
                id=ef.id,
                comment="Updated Test Email Filter"
            )
            updated_id = updated.id
            assert updated is not None
            assert updated.http_status == "success"
            return
    pytest.fail("test_emailfilter1 not found")
    updated = fgt.api.cmdb.emailfilter.block_allow_list.get(id=updated_id)
    assert updated.comment == "Updated Test Email Filter"

def test_delete_emailfilter_block_allow_list():
    """Test: Delete email filter block/allow list entry"""
    result = fgt.api.cmdb.emailfilter.block_allow_list.get()
    for ef in result:
        if ef.name == "test_emailfilter1":
            deleted = fgt.api.cmdb.emailfilter.block_allow_list.delete(id=ef.id)
            assert deleted is not None
            assert deleted.http_status == "success"
            return
    pytest.fail("test_emailfilter1 not found")
    

def test_get_emailfilter_bword():
    """Test: Get email filter bad word list"""
    result = fgt.api.cmdb.emailfilter.bword.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_emailfilter_bword():
    """Test: Create email filter bad word entry"""
    result = fgt.api.cmdb.emailfilter.bword.post(
        name="test_bword1",
        comment="Test Bad Word",
        entries=[
            {
                "status": "enable",
                "pattern": "spamword",
                "pattern_type": "wildcard",
                "action": "spam",
                "where": "all",
                "language": "western"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_emailfilter_bword():
    """Test: Get specific email filter bad word entry"""
    result = fgt.api.cmdb.emailfilter.bword.get()
    for bw in result:
        if bw.name == "test_bword1":
            specific = fgt.api.cmdb.emailfilter.bword.get(id=bw.id)
            assert specific is not None
            assert specific.name == "test_bword1"
            return
    pytest.fail("test_bword1 not found")


def test_put_emailfilter_bword():
    """Test: Update email filter bad word entry"""
    result = fgt.api.cmdb.emailfilter.bword.get()
    for bw in result:
        if bw.name == "test_bword1":
            updated = fgt.api.cmdb.emailfilter.bword.put(
                id=bw.id,
                comment="Updated Test Bad Word"
            )
            updated_id = updated.id
            assert updated is not None
            assert updated.http_status == "success"
            return
    pytest.fail("test_bword1 not found")
    updated = fgt.api.cmdb.emailfilter.bword.get(id=updated_id)
    assert updated.comment == "Updated Test Bad Word"


def test_delete_emailfilter_bword():
    """Test: Delete email filter bad word entry"""
    result = fgt.api.cmdb.emailfilter.bword.get()
    for bw in result:
        if bw.name == "test_bword1":
            deleted = fgt.api.cmdb.emailfilter.bword.delete(id=bw.id)
            assert deleted is not None
            assert deleted.http_status == "success"
            return
    pytest.fail("test_bword1 not found")

def test_get_emailfilter_dnsbl():
    """Test: Get email filter DNSBL settings"""
    result = fgt.api.cmdb.emailfilter.dnsbl.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_emailfilter_dnsbl():
    """Test: Create email filter DNSBL entry"""
    result = fgt.api.cmdb.emailfilter.dnsbl.post(
        name="test_dnsbl1",
        comment="Test DNSBL",
        entries=[
            {
                "status": "enable",
                "server": "zen.spamhaus.org",
                "action": "reject"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_emailfilter_dnsbl():
    """Test: Get specific email filter DNSBL entry"""
    result = fgt.api.cmdb.emailfilter.dnsbl.get()
    for db in result:
        if db.name == "test_dnsbl1":
            specific = fgt.api.cmdb.emailfilter.dnsbl.get(id=db.id)
            assert specific is not None
            assert specific.name == "test_dnsbl1"
            return
    pytest.fail("test_dnsbl1 not found")


def test_put_emailfilter_dnsbl():
    """Test: Update email filter DNSBL entry"""
    result = fgt.api.cmdb.emailfilter.dnsbl.get()
    for db in result:
        if db.name == "test_dnsbl1":
            updated = fgt.api.cmdb.emailfilter.dnsbl.put(
                id=db.id,
                comment="Updated Test DNSBL"
            )
            updated_id = updated.id
            assert updated is not None
            assert updated.http_status == "success"
            return
    pytest.fail("test_dnsbl1 not found")
    updated = fgt.api.cmdb.emailfilter.dnsbl.get(id=updated_id)
    assert updated.comment == "Updated Test DNSBL"


def test_delete_emailfilter_dnsbl():
    """Test: Delete email filter DNSBL entry"""
    result = fgt.api.cmdb.emailfilter.dnsbl.get()
    for db in result:
        if db.name == "test_dnsbl1":
            deleted = fgt.api.cmdb.emailfilter.dnsbl.delete(id=db.id)
            assert deleted is not None
            assert deleted.http_status == "success"
            return
    pytest.fail("test_dnsbl1 not found")


def test_get_emailfilter_fortishield():
    """Test: Get email filter FortiShield settings"""
    result = fgt.api.cmdb.emailfilter.fortishield.get()
    assert result is not None
    assert result.http_status_code == 200

def test_put_emailfilter_fortishield():
    """Test: Update email filter FortiShield settings"""
    result = fgt.api.cmdb.emailfilter.fortishield.put(
        spam_submit_force="disable"
    )
    assert result is not None
    assert result.http_status_code == 200
    updated = fgt.api.cmdb.emailfilter.fortishield.get()
    assert updated.spam_submit_force == "disable"

def test_emailfilter_reset_default():
    """Test: Reset email filter settings to default"""
    result = fgt.api.cmdb.emailfilter.fortishield.put(
        spam_submit_force="enable"
    )
    assert result is not None
    assert result.http_status_code == 200
    updated = fgt.api.cmdb.emailfilter.fortishield.get()
    assert updated.spam_submit_force == "enable"


def test_get_emailfilter_iptrust():
    """Test: Get email filter IP trust list"""
    result = fgt.api.cmdb.emailfilter.iptrust.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_emailfilter_iptrust():
    """Test: Create email filter IP trust entry"""
    result = fgt.api.cmdb.emailfilter.iptrust.post(
        name="test_iptrust1",
        comment="Test IP Trust",
        entries=[
            {
                "status": "enable",
                "addr_type": "ipv4",
                "ip4_subnet": "192.168.1.0/24"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_emailfilter_iptrust():
    """Test: Get specific email filter IP trust entry"""
    result = fgt.api.cmdb.emailfilter.iptrust.get()
    for it in result:
        if it.name == "test_iptrust1":
            specific = fgt.api.cmdb.emailfilter.iptrust.get(id=it.id)
            assert specific is not None
            assert specific.name == "test_iptrust1"
            return
    pytest.fail("test_iptrust1 not found")  

def test_put_emailfilter_iptrust():
    """Test: Update email filter IP trust entry"""
    result = fgt.api.cmdb.emailfilter.iptrust.get()
    for it in result:
        if it.name == "test_iptrust1":
            updated = fgt.api.cmdb.emailfilter.iptrust.put(
                id=it.id,
                comment="Updated Test IP Trust"
            )
            updated_id = updated.id
            assert updated is not None
            assert updated.http_status == "success"
            return
    pytest.fail("test_iptrust1 not found")
    updated = fgt.api.cmdb.emailfilter.iptrust.get(id=updated_id)
    assert updated.comment == "Updated Test IP Trust"   

def test_delete_emailfilter_iptrust():
    """Test: Delete email filter IP trust entry"""
    result = fgt.api.cmdb.emailfilter.iptrust.get()
    for it in result:
        if it.name == "test_iptrust1":
            deleted = fgt.api.cmdb.emailfilter.iptrust.delete(id=it.id)
            assert deleted is not None
            assert deleted.http_status == "success"
            return
    pytest.fail("test_iptrust1 not found")

def test_get_emailfilter_mheader():
    """Test: Get email filter mime header list"""
    result = fgt.api.cmdb.emailfilter.mheader.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_emailfilter_mheader():
    """Test: Create email filter mime header entry"""
    result = fgt.api.cmdb.emailfilter.mheader.post(
        name="test_mheader1",
        comment="Test Mime Header",
        entries=[
            {
                "status": "enable",
                "fieldname": "X-Spam-Flag",
                "fieldbody": "YES",
                "pattern_type": "wildcard",
                "action": "spam"
            }
        ]
    )
    assert result is not None
    assert result.http_status == "success"

def test_get_specific_emailfilter_mheader():
    """Test: Get specific email filter mime header entry"""
    result = fgt.api.cmdb.emailfilter.mheader.get()
    for mh in result:
        if mh.name == "test_mheader1":
            specific = fgt.api.cmdb.emailfilter.mheader.get(id=mh.id)
            assert specific is not None
            assert specific.name == "test_mheader1"
            return
    pytest.fail("test_mheader1 not found")

def test_put_emailfilter_mheader():
    """Test: Update email filter mime header entry"""
    result = fgt.api.cmdb.emailfilter.mheader.get()
    for mh in result:
        if mh.name == "test_mheader1":
            updated = fgt.api.cmdb.emailfilter.mheader.put(
                id=mh.id,
                comment="Updated Test Mime Header"
            )
            assert updated is not None
            assert updated.http_status == "success"
            return
    pytest.fail("test_mheader1 not found")

def test_delete_emailfilter_mheader():
    """Test: Delete email filter mime header entry"""
    result = fgt.api.cmdb.emailfilter.mheader.get()
    for mh in result:
        if mh.name == "test_mheader1":
            deleted = fgt.api.cmdb.emailfilter.mheader.delete(id=mh.id)
            assert deleted is not None
            assert deleted.http_status == "success"
            return
    pytest.fail("test_mheader1 not found")

def test_get_emailfilter_options():
    """Test: Get email filter options"""
    result = fgt.api.cmdb.emailfilter.options.get()
    assert result is not None
    assert result.http_status_code == 200

def test_put_emailfilter_options():
    """Test: Update email filter options"""
    result = fgt.api.cmdb.emailfilter.options.put(
        dns_timeout=10
    )
    assert result is not None
    assert result.http_status_code == 200
    updated = fgt.api.cmdb.emailfilter.options.get()
    assert updated.dns_timeout == 10

def test_reset_emailfilter_options():
    """Test: Reset email filter options to default"""
    result = fgt.api.cmdb.emailfilter.options.put(
        dns_timeout=7
    )
    assert result is not None
    assert result.http_status_code == 200
    updated = fgt.api.cmdb.emailfilter.options.get()
    assert updated.dns_timeout == 7


def test_get_emailfilter_profile():
    """Test: Get email filter profile"""
    result = fgt.api.cmdb.emailfilter.profile.get()
    assert result is not None
    assert result.http_status_code == 200

def test_post_emailfilter_profile():
    """Test: Create email filter profile"""
    result = fgt.api.cmdb.emailfilter.profile.post(
        name="test_profile1",
        comment="Test Email Filter Profile",
        spam_log="enable"
    )
    assert result is not None
    assert result.http_status == "success"


def test_get_specific_emailfilter_profile():
    """Test: Get specific email filter profile"""
    result = fgt.api.cmdb.emailfilter.profile.get()
    for ep in result:
        if ep.name == "test_profile1":
            specific = fgt.api.cmdb.emailfilter.profile.get(name=ep.name)
            assert specific is not None
            assert specific.name == "test_profile1"
            return
    pytest.fail("test_profile1 not found")  

def test_put_emailfilter_profile():
    """Test: Update email filter profile"""
    result = fgt.api.cmdb.emailfilter.profile.get()
    for ep in result:
        if ep.name == "test_profile1":
            updated = fgt.api.cmdb.emailfilter.profile.put(
                name=ep.name,
                comment="Updated Test Email Filter Profile"
            )
            assert updated is not None
            assert updated.http_status == "success"
            return
    pytest.fail("test_profile1 not found")
    updated = fgt.api.cmdb.emailfilter.profile.get(name="test_profile1")
    assert updated.comment == "Updated Test Email Filter Profile"   

def test_delete_emailfilter_profile():
    """Test: Delete email filter profile"""
    result = fgt.api.cmdb.emailfilter.profile.get()
    for ep in result:
        if ep.name == "test_profile1":
            deleted = fgt.api.cmdb.emailfilter.profile.delete(name=ep.name)
            assert deleted is not None
            assert deleted.http_status == "success"
            return
    pytest.fail("test_profile1 not found")  
    verify = fgt.api.cmdb.emailfilter.profile.get()
    for ep in verify:
        if ep.name == "test_profile1":
            pytest.fail("test_profile1 was not deleted")    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests")
    parser.add_argument("--client", choices=["direct", "fmg_proxy"], default="direct",
                        help="Client to use: direct (default) or fmg_proxy")
    args = parser.parse_args()
    
    if args.client == "fmg_proxy":
        from fmgclient import fgt, fmg
        client_name = "FMG proxy"
    else:
        from fgtclient import fgt
        fmg = None
        client_name = "direct"
    
    print(f"Running tests with {client_name} client...")
    print("Testing cmdb/emailfilter API endpoints...")
    print("=" * 60)
    print()
    
    cleanup()
    print("✓ Pre-Cleanup passed")

    test_post_emailfilter_block_allow_list()
    print("✓ test_post_emailfilter_block_allow_list passed")

    test_get_emailfilter_block_allow_list()
    print("✓ test_get_emailfilter_block_allow_list passed")
    
    test_get_specific_emailfilter_block_allow_list()
    print("✓ test_get_specific_emailfilter_block_allow_list passed")

    test_put_emailfilter_block_allow_list()
    print("✓ test_put_emailfilter_block_allow_list passed")

    test_delete_emailfilter_block_allow_list()
    print("✓ test_delete_emailfilter_block_allow_list passed")

    test_get_emailfilter_bword()
    print("✓ test_get_emailfilter_bword passed")

    test_post_emailfilter_bword()
    print("✓ test_post_emailfilter_bword passed")

    test_get_specific_emailfilter_bword()
    print("✓ test_get_specific_emailfilter_bword passed")

    test_put_emailfilter_bword()
    print("✓ test_put_emailfilter_bword passed")

    test_delete_emailfilter_bword()
    print("✓ test_delete_emailfilter_bword passed")

    test_get_emailfilter_dnsbl()
    print("✓ test_get_emailfilter_dnsbl passed")

    test_post_emailfilter_dnsbl()
    print("✓ test_post_emailfilter_dnsbl passed")

    test_get_specific_emailfilter_dnsbl()
    print("✓ test_get_specific_emailfilter_dnsbl passed")

    test_put_emailfilter_dnsbl()
    print("✓ test_put_emailfilter_dnsbl passed")

    test_delete_emailfilter_dnsbl()
    print("✓ test_delete_emailfilter_dnsbl passed")

    test_get_emailfilter_fortishield()
    print("✓ test_get_emailfilter_fortishield passed")

    test_put_emailfilter_fortishield()
    print("✓ test_put_emailfilter_fortishield passed")

    test_emailfilter_reset_default()
    print("✓ test_emailfilter_reset_default passed")

    test_get_emailfilter_iptrust()
    print("✓ test_get_emailfilter_iptrust passed") 

    test_post_emailfilter_iptrust()     
    print("✓ test_post_emailfilter_iptrust passed")

    test_get_specific_emailfilter_iptrust()
    print("✓ test_get_specific_emailfilter_iptrust passed")

    test_put_emailfilter_iptrust()
    print("✓ test_put_emailfilter_iptrust passed")

    test_delete_emailfilter_iptrust()
    print("✓ test_delete_emailfilter_iptrust passed")

    test_get_emailfilter_mheader()
    print("✓ test_get_emailfilter_mheader passed")

    test_post_emailfilter_mheader()
    print("✓ test_post_emailfilter_mheader passed")

    test_get_specific_emailfilter_mheader()
    print("✓ test_get_specific_emailfilter_mheader passed")

    test_put_emailfilter_mheader()
    print("✓ test_put_emailfilter_mheader passed")

    test_delete_emailfilter_mheader()
    print("✓ test_delete_emailfilter_mheader passed")    

    test_get_emailfilter_options()
    print("✓ test_get_emailfilter_options passed")

    test_put_emailfilter_options()
    print("✓ test_put_emailfilter_options passed") 

    test_reset_emailfilter_options()
    print("✓ test_reset_emailfilter_options passed")

    test_get_emailfilter_profile()
    print("✓ test_get_emailfilter_profile passed")

    test_post_emailfilter_profile()
    print("✓ test_post_emailfilter_profile passed")

    test_get_specific_emailfilter_profile()
    print("✓ test_get_specific_emailfilter_profile passed")

    test_put_emailfilter_profile()
    print("✓ test_put_emailfilter_profile passed")
    
    test_delete_emailfilter_profile()
    print("✓ test_delete_emailfilter_profile passed")



    cleanup()
    print("✓ Post-Cleanup passed") 

    print()
    print("=" * 60)
    print("✓ All 36 tests passed!")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
