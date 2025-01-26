from fastapi import HTTPException
from common.logging import logger
from common.metrics import dns_create_counter, dns_delete_counter, increment_create_counter, increment_delete_counter, increment_update_counter, increment_failure_counter
from dns.operation_dns import create_dns, delete_dns, update_dns, get_dns 
from dns.schemas import DNSRecordResponse, DNSRecordUpdate

# Business logic for DNS operations
async def create_dns_record(record) -> DNSRecordResponse:
    try:
        logger.info(f"Creating DNS record: {record.record_name}")
        # Here is the implementation for creating DNS record by Domain services Team
        response = await create_dns(record.record_name, record.ip)
        increment_create_counter(record.record_name, record.ip)
        return DNSRecordResponse(record_name=record.record_name, status_code=response.status_code, status= "in progress")
    except Exception as e:
        logger.error(f"Failed to create DNS record: {str(e)}")
        increment_failure_counter("create", record.record_name)
        raise HTTPException(status_code=404, detail=str(e))


async def delete_dns_record(record_name) -> DNSRecordResponse:
    try:
        logger.info(f"Deleting DNS record: {record_name}")
        response = await delete_dns(record_name)
        increment_delete_counter(record_name)
        return DNSRecordResponse(record_name=record_name, status= "deleted")
    except Exception as e:
        logger.error(f"Failed to delete DNS record: {str(e)}")
        increment_failure_counter("delete", record_name)
        raise HTTPException(status_code=404, detail=str(e))


async def update_dns_record(record_name: str, record: DNSRecordUpdate) -> DNSRecordResponse:
    try:
        logger.info(f"Updating DNS record: {record_name} with IP: {record.ip}")
        response = await update_dns(record_name, record.ip)
        increment_update_counter(record_name)
        return DNSRecordResponse(record_name=record_name, status= "updated")
    except Exception as e:
        logger.error(f"Failed to update DNS record: {str(e)}")
        increment_failure_counter("update", record_name)
        raise HTTPException(status_code=404, detail=str(e))

async def get_dns_record(record_name: str) -> DNSRecordResponse:
    try:
        logger.info(f"Getting DNS record: {record_name}")
        ip = await get_dns(record_name)
        return DNSRecordResponse(record_name=record_name, status= "fetched")
    except Exception as e:
        logger.error(f"Failed to get DNS record: {str(e)}")
        increment_failure_counter("get", record_name)
        raise HTTPException(status_code=404, detail=str(e))