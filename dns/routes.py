from fastapi import APIRouter
from dns.schemas import DNSRecordCreate, DNSRecordResponse
from dns.service import create_dns_record, delete_dns_record

router = APIRouter()

@router.post("/", response_model=DNSRecordResponse)
def create_dns(record: DNSRecordCreate):
    return create_dns_record(record)

@router.delete("/{record_name}")
def delete_dns(record_name: str):
    return delete_dns_record(record_name)