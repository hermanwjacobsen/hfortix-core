import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

def test_firewall_internet_service_ipbl_vendor_get():
    result = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.get()
    assert result is not None
    assert result.http_status_code == 200
