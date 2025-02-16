from fastapi import APIRouter, HTTPException, BackgroundTasks
from dns.schemas import DNSRecordCreate, DNSRecordResponse, DNSRecordUpdate
from common.logging import logger
from dns.operation_dns import create_dns, delete_dns, update_dns, get_dns 
import time

router = APIRouter()

@router.post("/", 
    response_model=DNSRecordResponse,
    summary="Create DNS Record",
    description="Creates a new DNS record with the specified Name and IP address"
)
def create(record: DNSRecordCreate):
    try:
        logger.info(f"Creating DNS record: {record.record_name}")
        # Here is the implementation for creating DNS record by Domain services Team
        response = create_dns(record.record_name, record.ip)
        return DNSRecordResponse(record_name=record.record_name, status_code=response, status= "in progress")
    except Exception as e:
        logger.error(f"Failed to create DNS record: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{record_name}",
    response_model=DNSRecordResponse,
    summary="Delete DNS Record",
    description="Deletes an existing DNS record by its name"
)
def delete(record_name: str, background_tasks: BackgroundTasks):
    try:
        logger.info(f"Deleting DNS record: {record_name}")
        response = delete_dns(record_name)
        return DNSRecordResponse(record_name=record_name,status_code=response, status= "deleted")
    except Exception as e:
        logger.error(f"Failed to delete DNS record: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put("/{record_name}", 
    response_model=DNSRecordResponse,
    summary="Update DNS Record",
    description="Updates the IP address of an existing DNS record"
)
def update(record_name: str, record: DNSRecordUpdate):
    try:
        logger.info(f"Updating DNS record: {record_name} with IP: {record.ip}")
        response =  update_dns(record_name, record.ip)
        return DNSRecordResponse(record_name=record_name, status= "updated")
    except Exception as e:
        logger.error(f"Failed to update DNS record: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{record_name}", 
    response_model=DNSRecordResponse,
    summary="Get DNS Record",
    description="Retrieves the details of a DNS record by its name"
)
def get(record_name: str):
    try:
        logger.info(f"Getting DNS record: {record_name}")
        response = get_dns(record_name)
        return DNSRecordResponse(record_name=record_name, status_code=response ,status= "fetched")
    except Exception as e:
        logger.error(f"Failed to get DNS record: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))