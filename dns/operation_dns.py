# Description: This file contains the functions to create and delete DNS records.
import time
# The create_dns function creates a DNS record with the provided record name and IP address.
async def create_dns(record_name: str, ip: str) -> str:
    print("create")
    return "DNS record created successfully"

# The delete_dns function deletes a DNS record with the provided record name.
async def delete_dns(record_name: str) -> str:
    print("delete")
    return "DNS record deleted successfully"