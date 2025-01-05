from prometheus_client import Counter, start_http_server, make_asgi_app, Gauge
import time

# Metrics for DNS service with labels
dns_create_counter = Counter(
    "dns_create_count",
    "Number of DNS records created",
    ['record_name', 'zone']  # Labels for DNS type and zone
)

dns_delete_counter = Counter(
    "dns_delete_count", 
    "Number of DNS records deleted",
    ['record_name']  # Labels for DNS type and zone
)

# Uptime metric
uptime_gauge = Gauge("uptime_seconds", "Uptime in seconds")

def increment_create_counter(record_name: str, zone: str):
    """Increment create counter with specific labels"""
    dns_create_counter.labels(record_name=record_name, zone=zone).inc()

def increment_delete_counter(record_name: str):
    """Increment delete counter with specific labels"""
    dns_delete_counter.labels(record_name=record_name).inc()

start_time = time.time()

def setup_metrics(app):
    """Initialize and expose Prometheus metrics endpoint"""
    metrics_app = make_asgi_app()
    start_time = time.time()
        # Define a middleware to update the uptime gauge dynamically
    async def metrics_middleware(scope, receive, send):
        if scope["type"] == "http" and scope["root_path"] == "/metrics":
            # Update the uptime gauge before the metrics are served
            uptime_gauge.set(time.time() - start_time)
        # Pass the request to the Prometheus ASGI app
        await metrics_app(scope, receive, send)
    # Mount the metrics endpoint with the middleware
    app.mount("/metrics", metrics_middleware)

