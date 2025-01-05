from common.awx_client import run_playbook
from common.logging import logger
from common.metrics import dns_create_counter, dns_delete_counter, increment_create_counter, increment_delete_counter

# Business logic for DNS operations
def create_dns_record(record):
    playbook_data = {
        "record_name": record.record_name,
        "ip_address": record.ip_address
    }
    logger.info(f"Creating DNS record: {record.record_name}")
    response = run_playbook("dns_create.yaml", playbook_data)
    increment_create_counter(record.record_name, record.ip_address)
    return {"record_name": record.record_name, "status": "created"}

def delete_dns_record(record_name):
    logger.info(f"Deleting DNS record: {record_name}")
    response = run_playbook("dns_delete.yaml", {"record_name": record_name})
    increment_delete_counter(record_name)
    return {"record_name": record_name, "status": "deleted"}