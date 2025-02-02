""" from prometheus_client import REGISTRY

def test_create_metrics(client, valid_dns_record):
    initial_count = REGISTRY.get_sample_value('dns_create_count_total')
    client.post("/dns/", json=valid_dns_record)
    final_count = REGISTRY.get_sample_value('dns_create_count_total')
    assert final_count - initial_count == 1

def test_failure_metrics(client, invalid_dns_record):
    initial_count = REGISTRY.get_sample_value('dns_failure_count_total')
    client.post("/dns/", json=invalid_dns_record)
    final_count = REGISTRY.get_sample_value('dns_failure_count_total')
    assert final_count - initial_count == 1 """