import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fgtclient import fgt_object

def test_post_firewall_address():
    """Test: Create firewall address"""
    result = fgt_object.api.cmdb.firewall.address.post(
        name="test_address11",
        subnet="10.0.0.0/24"
    )
    assert result is not None
    assert result.http_status == "success"    

def test_get_specific_firewall_address():
    """Get firewall address list as objects"""
    result = fgt_object.api.cmdb.firewall.address.get(name="test_address11")
    assert result is not None
    # Find the specific address in the list
    address = result if result.name == "test_address11" else None
    assert address is not None
    assert address.subnet == "10.0.0.0 255.255.255.0"  
    

def test_delete_firewall_address():
    """Test: Delete firewall address"""
    result = fgt_object.api.cmdb.firewall.address.delete(name="test_address11")
    assert result is not None
    assert result.http_status == "success"

if __name__ == "__main__":
    try:
        fgt_object.api.cmdb.firewall.address.delete(name="test_address11")
    except:
        pass

    test_post_firewall_address()
    print("✓ test_post_firewall_address passed with object model")

    test_get_specific_firewall_address()
    print("✓ test_get_specific_firewall_address passed with object model")

    test_delete_firewall_address()
    print("✓ test_delete_firewall_address passed with object model")   

