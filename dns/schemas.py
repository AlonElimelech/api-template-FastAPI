from pydantic import BaseModel, Field, field_validator
import re

class DNSRecordCreate(BaseModel):
    record_name: str = Field(..., max_length=15)
    ip: str

    @field_validator('ip')
    def validate_ip(cls, v):
        ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        if not re.match(ip_pattern, v):
            raise ValueError('Invalid IP address format')
        return v

class DNSRecordResponse(BaseModel):
    record_name: str = Field(..., max_length=15)
    status_code: int
    status: str


class DNSRecordUpdate(BaseModel):
    ip: str

    @field_validator('ip')
    def validate_ip(cls, v):
        ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        if not re.match(ip_pattern, v):
            raise ValueError('Invalid IP address format')
        return v