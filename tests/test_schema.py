import pytest
from dns.schemas import DNSRecordCreate
from pydantic import ValidationError

def test_valid_schema():
    record = DNSRecordCreate(
        record_name="test.lab.com",
        ip="192.168.1.1"
    )
    assert record.record_name == "test.lab.com"
    assert record.ip == "192.168.1.1"

def test_invalid_ip():
    with pytest.raises(ValidationError):
        DNSRecordCreate(
            record_name="test.example.com",
            ip="invalid-ip"
        )

def test_invalid_record_name():
    with pytest.raises(ValidationError):
        DNSRecordCreate(
            record_name="dns-longest-then-15",  # too short
            ip="192.168.1.1"
        )