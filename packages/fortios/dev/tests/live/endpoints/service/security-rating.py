#!/usr/bin/env python
"""Tests for service/sniffer API endpoints.

Note: These tests must run serially (not in parallel) because they all
use the same sniffer resource on the FortiGate.
"""

import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fgtclient import fgt

# Mark all tests in this module to run in the same worker (serially)
pytestmark = pytest.mark.xdist_group(mkey="security_rating")


report_global_psirt_report = fgt.api.service.security_rating.report.get(scope="global", type="psirt") 
print(report_global_psirt_report.json)

print("\n" * 10)

report_global_psirt_report = fgt.api.service.security_rating.report.get(scope="global", type="insight") 
print(report_global_psirt_report.json)

print("\n" * 10)


report_global_psirt_report = fgt.api.service.security_rating.report.get(scope="vdom", type="psirt") 
print(report_global_psirt_report.json)

print("\n" * 10)

report_global_psirt_report = fgt.api.service.security_rating.report.get(scope="vdom", type="insight") 
print(report_global_psirt_report.json)
