"""
Auto-generated basic tests for monitor.switch_controller/mclag_icl/set_tier1

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/monitor/switch-controller.mclag-icl.set-tier1.json
Category: monitor
Endpoint: /monitor/switch-controller/mclag-icl/set-tier1

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_set-tier1.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.monitor.switch_controller.mclag_icl.set_tier1


# ============================================================================
# No Auto-Generated Tests for Action/Category Endpoints
# ============================================================================
# 
# This endpoint is a category container or action endpoint with sub-endpoints.
# It does not have direct GET/POST methods but provides access to sub-actions.
# 
# Auto-generated tests only cover safe, read-only GET operations.
# Write operations require careful manual testing with proper setup/teardown.
#
# Available sub-endpoints can be accessed via this category object.
# Refer to the API documentation for available actions.
#
# To test this endpoint, create manual tests in test_set-tier1.py
# ============================================================================


# Metadata for test discovery
TEST_ENDPOINT = "monitor/switch_controller/mclag_icl/set_tier1"
TEST_CATEGORY = "monitor"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/monitor/switch-controller.mclag-icl.set-tier1.json"
TEST_HTTP_METHODS = ['POST']