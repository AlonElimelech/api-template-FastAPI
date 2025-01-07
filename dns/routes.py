from fastapi import APIRouter
from dns.schemas import DNSRecordCreate, DNSRecordResponse
from dns.service import create_dns_record, delete_dns_record
router = APIRouter()

@router.post("/", response_model=DNSRecordResponse)
async def create_dns(record: DNSRecordCreate):
    return await create_dns_record(record)

@router.delete("/{record_name}")
async def delete_dns(record_name: str):
    return await delete_dns_record(record_name)