"""
Auto-generated tests for LOG fortianalyzer endpoint.

These are basic smoke tests to verify:
  1. Endpoint class can be imported
  2. Methods exist and are callable
  3. Basic structure is correct

Note: These tests do NOT make actual API calls.
      They only verify the generated code structure.
"""

import pytest
from unittest.mock import Mock, MagicMock

from packages.fortios.hfortix_fortios.api.v2.log.fortianalyzer import Fortianalyzer


class TestFortianalyzerStructure:
    """Test fortianalyzer endpoint structure."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock HTTP client."""
        client = Mock()
        client.get = MagicMock(return_value={"status": "success"})
        client.post = MagicMock(return_value={"status": "success"})
        return client

    @pytest.fixture
    def fortianalyzer_endpoint(self, mock_client):
        """Create fortianalyzer endpoint instance."""
        return Fortianalyzer(mock_client)

    def test_import_fortianalyzer(self):
        """Test that fortianalyzer class can be imported."""
        from packages.fortios.hfortix_fortios.api.v2.log.fortianalyzer import Fortianalyzer
        assert Fortianalyzer is not None

    def test_fortianalyzer_has_get_method(self, fortianalyzer_endpoint):
        """Test that endpoint has get() method."""
        assert hasattr(fortianalyzer_endpoint, "get")
        assert callable(getattr(fortianalyzer_endpoint, "get"))

    def test_fortianalyzer_structure(self, fortianalyzer_endpoint, mock_client):
        """Test endpoint structure and method calls."""
        # Call get() - should not raise
        result = fortianalyzer_endpoint.get()
        
        # Verify mock was called
        assert mock_client.get.called or mock_client.post.called
