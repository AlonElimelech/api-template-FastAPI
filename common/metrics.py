from prometheus_client import  Gauge
import time
from fastapi import Request, FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

# Uptime metric
uptime_metrics = Gauge("uptime_seconds", "Uptime in seconds", ["app_name"])
start_time = time.time()

def setup_metrics(app: FastAPI, resource_name: str):
    app.add_middleware(PrometheusMiddleware, app_name=resource_name)
    app.add_route("/metrics", custom_metrics(resource_name))

def custom_metrics(resource_name: str):
    def metrics_handler(request: Request):
        """Expose metrics with added uptime tracking."""
        uptime_metrics.labels(app_name=resource_name).set(time.time() - start_time)
        return handle_metrics(request)
    return metrics_handler



