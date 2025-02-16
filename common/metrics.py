from prometheus_client import  Gauge
import time
from fastapi import Request, FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

# Uptime metric
uptime_metrics = Gauge("uptime_seconds", "Uptime in seconds")
start_time = time.time()

def setup_metrics(app: FastAPI):
    app.add_middleware(PrometheusMiddleware, app_name="dns")
    app.add_route("/metrics", custom_metrics)


def custom_metrics(request: Request):
    """Expose metrics with added uptime tracking."""
    uptime_metrics.set(time.time() - start_time)
    return handle_metrics(request)



