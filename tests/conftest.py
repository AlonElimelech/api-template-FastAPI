import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_dns_record():
    return {
        "record_name": "test.lab.com",
        "ip": "192.168.1.1"
    }

@pytest.fixture
def invalid_dns_record():
    return {
        "record_name": "test.fail.com", 
        "ip": "invalid-ip"  # too short, there is no four octets
    }