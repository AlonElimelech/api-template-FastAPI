from dns.settings import API_PREFIX

def test_create_dns_record(client, valid_dns_record):
    response = client.post(API_PREFIX, json=valid_dns_record)
    assert response.status_code == 200
    data = response.json()
    assert data["record_name"] == valid_dns_record["record_name"]
    assert data["status"] == "in progress"
 
def test_create_invalid_record(client, invalid_dns_record):
    response = client.post(API_PREFIX, json=invalid_dns_record)
    assert response.status_code == 422
 
def test_delete_dns_record(client, valid_dns_record):
    # Create first
    client.post(API_PREFIX, json=valid_dns_record)
    # Then delete
    response = client.delete(f"{API_PREFIX}/{valid_dns_record['record_name']}")
    assert response.status_code == 200
    assert response.json()["status"] == "deleted"

def test_get_dns_record(client, valid_dns_record):
    # Create first
    client.post(API_PREFIX, json=valid_dns_record)
    # Then get
    response = client.get(f"{API_PREFIX}/{valid_dns_record['record_name']}")
    assert response.status_code == 200
    assert response.json()["record_name"] == valid_dns_record["record_name"] 