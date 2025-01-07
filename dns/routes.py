from fastapi import APIRouter
from dns.schemas import DNSRecordCreate, DNSRecordResponse, DNSRecordUpdate
from dns.service import create_dns_record, delete_dns_record, update_dns_record, get_dns_record

router = APIRouter()

@router.post("/", 
    response_model=DNSRecordResponse,
    summary="Create DNS Record",
    description="Creates a new DNS record with the specified Name and IP address"
)
async def create_dns(record: DNSRecordCreate):
    return await create_dns_record(record)

@router.delete("/{record_name}",
    response_model=DNSRecordResponse,
    summary="Delete DNS Record",
    description="Deletes an existing DNS record by its name"
)
async def delete_dns(record_name: str):
    return await delete_dns_record(record_name)

@router.put("/{record_name}", 
    response_model=DNSRecordResponse,
    summary="Update DNS Record",
    description="Updates the IP address of an existing DNS record"
)
async def update_dns(record_name: str, record: DNSRecordUpdate):
    return await update_dns_record(record_name, record)

@router.get("/{record_name}", 
    response_model=DNSRecordResponse,
    summary="Get DNS Record",
    description="Retrieves the details of a DNS record by its name"
)
async def get_dns(record_name: str):
    return await get_dns_record(record_name)
