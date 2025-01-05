from pydantic import BaseModel

class DNSRecordCreate(BaseModel):
    record_name: str
    ip_address: str

class DNSRecordResponse(BaseModel):
    record_name: str
    status: str