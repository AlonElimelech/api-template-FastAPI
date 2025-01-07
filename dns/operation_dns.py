# Description: This file contains the functions to create and delete DNS records.

# The create_dns function creates a DNS record with the provided record name and IP address.
async def create_dns(record_name: str, ip: str) -> str:
    print("create")
    return "DNS record created successfully"

# The delete_dns function deletes a DNS record with the provided record name.
async def delete_dns(record_name: str) -> str:
    print("delete")
    return "DNS record deleted successfully"

async def update_dns(record_name: str, ip: str) -> str:
    """Update DNS record with new IP"""
    print(f"update dns record: {record_name} with ip: {ip}")
    return "DNS record updated successfully"

async def get_dns(record_name: str) -> str:
    """Get DNS record IP"""
    print(f"get dns record: {record_name}")
    return "192.168.1.1"  # Simulated IP address