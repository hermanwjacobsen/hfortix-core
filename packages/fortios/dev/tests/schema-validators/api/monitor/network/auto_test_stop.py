"""
Auto-generated basic tests for monitor.network/debug_flow/stop

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/monitor/network.debug-flow.stop.json
Category: monitor
Endpoint: /monitor/network/debug-flow/stop

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_stop.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.monitor.network.debug_flow.stop


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
# To test this endpoint, create manual tests in test_stop.py
# ============================================================================


# Metadata for test discovery
TEST_ENDPOINT = "monitor/network/debug_flow/stop"
TEST_CATEGORY = "monitor"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/monitor/network.debug-flow.stop.json"
TEST_HTTP_METHODS = ['POST']