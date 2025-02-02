# Description: This file contains the functions to create and delete DNS records.
import common.awx_client as awx_client
# The create_dns function creates a DNS record with the provided record name and IP address.
def create_dns(record_name: str, ip: str) -> int:
    print("create")
    #response = awx_client.launch_job()
    return 200

# The delete_dns function deletes a DNS record with the provided record name.
def delete_dns(record_name: str) -> str:
    print("delete")
    return 200

def update_dns(record_name: str, ip: str) -> str:
    """Update DNS record with new IP"""
    print(f"update dns record: {record_name} with ip: {ip}")
    return "DNS record updated successfully"

def get_dns(record_name: str) -> str:
    """Get DNS record IP"""
    print(f"get dns record: {record_name}")
    return 200  # Simulated IP address