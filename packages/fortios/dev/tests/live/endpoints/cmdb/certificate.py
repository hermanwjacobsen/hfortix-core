import argparse
import sys
from pathlib import Path

# Add pytest directory to path (go up from endpoints/cmdb/ to pytest/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt



def test_get_certificate_hsm_local():
    """Test: Get local HSM certificate settings"""
    result = fgt.api.cmdb.certificate.hsm_local.get()
    assert result is not None
    assert isinstance(result, list)

def test_get_certificate_ca():
    """Test: Get CA certificates"""
    ca_list = fgt.api.cmdb.certificate.ca.get()
    assert ca_list is not None
    assert isinstance(ca_list, list)


def test_get_specific_certificate_ca():
    """Test: Get specific CA certificate by name"""
    ca_list = fgt.api.cmdb.certificate.ca.get()
    if not ca_list:
        # No CA certificates to test
        return
    ca_name = ca_list[0].name
    ca_cert = fgt.api.cmdb.certificate.ca.get(name=ca_name)
    assert ca_cert is not None
    assert ca_cert.name == ca_name

def test_get_certificate_crl():
    """Test: Get CRL certificates"""
    crl_list = fgt.api.cmdb.certificate.crl.get()
    assert crl_list is not None
    assert isinstance(crl_list, list)

def test_get_certificate_local():
    """Test: Get local certificates"""
    local_list = fgt.api.cmdb.certificate.local.get()
    assert local_list is not None
    assert isinstance(local_list, list)

def test_get_specific_certificate_local():
    """Test: Get specific local certificate by name"""
    if not fgt.api.cmdb.certificate.local.get():
        # No local certificates to test
        return
    local_name = fgt.api.cmdb.certificate.local.get()[0].name
    local_cert = fgt.api.cmdb.certificate.local.get(name=local_name)
    assert local_cert is not None
    assert local_cert.name == local_name
    
def test_get_certificate_remote():
    """Test: Get remote certificates"""
    remote_list = fgt.api.cmdb.certificate.remote.get()
    assert remote_list is not None
    assert isinstance(remote_list, list)


if __name__ == "__main__":  
    test_get_certificate_hsm_local()
    print("✓ test_get_certificate_hsm_local passed")

    test_get_certificate_ca()
    print("✓ test_get_certificate_ca passed")

    test_get_specific_certificate_ca()
    print("✓ test_get_specific_certificate_ca passed")

    test_get_certificate_crl()
    print("✓ test_get_certificate_crl passed")

    test_get_certificate_local()
    print("✓ test_get_certificate_local passed")

    test_get_specific_certificate_local()
    print("✓ test_get_specific_certificate_local passed")

    test_get_certificate_remote()
    print("✓ test_get_certificate_remote passed")

    if fmg:
        logout_response = fmg.logout()
        status_code = logout_response["result"][0]["status"]["code"]
        assert status_code == 0, f"FMG logout failed with code {status_code}"
        print("✓ FMG logout successful")
