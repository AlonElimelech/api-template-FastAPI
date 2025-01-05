from common.logging import logger
from common.metrics import dns_create_counter, dns_delete_counter, increment_create_counter, increment_delete_counter
from dns.operation_dns import create_dns, delete_dns

# Business logic for DNS operations
def create_dns_record(record):
    logger.info(f"Creating DNS record: {record.record_name}")
    response = create_dns(record.record_name, record.ip_address)
    increment_create_counter(record.record_name, record.ip_address)
    return {"record_name": record.record_name, "status": "created"}

def delete_dns_record(record_name):
    logger.info(f"Deleting DNS record: {record_name}")
    response = delete_dns(record_name)
    increment_delete_counter(record_name)
    return {"record_name": record_name, "status": "deleted"}