import sys
from pathlib import Path
import pytest

pytestmark = pytest.mark.xdist_group(Path(__file__).stem)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from fgtclient import fgt

def test_firewall_internet_service_subapp_get():
    result = fgt.api.cmdb.firewall.internet_service_subapp.get()
    assert result is not None
    assert result.http_status_code == 200
