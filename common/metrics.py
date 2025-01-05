from prometheus_client import Counter, start_http_server

# Metrics for DNS service with labels
dns_create_counter = Counter(
    "dns_create_count",
    "Number of DNS records created",
    ['record_name', 'zone']  # Labels for DNS type and zone
)

dns_delete_counter = Counter(
    "dns_delete_count", 
    "Number of DNS records deleted",
    ['record_name', 'zone']  # Labels for DNS type and zone
)

def increment_create_counter(record_name: str, zone: str):
    """Increment create counter with specific labels"""
    dns_create_counter.labels(record_name=record_name, zone=zone).inc()

def increment_delete_counter(record_name: str, zone: str):
    """Increment delete counter with specific labels"""
    dns_delete_counter.labels(record_name=record_name, zone=zone).inc()

def setup_metrics():
    """Initialize and expose Prometheus metrics server"""
    start_http_server(8000)  # Expose metrics on port 8000