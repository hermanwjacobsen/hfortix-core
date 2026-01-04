"""
Auto-generated tests for LOG search endpoint.

These are basic smoke tests to verify:
  1. Endpoint class can be imported
  2. Methods exist and are callable
  3. Basic structure is correct

Note: These tests do NOT make actual API calls.
      They only verify the generated code structure.
"""

import pytest
from unittest.mock import Mock, MagicMock

from packages.fortios.hfortix_fortios.api.v2.log.search import Search


class TestSearchStructure:
    """Test search endpoint structure."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock HTTP client."""
        client = Mock()
        client.get = MagicMock(return_value={"status": "success"})
        client.post = MagicMock(return_value={"status": "success"})
        return client

    @pytest.fixture
    def search_endpoint(self, mock_client):
        """Create search endpoint instance."""
        return Search(mock_client)

    def test_import_search(self):
        """Test that search class can be imported."""
        from packages.fortios.hfortix_fortios.api.v2.log.search import Search
        assert Search is not None

    def test_search_has_get_method(self, search_endpoint):
        """Test that endpoint has get() method."""
        assert hasattr(search_endpoint, "get")
        assert callable(getattr(search_endpoint, "get"))

    def test_search_structure(self, search_endpoint, mock_client):
        """Test endpoint structure and method calls."""
        # Call get() - should not raise
        result = search_endpoint.get()
        
        # Verify mock was called
        assert mock_client.get.called or mock_client.post.called
