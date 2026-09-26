import pytest
from api.api_client import APIClient
from config.config import BASE_URL, API_TOKEN, TIMEOUT
from utils.logger import configure_logging
configure_logging()

@pytest.fixture
def api_client():
    return APIClient(BASE_URL, API_TOKEN or None, TIMEOUT)
