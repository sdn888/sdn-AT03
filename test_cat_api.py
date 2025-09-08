# test_cat_api.py
import pytest
from unittest.mock import patch, MagicMock
from cat_api import get_random_cat_image

def test_get_random_cat_image_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/abc123.jpg"}]

    with patch("cat_api.requests.get", return_value=mock_response):
        result = get_random_cat_image()
        assert result == "https://cdn2.thecatapi.com/images/abc123.jpg"


def test_get_random_cat_image_fail():
    mock_response = MagicMock()
    mock_response.status_code = 404

    with patch("cat_api.requests.get", return_value=mock_response):
        result = get_random_cat_image()
        assert result is None
