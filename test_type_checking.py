"""Test type checking and autocomplete"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "packages" / "core"))
sys.path.insert(0, str(Path(__file__).parent / "packages" / "fortios"))

from hfortix_fortios import FortiOS

# Test autocomplete
fgt = FortiOS(host="192.168.1.99", token="test123")

# This should autocomplete - type a dot after fgt and see if 'api' appears
# fgt.

# After typing fgt.api. you should see cmdb, monitor, log, service
# fgt.api.

# After typing fgt.api.cmdb. you should see firewall, system, etc.
# fgt.api.cmdb.

# After typing fgt.api.cmdb.firewall. you should see address, policy, etc.
# fgt.api.cmdb.firewall.
